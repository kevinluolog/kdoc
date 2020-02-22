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


`shell 判断文件夹或文件是否存在 <https://www.cnblogs.com/37yan/p/6962563.html>`__

`
linux shell 脚本基本用法 <https://blog.csdn.net/weixin_44792344/article/details/88807391>`__

`【Linux】shell脚本参数传递 <https://www.cnblogs.com/jxd283465/p/11611146.html>`__

`时间管理，用这三个工具就够了 <https://www.jianshu.com/p/1e43c0a8fa19>`__

1. Teambition 
2. 滴答清单
3. Forest

GTD，Getting Things Done的缩写。来自于David Allen的一本畅销书《Getting Things Done》，中国的中文翻译本《尽管去做：无压工作的艺术》由中信出版社出版。
《尽管去做：无压工作的艺术》
GTD的基本方法：GTD的具体做法可以分成收集、整理、组织、回顾与行动五个步骤。

`金融梦碎？华尔街23万交易员最终被AI逼到死角 <https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9081408068852912173%22%7D&n_type=1&p_from=4>`__

`中国人民银行上海总部关于促进金融科技发展 支持上海建设金融科技中心的指导意见 <http://news.emoney.cn/zonghetishi/3396934.shtml>`__

`《金融科技(FinTech)发展规划(2019-2021年)》 <http://baijiahao.baidu.com/s?id=1643920208596875562&wfr=spider&for=pc>`__

`《用金融科技赋能银行资管转型》 <http://www.sohu.com/a/283730483_211428>`__

`金融科技是什么？ <https://baijiahao.baidu.com/s?id=1593183016200208534&wfr=spider&for=pc>`__

`资管机构法规 <https://wenku.baidu.com/view/33b614f4a36925c52cc58bd63186bceb19e8edc2.html>`__

`新三板企业融资模式大全共48种 <https://wenku.baidu.com/view/38cb6bb24b73f242326c5f55.html>`__

`2019年Fintech行业有多火爆？摩根大通边骂边发币！  <http://www.sohu.com/a/296011206_734221>`__

`英文搜索引擎 <http://www.sowang.com/search/searchen.htm>`__

英文搜索引擎
AltaVista Excite Infoseek
Bing（必应搜索）
http://www.bing.com/
Dogpile
http://www.dogpile.com/
HotBot
http://www.hotbot.com
HotBot 是美国一个非常优秀的搜索引擎，它获得了许多杂志及媒体的奖项。
Ask.com
http://www.ask.com/
提供搜索网站，图片，新闻，博客，视频，地图和方向，本地搜索和购物。

`中国银保监会发布《商业银行理财子公司管理办法》 <http://www.cbrc.gov.cn/chinese/newShouDoc/EC5C3807543C4B0EA9DF5A8267B59433.html>`__

