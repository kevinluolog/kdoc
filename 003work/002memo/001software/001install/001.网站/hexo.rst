***************
hexo
***************

.. contents:: 目录
.. section-numbering::

.. 
 :Author: kevinluo
 :Contact: kevinluo_72@163.com

.. 
 .. contents:: 目录
 .. section-numbering::


install
=======

`Installation guide on hexo.io <https://hexo.io/docs/>`__

`手把手教你使用Hexo + Github Pages搭建个人独立博客 <https://segmentfault.com/a/1190000004947261>`__

hexo module 安装
----------------

::

  npm install hexo-cli -g

hexo module安装到node目录node_modules，根目录有hexo.cmd

hexo blog init
--------------

::

  $ cd d:/hexo
  $ npm install hexo-cli -g
  $ hexo init blog
  $ cd blog
  $ npm install
  $ hexo g # 或者hexo generate
  $ hexo s # 或者hexo server，可以在http://localhost:4000/ 查看


另外还有其他几个常用命令：

::

  $ hexo new "postName" #新建文章
  $ hexo new page "pageName" #新建页面


常用简写

::

  $ hexo n == hexo new
  $ hexo g == hexo generate
  $ hexo s == hexo server
  $ hexo d == hexo deploy
  
  
常用组合
  
::

  $ hexo d -g #生成部署
  $ hexo s -g #生成预览

现在我们打开 ``http://localhost:4000/`` 已经可以看到一篇内置的blog。

configuration
-------------

`hexo.io/docs/configuration <https://hexo.io/docs/configuration>`__


Commands
--------

Migration
---------

Basic Usage
===========



Customization
=============



Permalinks

Themes

`hexo.io-spec-配置 <https://hexo.io/zh-cn/docs/configuration.html>`__


Templates

Variables

Helpers

Internationalization (i18n)

Plugins
  
  
  
theme分享
=========

几款简单的theme
---------------

`【Hexo】推荐5款简洁美观的主题  <https://www.jianshu.com/p/f4ae9ee1328a>`__

推荐第一款。理由简单，全文字，色调浅色系不扎眼。

1. `hexo-theme-polarbear <https://github.com/frostfan/hexo-theme-polarbear>`__

   `demo <https://d2fan.com/>`__

#. `hexo-theme-xoxo <https://github.com/KevinOfNeu/hexo-theme-xoxo>`__
   
   `demo <https://d2fan.com/>`__

#. `hexo-theme-sky <https://github.com/iJinxin/hexo-theme-sky>`__
   
   `demo <https://ijinxin.github.io/>`__



melody
------

`hexo-theme-melody-doc <https://molunerfinn.com/hexo-theme-melody-doc/>`__

melody-设置
^^^^^^^^^^^


fireworks,live2d 白猫 animation
"""""""""""""""""""""""""""""""

`detail guide on melody doc <https://molunerfinn.com/hexo-theme-melody-doc/third-party-support.html#installation>`__

- fireworks

  Like the `anime.js <http://animejs.com/>`__ clicking effects
  
  Set the melody.yml
  
  ::
  
      fireworks: true

- Live2D Animated model pendant

  install the Live2D module, which needs to be executed in the root   directory of the blog through the terminal:
  
  ::
  
      npm install --save hexo-helper-live2d


  The corresponding module is downloaded `here <https://github.com/xiazeyu/live2d-widget-models>`__ , For example,  tororo(Cute White Cat)

  copy all the files in packages to the node_moduels folder in the root directory of the blog.

  or install as following:

  ::

      npm install {packagename} 

      The package name is the folder name in packages/ such as:
      live2d-widget-model-chitose
      live2d-widget-model-tororo

next
----

next-设置
^^^^^^^^^


busuanzi_count 阅读次数/访问人数
""""""""""""""""""""""""""""""""

- 原理： 

  页面植入busuanzi提供的js链接代码，
  在 ``\themes\next\layout\_partials\analytics\busuanzi-counter.swig`` 中

  ::

     <script{{ pjax }} async src="https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>
  

  同时在相应的页面模板加入阅读次数等数据。
  其提供单页文章和全站的字数和次数信息。next分别把它放在页面标题下面和footer底部。
  其渲染过程仍不清楚，

  页面标题下面：
  
  在 ``\themes\next\layout\_macro\post.swig`` 中,只是 ``<span class="busuanzi-value" id="busuanzi_value_page_pv"></span>``  没有实体，不知什么时候，渲染进去的？

  footer底部,全站的访问人数等数据：

  在 ``\themes\next\layout\_partials\analytics\busuanzi-counter.swig``  中，此处我增加了一个theme变量来控制

  ::

     {%- if theme.kl_footer_eye === true %}



