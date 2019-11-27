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


