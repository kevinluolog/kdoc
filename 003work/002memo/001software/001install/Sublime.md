


<!-- MarkdownTOC levels="1,2,3,4,5,6" autolink="true" style="unordered" uri_encoding="false" -->

- [sublime](#sublime)
- [basic information](#basic-information)
- [website](#website)
- [install components](#install-components)
  - [package control install](#package-control-install)
    - [如果想要删除插件，](#如果想要删除插件，)
    - [用Package Control安装插件的方法](#用package-control安装插件的方法)
  - [sublimegit package install](#sublimegit-package-install)
    - [sumlimeGit usage用法](#sumlimegit-usage用法)
- [有用的插件](#有用的插件)
  - [ConvertToUTF8](#converttoutf8)
  - [markdown, 也可以用简书直接编辑查看](#markdown-也可以用简书直接编辑查看)
    - [MarkdownEditing](#markdownediting)
    - [OmniMarkupPreviewer](#omnimarkuppreviewer)
      - [TOC render Preview支持](#toc-render-preview支持)
      - [OmniMarkupPreviewer中支持LaTeX公式显示：](#omnimarkuppreviewer中支持latex公式显示：)
    - [Markdown Extended](#markdown-extended)
    - [MarkdownLivePreview](#alt+m 在sublime启动并列窗口,实时查看结果)
    - [MarkdownTOC](#markdowntoc)
  - [Restructured Text \(RST\) Snippets](#restructured-text-rst-snippets)
  - [Anaconda - python completion](#anaconda---python-completion)
  - [HexViewer](#hexviewer)
  - [latex tools](#latex-tools)
- [tips](#tips)
  - [快捷键介绍](#快捷键介绍)
  - [列编辑模式](#列编辑模式)
  - [hex查看模式](#hex查看模式)
- [FAQ](#faq)
  - [字体怎么调整回来](#字体怎么调整回来)
  - [缺省保存为UTF8文件](#缺省保存为utf8文件)
  - [怎么用正则模式查找替换](#怎么用正则模式查找替换)
  - [出现服务找不到，preview不成功如下提示](#出现服务找不到，preview不成功如下提示)
- [LaTex公式案例](#latex公式案例)

<!-- /MarkdownTOC -->

sublime
=======

# basic information

# website

- main page

- package get

- help

- tutorial


# install components

1. portable sublime
2. package control install
3. packages
 1. sublimeGit

## package control install

portable sublime 缺省没有安装，可2个方法安装
1. tools-package control install
装完此菜单消失，preferences出现->package setting; ->package control
2. https://packagecontrol.io/installation
在页面查看2种另外的方法，自动和手动


### 如果想要删除插件，

Ctrl+Shift+P调出命令面板，输入remove，调出Remove Package选项并回车，选择要删除的插件即可，当然，更新插件，upgrade packages，通过简单的几个命令就可以方便的管理我们的插件了


### 用Package Control安装插件的方法

按下Ctrl+Shift+P调出命令面板
输入install 调出 Install Package 选项并回车，然后在列表中选中要安装的插件。
不爽的是，有的网络环境可能会不允许访问陌生的网络环境从而设置一道防火墙，而Sublime Text 3貌似无法设置代理，可能就获取不到安装包列表了。

## sublimegit package install

tools-command palette ctl+shift+p
pci package control install
等待载入package information,然后在命令行输入sublimeGit
安装完后，在
preference->package Settings-> 此处出现安装的sublimeGit
同时在
preference->package settings-> package control -> user setting 中可以看到已经增加选项


### sumlimeGit usage用法

https://sublimegit.readthedocs.io/en/latest/

【下面的有些问题，看readthedocs就行了】
full tutorial, go to
https://docs.sublimegit.net/tutorial.html
https://sublimegit.readthedocs.io/en/latest/tutorial.html
how to get set up
https://docs.sublimegit.net/quickstart.html




# 有用的插件

超级文本编辑器Sublime Text3
https://blog.csdn.net/enjoyyl/article/details/50057491# _90

##  ConvertToUTF8

比上面的那个要方便，直接在菜单栏中可以转了，专为中文设计，妈妈再也不通担心中文乱码问题了

## markdown, 也可以用简书直接编辑查看

### MarkdownEditing

### OmniMarkupPreviewer 

#### TOC render Preview支持

[右键menu preview markdown in browser, export/copy markdown as html]
1. 如果你发现它不支持markdown目录的预览生成，那么不是它不行，是你没配置。
   当然首先是装markdwon TOC插件
2. 复制Preferences -> Package Settings -> OmniMarkupPreviewer -> Settings - Default 中的内容到Settings - Users中，
3. 并在 // MarkdownRenderer options区域，即
“renderer_options-MarkdownRenderer”: 中添加"toc"，代码如下
        "extensions": ["tables", "strikeout", "fenced_code", "codehilite", "toc"]
4. 然后通过Ctrl+Alt+O快捷键生成HTML预览，或者Ctrl+Alt+X导出。

#### OmniMarkupPreviewer中支持LaTeX公式显示：

1.设置。公式的渲染使用了MathJax库，所以需要在OmniMarkupPreviewer的设置中，将"mathjax_enabled"设置为“true”。之后MathJax会在后端自动下载。
2.可能是网速的原因，MathJax库下载很慢，所以可以选择手动安装。
下载MathJax：
https://github.com/downloads/timonwong/OmniMarkupPreviewer/mathjax.zip
然后解压到下面的目录里：Sublime Text 2\Packages\OmniMarkupPreviewer\public
之后在目录“Sublime Text 2\Packages\OmniMarkupPreviewer”中创建一个空文件MATHJAX.DOWNLOADED这样子MathJax就安装成功了。
测试，输入下面内容：
This expression 
$\sqrt{3x-1}+(1+x)^2$ is an example of a $\LaTeX$ inline equation.he Lorenz Equations:
$$\begin{aligned}\dot{x} & = \sigma(y-x) \\\dot{y} & = \rho x - y - xz \\\dot{z} & = -\beta z + xy\end{aligned}$$

在Sublime Text 3中使用命令：
Ctrl+Alt+O：在浏览器中预览
Ctrl+Alt+X：输出为HTML文件
Ctrl+Alt+C：复制为HTML文件

### Markdown Extended

### MarkdownLivePreview [alt+m 在sublime启动并列窗口,实时查看结果]

### MarkdownTOC
  
Sublime Text 3 plugin for generating a Table of Contents (TOC) in a Markdown document.
- [Features](https://github.com/naokazuterada/MarkdownTOC# features)
- [Usage](https://github.com/naokazuterada/MarkdownTOC# usage)

## Restructured Text (RST) Snippets

装完后preferences-package setting中的名字为，sumlime-rst-completion
http://www.addonhunt.com/sublime/p05jg.html
[Restructured Text (RST) Snippets](https://packagecontrol.io/packages/Restructured%20Text%20(RST)%20Snippets)

- 用法链接
  - [本地README](H:\tmp_H\001.work\002git\000study\000misc\sublime-rst-completion\README.rst)
  - [Git-README](https://github.com/kevinluolog/sublime-rst-completion/blob/master/README.rst)
- 快捷键
  -magic table
   1. grid table `ctrl+t, enter`
     1. keep the column width fixed, `ctrl+t, r` (``super+shift+t, r`` in Mac)
     2. merge simple cells: ``ctrl+t, down`` ``ctrl+t, up``
     3. ``


   2. simple table `ctrl+t, s`
     1. `dfd`
     2. ``
     3. ``

  - Adjust header level： `ctrl+-` | `ctrl+keypad-`
  - 补齐: `tab`
  - jump between headers: `alt+down` | `alt+up`
  - add new footnote: `alt+shift+f`
    go back to the reference with `shift+up`
  - 
-usage snippets

 |shortcut     |result             |key binding             |   
 |-------------|-------------------|------------------------|
 |``h1``       |Header level 1     |see `Headers`_          |   
 |``h2``       |Header level 2     |                        |   
 |``h3``       |Header level 3     |                        |   
 |``e``        |emphasis           |``ctrlalti``            | 
 |             |                   |(``supershifti`` on Mac)| 
 |``se``       |strong emphasis    |``ctrlaltb``            | 
 |             |(bold)             |(``supershiftb`` on Mac)| 
 |``lit``      |literal text       |``ctrlaltk``            | 
 |``literal``  |(inline code)      |(``supershiftk`` on Mac)| 
 |``list``     |unordered list     |see `Smart Lists`_      |   
 |``listn``    |ordered list       |                        |   
 |``listan``   |auto ordered list  |                        |   
 |``def``      |term definition    |                        |   
 |``code``     |codeblock (sphinx) |                        |  
 |``source``   |preformatted (``::`` block)      |
 |``img``      |image              |                        |   
 |``fig``      |figure             |                        |   
 |``table``    |simple table       |``ctrlt`` see `Magic Tables`|  
 |``link``     |refered hyperlink  |                        |   
 |``linki``    |embeded hyperlink  |                        |   
 |``fn``       |autonumbered       |``altshiftf`` see `Magic| 
 |``cite``     |footnote or cite   |Footnotes`_             |   
 |``quote``    |Quotation (`epigraph`)|Tables`_             |   

 |shortcut     |
 |-------------| 
 |``attention``| 
 |``caution``  | 
 |``danger``   | 
 |``error``    | 
 |``hint``     | 
 |``important``| 
 |``note``     | 
 |``tip``      | 
 |``warning``  | 


-编译Python项目文档

Python的项目文档，大都基于 reStructuredText 撰写， Sphinx 发布，如何在 Sublime 中，通过按 Ctrl + B 直接编译工程呢？很简单，点击 Tools --> Build System --> New Build System ，输入
```
{
	"shell_cmd": "make html"
}
```
保存，打开你工程的 Makefile 文件，然后按 Ctrl + Shift + B 选择你刚才保存的那个名字，就可以自动编译成html文档了。

## Anaconda - python completion

Anaconda 强大的补全工具, 还能实时看文档, 转到定义, 自动格式化代码
doc:http://damnwidget.github.io/anaconda/
http://damnwidget.github.io/anaconda/

## HexViewer

hex查看模式

## latex tools
[git latextools项目](https://github.com/SublimeText/LaTeXTools)
[DOC on readthedocs](https://latextools.readthedocs.io/en/latest/)
- 配套
1. sumatrapdf
[sumatraPdf网址](https://www.sumatrapdfreader.org/free-pdf-reader.html)
[gitREP sumatrpdf](https://github.com/sumatrapdfreader/sumatrapdf)

# tips

## 快捷键介绍
看这里，[Sublime Text3使用指南](https://www.cnblogs.com/ma-dongdong/p/7653231.html)

## 列编辑模式

1. 方式一
Shift+鼠标右键
鼠标中键
2. 方式二
sublime  对 列编辑模式 Key  binding设置如下：
路径：Preferences→Key Bindings  
   { "keys": ["ctrl+alt+up"], "command": "select_lines", "args": {"forward": false} },
   { "keys": ["ctrl+alt+down"], "command": "select_lines", "args": {"forward": true} },
但ctrl+alt+up/down 和windows的快捷键设置冲突，我们可以自定义上述设置
路径：Preferences→Key Bindings – User
[{ "keys": ["alt+up"], "command": "select_lines", "args": {"forward": false} },
 { "keys": ["alt+down"], "command": "select_lines", "args": {"forward": true} },
]    

3. 方式三
选中需要进行列编辑的多行，然后按下Ctrl+Shift+L也可以开启列编辑模式。

## hex查看模式

HexViewer
Ctrl + Shift + P
安装HexViewer
Tools > Packages > Hex Viewer > Toggle Hex View

# FAQ

## 字体怎么调整回来

preferences->font 
- 快捷键

  larger: ctrl+= smaller:ctrl+shift+ keypad+(注意一定要是小键盘上的+)
- 和OmnMarkupPreview中切换标题的快捷键的误用
  增大标题: ctrl+  减小标题: ctrl+ keypad+

## 缺省保存为UTF8文件
Preferences 设置-默认
Preferences.sublime-settings文件：
// 默认编码格式
"default_encoding": "UTF-8",

##怎么用正则模式查找替换
(#{1,6}): 表示查找1到6个#的字符,()表示匹配的意思，并放入$1
替换成$1 ：表示在原先的标题符号后面加上空格

##出现服务找不到，preview不成功如下提示
>Error: 404 Not Found
>Sorry, the requested URL 'http://127.0.0.1:51004/view/28' caused an error:
>'buffer_id(28) is not valid (closed or unsupported file format)'
>**NOTE:** If you run multiple instances of Sublime Text, you may want to adjust
>the `server_port` option in order to get this plugin work again.

```
sublime Text > Preferences > Package Settings > OmniMarkupPreviewer > Settings - User
粘贴下列的扩展去代替原来的扩展（我用了方法1）
{
    "renderer_options-MarkdownRenderer": {
        "extensions": ["tables", "fenced_code", "codehilite"]
    }
}
```

移除了"Strikethrough" 就好了，但是发现把这个再加回也好了。不知道什么原因

# LaTex公式案例

$$latex
f(x;\mu,\sigma^2) = \frac{1}{\sigma\sqrt{2\pi}} e^{ -\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2 }
$$

This expression 
$\sqrt{3x-1}+(1+x)^2$ is an example of a $\LaTeX$ inline equation.he Lorenz Equations
$$\begin{aligned}\dot{x} & = \sigma(y-x) \\\dot{y} & = \rho x - y - xz \\\dot{z} & = -\beta z + xy\end{aligned}$$




