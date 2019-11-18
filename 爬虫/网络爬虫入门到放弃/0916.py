# 3.2节  获取响应内容
import requests
url = "http://www.santostang.com/"
r = requests.get(url)

print('文本编码:',r.encoding)
print('响应状态码:',r.status_code)
#print('字符串方式的响应体:',r.text)
#print('字节方式响应',r.content)
#print(r.json)

# 3.3.1  传递url参数
key_dict = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=key_dict)
print('URL正确解码:',r.url)
#print(r.text)

# 3.3.2  get请求头
#User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r = requests.get(url,headers=headers)
print(r.status_code)

# 3.3.3  post请求
key_dict = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=key_dict)
print(r.text)

# 3.3.4  超时
r = requests.get(url, timeout=0.001)