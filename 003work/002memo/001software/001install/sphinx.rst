########
sphinx
########

***************
sphinx is great
***************

.. contents:: 目录
.. section-numbering::


sphinx install+2
=====================================================

`sphinx install 官方spec <http://www.sphinx-doc.org/en/master/usage/installation.html#linux>`__

windows
---------

`pypi sphinx website <https://pypi.org/project/Sphinx/>`__

pip install Sphinx

or 

pip install -U sphinx

版本显示：

sphinx-build --version

Linux
----------

Debian/Ubuntu
^^^^^^^^^^^^^^^^^^^

Install either python3-sphinx (Python 3) or python-sphinx (Python 2) 

using apt-get:
::

  $ apt-get install python3-sphinx

If it not already present, this will install Python for you.

RHEL, CentOS
^^^^^^^^^^^^^^^^^

Install python-sphinx using yum:
::

  $ yum install python-sphinx

If it not already present, this will install Python for you.

mac Os
-----------

Sphinx can be installed using Homebrew, MacPorts, or as part of a Python distribution such as Anaconda.

Homebrew
::

  $ brew install sphinx-doc



sphinx项目创建
==============

`sphinx spec: Getting Started <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`__

需要创建两个文件必须文件

- conf.py

  where you can configure all aspects of how Sphinx reads your sources and builds your documentation. 

- index.rst

  a master document, The main function of the master document is to serve as a welcome page, and to contain the root of the “table of contents tree” (or toctree). This is one of the main things that Sphinx adds to reStructuredText, a way to connect multiple files to a single hierarchy of documents.


可以手工添加，也可以用下面的sphinx-quickstart来创建一个模板

sphinx-quickstart 模式
---------------------------------------

::

  $ sphinx-quickstart

自动创建两个文件必须文件
conf.py， index.rst (if you accepted the defaults)，

还有文件make.bat，makefile， 目录_static，_templates

直接用sphinx-build program:
-------------------------------------

有了conf.py， index.rst, 就可以直接

::

  $ sphinx-build -b html sourcedir builddir



sphinx选项
==============

引入graphviz???要加入详细描述。。。kl+

.. graphviz::

   digraph foo {
      "step 1" -> "step 2";
      "step 2" -> "step 3";
      "step 3" -> "step 1";
 
   }

.. graphviz:: H:\tmp_H\001.work\002git\000GT\dot01.dot

issues
======

kevinluo

makefile 中设定 SOURCEDIR 失败
----------------------------------------

.. 
 - 目的：
 - 问题：
 - 分析：
 - 解决：


- 目的：

想把源文件和编译位置分开，这样可以直接把github控制下的目录作为源文件，同时编译位置可以任意，这样编译系统和编译输出文件不会进入github系统。

- 问题：
  
  ::

    makefile中：
    修改
    SOURCEDIR     = source
    为
    SOURCEDIR     = "H:\tmp_H\001.work\002git\kdoc\003work\002memo\001software"

  提示出错，"conf.py 找不到。"

- 分析：
  
  一开始以为是文件目录的写法不对，或者是没有加引号。加入echo分析，发现SOURCEDIR仍为source,没改过来。不起作用。原来是没有理解透sphinx的MAKEFILE变量overriding的顺序。make.bat中带入的变量会override makefile中的变量定义。.bat文件相当于命令行运行。此make是个BAT,非真正的make.exe.

- 解决：
  
  直接跑到make.bat 中修改即可以。

index.rst中用glob加入toctree的多文件内容失败，没找出来
-------------------------------------------------------

- 目的：
  
  用通配符\*把当前和子文件夹中所有的.rst文件找出来，加入toctree

- 问题：
  
  \*用了，不起作用，子文件夹中一个文件也没找出来。

- 分析：
  
  glob只匹配指定文件夹1层，不包括子文件夹。

- 解决：
  
  每个文件夹指定匹配模式
  001install/*

  001install/*


tips
====


FAQ
===


