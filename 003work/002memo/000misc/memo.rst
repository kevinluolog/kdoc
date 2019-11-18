*********************************************************************
memo
*********************************************************************

.. contents:: 目录
.. section-numbering::

.. 
 :Author: kevinluo
 :Contact: kevinluo_72@163.com

.. 
 .. contents:: 目录
 .. section-numbering::

recent 
=====================================================================

xxx
---------------------------------------------------------------------

life
=====================================================================

xxx
---------------------------------------------------------------------

study
=====================================================================

编程
=====================================================================

经验
---------------------------------------------------------------------

web
---------------------------------------------------------------------

wiki:

`encyclopedia.thefreedictionary.com <http://encyclopedia.thefreedictionary.com/>`__

`www.answers.com <https://www.answers.com/>`__

`吸管秒变笛子 <https://www.sohu.com/a/230583209_614840>`__

misc 
=====================================================================

xxx
---------------------------------------------------------------------

temp 
=====================================================================

xxx
---------------------------------------------------------------------

raw materials
---------------------------------------------------------------------


?????

用echo $date，结果只输出一个ate

?????


date +%Y%m%d -d @1425384141

?????


cp -t -T问题,想copy目录里的文件和子目录，travis提示错

?????

只查看最后一行
tail -1

?????

%ad
author date (format respects --date= option)

--date=iso (or --date=iso8601) shows timestamps in a ISO 8601-like format. The differences to the strict ISO 8601 format are:

?????
For TravisCI users, simply add a config to .travis.yml so it clones the full repository history:
`MestreLion/git-tools <https://github.com/MestreLion/git-tools#install>`__


可以解决拉取全部历史原数据到本地的问题，不加在clone时，只是本分支的历史。这样git log 能拿到文件所有commit的时间

# 根据上面网址介绍加入下面两行
git:
  depth: false

?????
`hexo.io/docs/variables#Page-Variables <https://hexo.io/docs/variables#Page-Variables>`__

`https://hexo.io/zh-cn/docs/variables.html#%E9%A1%B5%E9%9D%A2%E5%8F%98%E9%87%8F
>`__


???
Linux下修改文件创建时间(修改文件更改时间)
进到要改的文件目录里
find . -name “*” -exec touch ‘{}’ \;
注：最后一定要加分号，{}外一定要加单引号，*表示所有的文件（. 代表当前目录下）

???
`Hexo常见问题解决方案 <http://wp.huangshiyang.com/hexo%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88>`__

`Hexo搭建技术博客使用与常见问题详细讲解 <https://code.skyheng.com/post/50982.html>`__

`大前端-5分钟带你读懂Hexo源码设计模式 <https://www.jianshu.com/p/ef88b5bbb914>`__

`Hexo源码剖析 <https://blog.csdn.net/li20081006/article/details/73319054>`__

`hexo博客框架从入门到弃坑 <https://segmentfault.com/a/1190000018082781?utm_source=tag-newest>`__

`hexo-generator-index 源码分析 <https://www.jianshu.com/p/7bec9866a04d>`__

`hexo过滤器before_post_render-theme\\scripts\\filters\\kl-touch-file-time.js <https://hexo.io/zh-cn/api/filter>`__

`ALL TO ALL 在线格式转换 <http://www.alltoall.net/rst_pdf/>`__

`起飞页建站平台 <https://www.qifeiye.com/>`__

`ubuntu下通过PPA源安装texlive2012 <http://luly.lamost.org/oldtown/?p=385>`__

`Latex中文支持Ubuntu <https://www.cnblogs.com/ccoming/p/7810861.html>`__

可以使用fc-list :lang=zh-cn查看所有中文字体
详细设置可以看这个: ubuntu下latex终极安装方案的字体部分=D



`ubuntu下latex终极安装方案的字体部分 <http://segmentfault.com/a/1190000004059490>`__

`Ubuntu 14.04 下 TexLive2014 完美安装攻略 <https://segmentfault.com/a/1190000004059490>`__

`间接链接：如何避免“太深嵌套”使用Sphinx创建PDF时出错？(How to avoid the “too deeply nested error” when creating PDFs with Sphinx?) <http://www.it1352.com/650222.html>`__

`直接链接：如何避免“太深嵌套”使用Sphinx创建PDF时出错？(How to avoid the “too deeply nested error” when creating PDFs with Sphinx?) <https://www.xszz.org/faq-1/question-2018083122086.html
>`__


