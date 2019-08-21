# Databricks notebook source
# DBTITLE 1,201805 dataset parameters
# prerequisites: 
# 1: a (scopus) Hive table with affiliation/author/citation data 
# 2: for the subject classifications, 2 Hive tables:
#     a: ScienceMetrix 176 subfield classifications to Source-IDs 
#     b: ScienceMetrix 176 subfields, 22 fields and 6 domains hierarchy
Last_ani='ani_20180503' # snapshot
sort_pub_year='sort_year' # or 'pub_year'
minyear='1960'
mincityear='1996'
maxyear='2017'
cachePath='/mnt/dest/bucket/example/path/available/in/databricks/'
cacheDb='dbName'

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql import functions as func
from pyspark.sql import Window
from pyspark.sql import Row

# for printing labels on the result columns:
Y1=minyear[2:]
Y2=mincityear[2:]
Y3=maxyear[2:]

csvOutFileName_s1='Table-S1_'+Last_ani+'_'+minyear+'_'+mincityear+'_'+maxyear+'_'+sort_pub_year
csvOutFileName_s3='Table-S3_'+Last_ani+'_'+minyear+'_'+mincityear+'_'+maxyear+'_'+sort_pub_year

df_ani=table('scopus.'+Last_ani)
print ("running with: "+Last_ani)

sqlContext.sql('DROP TABLE IF EXISTS '+cacheDb+'.temp_df_agg_count')
sqlContext.sql('DROP TABLE IF EXISTS '+cacheDb+'.temp_df_agg_count_ln_wmaxc')
sqlContext.sql('DROP TABLE IF EXISTS '+cacheDb+'.temp_df_agg_count_ln_max')
sqlContext.sql('DROP TABLE IF EXISTS '+cacheDb+'.temp_df_ani_auth_affinst')
sqlContext.sql('DROP TABLE IF EXISTS '+cacheDb+'.temp_df_ani_auth_name')

# COMMAND ----------

# for each author in Scopus, get their latest record and select the name from that record.
# we will use this in the end to label each author record for which we create stats.
df_ani_auth_name_t=(
  df_ani
  .withColumn('Au',func.explode('Au'))
  .orderBy('datesort',Ascending=False)
  #.filter('Au.given_name_pn IS NOT NULL')
  # no need to filter if we order and prefer the presence of the given_name:
  .withColumn(
    'recRank',
    func.rank().over(
      Window
      .partitionBy('Au.auid')
      .orderBy(
        func.expr('IF(Au.given_name_pn IS NULL,0,1)').desc(),
        func.desc('datesort'),
        func.desc('Eid'),
        func.desc('Au.authorseq') # have issues with records with multiple auid repeats on same record. this breaks those ties.
      )
    )
  )
  .withColumn('lastPubYear',func.max(sort_pub_year).over(Window.partitionBy('Au.auid')))
  .withColumn('firstPubYear',func.min(sort_pub_year).over(Window.partitionBy('Au.auid')))
  .filter('recRank=1')
  .select(func.col('Au.auid').alias('auid'),func.col('Eid').alias('LastEidName'),func.expr('CONCAT(Au.surname_pn,", ",IFNULL(Au.given_name_pn,Au.initials_pn))').alias('authfull'),'lastPubYear','firstPubYear')
)

tbn_df_ani_auth_name="temp_df_ani_auth_name"
if tbn_df_ani_auth_name not in sqlContext.tableNames(cacheDb):
  print ("Generating "+cacheDb+"."+tbn_df_ani_auth_name)
  df_ani_auth_name_t.repartition(200).write.mode("overwrite").saveAsTable(cacheDb+"."+tbn_df_ani_auth_name)
else:
  print ("Reusing existing "+cacheDb+"."+tbn_df_ani_auth_name)
df_ani_auth_name=table(cacheDb+"."+tbn_df_ani_auth_name)

# COMMAND ----------

# citation counts (mincityear+)
df_mincityear_onw_cit=(
  df_ani
  .filter(sort_pub_year+' >= '+mincityear)
  .select(
    func.col('Eid').alias('CitingEid'),
    func.explode('citations').alias('Eid'),
    func.col('Au.auid').alias('CitingAuids')
  )
  .distinct()
  .join(
    df_ani.select(
      'Eid',
      func.col('Au.auid').alias('CitedAuids')
    ),["Eid"]
  )
  .withColumn('overLappingAuthors',func.size(func.array_intersect('CitingAuids','CitedAuids')))
  .select(
    "CitingEid",
    "Eid",
    func.expr("IF(overLappingAuthors>0,1,0)").alias('isSelfCitation'),
    func.expr("IF(overLappingAuthors>0,NULL,CitingEid)").alias('CitingEidNonSelf'),
  )
  .groupBy('Eid')
  .agg(
    func.count('*').alias('CitationCount'),
    func.sum('isSelfCitation').alias('SelfCitationCount'),
    (func.count('*')-func.sum('isSelfCitation')).alias('CitationCountNonSelf'),
    func.collect_list('CitingEid').alias('CitingEids'),
    func.collect_list('CitingEidNonSelf').alias('CitingEidsNonSelf'),
  )
)

