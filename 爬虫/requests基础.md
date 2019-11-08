## requests库
```
import requests
url = "http://www.santostang.com/"
r = requests.get(url)
```
### 基本响应内容
+ r.text 是服务器响应的内容（html代码）
+ r.encoding 是服务器内容使用的文本编码
   + UTF-8
+ r.status_code 服务器响应状态码
   + 200 ： 请求成功
   + 4xx ： 客户端错误
   + 5xx ： 服务器响应错误
+ r.content 是字节方式响应
+ r.json 是内置JSON解码器
### 参数
#### 传递URL参数
为了请求特定的数据，需要在URL的查询字符串中加入某些数据。   
如果是自己构建的URL，其数据一般会跟在一个问好后面，并且以键/值的形式放在URL中，如***http://httpbin.org/get?key1=value1&key2=value2***   
+ 使用params传递
```
key_dict = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=key_dict)
print('URL正确解码:',r.url)
```
#### 定制请求头
+ 使用headers参数
```
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r = requests.get(url,headers=headers)
```
#### 发送POST请求
有时需要发送一些编码为表单形式的数据，如在登录的时候请求就为POST
+ 使用data参数
```
key_dict = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=key_dict)
```
#### 超时问题
若爬虫遇到服务器长时间不返回，会导致其一直等待   
+ 设置timeout参数，在timeout时间内没有应答，会抛出异常
```
r = requests.get(url, timeout=0.001)
```
