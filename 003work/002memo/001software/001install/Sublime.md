


<!-- MarkdownTOC levels="1,2,3,4,5,6" autolink="true" style="unordered" uri_encoding="false" -->

- [sublime](#sublime)
- [basic information](#basic-information)
- [website](#website)
- [install components:](#install-components)
    - [package control install:](#package-control-install)
        - [如果想要删除插件，](#如果想要删除插件，)
        - [用Package Control安装插件的方法：](#用package-control安装插件的方法：)
    - [sublimegit package install:](#sublimegit-package-install)
        - [sumlimeGit usage用法:](#sumlimegit-usage用法)
- [有用的插件：](#有用的插件：)
    - [~~ ConvertToUTF8：](#~~-converttoutf8：)
    - [~~ markdown, 也可以用简书直接编辑查看](#~~-markdown-也可以用简书直接编辑查看)
        - [MarkdownEditing](#markdownediting)
        - [OmniMarkupPreviewer](#omnimarkuppreviewer)
        - [Markdown Extended](#markdown-extended)
        - [MarkdownLivePreview](#alt+m 在sublime启动并列窗口,实时查看结果)
        - [MarkdownTOC](#markdowntoc)
    - [~~reStructuredText](#~~restructuredtext)
    - [~~ Anaconda - python completion](#~~-anaconda---python-completion)
    - [~~](#~~)

<!-- /MarkdownTOC -->

sublime
=======

#basic information
#website
- main page:

- package get:

- help:

- tutorial:


#install components:
1. portable sublime
2. package control install
3. packages
 1. sublimeGit

##package control install:
portable sublime 缺省没有安装，可2个方法安装
1. tools-package control install
装完此菜单消失，preferences出现->package setting; ->package control
2. https://packagecontrol.io/installation
在页面查看2种另外的方法，自动和手动


###如果想要删除插件，
Ctrl+Shift+P调出命令面板，输入remove，调出Remove Package选项并回车，选择要删除的插件即可，当然，更新插件，upgrade packages，通过简单的几个命令就可以方便的管理我们的插件了


###用Package Control安装插件的方法：
按下Ctrl+Shift+P调出命令面板
输入install 调出 Install Package 选项并回车，然后在列表中选中要安装的插件。
不爽的是，有的网络环境可能会不允许访问陌生的网络环境从而设置一道防火墙，而Sublime Text 3貌似无法设置代理，可能就获取不到安装包列表了。

##sublimegit package install:
tools-command palette ctl+shift+p
pci package control install
等待载入package information,然后在命令行输入sublimeGit
安装完后，在
preference->package Settings-> 此处出现安装的sublimeGit
同时在
preference->package settings-> package control -> user setting 中可以看到已经增加选项


###sumlimeGit usage用法:
https://sublimegit.readthedocs.io/en/latest/

【下面的有些问题，看readthedocs就行了】
full tutorial, go to:
https://docs.sublimegit.net/tutorial.html
https://sublimegit.readthedocs.io/en/latest/tutorial.html
how to get set up:
https://docs.sublimegit.net/quickstart.html




#有用的插件：
超级文本编辑器Sublime Text3
https://blog.csdn.net/enjoyyl/article/details/50057491#_90
##~~ ConvertToUTF8：
比上面的那个要方便，直接在菜单栏中可以转了，专为中文设计，妈妈再也不通担心中文乱码问题了
##~~ markdown, 也可以用简书直接编辑查看
###MarkdownEditing
###OmniMarkupPreviewer 
[右键menu preview markdown in browser, export/copy markdown as html]
如果你发现它不支持markdown目录的预览生成，那么不是它不行，是你没配置。复制Preferences -> Package Settings -> OmniMarkupPreviewer -> Settings - Default 中的内容到Settings - Users中，并在 // MarkdownRenderer options区域，即
“renderer_options-MarkdownRenderer”: 中添加"toc"，代码如下：
        "extensions": ["tables", "strikeout", "fenced_code", "codehilite", "toc"]
然后通过Ctrl+Alt+O快捷键生成HTML预览，或者Ctrl+Alt+X导出。

###Markdown Extended
###MarkdownLivePreview [alt+m 在sublime启动并列窗口,实时查看结果]

###MarkdownTOC
  
Sublime Text 3 plugin for generating a Table of Contents (TOC) in a Markdown document.
- [Features](https://github.com/naokazuterada/MarkdownTOC#features)
- [Usage](https://github.com/naokazuterada/MarkdownTOC#usage)

##~~reStructuredText
Restructured Text (RST) Snippets
http://www.addonhunt.com/sublime/p05jg.html
https://packagecontrol.io/packages/Restructured%20Text%20(RST)%20Snippets

编译Python项目文档
Python的项目文档，大都基于 reStructuredText 撰写， Sphinx 发布，如何在 Sublime 中，通过按 Ctrl + B 直接编译工程呢？很简单，点击 Tools --> Build System --> New Build System ，输入：
{
	"shell_cmd": "make html"
}
保存，打开你工程的 Makefile 文件，然后按 Ctrl + Shift + B 选择你刚才保存的那个名字，就可以自动编译成html文档了。

##~~ Anaconda - python completion
Anaconda 强大的补全工具, 还能实时看文档, 转到定义, 自动格式化代码
doc:http://damnwidget.github.io/anaconda/
http://damnwidget.github.io/anaconda/

##~~

