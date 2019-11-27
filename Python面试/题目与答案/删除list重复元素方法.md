## 问：说说Python删除list里的重复元素有几种方法？

## 答：在Python中主要有5种方式。

1. 使用set函数
```
numList = [1,1,2,3,4,5,4]
print(list(set(numList)))
#[1, 2, 3, 4, 5]
```

2. 先把list重新排序，然后从list的最后开始扫描
```
a = [1, 2, 4, 2, 4, 5,]
a.sort()
last = a[-1]
for i in range(len(a) - 2, -1, -1):
    if last == a[i]:
        del a[i]
    else:
        last = a[i]
print(a) #[1, 2, 4, 5]
```

3. 使用字典函数
```
a = [1,2,4,2,4,]
b = {}
b = b.fromkeys(a)
c = list(b.keys())

print(c) #[1, 2, 4]
```
[Python 字典(Dictionary) fromkeys()方法](https://www.runoob.com/python/att-dictionary-fromkeys.html)

- 描述
Python 字典 `fromkeys()` 函数用于创建一个新字典，以序列 `seq` 中元素做字典的键，`value` 为字典所有键对应的初始值

- 语法
```dict.fromkeys(seq[, value])```

- 参数
   - seq -- 字典键值列表。
   - value -- 可选参数, 设置键序列（seq）的值。

- 返回值
该方法返回一个新字典。

- 实例
```
seq = ('Google', 'Runoob', 'Taobao')
 
dict = dict.fromkeys(seq)
print("新字典为 : %s" %  str(dict))
 
dict = dict.fromkeys(seq, 10)
print("新字典为 : %s" %  str(dict))
```
以上实例输出结果为：
```
新字典为 : {'Google': None, 'Taobao': None, 'Runoob': None}
新字典为 : {'Google': 10, 'Taobao': 10, 'Runoob': 10}
```

4. append方式 - 构造一个新的list
```
def delList(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1
print(delList([1, 2, 2, 3, 3, 4, 5])) #[1, 2, 3, 4, 5]
```

5. count + remove方式
```
def delList(L):
    for i in L:
        if L.count(i) != 1:
            for x in range((L.count(i) - 1)):
                L.remove(i)
    return L
print(delList([1, 2, 2, 3, 3, 4]))#[1, 2, 3, 4]
```