symbols_count_time 文章字数统计与阅读时长
"""""""""""""""""""""""""""""""""""""""""

同样全站的显示的FOOTER, 单文章显示在文章title下面。

配置使能要注意：

模块说明里就说明，使能要在root/_config.yml中加入，

::

    symbols_count_time: ## 此处定义是用来控制模块计算的。下面的变量和next.yml中的配    置一起控制字数和时长显示与否。要同时设置才有效果。
      symbols: true
      time: true
      total_symbols: false ##kl+ true
      total_time: false ##kl+ true
      exclude_codeblock: false ##kl+ false

同时在theme的_config.yml中，同样要使能，

::

    symbols_count_time: ## 此处定义是用来控制显示的。klblog\_    config.yml中是用来控制模块计算的。下面的变量和klblog\_    config.yml中中的配置一起控制字数和时长显示与否。要同时设置才有效果。
      separated_meta: true ##kl+ true 换行显示
      item_text_post: true ##kl+ true
      item_text_total: true ##kl+ false
      awl: 4
      wpm: 275

- 删除footer底部的全站字数，时长信息。
  
  只要在 ``root\_config.yml`` 中

  ::

      total_symbols: false ##kl+ true
      total_time: false ##kl+ true

- 文章字数统计与阅读时长，取不到数据
  
  hexo clean 一下，再编译就可以了，原因不明。


hexo-Next修改内容区域的宽度
"""""""""""""""""""""""""""

`如何更改内容区域的宽度？ <http://theme-next.iissnan.com/faqs.html#custom-content-width>`__

`leeze Hexo之修改内容区域的宽度 <http://leeze.coding.me/2019/09/03/hexoarea/>`__

在 ``\themes\next\source\css\_variables\base.styl`` 

::

    //kl+ new,参见
    //当屏幕宽度 < 1600px
    $content-desktop                = 900px;
    //当屏幕宽度 >= 1600px
    $content-desktop-large          = 900px;
    $content-desktop-largest        = 900px;


实现点击出现桃心效果animation
"""""""""""""""""""""""""""""

在 ``/themes/*/source/js/src下新建文件click.js`` ，接着把以下粘贴到click.js文件中。

代码如下：

::

    !function(e,t,a){function n(){c(".heart{width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);}.heart:after,.heart:before{content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: fixed;}.heart:after{top: -5px;}.heart:before{left: -5px;}"),o(),r()}function r(){for(var e=0;e<d.length;e++)d[e].alpha<=0?(t.body.removeChild(d[e].el),d.splice(e,1)):(d[e].y--,d[e].scale+=.004,d[e].alpha-=.013,d[e].el.style.cssText="left:"+d[e].x+"px;top:"+d[e].y+"px;opacity:"+d[e].alpha+";transform:scale("+d[e].scale+","+d[e].scale+") rotate(45deg);background:"+d[e].color+";z-index:99999");requestAnimationFrame(r)}function o(){var t="function"==typeof e.onclick&&e.onclick;e.onclick=function(e){t&&t(),i(e)}}function i(e){var a=t.createElement("div");a.className="heart",d.push({el:a,x:e.clientX-5,y:e.clientY-5,scale:1,alpha:1,color:s()}),t.body.appendChild(a)}function c(e){var a=t.createElement("style");a.type="text/css";try{a.appendChild(t.createTextNode(e))}catch(t){a.styleSheet.cssText=e}t.getElementsByTagName("head")[0].appendChild(a)}function s(){return"rgb("+~~(255*Math.random())+","+~~(255*Math.random())+","+~~(255*Math.random())+")"}var d=[];e.requestAnimationFrame=function(){return e.requestAnimationFrame||e.webkitRequestAnimationFrame||e.mozRequestAnimationFrame||e.oRequestAnimationFrame||e.msRequestAnimationFrame||function(e){setTimeout(e,1e3/60)}}(),n()}(window,document);


在 ``\themes\*\layout\_layout.swig`` 文件末尾body内添加:

::

    <!-- 页面点击小红心 -->
    <script type="text/javascript" src="/js/clicklove.js"></script>


目录栏链接选中颜色
""""""""""""""""""

copy到

::

    // Sidebar
    // --------------------------------------------------
    $sidebar-nav-hover-color          = $orange;
    $sidebar-highlight                = $orange;
 
    $toc-link-color                       = $grey-dim;
    $toc-link-border-color                = $grey-light;
    $toc-link-hover-color                 = black;
    $toc-link-hover-border-color          = black;
    $toc-link-active-color                = $sidebar-highlight;
    $toc-link-active-border-color         = $sidebar-highlight;
    $toc-link-active-current-color        = $sidebar-highlight;
    $toc-link-active-current-border-color = $sidebar-highlight;


custom path
"""""""""""



Maupassant - Hexo最简洁主题 - cho
---------------------------------

`大道至简——Hexo简洁主题推荐 <https://www.haomwei.com/technology/maupassant-hexo.html>`__

安装
^^^^^

注：若\ ``npm install hexo-renderer-sass``\ 安装时报错，可能是国内网络问题，请尝试使用代理或者切换至\ `淘宝NPM镜像 <http://npm.taobao.org>`__\ 安装。 ``npm install hexo-renderer-sass``\ 

出现问题: hexo 3.8.0用淘宝镜像装hexo-renderer-sass，生成的网页有问题，装hexo-renderer-scss，就没问题了。
kl: 建议尽量用npm来安装。

1. 安装主题和渲染器：

   ::

      $ git clone https://github.com/tufu9441/maupassant-hexo.git themes/    maupassant
      $ npm install hexo-renderer-pug --save
      $ npm install hexo-renderer-sass --save


#. 编辑Hexo目录下的
   
   ``_config.yml``\ ，将\ ``theme``\ 的值改为\ ``maupassant``\ 。