`latex-elements：preamble <https://www.sphinx-doc.org/en/master/latex.html#latex-elements-confval>`__


`Ubuntu系统中添加中文字体和修改默认中文字体 <https://blog.csdn.net/gengyuchao/article/details/101215243>`__

`字体- Ubuntu中文wiki.ubuntu.org.cn <https://wiki.ubuntu.org.cn/%E5%AD%97%E4%BD%93>`__

获取字体
中文
主条目：免费中文字体
sudo apt-get install ttf-wqy-microhei  #文泉驿-微米黑
sudo apt-get install ttf-wqy-zenhei  #文泉驿-正黑
sudo apt-get install xfonts-wqy #文泉驿-点阵宋体

`免费中文字体wiki.ubuntu.org.cn <https://wiki.ubuntu.org.cn/%E5%85%8D%E8%B4%B9%E4%B8%AD%E6%96%87%E5%AD%97%E4%BD%93>`__

`ubuntu添加中文字体ucloud <https://www.ucloud.cn/yun/23516.html>`__
ubuntu添加中文字体ubuntu
查看系统类型
cat /proc/version

查看中文字体
fc-list :lang=zh-cn

安装字体
apt-get install -y --force-yes --no-install-recommends fonts-wqy-microhei

apt-get install -y --force-yes --no-install-recommends ttf-wqy-zenhei

`Ubuntu 安装 Courier New字体和雅黑consolas字体 <https://www.cnblogs.com/jpfss/p/7895773.html>`__

`网站链接-免费中文字体整理zenozeng.github.io/Free-Chinese-Fonts <http://zenozeng.github.io/Free-Chinese-Fonts/>`__

`网站源码-免费中文字体整理github.com/zenozeng/Free-Chinese-Fonts <https://github.com/zenozeng/Free-Chinese-Fonts>`__

`[转载]latex】itemize, enumerate枚举，编号使用及编号样式设计 <http://blog.sciencenet.cn/blog-597740-1077676.html>`__

`linux比较两个文件是否一样(linux命令md5sum使用方法) <https://www.jb51.net/LINUXjishu/123859.html>`__

`linux 比较两个文件夹不同 (diff命令, md5列表) <https://www.cnblogs.com/xudong-bupt/p/6493903.html>`__

比较文件夹diff，可以直接使用diff命令

::

   [root@~]# diff -urNa dir1 dir2
   　　-a Treat all files as text and compare them line-by-line, even if they    do not seem to be text.
   　　-N, --new-file
   　　　　In directory comparison, if a file is found in only one directory,    treat it as present but empty in the other directory.
   　　-r When comparing directories, recursively compare any subdirectories    found.
   　　-u Use the unified output format.

 

比较文件夹diff，也可以比较文件MD5列表。下面命令可以获取文件夹中文件md5列表

::

   find /home/ -type f -not \( -name '.*' \) -exec md5sum {} \;
   说明：
   (1) /home/文件目录
   (2) -type f 文件类型为普通文件
   (3) -not \( -name '.*' \)  过滤掉隐藏文件。可以过滤掉不需要考虑的文件
   (4) -exec md5sum {} \;  对每个文件执行md5sum命令 

`linux下md5sum用法 (查看文件或字符串的md5值) <https://www.cnblogs.com/kevingrace/p/10201723.html>`__

[root@web-master ~]# echo -n "hello world"|md5sum |cut -d" " -f1

5eb63bbbe01eeed093cb22bb8f5acdc3

命令解释：

md5sum: 显示或检查 MD5(128-bit) 

校验和,若没有文件选项，或者文件处为"-"，则从标准输入读取。

echo -n : 不打印换行符。(注意: echo -n 后面的-n参数必须加上, 

这样算出的字符串的md5值才正确)

cut: 

cut用来从标准输入或文本文件中剪切列或域。剪切文本可以将之粘贴到一个文本文件。 -d 指定与空格和tab键不同的域分隔符。-f1 表示第一个域。

查看一个文件的md5值

[root@web-master ~]# echo "test md5" > kevin.sql

查看并获取这个文件的md5值

[root@web-master ~]# md5sum kevin.sql

170ecb8475ca6e384dbd74c17e165c9e  kevin.sql

