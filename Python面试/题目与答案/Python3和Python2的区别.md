## 问：谈谈Python3 和 Python2 的区别？
## 答：Python3跟Python2比，语法上就有很多区别，都需要特别注意，下面给大家列举几个常见的 。

### Python3和Python2相比:
1. Python3去除print语句，加入print()函数实现相同的功能。

2. Python2 中符号`/`的结果是整型，Python3 中是浮点类型。

3. **字符串存储的区别**。python2中 字符串以 8-bit 字符串存储，python3中字符串以 16-bit Unicode 字符串存储。存储格式得到了升级。

4. **xrange与range**。python2中用xrange ，python3中用range。如：python2中的 xrange( 0, 4 ) 改为python3中的range(0,4)。

5. 键盘**输入**的区别。从键盘录入一个字符串，python2中是 raw_input( "hello world" )，python3则是 input( "hello world" )。

6. **元类的声明**。Python2 中声明元类：`_metaclass_ = MetaClass`，然而在Python3 中声明元类：`class newclass(metaclass=MetaClass)：pass`。