中国银保监会发布《商业银行理财子公司管理办法》
2018年12月2日 - 《商业银行理财业务监督管理办法》(以下简称“理财新规”)相关要求,银保监会制定了《商业银行理财子公司管理办法》(以下简称《理财子公司管理办法》

`附：《商业银行理财子公司管理办法》 <http://www.cbrc.gov.cn/chinese/newShouDoc/C441E44624394A76B25051CA7F4AFE5C.htm>`__

`中国银保监会有关部门负责人就《商业银行理财子公司管理办法》答记者问 <http://www.cbrc.gov.cn/chinese/newShouDoc/E00BC90733364359949BB2AE9104FBB4.html>`__



`刚性兑付 <https://baike.baidu.com/item/%E5%88%9A%E6%80%A7%E5%85%91%E4%BB%98/197783?fr=aladdin>`__

根据《关于规范金融机构资产管理业务的指导意见》（以下简称“资管新规”）、《商业银行理财业务监督管理办法》（以下简称“理财新规”）相关要求，银保监会发布实施《商业银行理财子公司管理办法》（以下简称《理财子公司管理办法》）。银保监会有关部门负责人就相关问题回答了记者提问。

中国信托业协会日前发布的《2012年二季度末信托公司主要业务数据》显示，截至2012年二季度末，信托资产规模在一季度突破5万亿元的基础上再增长2300亿元至5.5万亿元。而在2007年，这一数字仅为9491.53亿元，在6年之中，信托行业资产规模增长近6倍。
信托业盈利情况也十分理想。数据显示，二季度，信托行业经营收入259亿元，同比增长50%;利润总额189.96亿元，同比增59.5%。 [1]


` <http://www.xtxh.net/xtxh/>`__

`2019年3季度末信托公司主要业务数据 <http://www.xtxh.net/xtxh/statistics/45668.htm>`__

`2019年3季度中国信托业发展评析 <http://www.xtxh.net/xtxh/statistics/45657.htm>`__

`银行理财子公司来了！选择更多，收益更高？ <https://baijiahao.baidu.com/s?id=1634668150004762385&wfr=spider&for=pc>`__

`weiyangx-未央信-专注金融科技与创新 <https://www.weiyangx.com>`__

`王玉珍：未来银行理财的九个发展特征 <https://www.weiyangx.com/344596.html>`__

`金融科技fintech百科 <https://baike.baidu.com/item/%E9%87%91%E8%9E%8D%E7%A7%91%E6%8A%80/23222298?fr=aladdin>`__

`论文检测系统 <https://www.jianshu.com/p/d3a55d05d5d1>`__

`reveal.js: slide make online editor <https://slides.com/>`__

`reveal.js: markdown grammar <https://github.com/hakimel/reveal.js#markdown>`__

<<<<<<< HEAD
`git-svn — 让git和svn协同工作 <https://blog.csdn.net/weixin_30484739/article/details/95816525>`__

投资相关
`互联网金融分析系列之一:赢时胜(300377)业绩与概念的完美结 <https://xueqiu.com/2290121721/80985681?from=groupmessage>`__

`研报 | “互联网金融”系列之二：百舸争流，互联网金融萌芽  <https://www.sohu.com/a/233328397_476016>`__

`ppt数据中台8问 <http://www.360doc.com/content/19/0408/10/37805727_827158031.shtml>`__

`数据仓库之ETL实战 <https://www.jianshu.com/p/8da8968c3a09>`__

`几款开源的ETL工具及ELT初探 <https://blog.csdn.net/juceli/article/details/81448224>`__

`ETL讲解（很详细！！！） <https://www.cnblogs.com/yjd_hycf_space/p/7772722.html>`__

ETL是将业务系统的数据经过抽取、清洗转换之后加载到数据仓库的过程，目的是将企业中的分散、零乱、标准不统一的数据整合到一起，为企业的决策提供分析依据。 ETL是BI项目重要的一个环节。 通常情况下，在BI项目中ETL会花掉整个项目至少1/3的时间,ETL设计的好坏直接关接到BI项目的成败。       

　　ETL的设计分三部分：数据抽取、数据的清洗转换、数据的加载。在设计ETL的时候我们也是从这三部分出发。数据的抽取是从各个不同的数据源抽取到ODS(Operational Data Store，操作型数据存储)中——这个过程也可以做一些数据的清洗和转换)，在抽取的过程中需要挑选不同的抽取方法，尽可能的提高ETL的运行效率。ETL三个部分中，花费时间最长的是“T”(Transform，清洗、转换)的部分，一般情况下这部分工作量是整个ETL的2/3。数据的加载一般在数据清洗完了之后直接写入DW(Data Warehousing，数据仓库)中去。

　　ETL的实现有多种方法，常用的有三种。一种是借助ETL工具(如Oracle的OWB、SQL Server 2000的DTS、SQL Server2005的SSIS服务、Informatic等)实现，一种是SQL方式实现，另外一种是ETL工具和SQL相结合。前两种方法各有各的优缺点，借助工具可以快速的建立起ETL工程，屏蔽了复杂的编码任务，提高了速度，降低了难度，但是缺少灵活性。SQL的方法优点是灵活，提高ETL运行效率，但是编码复杂，对技术要求比较高。第三种是综合了前面二种的优点，会极大地提高ETL的开发速度和效率。

`阿里架构总监一次讲透中台架构，13页PPT精华详解 <http://www.sohu.com/a/331776003_692515>`__
=======
`使用pandoc制作幻灯片 <https://www.cnblogs.com/wybert/p/11523311.html>`__

包含在使用pandoc转化pptx的时候表格和图片会单独的出现在一页ppt里面的解决方案链接

`利用Markdown和Pandoc制作PPT（七）Pandoc的命令行参数 <https://zhuanlan.zhihu.com/p/35719599>`__

`利用Beamer做slides时让enumerate内容跨越2个frame显示 <https://blog.csdn.net/RobertChenGuangzhi/article/details/79467438>`__

`适合程序员的画图技法 <https://blog.csdn.net/younger_z/article/details/70227948>`__

`程序员的绘图利器 — Graphviz <https://blog.csdn.net/zhangskd/article/details/8250470>`__

案例全面

`程序员画图工具总结 <https://blog.csdn.net/judyjie/article/details/84454560>`__

1. visio：用的很多。做这个行业的码农，都知道吧。
2. wps：用的多。用过电脑的民工，都知道吧。
3. 亿图：很强大，功能丰富。就是要付费。想免费试用，你知道的。
4. Astah Community：Astah Community是一个非常强大的免费的UML建图工具，支持最新的UML图。地址：http://astah.net/tutorial#new-to-astah。
5. Graphviz：代码生成图像。AT&T实验室启动的开源工具包。DOT是一种图形描述语言，非常简单的
6. Processon：在线流程图。专注于为作图人员提供价值，利用互联网和社交技术颠覆了人们梳理流程的方法习惯，继而使商业用户获得比传统模式更高的效率和回报，改善人们对流程图的创作过程。地址：https://www.processon.com
7. XMind：思维脑图。要付费，要免费试用，你知道怎么做的。
8. draw.io ：在线流程图。图形颜色很漂亮。
9. OmniGraffle：OmniGraffle是由The Omni Group制作的一款绘图软件，其只能于运行在Mac OS X和iPad平台之上。


