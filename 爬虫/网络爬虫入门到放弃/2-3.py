#第一步： 获取页面
import requests
url = "http://www.santostang.com/"
#网页检查   点击一次后查看 Network CSS Headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

#浏览器代理问题会出现Requests.exceptions.ProxyError: HTTPConnectionPool(host='127.0.0.1', port=63222)
r = requests.get(url,headers=headers)
#print(r.text)#返回网页源码

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'lxml')#使用BeautifulSoup解析源码

#在网页上，所需要的数据部分右击检查，找到对应位置
#title = soup.find('h1',class_='post-title').a.text.strip()#第一篇文章标题
tag = soup.find('h1',class_='post-title').a #标签
print(tag)
#<a href="http://www.santostang.com/2018/07/15/4-3-%e9%80%9a%e8%bf%87selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/">第四章 – 4.3 通过selenium 模拟浏览器抓取</a>
print(tag.string)#获取标签内非属性字符串
#第四章 – 4.3 通过selenium 模拟浏览器抓取