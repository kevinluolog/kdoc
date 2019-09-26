########
Graphviz
########

.. contents:: 目录
.. section-numbering::

install
--------

1. download_
   
.. _download: http://www.graphviz.org/download/


2. 设置

   i. 环境变量
      path: ~\graphviz-2.38\bin

   #. font中文支持

      - \graphviz-2.38\etc\fonts\fonts.conf， 指明字体文件目录

       ::

          <dir>#WINFONTDIR#</dir>
          改为
          <dir>C:\Windows\Fonts</dir>

      - .dot文件指明引用哪种字体
       
       ::
       
            .dot文件加入
            fontname="Microsoft YaHei"
            edge [fontname="Microsoft YaHei"];
            node [fontname="Microsoft YaHei"];
             
3. tools

  - ~\graphviz-2.38\bin\gvedit.exe 
  - ~\graphviz-2.38\bin\lefty.exe
  - ~\graphviz-2.38\bin\dotty.exe


tips
----

faq
---
