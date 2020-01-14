########
make
########

*****************
make and makefile
*****************

.. contents:: 目录
.. section-numbering::

make
====

gnu make 安装
-------------
- make 官方下载地址
  
  GNU ftp server: http://ftp.gnu.org/gnu/make/ (via HTTP) and ftp://ftp.gnu.org/gnu/make/ (via FTP)

- make4.2（GNU make）的安装步骤

  1. 解压

     ``tar -zxvf make4.2.tar.gz``



  2. 安装
     
     window: 要用到gcc of MinGW,或者visual studio.

     ::
       
       E:\E-ProgramFiles\portable\codeblocks-mingw\MinGW\mingwvars.bat
       cd make4.2
       build_w32.bat gcc
     
     在 ``\make-4.2\GccRel`` 下生成gnumake.exe 

     Linux

     ::

       cd make4.2
       ./configure
       make && make install

  3. 打开新的窗口，验证

     ``make -v`` 或 ``gnumake -v``

help
----

GNU官方
^^^^^^^

`gnu make manual <http://www.gnu.org/software/make/manual/>`__

`gnu make Wildcard-Function <http://www.gnu.org/software/make/manual/html_node/Wildcard-Function.html#Wildcard-Function>`__

`gnu make index <http://www.gnu.org/software/make/manual/html_node/Concept-Index.html#Concept-Index_cp_letter-W>`__

gnu其它
^^^^^^^

这篇文章写得短小全面。 外链-> 
`gcc与makefile <https://blog.csdn.net/qq_30650153/article/details/83384248>`__


make misc
---------



cmake
=====

cmake install
-------------

`cmake download <https://cmake.org/download/>`__


cmake help
----------

`cmake documments <https://cmake.org/documentation/>`__

`cmake tutorial <https://cmake.org/cmake-tutorial/>`__

`cmake help v3.15 <https://cmake.org/cmake/help/v3.15/>`__


FAQ
======


Makefile变量$@，$^，$<代表的意义
---------------------------------

`makefile中$@ $^ %\<使用 <https://www.cnblogs.com/baiduboy/p/6849587.html>`__

$@目标文件，$^所有的依赖文件，$<第一个依赖文件。

这是再一次简化后的Makefile

::

  main：main.o mytool1.o mytool2.o
  gcc -o $@ $^
  .c.o：
  gcc -c $<

怎么查到函数是哪个库的？
---------------------------

有时候我们使用了某个函数，但是我们不知道库的名字，这个时候怎么办呢?

比如我要找sin这个函数所在的库。 就只好用命令

::

  nm -o /lib/\*.so|grep sin>~/sin

然后看~/sin文件，会找到这样的一行

::

  libm-2.1.2.so：00009fa0 W sin 

这样我就知道了sin在 libm-2.1.2.so库里面，
-lm选项就可以了(去掉前面的lib和后面的版本标志，就剩下m了所以是 -lm)。

::

  gcc -o temp temp.c -lm

只知道函数的大概形式，怎么找到头文件。用man
---------------------------------------------

想知道fread这个函数的确切形式，我们只要执行 man fread 系统就会输出着函数的详细解释的。和这个函数所在的头文件说明了。 

如果我们要write这个函数的说明，当我们执行 `man write` 时，输出的结果却不是我们所需要的。 因为我们要的是write这个函数的说明，可是出来的却是write这个命令的说明。
为了得到write的函数说明我们要用 `man 2 write` 2表示我们用的write这个函数是系统调用函数，还有一个我们常用的是3表示函数是C的库函数。


引用文章全文
================

gcc与makefile
-------------

| 本文不会详细展开如何编写一个Makefile。如想了解种种细节，请参考下面这个非常详细的教程，包含几乎GNU
  make的Makefile的所有细节：

`跟我一起写Makefile <https://seisman.github.io/how-to-write-makefile/>`__

而本文包含以下内容：

-  makefile小模板
-  gcc指令

Makefile小模板

适用于纯 Ｃ 语言