#. hexo-wordcount 字数统计，阅读时长：缺省没装
   
   这是在 ``_config.yml`` 中设置 ``wordcount: true ##kl+ false`` 时报错的。

   参考 `Hexo-文章字数统计与阅读时长 <https://www.jianshu.com/p/f615e79a50d7>`__

   
   ``npm i --save hexo-wordcount``

   因缺省已经使能。下面修改不用了，可以作用改动参考

   1. 在maupassant主题下的新建一个wordcount.pug文件
      
      ``themes\maupassant\layout\_partial\wordcount.pug
      wordcount.pug`` 文件增加内容：
      
      ::

         span(class="post-time")
           span.post-meta-item-text= " | "
           span(class="post-meta-item-icon")
             i(class="fa fa-keyboard-o")
             // span.post-meta-item-text= " 字数统计："
             span.post-count= ' '+wordcount(page.content)
             span.post-meta-item-text= ' 字'
         span(class="post-time") &nbsp; | &nbsp;
           span(class="post-meta-item-icon")
               i(class="fa fa-hourglass-half")
               // span.post-meta-item-text= " 阅读时长："
               span.post-count= ' '+min2read(page.content)
               span.post-meta-item-text= " 分钟"
   2. 在 ``themes\maupassant\layout\post.pug``  文件中引入wordcount.pug文件（我自定义的位置在busuanzi与disqus之间）
      
      ::

          if theme.busuanzi == true
            script(src='https://dn-lbstatics.qbox.me/          busuanzi/2.3/busuanzi.pure.mini.js', async)
            span#busuanzi_container_page_pv= ' | '
              span#busuanzi_value_page_pv
              span= ' ' + __('Hits')
          include _partial/wordcount.pug
          if theme.disqus

设置
^^^^^

1. in _config.yml

   fontawesome:
   
   | fa-home
   | fa-th categories
   | fa-tags
   | fa-history
   | fa-user
   | fa-book
   
   ::

     show_category_count: false
     wordcount: true ## 统计字数
     widgets_on_small_screens: true
     busuanzi: true ##kl+ false，网页访问统计
   
   
     menu:
       - page: home
         directory: .
         icon: fa-home
         
     widgets:
       - search
       - category
       - tag

hexo plugin插件
===============

Generate flowchart diagrams for Hexo.
-------------------------------------

`hexo-filter-flowchart <https://github.com/bubkoo/hexo-filter-flowchart>`__

- install
  
  npm install --save hexo-filter-flowchart

  setting: 实测下面的不改动也可以显示出来

  ::
  
    Config
    In your site's _config.yml:

    flowchart:
      # raphael:   # optional, the source url of raphael.js
      # flowchart: # optional, the source url of flowchart.js
      options: # options used for `drawSVG`


This plugin is based on `flowchart.js <https://github.com/adrai/flowchart.js>`__, so you can defined the chart as follow:

```flow
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|request

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2->e
```

hexo-generator-feed
-------------------

`github download <https://github.com/hexojs/hexo-generator-feed.git>`__

Install

::

    $ npm install hexo-generator-feed --save
    Hexo 3: 1.x
    Hexo 2: 0.x

Use

In the front-matter of your post, you can optionally add a description, intro or excerpt setting to write a summary for the post. Otherwise the summary will default to the excerpt or the first 140 characters of the post.

Options

You can configure this plugin in _config.yml.

::

    feed:
      type: atom
      path: atom.xml
      limit: 20
      hub:
      content:
      content_limit: 140
      content_limit_delim: ' '
      order_by: -date
      icon: icon.png

