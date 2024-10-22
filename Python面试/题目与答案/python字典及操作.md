## 问：说说Python字典以及基本操作？

## 答：字典是 Python 提供的一种常用的数据结构，主要用于存放**具有映射关系的数据**。

比如保存某班同学的成绩单数据，张三：95分，李四：70分，王五：100分 ... ，因为姓名和成绩是有关联的，所以不能单独用两个列表来分别保存，这时候用字典来存储，再合适不过了。

字典是一种可变的容器模型，它是通过一组键（key）值（value）对组成，这种结构类型通常也被称为映射，或者叫关联数组，也有叫哈希表的。每个key-value之间用“:”隔开，每组用“,”分割，整个字典用“{}”括起来 ，格式如下所示：
```
dictionary = {key1 : value1, key2 : value2 }
```

定义字典时，键前值后，键必须唯一性，值可以不唯一，如果键有相同，值则取最后一个；

值可以是任何的数据类型，但是键必须是**不可变的数据类型**（数字、字符串、元组）。想要访问字典中的值，只需要将键放入方括号里，如果用字典里没有的键访问数据，会输出错误 

### 如何访问字典中的值？
想要访问字典中的值，只需要将键放入方括号里，如果用字典里没有的键访问数据，程序会输出错误，如下图所示 。
```
scores = {'张三': 89 ,'李四': 100 ,'王五': 79}

print(scores['张三']) # 通过key访问value ，输出：89

print(scores['老六']) # 输出 KeyError: '老六'
```

### 字典中值的如何增删改？
#### 增加 - 对不存在的key直接赋值
#### 删除 - `del`
#### 修改 - 对key重新赋值

### 常用方法
- **clear()** - 清空字典里的数据

- **copy()** - 拷贝（浅拷贝）一个字典里的数据

- **fromkeys()** - 使用给定的键建立字典，对应的值默认为“None”

- **get(key, default=None)** - 访问字典中对应的键里的值，如不存在该键返回default的值

- **items()** - 获取字典键值对数据，以列表形式返回

- **keys()** - 获取字典键的数据，以列表形式返回

- **values()** - 获取字典值的数据，以列表形式返回

- **setdefault(key, default=None)** - 和`get()`类似, 但如果键不存在于字典中，将会添加键并将值设为default

- **update(dict2)** - 把字典dict2的数据（键值对）更新到另一个字典中