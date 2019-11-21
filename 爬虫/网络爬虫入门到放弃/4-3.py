# selenium 的安装之后，以谷歌浏览器为例，需要下载[chromedriver](https://npm.taobao.org/mirrors/chromedriver)，到环境中，才能狗正常运行

from selenium import webdriver
# 打开浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('http://www.santostang.com/2018/07/04/hello-world/')

# 人工网页检查，定位评论数据，得到标签为 < div class="reply-content"><p>评论</p>

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
'''为什么没有定位到评论元素
代码中的 JavaScript 解析成了一个 iframe，
<
iframe title=”livere” scrolling=”no”…>
也就是说，所有的评论都装在这个框架之中，里面的评论并没有解析出来，所以我们才找不到div.reply-content元素。
需要加上对 iframe 的解析。
'''

# 获取第一条评论数据
comment = driver.find_element_by_css_selector('div.reply-content')
#> driver.find_element_by_css_selector是用CSS选择器查找元素，找到class为’reply-content’的div元素；
content = comment.find_element_by_tag_name('p')
#> find_element_by_tag_name则是通过元素的tag去寻找，意思是找到comment中的p元素。
print(content.text) 
#> 输出text文本


'''
http://www.santostang.com/2018/07/15/4-3-%E9%80%9A%E8%BF%87selenium-%E6%A8%A1%E6%8B%9F%E6%B5%8F%E8%A7%88%E5%99%A8%E6%8A%93%E5%8F%96/

使用Selenium抓取所有评论及一些操作

> selenium -- https://github.com/2048JiaLi/my-learning-100days/blob/master/1121-day20.md
'''