# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Hi post'
copyright = '2019, kevinluo'
author = 'kevinluo'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.graphviz'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# zh_CN – Simplified Chinese
# zh_TW – Traditional Chinese
# en – English
# 
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# kl+: orginal default theme
# html_theme = 'alabaster'

# kl+ better theme, not pretty
# from better import better_theme_path
# html_theme_path = [better_theme_path]
# html_theme = 'better'

# kl+ readdocs theme
# import sphinx_rtd_theme
# extensions = [
#     'sphinx_rtd_theme',
# ]
# html_theme = "sphinx_rtd_theme"

# html_theme=""
# html_theme="agogo"
# html_theme="basic"
html_theme="bizstyle"
#html_theme="classic"
# html_theme="default"
# html_theme="epub"
# html_theme="haiku"
# html_theme="nature"
# html_theme="nonav"
# html_theme="pyramid"
# html_theme="scrolls"
# html_theme="sphinxdoc"
#html_theme="traditional"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_copy_source=False
# If true, the reST sources are included in the HTML build as _sources/name. The default is True.
# 
html_show_sourcelink=False
# If true (and html_copy_source is true as well), links to the reST sources will be added to the sidebar. The default is True.

# html_show_copyright="True"
# If true, “(C) Copyright …” is shown in the HTML footer. Default is True.
# New in version 1.0.
 
html_show_sphinx=False
# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.

# -- Options for latex output -------------------------------------------------

latex_engine='xelatex'
# The LaTeX engine to build the docs. The setting can have the following values:
# 'pdflatex' – PDFLaTeX (default)
# 'xelatex' – XeLaTeX
# 'lualatex' – LuaLaTeX
# 'platex' – pLaTeX (default if language is 'ja')


latex_elements = {
    # Additional stuff for the LaTeX preamble.
    #'preamble': r'\input{fix-deeplynested.sty}',
    #'preamble': r'\usepackage{mystyle}',

    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
\usepackage{enumitem}
\setlistdepth{99}
''',
    'fontpkg': r'''
\setCJKmainfont{FZYingBiXingShu-S16S}
''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

#中文字体
#CJKmainfont: "FZShouJinShu-S10S"
#CJKmainfont: "Microsoft YaHei"
#CJKmainfont: "FZLiShu-S01S"
#CJKmainfont: "FZLiShu-S01T"
#CJKmainfont: "经典行书简"
#CJKmainfont: "书体坊米芾体"
#CJKmainfont: "经典隶书简"
#CJKmainfont: "FZWeiBei-S03"
#CJKmainfont: "FZShouJinShu-S10S"
#CJKmainfont: "Adobe Fangsong Std"
#CJKmainfont: "WenQuanYi Zen Hei"
#FontType
#fc-list -f "%{family}\n" :lang=zh > zhfont.txt

#linux
#  - sudo apt-get install ttf-wqy-microhei  #文泉驿-微米黑
#  - sudo apt-get install ttf-wqy-zenhei  #文泉驿-正黑
#  - sudo apt-get install xfonts-wqy #文泉驿-点阵宋体
#`免费中文字体wiki.ubuntu.org.cn <https://wiki.ubuntu.org.cn/%E5%85%8D%E8%B4%B9%E4%B8%AD%E6%96%87%E5%AD%97%E4%BD%93>`__
#$ fc-list :lang=zh-cn
#/usr/share/fonts/truetype/wqy/wqy-microhei.ttc: WenQuanYi Micro Hei,文泉驛微米黑,文泉驿微米黑:style=Regular
#/usr/share/fonts/X11/misc/wenquanyi_13px.pcf: WenQuanYi Bitmap Song:style=Regular
#/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc: WenQuanYi Zen Hei,文泉驛正黑,文泉驿正黑:style=Regular
#/usr/share/fonts/X11/misc/wenquanyi_12pt.pcf: WenQuanYi Bitmap Song:style=Regular
#/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc: WenQuanYi Zen Hei Sharp,文泉驛點陣正黑,文泉驿点阵正黑:style=Regular
#/usr/share/fonts/X11/misc/wenquanyi_10pt.pcf: WenQuanYi Bitmap Song:style=Regular
#/usr/share/fonts/X11/misc/wenquanyi_9pt.pcf: WenQuanYi Bitmap Song:style=Regular
#/usr/share/fonts/X11/misc/wenquanyi_11pt.pcf: WenQuanYi Bitmap Song:style=Regular
#/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc: WenQuanYi Zen Hei Mono,文泉驛等寬正黑,文泉驿等宽正黑:style=Regular

# linux下：自己安装的字体，中文
# Adobe Fangsong Std,Adobe 仿宋 Std,Adobe Fangsong Std R,Adobe 仿宋 Std R
# Adobe Heiti Std,Adobe 黑体 Std,Adobe Heiti Std R,Adobe 黑体 Std R
# Adobe Kaiti Std,Adobe 楷体 Std,Adobe Kaiti Std R,Adobe 楷体 Std R
# Adobe Song Std,Adobe 宋体 Std,Adobe Song Std L,Adobe 宋体 Std L
# FangSong,仿宋
# FZFangSong-Z02S,方正仿宋简体
# FZGuLi-S12T,方正古隶繁体
# FZLiShu-S01S,方正隶书简体
# FZLiShu-S01T,方正隶书繁体
# FZShouJinShu-S10,方正瘦金书_GBK
# FZShouJinShu-S10S,方正瘦金书简体
# FZShouJinShu-S10T,方正瘦金书繁体
# FZWeiBei-S03,方正魏碑_GBK
# FZWeiBei-S03T,方正魏碑繁体
# FZXiaoZhuanTi-S13T,方正小篆体
# FZXingKai-S04T,方正行楷繁体
# FZYingBiXingShu-S16S,方正硬笔行书简体
# FZYingBiXingShu-S16T,方正硬笔行书繁体
# KaiTi,楷体
# Microsoft YaHei,微软雅黑
# Microsoft YaHei,微软雅黑
# NSimSun,新宋体
# SimHei,黑体
# SimSun,宋体
# WenQuanYi Micro Hei Mono,文泉驛等寬微米黑,文泉驿等宽微米黑
# WenQuanYi Micro Hei,文泉驛微米黑,文泉驿微米黑
# WenQuanYi Zen Hei Mono,文泉驛等寬正黑,文泉驿等宽正黑
# WenQuanYi Zen Hei Sharp,文泉驛點陣正黑,文泉驿点阵正黑
# WenQuanYi Zen Hei,文泉驛正黑,文泉驿正黑
# 经典繁行书
# 经典行书简
# 经典隶书简
# 书体坊米芾体

#windows下的引用名字
#Microsoft YaHei,微软雅黑
#FangSong,仿宋
#Microsoft JhengHei,微軟正黑體
#SimHei,黑体
#NSimSun,新宋体
#SimSun,宋体
#KaiTi,楷体

