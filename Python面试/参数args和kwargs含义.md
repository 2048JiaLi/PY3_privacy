## 问：Python中 *args 和 **kwargs 的含义？

### 答：在python中，*args和**kwargs通常使用在函数定义里。   
\*args 和 \*\*kwargs 都允许你给函数传不定数量的参数，即使在定义函数的时候不知道调用者会传递几个参数。   
***ps***: \*args和\*\*kwargs只是一个大家都遵守的习惯，名字可以任意写的。

+ #### \*args例子   
\*args能够接收不定量的非关键字参数，会把位置参数转化为tuple（非键值对的参数组），例子如下面代码所示：
```
def func(*args):
    for i in args:
        print(i)
func(1,2,3,4)

运行结果：
1
2
3
4
```
+ ### \*\*kwargs例子   
\*\*kwargs允许你传递不定量个关键字参数。   
如果你需要在函数中定义不定量个命名参数，那么你就要使用**kwargs了，它会把关键字参数转化为dict（键值对参数组），例子如下面代码所示：
```
def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
func(a=1,b=2,c=3,d=4)

运行结果：
a 1
b 2
c 3
d 4
```

# 主要区别：\*args不能接收带位置参数
