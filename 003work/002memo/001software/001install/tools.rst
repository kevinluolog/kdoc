*******************
Little Tools
*******************

.. contents:: contents
.. section-numbering::

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