`drawio-desktop/releases <https://github.com/jgraph/drawio-desktop/releases/tag/v12.3.2>`__

`一键搭建drawio <https://blog.csdn.net/weixin_34056162/article/details/91468523?locationNum=7&fps=1>`__

`使用drawio进行画图真的很方便(WEB版/Chrome APP版/桌面版) <https://blog.csdn.net/dog250/article/details/89272808>`__

`代替Visio第三波，并且是开源的哦：le5le-topology <http://topology.le5le.com/>`__

`代替Visio第三波详细介绍： <https://juejin.im/post/5d6c88726fb9a06b0e54ab35>`__
>>>>>>> 54d7771b54c748ee1d33ed10f51f07f48a33a2e0

`李广乾ppt：数据中台促进“互联网＋”产业创新 <https://www.jianshu.com/p/6edcdc98c33a>`__

` <https://bigdata.163yun.com/middlePlatform?channel=B_baidu_mammut_117>`__

`FS-LDM第一讲-----金融业务逻辑数据模型 <https://blog.csdn.net/oracle8090/article/details/84189966>`__

逻辑数据模型(Logical Data Model)
TD建模主题思想FS-LDM

Teradata天睿公司（纽交所代码：TDC），是美国前十大上市软件公司之一。经过逾30 年的发展，Teradata天睿公司已经成为全球最大的专注于大数据分析、数据仓库和整合营销管理解决方案的供应商之一。
数量庞大、增长迅猛、种类多样的数据已经成为企业在大数据时代发展不得不面临的现实境况。这是挑战，也是机遇。对此，Teradata天睿公司基于客户需求，提供领先、全面、有效的解决方案，帮助企业获取商业洞察力，并且将之转化为行动力，创造商业价值。

->NCR->AT&T 
2012年 Teradata天睿公司发布Teradata统一数据架构（Teradata Unified Data Architecture™, UDA）。

Teradata数据仓库配备性能最高、最可靠的大规模并行处理 (MPP) 平台，能够高速处理海量数据。它使得企业可以专注于业务，无需花费大量精力管理技术，因而可以更加快速地做出明智的决策，实现 ROI 最大化。


1、 什么是MPP？

MPP (Massively Parallel Processing)，即大规模并行处理，在数据库非共享集群中，每个节点都有独立的磁盘存储系统和内存系统，业务数据根据数据库模型和应用特点划分到各个节点上，每台数据节点通过专用网络或者商业通用网络互相连接，彼此协同计算，作为整体提供数据库服务。非共享数据库集群有完全的可伸缩性、高可用、高性能、优秀的性价比、资源共享等优势。

简单来说，MPP是将任务并行的分散到多个服务器和节点上，在每个节点上计算完成后，将各自部分的结果汇总在一起得到最终的结果(与Hadoop相似)。

`数据建模三范式 <https://blog.csdn.net/BabyFish13/article/details/99810727>`__

`数据仓库建模三范式建模为什么能保证口径的一致性 <TD建模主题思想FS-LDM>`__

`MPP(大规模并行处理)简介 <https://blog.csdn.net/qq_42189083/article/details/80610092>`__

OLTP面对的是操作人员和低层管理人员，OLAP面员和高层管理人员。 [3] 
联机分析处理 (OLAP) 的概念最早是由关系数据库之父E.F.Codd于1993年提出的，他同时提出了关于OLAP的12条准则。OLAP的提出引起了很大的反响，OLAP作为一类产品同联机事务处理(OLTP) 明显区分开来。
OLAP是使分析人员、管理人员或执行人员能够从多角度对信息进行快速、一致、交互地存取，从而获得对数据的更深入了解的一类软件技术。OLAP的目标是满足决策支持或者满足在多维环境下特定的查询和报表需求，它的技术核心是"维"这个概念。
“维”是人们观察客观世界的角度，是一种高层次的类型划分。“维”一般包含着层次关系，这种层次关系有时会相当复杂。通过把一个实体的多项重要的属性定义为多个维(dimension)，使用户能对不同维上的数据进行比较。因此OLAP也可以说是多维数据分析工具的集合。
OLAP的基本多维分析操作有钻取（roll up和drill down）、切片（slice）和切块（dice）、以及旋转（pivot）、drill across、drill through等。
OLAP工具是针对特定问题的联机数据访问与分析。它通过多维的方式对数据进行分析、查询和报表。维是人们观察数据的特定角度。例如，一个企业在考虑产品的销售情况时，通常从时间、地区和产品的不同角度来深入观察产品的销售情况。这里的时间、地区和产品就是维。而这些维的不同组合和所考察的度量指标构成的多维数组则是OLAP分析的基础，可形式化表示为（维1，维2，……，维n，度量指标），如（地区、时间、产品、销售额）。多维分析是指对以多维形式组织起来的数据采取切片（Slice）、切块（Dice）、钻取（Drill-down和Roll-up）、旋转（Pivot）等各种分析动作，以求剖析数据，使用户能从多个角度、多侧面地观察数据库中的数据，从而深入理解包含在数据中的信息。
根据综合性数据的组织方式的不同，常见的OLAP主要有基于多维数据库的MOLAP及基于关系数据库的ROLAP两种。MOLAP是以多维的方式组织和存储数据，ROLAP则利用现有的关系数据库技术来模拟多维数据。在数据仓库应用中，OLAP应用一般是数据仓库应用的前端工具，同时OLAP工具还可以同数据挖掘工具、统计分析工具配合使用，增强决策分析功能。
两者区别
OLTP
OLAP
用户
操作人员，低层管理人员
决策人员，高级管理人员
功能
日常操作处理
分析决策

