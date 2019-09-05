+ ***ls [OPTION] [FILE]*** 显示目录内容
   + ***-a*** 显示以 . 开头的文件（root 用户默认带此参数
   + ***-l*** 列出文件具体信息

+ ***cp [OPTION] SOURCE DIRECTORY*** 复制文件
   + ***-f*** 强制
   + ***-p*** 复制属性
   + ***-i*** 文件存在时再次确认
   + ***-r*** 递归复制

+ ***cd [dir]*** 进入目录

+ ***mv [OPTION] SOURCE DIRECTORY*** 移动文件 / 重命名
   + ***-f*** 强制
   + ***-i*** 文件存在时再次确认

+ ***rm [OPTION] FILE*** 删除文件
   + ***-f*** 强制
   + ***-i*** 再次确认
   + ***-r*** 递归删除

+ ***pwd*** 查看当前目录路径

+ ***vim [OPTION] FILE*** vim文本编辑器，只在此写出基本用法   
```
在命令模式（即进入 vim 默认的模式）中按 i 或者 Ins 键进入插入模式   
插入模式中可以自由编辑文件。按 Esc 退出插入模式。   
命令模式中输入 :q! 不保存强制退出； :wq 保存并退出； :w 保存 ；/word 搜索 word，n 下一条符合的记录；
```
+ ***clear*** 清屏 / ***Ctrl + L***

+ ***alias [name]=[value]*** 指令别名   
```e.g. $ alias cls=’clear’```

+ ***UPDATE***：
   + ***wget [OPTION] [URL]*** 远程下载你懂的
   + ***-c***, –continue 继续下载上次未下载完的文件

+ ***passwd [LOGIN]*** 修改密码

+ ***tar [OPTION] [FILE]*** tar解压
   + ***-x***, –extract, –get extract files from an archive
   + ***-v***, –verbose verbosely list files processed
   + ***-f***, –file=ARCHIVE use archive file or device ARCHIVE

+ ***unzip [-opts] file[.zip] [-d exdir]*** zip解压
   + ***-o*** 覆盖已存在文件
   + ***-d*** 指定解压缩到的目录

+ ***ps [options]*** 查询进程状态
   + ***-a*** all with tty, except session leaders
   + ***-u***, U, –user effective user id or name
   + ***x*** processes without controlling ttys   
```e.g. ps -aux | grep nginx 在所有进程中，查找nginx的进程```

+ ***kill [-n signum] pid*** 根据进程号杀死进程

+ ***top*** 查看程序的cpu，内存使用情况

+ ***free -m*** 查看内存，swap使用情况

+ ***netstat -ntl*** 查看端口占用情况
