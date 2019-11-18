# http://www.santostang.com/2018/07/14/4-2-%E8%A7%A3%E6%9E%90%E7%9C%9F%E5%AE%9E%E5%9C%B0%E5%9D%80%E6%8A%93%E5%8F%96/
import requests
import json

# 找到真实地址
link = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112405380131615034451_1573727301656&limit=10&offset=1&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1573727301659'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
   
# link 中 limit=10&offset=1 , limit 代表的是每一页评论数量的最大值，也就是说，这里每一页评论最多显示30条；offset 代表的是第几页，第一页 offset 为0，第二页为1，那么第三页 offset 会是3。
#因此，我们只需在URL中改变 offset 的值，便可以实现换页。

def dynamic(headers, k):
    link_pre = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112405380131615034451_1573727301656&limit=10&'
    link_aft = '&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1573727301659'

    for i in range(k):
        link = link_pre + f'offset={i+1}' + link_aft
        r = requests.get(link,headers=headers)

        json_string = r.text
        json_string = json_string[json_string.find('{'):-2]
        json_data = json.loads(json_string)

        comment_list = json_data['results']['parents']
        for eachone in comment_list:
            message = eachone['content']
            print (message)

''' json_data格式 ， 其中'content':' ' 才是爬取内容 , 通过打印查看
json_data = {
    'results' : {
        'parents': [{... , 'content':' ' , ...} , {... , 'content':' ' , ...}],
        'children': [], 
        'quotations': []
    }
    'resultCode': 200, 
    'resultMessage': 'Okay, livere'
}
'''     

'''
代码的说明
1. 使用json_string[json_string.find('{'):-2]， 仅仅提取字符串中符合json格式的部分
2. 使用 json.loads 可以把字符串格式的响应体数据转化为 json 数据
3. json 数据的结构，我们可以提取到评论的列表comment_list
4. 通过一个 for 循环，提取其中的评论文本，并输出打印。
'''
dynamic(headers,2)