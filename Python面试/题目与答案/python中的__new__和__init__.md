## 问：说说Python中的__new__和__init__的区别？

## 答：在Python中`__new__`和`__init__`具有不同的功能。并且对于Python的新类和旧类而言功能也不同。

`__new__`是在实例**创建之前被调用的**，因为它的任务就是创建实例然后返回该实例对象，是个静态方法。

`__init__`是当实例对象**创建完成后被调用的**，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候。是一个实例方法。


> 以下来自https://www.jianshu.com/p/14b8ebf93b73
### `__new__`和`__init__`功能上的区别
**主要区别在于**：`__new__`是用来创造一个类的实例的，而`__init__`是用来初始化一个实例的。

## Python的新类和旧类

Python中的类分为新类和旧类。旧类是Python3之前的类，旧类并不是默认继承object类，而是继承type类。

Python2中的旧类如下面代码所示：
```
class oldStyleClass: # inherits from 'type'
    pass
```
Python2中定义一个新类：
```
class newStyleClass(object): # explicitly inherits from 'object'
    pass
```
在Python3中所有的类均默认继承`object`，所以并不需要显式地指定`object`为基类。

以`object`为基类可以使得所定义的类具有新类所对应的方法（`methods`）和属性（`properties`）。

在下面的文章中我们会分别基于新类和旧类探讨`__new__`和`__init__`。

### `__new__`和`__init__`参数的不同
`__new__`所接收的第一个参数是`cls`，而`__init__`所接收的第一个参数是`self`。

这是因为当我们调用`__new__`的时候，该类的实例还并不存在（也就是`self`所引用的对象还不存在），所以需要接收一个类作为参数，从而产生一个实例。而当我们调用`__init__`的时候，实例已经存在，因此`__init__`接受`self`作为第一个参数并对该实例进行必要的初始化操作。

**这也意味着`__init__`是在`__new__`之后被调用的**。


## Python新类中的`__new__`和`__init__`

Python的新类允许用户重载`__new__`和`__init__`方法，且这两个方法具有不同的作用。`__new__`作为构造器，起创建一个类实例的作用。而`__init__`作为初始化器，起初始化一个已被创建的实例的作用。

如下面代码是所示：
```
class newStyleClass(object): 
    # In Python2, we need to specify the object as the base.
    # In Python3 it's default.

    def __new__(cls):
        print("__new__ is called")
        return super(newStyleClass, cls).__new__(cls)

    def __init__(self):
        print("__init__ is called")
        print("self is: ", self)

newStyleClass()
```

结果如下：
```
__new__ is called
__init__ is called
self is: <__main__.newStyleClass at 0x109290890>
<__main__.newStyleClass at 0x109290890>
```

创建类实例并初始化的过程中`__new__`和`__init__`被调用的顺序也能从上面代码的输出结果中看出：`__new__`函数首先被调用，构造了一个`newStyleClass`的实例，接着`__init__`函数在`__new__`函数返回一个实例的时候被调用，并且这个实例作为`self`参数被传入了`__init__`函数。

这里需要注意的是，如果__new__函数返回一个已经存在的实例（不论是哪个类的），__init__不会被调用。如下面代码所示：
```
obj = 12 
# obj can be an object from any class, even object.__new__(object)

class returnExistedObj(object):
    def __new__(cls):
        print("__new__ is called")
        return obj

    def __init(self):
        print("__init__ is called")

returnExistedObj()
```
执行结果如下：
```
__new__ is called
12
```

同时另一个需要注意的点是：

如果我们在__new__函数中不返回任何对象，则__init__函数也不会被调用。

如下面代码所示：
```
class notReturnObj(object):
    def __new__(cls):
        print("__new__ is called")

    def __init__(self):
        print("__init__ is called")

print(notReturnObj())
```
执行结果如下：
```
__new__ is called
None
```

可见如果`__new__`函数不返回对象的话，不会有任何对象被创建，`__init__`函数也不会被调用来初始化对象。

## 总结
1. `__init__`不能有返回值

2. `__new__`函数直接上可以返回别的类的实例。如上面例子中的`returnExistedObj`类的`__new__`函数返回了一个`int`值。

3. 只有在`__new__`返回一个新创建属于该类的实例时当前类的`__init__`才会被调用。如下面例子所示：
```
class sample(object):
    def __str__(self):
        print("sample")

class example(object):
    def __new__(cls):
        print("__new__ is called")
        return sample()

    def __init__(self):
        print("__init__ is called")

example()
```
输出结果为：
```
__new__ is called
sample
```