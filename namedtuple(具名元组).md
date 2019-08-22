### Python元组的升级版本 -- namedtuple(具名元组)
**因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，所以在这里引入了 *collections.namedtuple* 这个工厂函数，来构造一个带字段名的元组。具名元组的实例和普通元组消耗的内存一样多，因为字段名都被存在对应的类里面。这个类跟普通的对象实例比起来也要小一些，因为 Python 不会用 *__dict__* 来存放这些实例的属性。**
___
### *namedtuple*对象的定义如以下格式：
`collections.namedtuple(typename, field_names, verbose=False, rename=False)`

**返回一个具名元组子类 typename，其中参数的意义如下：**
+ typename：元组名称
+ field_names: 元组中元素的名称
+ rename: 如果元素名称中含有 python 的关键字，则必须设置为 rename=True
+ verbose: 默认就好

___
#### 下面是具名元组实例化的方法：
```
import collections

# 两种方法来给 namedtuple 定义方法名, 且两种方法效果相同
#User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', 'name age id')
user = User('tester', '22', '464643123')

user
>>>User(name='tester', age='22', id='464643123')
```
***collections.namedtuple('User', 'name age id')*** 创建一个具名元组，需要**两个参数**，一个是类名，另一个是类的各个字段名。后者可以是有多个字符串组成的**可迭代对象**，或者是有空格分隔开的字段名组成的**字符串**（比如本示例）。

**具名元组可以通过字段名或者位置来获取一个字段的信息:**
```
user.name
>>>'tester'
user.age
>>>'22'
user.id
>>>'464643123'
```
**具名元组的特有属性:**
+ 类属性 ***_fields***：包含这个类所有字段名的元组 
+ 类方法 ***_make(iterable)***：接受一个可迭代对象来生产这个类的实例 
+ 实例方法 ***_asdict()***：把具名元组以 *collections.OrdereDict* 的形式返回，可以利用它来把元组里的信息友好的展示出来
