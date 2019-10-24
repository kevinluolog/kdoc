
*********************************************************************
github
*********************************************************************

.. contents:: contents
.. section-numbering::

参考链接 
=====================================================================

`git-scm 官方doc 网址 <https://git-scm.com/doc>`__

`Git push常见用法 <https://www.cnblogs.com/qianqiannian/p/6008140.html>`__

`git add -A 和 git add . 的区别 <https://blog.csdn.net/caseywei/article/details/90945295>`__

`git命令之git remote的用法 <https://www.cnblogs.com/wuer888/p/7655856.html>`__

` <>`__

` <>`__


经验点滴 
=====================================================================


命令
---------------------------------------------------------------------

git clone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   # 注意：如果直接显式指明clone目标目录，则一定要把repo名字写上，不然不会自动加上;   如果省略,则会自动创建repo名的目录，然后clone进这个目录
   # <directory>The name of a new directory to clone into. The "humanish"    part of the source repository is used if no directory is explicitly given    (repo for /path/to/repo.git and foo for host.xz:foo/.git). Cloning into    an existing directory is only allowed if the directory is empty  #- git    clone -b gh-pages https://$GH_TOKEN_FULL@github.com/kevinluolog/   gp-memo.git /tmp/klgit/gp-memo

     - git clone -b gh-pages https://$GH_TOKEN_FULL@github.com/kevinluolog/gp-memo.git
   # 进入到clone 创建的repo目录
     - cd gp-memo

git add
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- git add -A  提交所有变化
- git add -u  提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
- git add .  提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件

::

   git add .：他会监控工作区的状态树，使用它会把工作时的所有变化提交到暂存区，包括文件内容修改(   modified)以及新文件(new)，但不包括被删除的文件。
   git add -u ：他仅监控已经被add的文件（即tracked    file），他会将被修改的文件提交到暂存区。add -u 不会提交新文件（untracked    file）。（git add --update的缩写）
   git add -A ：是上面两个功能的合集（git add --all的缩写）


git commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   # git commit -m ‘message’
   # -m 参数表示可以直接输入后面的“message”，如果不加 -m参数，那么是不能直接输入mess   age的，而是会调用一个编辑器一般是vim来让你输入这个message，
   # message即是我们用来简要说明这次提交的语句。
   # git commit -am ‘message’ -am等同于-a -m
   # -a参数可以将所有已跟踪文件中的执行修改或删除操作的文件都提交到本地仓库，即使它们   没有经过git add添加到暂存区，
   # 注意: 新加的文件（即没有被git系统管理的文件）是不能被提交到本地仓库的。
   # --allow-empty
   # Usually recording a commit that has the exact same tree as its sole    parent commit is a mistake, and the command prevents you from making such    a commit. This option bypasses the safety, and is primarily for use by    foreign SCM interface scripts.
     - git commit --allow-empty -m "kl+travis+"

git push
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   # git push的一般形式为 git push <远程主机名> <本地分支名> <远程分支名> ，例如    git push origin master：refs/for/master    ，即是将本地的master分支推送到远程主机origin上的对应master分支， origin    是远程主机名。第一个master是本地分支名，第二个master是远程分支名。
   # git push origin master
   # 如果远程分支被省略，如上则表示将本地分支推送到与之存在追踪关系的远程分支（通常两   者同名），如果该远程分支不存在，则会被新建
   # git push origin ：refs/for/master
   # 如果省略本地分支名，则表示删除指定的远程分支，因为这等同于推送一个空的本地分支到   远程分支，等同于 git push origin –delete master
   # git push origin
   # 如果当前分支与远程分支存在追踪关系，则本地分支和远程分支都可以省略，将当前分支推   送到origin主机的对应分支
   # git push
   # 如果当前分支只有一个远程分支，那么主机名都可以省略，形如 git push，可以使用git    branch -r ，查看远程的分支名
   #  关于 refs/for：
   # refs/for 的意义在于我们提交代码到服务器之后是需要经过code review    之后才能进行merge的，而refs/heads 不需要
   # 原文链接：https://blog.csdn.net/qq_37577660/article/details/78565899
     - git push https://$GH_TOKEN_FULL@github.com/kevinluolog/gp-memo.git


git remote
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   git remote -v
   git init
   git add xxx
   git commit -m 'xxx'
   git remote add origin ssh://software@172.16.0.30/~/yafeng/.git
   git push origin master 
   git remote show origin
   git clone https://$GH_TOKEN_FULL@github.com/kevinluolog/gp-memo.git


离散点滴
---------------------------------------------------------------------

- git clone -b gh-pages https://$GH_TOKEN_FULL@github.com/kevinluolog/gp-memo.git： 不写目标目录时，会把repo名gp-memo作为目录名
- git clone -b gh-pages https://$GH_TOKEN_FULL@github.com/kevinluolog/gp-memo.git /tmp/gp-memo： 写目标目录时，不会自动把repo名gp-memo作为目录名，需要显式地写上，要不会把repo内容直接写入目标目录。
- git commit --allow-empty -m "kl+travis+" : --allow-empty 让commit相同时不返回错exit(1),如travis CI 不会报错
