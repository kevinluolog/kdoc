*******************
travis CI
*******************

.. contents:: contents
.. section-numbering::

install
=======

`travis website <https://travis-ci.com>`__

教程链接
----------

`持续集成服务TravisCI教程-阮一峰 <http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html>`__

`SSH deploys with Travis CI-frenchman <https://oncletom.io/2016/travis-ssh-deploy/>`__

`spec for deploy of github pages <https://docs.travis-ci.com/user/deployment/pages/>`__

`Travis Ci的最接地气的中文使用教程 <https://www.jianshu.com/p/8308b8f08de9>`__

` <>`__

` <>`__

案例
======

gcc c
-----

同时我们需要在仓库中编写一份名为.travis.yml的配置文件，来指定我们的项目需要进行怎样的操作。

::

   sudo: required
   language: c
   complier: gcc
   before_script: sudo apt-get install libev-dev
   script: make
   notifications:
     email:
       recipients:
         - xxx@gmail.com
       on_success: change
       on_failure: always


可以看到这里指定了需要的sudo权限，编程语言，编译器，script即执行的操作，before_script则安装了项目依赖的libev-dev包，通知的方式email，并且指定了邮件地址。

official deploy spec
--------------------

For a minimal configuration, add the following to your .travis.yml:

::

   deploy:
     provider: pages
     skip_cleanup: true
     github_token: $GITHUB_TOKEN  # Set in the settings page of your repository,    as a secure variable
     keep_history: true
     on:
       branch: master

Make sure you have skip_cleanup set to true, otherwise Travis CI will delete all the files created during the build, which will probably delete what you are trying to upload.

Further configuration #

local_dir: Directory to push to GitHub Pages, defaults to current directory. Can be specified as an absolute path or a relative path from the current directory.

repo: Repo slug, defaults to current repo. Note: The slug consists of username and repo name and is formatted like user/repo-name.

target_branch: Branch to (force, see: keep_history) push local_dir contents to, defaults to gh-pages.

keep_history: Optional, create incremental commit instead of doing push force, defaults to false.
fqdn: Optional, sets a custom domain for your website, defaults to no custom domain support.

project_name: Defaults to value of fqdn or repo slug, used for metadata.
email: Optional, committer info, defaults to deploy@travis-ci.org.
name: Optional, committer, defaults to Deployment Bot.

committer_from_gh: Optional, defaults to false. Allows you to use the token’s owner name and email for commit. Overrides email and name options.

allow_empty_commit: Optional, defaults to false. Enabled if only keep_history is true.

github_url: Optional, the URL of the self-hosted GitHub enterprise, defaults to github.com.

verbose: Optional, be verbose about internal steps, defaults to false.

deployment_file: Optional, defaults to false, enables creation of deployment-info files.

official notification spec
--------------------------

Configuring email notifications
Specify when you want to get notified:

::

   notifications:
     email:
       recipients:
         - one@example.com
         - other@example.com
       on_success: never # default: change
       on_failure: always # default: always

travis CI 问题集锦
=======================



KDOC:

travis CI环境变量 设置,env: -单行 VS 多行
-----------------------------------------------

不能这样分开写：会报错，变量找不到，要写到同一行

::

   env:
     - T_DIR_BASE_SRC=$TRAVIS_BUILD_DIR/003work/002memo
     - T_DIR_BASE_OBJ=$TRAVIS_BUILD_DIR/output/002memo
     - T_DIR_BASE_COPYTO=$TRAVIS_BUILD_DIR/output/copy2 
     - T_DIR_TEMPLATE=$TRAVIS_BUILD_DIR/003work/000tools/002makefiles/   001pandoc/templates

参考：

`travis CI spec: 环境变量environment-variables <https://docs.travis-ci.com/user/environment-variables#defining-public-variables-in-travisyml>`__

::

   env:
     - FOO=foo BAR=bar

一个build要写到同一行中, 不同行是不同的build中的变量



  

linux上文件名大小写敏感，包括后缀名。Makefile VS makefile
----------------------------------------------------------------

::

   make startconv -f $TRAVIS_BUILD_DIR/003work/000tools/002makefiles/001pandoc/linux/makefile

报错找不文件或目录，没有编译rule

原因：makefile 和 Makefile 是两个不一样的文件

.c 和 .C 也是不一样的，要用脚本更改过来。


cp目标目录不存在，先mkdir -p
--------------------------------

::

   ifdef DIR_BASE_COPYTO
       @echo copy $(SUFFIX_TO) file to {hexo post}$(DIR_BASE_COPYTO) ...
   #   cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) 
   #因copy目标目录如果不存在，不能直接用cp命令，会出错，所以分两步，先mkdir, 再CP
       mkdir -p $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) 
       cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1)))
   endif

