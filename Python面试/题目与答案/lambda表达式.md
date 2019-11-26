## 问：说说Python中的lambda表达式？

## 答：在Python中lambda表达式也叫匿名函数，即函数没有具体的名称。

> 注 ： [PEP8](https://github.com/2048JiaLi/my-learning-100days/blob/master/PEP8.md)介绍：使用def语句而不是使用赋值语句将lambda表达式绑定到标识符上。
```
Yes:
def f(x): return 2*x

No:
f = lambda x: 2*x
```

lambda表达式是Python中一类特殊的定义函数的形式，使用它可以定义一个匿名函数。与其它语言不同，Python的lambda表达式的函数体只能有单独的一条语句，也就是返回值表达式语句。

lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用 。lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，就重新定义一个函数了。lambda 表达式允许在一行代码中创建一个函数并传递。

### 优点和缺点: 一方面，Lambda函数的减少了代码的行数，方便又简洁。另一方面，Lambda表达式有诸多限制，不能使用复杂逻辑。

lambda 表达式的两个要点：

1. lambda 表达式必须使用 lambda 关键字定义。
2. 在 lambda 关键字之后、冒号左边为参数列表，可不带参数，也可有多个参数。若有多个参数，则参数间用逗号隔开，冒号右边为 lambda 表达式的返回值。
