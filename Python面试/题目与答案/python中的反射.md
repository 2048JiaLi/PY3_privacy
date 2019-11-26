在程序开发中，常常会遇到这样的需求：在执行对象中的某个方法，或者在调用对象的某个变量，但是由于一些原因，我们无法确定或者并不知道该方法或者变量是否存在，这时我们需要一个特殊的方法或者机制来访问或操作该未知的方法或变量，这种机制就被称之为**反射**。
> https://blog.csdn.net/perfect1t/article/details/80825372

## 问：说说Python中的反射？

## 答：在反射机制就是在运行时，动态的确定对象的类型，并可以通过字符串调用对象属性、方法、导入模块，是一种基于字符串的事件驱动。通过字符串的形式，去模块寻找指定函数，并执行。利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员。

Python是一门解释型语言，因此对于反射机制支持很好。在Python中支持反射机制的函数有`getattr()`、`setattr()`、`delattr()`、`exec()`、`eval()`、`__import__`，这些函数都可以执行字符串。




### 在 Python 中，反射的实现很简单，主要通过以下 4 个函数：

1. getattr()
   - 描述
   getattr() 函数用于返回一个对象属性值。

   - 语法   
   `getattr(object, name[, default])`

   - 参数
      - object -- 对象。
      - name -- 字符串，对象属性。
      - default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
   
   - 返回值
   返回对象属性值。

   - 实例
   ```
   >>>class A(object):
   ...     bar = 1
   ... 
   >>> a = A()
   >>> getattr(a, 'bar')        # 获取属性 bar 值
   1
   >>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
   Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
   AttributeError: 'A' object has no attribute 'bar2'
   >>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
   3
   >>>
   ```


2. hasattr()
   - 描述
   hasattr() 函数用于判断对象是否包含对应的属性。

   - 语法   
   ```hasattr(object, name)```

   - 参数
      - object -- 对象。
      - name -- 字符串，属性名。

   - 返回值
   如果对象有该属性返回 True，否则返回 False。

   - 实例
   ```
   class Coordinate:
       x = 10
       y = -5
       z = 0
 
   point1 = Coordinate() 
   print(hasattr(point1, 'x'))
   print(hasattr(point1, 'y'))
   print(hasattr(point1, 'z'))
   print(hasattr(point1, 'no'))  # 没有该属性
   ```
   输出结果：
   ```
   True
   True
   True
   False
   ```

3. setattr()
   - 描述
   setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。

   - 语法   
   ```setattr(object, name, value)```

   - 参数
      - object -- 对象。
      - name -- 字符串，对象属性。
      - value -- 属性值。

   - 返回值
   无

   - 实例
   对已存在的属性进行赋值：
   ```
   >>>class A(object):
   ...     bar = 1
   ... 
   >>> a = A()
   >>> getattr(a, 'bar')          # 获取属性 bar 值
   1
   >>> setattr(a, 'bar', 5)       # 设置属性 bar 值
   >>> a.bar
   5
   ```
   如果属性不存在会创建一个新的对象属性，并对属性赋值：
   ```
   >>>class A():
   ...     name = "runoob"
   ... 
   >>> a = A()
   >>> setattr(a, "age", 28)
   >>> print(a.age)
   28
   >>>
   ```

4. delattr()
   - 描述
   delattr 函数用于删除属性。

   > `delattr(x, 'foobar')` 相等于 `del x.foobar`。

   - 语法   
   ```delattr(object, name)```

   - 参数
      - object -- 对象。
      - name -- 必须是对象的属性。
   
   - 返回值
   无

   - 实例
   ```
   class Coordinate:
       x = 10
       y = -5
       z = 0
 
   point1 = Coordinate() 
 
   print('x = ',point1.x)
   print('y = ',point1.y)
   print('z = ',point1.z)
 
   delattr(Coordinate, 'z')
 
   print('--删除 z 属性后--')
   print('x = ',point1.x)
   print('y = ',point1.y)
 
   # 触发错误
   print('z = ',point1.z)
   ```
   输出结果
   ```
   ('x = ', 10)
   ('y = ', -5)
   ('z = ', 0)
   --删除 z 属性后--
   ('x = ', 10)
   ('y = ', -5)
   Traceback (most recent call last):
     File "test.py", line 22, in <module>
       print('z = ',point1.z)
   AttributeError: Coordinate instance has no attribute 'z'
   ```