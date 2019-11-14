## 问：说说 Python 中有几种数据类型？

## 答：Python 中主要有8种数据类型：number（数字）、string（字符串）、list（列表）、tuple（元组）、dict（字典）、set（集合）、Boolean（布尔值）、None（空值）。

### 六个标准的数据类型

![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WpweWtheKGHRomj1A6IolUHQHTlF7qLBpWRSwPTqAbDicib3wZ58DXUba3mKhibVH0pHpaBsxMZSK34g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

1. 字符串
字符串的声明有三种方式：单引号、双引号和三引号（包括三个单引号或三个双引号）
```
>>> str1 = 'hello world'
>>> str2 = "hello world"
>>> str3 = '''hello world'''
>>> str4 = """hello world"""
>>> print str1
hello world
>>> print str2
hello world
>>> print str3
hello world
>>> print str4
hello world
```

2. 数字
Python3 支持三种不同的数值类型：

   - **整型(int)**： 通常被称为是整型或整数，是正或负整数，不带小数点。
   > **Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。**

   - **浮点型(float)**: 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示 。

   - **复数(complex)**: 复数由实数部分和虚数部分构成，可以用`a + bj`,或者`complex(a,b)`表示， 复数的实部a和虚部b都是浮点型。

3. 列表
列表是一种可修改的集合类型，其元素可以是数字、string等基本类型，也可以是列表、元组、字典等集合对象，甚至可以是自定义的类型。其定义方式如下：
```
>>> nums = [1,2,3,4]
>>> type(nums)
<type 'list'>
>>> print nums
[1, 2, 3, 4]
>>> strs = ["hello","world"]
>>> print strs
['hello', 'world']
>>> lst = [1,"hello",False,nums,strs]
>>> type(lst)
<type 'list'>
>>> print lst
[1, 'hello', False, [1, 2, 3, 4], ['hello', 'world']]
```

4. 元组

元组类型和列表一样，也是一种序列，与列表不同的是，**元组是不可修改的**。元组的声明如下：
```
lst = (0,1,2,2,2)
lst1=("hello",)
lst2 = ("hello")
print type(lst1) #<type 'tuple'> 只有一个元素的情况下后面要加逗号 否则就是str类型
print type(lst2) #<type 'str'>
```

5. 字典

字典是另一种**可变容器模型**，且可**存储任意类型对象**。字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
```
>>>dict = {'a': 1, 'b': 2, 'b': '3'}
>>> dict['b']
'3'
>>> dict
{'a': 1, 'b': '3'}
```

> 不存在__hash__方法的不可用于字典键
>
> list , set都不行， frozenset可以

6. 集合

集合（set）是一个无序的不重复元素序列。可以使用大括号 { } 或者 set() 函数创建集合。

> 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。创建格式：
```
a={'a','b','c','d'}
b=set('abcdefabcd')
c=set({'a':1,'b':2})
d=set(['a','b','c','a'])
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

#运行结果
{'c', 'd', 'b', 'a'} <class 'set'>
{'f', 'e', 'b', 'c', 'd', 'a'} <class 'set'>
{'b', 'a'} <class 'set'>
{'c', 'b', 'a'} <class 'set'>
```