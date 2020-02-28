
# 110道python面试笔试题汇总
> https://mp.weixin.qq.com/s/Xx1EFDlDHKZ6csj7OjVO7w

- [1、一行代码实现1--100之和](#一行代码实现1--100之和)
- [2、如何在一个函数内部修改全局变量](#如何在一个函数内部修改全局变量)
- [3、列出5个python标准库](#列出5个python标准库)
- [4、字典如何删除键和合并两个字典](#字典如何删除键和合并两个字典)
- [5、谈下python的GIL](#python的GIL)
- [6、`fun(*args,**kwargs)`中的`*args`,`**kwargs`什么意思？](#fun(*args,**kwargs)中的*args,**kwargs什么意思？)
- [7、python2和python3的`range（100）`的区别](#python2和python3的range（100）的区别)
- [8、什么样的语言能够用装饰器？](#什么样的语言能够用装饰器？)
- [9、简述面向对象中`__new__`和`__init__`区别](#简述面向对象中__new__和__init__区别)
- [10、简述with方法打开处理文件帮我我们做了什么？](#简述with方法打开处理文件帮我我们做了什么？)
- [11、python中断言方法举例](#python中断言方法举例)
- [12、SQL去重语句](#SQL去重语句)
- [13、Linux常用命令](#Linux常用命令)


## 一行代码实现1--100之和
利用sum()函数求和
```py
sum(range(0,101))
```

## 如何在一个函数内部修改全局变量
利用global 修改全局变量
```py
a = 5

def fun():
    global a
    a = 4

fun()
print(a)
```

> 在函数内部只需首次使用`global a`，其后在使用全局变量`a`时不需要再次使用`global`关键字

## 列出5个python标准库
- `os`：提供了不少与操作系统相关联的函数
- `sys`:   通常用于命令行参数
- `re`:   正则匹配
- `math`: 数学运算
- `datetime`: 处理日期时间
- `time`
- `path`
- `random`
- `threading` : 线程
- `multiprocessing` : 进程
- `queue` : 队列

## 字典如何删除键和合并两个字典
del和update方法
```py
dic = {'name':'zs', 'age':'18'}
del dic['name']

>>> dic
>>> {'age':18}

dic.update({'name':'ls'})

>>> dic
>>> {'age':18, 'name':'ls'}
```

合并的其他方法
- dict1.items()+dict2.items()
- dict3 = {**dict1, **dict2}  ， 若有重复的键，只会保留其中一个键值（\*\*将字典转换为关键字参数）
  > 这里还有一种是dict3 = dict(dict1 , **dict2)
  > 使用这种方法时，dict2的键必须为字符串形式

## python的GIL
GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

## fun(*args,\*\*kwargs)中的\*args,\*\*kwargs什么意思？
\*args和\*\*kwargs主要用于函数定义。

你可以将不定数量的参数传递给一个函数。这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你，所以在这个场景下使用这两个关键字。

`*args`是用来发送一个非键值对的可变数量的参数列表给函数。

例：
```py
def demo(args_f, *args_v):
    print(args_f)
    for x in args_v:
        print(x)


>>> demo('a','b','c','d')
>>> a
>>> b
>>> c
>>> d
```

`**kwargs`允许将不定长的键值对作为参数传递给一个函数。如果在一个函数里处理带名字的参数，就应该使用`**kwargs`

例：
```py
def demo(**args_v):
    for k,v in args_v.items():
        print(k,v)

>>> demo(name='wj')
>>> name wj
```

## python2和python3的range（100）的区别
python2返回列表，python3返回迭代器，节约内存

## 什么样的语言能够用装饰器？
函数可以作为参数传递的语言，可以使用装饰器

## 简述面向对象中__new__和__init__区别
`__init__`是初始化方法，创建对象后，就立刻被默认调用了，可接收参数，如

```py
class Bike:
    
    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def move(self):
        print('run')

# 创建对象
BM = Bike(2,'green')

print(BM.wheelNum,BM.color)
```

1. `__new__`至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
2. `__new__`必须要有返回值，返回实例化出来的实例，这点在自己实现`__new__`时要特别注意，可以`return`父类（通过`super(当前类名, cls)`）`__new__`出来的实例，或者直接是`object`的`__new__`出来的实例
3. `__init__`有一个参数`self`，就是这个`__new__`返回的实例，`__init__`在`__new__`的基础上可以完成一些其它初始化的动作，`__init__`不需要返回值
4. 如果`__new__`创建的是当前类的实例，会自动调用`__init__`函数，通过`return`语句里面调用的`__new__`函数的第一个参数是`cls`来保证是当前类实例，如果是其他类的类名，那么实际创建返回的就是其他类的实例，其实就不会调用当前类的`__init__`函数，也不会调用其他类的`__init__`函数。

```py
class A(object):
    def __init__(self):
        print('this is method of init',self)

    def __new__(cls):
        print('this is ID of cls', id(cls))
        print('this is method of new', object.__new__(cls))
        return object.__new__(cls)

>>> A()
>>> print(id(A))

>>> this is ID of cls 55440648
>>> this is method of new <__main__.A object at 0x0000000003D32550>
>>> this is method of init <__main__.A object at 0x0000000003D32550>
>>> 55440648
```

> `init`方法中的`self`和`new`方法返回值地址一样
> 
> `cls`和类ID一样，说明指向同一个类，也就是`cls`创建的实例类

## 简述with方法打开处理文件帮我我们做了什么？
```py
f = open('1.txt','wb')
try:
    f.write('hello world')
except:
    pass
finally:
    f.close()
```
打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的`f.open`写法，我们需要`try`,`except`,`finally`，做异常判断，并且文件最终不管遇到什么情况，都要执行`f.close()`关闭文件，`with`方法帮我们实现了`finally`中`f.close`

（当然还有其他自定义功能，有兴趣可以研究with方法源码）

## python中断言方法举例
`assert（）`方法，断言成功，则程序继续执行，断言失败，则程序报错
```py
a = 3
assert(a>1)
print('success! program is going on')

b = 4
assert(b>7)
print('error!')
```

## SQL去重语句
数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句

`select  distinct  name  from  student`

## Linux常用命令
[Linux命令大全](https://www.runoob.com/linux/linux-command-manual.html)
1. `ls`：用于显示指定工作目录下之内容（列出目前工作目录所含之文件及子目录)。
2. `pwd`: 用于显示工作目录（执行`pwd`指令可立刻得知您目前所在的工作目录的绝对路径名称。）
3. `cd`：用于切换当前工作目录至 `dirName(目录参数)`。
>> 其中` dirName `表示法可为绝对路径或相对路径。若目录名称省略，则变换至使用者的 `home` 目录 (也就是刚 login 时所在的目录)。

>> 另外，`~` 也表示为 `home` 目录 的意思，`.` 则是表示目前所在的目录，`..` 则表示目前目录位置的上一层目录。
4. `touch`：用于修改文件或者目录的时间属性，包括存取时间和更改时间。若文件不存在，系统会建立一个新的文件。
>> ls -l 可以显示档案的时间记录。
5. `rm`：用于删除一个文件或者目录。
6. `mkdir`： 用于建立名称为 `dirName `之子目录。
7. `tree`： 用于以树状图列出目录的内容。(执行`tree`指令，它会列出指定目录下的所有文件，包括子目录里的文件。)
8. `cp`： 用于复制文件或目录
9.  `mv`： 为文件或目录改名、或将文件或目录移入其它位置。
10. `cat`： 用于连接文件并打印到标准输出设备上。
11. `more`： 类似 `cat` ，不过会以一页一页的形式显示，更方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示，而且还有搜寻字串的功能（与 `vi` 相似），使用中的说明文件，请按 h 。
12. `grep`：用于查找文件里符合条件的字符串。
>> `grep` 指令用于查找内容包含指定的范本样式的文件，如果发现某文件的内容符合所指定的范本样式，预设 `grep` 指令会把含有范本样式的那一列显示出来。若不指定任何文件名称，或是所给予的文件名为 `-`，则 `grep` 指令会从标准输入设备读取数据。
13. `echo`： Shell 的 `echo` 指令与 PHP 的 `echo` 指令类似，都是用于字符串的输出。


## 