# COMMAND ----------

# get science-metrix tables for subject classification; the map scopus source-ids (i.e. journals, serials etc) to S-M classes.
df_smc_m=table(cacheDb+".ScienceMetrixMapping_POC_Journal_Subject")
df_smc_c=table(cacheDb+".ScienceMetrixMapping_POC_SubjectStructure")

# window definitions used in next command to calculate the volume and rank of the (sub)fields per author to assign the best subject per author.
w_au=Window.partitionBy('auid')
w_au_sf=Window.partitionBy('auid','subfieldCode')
w_sf=Window.partitionBy('subfieldCode')
# this window won't have ties. That way the dense_rank can be used to de-duplicate the results 
# (i.e. all those ranked #1 will be the same item, no risk of two items being ranked #1)
# note also the first subfieldCode IS NULL: designed to put the count of null subfields to the END of the rank.
w_au_sort_sf_auth_overall=Window.partitionBy('auid').orderBy(
  func.expr('subfieldCode IS NULL').asc(),
  func.desc('subfieldCode_count_thisauth'),
  func.asc('subfieldCode_count_overall'),
  func.asc('subfieldCode')
)
w_au_f=Window.partitionBy('auid','fieldCode')
w_f=Window.partitionBy('fieldCode')
# see comment about ties above.
w_au_sort_f_auth_overall=Window.partitionBy('auid').orderBy(
  func.expr('fieldCode IS NULL').asc(),
  func.desc('fieldCode_count_thisauth'),
  func.asc('fieldCode_count_overall'),
  func.asc('fieldCode')
)

# COMMAND ----------

# calculate the metric per author in Scopus.
# Note: ns_ and ws_ prefixes as found in the code, indicate NonSelf and WithSelf citation counts used.

# list of metrics:

# npY1Y3	# papers minyear-maxyear
# firstyr	year of first publication
# lastyr	year of most recent publication
# ncY2Y3	total cites mincityear-maxyear
# ncY2Y3_cp number of citing papers (unique) citing ncY2Y3
# hY3	h-index as of end-maxyear
# hmY3	hm-index as of end-maxyear
# nps	number of single authored papers
# ncs	total cites to single authored papers
# npsf	number of single+first authored papers
# ncsf	total cites to single+first authored papers
# npsfl	number of single+first+last authored papers
# ncsfl	total cites to single+first+last authored papers

