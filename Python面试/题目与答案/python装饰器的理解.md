## 问：说说对于Python装饰器的理解？

## 答：装饰器在python在面试中非常常见，属于比较重要的内容了 。Python装饰器本质上就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用Python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能 。

在实际项目中，python装饰器也是一个非常有用的功能，可以在不改变函数代码和调用方式的情况下给函数添加新的功能，广泛应用于权限校验、性能统计、日志打印等应用场景。

### python装饰器完全解读
> 来自于 https://www.cnblogs.com/chenhuabin/p/11369359.html


#### 1 引言

装饰器（Decorators）可能是Python中最难掌握的概念之一了，也是最具Pythonic特色的技巧，深入理解并应用装饰器，你会更加感慨——人生苦短，我用Python。

#### 2 初步理解装饰器
- 2.1 什么是装饰器

Python是一门面向对象的语言，Python基本思想就是一些皆对象，数据类型是对象、类是对象、类实例也是对象……对于接下来我们要说的装饰器而言，最重要的是，**函数也是对象**！

函数也和数据类型等概念一样，都是对象，那么既然数据类型可以进行赋值操作，那么函数是不是也可以赋值呢？当然可以！

```
def do_something():
    print('完成一些功能')

if __name__ == '__main__':
    do = do_something
    do()
```

输出：
```
完成一些功能
```

不仅如此，函数当做参数传递给其他函数：
```
def do_something():
    print('正在完成功能')

def func(f):
    f()

if __name__ == '__main__':
    func(do_something)
```

正是因为Python中函数既可以赋值给其他变量名，也可以当做参数参数进其他函数，所以，上面的代码没有任何问题。

当然，毕竟被称呼为函数，有别有变量之类的概念，所以它也有自己的特性，例如在函数内部，还可以定义函数，甚至作为返回值返回：
```
def func():
    def inner_func():
        print('我是內部函数')
    return inner_func

if __name__ == '__main__':
    fun1 = func()
    fun1()
```

函数的这几个特性：
   - 可以赋值给其他变量；

   - 可以作为参数传递给其他函数；

   - 可以在内部定义一个函数；

   - 可以当做返回值返回

**装饰器正是这几个特性为基石**。从本质上来说，装饰器就是一个函数，它也具有我们上面说到的4个特性，而且充分利用了这4个特性。

装饰器接受一个普通函数作为参数，并在内部定义了一个函数，在这个内部函数中实现了一些功能，并调用了传递进来的函数，最后将内部函数作为返回值返回。如果一个函数把这个步骤全走了一遍，我们就可以认为，这个函数是一个装饰器函数，或者说装饰器。

一个简单的装饰器：
```
def func(f):
    def inner_func():
        print('{}函数开始运行……'.format(f.__name__))
        f()
        print('{}函数结束运行……'.format(f.__name__))
    return inner_func

def do_something():
    print('正在完成功能')

if __name__ == '__main__':
    do_something = func(do_something)
    do_something()
```

输出结果：
```
do_something函数开始运行……

正在完成功能

do_something函数结束运行……
```

上面代码，将`do_something`方法作为参数传递给`func`方法，在`func`方法内部我们定义了一个`inner_func`方法，并在这个方法中添加了函数开始执行和结束执行的提示，在`func`方法最后，我们将`inner_func`作为参数返回，更加值得一说的是，我们重新将`func`函数的返回值赋给了`do_something`.

所以，最后一行我们再次调用的`do_something`方法已经不再是最初的`do_something`函数，而是`func`方法内定义的`inner_func`函数，所以最后执行`do_something`函数时，会有函数开始执行和结束执行的提示功能，而后面再调用`do_something`函数时，也都直接使用`do_something()`。

> `func`函数就是一个装饰器，捋一捋你会发现，`func`函数把我们上面说过的所有特性、步骤全实现了。

如果你在别处见过Python装饰器的使用，你可能会疑惑，我们实现的`func`装饰器跟你见过的装饰器不都一样，因为在实际应用中，装饰器大多是与“@”符号结合起来使用。其实“@”符号所实现的功能就是 `do_something = func(do_something)`这行代码的功能。来，我们尝试一下使用“@”：

