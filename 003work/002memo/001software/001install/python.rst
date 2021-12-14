######
python
######

.. contents:: 目录
.. section-numbering::

install
=======

需要学习的东西
--------------------

大类：

1. install environment
2. module install and distribution
3. language reference
4. library reference
5. tutorials

小类：

1. class 
2. file. open, with open 

安装过程
--------------------

python3 python2 共存安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 下载安装包
2. 分别安装
3. 加入path, 修改python.exe 成python3.exe python2.exe; pythonw.exe同样修改
4. 更新各自pip, python3 -m pip install --upgrade pip --force-reinstall, python3用pip3
5. 建立虚拟环境，virtualenv -p python3 --no-download .\\std3 ，加上--no-download可以避免pypi.org 连接不上的报错。这样也可以安装pip，setuptools等。
6. 激活退出虚拟环境，进入scription, activate激活，本质是设置最前的路径和相关工作目录
7. 虚拟环境中安装包，pip install flask==0.10.1
8. 查看虚拟环境中安装的包，pip freeze，pip list
9. 在Pycharm中设置虚拟环境，在每个项目属性中选择
10. 主要目录，Scripts：命令执行文件， site-packages：安装模块

包安装工具
--------------------

`pip setuptools easy_install <https://blog.csdn.net/u010458170/article/details/46438763?utm_medium=distribute.pc_relevant_download.none-task-blog-blogcommendfrombaidu-1.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-blogcommendfrombaidu-1.nonecas>`_ 

setuptools->distribute->pip

easy_install .tgz .egg 均可安装

pip 可以利用 requirments.txt 来实现在依赖的安装。

Eggs格式是setuptools引入的一种文件格式，用于 Python 模块的安装。setuptools 可以识别这种格式。并解析它，安装它。
wheel本质上是一个zip包格式，用于python编译过的模块的安装，较快，它的出现是为了替代Eggs。
pip也可以直接安装wheel包。

常用命令
--------------------

1. pip3, --help 查看用法
2. virtualenv
3. 

主要相关工具和包为：
--------------------

-  setuptools
-  pip
-  virtualenv

目标是用PIP安装包。好处多，如自动下载安装依赖包
-----------------------------------------------

怎么装上pip
-----------

路径1:get-pip.py法 把pip/easy_install一起装了
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| `download get-pip.py <https://bootstrap.pypa.io/get-pip.py>`__
| curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
| python get-pip.py

| `Download get-pip.py <https://bootstrap.pypa.io/get-pip.py>`__
| python get-pip.py #install or upgrade pip. Additionally, it will
  install setuptools and wheel
| python get-pip.py –prefix=/usr/local/ #装到指定的目录
| python -m pip install –upgrade pip setuptools wheel #up to date copies
  of the setuptools and wheel projects are useful

| pip can automatically install dependency
| pip can install from either Source Distributions (sdist) or Wheels,
| pip will prefer a compatible wheel.
| Wheels are a pre-built distribution format that provides faster
  installation compared to Source Distributions (sdist), especially when
  a project contains compiled extensions.

路径2: 源包setup.py python setup.py install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 用源包先装setuptools,再装pip
| `tutorial-help-install
  package <https://packaging.python.org/tutorials/installing-packages/>`__
| `setuptools包下载 <https://pypi.org/project/setuptools/#files>`__
| `PIP包下载 <https://pypi.org/project/pip/#files>`__
| 解压进入目录执行,
| python setup.py install

路径3:easy_install 法
~~~~~~~~~~~~~~~~~~~~~

| `easy_install下载地址 <https://pypi.python.org/pypi/ez_setup>`__
| python ez_setup.py
| 会在python的安装目录中生成scripts目录，其中有easy_install.exe

| 然后用
| easy_install pip

easy_install是由PEAK(Python Enterprise Application
Kit)开发的setuptools包里带的一个命令，所以使用easy_install实际上是在调用setuptools来完成安装模块的工作。

pip文档链接
~~~~~~~~~~~

| `pip docs <https://pip.pypa.io/>`__
| `pip Reference
  Guide <https://pip.pypa.io/en/latest/reference/index.html>`__
| `dependency management
  tutorial <https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies>`__

pip命令用法
~~~~~~~~~~~

| 如果 Python2 和 Python3 同时有 pip，则使用方法如下：
| python3 -m pip install XXX

| pip –version
| pip –help
| pip install -U pip # 升级 pip
| python -m pip install -U pip
| pip install SomePackage # 最新版本 pip install SomePackage==1.0.4 #
  指定版本
| pip install ‘SomePackage>=1.0.4’ # 最小版本
| pip uninstall SomePackage

| pip freeze > requirements.txt #当前系统包系统
| pip install -r requirements.txt

virtualenv
----------

`virtualenv <https://pypi.org/project/virtualenv/#files>`__

::

    virtualenv <pathName> #在pathname处建立环境，可以 -p 指定母python路径  
    \path\to\env\Scripts\activate.bat  
    deactivate.bat  


| `virtualenv docs <http://virtualenv.pypa.io/>`__
| `venv docs <https://docs.python.org/3/library/venv.html>`__
| `Pipenv <https://packaging.python.org/key_projects/#pipenv>`__

web资源
=======

| python - pypi pypa
| Perl - CPAN
| Ruby - Gems

| latex - CTAN
| sublime - packagecontol.io

website
-------

-  main page:

   https://www.python.org

- help
  
  `docs.python.org <https://docs.python.org>`_ 

-  package get:

| PYPI/PYPA python package
| https://www.pypa.io/
| https://pypi.org/
| - tutorial:教程 https://readthedocs.org/projects/python/
| tutorial
| https://packaging.python.org/tutorials/
| https://packaging.python.org/tutorials/installing-packages/#

package
=======

mp3
--------------------

eye3D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`eye3D help <https://eyed3.readthedocs.io/en/latest/>`_ 

:: 

pip3 install python-magic-bin :(Windows dep)
pip3 install eyeD3
pip3 install eyeD3[display-plugin]


Development Dependencies(for development work)

::

  pip install -r requirements/test.txt $ pip install -r requirements/dev.txt

- 从包安装：

::

  tar xzf eyeD3-X.Y.Z.tar.gz
  cd eyeD3-X.Y.Z
  This may require root access
  python setup.py install


安装总结

::

  pip install eyeD3
  pip install python-magic-bin==0.4.
  不执行这一句会报错的。eyeD3环境因为他整了好久。

下面给网上安装问题

::

  pip install msgp
  #不安装会报错distributed 1.21.8 requires msgpack, which is install
  pip install python-magic-bin==0.4
  #不安装，在import eyed3时会报错ImportError: failed to find libmagChecyour installat
  pip install ey
  实际安装3个包eyeD3-0.8.7 pathlib-1.0.1 python-magic-0.4
  版权声明：本文为CSDN博主「优绎」的原创文章，遵循Cby-sa版权协议，转载请附上原文出处链接及本声明。
  原文链接：https://blog.csdn.net/YeoYi/article/details/80880639

使用命令行
::

  eyeD3 --encoding utf16-be --add-lyric ch01.rst ch01.mp3
  eyeD3 --remove-all-lyric ch01.mp3