wns = (Window.partitionBy('auid').orderBy(func.desc('CitationCountNonSelf'),'Eid'))
wws = (Window.partitionBy('auid').orderBy(func.desc('CitationCount'),'Eid'))
wsm = (Window.partitionBy('auid','subfieldCode'))
wsm_a = (Window.partitionBy('subfieldCode'))
df_agg_count_t=(
  df_ani
  #.filter('citation_type IN ("ar","cp","re")')
  .filter(sort_pub_year+' <= '+maxyear)
  .join(df_mincityear_onw_cit,["Eid"],"LEFT_OUTER").na.fill({'CitationCountNonSelf':0,'CitationCount':0})
  .select('Eid',sort_pub_year,func.size('Au').alias('n_authors'),func.explode('Au').alias('Au'),'CitationCountNonSelf','CitationCount','CitingEidsNonSelf','CitingEids',func.col('source.srcid').alias('srcid'),'citation_type')
  .withColumn('auid',func.col('Au.auid')).withColumn('Authorseq',func.col('Au.Authorseq')).drop('Au')
  
  # join ScienceMetrix to count volume per subfield code
  .join(df_smc_m,["srcid"],"LEFT_OUTER")
  .withColumn('subfieldcode',func.expr('IF(citation_type IN ("ar","cp","re"),subfieldcode,NULL)')) # assign field only if ar/cp/re
  .join(df_smc_c,["subfieldCode"],"LEFT_OUTER")
  .withColumn('totalDocCountAuthor',func.count('*').over(w_au))
  .withColumn('arcpreDocCountAuthor',func.count(func.expr('IF(citation_type IN ("ar","cp","re"),Eid,NULL)')).over(w_au))
  .filter('arcpreDocCountAuthor>=5') # only authors with >= 5 ar/cp/re's 
  .withColumn('SMFCMdocCountAuthor',func.count('fieldCode').over(w_au)) # number of documents the author has mapped to a S-M; 
  # calculate ranks for 176-level subfield per author
  .withColumn('subfieldCode_count_thisauth',func.count('*').over(w_au_sf))
  .withColumn('subfieldCode_count_overall',func.count('*').over(w_sf))
  .withColumn('subfieldRank',func.dense_rank().over(w_au_sort_sf_auth_overall))
  .withColumn(
    "subfield_tuple",
    func.struct(
      'subfieldRank',
      'subfieldCode',
      'subfieldName',
      'subfieldCode_count_thisauth',
      'subfieldCode_count_overall',
      'SMFCMdocCountAuthor',
      func.expr('subfieldCode_count_thisauth/SMFCMdocCountAuthor').alias('subfieldFrac')
    )
  )
  # same for 22-level fields
  .withColumn('fieldCode_count_thisauth',func.count('*').over(w_au_f))
  .withColumn('fieldCode_count_overall',func.count('*').over(w_f))
  .withColumn('fieldRank',func.dense_rank().over(w_au_sort_f_auth_overall))
  .withColumn(
    "field_tuple",
    func.struct(
      'fieldRank',
      'fieldCode',
      'fieldName',
      'fieldCode_count_thisauth',
      'fieldCode_count_overall',
      'SMFCMdocCountAuthor',
      func.expr('fieldCode_count_thisauth/SMFCMdocCountAuthor').alias('fieldFrac')
    )
  )
  
  # ranks and sums needed to calculate h and hm index
  .withColumn('ns_r_eff',func.sum(1/func.col('n_authors')).over(wns.rangeBetween(Window.unboundedPreceding, 0)))
  .withColumn('ns_r',func.rank().over(wns))
  .withColumn('ws_r_eff',func.sum(1/func.col('n_authors')).over(wws.rangeBetween(Window.unboundedPreceding, 0)))
  .withColumn('ws_r',func.rank().over(wws))
  
  .groupBy('auid')
  .agg(
    func.sort_array(func.collect_set("subfield_tuple"),True).alias("subFields"),
    func.sort_array(func.collect_set("field_tuple"),True).alias("Fields"),
    func.sum(func.expr('IF('+sort_pub_year+' BETWEEN '+minyear+' AND '+maxyear+',1,0)')).alias('npY1Y3'),
    # no longer capture first/last here; we want to get those values from the full database and therefore collect them with the author names dataframe (where we also get the last known full prefereed name)
    #func.min(sort_pub_year).alias('firstyr'),
    #func.max(sort_pub_year).alias('lastyr'),
    
    func.sum('CitationCountNonSelf').alias('ns_ncY2Y3'),
    func.size(func.array_distinct(func.flatten(func.collect_list('CitingEidsNonSelf')))).alias('ns_ncY2Y3_cp'),
    func.max(func.expr('IF(ns_r<=CitationCountNonSelf,ns_r,0)')).alias('ns_hY3'),
    func.max(func.expr('IF(ns_r_eff<=CitationCountNonSelf,ns_r_eff,0)')).alias('ns_hmY3'),
    func.sum(func.expr('IF(n_authors=1,1,0)')).alias('ns_nps'),
    func.sum(func.expr('IF(n_authors=1,CitationCountNonSelf,0)')).alias('ns_ncs'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1,1,0)')).alias('ns_npsf'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1,CitationCountNonSelf,0)')).alias('ns_ncsf'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1 OR Authorseq=n_authors,1,0)')).alias('ns_npsfl'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1 OR Authorseq=n_authors,CitationCountNonSelf,0)')).alias('ns_ncsfl'),

    func.sum('CitationCount').alias('ws_ncY2Y3'),
    func.size(func.array_distinct(func.flatten(func.collect_list('CitingEids')))).alias('ws_ncY2Y3_cp'),
    func.max(func.expr('IF(ws_r<=CitationCount,ws_r,0)')).alias('ws_hY3'),
    func.max(func.expr('IF(ws_r_eff<=CitationCount,ws_r_eff,0)')).alias('ws_hmY3'),
    func.sum(func.expr('IF(n_authors=1,1,0)')).alias('ws_nps'),
    func.sum(func.expr('IF(n_authors=1,CitationCount,0)')).alias('ws_ncs'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1,1,0)')).alias('ws_npsf'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1,CitationCount,0)')).alias('ws_ncsf'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1 OR Authorseq=n_authors,1,0)')).alias('ws_npsfl'),
    func.sum(func.expr('IF(n_authors=1 OR Authorseq=1 OR Authorseq=n_authors,CitationCount,0)')).alias('ws_ncsfl'),

  )
)
# store this as a table if it doesn't already exist.
tbn_df_agg_count="temp_df_agg_count"
if tbn_df_agg_count not in sqlContext.tableNames(cacheDb):
  print ("Generating "+cacheDb+"."+tbn_df_agg_count)
  df_agg_count_t.repartition(200).write.mode("overwrite").saveAsTable(cacheDb+"."+tbn_df_agg_count)
else:
  print ("Reusing existing "+cacheDb+"."+tbn_df_agg_count)
df_agg_count=table(cacheDb+"."+tbn_df_agg_count)