::

   # 指令编译器和选项
   CC=gcc
   CFLAGS=-Wall -std=gnu99
    
   # 目标文件
   TARGET=main
   SRCS = main1.c \
               main2.c  \
               main3.c  
   INC = -I./
   OBJS = $(SRCS:.c=.o)

   $(TARGET):$(OBJS)
       $(CC) -o $@ $^
    
   clean:
       rm -rf $(TARGET) $(OBJS)
    
   %.o:%.c
       $(CC) $(CFLAGS) $(INC) -o $@ -c $<

| 注意：Makefile有个规则就是命令行是以tab键开头，4个空格或其他则会报错：
| ``Makefile:2: *** missing separator。stop``

-  相比于单个文件和多个文件的makefile，通过变量\ ``INC``\ 制定了头文件路径。头文件路径之间通过空格隔开。
-  编译规则\ ``%.o:%.c``\ 中加入了头文件参数\ ``$(CC) $(CFLAGS) $(INC) -o $@ -c $<``\ ，
-  单个文件和多个文件的makefile相比增加了头文件路径参数。
-  ``SRCS``\ 变量中，文件较多时可通过\ ``“\”``\ 符号续行。
-  ``$@`` --代表目标文件
-  ``$^`` --代表所有的依赖文件
-  ``$<`` --代表第一个依赖文件(最左边的那个)。

适用于 C/C++ 混合编译

目录结构如下：

::

   httpserver
   │   main.cpp
   │   Makefile  
   └─────inc
   │      │   mongoose.h
   │      │   http_server.h
   │   
   ──────src
   │       │   http_server.cpp
   │       │   mongoose.c
   │       │   ...

Makefile 如下：