type - Feed type. (atom/rss2)
path - Feed path. (Default: atom.xml/rss2.xml)
limit - Maximum number of posts in the feed (Use 0 or false to show all posts)
hub - URL of the PubSubHubbub hubs (Leave it empty if you don't use it)
content - (optional) set to 'true' to include the contents of the entire post in the feed.
content_limit - (optional) Default length of post content used in summary. Only used, if content setting is false and no custom post description present.
content_limit_delim - (optional) If content_limit is used to shorten post contents, only cut at the last occurrence of this delimiter before reaching the character limit. Not used by default.
order_by - Feed order-by. (Default: -date)
icon - (optional) Custom feed icon. Defaults to a gravatar of email specified in the main config.

hexo-generator-search
---------------------

产生搜索功能，search.XML

::

    $ npm install hexo-generator-search --save



hexo-symbols-count-time for next theme
--------------------------------------

::

    $ npm install hexo-symbols-count-time --save

hexo-generator-category
-----------------------

::

    $ npm install hexo-generator-category --save
    option:
    tag_generator:
      per_page: 10
      order_by: -date
      

hexo-generator-tag
------------------

::

    $ npm install hexo-generator-tag --save
    Options
    tag_generator:
      per_page: 10
      order_by: -date


hexo-directory-category
-----------------------

Automatically add front-matter categories to Hexo article according to the article file directory.

Directory is means relative form article file path to Hexo source _posts folder.

`github-hexo-directory-category <https://github.com/zthxxx/hexo-directory-category>`__

::

    npm install --save hexo-directory-category
    auto_dir_categorize:
        enable: true  # options:true, false; default is true
        force: false # options:true, false; default is false
    enable - Enable the plugin. Defaults to true.
    force - Overwrite article front-matter categories, even if it has option categories.Defaults to false.


some module install
-------------------

::

   $ npm install hexo-generator-search --save
   $ npm install hexo-symbols-count-time --save
   
   
   $ npm install hexo-generator-category --save
   option:
   tag_generator:
     per_page: 10
     order_by: -date
     
     
   $ npm install hexo-generator-tag --save
   Options
   tag_generator:
     tag_generator:true
     per_page: 10
     order_by: -date   

hexo高级教程
============

参考

`Hexo高级教程 <https://www.jianshu.com/nb/33192262>`__

`hexo脚本编写指南（一） <https://www.jianshu.com/p/26b5a0b59cdd>`__

`Hexo Docs（三）- 高级进阶 <https://www.jianshu.com/p/12279cabca81>`__

`脚本需要掌握hexo api <https://hexo.io/zh-cn/api/>`__

`nodejs doc-en <https://nodejs.org/en/docs/>`__

`nodejs debug guide <https://nodejs.org/en/docs/guides/debugging-getting-started/>`__

`nodejs doc-zh 中文 <https://nodejs.org/zh-cn/docs/>`__

教程

`Node.js 教程 <https://www.runoob.com/nodejs/nodejs-tutorial.html>`__

`hexo-generator-category 源码分析 <https://www.jianshu.com/p/fe2074527ca2>`__


`hexo-generator-tag 源码分析 <https://www.jianshu.com/p/470904307d2c>`__

`hexo-generator-index 源码分析 <https://www.jianshu.com/p/7bec9866a04d>`__

`next主题的模板引擎swig语法介绍 <https://www.jianshu.com/p/c5d333e6353c>`__


脚本Script
----------

只需要把 JavaScript 文件放到 scripts 文件夹，在启动时就会自动载入。

hexo扩展
--------



1. 控制台 (Console)

#. 部署器 (Deployer)

#. 过滤器 (Filter)

#. 生成器 (Generator)

#. 辅助函数 (Helper)

#. 迁移器 (Migrator)

#. 处理器 (Processor)

#. 渲染引擎 (Renderer)

#. 标签 (Tag)

tips
=======

tortoiseGit使用密钥，为何每次还是需要输入用户名密码
-------------------------------------------------------

`tortoiseGit使用密钥，为何每次还是需要输入用户名密码 <https://gitee.com/oschina/git-osc/issues/I57KR?from=project-issue>`__

Q:tortoiseGit使用密钥，为何每次还是需要输入用户名密码

A:那个URL应该选择ssh的，也就是以git@git.oschina.net:{username}/{repo name}
这种形式的，你虽然把SSH key加进去了，
但是你如果仍使用的是https方式，当然要提示输入用户名密码了。
如，git@github.com:kevinluolog/hexo-klblog-src.git

不过用https方式访问，也有方法可以免手工输入用户名密码的。

方法1：直接带入，https://{用户名}：{密码}@github.com/{username}/{repo name}
如， `https://kevinluolog:XXX@github.com/kevinluolog/hexo-next-muse.git`

方法2：利用token, 当然先要创建。
如， `https://gh_token@github.com/kevinluolog/hexo-next-muse.git`

怎么改掉网页底部的COPYRIGHT缺省内容？
----------------------------------------

::

  \hexo\klBlog\themes\maupassant-hexo\layout\_partial\footer.pug(7):   a(rel='nofollow', target='_blank', href='https://github.com/pagecho')  Cho.
  
    #footer= 'Copyright © ' + date(Date.now(), 'YYYY') + ' '
      a(href=url_for('.'), rel='nofollow')= config.title + '.'
      |  Powered by
      a(rel='nofollow', target='_blank', href='https://hexo.io')  Hexo.
      a(rel='nofollow', target='_blank', href='https://github.com/tufu9441/maupassant-hexo')  Theme
      |  by
      a(rel='nofollow', target='_blank', href='https://github.com/pagecho')  Cho.

help 网址
---------

非常详细的教程，看完照做就可以了。这个写手做事非常细致。就象博主自己讲的 -- `我走的很慢，但我从不后退。`

`Hexo使用攻略 index <http://ijiaober.github.io/2014/08/02/hexo/hexo-index/>`__

.. 此处不用这样的内联形式链接，是因为pandoc 不支持，所以用下面的独行模式。情况类似 frontmatter-categories
 `Hexo博客从搭建部署到SEO优化等详细教程 <https://www.jianshu.com/p/efaf72aab32e>`_

Hexo博客从搭建部署到SEO优化等详细教程_

.. _Hexo博客从搭建部署到SEO优化等详细教程: https://www.jianshu.com/p/efaf72aab32e

`Hexo seo org <https://www.jianshu.com/p/efaf72aab32e>`_


`hexo-theme-maupassant-中文help-大道至简——Hexo简洁主题推荐 <https://www.haomwei.com/technology/maupassant-hexo.html>`__

`hexo主题中添加相册功能 <https://www.cnblogs.com/xljzlw/p/5137622.html>`__
 http://lwzhang.github.io/

`hexo-generator-index 源码分析 <https://www.jianshu.com/p/7bec9866a04d>`__

很好的主题开发文章

`Hexo主题开发经验杂谈org <https://molunerfinn.com/make-a-hexo-theme/#%E5%89%8D%E8%A8%80>`__

参考hexo渲染的事件，可以找到generateBefore这个钩子hook，只要在这个钩子触发的时候，判断一下存不存在data files里的配置文件_data\/next.yml，存在的话就把这个配置文件替换或者合并主题本身的配置文件。Next主题采用的是覆盖，melody主题采用的是替换。各有各的好处，并不是绝对的。

写法是就是在我们的temp主题目录下的scripts文件夹里（没有就创建一个），写一个js文件，内容如下：

::

  /**
   * Note: configs in _data/temp.yml will replace configs in   hexo.theme.config.
   */
  hexo.on('generateBefore', function () {
    if (hexo.locals.get) {
      var data = hexo.locals.get('data') // 获取_data文件夹下的内容
      data && data.temp && (hexo.theme.config = data.temp) // 如果temp.yml   存在，就把内容替换掉主题的config
    }
  })

`Hexo主题开发经验杂谈 <https://juejin.im/entry/59ba97216fb9a00a6b6e50bf>`__

字体大清晰。文字title
`hexo-theme-random <https://github.com/stiekel/hexo-theme-random>`__

`Hexo 主题开发指南-random-不可能不确定 <http://chensd.com/2016-06/hexo-theme-guide.html>`__


theme-front-matter
------------------

在 ``\source\*.md`` 文件的开头

::

    ---
    title: sublime
    date: 2019-09-03 17:31:37
    toc: true
    mathjax: true
    tags: 
    - 技术
    - 文本编辑器
    categories:
    - 技术
    - sublime
    ---

.. 
 - 分类 _`frontmatter-categories`

.. 此处不用内联形式，因为pandoc转成md时不支持，参见注解，Hexo博客从搭建部署到SEO优化等详细教程。 同时注意下面单行段落链接的定义要和前面LIST的开头对齐。

- 分类frontmatter-categories

  .. _frontmatter-categories:

  编辑文章的时候，直接在categories:项填写属于哪个分类，但如果分类是中文的时候，路径也会包含中文。

  访问路径是：

  ``*/categories/编程``

  想要把路径名和分类名分别设置，参见 `路径名和分类名分别设置，需要怎么办呢？`_

- 标签frontmatter-tags
  
  .. _frontmatter-tags:

  在编辑文章的时候，tags:后面是设置标签的地方，如果有多个标签的话，可以用下面两种办法来设置：

  ::

     tages: [标签1,标签2,...标签n]

     tages: 
     - 标签1
     - 标签2
     ...
     - 标签n


- 文章摘要description:
  
  .. 文章摘要description:

  首页默认显示文章摘要而非全文，可以在文章的front-matter中填写一项description:来设置你想显示的摘要，或者直接在文章内容中插入<!--more-->以隐藏后面的内容。
  
  若两者都未设置，则自动截取文章第一段作为摘要。

- 添加页面 layout:
  在source目录下建立相应名称的文件夹，然后在文件夹中建立index.md文件，并在index.md的front-matter中设置layout为layout: page。若需要单栏页面，就将layout设置为 layout: single-column。


- 文章目录frontmatter-toc:
  
  .. _frontmatter-toc:

  在文章的front-matter中添加toc: true即可让该篇文章显示目录。

- 文章评论 comments:
  
  文章和页面的评论功能可以通过在front-matter中设置comments: true或comments: false来进行开启或关闭（默认开启）。

- 数学公式frontmatter-mathjax: 
  
  .. _frontmatter-mathjax:

  要启用数学公式支持，请在Hexo目录的_config.yml中添加：

  1. mathjax: true
     
     并在相应文章的front-matter中添加mathjax: true，例如：

     ::

        title: Test Math
        date: 2016-04-05 14:16:00
        categories: math
        mathjax: true
        ---

     数学公式的默认定界符是 `$$...$$和\\[...\\]（对于块级公式），以及$...$和\\(...\\)     （对于行内公式）` 。

  2. mathjax2: true

     但是，如果你的文章内容中经常出现美元符号“$”, 或者说你想将“$”用作美元符号而非行内公     式的定界符，请在Hexo目录的_config.yml中添加：
     
     而不是mathjax: true。      相应地，在需要使用数学公式的文章的front-matter中也添加mathjax2: true。
     
- donate: donate:
  
  enable: false ## If you want to show the donate button after each post, please set the value to true and fill the following items according to your need. You can also enable donate button in a page by adding a "donate: true" item to the front-matter.

- timeline: (layout: timeline)
  
  网站历史时间线，在页面front-matter中设置layout: timeline可显示。

hexo editor 编辑器有哪些？
-----------------------------



- Markdown 工具 HexoEditor

  `一款清新的 Markdown 工具 HexoEditor，重要的是支持 Hexo 框架 <https://www.v2ex.com/amp/t/421246>`__

  `github repo-hexo editor <https://github.com/zhuzhuyule/HexoEditor>`__


怎么使用 yeoman 生成基础代码？
--------------------------------

现在开始项目之前，我都会搜索一下 yeoman 有没有库，生成 Hexo 主题就有 generator-hexo-theme 。如果还没有安装 yeoman ，那先用 npm 全局安装。

::

    npm i -g yo

安装生成器的库：

::

    npm i -g generator-hexo-theme

到博客目录下，进入到 themes 目录，创建一个用主题名命名的新文件夹，比如test，进入新文件夹，开始生成代码：

::

    yo hexo-theme

然后选择一些基本的配置，比如使用什么模板引擎，使用什么 CSS 预编译等，这里分别选择 Swig 和 Stylus。完成之后，主题目录下就会生成一些如下结构的文件：

::

    ├── _config.yml // 主题配置文件
    ├── languages // 多语言文件夹
    ├── layout
    │   ├── archive.swig // 存档页模板
    │   ├── category.swig // 分类文章列表页模板
    │   ├── includes // 各页面共享的模板
    │   │   ├── layout.swig // 页面布局模板，其它的页面模板都是根据它扩展来的
    │   │   ├── pagination.swig // 翻页按钮模板
    │   │   └── recent-posts.swig // 文章列表模板
    │   ├── index.swig // 首页模板
    │   ├── page.swig // 页面详情页模板
    │   ├── post.swig // 文章详情页模板
    │   └── tag.swig // 标签文章列表页模板
    └── source
        ├── css
        │   └── theme.styl // 主题自定义 CSS 文件
        ├── favicon.ico
        └── js
            └── theme.js // 主题 JavaScript 文件
    在Hexo的主配置文件中使用新主题，到博客根目录下找到 _config.yml 文件，找到theme行，修改如下：

theme: test

hexo s 启动博客，到浏览器看效果。

FAQ
====

Hexo网站名中文乱码
------------------

因为站点配置文件没有使用utf-8编码造成的，所以在站点配置文件_config.yml中写中文网站名，然后把站点配置文件保存为utf-8格式。

::

  title: 岁月留痕
  subtitle: kevinluo's BLOG

怎么列出hexo依赖插件的完整性？
--------------------------------

::

  npm ls --depth 0

klBlog:

::

   hexo-site@0.0.0 H:\tmp_H\001.work\004.env\01prjsp\hexo\klBlog
   +-- eslint@6.3.0
   +-- hexo@3.9.0
   +-- hexo-deployer-git@1.0.0
   +-- hexo-filter-flowchart@1.0.4
   +-- hexo-generator-archive@0.1.5
   +-- hexo-generator-category@0.1.3
   +-- hexo-generator-feed@2.0.0
   +-- hexo-generator-index@0.2.1
   +-- hexo-generator-tag@0.2.0
   +-- hexo-renderer-ejs@0.3.1
   +-- hexo-renderer-jade@0.4.1
   +-- hexo-renderer-marked@2.0.0
   +-- hexo-renderer-pug@0.0.5
   +-- hexo-renderer-sass@0.4.0
   +-- hexo-renderer-stylus@0.3.3
   +-- hexo-server@0.3.3
   +-- hexo-wordcount@6.0.1

路径名和分类名分别设置，需要怎么办呢？
-----------------------------------------

设置分类名可以在文章中设置 frontmatter-categories_:

打开根目录下的配置文件_config.yml，找到如下位置做更改：

::

   # Category & Tag
   default_category: uncategorized
   category_map:
       编程: programming
       生活: life
       其他: other
   tag_map:

在这里category_map:是设置分类的地方，每行一个分类，冒号前面是分类名称，后面是访问路径。

可以提前在这里设置好一些分类，当编辑的文章填写了对应的分类名时，就会自动的按照对应的路径来访问。


package.json是什么？
------------------------


`package.json是什么？ <http://www.fly63.com/article/detial/1070>`__


`关于项目中package.json的理解 <https://blog.csdn.net/weixin_44051815/article/details/88114480>`__


fontawesome是什么？
------------------------



`github Font-Awesome lib <https://github.com/FortAwesome/Font-Awesome>`__

`一套绝佳的图标字体库和CSS框架 <http://fontawesome.dashgame.com/>`__


怎么添加点击红心和汉字？
----------------------------

1. js文件
   
   ::

       \themes\next\source\js\
       hanzi.js 
       clicklove.js


2. 页面文件
   
   ::

      {%- if theme.kl_click_hanzi %}
            <script src="//lib.baomitu.com/jquery/3.4.0/jquery.min.js"></script>
            <!-- 页面点击汉字 -->
            <script type="text/javascript" src="/js/hanzi.js"></script>
      {%- endif %}

      {%- if theme.kl_click_love %}
            <!-- 页面点击小红心 -->
            <script type="text/javascript" src="/js/clicklove.js"></script>
      {%- endif %}

      </body>

   next 中应该用root相对路径，当root在子目录中，这样JS也可以引用到, ``\klBlog\themes\next\layout\_layout.swig``

   ::

      {%- if theme.kl_click_hanzi %}
            <script src="//lib.baomitu.com/jquery/3.4.0/    jquery.min.js"></script>
            <!-- 页面点击汉字 -->
            {{- next_js('hanzi.js') }}
      {%- endif %}
    
      {%- if theme.kl_click_love %}
            <!-- 页面点击小红心 -->
            {{- next_js('clicklove.js') }}
      {%- endif %}


国内Jquery CDN 有哪些？
---------------------------

1. 新浪CDN（推荐）

   一直好使

   ::

      <script src="http://lib.sinaapp.com/js/jquery/2.0.2/jquery-2.0.2.min.js">
      </script>

2. Baidu CDN
   有时候不好使

   ::

      <script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js">
      </script>

3. 微软CDN:

   ::

      <script src="http://ajax.htmlnetcdn.com/ajax/jQuery/jquery-1.10.2.min.js">
      </script>


怎么解决githubpages不能识别下划线开头的目录？
--------------------------------------------------------

`githubpages不能识别下划线开头的目录解决方法 <https://blog.csdn.net/lineuman/article/details/89600484>`__

使用sphinx创建的文档，资源文件夹前面会带着下划线，本地使用没有问题，提交到github上面，想使用github pages的时候提示404，原因为github pages的jekyll模版会忽略下划线开头的文件，自动忽略下划线开头的目录，从而导致引用不到CSS,JAVASCRIPT,ETC.，所以要禁用jekyll

禁用方法就是在文件在项目目录下添加.nojekyll文件


CDN

`CDN前端静态资源库baomitu-used in maupassant-hexo <https://cdn.baomitu.com/>`__

`75CDN奇舞团 <https://75team.com/cate/75cdn>`__

hexo deploy 网站部署
====================

参见 Hexo博客从搭建部署到SEO优化等详细教程_


hexo d 法
---------

`hexo.io/docs/deployment <https://hexo.io/docs/deployment.html>`__

安装扩展：

::

  $ npm install hexo-deployer-git --save

需要在配置文件_config.xml中作如下修改：

::

   deploy:
     type: git
     repo: git@github.com:jiji262/jiji262.github.io.git
     branch: master
   然后在命令行中执行
   
   hexo d

密码输入形式

::

   deploy:
     type: git
     repo: https://kevinluolog:xxxxxx[密码]@github.com/kevinluolog/   kevinluolog.github.io.git
     branch: master
   
   #  repo: git@github.com:kevinluolog/kevinluolog.github.io.git
   
   #例如你的账号为:crown3,密码为 BBB;
   #那你的repo填写为下面这样即可
   #github: https://crown3:BBB@github.com/crown3/crown3.github.io.git
   #coding: https://crown3:BBB@git.coding.net/crown3/仓库名.git


直接git clone 法
---------------------

CI 法，
-------------

`hexo_klblog <git@github.com:kevinluolog/hexo_klblog.git>`__


这个网址里面提到了常用的持续集成CI工具:

`好代码是管出来的——使用GitHub实现简单的CI/CD <https://www.cnblogs.com/selimsong/p/9398738.html>`__

`Hexo遇上Travis-CI：可能是最通俗易懂的自动发布博客图文教程 <https://blog.csdn.net/Xiong_IT/article/details/78675874>`__

`GitHub的CI/CD与Travis配置小记 <https://yq.aliyun.com/articles/675660>`__

十大CI工具:
^^^^^^^^^^^

::

   Travis CI
   Circle CI
   Jenkins
   AppVeyor
   CodeShip
   Drone
   Semaphore CI
   Buildkite
   Wercker
   TeamCity


travis CI：
^^^^^^^^^^^^^^^

Travis可以执行多种语言的测试及构建， `官方文档 <https://docs.travis-ci.com/user/languages/>`__

`Build Lifecycle documentation <https://docs.travis-ci.com/user/job-lifecycle>`__


travis CI 配置步骤:
"""""""""""""""""""

那既然需要使用travis自动化更新你的博客，travis自然需要读写你的github上的repo。github提供了token机制来供外部访问你的仓库。

https://github.com/settings/tokens

1. 安装 travis, 并授权管理repo
   
   marketplace搜索travis,并安装。

   github/{user name}/personal settings/application/ travis CI configure
   选择要travis管理的repo.

2. 配置github token
   
   分三步，

   ::

      step 1: 在github中生成token，
              github/{user name}/-> setting->Developer settings-> Personal access tokens -> generate new token
      step 2: 再在travis网页项目中配置环境变量$GH_TOKEN，填入token
      step 3: 在blog root _config.yml deploy 中，设置gh_token访问标记
      step 4: 在.travis.yml中，在编译完后，deploy之前用sed替换，step 3 中在 _confi.yml 中的gh_token访问标记，用真正的保存在环境变量中的token替换掉。这样做的目的只是为了保密。一般repo是public的，就会泄漏token.

3. 配置travis

   在travis进入仓库同步管理, `here <https://travis-ci.com/kevinluolog/hexo-klblog-src/settings>`__
   
   主要是前面的gh-token环境变量.

4. 在源码仓库根目录增加.travis.yml 修改 _config.yml
   
   - 增加 .travis.yml
     
     注意，如果源码是在分支上要修改branches为相应的分支名，缺省是master:

     ::

        ### for branch of hexo-next-muse
        
        # 指定语言环境
        language: node_js
        # 指定需要sudo权限
        sudo: required
        # 指定node_js版本
        node_js: 
          - 10.16.3
        # 指定缓存模块，可选。缓存可加快编译速度。
        cache:
          directories:
            - node_modules
        
        # 指定博客源码分支，因人而异。hexo博客源码托管在独立repo则不用设置此项
        branches:
          only:
            - hexo-next-muse 
        
        before_install:
          - npm install -g hexo-cli
        
        # Start: Build Lifecycle
        install:
          - npm install
          - npm install hexo-deployer-git --save
        
        # 执行清缓存，生成网页操作
        script:
          - hexo clean
          - hexo generate
        
        # 设置git提交名，邮箱；替换真实token到_config.yml文件，最后depoy部署
        after_script:
          - git config user.name "kevinluolog"
          - git config user.email "kevinluolog_72@163.com"
          # 替换同目录下的_config.yml文件中gh_token字符串为travis后台刚才配置的变量，注意此处sed命令用了双引号。单引号无效！
          - sed -i "s/gh_token/${GH_TOKEN}/g" ./_config.yml
          - hexo deploy
        # End: Build LifeCycle



   - 修改 _config.yml
     
     1. 主要是修改deploy部分，决定gh-token和推送部署到什么repo的什么分支。
     如果是xxxx.github.io就推到master, 如果是子目录repo,则推送到gh-pages分支。
     
     2. 设置 root变量， 如果是子目录repo，则需要设置相应的子目录repo名字。这样在网页引用css等资源时可以直接引用到。因为hexo引用CSS等资源时用的是绝对目录，如/{子目录repo名}/css/xxx.css, sphinx 用的是相对目录，如 _static/css/xxx.css。 此处因为sphinx资源目录前面带了下划线， _ , 因hexo和jekyll会自动忽略下划线开头的目录，从而导致引用不到CSS,JAVASCRIPT,ETC.，所以在根目录要添加.nojekyll文件, 详细请参考 `怎么解决githubpages不能识别下划线开头的目录？`_

        
     ::

        root: /hexo-next-muse/
        # Deployment
        deploy:
          type: git
          repo: https://gh_token@github.com/kevinluolog/hexo-next-muse.git  
          branch: gh-pages                                                      


travis CI 配置实例
^^^^^^^^^^^^^^^^^^

网站规划结构参见 `my deploy: kevinluolog.github.io`_

简单讲就是，kevinluolog/hexo-klblog-src repo作为源码仓库，master分支对应主网站repo的master分支，其余分支各对应主网站的子目录网站repo的gp-pages分支。源码repo分支名称和子目录网站的仓库名要取得一样，以方便对应。每次源码有推送时，触发对应分支的travis CI启动，源码拉取->环境搭建->编译->部署，部署时是部署到对应的网站repo的gp-pages分支上的。

最终的效果是，写或修改文章时只和source目录中的_post目录相关 ``\hexo\klBlog\source\_posts`` 改动完成提交到对应的分支后， 过2分钟左右， 对应的网站即要自动更新。非常方便和快捷，不用占用本人的时间也不用占用本机的CPU去编译和部署。同时可以的任何可以上网的地方写文章，提交。 和写程序一模一样，一个github搞定一切。

创建源码新分支需要改动的文件
""""""""""""""""""""""""""""

1. 文件.travis.yml
   
   启动分支名。
   
   ::

      # 指定博客源码分支，因人而异。hexo博客源码托管在独立repo则不用设置此项
      branches:
        only:
          - hexo-next-xxx

2. 文件_config.yml
   
   - theme
     
     ::

        theme: next


   - root, 子网站根目录，要和网站repo名字相同
     
     ::

        root: /hexo-next-xxx/
     
   - deloy, 推送目标仓库名

     ::
  
        deploy:
          type: git
          repo: https://gh_token@github.com/kevinluolog/hexo-next-xxx.git
          branch: gh-pages

3. 其它博客定制相关文件
   
   如theme下配置文件_config.yml，next和melody支持独立配置文件在_data/next.yml 和 melody.yml

   i. _data/next.yml
   
      - 风格
        
        ::
  
           # Schemes
           #scheme: Muse
           #scheme: Mist ##kl+  
           #scheme: Pisces
           scheme: Gemini




需求：在github pages子目录建立hexo博客
-------------------------------------------

`在githubpages子目录建立hexo博客 <https://www.jianshu.com/p/986b975a29ae>`__


实现：

1. 首先建立xxx.github.io的repo，xxx是你的用户名，之后开启github pages服务
2. 再建立一个bbbb的repo，bbbb是你想要的子目录
3. 设置hexo的deploy配置文件 _config.yml

::

   - type: git
     repo: https://github.com/xxx/bbbb.git
     branch: gh-pages

4. 修改_config.yml中的root选项，由"/"改为"/bbbb"

github page就大概两种，一种user page必须master分支，另一种project page需要给对应的project设置一个gh-pages分支，上传好网页资源文件之后，就可以在username.github.io/projectname这样的域名访问了。

网上挺多教程都不太对，自己解决了之后记录一下。


my deploy: kevinluolog.github.io
--------------------------------

Repo of sites:
^^^^^^^^^^^^^^

1. kevinluolog.github.io: branch:master
   
   generated by travis Ci from repo of hexo source - branch of master

#. hexo-XXX: branch:gh-pages
   
   can be accessed by ``kevinluolog.github.io/hexo-xxx``
   
   generated by travis Ci from repo of hexo source - branch of hexo-XXX

#. gp: branch:gh-pages

   can be accessed by ``kevinluolog.github.io/gp/xxx``

   generated by sphinx etc. directly


Repo of hexo source: private
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Travis can access with private repo.

- branch: master

  hexo source, and deploy to kevinluolog.github.io - master automatically

- branch: hexo-xxx
  

  deploy to REPO：hexo-xxx - gh-pages, automatically.

  branch _config.yml for set differrent theme

  travis-ci triggered by source file merged in. then compile and deploy.

  books, created by sphinx or docutils or pandoc.