```
def func(f):
    def inner_func():
        print('{}函数开始运行……'.format(f.__name__))
        f()
        print('{}函数结束运行……'.format(f.__name__))
    return inner_func

@func
def do_something():
    print('正在完成功能')

if __name__ == '__main__':
    do_something()
```

输出结果：
```
do_something函数开始运行……

正在完成功能

do_something函数结束运行……
```

`func`函数就是一个装饰器，所以使用“@”符号时，我们只需要在被装饰的函数前面加上“@func”就表示该函数被`func`装饰器装饰，在需要处直接调用`do_something`函数即可。

- 2.2 为什么要用装饰器

在上面代码中，我们写了一个装饰器`func`，在这个装饰器中，使用装饰器的好处就已经初见端倪了。

   - 可以在不对被装饰函数做任何修改的前提下，给被装饰函数附加上一些功能。使用`@func`对`do_something`函数进行装饰时，我们没有对`do_something`函数的代码做什么的改变，但是被装饰后的`do_something`函数却多了开始运行和结束运行的功能。

   - 不改变被装饰函数的调用方式。在被装饰前，我们通过`do_something()`调用这个函数，被装饰后，还是通过`do_something()`调用这个函数。

   - 代码更加精简。在上面代码中，我们只是用`@func`装饰了`do_something`一个函数，但是如果有多个函数需要添加开始运行和结束运行的提示功能，如果不用装饰器，那么就需要对每一个函数进行修改，则工作量和需要修改的代码量……用了装饰器之后，只需要在需要添加这一功能的函数前面添加`@func`就可以了。

装饰器可以在不改变原函数调用方式和代码情况下，为函数添加一些功能，使代码更加精简。

例：统计一个函数的运行时间
```
import time
def timmer(f):
    def inner_func():
        start_time = time.time()
        f()
        end_time = time.time()
        print('{}函数运行消耗时间为：{}'.format(f.__name__, end_time-start_time))
    return inner_func

@timmer
def do_something():
    print('do_something函数运行……')
    time.sleep(1)

if __name__ == '__main__':
    do_something()
```

输出结果：
```
do_something函数运行……

do_something函数运行消耗时间为：1.000662088394165
```

在上面例子中，我们首先定义了一个计时装饰器`timmer`，当需要统计某个函数运行时间时，只需要在函数定义时，在前面添加一行写上`@timmer`即可，例如上面对`do_something`函数运行时间进行统计，对`do_something`原来要实现什么功能就继续实现这一功能，原来代码该怎样还怎样，该怎么调用还怎么调用。所以说，使用装饰器可以在不改变原函数代码和调用方式的情况下附加上其他功能。

#### 3 深入理解装饰器
- 3.1 被装饰的函数带返回值

上面写的两个装饰器所装饰的`do_something`函数是没有返回值的，但大多数函数可都是有返回值的。针对有返回值的函数，装饰器该怎么写呢？
```
def func(f):
    def inner_func():
        print('{}函数开始运行……'.format(f.__name__))
        ret = f()
        print('{}函数结束运行……'.format(f.__name__))
        return ret  # 这里返回值
    return inner_func

@func
def do_something():
    print('正在完成功能')
    return '我是返回值'

if __name__ == '__main__':
    ret = do_something()
    print(ret)
```

输出结果：
```
do_something函数开始运行……

正在完成功能

do_something函数结束运行……

我是返回值
```

被装饰后的`do_something`函数其实不再是最初的`do_something`函数，而是装饰器内部定义的`inner_func`函数，所以，被装饰的函数的返回值只需要通过装饰器内部定义的`inner_func`函数返回返回即可即可。

- 3.2 被装饰函数带参数
对于装饰器，我们要深刻理解一件事：以上面的装饰器`func`和被装饰函数`do_something`为例，被装饰后的`do_something`函数已经不再是原来的`do_something`函数，而是装饰器内部的`inner_func`函数。

