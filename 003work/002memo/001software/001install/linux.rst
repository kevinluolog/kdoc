*******************
gramma and template
*******************

.. contents:: contents
.. section-numbering::

网络资源地址
=================

`Linux基础知识——Linux常用命令大全 <https://yq.aliyun.com/articles/681643>`__

`Linux命令大全 <https://man.linuxde.net/>`__


Linux命令
=============

`Linux命令 <https://www.cnblogs.com/ftl1012/tag/Linux%E5%91%BD%E4%BB%A4/>`__

wget
----

`Linux wget命令详解 <https://www.cnblogs.com/ftl1012/p/9265699.html>`__

`Linux命令 <https://www.cnblogs.com/ftl1012/tag/Linux%E5%91%BD%E4%BB%A4/>`__

wget是一个下载文件的工具，它用在命令行下。

使用wget -O下载并以不同的文件名保存(-O：下载文件到对应目录，并且修改文件名称)

::

  wget -O wordpress.zip http://www.minjieren.com/download.aspx?id=1080
  wget https://github.com/jgm/pandoc/releases/download/1.17.1/pandoc-1.17.1-2-amd64.deb

使用wget -b后台下载

::

  wget -b <a href="http://www.minjieren.com/wordpress-3.1-zh_CN.zip">http://www.minjieren.com/wordpress-3.1-zh_CN.zip</a>

  备注： 你可以使用以下命令来察看下载进度：tail -f wget-log

利用-spider: 模拟下载，不会下载，只是会检查是否网站是否好着

::

  wget --spider  www.baidu.com #不下载任何文件

gsub函数
----------------

gsub函数则使得在所有正则表达式被匹配的时候都发生替换

::

  gsub(regular expression, subsitution string, target string);
  简称 gsub（r,s,t)

sub和gsub的区别
---------------------

sub匹配第一次出现的符合模式的字符串，相当于 sed 's//' 。
gsub匹配所有的符合模式的字符串，相当于 sed 's//g' 。
例如：

::

  awk '{sub(/Mac/,"Macintosh");print}' urfile 用Macintosh替换Mac
  awk '{sub(/Mac/,"MacIntosh",$1); print}' file 第一个域内用

Macintosh替换Mac
把上面sub换成gsub就表示在满足条件得域里面替换所有的字符。

awk的sub函数用法：

sub函数匹配指定域/记录中最大、最靠左边的子字符串的正则表达式，并用替换字符串替换这些字符串。如果没有指定目标字符串就默认使用整个记录。替换只发生在第一次匹配的时候。格式如下：

::

  sub (regular expression, substitution string):
  sub (regular expression, substitution string, target string)

实例：

::

  $ awk '{ sub(/test/, "mytest"); print }' testfile
  $ awk '{ sub(/test/, "mytest", $1); print }' testfile

第一个例子在整个记录中匹配，替换只发生在第一次匹配发生的时候。
第二个例子在整个记录的第一个域中进行匹配，替换只发生在第一次匹配发生的时候。

如要在整个文件中进行匹配需要用到gsub



awk gawk
-----------

`Linux awk命令详解 <https://www.cnblogs.com/ftl1012/p/9250541.html>`__

`linux gawk命令 <https://blog.csdn.net/believexfr/article/details/78010117>`__

`LinuxShell编程之gawk详解 <https://blog.51cto.com/13706064/2176615>`__


awk是一个强大的文本分析工具，相对于grep的查找，sed的编辑，awk在其对数据分析并生成报告时，显得尤为强大。简单来说awk就是把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行各种分析处理。

使用方法   ： awk '{pattern + action}' {filenames}

尽管操作可能会很复杂，但语法总是这样，其中 pattern 表示 AWK 在数据中查找的内容，而 action 是在找到匹配内容时所执行的一系列命令。花括号（{}）不需要在程序中始终出现，但它们用于根据特定的模式对一系列指令进行分组。 pattern就是要表示的正则表达式，用斜杠括起来。

