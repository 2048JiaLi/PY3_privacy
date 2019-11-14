## 问：说说Python中xrange和range的区别？

## 答：range()和xrange()都是在循环中使用，输出结果一样。

> range()返回的是一个list对象，而xrange返回的是一个**生成器对象**(xrange object)。
>
> xrange()则不会直接生成一个list，而是每次调用返回其中的一个值，内存空间使用极少。因而性能非常好，所以尽量用xrange吧。
>
> **在python3 中没有xrange，只有range。range和python2 中的xrange()一样。**

### 用法

1. range()
range 函数说明：`range([start,] stop[, step])`，根据start与stop指定的范围以及step设定的步长，生成一个序列。
> 起点是start，终点是stop，但不包含stop，公差是step。start和step是可选项，没给出start时，从0开始；没给出step时，默认公差为1。

```
>>> range(10) #起点是0，终点是10，但是不包括10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1,10) #起点是1，终点是10，但是不包括10
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1,10,2) #起点是1，终点是10，步长为2
[1, 3, 5, 7, 9]
>>> range(0,-10,-1) #起点是1，终点是10，步长为-1
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0,-10,1) #起点是0，终点是-10，终点为负数时，步长只能为负数，否则返回空
[]
>>> range(0) #起点是0，返回空列表
[]
>>> range(1,0) #起点大于终点，返回空列表
[]
```

2. xrange()
xrange与range类似，只是返回的是一个"xrange object"生成器对象，而非数组list。

```
>>> xrange(6)
xrange(6) # 注意：这里输出的和range就不同喽
>>> list(xrange(6))
[0, 1, 2, 3, 4, 5]
>>> xrange(1, 6)
xrange(1, 6)
>>> list(xrange(1, 6))
[1, 2, 3, 4, 5]
>>> xrange(0,6,2)
xrange(0, 6, 2)
>>> list(xrange(0, 6, 2))
[0, 2, 4]
```

都是在循环的时候用
```
for i in range(0, 100):
  print(i)
for i in xrange(0, 100):
  print(i)
```

> xrange()函数在Python3中已经取消。**在python3中**range()这种实现被移除了，保留了xrange()的实现，且将**xrange()重新命名成range()**。所以Python3不能使用xrange()，只能使用range()。