> 使用git bash时最直接的方法是利用https链接克隆仓库

# *PY3_personal*

### [数据分析常用的Matplotlib图](https://mp.weixin.qq.com/s?__biz=MzU1MjYzNjQwOQ==&mid=2247486636&idx=2&sn=44ff6554408a5252bed8fd97bbcbfdf5&chksm=fbfe563acc89df2c36eedfd84671f4435994bb7509a025533c008d710f3da6de1335963184fa&mpshare=1&scene=23&srcid=&sharer_sharetime=1573120171389&sharer_shareid=146e00a5d117656b5e8159f8890e708c#rd)
### [爬虫](https://github.com/2048JiaLi/PY3_privacy/tree/master/%E7%88%AC%E8%99%AB)
### [面试](https://github.com/2048JiaLi/PY3_privacy/tree/master/Python%E9%9D%A2%E8%AF%95)
+ [python设计和历史常见问题](https://github.com/2048JiaLi/PY3_privacy/blob/master/python%E8%AE%BE%E8%AE%A1%E5%92%8C%E5%8E%86%E5%8F%B2%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98.md)
- [算法学习](./算法学习/readme.md)

### [Py3学习资源](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90.md)
+ [collection.nametuple具名元组](https://github.com/2048JiaLi/PY3_privacy/blob/master/namedtuple(%E5%85%B7%E5%90%8D%E5%85%83%E7%BB%84).md)
+ [re正则化符号](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.md)
+ [可视化](https://github.com/2048JiaLi/PY3_privacy/tree/master/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96)
+ [简短的代码片段，直接可用](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E7%AE%80%E7%9F%AD%E4%BB%A3%E7%A0%81%E7%89%87%E6%AE%B5.md)

___
### [Linux Shell常用命令](https://github.com/2048JiaLi/PY3_privacy/blob/master/LinuxShell%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.md)
### [Vim指令](https://github.com/2048JiaLi/PY3_privacy/blob/master/Vim%E6%8C%87%E4%BB%A4.md)
### [MarkDown语法详解](https://blog.csdn.net/u014061630/article/details/81359144)
### [vs code操作github](https://blog.csdn.net/jiangyu1013/article/details/84031418)
### [Git命令](https://www.cnblogs.com/chris0710/p/8925977.html)
+ 通过Git提交更新代码的两种方法
   + ***git push origin 当前分支***    当前分支为master直接更新仓库，为分支dev需执行合并
```
pull：是下拉代码，相等于将远程的代码下载到你本地，与你本地的代码合并
push：是推代码，将你的代码上传到远程的动作
完整的流程是：

第一种方法：（简单易懂）

1、git add .（后面有一个点，意思是将你本地所有修改了的文件添加到暂存区）
2、git commit -m""(引号里面是你的介绍，就是你的这次的提交是什么内容，便于你以后查看，这个是将索引的当前内容与描述更改的用户和日志消息一起存储在新的提交中)
3、git pull origin master 这是下拉代码，将远程最新的代码先跟你本地的代码合并一下，如果确定远程没有更新，可以不用这个，最好是每次都执行以下，完成之后打开代码查看有没有冲突，并解决，如果有冲突解决完成以后再次执行1跟2的操作
4、git push origin master 将代码推至远程就可以了

 

第二种方法：

1、git stash （这是将本地代码回滚值至上一次提交的时候，就是没有你新改的代码）
2、git pull origin master（将远程的拉下来）
3、git stash pop（将第一步回滚的代码释放出来，相等于将你修改的代码与下拉的代码合并）
然后解决冲突，你本地的代码将会是最新的代码
4、git add .
5、git commit -m""
6、git push origin master
这几步将代码推至了远程
最后再git pull origin master 一下，确保远程的全部拉下来，有的你刚提交完有人又提交了，你再拉一下会避免比的不是最新的问题
```