这句话我已经在上文中我已经不止提过一次，因为真的很重要。如果被装饰的函数有参数（加入参数为`name`），我们还是通过`do_something(name)`的方式传递传输，不过，既然我们最终调用的时候，通过`do_something`实质调用的`inner_func`函数，那么在定义装饰器是，定义的`inner_func`函数时也需要接受参数。

```
def func(f):
    def inner_func(name):
        print('{}函数开始运行……'.format(f.__name__))
        ret = f(name)
        print('{}函数结束运行……'.format(f.__name__))
        return ret
    return inner_func

@func
def do_something(name):
    print('你好，{}！'.format(name))
    return '我是返回值'

if __name__ == '__main__':
    ret = do_something('姚明')
    print(ret)
```


输出结果：
```
do_something函数开始运行……

你好，姚明！

do_something函数结束运行……

我是返回值
```

一个装饰器可用于装饰千千万万个函数，则千千万万个函数参数情况可能各不相同，有的没有参数，有的可能多个参数，甚至还有关键字参数，对于这参数情况不同的函数，我们不可能为每个函数都写一个`func`装饰器，那怎么办呢？

Python中提供了\*args， \*\*kwargs这种机制来接受任意位置的位置参数和关键字参数，参数前面带\*表示接受任意个数**位置参数**，接收到的所有位置参数存储在变量名为`args`的**元组**中，带\*\*表示接受任意个数的**关键字参数**，接收到的所有关键字参数以字典的形式参数在变量名为kwargs的**字典**中。

当我们知道只有位置参数，但不知道有多少个位置参数是`func`装饰器可以这么写：

```
def func(f):
    def inner_func(*name):
        print('{}函数开始运行……'.format(f.__name__))
        ret = f(*name)
        print('{}函数结束运行……'.format(f.__name__))
        return ret
    return inner_func

@func
def do_something(name):
    print('你好，{}！'.format(name))

@func
def do_something_2(name_1, name_2):
    print('你好，{}！'.format(name_1))
    print('你好，{}！'.format(name_2))

@func
def do_something_3(*name):
    for n in name:
        print('你好，{}！'.format(n))

if __name__ == '__main__':
    do_something('姚明')
    print('-------------------------------')
    do_something_2('姚大明', '姚小明')
    print('-------------------------------')
    do_something_3('姚一明', '姚二明', '姚三明', '姚四明')
```

输出结果：
```
do_something函数开始运行……

你好，姚明！

do_something函数结束运行……

-------------------------------

do_something_2函数开始运行……

你好，姚大明！

你好，姚小明！

do_something_2函数结束运行……

-------------------------------

do_something_3函数开始运行……

你好，姚一明！

你好，姚二明！

你好，姚三明！

你好，姚四明！

do_something_3函数结束运行……
```

> *args，**args只是一个变量名，可以更改，只不过是约定俗成，

当我们知道只有关键字参数，却不知道参数个数时，可以func装饰器这么写：
```
def func(f):
    def inner_func(**name):
        print('{}函数开始运行……'.format(f.__name__))
        ret = f(**name)
        print('{}函数结束运行……'.format(f.__name__))
        return ret
    return inner_func

@func
def do_something(name='无名氏'):
    print('你好，{}！'.format(name))

@func
def do_something_2(name_1='无名氏', name_2='无名氏'):
    print('你好，{}！'.format(name_1))
    print('你好，{}！'.format(name_2))

@func
def do_something_3(**name):
    for n in name.keys():
        print('你好，{}！'.format(name[n]))

if __name__ == '__main__':
    do_something(name='姚明')
    print('-------------------------------')
    do_something_2(name_1='姚大明', name_2='姚小明')
    print('-------------------------------')
    do_something_3(name_1='姚一明', name_2='姚二明', name_3='姚三明', name_4='姚四明')
```

输出结果：
```
do_something函数开始运行……

你好，姚明！

do_something函数结束运行……

-------------------------------

do_something_2函数开始运行……

你好，姚大明！

你好，姚小明！

do_something_2函数结束运行……

-------------------------------

do_something_3函数开始运行……

你好，姚一明！

你好，姚二明！

你好，姚三明！

你好，姚四明！

do_something_3函数结束运行……
```

