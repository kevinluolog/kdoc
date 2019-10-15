***************
readme
***************

.. contents:: 目录
.. section-numbering::

makefile说明
================

makefile
--------

功能
^^^^^^^

搜索出源目录下有指定类型文件，利用pandoc在pandoc支持的格式之间进行转换，并把转换结果输出到指定的目标目录下，并保持和源文件一样的下层目录结构。再把目标文件覆盖式拷贝到发布目录，同时也保持和源文件一样的下层目录结构。
关键词： 自动搜索目录下文件，自动转换自动发布，并自动创建和源目录一样的下层目录

rst2pdf + copy2
"""""""""""""""

命令用法
++++++++++++

::

  .\..\..\001make\gnumake startconv -f makefile ^
  DIR_BASE_SRC=H:\tmp_H\001.work\002git\kdoc\003work\002memo ^
  DIR_BASE_OBJ=H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\tmp2 ^
  DIR_BASE_COPYTO=H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\tmp2\copy2 ^
  SUFFIX_FROM=.rst ^
  SUFFIX_TO=.pdf ^
  DIR_TEMPLATE=H:\tmp_H\001.work\002git\kdoc\003work\000tools\002makefiles\001pandoc\templates

参数 
~~~~~~~

注意
#######

注意: 要加入 --metadata-file 或 -M 引用metadata.yaml, pandoc帮助文档的案例是.md 的文件不用加，但是实践证明，在.rst转成.pdf时，必须要加上，不然直接加入了文档中，同时因引用不到汉字字体定义CJKmainfont: "SimSun"，会报错汉字找不到。所以统一加上。

rst2md + copy2 + hexo head
"""""""""""""""""""""""""""""""""""

命令用法
++++++++++++

::


参数 
~~~~~~~

注意
#######

注意: 

rst2html + copy2
"""""""""""""""""""""""

命令用法
++++++++++++

::


参数 
~~~~~~~

注意
#######

注意: 