# more metrics: log scales of the calculated metrics.
# lnc	ln(ncY2Y3+1)
# lh	ln(hY3+1)
# lhm	ln(hmY3+1)
# lns	ln(ncs+1)
# lnsf	ln(ncsf+1)
# lnsfl	ln(ncsfl+1)
df_agg_count_ln=(
  df_agg_count
  .withColumn('ns_lnc',func.log(func.expr('ns_ncY2Y3+1')))
  .withColumn('ns_lh',func.log(func.expr('ns_hY3+1')))
  .withColumn('ns_lhm',func.log(func.expr('ns_hmY3+1')))
  .withColumn('ns_lns',func.log(func.expr('ns_ncs+1')))
  .withColumn('ns_lnsf',func.log(func.expr('ns_ncsf+1')))
  .withColumn('ns_lnsfl',func.log(func.expr('ns_ncsfl+1')))

  .withColumn('ws_lnc',func.log(func.expr('ws_ncY2Y3+1')))
  .withColumn('ws_lh',func.log(func.expr('ws_hY3+1')))
  .withColumn('ws_lhm',func.log(func.expr('ws_hmY3+1')))
  .withColumn('ws_lns',func.log(func.expr('ws_ncs+1')))
  .withColumn('ws_lnsf',func.log(func.expr('ws_ncsf+1')))
  .withColumn('ws_lnsfl',func.log(func.expr('ws_ncsfl+1')))
)  

# and to complement further, the MAX of the log functions above (aggregate across the DB)
# flnc	lnc/max(lnc)
# flh	lh/max(lh)
# flhm	lhm/max(lhm)
# flns	lns/max(lns)
# flnsf	lnsf/max(lnsf)
# flnsfl	lnsfl/max(lnsfl)
# c	composite: sum of six fractions (flnc+flh+flhm+flns+flnsf+flnsfl)
df_agg_count_ln_max_t=df_agg_count_ln.agg(
  func.max('ns_lnc').alias('ns_maxlnc'),
  func.max('ns_lh').alias('ns_maxlh'),
  func.max('ns_lhm').alias('ns_maxlhm'),
  func.max('ns_lns').alias('ns_maxlns'),
  func.max('ns_lnsf').alias('ns_maxlnsf'),
  func.max('ns_lnsfl').alias('ns_maxlnsfl'),
  
  func.max('ws_lnc').alias('ws_maxlnc'),
  func.max('ws_lh').alias('ws_maxlh'),
  func.max('ws_lhm').alias('ws_maxlhm'),
  func.max('ws_lns').alias('ws_maxlns'),
  func.max('ws_lnsf').alias('ws_maxlnsf'),
  func.max('ws_lnsfl').alias('ws_maxlnsfl')  
)
tbn_df_agg_count_ln_max="temp_df_agg_count_ln_max"
if tbn_df_agg_count_ln_max not in sqlContext.tableNames(cacheDb):
  print ("Generating "+cacheDb+"."+tbn_df_agg_count_ln_max)
  df_agg_count_ln_max_t.repartition(200).write.mode("overwrite").saveAsTable(cacheDb+"."+tbn_df_agg_count_ln_max)
else:
  print ("Reusing existing "+cacheDb+"."+tbn_df_agg_count_ln_max)
df_agg_count_ln_max=table(cacheDb+"."+tbn_df_agg_count_ln_max)

# now bring the aggregate back into the metrics table so we can calculate the normalized score.
df_agg_count_ln_wmaxc_t=(
  df_agg_count_ln
  .crossJoin(df_agg_count_ln_max)
  #.withColumn('flnc',func.expr('lnc/(max(lnc) over(Partition By true))'))
  .withColumn('ns_flnc',func.expr('ns_lnc/ns_maxlnc')).drop('ns_maxlnc')
  .withColumn('ns_flh',func.expr('ns_lh/ns_maxlh')).drop('ns_maxlh')
  .withColumn('ns_flhm',func.expr('ns_lhm/ns_maxlhm')).drop('ns_maxlhm')
  .withColumn('ns_flns',func.expr('ns_lns/ns_maxlns')).drop('ns_maxlns')
  .withColumn('ns_flnsf',func.expr('ns_lnsf/ns_maxlnsf')).drop('ns_maxlnsf')
  .withColumn('ns_flnsfl',func.expr('ns_lnsfl/ns_maxlnsfl')).drop('ns_maxlnsfl')
  # c = the composite metric
  .withColumn('ns_c',func.expr('ns_flnc+ns_flh+ns_flhm+ns_flns+ns_flnsf+ns_flnsfl'))

  .withColumn('ws_flnc',func.expr('ws_lnc/ws_maxlnc')).drop('ws_maxlnc')
  .withColumn('ws_flh',func.expr('ws_lh/ws_maxlh')).drop('ws_maxlh')
  .withColumn('ws_flhm',func.expr('ws_lhm/ws_maxlhm')).drop('ws_maxlhm')
  .withColumn('ws_flns',func.expr('ws_lns/ws_maxlns')).drop('ws_maxlns')
  .withColumn('ws_flnsf',func.expr('ws_lnsf/ws_maxlnsf')).drop('ws_maxlnsf')
  .withColumn('ws_flnsfl',func.expr('ws_lnsfl/ws_maxlnsfl')).drop('ws_maxlnsfl')
  .withColumn('ws_c',func.expr('ws_flnc+ws_flh+ws_flhm+ws_flns+ws_flnsf+ws_flnsfl'))
)

