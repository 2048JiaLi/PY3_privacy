### Python元组的升级版本 -- namedtuple(具名元组)
**因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，所以在这里引入了 *collections.namedtuple* 这个工厂函数，来构造一个带字段名的元组。具名元组的实例和普通元组消耗的内存一样多，因为字段名都被存在对应的类里面。这个类跟普通的对象实例比起来也要小一些，因为 Python 不会用 *__dict__* 来存放这些实例的属性。**
___
### *namedtuple*对象的定义如以下格式：
```collections.namedtuple(typename, field_names, verbose=False, rename=False) ```

**返回一个具名元组子类 typename，其中参数的意义如下：**
+ typename：元组名称
+ field_names: 元组中元素的名称
+ rename: 如果元素名称中含有 python 的关键字，则必须设置为 rename=True
+ verbose: 默认就好