事实上，大多数情况下，我们对被装饰函数是一无所知的——我们不知道有多少个位置参数、多少个关键字参数，甚至对有没有位置参数、关键字参数都不知道，这时候，我们就只能\*args和\*\*kwargs齐上阵了：
```
def func(f):
    def inner_func(*name1, **name2):
        print('{}函数开始运行……'.format(f.__name__))
        ret = f(*name1, **name2)
        print('{}函数结束运行……'.format(f.__name__))
        return ret
    return inner_func

@func
def do_something(name):
    print('你好，{}！'.format(name))

@func
def do_something_2(name_1, name_2='无名氏'):
    print('你好，{}！'.format(name_1))
    print('你好，{}！'.format(name_2))

@func
def do_something_3(*name1, **name2):
    for n in name1:
        print('你好，{}！'.format(n))
    for n in name2.keys():
        print('你好，{}！'.format(name2[n]))

if __name__ == '__main__':
    do_something(name='姚明')
    print('-------------------------------')
    do_something_2(name_1='姚大明', name_2='姚小明')
    print('-------------------------------')
    do_something_3('姚一明', '姚二明', '姚三明', name_4='姚四明')
```

- 3.3 装饰器本身带参数

上面写的装饰器都没有参数，或者说只有一个自带参数，也就是被装饰函数f。

其实，**装饰器也是可以有其他参数的**，这样的装饰器更加灵活。

我们通过实例来说明：现在我们要对上面的`func`装饰器进行改进，需要做到灵活控制装饰器是用中文输出还是用英文输出，代码如下。

```
def language(lang='中文'):  # 这里带参数
    def func(f):  # 往里嵌套了一层
        def inner_func(*name1, **name2):
            if lang=='中文':
                print('{}函数开始运行……'.format(f.__name__))
            else:
                print('The function of {} starts runging…'.format(f.__name__))
            ret = f(*name1, **name2)
            if lang=='中文':
                print('{}函数结束运行……'.format(f.__name__))
            else:
                print('The function of {} ends runging…'.format(f.__name__))
            return ret
        return inner_func
    return func

@language('中文')
def do_something(name):
    print('你好，{}！'.format(name))

@language('English')
def do_something_2(name):
    print('你好，{}！'.format(name))


if __name__ == '__main__':
    do_something(name='姚明')
    print('-------------------------')
    do_something_2(name='姚明')
```

输出如下：
```
do_something函数开始运行……

你好，姚明！

do_something函数结束运行……

-------------------------

The function of do_something_2 starts runging…

你好，姚明！

The function of do_something_2 ends runging…
```

可以看到，通过装饰器带参数的方式，我们只需要在定义被装饰函数时，指定装饰器参数，就可以灵活控制每个被装饰函数提示的语言。

必须承认，**装饰器带参数后，看起来更加复杂，需要多嵌套一层函数，由最外层的函数接受参数，里层函数才是真正的装饰器**。**使用装饰器时，会首先运行带参数的最外层函数，返回装饰器，这一步Python会自动帮我们完成**。所以，带参数的装饰器甚至可以这么使用：
```
h = language('中文')
@h
def do_something(name):
    print('你好，{}！'.format(name))
```

- 3.4 多层装饰器

装饰器也是可以多层嵌套使用的，也就是说，**一个函数可以通过是被多个装饰器所装饰，执行顺序是从下到上的优先顺序加载装饰**：
```
# -*- coding: utf-8 -*-
import time

print(1)
def func(f):
    print(2)
    def inner_func(*name1, **name2):
        print('{}函数开始运行……'.format(f.__name__))
        f(*name1, **name2)
        print('{}函数结束运行……'.format(f.__name__))
    print(3)
    return inner_func

print(4)
def timmer(f):
    print(5)
    def inner_timmer(*args, **kwargs):
        print('开始计时……')
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print('开始结束……')
        time_cost = end_time - start_time
        print('{}函数运行时长为：{}秒'.format(f.__name__, time_cost))
    print(6)
    return inner_timmer

print(7)
@func
@timmer
def do_something(name):
    time.sleep(1)
    print('你好，{}！'.format(name))

print(8)
def do_something_2(name):
    time.sleep(1)
    print('你好，{}！'.format(name))


if __name__ == '__main__':
    print(9)
    do_something(name='姚明')
    print('-------------------------')
    func(timmer(do_something_2))(name='姚明')  # 执行效果与上面使用了@符号的do_something一样
```