[root@web-master ~]# md5sum kevin.sql|cut -d" " -f1

170ecb8475ca6e384dbd74c17e165c9e
 
生产这个个文件的md5值

[root@web-master ~]# md5sum kevin.sql > kevin.sql.md5
 
检查两个文件是否一样，可以通过比较两个文件的md5值 (后续可以用这个方法来检验kevin.sql文件是否被修改)。

[root@web-master ~]# md5sum kevin.sql

170ecb8475ca6e384dbd74c17e165c9e  kevin.sql
 
[root@web-master ~]# cat kevin.sql.md5

170ecb8475ca6e384dbd74c17e165c9e  kevin.sql


`耿老师详解 LaTeX 编译过程绘图源码 <https://www.latexstudio.net/archives/51759.html>`__

`LaTeX 工作室 <https://www.latexstudio.net>`__

`学习资源-LaTeX工作室 <https://www.latexstudio.net/page/tex-documents/>`__

`TeXDoc-在线的texdoc 应用站点可以看到 LaTeX 配套的文档和宏包。 <http://texdoc.net/>`__

`LaTeX 科技排版--华东师范大学数学系 LaTeX 教学课程网页 <http://math.ecnu.edu.cn/~latex/>`__

`潘建瑜老师 LaTeX 科技排版 <http://math.ecnu.edu.cn/~jypan/Teaching/Latex/>`__

`黄正华老师 LaTeX 教学首页 <http://aff.whu.edu.cn/huangzh/>`__

`UK TeX FAQ-这是非常完整的TeX常见问题，推荐多多阅读 <http://www.tex.ac.uk/index.html>`__


`linux 命令 find与rm实现查找并删除目录或文件 <https://www.cnblogs.com/xingchong/p/9961368.html>`__

`https://www.jb51.net/article/99315.htm <https://www.jb51.net/article/99315.htm>`__


`linux下find查找文件后使用xargs和exec进行删除、压缩处理。 <https://blog.51cto.com/13528748/2119490>`__

`linux中find与rm实现查找并删除目录或文件 <https://www.cnblogs.com/langzou/p/5959940.html>`__

`grep正则超详细-linux中grep命令的用法 <https://www.cnblogs.com/flyor/p/6411140.html>`__

`ctan: The Not So Short Introduction to LaTeX, 2015 <https://ctan.org/tex-archive/info/lshort/english/>`__

`lshort中文版: The Not So Short Introduction to LaTeX, 2015 <http://mirrors.ctan.org/info/lshort/chinese/lshort-zh-cn.pdf>`__

`latex_additional_files of Example of configuration file of latex_elements  <https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-c-domain>`__

`the-latex-elements-configuration-setting:'preamble': r'''\\usepackage''', <https://www.sphinx-doc.org/en/master/latex.html#the-latex-elements-configuration-setting>`__

`latex-project.org documentation <https://www.latex-project.org/help/documentation/>`__

`Latex 控制目录显示的深度 <https://blog.csdn.net/jueshu/article/details/90267983>`__

以撰写 book 为例：

book 的 latex 目录默认只显示深度只能到 subsection

如果想要显示到 subsubsection 深度，就要设置目录显示的深度，在 

::

   \begin{document} 前添加：
   \setcounter{tocdepth}{4}
   \setcounter{secnumdepth}{3}
   tocdepth：设置在目录的显示的章节深度
   secnumdepth：设置章节的编号深度
   两者可选的设置值如下：
   -1 part
   0 chapter
   1 section
   2 subsection
   3 subsubsection
   4 paragraph
   5 subparagraph

`LaTeX中设置目录显示深度的一次乌龙经历 <https://www.it610.com/article/5114750.htm>`__

`Linux expect 介绍和用法 <https://www.cnblogs.com/saneri/p/10819348.html>`__

`Linux expect的安装与使用 <https://blog.csdn.net/u013181216/article/details/83055909>`__

`LaTeX：XeLaTeX+xeCJK的初学习笔记(排版我的诗) <https://www.jianshu.com/p/2169a950368d>`__

`万泽:xelatex指南-在 Ubuntu 下排版专业的 pdf 文章 <https://www.latexstudio.net/archives/2249.html>`__

`万泽:xelatex指南 本站下载：xelatex-guide-book-master <http://static.latexstudio.net/wp-content/uploads/2014/09/xelatex-guide-book-master.zip>`__