On-Line Transaction Processing联机事务处理过程(OLTP)，也称为面向交易的处理过程，其基本特征是前台接收的用户数据可以立即传送到计算中心进行处理，并在很短的时间内给出处理结果，是对用户操作快速响应的方式之一。

`OLTP百科 <https://baike.baidu.com/item/OLTP/5019563?fr=aladdin>`__

`OLAP百科 <https://baike.baidu.com/item/%E8%81%94%E6%9C%BA%E5%88%86%E6%9E%90%E5%A4%84%E7%90%86?fromtitle=OLAP&fromid=1049009>`__

OLAP的基本多维分析操作有钻取（Drill-up和Drill-down）、切片（Slice）和切块（Dice）、以及旋转（Pivot）等。

事实上，随着数据仓库理论的发展，数据仓库系统已逐步成为新型的决策管理信息系统的解决方案。数据仓库系统的核心是联机分析处理，但数据仓库包括更为广泛的内容。
概括来说，数据仓库系统是指具有综合企业数据的能力，能够对大量企业数据进行快速和准确分析，辅助做出更好的商业决策的系统。它本身包括三部分内容：
1、数据层：实现对企业操作数据的抽取、转换、清洗和汇总，形成信息数据，并存储在企业级的中心信息数据库中。
2、应用层：通过联机分析处理，甚至是数据挖掘等应用处理，实现对信息数据的分析。
3、表现层：通过前台分析工具，将查询报表、统计分析、多维联机分析和数据发掘的结论展现在用户面前。
从应用角度来说，数据仓库系统除了联机分析处理外，还可以采用传统的报表，或者采用数理统计和人工智能等数据挖掘手段，涵盖的范围更广；就应用范围而言，联机分析处理往往根据用户分析的主题进行应用分割，例如：销售分析、市场推广分析、客户利润率分析等等，每一个分析的主题形成一个OLAP应用，而所有的OLAP应用实际上只是数据仓库系统的一部分。

`OLTP与OLAP：在新IT环境下的相互结合 <https://baijiahao.baidu.com/s?id=1627885723219801116&wfr=spider&for=pc>`__

OLTP和OLAP协同工作

上述示例中上部的数据(HR数据库、CRM、计费系统)一般是通过一个萃取、转置和加载(Extract, Transform and Load, ETL)的过程进行批量处理(通常是在夜间)。它用于从多个OLTP源收集数据并将其放入OLAP数据仓库(允许跨系统分析)。在图的下半部分，您可以看到数据在OLAP立方体中得到了正确的存储和组织。

`大数据分析之OLTP与OLAP的区别 <https://baijiahao.baidu.com/s?id=1611554859260686629&wfr=spider&for=pc>`__

`大数据生死时刻：七成数据接口被切断，数万员工离开行业 <https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9331469534616139584%22%7D&n_type=1&p_from=4>`__

`TD建模系列（二）-FS-LDM设计要点 <https://www.jianshu.com/p/42b011e69c6a>`__

`TD建模系列（一）-TERADATA关键技术知识点 <TD建模系列（一）-TERADATA关键技术知识点>`__

`元数据（MetaData） <https://www.jianshu.com/p/abd09ccd9842>`__

`元数据-百科 <https://baike.baidu.com/item/%E5%85%83%E6%95%B0%E6%8D%AE/1946090?fr=aladdin>`__

元数据（Metadata），又称中介数据、中继数据，为描述数据的数据（data about data），主要是描述数据属性（property）的信息，用来支持如指示存储位置、历史数据、资源查找、文件记录等功能。元数据算是一种电子式目录，为了达到编制目录的目的，必须在描述并收藏数据的内容或特色，进而达成协助数据检索的目的。

`基金投资管理系统O32操作手册-风险控制 <https://wenku.baidu.com/view/892374d9b14e852458fb57fb.html>`__

