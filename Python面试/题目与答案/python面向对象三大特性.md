## 问：说说Python面向对象三大特性?
## 答：Python是一门面向对象的语言。面向对象都有三大特性：封装、继承、多态。

### 三大特性

1. 封装
隐藏对象的属性和实现细节，仅对外提供公共访问方式。在python中用双下划线开头的方式将属性设置成私有的 。

> 好处：1. 将变化隔离；2. 便于使用；3. 提高复用性；4. 提高安全性。

2. 继承
继承是一种创建新类的方式，在python中，**新建的类可以继承一个或多个父类**，父类又可称为基类或超类，新建的类称为派生类或子类。即一个派生类继承基类的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。

例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系 。

python中类的继承分为：单继承和多继承
```
class ParentClass1: #定义父类

class ParentClass2: #定义父类

class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass

class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
```

3. 多态
一种事物的多种体现形式，函数的重写其实就是多态的一种体现 。Python中，多态指的是父类的引用指向子类的对象 。

实现多态的步骤：
   - 定义新的子类

   - 重写对应的父类方法

   - 使用子类的方法直接处理,不调用父类的方法

多态的好处：

   - 增加了程序的灵活性

   - 增加了程序可扩展性