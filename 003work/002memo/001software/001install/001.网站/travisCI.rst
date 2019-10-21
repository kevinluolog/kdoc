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

` <>`__

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
--------------------------------------------------

::

   $(file >$$@.tmp

iconv转换文件报错，文件中有不支持的字符
----------------------------------------------

其实是几个乱码，$(file 在输出中文文件和文件夹名字时，不知道成了什么编码，反正是乱码，自然不能在转换字库中找到了。

所以加入-c,表示忽略。即保持原样不转换。

::


  #   iconv -f GBK -t UTF-8 $$@.tmp >$$@
  # 加入-c，表示忽略那些不能解释的字符
      iconv -f GBK -t UTF-8 -c $$@.tmp >$$@

$(file 在输出中文文件和文件夹名字时，不知道成了什么编码。iconv不支持
--------------------------------------------------------------------------





拷贝命令比较，XCOPY(win) VS cp(linux)
--------------------------------------------

windows下XCOPY命令，目标目录的父目录可以不存在，命令自己会创建

Linux下cp不会自动创建目标目录的父目录，如果目标目录不在在会直接报错。

gnumake-wildcard(win) VS cp(linux)
----------------------------------

windows 下gnumake命令wildcard返回匹配文件名带目录（待确认）

Linux 下gnumake命令wildcard返回匹配文件名带目录（已确认）