基金投资管理系统o32用户手册(01更新)资料


`售前-百科 <https://baike.baidu.com/item/%E5%94%AE%E5%89%8D%E5%B7%A5%E7%A8%8B%E5%B8%88/9341955?fr=aladdin>`__
产品型到解决方案型，IT服务型

在售前的发展过程中，从售前工程师到售前咨询师，又是一个大的跨度。现在，在行业内售前咨询师的需求在增大，而售前工程师的需求缺并不见得有增长。就个人体会，我简单的说说二者的区别：
1、售前工程师仅仅是针对用户的需求，提供技术实现的方案。也就是说，在售前工程师工作时，有个前提假设，即用户需求的是已经得到确定或者是已经成型。而售前咨询师的工作大部分是通过对用户当前业务或者管理状况的分析，提出用户信息化的架构和策略，并且，根据此架构和策略，提供一套可以实现此架构和策略的方案。如果我们将投标作为一个临界点，那么售前工程师往往提供给用户的是标书，而售前咨询师提供给用户的一般为两个部分：信息化规划和信息系统建设建议书。
2、售前工程师要求对于技术实现、项目管理的熟悉程度要长于用户业务。因为用户的原始需求具有比较高的确定性，所以，只需要通过原始需求的分析，结合自己的技术知识和项目管理知识，为用户展现公司在某个项目上的技术和项目管理实例。而售前咨询师要求对用户的业务和管理理解程度要更高，即，更多的时候，售前咨询师是在对用户当前的业务状况和管理状况数据进行收集、统计和分析，通过对这些数据的利用，为用户提供一套有理有据有益的信息化策略和投资收益比率报告。

售前工程师-售前经理-行业顾问-行业专家

`售前工程师-知乎 <https://www.zhihu.com/topic/19705996/hot>`__

作者：项目经理职业生涯
链接：https://zhuanlan.zhihu.com/p/81982040
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

一、业务能力：

听：需求获取能力，客户需求引导公司产品及解决方案能力。

说：语言表达能力，产品及方案阐述能力，演讲能力，面对不同的群体的表达能力，再深一点能够快速识别现场的需求，然后迎合需求的表达能力。

读：产品阅读能力，客户现有痛点，其他竞品参与程度

写：方案编制能力，演讲材料编制能力，投标技术材料输出

动手能力：演示能力，客户场景设计能力，行业场景设计

能力知识面：行业背景，实际项目经验，专业技能知识，新兴技能掌握能力

二、非业务能力，软技能

人情世故：情商，如何管理好项目中销售，客户; 公司内领导、研发、实施及运维各个团队的需求。

教育背景：年薪30万以上，基本都是本科起步

项目管理技能：比较优秀的项目管理技能，特别熟悉买方的采购流程，懂得项目关键时间节点。

学习能力：新技术的学习能力，已有技术的掌握能力，新老技术组合产生的商机

抗压能力：大心脏，能够抗住客户现场的压力，能够顶住业绩指标的压力

形象及行为举止：客户现场你就是公司技术能力输出的代表，一言一行就是代表公司的能力那么对于售前岗位中业务和非业务两部分，业务能力反倒是通过职场经验的积累，是比较容易获得，而非业务技能，软技能是难以复制批量生产，才是一个卓越售前的核心竞争力。

业务技能决定你是否可以做售前工作，非业务技能决定你能否做好售前工作。


除了上述总结的售前技能，另外的核心技能按照优先级，我进行了排序。

核心一、主观能动性，积极，结果导向，破局能力，特别是有竞品参与。

核心二、项目把控能力，销售需求管理能力，销售是售前第一位的管理者，学会把握销售的需求是非常重要的。

核心三、按需说话，大心脏，能够快速客户的真实目标，临场应变能力，大局观，视角足够高，思考全面，经受得住时间的考验。

核心四、听说读写，专业技能，不可取代，察言观色。围绕目标，通过各种努力让客户买单，才能售前工程真正价值体现。

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
/H/tmp_H/001.work/002git/004output/backup/travis-output/test

/浮生六记.txt: OK

md5sum file > file.md5

md5sum -c file.md5

if [ "$a"x = "1"x ]; then sh 1.sh & echo "123";sh st.sh &;fi


shell 判断文件夹或文件是否存在                                 
文件夹不存在则创建                                             
                                                               
1                                                              
2                                                              
3                                                              
4                                                              
5                                                              
if [ ! -d "/data/" ];then                                      
mkdir /data                                                    
else                                                           
echo "文件夹已经存在"                                          
fi                                                             
文件存在则删除                                                 
                                                               
1                                                              
2                                                              
3                                                              
4                                                              
5                                                              
if [ ! -f "/data/filename" ];then                              
echo "文件不存在"                                              
else                                                           
rm -f /data/filename                                           
fi                                                             
判断文件夹是否存在                                             
                                                               
