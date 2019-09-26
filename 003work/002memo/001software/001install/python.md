

python
======


# install

## 主要相关工具和包为： 
- setuptools
- pip
- virtualenv


## 目标是用PIP安装包。好处多，如自动下载安装依赖包

## 怎么装上pip

### 路径1:get-pip.py法 把pip/easy_install一起装了

[download get-pip.py](https://bootstrap.pypa.io/get-pip.py)  
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
python get-pip.py

[Download get-pip.py](https://bootstrap.pypa.io/get-pip.py)  
python get-pip.py  #install or upgrade pip. Additionally, it will install setuptools and wheel  
python get-pip.py --prefix=/usr/local/ #装到指定的目录  
python -m pip install --upgrade pip setuptools wheel #up to date copies of the setuptools and wheel projects are useful

pip can automatically install dependency  
pip can install from either Source Distributions (sdist) or Wheels,   
pip will prefer a compatible wheel.  
Wheels are a pre-built distribution format that provides faster installation compared to Source Distributions (sdist), especially when a project contains compiled extensions.


### 路径2: 源包setup.py python setup.py install

用源包先装setuptools,再装pip  
[tutorial-help-install package](https://packaging.python.org/tutorials/installing-packages/)  
[setuptools包下载](https://pypi.org/project/setuptools/#files)  
[PIP包下载](https://pypi.org/project/pip/#files)  
解压进入目录执行,  
python setup.py install  


### 路径3:easy_install 法 

[easy_install下载地址](https://pypi.python.org/pypi/ez_setup)  
python ez_setup.py  
会在python的安装目录中生成scripts目录，其中有easy_install.exe

然后用  
easy_install pip

easy_install是由PEAK(Python Enterprise Application Kit)开发的setuptools包里带的一个命令，所以使用easy_install实际上是在调用setuptools来完成安装模块的工作。



### pip文档链接

[pip docs](https://pip.pypa.io/)  
[pip Reference Guide](https://pip.pypa.io/en/latest/reference/index.html)  
[dependency management tutorial](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)  

### pip命令用法

如果 Python2 和 Python3 同时有 pip，则使用方法如下：  
python3 -m pip install XXX

pip --version  
pip --help  
pip install -U pip                   # 升级 pip  
python -m pip install -U pip  
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本  
pip install 'SomePackage>=1.0.4'     # 最小版本  
pip uninstall SomePackage

pip freeze > requirements.txt    #当前系统包系统  
pip install -r requirements.txt



## virtualenv

[virtualenv](https://pypi.org/project/virtualenv/#files)

    virtualenv <pathName> #在pathname处建立环境，可以 -p 指定母python路径  
    \path\to\env\Scripts\activate.bat  
    deactivate.bat  

[virtualenv docs](http://virtualenv.pypa.io/)  
[venv docs](https://docs.python.org/3/library/venv.html)  
[Pipenv](https://packaging.python.org/key_projects/#pipenv)  



# web资源
python - pypi pypa  
Perl - CPAN  
Ruby - Gems  

latex - CTAN  
sublime - packagecontol.io  

## website

- main page:

  https://www.python.org

- package get:

PYPI/PYPA python package  
https://www.pypa.io/  
https://pypi.org/  
- tutorial:教程
https://readthedocs.org/projects/python/  
tutorial  
https://packaging.python.org/tutorials/  
https://packaging.python.org/tutorials/installing-packages/#  


# package




