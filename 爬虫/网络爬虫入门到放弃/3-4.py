# 2019/11/13
import requests
from bs4 import BeautifulSoup
# 目的是获取豆瓣电影top250的所有电影名称，网页地址为https://movie.douban.com/top250

# 请求头
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Host' : 'movie.douban.com'
}

# 第一页为https://movie.douban.com/top250?start=0&filter=
# 第二页https://movie.douban.com/top250?start=25&filter=
# 使用for循环进行翻页

def get_movies(headers, k=10):
    movie_list = []
    for i in range(k): # top250
        link = f'https://movie.douban.com/top250?start={i*25}&filter='
        r = requests.get(link,headers=headers,timeout=10)

        #print(f'{i+1} 页面响应码 : {r.status_code}')
        #print(r.text)

        soup = BeautifulSoup(r.text,'lxml')
        div_list = soup.find_all('div',class_='hd')

        for each in div_list:
            # .a   .span 都是html中存在的标签
            tag = each.a
            #print(tag)
            #>>> <a class="" href="https://movie.douban.com/subject/1292052/">
            #>>> <span class="title">肖申克的救赎</span>
            #>>> <span class="title"> / The Shawshank Redemption</span>
            #>>> <span class="other"> / 月黑高飞(港)  /  刺激1995(台)</span>
            #>>> </a>
            
            tag = tag.span
            #print(tag)
            #>>> <span class="title">肖申克的救赎</span>

            movie_list.append(tag.string)  #标签内非属性字符串

    return movie_list

#movies = get_movies(headers,k=2)
#print(movies)

'''
[遍历](https://www.jianshu.com/p/fdee8d2be876)
1、contents 属性：返回所有子节点的列表，包括 NavigableString 类型节点。如果节点当中有换行符，会被当做是 NavigableString 类型节点而作为一个子节点。NavigableString 类型节点没有 contents 属性，因为没有子节点。

soup = BeautifulSoup("""<div> <span>test</span> </div> """) 
element = soup.div.contents 
print(element) 
# ['\n', <span>test</span>, '\n']
2、children 属性：children 属性跟 contents 属性基本一样，只不过返回的不是子节点列表，而是子节点的可迭代对象。

3、descendants 属性：descendants 属性返回 tag 的所有子孙节点。

4、string 属性：如果一个 tag 仅有一个子节点，那么这个 tag 也可以使用 .string 方法，输出结果与当前唯一子节点的 .string 结果相同。
'''

def get_movies_score(headers):
    score_list = []
    for i in range(3): # top250
        link = f'https://movie.douban.com/top250?start={i*25}&filter='
        r = requests.get(link,headers=headers,timeout=10)

        soup = BeautifulSoup(r.text,'lxml')
        div_list = soup.findAll('div',class_='star')

        for each in div_list:
            tag = each.span
            tag = tag.next_sibling.next_sibling     # 多个标签时，获取下一个标签内容
            #print(tag)

            #print(each.contents)  # 将多个标签以列表返回

            score_list.append(tag.string)

    return score_list
#scores = get_movies_score(headers)
#print(scores)



class movies_scores(object):
    def __init__(self, headers, k):     # k最大为20， 因为网页最多只有250个电影
        self.res = self.get_result(headers,k)
    
    @staticmethod
    def get_result(headers, k):
        result = []

        for i in range(k):
            link = f'https://movie.douban.com/top250?start={i*25}&filter='
            r = requests.get(link,headers=headers,timeout=10)

            soup = BeautifulSoup(r.text,'lxml')
            
            div_list = soup.findAll('div',class_='info')

            for each in div_list:
                movie = each.a.span.string
                score = each.find('span',class_='rating_num').string

                result.append((movie,score))
        return result

res = movies_scores(headers,k=2)
res = res.res
print(res)

