############
markdow demo
############

******
副标题
******

.. contents:: 目录
.. section-numbering::

.. 
 :Author: kevinluo
 :Contact: kevinluo_72@163.com

.. 
 .. contents:: 目录
 .. section-numbering::

====================================================================
标题，这里前面要有空格，前后有空行，此处最好不要添加链接以和reST一致
====================================================================


body
====

标题级段落，paragraph
---------------------

段落，paragraph,前后面要有空行，除非是文档的头和尾。\ **``\n``\ 被去掉了**
紧接的另一行会被视为同一段落，换行符会被去掉。这样可以\ **``\n``\ 被去掉了**
方便段落书写时随意换行，不用启用文本编辑器的自动换行\ **``\n``\ 被去掉了**
也能实现一个段落。段落内连续两个以上空格 tab 会skip

| 段落，保留换行符，行尾加2个空格
| 因前面行尾加了两个空格，此行成一个独立行，如是html语言则是前行尾加了\ ``<br>``

缩进段落仍是段落，tab或4个空格以下，自动去掉

缩进段落仍是段落，tab或4个空格以下，自动去掉

缩进段落仍是段落，tab或4个空格以下，自动去掉

::

   缩进段落变成代码块，tab或4个空格，表示代码段，相当于.. code:: **多   空格**，**多          tab被保留**，并且不解析markup***符号***，大部份解释器还不自动换行。

    缩进段落，>tab或4个空格,<2个tab或8个空格

       缩进段落，2个tab或8个空格

         缩进段落，>2个tab或8个空格

建议：正常使用仅不缩进和缩进tab或4个空格。前者表示正常段落，后者表示是代码块。前者如果需要换行符则行尾加2空格。

列表级段落，paragraph
---------------------

由于列表自己有层级缩进结构，要从属于相应列表的，以相应列表层级数目作为标基，参考标题段落。对齐都是参考本层级的位置的。

-  一个空行才表示分段，在要分段的地方，一定要空一行；不想分段的地方，敲个回车就行了

-  tab缩进主要表示一种层级关系，在各种嵌套的时候，一定要注意缩进，
   缩进少一个空格都有可能出问题。多段也是tab缩进一次，相对于列表箱号位。

示例

-  列表1级

   列表1级多段落，paragraph，4个空格，必须要缩进4个空格，否则不能支持列表段。
   第2行顶格。

   列表1级多段落，paragraph，4个空格，必须要缩进4个空格，否则不能支持列表段。
   第2行对齐。

   列表1级多段落，paragraph，5个空格，必须要缩进4个空格，否则不能支持列表段
   顶格第2行

   ::

        列表1级多段落，paragraph，8个空格，表示代码段
        第2行

   -  列表2级，相对上级列表3个空格，高于3个空格会被视为代码块

      列表2级多段落，paragraph，相对本级列表位4个空格，不能少于4个，要不会会被视为本级列表结束，跑到上一个列表。
      对齐第2行

      列表2级多段落，paragraph，相对本级列表位5个空格。5,6,7个空格都可以。不能8个，8个则成代码块了
      第2行对齐

      -  列表3级

         列表3级段落，paragraph，4个空格 第2行

         ::

              列表1级段落，paragraph，相对本列表8个空格，表示代码块
              第2行

      列表2级段落，paragraph，顶格8个空格
      对齐第2行，建议还是和上行缩进一致，这样代码美观

   -  续上列表2级，一个tab/4个空格

列表
====

-  一个空行才表示分段，在要分段的地方，一定要空一行；不想分段的地方，敲个回车就行了
-  tab缩进主要表示一种层级关系，在各种嵌套的时候，一定要注意缩进，
   缩进少一个空格都有可能出问题

参考\ `Github+Jekyll
搭建个人网站详细教程 <https://www.jianshu.com/p/9f71e260925d>`__

-  `Ruby
   installer <https://links.jianshu.com/go?to=https%3A%2F%2Frubyinstaller.org%2F>`__

.. header:: This space for rent.

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!
       
.. list-table::
    :header-rows: 1

    * - 1
      - 2
      - 3
      - 4
    * - 5
      - 6
      - 7
      - 8
    * -
      -
      - 9
      -


block indent

    dark night give me **black** :sub:`eyes`  
    but I use it to :sup:`seek` for *bright*

    -- gu Cheng

part :math:`(\pi/4)*d^2`  

this is the grammar of markdown:
$A = (\pi/4)d^2$


.. math::
  
  A = (\pi/4)d^2