gnumake-file写文件命令输出GBK码，$(file, 需iconv转换
-------------------------------------------------------------

::

   $(file >$$@.tmp

iconv转换文件(GBK=>UTF8)报错，文件中有不支持的字符
------------------------------------------------------

从文件系统中取到的中文目录名和makefile中的中文，变成了几个乱码导致iconv认为是不认识的GBK码，从而iconv报错

$(file 在输出中文文件和文件夹名字时，不知道成了什么编码，反正是乱码，自然不能在转换字库中找到了。

所以加入-c,表示忽略。即保持原样不转换。

::


  #   iconv -f GBK -t UTF-8 $$@.tmp >$$@
  # 加入-c，表示忽略那些不能解释的字符
      iconv -f GBK -t UTF-8 -c $$@.tmp >$$@

真正原因：iconv转换文件(GBK=>UTF8)报错，文件中有不支持的字符
--------------------------------------------------------------------------

.travis.yml 是以 UTF-16 littel endian (0xFFFE)存储的。 所以make带入的参数 ADD_HEXO_TAG_FROM_DIR=技术 也是UTF16LE的。

`/linux/Makefile` 是以no BOM的自然方式存储的，后来发觉不是UTF8的模式，是以中文windows的codePage存储的，所以是GBK码形式的。

这样前面问题就可以解释了,  `$(file >$$@.tmp` 写入文件时， makefile中自然写入的中文"笔记"，被写成GBK码，.travis.yml带入的参数“技术”，却写入的是UTF16LE，同一文件中有不同的编码，这样如果用iconv转换自然会报错，UTF16LE编码的中文在GBK库中是没有的。同时如果用iconv强行当GBK转换就会乱了不知道是什么结果,如果保持原值用UTF8来解释自然就是乱码了。

解决方法：

把 `/linux/Makefile` 存储成UTF8的。
这样发觉iconv也可以不用了，大概 `$(file >$$@.tmp` 写入文件时，系统自然就把文件格式设成了UTF,然后用 `pandoc $$< -o - >>$$@` append模式添加输入UTF时，就成了utf了。 有一点没搞清楚，到底最后成了UTF8还是UTF16LE，猜想大概是utf8.


字符编码小知识： 参见 字符文件编码.rst 字符编码小知识

misc - raw materials
--------------------------------------------------------------------------


?????

用echo $date，结果只输出一个ate

?????


date +%Y%m%d -d @1425384141

?????


cp -t -T问题,想copy目录里的文件和子目录，travis提示错

?????

只查看最后一行
tail -1

?????

%ad
author date (format respects --date= option)

--date=iso (or --date=iso8601) shows timestamps in a ISO 8601-like format. The differences to the strict ISO 8601 format are:

?????
#For TravisCI users, simply add a config to .travis.yml so it clones the full repository history:
# `MestreLion/git-tools <https://github.com/MestreLion/git-tools#install>`__


可以解决拉取全部历史原数据到本地的问题，不加在clone时，只是本分支的历史。这样git log 能拿到文件所有commit的时间

# 根据上面网址介绍加入下面两行
git:
  depth: false

?????
`hexo.io/docs/variables#Page-Variables <https://hexo.io/docs/variables#Page-Variables>`__

`https://hexo.io/zh-cn/docs/variables.html#%E9%A1%B5%E9%9D%A2%E5%8F%98%E9%87%8F
>`__


???
Linux下修改文件创建时间(修改文件更改时间)
进到要改的文件目录里
find . -name “*” -exec touch ‘{}’ \;
注：最后一定要加分号，{}外一定要加单引号，*表示所有的文件（. 代表当前目录下）

???
`Hexo常见问题解决方案 <http://wp.huangshiyang.com/hexo%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88>`__

`Hexo搭建技术博客使用与常见问题详细讲解 <https://code.skyheng.com/post/50982.html>`__

`大前端-5分钟带你读懂Hexo源码设计模式 <https://www.jianshu.com/p/ef88b5bbb914>`__

`Hexo源码剖析 <https://blog.csdn.net/li20081006/article/details/73319054>`__

`hexo博客框架从入门到弃坑 <https://segmentfault.com/a/1190000018082781?utm_source=tag-newest>`__

`hexo-generator-index 源码分析 <https://www.jianshu.com/p/7bec9866a04d>`__

`hexo过滤器before_post_render-theme\scripts\filters\kl-touch-file-time.js <https://hexo.io/zh-cn/api/filter>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

