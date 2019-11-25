*******************
gitpages
*******************

.. contents:: contents
.. section-numbering::

Travis Ci-kevinluolog
=====================

travis ci repo 关系
---------------------------------------------------------------------

序号  触发仓@分支  源仓@分支  输出仓@分支

kevinluolog/kdoc.git push触发
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

触发仓/输出仓关系
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

+-----------------+--------------------+-------------------------------+
| 触发仓@分支     | 源仓@分支          | 输出仓@分支                   |
+=================+====================+===============================+
| kdoc@dev        | kdoc@dev           | travisci_out_kdoc@output      |
+-----------------+--------------------+-------------------------------+
| kdoc@dev        | kdoc@dev           | hexo-klblog-src@x5个分支      |
+-----------------+--------------------+-------------------------------+
| kdoc@dev        | tran002memo@master | travisci_out_kdoc@tran002memo |
+-----------------+--------------------+-------------------------------+
| kdoc@dev        | tran003post@master | travisci_out_kdoc@tran003post |
+-----------------+--------------------+-------------------------------+
| kdoc@dev        | tran004book@master | travisci_out_kdoc@tran004book |
+-----------------+--------------------+-------------------------------+
| tran005work@xxx | ~                  | travisci_out_005work@xxx      |
+-----------------+--------------------+-------------------------------+
| tran006tmp@xxx  | ~ pdf html slide   | travisci_out_006tmp@xxx       |
+-----------------+--------------------+-------------------------------+

xxx表示：dev=all pdf=pdf html=html slide=slide 

完成功能：
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

代码参考 根目录travis.yml

.rst 转成 .html; 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
- 用sphinx生成：

  ::

    sphinx-build -b html $TRAVIS_BUILD_DIR/003work/006tmp $TRAVIS_BUILD_DIR/output/sphinx/build-post

  ::

     .html输出到本地output目录： `/output/sphinx/build-memo/*` 
     .html输出到本地output目录： `/output/sphinx/build-post/*` 

- 用git deploy： 

  ::

    git add -A; 
    git commit --allow-empty -m ""
    git push

  ::

     输出到=>repo0: `github.com/kevinluolog/travisci_out_kdoc@dev`
     002memo=>deploy到WWWrepo3: `github.com/kevinluolog/gp-memo@gh-pages`
     006tmp=>deploy到WWWrepo4: `github.com/kevinluolog/gp-post@gh-pages`


kdoc发布 网站地址：
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
1. `kevinluolog.github.io gp-memo 002memo <http://kevinluolog.github.io/gp-memo>`__

2. `kevinluolog.github.io gp-post 002post <http://kevinluolog.github.io/gp-memo>`__

.rst 转成 hexo输入的 .md;(添加frontmatter信息，如tag,category)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- 用makefile + pandoc生成： 

  详细参考 `kdoc/003work/000tools/002makefiles/001pandoc/linux/Makefile`

  ::

    make startconv -f $TRAVIS_BUILD_DIR/003work/000tools/002makefiles/001pandoc/linux/Makefile DIR_BASE_SRC=$TRAVIS_BUILD_DIR/003work/006tmp DIR_BASE_OBJ=$TRAVIS_BUILD_DIR/output/pandoc/hexomd/006tmp DIR_BASE_COPYTO= SUFFIX_FROM=.rst SUFFIX_TO=.md DIR_TEMPLATE=$T_DIR_TEMPLATE ADD_HEXO_TAG_FROM_DIR=post+ CTL_TOC=TRUE
    
    make startconv -f $TRAVIS_BUILD_DIR/003work/000tools/002makefiles/001pandoc/linux/Makefile DIR_BASE_SRC=$TRAVIS_BUILD_DIR/003work/006tmp DIR_BASE_OBJ=$TRAVIS_BUILD_DIR/output/pandoc/html/006tmp DIR_BASE_COPYTO= SUFFIX_FROM=.rst SUFFIX_TO=.html DIR_TEMPLATE=$T_DIR_TEMPLATE ADD_HEXO_TAG_FROM_DIR=


  ::

     .md输出到本地output目录： `/output/pandoc/hexomd/002memo/*` 
     .md输出到本地output目录： `/output/pandoc/hexomd/006tmp/*` 

