## PEP是什么？

PEP的全称是Python Enhancement Proposals，其中Enhancement是增强改进的意思，Proposals则可译为提案或建议书，所以合起来，比较常见的翻译是Python增强提案或Python改进建议书。

PEP的官网是：https://www.python.org/dev/peps/， 这也就是PEP 0 的地址。其它PEP的地址是将编号拼接在后面，例如：https://www.python.org/dev/peps/pep-0020/ 就是PEP 20 的链接，以此类推。

第一个PEP诞生于2000年。

官方将PEP分成三类:
   - I - Informational PEP
   信息类：这类PEP就是提供信息，有告知类信息，也有指导类信息等等。
   > 例如PEP 20（The Zen of Python，即著名的Python之禅）、PEP 404 (Python 2.8 Un-release Schedule，即宣告不会有Python2.8版本)

   - P - Process PEP
   流程类：这类PEP主要是Python本身之外的周边信息。
   > 例如PEP 1（PEP Purpose and Guidelines，即关于PEP的指南）、PEP 347（Migrating the Python CVS to Subversion，即关于迁移Python代码仓）。

   - S - Standards Track PEP
   标准类：这类PEP主要描述了Python的新功能和新实践（implementation），是数量最多的提案。
   > 例如f-string方式，它出自PEP 498（Literal String Interpolation，字面字符串插值）。

每个PEP最初都是一个草案（Draft），随后会经历一个过程，因此也就出现了不同的状态。以下是一个流程图：

![image](./image/PEP流程图.png)

```
A – Accepted (Standards Track only) or Active proposal 已接受（仅限标准跟踪）或有效提案

D – Deferred proposal 延期提案

F – Final proposal 最终提案

P – Provisional proposal 暂定提案

R – Rejected proposal 被否决的提案

S – Superseded proposal 被取代的提案

W – Withdrawn proposal 撤回提案
```

在PEP 0（Index of Python Enhancement Proposals (PEPs)）里，官方列举了所有的PEP，你可以按序号、按类型以及按状态进行检索。而在PEP 1（PEP Purpose and Guidelines）里，官方详细说明了PEP的意图、如何提交PEP、如何修复和更新PEP、以及PEP评审的机制等等。

## 为什么要读PEP？

1. 了解Python有哪些特性，它们与其它语言特性的差异，为什么要设计这些特性，是怎么设计的，怎样更好地运用它们；

2. 跟进社区动态，获知业内的最佳实践方案，调整学习方向，改进工作业务的内容；

3. 参与热点议题讨论，或者提交新的PEP，为Python社区贡献力量。

> PEP提案是深入了解Python的途径，是真正掌握Python语言的一把钥匙，也是得心应手使用Python的一本指南。

## 哪些PEP是必读的？
推荐阅读：
```
PEP 0 -- Index of Python Enhancement Proposals
PEP 7 -- Style Guide for C Code，C扩展
PEP 8 -- Style Guide for Python Code，编码规范（必读）
PEP 20 -- The Zen of Python，Python之禅
PEP 202 -- List Comprehensions，列表生成式
PEP 274 -- Dict Comprehensions，字典生成式
PEP 234 -- Iterators，迭代器
PEP 257 -- Docstring Conventions，文档注释规范
PEP 279 -- The enumerate() built-in function，enumerate枚举
PEP 282 -- A Logging System，日志模块
PEP 285 -- Adding a bool type，布尔值（建议阅读《Python对象的身份迷思：从全体公民到万物皆数》）
PEP 289 -- Generator Expressions，生成器表达式
PEP 318 -- Decorators for Functions and Methods，装饰器
PEP 342 -- Coroutines via Enhanced Generators，协程
PEP 343 -- The "with" Statement，with语句
PEP 380 -- Syntax for Delegating to a Subgenerator，yield from语法
PEP 405 -- Python Virtual Environments，虚拟环境
PEP 471 -- os.scandir() function，遍历目录
PEP 484 -- Type Hints，类型约束
PEP 492 -- Coroutines with async and await syntax，async/await语法
PEP 498 -- Literal String Interpolation Python，字符串插值
PEP 525 -- Asynchronous Generators，异步生成器
PEP 572 -- Assignment Expressions，表达式内赋值（最争议）
PEP 3105 -- Make print a function，print改为函数
PEP 3115 -- Metaclasses in Python 3000，元类
PEP 3120 -- Using UTF-8 as the default source encoding
PEP 3333 -- Python Web Server Gateway Interface v1.0.1，Web开发
PEP 8000 -- Python Language Governance Proposal Overview，GvR老爹推出决策层后，事关新决策方案
```

> 关于PEP，知乎上有两个问题，推荐大家关注：[哪些PEP值得阅读](https://dwz.cn/7CHMBlLu)，[如何看待PEP 572](https://dwz.cn/L46jpzMB)。


## PEP的中文翻译
- [PEP8](https://dwz.cn/W01HexFD)
- [PEP257](https://dwz.cn/JLctlNLC)
- [PEP328](https://dwz.cn/4vCQJpEP)
- [PEP333](https://dwz.cn/TAXIZdzc)
- [PEP484](https://dwz.cn/dSLZgg5B)
- [PEP492](http://t.cn/EALeaL0)
- [PEP541](https://dwz.cn/ce98vc27)
- [PEP3107](http://suo.im/4xFESR)
- [PEP3333](https://dwz.cn/si3xylgw)