tbn_df_agg_count_ln_wmaxc="temp_df_agg_count_ln_wmaxc"
if tbn_df_agg_count_ln_wmaxc not in sqlContext.tableNames(cacheDb):
  print ("Generating "+cacheDb+"."+tbn_df_agg_count_ln_wmaxc)
  df_agg_count_ln_wmaxc_t.repartition(200).write.mode("overwrite").saveAsTable(cacheDb+"."+tbn_df_agg_count_ln_wmaxc)
else:
  print ("Reusing existing "+cacheDb+"."+tbn_df_agg_count_ln_wmaxc)
df_agg_count_ln_wmaxc=table(cacheDb+"."+tbn_df_agg_count_ln_wmaxc)


# COMMAND ----------

# in order to label the institution of each author:

# SciVal institution mappings
Last_ia=max([x for x in sqlContext.tableNames(cacheDb) if len(x)==32 and x[0:26]=="institution_affiliation_20"])
df_ia=table(''+cacheDb+'.'+Last_ia)

Last_i=max([x for x in sqlContext.tableNames(cacheDb) if len(x)==20 and x[0:14]=="institution_20"])
df_i=table(''+cacheDb+'.'+Last_i)

# for each author in Scopus, get their latest record and select the affiliation[s] from that record.

# inst_id	most recent institution ID
# inst_name	institution name
# cntry	country associated with most recent institution
# affil_id	most recent Scopus affiliation ID

# to get only one instid per afid:
df_afid_inst_unique=(
  df_ia
  .selectExpr('institution_id','afid')
  .withColumn('instrank',func.rank().over(Window.partitionBy('afid').orderBy(func.asc('institution_id'))))
  .filter('instrank=1').drop('instrank')
  .join(df_i.selectExpr('institution_id','name as sv_name','country_code as sv_country_code'),["institution_id"],"LEFT_OUTER")
)

df_ani_auth_affinst_t=(
  df_ani
  .withColumn('Au',func.explode('Au'))
  .withColumn("Au_af", func.explode("Au_af"))
  .filter('Au.Authorseq=Au_af.Authorseq') # only keep the au-af rows matching this author
  .selectExpr('*','Af[Au_af.affiliation_seq-1] as affiliation') # only keep the af rows matching this au-af.
  .drop('Af')
  .withColumn('afid',func.explode('affiliation.affiliation_ids'))
  .filter('affiliation IS NOT NULL') # so that we can filter to only the last publication. if it includes nulls we may select "null" as institution, not desirable.
  # 
  .withColumn('recRank',func.rank().over(Window.partitionBy('Au.auid').orderBy(
    func.desc('datesort'), # last record(s)
    # tie breakers:
    func.desc('Eid'), # so we only have one record
    func.asc('afid'), # so we only look at one AFID
    func.asc('Au_af.affiliation_seq'), # in case the same afid occurs multiple times only get one
    func.asc('Au_af.Authorseq'), # in case the same author ID occurs multiple times using a different sequence.
  ))) 
  .filter('recRank=1') # to get the last only.
  .select(func.col('Au.auid').alias('auid'),func.col('Eid').alias('LastEidAff'),'afid','affiliation')
  .join(df_afid_inst_unique,['afid'],'LEFT_OUTER')
  .select(
    'auid',
    'LastEidAff',
    func.col('institution_id').alias('inst_id'),
    func.coalesce('sv_name',func.concat_ws(', ','affiliation.affiliation_organization')).alias('inst_name'),
    func.coalesce('sv_country_code','affiliation.affiliation_tag_country').alias('cntry'),
    func.col('afid').alias('affil_id')
  )
  .distinct() # remove any duplicates left. This may occur in odd cases where the Au_af field is repeated.
# eid 84959828211
#  array
#0: {"Authorseq":1,"affiliation_seq":1,"validity_B":true}
#1: {"Authorseq":1,"affiliation_seq":1,"validity_B":true}

)

tbn_df_ani_auth_affinst="temp_df_ani_auth_affinst"
if tbn_df_ani_auth_affinst not in sqlContext.tableNames(cacheDb):
  print ("Generating "+cacheDb+"."+tbn_df_ani_auth_affinst)
  df_ani_auth_affinst_t.repartition(200).write.mode("overwrite").saveAsTable(cacheDb+"."+tbn_df_ani_auth_affinst)
else:
  print ("Reusing existing "+cacheDb+"."+tbn_df_ani_auth_affinst)