awk语言的最基本功能是在文件或者字符串中基于指定规则浏览和抽取信息，awk抽取信息后，才能进行其他文本操作。完整的awk脚本通常用来格式化文本文件中的信息。通常，awk是以文件的一行为处理单位的。awk每接收文件的一行，然后执行相应的命令，来处理文本。

gawk命令格式

Usage: gawk [POSIX or GNU styleoptions] -f progfile [--] file ...

Usage: gawk [POSIX or GNU styleoptions] [--] 'program' file ...

gawk选项

+--------------+--------------------------------------+
| -F fs        | 指定描绘一行中数据字段的文件分隔符   |
+==============+======================================+
| -f file      | 指定读取程序的文件名                 |
+--------------+--------------------------------------+
| -v var=value | 定义gawk程序中使用的变量和默认值     |
+--------------+--------------------------------------+
| -mf N        | 指定数据文件中要处理的字段的最大数目 |
+--------------+--------------------------------------+
| -mr N        | 指定数据文件中的最大记录大小         |
+--------------+--------------------------------------+
| -W keyword   | 指定gawk的兼容模式或警告级别         |
+--------------+--------------------------------------+

gawk的主要功能之一是其处理文本文件中数据的能力。它通过自动将变量分配给每行中的每个数据元素实现这一功能。默认情况下，gawk将下面的变量分配给在文本行中检测到的每个数据字段：

+----+------------------------------+
| $0 | 表示整行文本                 |
+====+==============================+
| $1 | 表示文本行中的第一个数据字段 |
+----+------------------------------+
| $2 | 表示文本行中的第二个数据字段 |
+----+------------------------------+
| $n | 表示文本行中的第n个数据字段  |
+----+------------------------------+

各数据字段依据文本行中的字段分隔符确定。gawk读取一行文本时，使用定义的字段分隔符描述各数据字段。gawk的默认字段分隔符是任意空白字符（如制表符或空格符）


find
-----------

`Linux-find命令详解 <https://blog.csdn.net/l_liangkk/article/details/81294260>`__


在目录结构中搜索文件，并执行指定的操作。Linux下find命令提供了相当多的查找条件，功能很强大

find命令格式：

::

  find path -option 【-print】 【-exec -ok |xargs |grep】 【command {} \;】

Linux下find命令在目录结构中搜索文件，并执行指定的操作。Linux下find命令提供了相当多的查找条件，功能很强大
find常见命令参数

命令选项：
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   -name   按照文件名查找文件。
   -perm   按照文件权限来查找文件。
   -user   按照文件属主来查找文件。
   -group  按照文件所属的组来查找文件。
   -mtime -n +n 按照文件的更改时间来查找文件 【-7 7天之内 +7 7天前】
   -nogroup  查找无效属组的文件，即该文件所属的组在/etc/groups中不存在。
   -nouser  查找无效属主的文件，即该文件的属主在/etc/passwd中不存在。
   -newer file1 ! file2 查找更改时间比文件file1新但比文件file2旧的文件。
   -type  查找某一类型的文件，诸如：
            b - 块设备文件。
            d - 目录。
            c - 字符设备文件。
            p - 管道文件。
            l - 符号链接文件。
            f - 普通文件。
   -size n：[c] 查找文件长度为n块的文件，带有c表示文件长度以字节计。
   -depth：在查找文件时，首先查找当前目录中的文件，然后再在其子目录中查找。
   -follow：如果find命令遇到符号链接文件，就跟踪至链接所指向的文件。
   另外,下面三个的区别:
   -amin n    查找系统中最后N分钟访问的文件
   -atime n   查找系统中最后n*24小时访问的文件
   -cmin n    查找系统中最后N分钟被改变文件状态的文件
   -ctime n   查找系统中最后n*24小时被改变文件状态的文件
   -mmin n    查找系统中最后N分钟被改变文件数据的文件
   -mtime n   查找系统中最后n*24小时被改变文件数据的文件

常用的命令展示
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

查找普通文件/目录
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /home/omd -type f  (普通文件)
   find /home/omd -type d  (查询目录)