1                                                              
2                                                              
3                                                              
4                                                              
5                                                              
if [ -d "/data/" ];then                                        
echo "文件夹存在"                                              
else                                                           
echo "文件夹不存在"                                            
fi                                                             
判断文件是否存在                                               
                                                               
1                                                              
2                                                              
3                                                              
4                                                              
5                                                              
if [ -f "/data/filename" ];then                                
echo "文件存在"                                                
else                                                           
echo "文件不存在"                                              
fi                                                             
文件比较符                                                     
                                                               
1                                                              
2                                                              
3                                                              
4                                                              
5                                                              
6                                                              
7                                                              
8                                                              
9                                                              
10                                                             
11                                                             
12                                                             
13                                                             
-e 判断对象是否存在                                            
-d 判断对象是否存在，并且为目录                                
-f 判断对象是否存在，并且为常规文件                            
-L 判断对象是否存在，并且为符号链接                            
-h 判断对象是否存在，并且为软链接                              
-s 判断对象是否存在，并且长度不为0                             
-r 判断对象是否存在，并且可读                                  
-w 判断对象是否存在，并且可写                                  
-x 判断对象是否存在，并且可执行                                
-O 判断对象是否存在，并且属于当前用户                          
-G 判断对象是否存在，并且属于当前用户组                        
-nt 判断file1是否比file2新  [ "/data/file1" -nt "/data/file2" ]
-ot 判断file1是否比file2旧  [ "/data/file1" -ot "/data/file2" ]


comments, headers, footers, footnotes, endnotes, or text boxes.
citation,quotation

脚注是在每页的下面，整个文章最后的叫尾注。
脚注和参考文献

很多刊物对参考文献和注释作出区分，将注释规定为“对正文中某一内容作进一步解释或补充说明的文字”，列于文末并与参考文献分列或置于当页脚地。


引文和参考文献有哪些区别？

1、表意不同。

引文和参考文献表意不同。引文是科学对话的一种方法，是作者认为对自己的研究“有用”的资料，但同时也表明，引文的含义不是简单的。参考文献是在学术研究过程中，对某一著作或论文的整体的参考或借鉴。
2、在文章中的位置不同。

引文和参考文献在文章中的位置不同，引文可以出现在文章的任意位置，参考文献是征引过的文献在注释中已注明，不再出现于文后参考文献中。


论文的参考文献、脚注和注释分别有什么区别？citation,footnotes,endnotes
https://www.keoaeic.org/featured/2006.html



sci论文格式
https://www.keoaeic.org/featured/4444.html

科学论文格式
https://www.keoaeic.org/featured/4441.html


中通544502058736
黄奇帆最新演讲：今后10年，中国经济将发生5个历史性变化2019-09-19 22:00
http://www.sohu.com/a/342036219_465485

黄奇帆最新演讲：房价暴涨已成历史，这三个地方还有机会（全文）
http://baijiahao.baidu.com/s?id=1639932463141834164&wfr=spider&for=pc

黄奇帆新年再支招中国股市！全是干货
https://baijiahao.baidu.com/s?id=1622599558371649716&wfr=spider&for=pc

英语学习者该如何打磨欧路词典？
https://www.zhihu.com/question/21328313


金融服务咨询公司Opimas报告显示：到2025年，全球金融机构将减员10%，近23万人将受到影响，电脑将取代他们的工作。在这些被裁的岗位中，40%都将来自资产管理部门。


上海携宁计算机科技股份有限公司于2003年2月20日
挂牌日期：2015-10-22


第十一条 发行人申请首次公开发行股票应当符合下列条件：
（一）发行人是依法设立且持续经营三年以上的股份有限公司。有限责任公司按原账面净资产值折股整体变更为股份有限公司的，持续经营时间可以从有限责任公司成立之日起计算；

（二）最近两年连续盈利，最近两年净利润累计不少于一千万元；或者最近一年盈利，最近一年营业收入不少于五千万元。净利润以扣除非经常性损益前后孰低者为计算依据； [1] 
（三）最近一期末净资产不少于二千万元，且不存在未弥补亏损；


报告期内，上交所科创板的开板，给公司投研系统升级带来契机，公司与数十家客户就投研系统 的科创板升级达成合作协议，这些项目将在 19 年下半年实现验收和收入确认。

报告期内，公司结合深度学习、知识图谱、大数据等技术，在人工智能领域加强了研发投入，公 司的“知丘”产品实现了重大升级，同时推出“鱼雷”、“有数”等新的资讯、投决支持产品。公司认 为现在是非常重要的产品战略机遇时期，紧紧抓住技术和行业的变化动态，加大研发投入的密度和强
度是极其有必要的，这些新的研发活动将对公司未来的规模和利润形成积极影响。

19 年 4 月公司中标招商银行理财子公司的非标项目管理系统，标志着公司在银行理财子行业的拓
展正式起步

