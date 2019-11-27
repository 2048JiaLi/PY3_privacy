## 问：说说Python中的`help()`和`dir()`函数？

## 答：在Python中`help()`和`dir()`这两个函数都可以从Python解释器直接访问，并用于查看内置函数的合并转储。

- `help()`函数：`help()`函数用于显示文档字符串，还可以查看与模块，关键字，属性等相关的使用信息。

- `dir()`函数：`dir()`函数可以列出指定类或模块包含的全部内容（包括函数、方法、类、变量等）

### 用法
1. 如果希望查看某个查看函数、方法的用法或模块用途的详细说明，则可使用 `help()` 函数。例如，在交互式解释器中输入如下命令：
```
import copy
print(help(copy.copy))

#输出结果：
Help on function copy in module copy:
copy(x)
    Shallow copy operation on arbitrary Python objects.
    See the module's __doc__ string for more info.
None
```

2. 要查看字符串变量（它的类型是 `str` 类型）所能调用的全部内容，可以在交互式解释器中输入如下命令：`dir(str)`
```
>>> dir(str)

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
上面列出了字符串类型（str）提供的所有方法，其中以“\_”开头、“\_”结尾的方法被约定成私有方法，不希望被外部直接调用。