::

   CC=gcc
   CXX=g++

   # 编译器在编译时的参数设置,包含头文件路径设置
   CFLAGS:=-Wall -O2 -g 
   CFLAGS+=-I $(shell pwd)/inc
   CXXFLAGS:=-Wall -O2 -g -std=c++11
   CXXFLAGS+=-I $(shell pwd)/inc

   # 库文件添加
   LDFLAGS:=
   LDFLAGS+=

   # 指定源程序存放位置
   SRCDIRS:=.
   SRCDIRS+=src

   # 设置程序中使用文件类型
   SRCEXTS:=.c .cpp

   # 设置运行程序名
   PROGRAM:=httpserver

   SOURCES=$(foreach d,$(SRCDIRS),$(wildcard $(addprefix $(d)/*,$(SRCEXTS))))
   OBJS=$(foreach x,$(SRCEXTS),$(patsubst %$(x),%.o,$(filter %$(x),$(SOURCES))))

   .PHONY: all clean distclean install

   %.o: %.c
       $(CC) -c $(CFLAGS) -o $@ $<
       
   %.o: %.cxx
       $(CXX) -c $(CXXFLAGS) -o $@ $<


   $(PROGRAM): $(OBJS)
   ifeq ($(strip $(SRCEXTS)),.c)
       $(CC) -o $(PROGRAM) $(OBJS) $(LDFLAGS)
   else
       $(CXX) -o $(PROGRAM) $(OBJS) $(LDFLAGS)
   endif


   install:
       install -m 755 -D -p $(PROGRAM) ./bin

   clean:
       rm -f $(shell find -name "*.o")
       rm -f $(PROGRAM)

   distclean:
       rm -f $(shell find -name "*.o")
       rm -f $(shell find -name "*.d")
       rm -f $(PROGRAM)

   all:
       @echo $(OBJS)

.. rubric:: gcc指令
   :name: gcc指令

.. rubric:: 一步到位
   :name: 一步到位

``gcc main.c -o main``

.. rubric:: 多个程序文件的编译
   :name: 多个程序文件的编译

``gcc main1.c main2.c -o main``

.. rubric:: 预处理
   :name: 预处理

| ``gcc -E main.c -o main.i``
| 或
| ``gcc -E main.c``
| gcc的-E选项，可以让编译器在预处理后停止，并输出预处理结果。

.. rubric:: 编译为汇编代码
   :name: 编译为汇编代码

| 预处理之后，可直接对生成的test.i文件编译，生成汇编代码:
| ``gcc -S main.i -o main.s``
| gcc的-S选项，表示在程序编译期间，在生成汇编代码后，停止，-o输出汇编代码文件。

.. rubric:: 汇编
   :name: 汇编

| 对于上文中生成的汇编代码文件test.s，gas汇编器负责将其编译为目标文件，如下:
| ``gcc -c main.s -o main.o``

.. rubric:: 连接
   :name: 连接

| gcc连接器是gas提供的，负责将程序的目标文件与所需的所有附加的目标文件连接起来，最终生成可执行文件。附加的目标文件包括静态连接库和动态连接库。
| 对于上一小节中生成的main.o，将其与Ｃ标准输入输出库进行连接，最终生成可执行程序main。

.. rubric:: 检错
   :name: 检错

| 参数\ ``-Wall``\ ，使用它能够使GCC产生尽可能多的警告信息。
| ``gcc -Wall main.c -o main``
| 在编译程序时带上\ ``-Werror``\ 选项，那么GCC会在所有产生警告的地方停止编译，迫使程序员对自己的代码进行修改，如下：
| ``gcc -Werrormain.c -o main``

.. rubric:: 创建动态链接库
   :name: 创建动态链接库

| 生成生成o文件
| ``gcc -c -fPIC add.c``
  //这里一定要加上-fPIC选项，目的使库不必关心文件内函数位置
| 再编译
| ``gcc -shared -fPIC -o libadd.so add.o``

.. rubric:: 库文件连接
   :name: 库文件连接

| 开发软件时，完全不使用第三方函数库的情况是比较少见的，通常来讲都需要借助许多函数库的支持才能够完成相应的功能。从程序员的角度看，函数库实际上就是一些头文件（\ ``.h``\ ）和库文件（\ ``so、或lib、dll``\ ）的集合。虽然\ ``Linux``\ 下的大多数函数都默认将头文件放到\ ``/usr/include/``\ 目录下，而库文件则放到\ ``/usr/lib/``\ 目录下；但也有的时候，我们要用的库不在这些目录下，所以GCC在编译时必须用自己的办法来查找所需要的头文件和库文件。
| 额外补充：Linux需要连接so库文件（带软连接），可以完完整整的复制到\ ``/usr/include/``\ 或\ ``/usr/lib/``\ 目录下，使用
  ``cp -d * /usr/lib/`` 命令，然后别忘记再运行
  ``ldconfig``\ 。

| 其中inclulde文件夹的路径是\ ``/home/test/include``,lib文件夹是\ ``/home/test/lib``,lib文件夹中里面包含二进制so文件\ ``libtest.so``
| 首先要进行编译main.c为目标文件，这个时候需要执行:
| ``gcc –c –I /home/test/include main.c –o main.o``
| 最后把所有目标文件链接成可执行文件:
| ``gcc –L /home/test/lib -ltest main.o –o main``

| 默认情况下，
  GCC在链接时优先使用动态链接库，只有当动态链接库不存在时才考虑使用静态链接库，如果需要的话可以在编译时加上-static选项，强制使用静态链接库。
| ``gcc –L /home/test/lib -static -ltest main.o –o main``

静态库链接时搜索路径顺序：

#. ``ld``\ 会去找GCC命令中的参数-L
#. 再找gcc的环境变量\ ``LIBRARY_PATH``
#. 再找内定目录 ``/lib``\ 、 ``/usr/lib``\ 、
   ``/usr/local/lib`` 这是当初compile gcc时写在程序内的

动态链接时、执行时搜索路径顺序:

#. 编译目标代码时指定的动态库搜索路径
#. 环境变量\ ``LD_LIBRARY_PATH``\ 指定的动态库搜索路径
#. 配置文件\ ``/etc/ld.so.conf``\ 中指定的动态库搜索路径
#. 默认的动态库搜索路径\ ``/lib``
#. 默认的动态库搜索路径\ ``/usr/lib``

| 相关环境变量：
| ``LIBRARY_PATH``\ 环境变量：指定程序静态链接库文件搜索路径
| ``LD_LIBRARY_PATH``\ 环境变量：指定程序动态链接库文件搜索路径


实践中的一些经验
===================

eval 和 define 中变量展开的坑
-----------------------------

先上参考代码，下面代码中的错误，让我一阵好找，费几天时间。
出现莫名其妙的错误，DIR_STEM 缺尾部的\, TBFILENAME引用不到，文件名中间被插入空格等等。原因都是行尾的\引起。

::

   define PROGRAM_template
   #把文件分成4部分,基-干(DIR_STEM)-文件名.后缀名
   DIR_STEM := $(subst $(DIR_BASE_OBJ),,$(dir $(1)))#XXX:这句语句执行完后展开后，行尾有\,会被视为连上下一行，导致下一行变量成内容了。后面就找不到这个变量了。所以用DIR_STEM := $(subst $(DIR_BASE_OBJ),,$(basename $(1)))代替，就不会有\了
   TBFILENAME := $(subst .md,,$(notdir $(1)))#XXX:此处因上面问题会连到上行
   $(info $(TBFILENAME))#XXX:此处会显示不出东西来
   #$(1): $(DIR_BASE_SRC)$$(DIR_STEM)\$$(TBFILENAME).rst
   #$(1): $(DIR_BASE_SRC)$(subst $(DIR_BASE_OBJ),,$(dir $(1)))\$(subst .md,,$(notdir $(1))).rst
   #$(1): $(DIR_BASE_SRC)$$(DIR_STEM)$$(TBFILENAME).rst
   #dep := $(DIR_BASE_SRC)$$(DIR_STEM)\$$(TBFILENAME).rst
   #dep := $(patsubst %.md,%.rst,$(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1)))
   dep := $(patsubst %.md,%.rst,$(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1)))
   ##不能直接写在[目标:依赖]里面,因为依赖里面带着模式匹配,有可能会使文件名乱套,未做实验再次证实，如果有问题，可以参考。最后发现没关系的。
   #$(1): $(patsubst %.md,%.rst,$(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1)))
   $(1): $$(dep)
   ##必须要写成$$(dep),$(dep)会使pandoc第一个参数为空。大概是因为命令集内部定义或组合生成的新变量要加双$
    $(info $(1): $(dep))
    pandoc $$< -o $$@
    $$(file >$(DIR_BASE_OBJ)-$$(DIR_STEM)-$$(TBFILENAME).tmp,$$(call def_hexo_md_head,$$TBFILENAME))
   ## 上面命令pandoc此处必须加$$,要不$<,$@会找不到,会出现pandoc -o 这样没有任何的参数带入的错误。花了我几天时间查了无数资料，做无数次的试验，才找到这个问题
   endef
   ## 写入文件的函数 $(file >xxx.xx,$(xxx)),这里要用$$(file， $$(call ，如果没有则在eval 的第一次展开时，函数就会被执行，所以会每次执行make都会写文件，而不是设计的源文件有更新时才编译更新文件。
   
   # 打散目标集合,一个一个送入命令集重组,同时用eval命令在makefile中使能。这样可以克服模式匹配依赖要一致的缺点(%只能匹配文件名,并且要规则一样)
   $(foreach temp,$(OBJ_PATH_MDS),$(eval $(call PROGRAM_template,$(temp))))

改好好用的代码

::

   $(OBJ_PATH_DIR):
   #因为mkdir支持多目录同时写在一起,所以不用再用模式来拆开成一个一个了。
    @echo "   MKDIR $@..." 
    @mkdir $@ 
   
   ##定义一个命令包, 来重新组合【目标:依赖】关系, 配合$(eval ) 和foreach 来使用。eval用来二次展开命令包，使用真正成为makefile的一部分，命令包只是一堆makefile标识文本。foreach用来展开目标集的每一个目标，并送入命令包进行替换重组。
   ##此处要注意的是，二次展开才用到的变量或函数要用$$,譬如自动变量$@等。
   ##define a function
   #$(info $(TBFILENAME))
   
   define PROGRAM_template
   DIR_STEM := $(subst $(DIR_BASE_OBJ),,$(basename $(1)))
   #TBFILENAME := $(subst .md,,$(notdir $(1)))
   #$(1): $(DIR_BASE_SRC)$$(DIR_STEM).rst
   #dep := $(patsubst %.md,%.rst,$(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1)))
   dep := $(basename $(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1))).rst
   $(1): $$(dep)
    @echo start hexo head output...
    $$(file >$$@.tmp,$$(call def_hexo_md_head,$(subst .md,,$(notdir $(1)))))
   #  @echo $$(TBFILENAME)+2
   #  @echo $(subst .md,,$(notdir $(1)))+1#直接函数填入才能取到。
    @echo convert to utf8
    iconv -f GBK -t UTF-8 $$@.tmp >$$@
    @echo start pandoc ...
    pandoc $$< -o - >>$$@
    @echo delete .tmp file...
    del $$@.tmp
    @echo copy .md file to hexo post...
    xcopy $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_HEXO_POST),$(1))) /y
   endef
   
   # 打散目标集合,一个一个送入命令集重组,同时用eval命令在makefile中使能。这样可以克服模式匹配依赖要一致的缺点(%只能匹配文件名,并且要规则一样)
   $(foreach temp,$(OBJ_PATH_MDS),$(eval $(call PROGRAM_template,$(temp))))

- 行尾有\,后一行的变量名被连上来了
  
  ::
  
    define function
    DIR_STEM := $(dir $(1))#这个不是出现在define中是没有关系的。但此处就有可能有问题
    endef
  
  或者
  
  ::
  
    DIR_STEM := c:\tmp\
  
- eval和define

  define只是一堆文字，在引用的地方展开，但是并不作为makefile的一部分，即展开的变量不会出现在makefile变量空间中，1tab缩进的命令会在展开时执行。
  
  eval则表示会有2次展开，第一次展开和define一样。第二次展开是把展开的内容变为makefile变量等空间的一部分，可以真正引用到。
  
  eval 2次展开才引用到的变量要用$$, 自动变量也一样，新生成变量也一样，define中创建的变量也一样，eval外面已经有的变量不用加双$，案例参考上面代码。
  函数也一样，如果是要在2次展开时，才启动执行的话，就需要加$$延迟defer


输出文件的方法
---------------------

- $(file >$$@.tmp,$$(call def_hexo_md_head,$$(TBFILENAME)))
- > 和 >> 法
  
一些工具
-------------

- iconv 文件编码转换
  
  因pandoc和Hexo都只支持UTF-8的编码形式，而中文版windows缺省输出的是GBK的中文编码，如果直接用>>把pandoc的输出重定向到GBK编码的文件中时，会出现什么也没有输出的现象。这里就需要iconv来做一下转换了。

  ::

     echo start hexo head output...
     $$(file >$$@.tmp,$$(call def_hexo_md_head,$$(TBFILENAME)))
     echo convert to utf8
     iconv -f GBK -t UTF-8 $$@.tmp >$$@
     echo start pandoc ...
     pandoc $$< -o - >>$$@
 

调试输出变量信息方式
---------------------------

- 输出信息方式为：

  ::
  
     $(warning xxx)
     $(error xxx)
     $(info xxx)

- 输出变量方式为：

  ::

     $(info $(dir $(1)))
     $(warning  $(XXX))

echo输出信息时加上""会使变量显示有问题，不对并且会报错
-----------------------------------------------------------------

::
   
   SRC_PATHDIRNAMES := $(shell dir $(DIR_BASE_SRC) /ad-h-s /b /w /s)
   SRC_PATHDIRNAMES_GITKEEPER := $(addsuffix \.gitkeeper,$(SRC_PATHDIRNAMES))
   $(info $(SRC_PATHDIRNAMES_GITKEEPER))
   @echo "$(SRC_PATHDIRNAMES_GITKEEPER)"

这么一段简单的代码，居然执行的时候会死机，或者报错，$info显示完全正确。 原因是echo后面 把“”去掉就好了。

pattern % make 模式匹配的限制
-----------------------------------------------------------------

::

   SRC_PATHDIRNAMES := $(filter-out $(DIR_BASE_SRC)\.git%,$(SRC_PATHDIRNAMES_FILTER_BEFORE))$(info $(SRC_PATHDIRNAMES))

此处的模式匹配，%只能用在中间，不能%.git%这种匹配。 匹配不出来。