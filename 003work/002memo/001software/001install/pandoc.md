pandoc

# install

# informations

1. [beamer](https://ctan.org/pkg/beamer)
    
    slide support of latex, same author with TikZ(CLI Package)


# tips

## 参数

### basic

1. pandoc -f -t -o

        -f --from:-r --read： inputfile format
        -t --to:-w --write: outputfile format
        pandoc -f markdown -t latex hello.txt -o hi.tex
    
2. --list-output-formats --list-input-formats

    查看输入输出格式支持格式

3. --atx-headers

    Use ATX-style headings in Markdown output. The default is to use setext-style headings for levels 1 to 2, and then ATX headings.

4. --reference-links

### template

1. -V/--variable

    Templates contain variables, which allow for the inclusion of arbitrary information at any point in the file. They may be **set at the command line using the -V/--variable option**. 

    *If a variable is not set*, pandoc will look for the key in the document’s metadata – which can be **set using either YAML metadata blocks or with the -M/--metadata option**.

    `-V slidy-url=slidy2` : 指定slidy Javascriptions 引用路径

2. pandoc -D *FORMAT*

    where FORMAT is the name of the output format. A custom template can be specified using the --template option. You can also override the system default templates for a given output format FORMAT by putting a file templates default.*FORMAT* in the user data directory (see **--data-dir**, above). Exceptions:

    - For odt output, customize the default.opendocument template.
    - For pdf output, customize the **default.latex** template (or the 
    default.context template, if you use -t context, or the default.ms template, if you use -t ms, or the default.html template, if you use -t html).

    - docx and pptx have no template (however, you can use --reference-doc to customize the output).
    
            pandoc slidy00.md .\templates\metadata.yml -o slidy00.tex --template .\templates\default.latex
            or
            pandoc slidy00.md .\templates\metadata.yml -o slidy00.tex --data-dir= .\templates

### pdf

1. --pdf-engine=xelatex

        xelatex： unicode汉字支持，新
        pdflatex: 不支持汉字，旧
        -t html defaults to --pdf-engine=wkhtmltopdf

2. -N,--number-sections

    Number section headings in LaTeX, ConTeXt, HTML, or EPUB output. By default, sections are not numbered.

### slide

1. --number-offset=NUMBER[,NUMBER,…]

    [slide list item show one by one]

2. --slide-level=NUMBER
    
    Specifies that headings with the specified level create slides (for beamer, s5, slidy, slideous, dzslides).

3. --reference-doc=FILE

    Use the specified file as a style reference in producing a docx or ODT file.
    
    - Docx
        
        + reference.docx:  
    
            pandoc -o custom-reference.docx --print-default-data-file reference.docx.
        
    - PowerPoint
    
        + reference.pptx: 

            pandoc -o custom-reference.pptx --print-default-data-file reference.pptx

4. title-meta, author-meta, and date-meta

    - pandoc:
    
            % title
            % author(s) (separated by semicolons)
            % date

            有没有的要加%空行

            %
            % Author

            % My title
            %
            % June 15, 2006

5. `--resource-path --extract-media`

        pandoc -t slideous -s slidy.md -o slidous.html -i --resource-path=.:resource\pic --extract-media=resource\pic

        --extract-media： 表示把链接的文件输出到指定的目录
        --resource-path： 表示指定链接的相对位置，相对于工作目录，用了这个需要显示指明当前目录.。同时这个选项只能和--self-contained 或者--extract-media一起用。

### Math rendering in HTML

1. --mathjax[=URL]
2. --mathml
3. --webtex[=URL]

Convert TeX formulas to <img> tags that link to an external script that converts formulas to images. 

svg: <https://latex.codecogs.com/svg.latex?>
png: <https://latex.codecogs.com/png.latex?>

# command


## md->web slide (reveal.js s5 slideous slidy)

### slide Javascription solutions

name      |explaination
----------|-----------
dzslides  |(DZSlides HTML5 + JavaScript slide show)
revealjs  |(reveal.js HTML5 + JavaScript slide show)
s5        |(S5 HTML and JavaScript slide show)
slideous  |(Slideous HTML and JavaScript slide show)
slidy     |(Slidy HTML and JavaScript slide show)

### default Url location

name         |explaination
-------------|-----------
revealjs-url |base URL for reveal.js (defaults to reveal.js)
s5-url       |base URL for S5  (defaults to s5/default)
slideous-url |base URL for Slideous (defaults to slideous)
slidy-url    |base URL for Slidy (defaults to https://www.w3.org/Talks/Tools/Slidy2)

### web slide commad:

1. md->dzslides
    
        pandoc -t dzslides -s slidy.md -o dzslides.html -i --slide-level=2 --resource-path=.:resource\pic --extract-media=resource\pic

2. md->revealjs:

        pandoc -t revealjs -s slidy.md -o revealjs.html -i --slide-level=2 --resource-path=.:resource\pic --extract-media=resource\pic -V revealjs-url=reveal.js

3. md->s5:

        pandoc -t s5 -s slidy.md -o s5.html -i --slide-level=2 --resource-path=.:resource\pic --extract-media=resource\pic -V s5-url=s5\ui\default

5. md->slideous:

        pandoc -t slideous -s slidy.md -o slideous.html -i --slide-level=1 --resource-path=.:resource\pic --extract-media=resource\pic -V s5-url=slideous

6. md->slidy:

        pandoc -t slidy -s slidy.md -o slidy.html -i --slide-level=2 --resource-path=.:resource\pic --extract-media=resource\pic -V slidy-url=slidy2

### command (md->pdf):

1. xelatex 终稿

    配合两个文件：
    
    - metadata.yaml
        
        元变量 可用 -V 在命令行输入

    - default.latex
        
        修改了latex的模板，主要是为了框线链接


    - 分两步，->.tex ->.pdf

            pandoc slidy00.md .\templates\metadata.yaml -o slidy00.tex -s -N --toc --toc-depth=3 --template .\templates\default.latex

            xelatex slidy00.tex

    - 一步头
        
            pandoc slidy00.md .\templates\metadata.yaml --pdf-engine=xelatex -o slidy00.pdf -s -N --toc --toc-depth=3 --data-dir=.\templates
        
2. xelatex

        pandoc slidy.md -o pdf.pdf --pdf-engine=xelatex -i

    - xelatex可以支持中文，同时缺省是支持目录的。 
    - 所以不用加-toc,--table-of-contents, 
    - -i,表示目录加上数字

            pandoc slidy.md -o pdf.tex -s
            xelatex pdf.tex -o pdf1.pdf -V CJKmainfont=xecjk

3. 参考网上xelatex

    [参考链接][Pandoc的使用和遇到的问题]
    
        pandoc --pdf-engine=xelatex --template=D:\tools\Pandoc\pm-template.latex test.md -o test.pdf

    [Tzeng Yuxio的支持中文latex模板文件](https://github.com/tzengyuxio/pages/blob/gh-pages/pandoc/pm-template.latex)

### command (md->html)

1. my
2. 参考网上

        pandoc -s -f gfm -t html5 --css=css/markdownPad-github.css test.md -o test.html
    
    [markdownPad-github.css](https://github.com/nicolashery/markdownpad-github)
    
    自己指定CSS显示模板

# faq

## pandoc生成SLIDE时，怎么用本地相对路径嵌入javascription代码？-s --stand-alone

1. To produce an HTML/JavaScript slide show, simply type
    
    pandoc -t FORMAT -s habits.txt -o habits.html
    
    where FORMAT is either s5, slidy, slideous, dzslides, or revealjs.
    
    For Slidy, Slideous, reveal.js, and S5, the file produced by pandoc with the -s/--standalone option embeds a link to JavaScript and CSS files, which are assumed to be available at the relative path s5/default (for S5), slideous (for Slideous), reveal.js (for reveal.js), or at the Slidy website at w3.org (for Slidy). 

2. These paths can be changed by setting variables: the slidy-url, slideous-url, revealjs-url, or s5-url 

        变量前面要加上 -V
        -V slidy-url=slidy2 : 指定slidy Javascriptions 引用路径

3. For DZSlides, the (relatively short) JavaScript and CSS are included in the file by default.

4. With all HTML slide formats, the `--self-contained` option can be used to produce a single file that contains all of the data necessary to display the slide show, including linked scripts, stylesheets, images, and videos.

## 怎么直接生成网页SLIDE?

    pandoc -t FORMAT -s habits.txt -o habits.html
    -i : incremental 指定逐步显示列表项
    -slide--level: 指定第几级Header开始分slide页面
    -s --stand-alone: 相对目录（slidy 除外），并包头部

## 怎么把javascript/css链接资源定位到指定目录

slidy-url, slideous-url, revealjs-url, or s5-url variables


## 怎么把图片链接资源定位到指定目录

    pandoc -t slideous -s slidy.md -o slidous.html -i --resource-path=.:resource\pic --extract-media=resource\pic

## 怎么直接生成pdf形式的PPT? -t beamer

To produce a PDF slide show using beamer, type

    pandoc -t beamer habits.txt -o habits.pdf

## 怎么直接生成DOCX文件？

    pandoc slidy.md -o slide.docx --toc --toc-depth=6 -N
    --toc, --table-of-contents
    --toc-depth=NUMBER
    --resource-path=SEARCHPATH : --resource-path=.:test will search the working directory and the test subdirectory

## 怎么指定并修改pandoc用的pptx/docX的模板文件？

## 为何LaTex的book类型中，目录及chapter前自动插入空白页面?

- [LaTex的book类型中，目录及chapter前自动插入空白页面](https://blog.csdn.net/Sarah_LZ/article/details/90737631)

    1. 如题，在book中开新的chapter，前面总是自动留空白页面，而且封面与目录之间也总是多出一张空白页，怎么设置页码都不会消除. 

        原因说明
        
        在book类中，默认目录与每一章都从奇数页码开始，如果上一章的结束刚好是奇数页码，就默认在后面补充一张空白页作为偶数页，使得下一章仍从奇数页码开始. 这是book的排版规范.
        
        此外documentclass中有一对选项openright和openany, book类默认为openright模式，这也是为什么book类的奇数页面与偶数页面的左右页边距刚好相反的原因.

    2. 如何解决book中自动留白的问题

        还有一对选项：oneside和twoside，book类文档默认为twoside模式：双面打印模式，在这种模式下，默认新章节从奇数页码开始打印，所以会自动留白,
        我们只需要在documentclass的选项中指定book为oneside的模式，就可以消除留白. 如下：   
        '\documentclass[UTF8,a4paper,15pt,titlepage,oneside]{ctexbook}'

## 拼接PDF

其实用tex就可以合并pdf, 而且这个方法是跨平台的,无论widows, linux, Mac X, 只要有装了tex和宏包pdfpages,这个宏包一般的tex发行版默认都包含了, texlive就已经有了.
代码:

    \documentclass[a4paper]{article}
    \usepackage{pdfpages}
    \begin{document}
    \includepdfmerge{1.pdf,1-3}
    \includepdfmerge{2.pdf,5-13}
    \end{document}
    其中命令\includepdfmerge{1.pdf,1-3}就是导入1.pdf的1至3页.
    命令\includepdfmerge{2.pdf,5-13}就是导入2.pdf的5至13页.

## md-pdfbook时，怎么添加章节号？ markdown语法解决

* [用 Pandoc 生成一篇调研论文 | Linux 中国](https://blog.csdn.net/F8qG7f9YD02Pe/article/details/83629436)
        
        Implementation 这个标题使用了 H1 并且声明了一个 {#sec:implementation} 的标签，这是作者用于引用该章节的标签。要想引用一个章节，输入 @符号并跟上对应章节标签，使用方括号括起来即可： [@sec:implementation]

# 参考

## 参考文章

- [Pandoc使用技巧](https://www.jianshu.com/p/be291ac296c3)
- [【转】RStudio+Markdown+Pandoc的中文配置](https://www.jianshu.com/p/a97b4a9f6d5b)
- [Pandoc中使用Reveal.js制作幻灯片](https://www.jianshu.com/p/0e0abc6feeb3)
- [Pandoc的使用和遇到的问题][]

[Pandoc的使用和遇到的问题]: https://www.jianshu.com/p/dcc2f95cc086

# MISC

## pandoc 基本命令

    -f: 指定输入格式，比如docx、epub、md、html等
    -t: 指定输出格式，比如docx、epub、md、html等
    -o: 输出到file文件
    --verbost: 显示详细调试信息
    --log： 指定输出日志信息
     
    --list-input-formats：列出支持的输入格式。
    --list-output-formats：列出支持的输出格式。
    --list-extensions：列表支持Markdown扩展，后面跟一个+或者-说明是否在pandoc的Markdown中默认启用。
    --list-highlight-languages:列出语法突出显示支持的语言。
    --list-highlight-styles:列出支持语法高亮的样式。。
    -v: 打印版本信息。
    -h：显示语法帮助

## pandoc帮助文档摘录 

### 待处理摘录

    package: xcolor hypreff 用来设置TOC颜色 link外框线


### Heading identifiers

    - Extension: header_attributes
        {#identifier .class .class key=value key=value}
    - example: will all be assigned the identifier foo:
        # My heading {#foo}
        ## My heading ##    {#foo}
        My other heading   {#foo}

    - Headings with the class unnumbered will not be numbered, even if --number-sections is specified. 
        # My heading {-}
        is just the same as
        # My heading {.unnumbered}
    Like regular reference links, these references are case-insensitive.

    -Extension: implicit_header_references

    - My heading {-}
    is just the same as
    - My heading {.unnumbered}
    Like regular reference links, these references are case-insensitive.

    Extension: implicit_header_references


## Writage是一款word插件

[下载网址为](http://www.writage.com/)
支持markdown与word互相转换

# tips

## 列出电脑中已安装字体

列出所有的中文字体的字体族名，要列出日文和韩文 zh改成 ja或 ko。

    fc-list -f "%{family}\n" :lang=zh > zhfont.txt

## 文档内部跳转

1. 先定义一个锚(id)

        <span id="jump">Hello World</span>

2. 然后使用markdown的语法:

        [XXXX](#jump)





