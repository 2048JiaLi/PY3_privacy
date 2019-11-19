## 问：说说Python种有几种字符串格式化？

## 答：Python字符串格式化主要有两种方式：分别为占位符(%)和format方式 。文末还有2种要介绍，所以总共有4种 。

其中，占位符(%)方式比较老，而format方式是比较先进的，目前两者共存。占位符方式在Python2.x中用的比较广泛，随着Python3.x的使用越来越广，format方式使用的更加广泛。

### 区别
1. 占位符(%)方式

![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoepeToeIaCzteib1Jc8xBdEMicRXBicrRibRCNQPjKvxcdIYDLh59TSRULOfkmXaw24DcbfAm4cquXibA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> 例
%d 格式整型
```
age = 29
print("my age is %d" %age)
#my age is 29
```

%s 格式字符串
```
name = "makes"
print("my name is %s" %name)
#my name is makes
```

2. format方式
> https://www.cnblogs.com/lvcm/p/8859225.html

在Python3引入了一个新的字符串格式化的方法，并且随后支持了Python2.7。这个新的字符串格式化方法摆脱了%操作符并且使得字符串格式化的语法更规范了。现在时候通过调用字符串对象的.format() 方法进行格式化。

**位置映射**
![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoepeToeIaCzteib1Jc8xBdE76Z4NHKfSMmvFjWMiaykHD7iblPWY1rUicbibRmIFtkgajycLD2q0eopvA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

```
print("{}:{}".format('192.168.0.100',8888))
#192.168.0.100:8888
```

**关键字映射**
![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoepeToeIaCzteib1Jc8xBdEe6zR8JZ22FfiaACboPoWYt5GlVJwnoGmVxtTtqJhD4qicjtEYz5eYS9w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
```
print("{server}{1}:{0}".format(8888,'192.168.1.100',server='Web Server Info :'))
#Web Server Info :192.168.1.100:8888
```

**元素访问**
![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoepeToeIaCzteib1Jc8xBdEc2LhvDpKiclPwHhibVsZYlWVmvb2Tqj7uwicMbX86UxRmtVOJmjMeWhrQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoepeToeIaCzteib1Jc8xBdEpOhnS8fv5U5ibqfZoTKpH8OhMVvccRc2aYlDIBiav9oibNyMx7oHqWcLw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

```
print("{0[0]}.{0[1]}".format(('baidu','com')))
#baidu.com
```

**填充对齐**
^、<、>分别是居中、左对齐、右对齐

![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoepeToeIaCzteib1Jc8xBdEB2Llib4Yp1K9BRINibwWp21HgEwj70jSpW9rrkeP1pE01iaaiaUibW8dkicA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> 九九乘法表

```
for i in range(1,10):
    a = 1
    while a <= i:
        print("{0}*{1}={2:0>2}".format(a,i,a*i),end="\t")
        a +=1
    print()
     
"""
1*1=01
1*2=02 2*2=04
1*3=03 2*3=06 3*3=09
1*4=04 2*4=08 3*4=12 4*4=16
1*5=05 2*5=10 3*5=15 4*5=20 5*5=25
1*6=06 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
1*7=07 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
1*8=08 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
1*9=09 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81
"""
```

- Python还有另外2种格式化。

1. 在Python 3.6 中添加了一个新的字符串格式化方法，被称为字面量格式化字符串或者“f-strings”。这个新的方法让你能够在字符串常量中嵌入Python表达式。
```
>>> f'Hello, {name}!'
'Hello, Bob!'
```

2. **模板字符串**。使用模板字符串的最佳的时机就是当你的程序需要处理由用户提供的输入内容时。
`Template()`里面把字符串中某个值用设置变量${key}的方式先写好，然后在substitute()的方式把变量用其他值代替，就完成了字符串的替换。

```
>>> from string import Template
>>> a=Template('would it be the ${key1} when we meet in ${key2}')
>>> a.substitute(key1='same',key2='heaven')
'would it be the same when we meet in heaven'
```
