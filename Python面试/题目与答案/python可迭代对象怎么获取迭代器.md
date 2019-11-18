## 问：说说Python中可迭代对象怎么获取迭代器？

## 答：今天这个问题，需要看下面代码解析，再来说参考答案，这样理解的看面试题，对大家的学习更有帮助，千万别死记硬背，那样记不牢的。

列表来说迭代器的用法：
```
list = [1,2,3,4] # list是可迭代对象
lterator = iter(list) # 通过iter()方法取得list的迭代器
print(next(lterator)) # 1 通过next()获取下一个位置的值
print(next(lterator)) # 2
print(next(lterator)) # 3
print(next(lterator)) # 4

输出：
1
2
3
4
```
> 列表怎么可以有一个迭代器？

```
import collections
print(isinstance([1, 2, 3], collections.Iterable)) #isinstance(object,classinfo)内置函数可以判断一个对象是否是一个已知的类型
输出：
True
```

从上面代码可以知道，**可迭代对象都是collections模块里的Iterable类创建出来的实例**。你写一个列表，不是简单一个列表，其实它就是Iterable类创建的实例对象。点进Iterable的类看一下：
```
class Iterable(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod
    def __iter__(self):  # 注意点
        while False:
            yield None
```

原来由Iterable创建的对象，是有一个方法__iter__(self)的。这个方法就是返回一个迭代器的。所以，由Iterable类创建的实例对象，是可以拿出一个迭代器的。