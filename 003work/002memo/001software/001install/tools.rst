*******************
Little Tools
*******************

.. contents:: contents
.. section-numbering::


工具应用汇总
================

文件比较
---------------------

1. winmerge

文件解压缩
---------------------

1. Bandizip
2. 7z
3. unzip/zip
4. 


MISC
---------------------

1. iconv
2. 

winmerge
================

1. explorer右键菜单安装

2. 设置

   a) file filter: tools->filter->,filefilters(指文件名), linfilters(是指文件内容)。 include/exclude 语境是"include或exclude-全部文件除xxx以外"
   b) tree浏览/Tabular: view->treemode, 一般是灰的，要valid需要在打开界面folder filter下面勾上：include subfolders. 这样tree可选。
   c) 启用单侧目录内容展开，另一侧没目录时不会展开:edit->option->compare->folder->,单侧子文件夹内容;子文件夹
   d) 启用比较简单模式，仅用时间和大小。edit->option->compare->folder->,compare method。
      
3. 案例

   a) 带目录拷贝/移动。
   

      0. tabular模式查看
      1. 选中要拷贝的文件，拷贝/移动这些文件，自然目录就创建了。如果是tree模式也可以，但是如果拷贝tree的话会把所有tree下的文件拷贝/移动的。
   
   b) 



---------------------


iconv 编码转换
================

参考链接
---------------------

` <>`__

`iconv: illegal input sequence at position <https://blog.csdn.net/sunnypotter/article/details/18218707>`__

` <>`__

` <>`__


用法
---------------------

使用iconv 命令

::

  iconv -f GBK -t UTF-8 file1 -o file2

  #   iconv -f GBK -t UTF-8 $$@.tmp >$$@
  # 加入-c，表示忽略那些不能解释的字符
  #   iconv -f GBK -t UTF-8 -c $$@.tmp >$$@


问题
---------------------


“iconv: illegal input sequence at position”的错误
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`iconv: illegal input sequence at position <https://blog.csdn.net/sunnypotter/article/details/18218707>`__

在使用iconv转换文件的字符编码时，如果遇到类似“iconv: illegal input sequence at position”的错误，原因是需要转换的字符编码没有涵盖文件中的字符，比如，将一个简体中文的GB2312的文件转换为BIG5的编码，而在繁体编码的BIG5里面，不包含很多的简体中文字符，所以在转换的时候就会遇到如上的错误。

顺便提供一个用于查看文件编码的工具“enca”，我在everest 0.5下做的RPM包。用法很简单，
::

  #　enca filename

解决方法，忽略那些不能解释的字符：

::

  iconv -f cp936 -t utf-8 -c file1 >  file2


命令行解压缩-zip/unzip/7z.exe/rar.exe
=====================================================================

unzip 
---------------------------------------------------------------------

下载 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`win32 zip下载地址 <http://gnuwin32.sourceforge.net/packages/zip.htm
>`_ 

`win32 unzip下载地址 <http://gnuwin32.sourceforge.net/packages/unzip.htm>`_ 

用法 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

批处理：
  
  ::

   set EXT_DIR="H:\tmp\downloads\chrome\周读readweek\000\pdf\xx"
   @REM unzip [-Z] [-cflptuvz[abjnoqsCLMVX$/:]] file[.zip] [file(s) ...]  [-x xfile(s) ...] [-d exdir]
   @REM -j 表示解压不带目录(必须放到解压文件名之前)， -d 后面接目标目录(必须放到最后面)
   @REM unzip -j *.zip -d %EXT_DIR%
   unzip -j *.zip -d %EXT_DIR%

注意： 需要加入执行路径，如果直接打入路径引用unzip会提示出错。

7z.exe 
---------------------------------------------------------------------

下载 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


用法 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`使用7-Zip 的命令行版本来压缩和解压文件 <https://blog.csdn.net/WPwalter/article/details/90638622>`_ 

运行 7z.exe 后可以看到命令行中列出了可用的命令行命令：

::

  a：将文件添加到压缩档案中
  b：测试压缩或解压算法执行时的 CPU 占用
  d：从压缩档案中删除文件
  e：将压缩档案中的所有文件解压到指定路径，所有文件将输出到同一个目录中
  h：计算文件的哈希值
  i：显示有关支持格式的信息
  l：列出压缩档案的内容
  rn：重命名压缩档案中的文件
  t：测试压缩档案的完整性
  u：更新要进入压缩档案中的文件
  x：将压缩档案中的所有文件解压到指定路径，并包含所有文件的完整路径

解压一个文件

::

  7z x {fileName} -o{outputDirectory}
  特别注意：-o 和 {outputDirectory} 之间是 没有空格 的。

一个例子：

::

  7z x C:\Users\walterlv\demo.7z -oC:\Users\walterlv\demo