输出结果：
```
1

4

7

5

6

2

3

8

9

inner_timmer函数开始运行……

开始计时……

你好，姚明！

开始结束……

do_something函数运行时长为：1.0004358291625977秒

inner_timmer函数结束运行……

-------------------------

5

6

2

3

inner_timmer函数开始运行……

开始计时……

你好，姚明！

开始结束……

do_something_2函数运行时长为：1.000028133392334秒

inner_timmer函数结束运行……
```

在上面代码中，我们同时用`func`和`timmer`两个装饰器来装饰`do_something`，从运行结果中可以看出，**两个装饰器都发挥了作用**。同时，为了方便大家理解，我们使用不带@符号的来使用两个装饰器装饰，两者运行结果是一样的，结合代码中的输出标记，我们来分析一下装饰器的执行过程：开始运行后，1->4->7这几个过程我相信大家都是可以理解的，到了位置7后，遇到了@符号标识的装饰器，而且是多层的，两个@装饰器相当于func(timmer(do_something_2))，所以是先执行timmer函数获取返回值作为参数传递给func，所以有了7之后是5->6，timmer函数返回值是inner_timmer函数，这时候就相当于func(inner_timmer),所以程序退出timmer函数后进入func函数，就有了2->3,从func函数返回后，继续向下执行遇到位置8，然后就进入了主函数运行，所以是8->9，此时的函数是被装饰过的，本质已经是func函数返回的inner_func函数了，所以最终在主函数中执行do_something时执行的是inner_func方法，所以先输出了func装饰器的函数开始提示，然后才是timmer装饰器的计时开始提示。

- 3.5 类装饰器

通过上面的介绍，**@符号是装饰器的一个表示，或者说一个装饰器语法糖，当使用@时，例如@A，这种语法糖会自动将被装饰函数f作为参数传递给A函数，然后将A函数的返回值重新f给f这个变量名，这就是@语法糖帮我们做的事情，概括来说就是f=A(f)()**。

我们现在发散一下思维，假设A如果是一个类会怎么样呢？我们知道当A是一个类时，A()表示调用A类的构造函数__init__实例化一个A类对象，那么A(f)就表示将函数f作为参数传递给A类的构造方法__init__来构造一个A类实例对象，如果使用了@符号，那么这种语法机制就还会在A(f)后面加一个括号变成A(f)()，这是什么鬼？执行一个类实例对象？不过话要说回来，如果A(f)()这种结构要是没有问题，能够成功执行，是不是就意味着Python中类也可以成为装饰器了呢？确实如此。我们先看看通过A()()执行一个类实例对象会怎么样：
```
class A(object):
    def __init__(self):
        print('实例化一个A类对象')
    def __call__(self, *args, **kwargs):
        print('__call__方法被调用……')

if __name__ == '__main__':
    A()()
```

输出结果：
```
实例化一个A类对象

__call__方法被调用……
```

通过`A()()`执行一个类实例对象时，执行的是A类内部的`__call__`方法。那么如果用A用作装饰器时，@A返回的就是A类内部定义的`__call__`方法，相当于函数装饰器`func`内的`inner_func`。感受一下类装饰器：
```
class A(object):
    def __init__(self, f):
        print('实例化一个A类对象……')
        self.f = f
    def __call__(self, *args, **kwargs):
        print('{}函数开始运行……'.format(self.f.__name__))
        self.f(*args, **kwargs)
        print('{}函数结束运行……'.format(self.f.__name__))

@A
def do_something(name):
    print('你好，{}！'.format(name))
if __name__ == '__main__':
    do_something('姚明')
```
输出结果：
```
实例化一个A类对象……

do_something函数开始运行……

你好，姚明！

do_something函数结束运行……
```