公司主要从事投资研究、客户管理、基金销售以及程序化平台等金融行业软件产品的研发、销售 及服务，主要的客户群包括证券公司、基金公司、保险公司、信托公司、银行以及其他资管类公司

软件行业技术进步快、产品更新快、客户需求变化快的特 点，并在投研、基金销售等金融软件产品方面具有较为显著的竞争优势。但是，技术更新和产品开发 始终是软件行业需要面临的课题，也将对公司未来的市场竞争力产生重大影响，如果公司不能正确把握自身软件产品发展的方向，及时调整技术和开发新的产品，或开发掌握的新技术、新产品不能有效
地在市场上进行推广，公司将面临技术更新与产品开发的风险。

人才是软件企业的核心竞争力之一，是软件企业的第一生产力，未来软件企业的市场竞争将会表 现为高素质人才的竞争。

摩根大通在技术方面投入巨资。根据其最新财务报表显示，
2018年科技支出为88亿美元，同比增长14%。

除此之外，摩根大通还在疯狂招Fintech人才！摩根大通在加州Palo Alto办公室计划于明年开业，这是一个“新金融科技园区”，将容纳多达1,000名与金融技术相关的员工，包括不断增长的人工智能团队。

华尔街现在到底有多爱Fintech？

华尔街早已开始AI的大规模实践和应用，目前许多岗位已被机器人和自动化程序替代。高盛已经开始使用机器人来帮助公司进行IPO进程；瑞银使用AI对客户的行为模式进行分析，为其提供更好的财富管理方案。

过去几年，华尔街各大银行巨头纷纷成立自己的战略投资部门，积极投资金融科技公司，以雄厚的资金优势来换取金融科技创业者的新技术与新商业模式。


银行理财占理财市场30%

五大国有银行理财子公司开业
2019年6月初
工银理财 北京
建信理财 深圳
2019年6月13日
交银理财 上海
2019年7月4日
中银理财 北京
2019年8月8日
农银理财 北京

7家银行理财子公司获批筹建
邮政储蓄银行
招商/光大/兴业 股份银行
杭州银行/宁波银行/徽商银行

20家银行公告等待获批。

公募基金＋私募基金＋类信托 全能型牌照

监管规定 刚兑 2020年底

银行理财产品销售渠道进一步扩大化，从而可以在更广泛的途径实现银行理财产品的购买和销售

银行理财子公司理财产品投资更加资本市场化

理财市场 三分天下格局 银行理财 保险/信托/证券理财 其它理财机构

销售渠道格局 销售全渠道化 无销售边界


2018.4 “资管新规”
《关于规范金融机构资产管理业务的指导意见》 
银保监会、证监会、外汇管理局

2018.9 “理财新规”
《商业银行理财业务监督管理办法》
银保监会

2018.12 ‘理财子公司管理办法’
《商业银行理财子公司管理办法》 
银保监会


金融科技关键技术

金融科技的关键技术，包括互联网技术（互联网、移动互联网、物联网），大数据，人工智能，分布式技术（区块链、云计算），安全技术（生物识别技术）等。


2019.9.6 央行发布《金融科技(FinTech)发展规划(2019-2021年)》
央行上海总部《关于促进金融科技发展支持上海建设金融科技中心的指导意见》

大数据
人工智能
云计算
上线一批基于人工智能、大数据、区块链、生物认证等技术的金融科技服务平台
鼓励金融机构创新思维与经营理念、顺应智能发展态势，借助云计算、区块链、人工智能、生物识别等技术，依托金融大数据平台，找准突破口和主攻方向，在智慧网点、智能客服、智能投顾、智能风控等金融产品和服务方面进行创新。

金融服务咨询公司Opimas报告显示：到2025年，全球金融机构将减员10%，近23万人将受到影响，电脑将取代他们的工作。在这些被裁的岗位中，40%都将来自资产管理部门。

摩根大通去年宣布，计划在旧金山帕洛阿尔托开设一个新的金融科技园区，这个最终能容纳1000人的园区将于2020年开放，这意味着会有大批的AI，机器学习人才坐阵。

Bloomberg采访了很多华尔街金融机构的高管，制作了一系列自动化交易图。红色方框底部的黑色文字是在交易过程中使用的人工智能技术，包括机器学习(ML)、自然语言处理(NLP) 、机器人过程自动化(PRA) 、预测分析(PA)。

研究：

相关知识

OLTP和OLAP

Pentaho：
kettle:spoon pan kitchen
ETL:
ETL，是英文Extract-Transform-Load的缩写，用来描述将数据从来源端经过抽取（extract）、转换（transform）、加载（load）至目的端的过程。

DB->ODS->DW->Dm
SDATA-PDATA-CDATA-MDATA
操作型数据存储（ODS，operational data store）是一种常被用作数据仓库临时区域的数据库。
操作型数据存储可用于整合来自多种源的不同数据，这样在进行业务操作时，可以执行业务分析和报告。当前操作中使用的大部分数据在被转入数据仓库进行长期存储或归档之前，就存储在操作型数据存储中。
操作型数据存储（ODS）是专为相对简单的少量数据查询设计的（如查找客户订单状态），而不是对数据仓库中的大量复杂数据进行查询。操作型数据存储类似于人的短期记忆，因为它只能存储最近的信息，相反，数据仓库更像是长期记忆，它存储相对永久的信息。

