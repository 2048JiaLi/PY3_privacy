## 问：说说Python中的类型转换有哪些？

## 答：在Python处理数据时，不可避免的要使用数据类型之间的转换。简单的诸如int、float、string之间的转换；更有数组array、列表list之间的转换。

| 函数 | 描述 |
| :-:  | :-:  |
| int(x [,base]) | 将x转换为一个整数 |
| long(x [,base]) | 将x转换为一个长整数 |
| float(x) | 将x转换到一个浮点数 |
| complex(real [,imag]) | 创建一个复数 |
| str(x) | 将对象 x 转换为字符串 |
| repr(x) | 将对象 x 转换为表达式字符串 |
| eval(str) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| tuple(s) | 将序列 s 转换为一个元组 |
| list(s) | 将序列 s 转换为一个列表 |
| set(s) | 转换为可变集合 |
| dict(d) | 创建一个字典。d 必须是一个序列 (key,value)元组。 |
| frozenset(s) | 转换为不可变集合 |
| chr(x) | 将一个整数转换为一个字符 |
| unichr(x) | 将一个整数转换为Unicode字符 |
| ord(x) | 将一个字符转换为它的整数值 |
| hex(x) | 将一个整数转换为一个十六进制字符串 |
| oct(x) | 将一个整数转换为一个八进制字符串 |

> 函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式。详见 https://www.cnblogs.com/bingabcd/p/6664216.html