df_ani_auth_affinst=table(cacheDb+"."+tbn_df_ani_auth_affinst)


# COMMAND ----------

display(
  df_ani_auth_affinst
  .withColumn('reccount',func.count('*').over(Window.partitionBy('auid')))
  .filter('reccount>1')
)
# should be empty response.

# COMMAND ----------

# complete to dataset: tie all together and calculate the rank of each author so that we can pull the top 100K.

# ord    order sorted on c
# author_id Scopus AUID
# authfull  author name
ns_wc = (Window.partitionBy(func.lit(True)).orderBy(func.desc('ns_c')))
ws_wc = (Window.partitionBy(func.lit(True)).orderBy(func.desc('ws_c')))
df_agg_result=(
  df_agg_count_ln_wmaxc
  .filter('auid IS NOT NULL')
  .filter("npY1Y3 >= 2") # only rank authors >= 2 papers since 1960
  .join(df_ani_auth_name,["auid"],"LEFT_OUTER")
  .join(df_ani_auth_affinst,["auid"],"LEFT_OUTER")
  .withColumnRenamed('auid','author_id')
  .withColumn('ns_ord',func.rank().over(ns_wc))
  .withColumn('ws_ord',func.rank().over(ws_wc))
  .select(
    
    
    "author_id",
    "authfull",
    #"inst_id",
    "inst_name",
    "cntry",
    #"affil_id",
    func.col("npY1Y3").alias('np'+Y1+Y3),
    #"firstyr",
    #"lastyr",
    func.col('firstPubYear').alias('firstyr'),
    func.col('lastPubYear').alias('lastyr'),
    
    func.col("ns_ord").alias('rank (ns)'),
    func.col("ns_ncY2Y3").alias('nc'+Y2+Y3+' (ns)'),
    # not showing citing papers
    #func.col("ns_ncY2Y3_cp").alias(''),
    #func.expr("ns_ncY2Y3/ns_ncY2Y3_cp").alias('ns_ncY2Y3_cp_ratio'),
    func.col("ns_hY3").alias('h'+Y3+' (ns)'),
    func.col("ns_hmY3").alias('hm'+Y3+' (ns)'),
    func.col("ns_nps").alias('nps (ns)'),
    func.col("ns_ncs").alias('ncs (ns)'),
    func.col("ns_npsf").alias('cpsf (ns)'),
    func.col("ns_ncsf").alias('ncsf (ns)'),
    func.col("ns_npsfl").alias('npsfl (ns)'),
    func.col("ns_ncsfl").alias('ncsfl (ns)'),
# no need to store these; the log, and normalized-log are just there to get to c.
#    "ns_lnc",
#    "ns_lh",
#    "ns_lhm",
#    "ns_lns",
#    "ns_lnsf",
#    "ns_lnsfl",
#    "ns_flnc",
#    "ns_flh",
#    "ns_flhm",
#    "ns_flns",
#    "ns_flnsf",
#    "ns_flnsfl",
    func.col("ns_c").alias('c (ns)'),
    func.col("ns_ncY2Y3_cp").alias('npciting (ns)'),
    func.expr("ns_ncY2Y3/ns_ncY2Y3_cp").alias('cprat (ns)'),    
    func.expr("CONCAT(100*(ws_ncY2Y3-ns_ncY2Y3)/ws_ncY2Y3,' %')").alias('self%'),
    
    func.col("ws_ord").alias('rank'),
    func.col("ws_ncY2Y3").alias('nc'+Y2+Y3),
    func.col("ws_hY3").alias('h'+Y3),
    func.col("ws_hmY3").alias('hm'+Y3),
    func.col("ws_nps").alias('nps'),
    func.col("ws_ncs").alias('ncs'),
    func.col("ws_npsf").alias('cpsf'),
    func.col("ws_ncsf").alias('ncsf'),
    func.col("ws_npsfl").alias('npsfl'),
    func.col("ws_ncsfl").alias('ncsfl'),    
# no need to store these; the log, and normalized-log are just there to get to c.    
#    "ws_lnc",
#    "ws_lh",
#    "ws_lhm",
#    "ws_lns",
#    "ws_lnsf",
#    "ws_lnsfl",
#    "ws_flnc",
#    "ws_flh",
#    "ws_flhm",
#    "ws_flns",
#    "ws_flnsf",
#    "ws_flnsfl",
    func.col("ws_c").alias('c'),
    func.col("ws_ncY2Y3_cp").alias('npciting'),
    func.expr("ws_ncY2Y3/ws_ncY2Y3_cp").alias('cprat'),
    
    func.expr('IF(subfields[0] IS NULL,NULL,IF(subfields[0].SMFCMdocCountAuthor<5,NULL,subfields[0].subfieldCode))').alias('sm-1'),
    func.expr('IF(subfields[0] IS NULL,NULL,IF(subfields[0].SMFCMdocCountAuthor<5,NULL,subfields[0].subfieldName))').alias('name1'),
    func.expr('IF(subfields[0] IS NULL,NULL,IF(subfields[0].SMFCMdocCountAuthor<5,NULL,subfields[0].subfieldFrac))').alias('frac1'),
    func.expr('IF(subfields[1] IS NULL,NULL,IF(subfields[1].SMFCMdocCountAuthor<5,NULL,subfields[1].subfieldCode))').alias('sm-2'),
    func.expr('IF(subfields[1] IS NULL,NULL,IF(subfields[1].SMFCMdocCountAuthor<5,NULL,subfields[1].subfieldName))').alias('name2'),
    func.expr('IF(subfields[1] IS NULL,NULL,IF(subfields[1].SMFCMdocCountAuthor<5,NULL,subfields[1].subfieldFrac))').alias('frac2'),
    func.expr('IF(fields[0] IS NULL,NULL,IF(fields[0].SMFCMdocCountAuthor<5,NULL,fields[0].fieldCode))').alias('sm22'),
    func.expr('IF(fields[0] IS NULL,NULL,IF(fields[0].SMFCMdocCountAuthor<5,NULL,fields[0].fieldName))').alias('name22'),
    func.expr('IF(fields[0] IS NULL,NULL,IF(fields[0].SMFCMdocCountAuthor<5,NULL,fields[0].fieldFrac))').alias('frac22'),   
    
  )
)

