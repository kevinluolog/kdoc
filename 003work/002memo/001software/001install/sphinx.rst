########
sphinx
########

***************
sphinx is great
***************

.. contents:: 目录
.. section-numbering::


sphinx install
==============

`pypi sphinx website <https://pypi.org/project/Sphinx/>`__

pip install Sphinx

or 

pip install -U sphinx

版本显示：

sphinx-build --version

sphinx项目创建
==============

sphinx-quickstart

sphinx选项
==============

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
------------------------------

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


