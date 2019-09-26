#############
memo of latex
#############

.. contents:: 目录
.. section-numbering::

.. 
 #########
 正标题
 #########

.. 
 ***********
 Kl副标题
 ***********

.. 
    this convention is used in Python’s Style Guide for documenting which you may follow:
    (h1-h8: in sublime package of "restructerTextImproved")
    # with overline, for parts
.. 
 h1 * with overline, for chapters
 h2 =, for sections
 h3 -, for subsections
 h4 ^, for subsubsections
 h5 ", for paragraphs
 h6 +,
 h7 ~,
 h8 #,
 ***
 h1 
 ***
 
 h2 
 ===
 
 h3 
 ---
 
 h4 
 ^^^
 
 h5 
 """
 
 h6 
 +++
 
 
 h6 
 ~~~
 
 h8 
 ###

安装方法
========

tex
---

MiTex
^^^^^

- CTEX 指的是CTEX 中文套装
  Windows下则有MiKTEX 和fpTEX

- MiKTeX
  添加中文支持, 点开 Package Manager admin), 安装 CJK 和 CJK-fonts 即可

texlive
^^^^^^^

IDE
---

TeXmaker
^^^^^^^^

::

    TeXmaker设置

    打开TexMaker->选项->配置TexMaker->命令，配置前两项如下：(如果texlive的/bin/win32/路径已经在PATH中了，就缺省就可以了)

    latex: "C:/texlive/2016/bin/win32/latex.exe" -interaction=nonstopmode %.tex

    Dvipm: "C:/texlive/2016/bin/win32/pdflatex.exe" -interacti on=nonstopmode %.tex


TeXstudio
^^^^^^^^^

TeXworks
^^^^^^^^

这是texlive 安装自带


SublimeText配置TexLive编辑和编译环境
====================================

- `Tex-Live安装及SublimeText 配置Tex-Live编辑和编译环境 <htt://blog.csdn.net/meiqi0538/article/details/82915406>`__

  1. LatexTools插件
  2. SumatraPDF配置

- `下载路径 <https://www.sumatrapdfreader.org/  download-free-pdf-viewer.html>`__
- 【设置】-》【选项】

  "C:\CommonTools\Sublime Text 3\Sublime Text 3\sublime_text.exe" "%f:%l"

::

    「LaTeXTools.sublime-settings」做以下配置：
    "windows":{
        "texpath" : "C:\\commontools\\texlive2018\\texlive\\2018\\bin\\win32;$PATH",
    "distro" : "texlive"
    "sumatra": "C:\\commontools\\texlive2018\\sumatrapdf\\sumatrapdf.exe",
    }
        "builder": "simple"
    }

- 测试test.tex

 ::

    \documentclass`UTF8]{ctexart}
    \begin{document}
    This is the context of the article.
    这就是文章的所有内容。
    \end{document}



CLI绘图工具
===========

TikZ和PGF
---------

TiKZ学习
^^^^^^^^

TikZ和PGF是一种用在TeX上的**CLI绘图工具**。
CLI和GUI是两种常见的绘图方式。

CLI: Commad Line Interface

    是所想即所得（WYTIWYG）的，通过类编程的思想实现绘图，这种方式往往能够生成精确控制的函数图，常见的有PostScript、PGF、Asymptote、PSTricks等。

GUI: Graphic User Interface

    后者则是所见即所得（WYSIWYG）的，常见的有CorelDraw、Illustrator、Photoshop、GIMP、Office、Visio等。 

TikZ和PGF的关系: classifier
 
    TikZ和PGF的关系则是高层和底层的关系，简单说来，TikZ基于PGF，它可以帮助我们用更易于理解的方式创建复杂的图形。

PGF: 全名
 
    PGF的全名是“portable graphics format”，或者“pretty, good, functional”

TikZ : 全名
 
    TikZ的命名更有趣，采用的是递归式的取名：“TikZ ist kein Zeichenprogramm”(TikZ is not a drawing program)。
    类似的取名最出名的恐怕就是GNU（GNU is Not Unix）了。

1. `TikZ的官网：内含很多示例代码 <http://www.texample.net/tikz/>`__
2. `LateX在线编辑工具 <https://www.overleaf.com>`__
3. `TikZ快速入门文档 <http://cremeronline.com/LaTeX/minimaltikz.pdf>`__
4. `LaTeX Graphics using TikZ: A Tutorial p1 <https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ:_A_Tutorial_for_Beginners_(Part_1)%E2%80%94Basic_Drawing>`__
5. `TikZ绘图学习笔记 <http://blog.sina.com.cn/s/blog_97d042500101g4jk.html>`__
   LaTeX中支持PGF(Portable Graphics Format/Pretty,Good,Functional).PGF能够画出精确的图像，但因为非所见即所得，所以学习起来也有一定难度。

   在**TeX中绘制图形有很多方法**，例如**picture环境、pstricks宏包、xypic宏包、dratex宏包、metapost宏包等**。PGF也是其中一种。PGF的结构包括系统层、基础层和前段层。在通常情况下，用户只会接触到如TikZ的前端层。TikZ是PGF的扩展，由同一个作者开发。

6. `Latex--TikZ和PGF--高级文本绘图，思维绘图，想到--得到！ <https://www.cnblogs.com/tsingke/p/6649800.html>`__
   这个网址收集了比较齐全的学习网址
7. `tikz & pgf manual - CTAN: Package pgf <https://www.ctan.org/pkg/pgf>`__
   用户手册，源码
   `gitHub源码仓库 <https://github.com/pgf-tikz/pgf>`__



TiKZ绘图
^^^^^^^^

1. 使用 LaTeX 宏包 TikZ 来绘制矢量流程图

   - `Latex 绘制流程图 <https://blog.csdn.net/tuzixini/article/details/72957211>`__
   - `LaTeX中TikZ绘图备忘一 <https://blog.csdn.net/weixin_44420912/article/details/86418033>`__
     编译器结构图
   - `latex tikz使用总结 <https://blog.csdn.net/sunwukong54/article/details/28292097>`__

程序语句使用绘图
^^^^^^^^^^^^^^^^

#. `LaTex中使用循环连续绘图的例子 <https://blog.csdn.net/rumswell/article/details/37962003>`__

::

    %%====================================================
    \begin{frame}[fragile]
        由 $3$ 个人群可以构成$2^3 = 8$张 \remph{人际关系图},只需分析如下 \remph{$4$}张图即可:\\[12pt] %
        \setcounter{maincounter}{0}%设置计数器的值
        %每次增加一个值用\stepcounter{maincounter}
        \begin{tikzpicture}[line width = 1.0pt]
        \pgfmathsetmacro{\h}{1.4}   %两点的水平间距
        \pgfmathsetmacro{\v}{1.4}   %两点的垂直间距
        % %------------------------------------------------------
        \foreach \r/\c in {0/0,2/0,4/0,6/0}  
        {    
            \stepcounter{maincounter} %增加计数器的值
            \setcounter{secondcounter}{0}%设置计数器的值
            %定义原点坐标
            \coordinate  (P0) at (\r,\c);    
            
            \path (P0)  node[circle,fill=red,inner sep=2pt](a){$a$};  
            \path (a)+(\h,0 )  node[circle,fill=red,inner sep=2pt](b){$b$}; 
            \path ($ (a)!0.5! (b) $)+(0,\v)   node[circle,fill=red,inner sep=2pt](c){$c$}; 
            \path ($ (a)!0.5! (b) $)+(0,-0.5)   node (T){ $\left( \themaincounter \right) $}; 
            %画直线  
            \foreach \from/\to in {a/b,a/c,b/c}  
            {
                \stepcounter{secondcounter} %增加计数器的值
                \ifthenelse{\value{secondcounter}<\value{maincounter}}{\draw[dashed] (\from) -- (\to)  ;}{\draw[blue] (\from) -- (\to)  ;}
            }
            
        }
        \end{tikzpicture}
    \end{frame}


3. `ifthen宏包使用——条件判断与循环语句 <https://blog.csdn.net/lishoubox/article/details/7316224>`__

    \ifthenelse{判断条件}{肯定结构}{否定结构}
    \whiledo{判断条件}{while语句}

::

    \documentclass{article}
    \usepackage{ifthen}
    \begin{document}

    \newcommand{\oddeven}[1]{Number #1 is %
    \ifthenelse{\isodd{#1}}{odd}{even}  }
    \oddeven{4}.\\ \oddeven{5}

    \newcounter{MYctr}
    \whiledo{\value{MYctr}<5}%
    {你会喜欢用~LaTeX~的。%
    \stepcounter{MYctr}}

    \end{document}



pgfplots绘图包
--------------

`在LaTeX中使用强大的pgfplots绘图包 <htt://blog.csdn.net/stereohomology/article/details/24266409>`__

PSTricks绘图
------------

使用PSTricks绘制精致的流程图
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`使用PSTricks绘制精致的流程图 <http://blog.sina.com.cn/s/blog_5e16f1770102e77g.html>`__
一个好用的package地址在http://texnik.dante.de/tex/generic/pstricks-add/  大家也可以下载替换系统的 texlive/2011/texmf-local/tex/generic/pstricks-add/pstricks-add.tex 文件，或者就放在自己编码的文件目录下也可。
我们可以利用已有的命令绘制出精致的流程图


TIPS
===

MISC
----

1. 参考文献可以搜bibtex，
2. 制作幻灯片可以搜beamer。


FAQ
===

PDFLaTeX和XeLaTeX有什么区别
---------------------------

区别: pdflatex and xelatex
    pdfLaTeX是比较原始的版本，对Unicode的支持不是很好，所以显示汉字需要使用CJK宏包。它不支持操作系统的truetype字体(\*.ttf)，只能使用type1字体。优点是支持的宏包比较多，有些老一点的宏包必须用pdfLaTeX来编译。XeLaTeX是新的Unicode版本，内建支持Unicode(UTF-8)，自然也包括汉字在内，而且可以调用操作系统的truetype字体。如果你的文档有汉字，那么推荐用XeLaTeX。缺点是不支持某一些宏包。

LaTeX 与 TeX 有什么本质区别
---------------------------

TeX是排版引擎，是给机器下指令的。它有好多种具体的实现。
LaTeX是宏包，方便用户调用TeX。
另外，比如XeTeX同样也是排版引擎，是TeX的一种实现，增加了对万国码的支持。
XeLaTeX是宏包，是指使用宏包LaTeX调用排版引擎XeTeX。



