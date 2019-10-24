*******************
github
*******************

.. contents:: contents
.. section-numbering::

kevinluolog
===========

Travis Ci
---------

travis ci repo 关系
^^^^^^^^^^^^^^^^^^^^^^^^^^^

序号  触发仓@分支  源仓@分支  输出仓@分支

kdoc
^^^^

+-------------+-----------+-----------------------+
| 触发仓@分支 | 源仓@分支 | 输出仓@分支           |
+=============+===========+=======================+
| kdoc@dev    | kdoc@dev  | travisci_out_kdoc@dev |
+-------------+-----------+-----------------------+

完成功能：

- .rst 转成 .html .pdf，并输出到输出仓
- .rst 转成 hexo输入的 .md, 并添加frontmatter信息，如tag,category,并输出到输出仓

实现方法：

 待加

本地用法：

 待加


hexo-klblog-src
^^^^^^^^^^^^^^^

~：表示和前面的 触发仓@分支 一样

| master
| hexo-next-Gemini :注意大写，linux下大小写敏感
| hexo-next-muse
| hexo-next-Pisces :注意大写，linux下大小写敏感
| hexo-maup

+------+-------------------------------------+-----------+------------------------------+
| 序号 | 触发仓@分支                         | 源仓@分支 | 输出仓@分支 gitpage          |
+======+=====================================+===========+==============================+
| 01   | hexo-klblog-src@master              | ~         | kevinluolog.github.io@master |
+------+-------------------------------------+-----------+------------------------------+
| 02   | hexo-klblog-src@hexo-next-Gemini    | ~         | hexo-next-gemini@gh-pages    |
+------+-------------------------------------+-----------+------------------------------+
| 03   | hexo-klblog-src@hexo-next-muse      | ~         | hexo-next-muse@gh-pages      |
+------+-------------------------------------+-----------+------------------------------+
| 04   | hexo-klblog-src@hexo-next-Pisces    | ~         | hexo-next-Pisces@gh-pages    |
+------+-------------------------------------+-----------+------------------------------+
| 05   | hexo-klblog-src@hexo-maup | ~         | hexo-maup@gh-pages      |
+------+-------------------------------------+-----------+------------------------------+


完成功能：

- 自动把 `\hexo\klBlog\source\_posts` 目录中的 .md 生成hexo静态网页，并输出到输出仓的gitpage发布分支。

实现方法：

- 电脑hexo文件目录,clone at `H:\tmp_H\001.work\004.env\01prjsp\hexo\klBlog` ,checkout相应分支即可。
- 所以仓库的gh-pages分支，可以用kevinluolog.github.io/仓库名， 访问到。

本地用法：


工作步骤:

目标是只要用sublime写好.rst文档，提交就可以直接在浏览器上看到写的东西了。即只要做完step1后,step 2,step3会自动完成，然后稍等即可以step4.
  
| step 1: 写文档 .rst
| step 2: .rst 2 .md(with hexo frontmatter)
| step 3: hexo编译成静态html,并发布到托管服务器
| stop 4: 用浏览器浏览网站


数据流路径(windown本地):

1. .rst 2 .md(with hexo frontmatter) (手动make)

   目标：

   ::

     H:\tmp_H\001.work\002git\kdoc\003work\002memo
     H:\tmp_H\001.work\002git\kdoc\003work\003post
     =>
     H:\tmp_H\001.work\004.env\01prjsp\hexo\klBlog\source\_posts\kl_notes
     H:\tmp_H\001.work\004.env\01prjsp\hexo\klBlog\source\_posts\kl_post

   command:

   ::

     H:\tmp_H\001.work\002git\kdoc\003work\000tools\002makefiles\001pandoc\rst2md_hexo_copy2.bat

     DIR_BASE_SRC=H:\tmp_H\001.work\002git\kdoc\003work\002memo ^
     DIR_BASE_OBJ=H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\tmp2 ^
     DIR_BASE_COPYTO=H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\copy2 ^

     此.bat用了一个临时目录，用时需要手工从copy2目录拷贝到kl_note目录。当然可以把.bat中的，obj目录直接转为kl_notes目录，就可以直接一步修改。注意把copyto目录置空。


2. 提交 hexo编译并发布 （tracis CI 自动 ）

   ::

     tortioseGit: H:\tmp_H\001.work\004.env\01prjsp\hexo\klBlog\
     提交到 repo: hexo-klblog-src@master
     触发travis CI 自动 hexo编译成静态html => kevinluolog.github.io@master


数据流路径(windown travis 全自动):