df_agg_result.repartition(200).write.mode("overwrite").csv('dbfs:'+cachePath+csvOutFileName_s1+'.csv',header = 'true')

# COMMAND ----------

df_agg_result_csv=(
  spark
  .read
  .format("csv")
  .option("header", True)
  .load(cachPathFull+csvOutFileName_s1+'.csv')
  .withColumn('rank',func.col('rank').cast('int'))
  .withColumn('rank (ns)',func.col('rank (ns)').cast('int'))
  .orderBy(func.col('rank (ns)'))
)

# COMMAND ----------

print(Last_ani+" has "+str(df_agg_result_csv.count())+" authors")
print(Last_ani+" has "+str(df_agg_result_csv.filter('sm22 IS NOT NULL').count())+" authors with field assigned")# 

# COMMAND ----------

# table S3 by SM 22
# SM22	SM22-Cat-Name	#Auth	Cites-25	Cites-50	Cites-75	Cites-90	Cites-95	Cites-99	c-25	c-50	c-75	c-90	c-95	c-99
df_S3_22=(
  df_agg_result_csv
  .withColumn('nc'+Y2+Y3,func.col('nc'+Y2+Y3).cast('long'))
  .withColumn('rec_count',func.count('*').over(Window.partitionBy('sm22')))
  .withColumn('nc'+Y2+Y3+'_perc',func.rank().over(Window.partitionBy('sm22').orderBy(func.col('nc'+Y2+Y3).asc()))/func.col('rec_count'))
  .withColumn('c_perc',func.rank().over(Window.partitionBy('sm22').orderBy(func.asc('c')))/func.col('rec_count'))
  .groupBy(
    func.col('sm22').alias('SM22'),func.col('name22').alias('SM22-Cat-Name')
  )
  .agg(
    func.first('rec_count').alias('#Auth'),
    func.count(func.expr('IF(`rank (ns)`<=100000,TRUE,NULL)')).alias('#Auth top 100k (ns)'),
    func.count(func.expr('IF(`rank`<=100000,TRUE,NULL)')).alias('#Auth top 100k'),
    func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.25,nc'+Y2+Y3+',NULL)')).alias('Cites-25'),
    func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.50,nc'+Y2+Y3+',NULL)')).alias('Cites-50'),
    func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.75,nc'+Y2+Y3+',NULL)')).alias('Cites-75'),
    func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.90,nc'+Y2+Y3+',NULL)')).alias('Cites-90'),
    func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.95,nc'+Y2+Y3+',NULL)')).alias('Cites-95'),
    func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.99,nc'+Y2+Y3+',NULL)')).alias('Cites-99'),
    func.min(func.expr('IF(c_perc>=.25,c,NULL)')).alias('c-25'),
    func.min(func.expr('IF(c_perc>=.50,c,NULL)')).alias('c-50'),
    func.min(func.expr('IF(c_perc>=.75,c,NULL)')).alias('c-75'),
    func.min(func.expr('IF(c_perc>=.90,c,NULL)')).alias('c-90'),
    func.min(func.expr('IF(c_perc>=.95,c,NULL)')).alias('c-95'),
    func.min(func.expr('IF(c_perc>=.99,c,NULL)')).alias('c-99'),  
  )
  .union(
    df_agg_result_csv
    .withColumn('nc'+Y2+Y3,func.col('nc'+Y2+Y3).cast('long'))
    .withColumn('rec_count',func.count('*').over(Window.partitionBy(func.lit(True))))
    .withColumn('nc'+Y2+Y3+'_perc',func.rank().over(Window.partitionBy(func.lit(True)).orderBy(func.col('nc'+Y2+Y3).asc()))/func.col('rec_count'))
    .withColumn('c_perc',func.rank().over(Window.partitionBy(func.lit(True)).orderBy(func.asc('c')))/func.col('rec_count'))
    .agg(
      func.first(func.lit("")).alias('SM22'),
      func.first(func.lit("TOTAL")).alias('SM22-Cat-Name'),
      func.first('rec_count').alias('#Auth'),
      func.count(func.expr('IF(`rank (ns)`<=100000,TRUE,NULL)')).alias('#Auth top 100k (ns)'),
      func.count(func.expr('IF(`rank`<=100000,TRUE,NULL)')).alias('#Auth top 100k'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.25,nc'+Y2+Y3+',NULL)')).alias('Cites-25'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.50,nc'+Y2+Y3+',NULL)')).alias('Cites-50'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.75,nc'+Y2+Y3+',NULL)')).alias('Cites-75'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.90,nc'+Y2+Y3+',NULL)')).alias('Cites-90'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.95,nc'+Y2+Y3+',NULL)')).alias('Cites-95'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.99,nc'+Y2+Y3+',NULL)')).alias('Cites-99'),
      func.min(func.expr('IF(c_perc>=.25,c,NULL)')).alias('c-25'),
      func.min(func.expr('IF(c_perc>=.50,c,NULL)')).alias('c-50'),
      func.min(func.expr('IF(c_perc>=.75,c,NULL)')).alias('c-75'),
      func.min(func.expr('IF(c_perc>=.90,c,NULL)')).alias('c-90'),
      func.min(func.expr('IF(c_perc>=.95,c,NULL)')).alias('c-95'),
      func.min(func.expr('IF(c_perc>=.99,c,NULL)')).alias('c-99'),  
    )
  )
).repartition(1).write.mode("overwrite").csv('dbfs:'+cachePath+csvOutFileName_s3+'_SM22.csv',header = 'true', quote='"', escape='"')