- 用git deploy： 

  ::

    git add -A; 
    git commit --allow-empty -m ""
    git push

  ::

     输出到=>repo1: `github.com/kevinluolog/travisci_out_kdoc@dev`
     002memo=>deploy到repo2-(@b1:b5): `hexo-klblog-src/source/_posts/kl_notes/   002memo@xxx`
     006tmp=>deploy到repo2-(@b1-b5): `hexo-klblog-src/source/_posts/kl_notes/   002memo@xxx`
     xxx:分支 = 
          master
          hexo-next-Gemini :注意大写，linux下大小写敏感
          hexo-next-muse
          hexo-next-Pisces :注意大写，linux下大小写敏感
          hexo-maup

  deploy到rep:kevinluolog/hexo-klblog-src.git后，各分支会继续触发travis CI，把各分支上的hexo源码，编译成网站并deploy到对应的WWWrepoXXX的github分支(以repo2（kevinluolog/hexo-klblog-src.git）的分支名字命名)-分别对应repo2-(b1:b5)，和主网站repo。
  详细参考 `kevinluolog/hexo-klblog-src.git push触发`_
  

输出output目录结构
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   .html：由sphinx产生
   /output/sphinx/build-memo/*
   /output/sphinx/build-post/*
   
   .md hexo：由Makefile 产生, pandoc.exe
   makefile位于/kdoc/003work/000tools/002makefiles/001pandoc/linux/
   /output/pandoc/hexomd/002memo
   /output/pandoc/hexomd/006tmp
   
hexo源码仓库中的_posts来源，是上面output目录中的pandoc/hexomd目录中的002memo和006tmp. 先clone下来，用rm删除002meo和006tmp,再用cp从hexomd中copy过来。


kevinluolog/hexo-klblog-src.git push触发
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

代码参考 根目录travis.yml

触发仓/输出仓关系
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

~：表示和前面的 触发仓@分支 一样

| master
| hexo-next-Gemini :注意大写，linux下大小写敏感
| hexo-next-muse
| hexo-next-Pisces :注意大写，linux下大小写敏感
| hexo-maup

+------+----------------------------------+-----------+------------------------------+
| 序号 | 触发仓@分支                      | 源仓@分支 | 输出仓@分支 gitpage          |
+======+==================================+===========+==============================+
| 01   | hexo-klblog-src@master           | ~         | kevinluolog.github.io@master |
+------+----------------------------------+-----------+------------------------------+
| 02   | hexo-klblog-src@hexo-next-Gemini | ~         | hexo-next-gemini@gh-pages    |
+------+----------------------------------+-----------+------------------------------+
| 03   | hexo-klblog-src@hexo-next-muse   | ~         | hexo-next-muse@gh-pages      |
+------+----------------------------------+-----------+------------------------------+
| 04   | hexo-klblog-src@hexo-next-Pisces | ~         | hexo-next-Pisces@gh-pages    |
+------+----------------------------------+-----------+------------------------------+
| 05   | hexo-klblog-src@hexo-maup        | ~         | hexo-maup@gh-pages           |
+------+----------------------------------+-----------+------------------------------+


完成功能：
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

代码参考 根目录travis.yml

错误时间.md 转成 正确时间.md
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

详细代码参见 `/MakefileLinuxkblog.mk /travis.yml` 

影响网站文章时间排序。最终实现正确排序，同时还需要hexo的渲染前的hook配合,把date时间，改成文件的修改时间。

时间传递路径为，
渲染用的文件创建日期post.date <3= post.updated <2= 文件的mtime <1= 文件的首次commit时间。

第<1=次转换 
详细代码参见 `/MakefileLinuxkblog.mk /travis.yml` 
利用 `git log --date=iso --format="%ad" -- ""` 获取历史commit时间数据, 
`tail -1` 获取首次commit时间， 
`touch -c -data "" -m` 设置mtime

第<2=次转换 
hexo编译渲染时自己读取文件时间产生，尚不知在什么module里做的。

第<3=次转换 
详细代码参见 `/klBlog/themes/next/scripts/filters/kl-touch-file-time.js` 
利用 hexo钩子before_post_render 替换。

- 用makefile + shell脚本 + git命令生成： 

  详细代码参考 `/MakefileLinuxkblog.mk`
  
  makefile

  ::

    make touch1 -f MakefileLinuxkblog.mk DIR_BASE_SRC=$TRAVIS_BUILD_DIR/source/_posts

  或纯脚本,单行即可。

  ::

    git ls-files -z --eol | sed -e "s/i\\/lf[ \\t]*w\\/lf[ \\t]*attr\\/[ \\t]*/\\n/g" | while read filename; do git log --date=iso --format="%ad" -- "$TRAVIS_BUILD_DIR/source/_posts/$filename" | tail -1 | xargs -I{} touch -c $filename --date="{}" -m; done


正确时间.md 转成 网站.html; 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

