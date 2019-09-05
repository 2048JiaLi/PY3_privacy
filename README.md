# *PY3_personal*

+ [collection.nametuple具名元组](https://github.com/2048JiaLi/PY3_privacy/blob/master/namedtuple(%E5%85%B7%E5%90%8D%E5%85%83%E7%BB%84).md)
+ [re正则化符号](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.md)
+ [可视化](https://github.com/2048JiaLi/PY3_privacy/tree/master/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96)

___
### [Linux Shell常用命令](https://github.com/2048JiaLi/PY3_privacy/blob/master/LinuxShell%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.md)
### [MarkDown语法详解](https://blog.csdn.net/u014061630/article/details/81359144)
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
