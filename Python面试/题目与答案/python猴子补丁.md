## 问：说说Python中猴子补丁是什么？

## 答：在Ruby、Python等动态编程语言中，猴子补丁仅指在运行时动态改变类或模块，为的是将第三方代码打补丁在不按预期运行的bug或者feature上 。
在运行时动态修改模块、类或函数，通常是添加功能或修正缺陷。**猴子补丁在代码运行时内存中发挥作用，不会修改源码，因此只对当前运行的程序实例有效**。因为猴子补丁破坏了封装，而且容易导致程序与补丁代码的实现细节紧密耦合，所以被视为临时的变通方案，不是集成代码的推荐方式。

### 为什么名字叫猴子补丁？
网络上有两种解释

1. 一种解释，起源于Zope框架，大家在修正Zope的Bug的时候经常在程序后面追加更新部分，这些被称作是“杂牌军补丁(guerilla patch)”，后来guerilla就渐渐的写成了gorllia(猩猩)，再后来就写了monkey(猴子)。

2. 第二种解释是说由于这种方式将原来的代码弄乱了(messing with it)，在英文里叫monkeying about(顽皮的)，所以叫做Monkey Patch。

### monkey patch的应用场景
stackoverflow上有个比较热的例子，很多代码用到 import json，后来发现ujson性能更高，如果觉得把每个文件的import json 改成 import ujson as json成本较高，或者说想测试一下用ujson替换json是否符合预期，只需要在入口加上：
```
import json
import ujson

def monkey_patch_json():  
    json.__name__ = 'ujson'  
    json.dumps = ujson.dumps
    json.loads = ujson.loads

monkey_patch_json()
```

猴子补丁还可以在运行时动态增加模块的方法，这种场景也比较多，比如引用通用库里的一个模块，又想丰富模块的功能，除了继承之外也可以考虑用Monkey Patch。

[更多解释](https://stackoverflow.com/questions/5626193/what-is-monkey-patching)