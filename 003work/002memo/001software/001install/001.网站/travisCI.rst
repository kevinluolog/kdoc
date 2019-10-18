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


