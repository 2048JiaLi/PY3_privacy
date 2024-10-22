## 问：说说提高Python运行效率的技巧？

## 答：提高python执行效率的10种方法如下

1. 使用局部变量
尽量使用局部变量代替全局变量：便于维护，提高性能并节省内存。

> 一方面可以提高程序性能，局部变量查找速度更快;另一方面可用简短标识符替代冗长的模块变量，提高可读性。

2. 使用较新的Python版本
Python已经更新了很多个版本，每个版本的Python都会包含优化内容，使其运行速度优于之前的版本，所以大家记得经常更新版本哦！

3. 先编译后调用
使用eval()、exec()函数执行代码时，最好调用代码对象(提前通过compile()函数编译成字节码)，而不是直接调用str，可以避免多次执行重复编译过程，提高程序性能。

正则表达式模式匹配也类似，也最好先将正则表达式模式编译成regex对象(通过re.complie()函数)，然后再执行比较和匹配。
```
import re

def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')
    x = regex.findall(content)
    print(x)


if __name__ == '__main__':
    main()

>>> ['Hello', 'from', 'Chongqing', 'montain', 'to', 'you']
```

4. 采用生成器表达式替代列表解析
列表解析会产生整个列表，对大量数据的迭代会产生负面效应。而生成器表达式则不会，其不会真正创建列表，而是返回一个生成器，在需要时产生一个值(延迟计算)，对内存更加友好。

5. 关键代码使用外部功能包
使用 C/C++ 或机器语言的外部功能包处理时间敏感任务，可以有效提高应用的运行效率。这些功能包往往依附于特定的平台，因此你要根据自己所用的平台选择合适的功能包 。比如下面四个功能包：Cython、Pylnlne、PyPy、Pyrex 。

6. 在排序时使用键
Python 含有许多古老的排序规则，这些规则在你创建定制的排序方法时会占用很多时间，而这些排序方法运行时也会拖延程序实际的运行速度。最佳的排序方法其实是尽可能多地使用键和内置的 `sort()` 方法。

7. 优化算法时间
算法的时间复杂度对程序的执行效率影响最大，在Python中可以通过选择合适的数据结构来优化时间复杂度，如**list和set查找某一个元素的时间复杂度分别是O(n)和O(1)**。不同的场景有不同的优化方式，总得来说，一般有分治，分支界限，贪心，动态规划等思想。

例如：set的用法

set的union，intersection，difference操作要比list的迭代要快。因此如果涉及到求list交集，并集或者差的问题可以转换为set来操作。

8. 循环优化
每种编程语言都会强调需要优化循环。当使用Python的时候，你可以依靠大量的技巧使得循环运行得更快。

- 技巧 1：减少循环内部不必要的计算

- 技巧 2：嵌套循环中，尽量减少内层循环的计算

- 技巧 3：尽量使用局部变量

- 技巧 4：使用 join() 连接字符串

9. 交叉编译你的应用
计算机其实并不理解用来创建现代应用程序的编程语言，计算机理解的是机器语言。所以我们可以用Python语言编写应用，再以C++这样的语言运行你的应用，这在运行的角度来说，是可行的。

> Nuitka是一款有趣的交叉编译器，能将你的Python代码转化成C++代码。这样，你就可以在native模式下执行自己的应用，而无需依赖于解释器程序。你会发现自己的应用运行效率有了较大的提高，但是这会因平台和任务的差异而有所不同。

10. 充分利用多核CPU的优势
因为GIL的存在，Python很难充分利用多核CPU的优势。但是，可以通过内置的模块multiprocessing实现下面几种并行模式：

   - 多进程并行编程
   对于CPU密集型的程序，可以使用multiprocessing的Process,Pool等封装好的类，通过多进程的方式实现并行计算。但是因为进程中的通信成本比较大，对于进程之间需要大量数据交互的程序效率未必有大的提高

   - 多线程并行编程
   对于IO密集型的程序，multiprocessing.dummy模块使用multiprocessing的接口封装threading，使得多线程编程也变得非常轻松(比如可以使用Pool的map接口，简洁高效)。分布式：multiprocessing中的Managers类提供了可以在不同进程之共享数据的方式，可以在此基础上开发出分布式的程序。 不同的业务场景可以选择其中的一种或几种的组合实现程序性能的优化。