# COMMAND ----------

# table s3 by SM 176
df_S3_176=(
  df_smc_c.select(func.col('fieldcode').alias('SM22'),func.col('subfieldcode').alias('SM176'))
  .join(
    df_agg_result_csv
    .withColumn('nc'+Y2+Y3,func.col('nc'+Y2+Y3).cast('long'))
    .withColumn('rec_count',func.count('*').over(Window.partitionBy('sm-1')))
    .withColumn('nc'+Y2+Y3+'_perc',func.rank().over(Window.partitionBy('sm-1').orderBy(func.col('nc'+Y2+Y3).asc()))/func.col('rec_count'))
    .withColumn('c_perc',func.rank().over(Window.partitionBy('sm-1').orderBy(func.asc('c')))/func.col('rec_count'))
    .groupBy(
      func.col('sm-1').alias('SM176'),func.col('name1').alias('SM176-Cat-Name')
    )
    .agg(
      func.first('rec_count').alias('#Auth'),
      func.count(func.expr('IF(`rank (ns)`<=100000,TRUE,NULL)')).alias('#Auth top 100k (ns)'),
      func.count(func.expr('IF(`rank`<=100000,TRUE,NULL)')).alias('#Auth top 100k'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.25,nc'+Y2+Y3+',NULL)')).alias('Cites-25'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.50,nc'+Y2+Y3+',NULL)')).alias('Cites-50'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.75,nc'+Y2+Y3+',NULL)')).alias('Cites-75'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.90,nc'+Y2+Y3+',NULL)')).alias('Cites-90'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.95,nc'+Y2+Y3+',NULL)')).alias('Cites-95'),
      func.min(func.expr('IF(nc'+Y2+Y3+'_perc>=.99,nc'+Y2+Y3+',NULL)')).alias('Cites-99'),
      func.min(func.expr('IF(c_perc>=.25,c,NULL)')).alias('c-25'),
      func.min(func.expr('IF(c_perc>=.50,c,NULL)')).alias('c-50'),
      func.min(func.expr('IF(c_perc>=.75,c,NULL)')).alias('c-75'),
      func.min(func.expr('IF(c_perc>=.90,c,NULL)')).alias('c-90'),
      func.min(func.expr('IF(c_perc>=.95,c,NULL)')).alias('c-95'),
      func.min(func.expr('IF(c_perc>=.99,c,NULL)')).alias('c-99'),    
    ),['SM176']
  )
).repartition(1).write.mode("overwrite").csv('dbfs:'+cachePath+csvOutFileName_s3+'_SM176.csv',header = 'true', quote='"', escape='"')


# COMMAND ----------

(
  df_agg_result_csv
  .filter('rank <= 100000 OR `rank (ns)` <= 100000')
  .repartition(1)
  .write
  .mode("overwrite")
  .csv(cachePath+csvOutFileName_s1+'_100K.csv',header = 'true', quote='"', escape='"')
)
