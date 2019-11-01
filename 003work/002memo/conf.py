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

project = 'memo of study'
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


latex_engine='xelatex'
# The LaTeX engine to build the docs. The setting can have the following values:
# 'pdflatex' – PDFLaTeX (default)
# 'xelatex' – XeLaTeX
# 'lualatex' – LuaLaTeX
# 'platex' – pLaTeX (default if language is 'ja')

#fix issue of "! LaTeX Error: Too deeply nested."

fh = open('fix-deeplynested.tex', 'r+')
PREAMBLE = fh.read()
fh.close()

# Additional stuff for the LaTeX preamble.
latex_elements = {
'preamble': PREAMBLE,
}

###latex_additional_files = ["fix-deeplynested.tex"]
###
###latex_elements = {
#### Additional stuff for the LaTeX preamble.
###'preamble': r'\input{fix-deeplynested.tex}',
###}

#参考1：`latex-elements：preamble <https://www.sphinx-doc.org/en/master/latex.html#latex-elements-confval>`__
#'preamble'
#Additional preamble content, default empty. One may move all needed macros into some file mystyle.tex.txt of the project source repertory, and get LaTeX to import it at run time:
#
#'preamble': r'\input{mystyle.tex.txt}',
## or, if the \ProvidesPackage LaTeX macro is used in a file mystyle.sty
#'preamble': r'\usepackage{mystyle}',
#It is then needed to set appropriately latex_additional_files, for example:
#
#latex_additional_files = ["mystyle.sty"]

#参考2：`如何避免“太深嵌套”使用Sphinx创建PDF时出错？(How to avoid the “too deeply nested error” when creating PDFs with Sphinx?) <http://www.it1352.com/650222.html>`__
#I solved the problem by adding some latex statements to the sphinx preamble. Accordingly, I created a new latex_preamble.tex file in my sphinx source folder. It contains only the following two commands:
#
#\usepackage{enumitem}
#\setlistdepth{99}
#Moreover, In the conf.py file, also within my source folder, I changed the following (you can lookout for the latex_elements variable in the conf.py file, it is usually commented out):
#
#fh = open('latex_preamble.tex', 'r+')
#PREAMBLE = fh.read()
#fh.close()
#
#latex_elements = {
## Additional stuff for the LaTeX preamble.
#'preamble': PREAMBLE,
#}