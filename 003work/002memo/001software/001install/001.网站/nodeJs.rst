***************
node.JS
***************

.. contents:: 目录
.. section-numbering::

.. 
 :Author: kevinluo
 :Contact: kevinluo_72@163.com

.. 
 .. contents:: 目录
 .. section-numbering::


install
=======

`download here <https://nodejs.org/en/>`__



reference
---------

`node.js 安装详细步骤教程 <https://blog.csdn.net/antma/article/details/86104068>`__

`廖雪峰的官方网站Node.js来龙去脉教程 <https://www.liaoxuefeng.com/wiki/1022910821149312/1023025235359040>`__

为什么NODEJS 基本命令 `nodejs的整体安装与使用详细步骤！小白必读！ <https://blog.csdn.net/a331790021/article/details/75661785>`__

` <>`__

` <>`__



.. 
 ` <>`__



setting
-------

环境变量
^^^^^^^^

msi安装版本已经配置PAHT，
非安装版，执行nodevars.bat

配置npm在安装全局模块时的路径和缓存cache的路径
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以先用 `npm config ls -l` 看一下当前配置变量

非安装版，npm -g 安装module时，自动放到node_modules目录下面。

`node.js 安装详细步骤教程-重配全局模块下载目录 <https://blog.csdn.net/antma/article/details/86104068>`__

在执行例如npm install webpack -g等命令全局安装的时候，默认会将模块安装在 `C:\Users\用户名\AppData\Roaming路径下的npm和npm_cache中` ，不方便管理且占用C盘空间

这里配置自定义的全局模块安装目录，在node.js安装目录下新建两个文件夹 

1. node_global和node_cache，然后在cmd命令下执行如下两个命令：

::

    npm config set prefix "D:\Program Files\nodejs\node_global"
    npm config set cache "D:\Program Files\nodejs\node_cache"

2. 加入环境变量 NODE_PATH
   
   环境变量 -> 系统变量中新建一个变量名为 “NODE_PATH”， 值为“D:\Program Files\nodejs\node_modules”

3. 用户变量里的Path
   
   编辑用户变量里的Path，将相应npm的路径改为：D:\Program Files\nodejs\node_global

4. 测试
   
   在cmd命令下执行 `npm install webpack -g` 然后安装成功后可以看到自定义的两个文件夹已生效

   webpack 也已安装成功，执行 npm webpack -v 可以看到所安装webpack的版本号


npm
---

淘宝NPM镜像安装
^^^^^^^^^^^^^^^

`淘宝NPM镜像安装 <http://npm.taobao.org/>`__ 

你可以使用我们定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm:

安装cnpm:

::

    $ npm install -g cnpm --registry=https://registry.npm.taobao.org

使用：

::

    $ cnpm install [name]

help
^^^^

where <command> is one of:

    access, adduser, audit, bin, bugs, c, cache, ci, cit,
    clean-install, clean-install-test, completion, config,
    create, ddp, dedupe, deprecate, dist-tag, docs, doctor,
    edit, explore, get, help, help-search, hook, i, init,
    install, install-ci-test, install-test, it, link, list, ln,
    login, logout, ls, org, outdated, owner, pack, ping, prefix,
    profile, prune, publish, rb, rebuild, repo, restart, root,
    run, run-script, s, se, search, set, shrinkwrap, star,
    stars, start, stop, t, team, test, token, tst, un,
    uninstall, unpublish, unstar, up, update, v, version, view,
    whoami

::

 npm <command> -h  quick help on <command>
 npm -l            display full usage info
 npm help <term>   search for help on <term>
 npm help npm      involved overview

 npm config ls -l

command
^^^^^^^

install
"""""""

npm install (in package directory, no arguments):

Install the dependencies in the local node_modules folder.

By default, npm install will install all modules listed as dependencies in package.json(5).




哪里可以检索可以用npm安装的module?
----------------------------------

象python package的pypi网站， sublime package的http://packagecontrol.io 

??

tips
----



