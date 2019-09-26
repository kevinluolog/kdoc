***************
extract
***************

.. contents:: 目录
.. section-numbering::

.. 
 :Author: kevinluo
 :Contact: kevinluo_72@163.com

.. 
 .. contents:: 目录
 .. section-numbering::

摘录东西
===========

新东西
==========

Graphviz
--------

高效而简洁的绘图工具graphviz。graphviz是贝尔实验室开发的一个开源的工具包，它使用一个特定的DSL(领域特定语言):
dot作为脚本语言，然后使用布局引擎来解析此脚本，并完成自动布局。graphviz提供丰富的导出格式，如常用的图片格式，SVG，PDF格式等。

网络
=======

日常开发中用到的工具Swagger，swagger是一个RESTful文档生成工具。
---------------------------------------------------------------

`页面定制CSS代码初探（六）：h2、h3 标题自动生成序号 详细探索过程 <https://www.cnblogs.com/36bian/p/7609304.html>`__
-------------------------------------------------------------------------------------------------------------------

标题要不要加序号？ 直到我碰到一个人这么说

::

   手动维护编号实在是一件很闹心的事情， 如果位置靠前的某个段落被删除了， 那么几乎每个段落的编号都要手动修改一下。

当即决定，放弃写序号，改由CSS自动生成。

`zencode.in/8.中文排版二三事.html <http://zencode.in/8.中文排版二三事.html>`__

-  安装setuptools

   ::

        https://pypi.python.org/pypi/setuptools
        python2 setup.py install

-  安装pip

   ::

        https://pypi.python.org/pypi/pip
        python2 setup.py install
        pip的安装目录E:\setup\Python27\Scripts，看下面截图中，有pip、pip2.7、pip2

-  安装Python3

   （由于Python3自带pip，所以无需另外安装pip）env自带

-  验证Python3里pip是否自动安装成功

   在cmd里输入pip3或是pip3.5

-  若有的包不支持pip的安装形式

   ::

        将相应的文件下载解压后放入到某个目录下，用cmd进入到解压后的目录
        若是给Python2安装该包，则执行python2 setup.py install
        若是给Python3安装该包，则执行python setup.py install      

-  pip2 和 pip3设置

   这时候需要重新安装pip，命令分别为：

   ::

        python2 -m pip install –upgrade pip –force-reinstall
        python3 -m pip install –upgrade pip –force-reinstall 

   现在可以通过pip2 -V 和 pip3-V 查看两个版本的pip信息

   以后只需运行pip2 install XXX和pip3 install
   XXX即可安装各自的python包。