详细代码参考 `/travis.yml /_config.yml`

deploy到rep:kevinluolog/hexo-klblog-src.git后，各分支会继续触发travis CI，把各分支上的hexo源码，编译成网站并deploy到对应的WWWrepoXXX的github分支(以repo2（kevinluolog/hexo-klblog-src.git）的分支名字命名)-分别对应repo2-(b1:b5)，和主网站repo。

- 用hexo g 生成
  
  自动把 `/hexo/klBlog/source/_posts` 目录中的 .md 生成hexo静态网页

  ::

    hexo clean
    hexo generate

- 用hexo deploy 发布到repo@gh-pages。

  ::

    sed -i "s/gh_token/${GH_TOKEN}/g" ./_config.yml
    hexo deploy
  
hexo-klblog-src发布 网站地址：
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `kevinluolog.github.io master <http://kevinluolog.github.io>`__

2. `kevinluolog.github.io hexo-next-gemini <http://kevinluolog.github.io/hexo-next-gemini>`__

3. `kevinluolog.github.io hexo-next-muse   <http://kevinluolog.github.io/hexo-next-muse>`__

4. `kevinluolog.github.io hexo-next-Pisces <http://kevinluolog.github.io/hexo-next-Pisces>`__

5. `kevinluolog.github.io hexo-maup        <http://kevinluolog.github.io/hexo-maup>`__


网站生成工作步骤:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

目标：写好即完成
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


目标是只要用sublime写好.rst文档，提交就可以直接在浏览器上看到写的东西了。即只要做完step1后,step 2,step3会自动完成，然后稍等即可以step4.
  
| step 1: 写文档 .rst
| step 2: .rst 2 .md(with hexo frontmatter)
| step 3: hexo编译成静态html,并发布到托管服务器
| stop 4: 用浏览器浏览网站


数据流路径(windown本地):
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1. .rst 2 .md(with hexo frontmatter) (手动make)

   目标：

   ::

     H:\\tmp_H\\001.work\\002git\\kdoc\\003work\\002memo
     H:\\tmp_H\\001.work\\002git\\kdoc\\003work\\006tmp
     =>
     H:\\tmp_H\\001.work\\004.env\\01prjsp\\hexo\\klBlog\\source\\_posts\\kl_notes
     H:\\tmp_H\\001.work\\004.env\\01prjsp\\hexo\\klBlog\\source\\_posts\\kl_post

   command:

   ::

     H:\\tmp_H\\001.work\\002git\\kdoc\\003work\\000tools\\002makefiles\\001pandoc\\rst2md_hexo_copy2.bat

     DIR_BASE_SRC=H:\\tmp_H\\001.work\\002git\\kdoc\\003work\\002memo ^
     DIR_BASE_OBJ=H:\\tmp_H\\001.work\\004.env\\01prjsp\\04make\\01rst2md\\tmp2 ^
     DIR_BASE_COPYTO=H:\\tmp_H\\001.work\\004.env\\01prjsp\\04make\\01rst2md\\copy2 ^

     此.bat用了一个临时目录，用时需要手工从copy2目录拷贝到kl_note目录。当然可以把.bat中的，obj目录直接转为kl_notes目录，就可以直接一步修改。注意把copyto目录置空。


2. 提交 hexo编译并发布 （tracis CI 自动 ）

   ::

     tortioseGit: H:\\tmp_H\\001.work\\004.env\\01prjsp\\hexo\\klBlog\\
     提交到 repo: hexo-klblog-src@master
     触发travis CI 自动 hexo编译成静态html => kevinluolog.github.io@master


数据流路径(travis 全自动):
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1. 写文档。
   
   【在clone下来的kdoc@dev子目录中(003work/002memo/* 003work/006tmp/*)】

3. 提交推送。
   
   【git add . ; git commit -m "" ; git push】

5. 触发kdoc@dev/travis.yml工作，编译/002memo /006tmp/*文档内容。

   详细参考  `kevinluolog/kdoc.git push触发`_

4. 触发hexo-klblog-src.git@xxx/travis.yml工作，编译/source/_posts/文档内容。
   
   详细参考  `kkevinluolog/hexo-klblog-src.git push触发`_

5. 浏览发布网站地址 sphinx和hexo
   
   参考 `kdoc发布 网站地址：`_ sphinx

   参考 `hexo-klblog-src发布 网站地址：`_  hexo

6. 生成输出 repo地址
   
   `kdoc的output输出仓库网址 travisci_out_kdoc <https://github.com/travisci_out_kdoc/>`__