如果类装饰器带参数呢？这时候，类装饰器的参数也可定是通过@A(t)的形式传递，这时候，因为@语法糖会自动加括号的原因，结构就编程这样A(t)()，A(t)是类实例对象，A(t)()就是__call__方法，所以，@语法糖会把被装饰函数f作为参数传递给__call__方法，被装饰函数的参数需要在__call__内部定义一个函数来接受。也就是话说，定义类装饰器时，装饰器的参数通过__init__构造方法接收，被装饰函数的作为参数被__call__方法接收。
```
import time
class A(object):
    def __init__(self, t):
        print('实例化一个A类对象……')
        self.t = t
    def __call__(self, f):
        def inner_A(*args, **kwargs):
            print('延迟{}秒后开始执行……'.format(self.t))
            time.sleep(self.t)
            print('{}函数开始运行……'.format(f.__name__))
            f(*args, **kwargs)
            print('{}函数结束运行……'.format(f.__name__))
        return inner_A

@A(1)
def do_something(name):
    print('你好，{}！'.format(name))

if __name__ == '__main__':
    do_something('姚明')

```

输出结果：
```
实例化一个A类对象……

延迟1秒后开始执行……

do_something函数开始运行……

你好，姚明！

do_something函数结束运行……
```

无论是函数装饰器还是类装饰器，原理上是一样的，**区别在于如果A是函数，A()是直接调用函数，而A是类时，A()是实例化，通过A()()是调用A类的__call__方法**。

#### 4 Python中内置的装饰器

- 4.1 @property，@setter，@deleter
`@property`，`@setter`，`@deleter`这三个装饰器提供了更加友好的方式来获取、设置或删除类中的属性。

`@property`装饰器所装饰的函数可以像访问属性一样调用函数，注意，`@property`装饰器必须先于`@setter`，`@deleter`使用，且三者所装饰的函数必须同名。
```
class A(object):
    def __init__(self, v):
        print('实例化一个A类对象……')
        self.__value = v

    @property
    def value(self):
        print('取值时被调用')
        return self.__value

    @value.setter
    def value(self, value):
        print('赋值时被调用')
        self.__value = value

    @value.deleter
    def value(self):
        print('删除值时被调用……')
        del self.__value


if __name__ == '__main__':
    a = A(123)
    print('-------------')
    print('__value的值为：{}'.format(a.value))
    print('-------------')
    a.value = 234
    print('__value的值为：{}'.format(a.value))
    print('--------------')
    del a.value
    print('__value的值为：{}'.format(a.value))
```

输出为：
```
Traceback (most recent call last):

实例化一个A类对象……

-------------

取值时被调用

File "E:/WorkProjectCode/study_pymysql/study_secorators/test2.py", line 33, in <module>

__value的值为：123

-------------

print('__value的值为：{}'.format(a.value))

赋值时被调用

取值时被调用

__value的值为：234

File "E:/WorkProjectCode/study_pymysql/study_secorators/test2.py", line 11, in value

--------------

return self.__value

删除值时被调用……

取值时被调用

AttributeError: 'A' object has no attribute '_A__value'
```

运行产生异常，因为最后访问了已经删除了的元素。

- 4.2 @classmethod
一个类中，如果一个方法被`@classmethod`所装饰，就代表该方法与类绑定，而不是与实例对象绑定，第一个参数`cls`由Python机制自动传递，表示类本身。
```
class A(object):
    @classmethod
    def f(cls):
        print('当前类名为：{}'.format(cls.__name__))


if __name__ == '__main__':
    A.f()
```
输出结果：
```
当前类名为：A
```

- 4.3 @staticmethod
被`@staticmethod`所装饰的方法为静态方法，静态方法一般使用场景就是和类相关的操作，但是又不会依赖和改变类、实例的状态，比如一些工具方法。
```
import time
class A(object):
    @staticmethod
    def f():
        time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return time_now


if __name__ == '__main__':
    print(A.f())
    print(A().f())

```

输出：
```
2019-08-16 19:29:32

2019-08-16 19:29:32
```