只显示1级目录文件且过滤自身
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find ./ -maxdepth 1  -type d  ! -name "hhh"  

查找一天内被访问过(access)的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /home/omd/ -atime -1 -type f 

查询inode相同的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::
   find / -inum inode数字  

除了某个文件以为，其余的均删除
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::
   find /home/omd/ -type f ! -name h.txt  | xargs  rm –f  
   ls | grep -v "h.txt" |xargs rm -rf (与上面类似，删除除了某个文件外的所有文件)

删除目录下所有文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /tmp/ -type f -exec rm -rf {} \;
   find /tmp/ -type f | xargs rm -rf

查看当前路径下所有文件的信息：
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /tmp/ -type f ! -name a |xargs rm –rf
   find ./ -type f -exec file {} \;
 
查找指定时间内修改过的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   # 当前路径下访问文件超过2分钟文件
   find ./ -amin +2
   # 当前路径下访问文件刚好2分钟的文件
   find ./ -amin 2
   find ./ -cmin +2
   find ./ -mmin +2
   find ./ -mtime +2
   find ./ -ctime +2
   find ./ -mtime +2
   find ./ -ctime +2 
   find / -ctime  +20  最近修改文件时间20分钟以前
   find / -mtime  +7   修改文件为7天之前的(最重要)
   find / -mtime  7    修改文件为第7天，就是往前推7天
   find / -mtime  -7   修改文件为7天之内的

按照目录或文件的权限来查找文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /opt -perm 777

按大小查找文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find / -size +10M  |sort 【查找大于10M的文件】
   find / -size -10M  |sort 【查找小于10M的文件】
   find / -size 10M   |sort  【查找10M的文件】
 
在test目录下查找不在test4子目录之内的所有文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find ./test -path "test/test4" -prune -o -print
   【可以使用-prune选项来指出需要忽略的目录。在使用-prune选项时要当心，因为如果你同时使用了-depth选项，那么-prune选项就会被find命令忽略】

查找比yum.log 但不比hhh.txt新的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   [root@localhost ftl]# find / newer /var/log/yum.log ! -newer ./hhh.txt
 
查找更改时间在比log2012.log文件新的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find ./ -newer log2012.log

在当前目录下查找文件长度大于1 M字节的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find ./ -size +1000000c –print
   find ./ –size +1M -print

在/home/apache目录下查找文件长度恰好为100字节的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   find /home/apache -size 100c -print

在当前目录下查找长度超过10块的文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find . -size 10 –print

    
其他命令：
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /home/omd/ -name *.txt | while read line; do cp $line /home/omd/h;done
   for name in `chkconfig | grep 3:on |awk '{print $1}'` ; do echo $name >> h.txt; done;
   find /home/omd/ -name *.txt | xargs -i cp {} /home/omd/h
   cat /home/omd/h/he.txt | while read line; do echo $line >> /home/omd/h.txt ; done;
   cat /home/omd/h.txt | awk 'BEGIN{print "Name "} {print $1}'
   cat /home/omd/h.txt | xargs -I {} cat {}
   find . -name  "*.txt" |xargs   sed -i 's/hhhh/\hHHh/g' 

find命令之execokprint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ls -l命令放在find命令的-exec选项中

::

   find . -type f -exec ls -l {} \; 【{}   花括号代表前面find查找出来的文件名】

在目录中查找更改时间在n日以前的文件并删除它们
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find ./ -mtime +10 -exec rm {} \;

在目录中查找更改时间在n日以前的文件并删除它们，在删除之前先给出提示
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find / -mtime +1 -a -name "*.log" -type f -ok cp {} /tmp/ftl \; 【-ok是安全模式，根exec效果同】

exec中使用grep命令
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find /etc -name "passwd*" -exec grep "root" {} \; 【过滤文件内容用】

查找文件移动到指定目录
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find . -name "*.log" -exec mv {} .. \;

用exec选项执行cp命令  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   find . -name "*.log" -exec cp {} test3 \;



Linux常用命令大全
=====================