`万泽:xelatex指南 github: https://github.com/a358003542/xelatex-guide-book <https://github.com/a358003542/xelatex-guide-book>`__

`万泽:github.com/a358003542 <https://github.com/a358003542>`__

`万泽:TIKZ制图简要教程tikz_gallery <https://github.com/a358003542/tikz_gallery>`__

`万泽:ximage tools <https://github.com/a358003542/ximage>`__

`Ubantu安装ttf和otf类型的字体 <https://blog.csdn.net/wc996789331/article/details/89168155>`__

`Ubuntu下安装字体 <https://blog.csdn.net/piscesyang87/article/details/80086780>`__

ubuntu可以与windows通用ttf格式的字体文件。

字体有.ttf格式（truetype font）和.otf格式（opentype font）字体，在Ubantu上安装相应的字体。

Ubuntu系统中的字体文件存放在下面文件夹中

::

   /usr/share/fonts

首先，需要将下载的ttf字体文件复制到该目录。

注意操作该目录的文件需要sudo权限。

为了方便区分各种字体的类型，可以自定义子文件夹。

::

   sudo mkdir /usr/share/fonts/windows
   sudo cp /home/sample/*.ttf /usr/share/fonts

安装mkfontscale和mkfontdir命令，fc-cache命令

::

   使mkfontscale和mkfontdir命令正常运行
   sudo apt-get install ttf-mscorefonts-installer
   使fc-cache命令正常运行
   sudo apt-get install fontconfig

然后重新建立字体索引文件。

::

   sudo mkfontscale
   sudo mkfontdir

最后更新字体缓存。

::

   sudo fc-cache

这样就可以正常使用该字体了。

合起来：

::

   sudo mkdir /usr/share/fonts/windows
   sudo cp /home/sample/*.ttf /usr/share/fonts
   sudo apt-get install ttf-mscorefonts-installer
   sudo apt-get install fontconfig
   sudo mkfontscale
   sudo mkfontdir
   sudo fc-cache


`Linux(Ubuntu，Cent OS)环境安装mkfontscale mkfontdir命令以及中文字库 <https://blog.csdn.net/a8039974/article/details/89845944>`__

` <http://manpages.ubuntu.com/manpages/trusty/en/man1/fc-list.1.html>`__


`为SublimeText3配置IDE(Anaconda虚拟环境) <https://www.jianshu.com/p/0ad5625e9717>`__

去掉代码边上的白框

::

   Sublime > Preferences > Package Settings > Anaconda > Settings User 
   {"anaconda_linting": false}

安装格式化插件Python PEP8 Autoformat，快捷键Ctrl+Shift+R。

`conf.py of Sphinx doc <https://www.sphinx-doc.org/en/master/usage/configuration.html>`__

latex_show_urls
source_suffix

`LaTeX customization of sphinx-doc <https://www.sphinx-doc.org/en/master/latex.html>`__

latex_engine 
latex_elements
latex_show_urls 

`Sphinx support markdown <https://www.sphinx-doc.org/en/master/usage/markdown.html>`__

`自定义：LaTeX字体设置（一） <https://www.jianshu.com/p/b1751078e28e>`__

`让pandoc输出pdf时支持中文 <https://www.cnblogs.com/liuyangnuts/archive/2013/04/23/3038354.html>`__

`Calibre 常用命令行工具详解之 ebook-convert <https://bookfere.com/post/642.html>`__

`Calibre 常用命令行工具详解之 calibre-smtp <https://bookfere.com/post/646.html>`__

`Calibre 常用命令行工具详解之 ebook-meta <https://bookfere.com/post/605.html#em>`__

`《Calibre 使用教程之抓取网站页面制成电子书》 <https://bookfere.com/post/562.html>`__

`Calibre 官方帮助页面-ebook-convert <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>`__

`南怀瑾-老子他说 <http://www.quanxue.cn/ct_nanhuaijin/LaoZiIndex.html>`__

`南怀瑾-历史的经验 <http://www.quanxue.cn/ct_nanhuaijin/LiShiIndex.html>`__


`劝学网-南怀瑾全集 <http://www.quanxue.cn/ct_nanhuaijin/index.html>`__

`南怀瑾-论语别裁 <http://www.quanxue.cn/ct_nanhuaijin/LunYuIndex.html>`__

`论语 <http://www.quanxue.cn/CT_RuJia/LunYuIndex.html>`__


`《楞严经》经文 <http://www.quanxue.cn/CT_FoJia/LengYanIndex.html>`__

`南怀瑾-《楞严大义今释》 <http://www.quanxue.cn/ct_nanhuaijin/LengYanIndex.html>`__

`南怀瑾-《金刚经说什么》 <http://www.quanxue.cn/ct_nanhuaijin/JinGangIndex.html>`__

`《金刚经》经文 <http://www.quanxue.cn/CT_FoJia/JinGangIndex.html>`__

`《金刚经》(原文) <http://www.quanxue.cn/CT_FoJia/JinGang/JinGang35.html>`__

` <>`__


`青风乘翼分享的百度网盘资源 <http://www.rufengso.net/u/bd-2050031688>`__

`如风搜：历史上最伟大的10个方程（美）Robert P.Crease.pdf <http://www.rufengso.net/r/42241052>`__

`电子书下载: 周读 ireadweek.com <http://www.ireadweek.com/>`__

`bash逐行读取文件内容 <https://blog.csdn.net/u011774239/article/details/51033960>`__

`bash 文本读写 并 按照规则输出到新文件中 <https://www.jianshu.com/p/4acc22cd04f3>`__

`shell比较两个字符串是否相等 <https://www.cnblogs.com/wangkongming/p/4221503.html>`__

`有很多linux脚本使用：如何在Hexo中对文章md文件分类 <http://www.manongjc.com/article/30849.html>`__

`英语系列｜读完这100本英文名著，成为英语牛人（四） <https://www.jianshu.com/p/ee1a77357889>`__

`GrimmsFairyTales <http://www.gutenberg.org/files/2591/2591-h/2591-h.htm>`__

`A Little Princess <http://www.gutenberg.org/files/146/146-h/146-h.htm>`__

`古登堡计划，全球最著名的免费电子书网站——Project Gutenberg offers over 42 000 free ebooks <www.gutenberg.org>`__

`很多书 <www.manybooks.net>`__

` <www.feedbooks.com>`__

`原版英语论坛，国内网友自由分享海量热门畅销书 <http://bbs.en8848.com.cn/forum.php>`__

`掌上书苑，EPUB格式 <www.cnepub.com/catalogs.html>`__

`The Secret Garden by Frances Hodgson Burnett <http://www.gutenberg.org/files/113/113-h/113-h.htm>`__

`Little Lord Fauntleroy by Frances Hodgson Burnett <http://www.gutenberg.org/files/479/479-h/479-h.htm>`__

`The Adventures of Pinocchio by Carlo Collodi <http://www.gutenberg.org/ebooks/500>`__

`windows下修改文件创建时间 <https://blog.csdn.net/shinegogo/article/details/7506291?utm_source=blogxgwz4
>`__

使用windows的copy命令达到修改文件创建时间的目的,方法如下:
1. 修改系统时间为你需要的修改到的目标时间;
2. 运行命令:copy 文件名+,,(注意是连续两个英文逗号).
done.

`How to Change the Last Modified Date, Creation Date, and Last Accessed Date for Files and Folders
 <https://www.online-tech-tips.com/computer-tips/how-to-change-the-last-modified-date-creation-date-and-last-accessed-date-for-files-and-folders/>`__

`bulk_file_changer <http://www.nirsoft.net/utils/bulk_file_changer.html>`__

`Linux sed 命令 <https://www.runoob.com/linux/linux-comm-sed.html>`__

` <>`__

#touch_time_$(1) := $$(shell tail -1 $$(TMP_TIME_FILE_$(1)))
touch_time_$(1) := $$(shell tail -1 $$(TMP_TIME_FILE_$(1)) | sed 's/ .*:.*:.* / 08:08:08 /g')

#Guest@OEM-20090831LIJ MINGW32 /H/tmp_H/001.work/004.env/01prjsp/hexo/klBlog/source/_posts/kl_post/003post (hexo-maup)
#$ git log --date=iso --format="%ad" -- "index.md" |tail -1 | sed 's/ .*:.*:.* / 08:08:08 /g'
#2019-10-24 08:08:08 +0000


`散策 VS 狩枫，游走在京都“立派”的秋色之中 <https://www.mafengwo.cn/i/17776687.html>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__

` <>`__