数据仓库（DW）
决策支持系统（DSS）
在线分析处理（OLAP）
数据挖掘（DM）
商业智能（BI）

疑问记录

1
位置：
数据挖掘->资产负债分析->银行存款-双击编辑>指标：ZCFZB.BANK_DEPOSITS

问题：
指标的公式在哪里。

2
报表管理->web报表5.0->.rpx rpg .sht 是什么东西

3
指标管理->算法引擎->SFTP配置。 什么是SFTP? 配了sftp从这里拿什么过来？
代码管理是什么代码？由谁来写和上传的。以及这些代码和实际指标的名称在哪里对应。
缓存表管理：是做什么的？
指标维护：
绩效评估->风险分析-上行标准差
SP_INDEX_CENTER_TOTAL_PKG.FUN_RISK_UPSIDESTDEV( 这是python写的库么

这些指标在哪里用的？

维度指什么？什么叫单维多维？

哪些是客户可以定制的？定制的流程是怎么样的？
公司的已有指标，哪些可以公开，哪些是可以收费的？

repair 维修 
=====================================================================

空调
---------------------------------------------------------------------

`空调重要元器件——滤波电感 <http://www.360doc.com/content/19/0827/06/58189075_857277691.shtml
>`_ 

resume 简历 
=====================================================================

已联系情况
---------------------------------------------------------------------

联系人  简历  日间  备注
TZ投资-杨苓-云基地，创智天地  已发hw  20200115  薪水要求20k左右
ZJL赵金龙-intel  已发intel  20200115  上海hr回复iot已招好人
TQ唐庆  已发hw  20200115 
LZY刘志扬-海思  已发hw  20200115
WXF王雪峰-cloudera  未发  20200115
gene-cloudera  已发  20200115  回复等headcount，再通知
傅盛  未发  20200116  回复HEHE
徐铮lsi  已发intel  20200116  已推荐给芯原和猎头，会安排节后和总经理谈一下
徐铮HW  未发  20200116  可以推荐给徐德好，总经理，称做不了
刘江涛  已发intel  20200116  春节后再说，称本周末在南方见一下
牛立伟  未发  20200116  称有空电话里详谈
王栋    未发  20200116  称研发部门还在招人
杨成功  未发  20200116  未接话
蔡照明  未发  20200116  称不懂这个行业
eric博通  未发  20200116  未回复
david-mavell  未发  20200116  称不在mavell,没有继续谈


公司job网站
---------------------------------------------------------------------

1. intel
   
   jobs.intel.com

2. arm
   


3. cloudera


<<<<<<< HEAD
4. qualcomm
   
   https://www.qualcomm.cn/company/careers
=======
干脆把图片导入到CDR中再描不是好一点吗？如果图比较简单的话，还可以用CDR的描幕位图功能来做，自动生成矢量图。


建议到nocang<http://www.nocang.com/office2016/>下载office2016/visio2016，注意区分32位和64位。
1.建议用KMSAuto Pro Net 2015 1.3.8激活工具直接激活，关闭杀毒软件和防火墙，运行后自动激活office/visio/project2010/13/16/win7/8/8.1/10系列系统。
2.电话或密钥激活比较费时间，软件激活方法已经很常见了，成功率也高，没必要用电话或密钥激活。该工具可以自动将零售版转换为VOL版。只要不卸载相关服务，是自动续期永久激活的。
https://zhidao.baidu.com/question/1244597580843857739.html

https://www.nocang.com/vs2019zhuanyeban/   
vs2019专业版激活序列号密钥，无需任何破解工作即可免费长久使用，需要的朋友赶紧下载使用吧。vs2019专业版激活序列号密钥：NYWVH-HT4XC-R2WYW-9Y3CM-X4V3Y。

https://www.nocang.com/microsoft-visio-2016/
Microsoft Visio 2016官方简体中文32位+64位破解版下载（含序列号密钥）

https://www.nocang.com/office-2016-rtm/
office2016

https://www.nocang.com/office2016/
Office2016/Project2016/Visio2016官方32位+64位大客户版下载(含激活工具)
kl+:上面这个网址最全

http://www.visiocafe.com
visio 模具

https://www.cnblogs.com/zhqian/p/9406520.html
office 2016 官方原版 （含Visio Project 等全套 ）下载地址 （不含破解，非网盘下载）不用登录
https://www.cnblogs.com/zhqian/p/9406520.html

http://www.zdfans.com/html/27514.html
techsmith camstasia
>>>>>>> 54d7771b54c748ee1d33ed10f51f07f48a33a2e0