`Linux基础知识——Linux常用命令大全 <https://yq.aliyun.com/articles/681643>`__


创建目录 mkdir
------------------
   
::
   
   作用：在当前目录下创建下一级目录，无法跨级创建
   
   常用参数
   -p 创建多级目录（跨级创建）
   -v 查看目录创建的过程（创建目录可视化）
   
   
删除文件 rmdir
------------------
   
::
   
   仅可以删除空白目录（不可以删除包含内容的目录）
   
创建文件 touch
------------------
   
::
   
   作用：创建空白文件
   
删除文件或目录 rm
------------------
   
::
   
   1、删除文件
   rm 文件名（删除时会询问是否删除）
   rm -f 文件名（强制删除）
   rm -v 文件名（可视化删除）
   
   2、删除目录
   rm -r 目录名（删除时会询问是否删除）
   rm -rf 目录名（强制删除，若目录不存在，此命令依旧可以执行，不报错）
   rm -rv 目录名（可视化强制）
   删除目录和文件时，先删除文件在删除目录

   rm的用法如下：
   1、删除文件夹以及文件夹中的所有文件命令：
   rm -rf 目录名字
   其中：
   -r：向下递归删除
   -f：直接强行删除，且没有任何提示
   2、删除文件命令
   rm -f 文件名
   将会强行删除文件，且无提示
   注意：
   使用rm -rf要格外注意，linux中没有回收站，慎重删除
   
   如果空目录就可以用rmdir
   如果是有文件的目录就用 rm -f
   一般文件用 rm

   
复制文件或目录（可以对目标文件或目录重命名） cp
---------------------------------------------------
   
::
   
   源文件始终不变，仅仅是对目标文件进行改变。
   
   1、复制文件
   格式：cp 源文件 目标文件
   
   2、拷贝目录（目录需要加/）注意区分绝对路径和相对路径
   格式：cp -r 源目录 目标目录
   
移动（类似于Windows中的剪切）mv
---------------------------------------
   
::
   
   注意与复制命令cp的区别。mv命令使源文件的状态发生改变。
   
   1、移动目录时：
   若果目录存在，则会将原目录移动到目标目录下；如果目录不存在，则相当于移动并重命名
   
查看文件内容cat tac more less head tail
--------------------------------------------

misc
------------

Linux-cp命令详解
^^^^^^^^^^^^^^^^^^^^^

`Linux-cp命令详解 <https://www.linuxidc.com/Linux/2019-08/159913.htm>`__

如果要仅在文件比目标更新时复制文件，请使用以下 -u 选项：

::

  cp -u file.txt file_backup.txt

另一个可能有用的选项是 -v，他告诉 cp 打印详细输出：

::

  cp -v file.txt file_backup.txt
  'file.txt' -> 'file_backup.txt'

使用 cp 命令复制目录
要复制目录(包括其所有文件和子目录)，请使用 -R 或 -r 选项。在以下示例中，我们将目录复制 Pictures 到 Pictures_backup ：

::

  cp -R Pictures Pictures_backup

要仅复制文件和子目录，而不复制目标目录，请使用以下 -T 选项：

::

  cp -RT Pictures Pictures_backup

另一种只复制目录内容而不是目录本身的方法是使用通配符 (*) 。以下命令的缺点是它不会复制隐藏文件和目录(以点 . 开头的文件和目录) ：

::

  cp -RT Pictures/* Pictures_backup/



拷贝命令比较，XCOPY(win) VS cp(linux)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

windows下XCOPY命令，目标目录的父目录可以不存在，命令自己会创建

Linux下cp不会自动创建目标目录的父目录，如果目标目录不在在会直接报错。

gnumake-wildcard(win) VS cp(linux)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

windows 下gnumake命令wildcard返回匹配文件名带目录（待确认）

Linux 下gnumake命令wildcard返回匹配文件名带目录（已确认）


` <>`__

` <>`__

` <>`__

` <>`__





.. 
  awk
  -----------
  
  ` <>`__
  
  ::

