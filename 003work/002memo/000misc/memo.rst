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

` <>`__

` <>`__

` <>`__
