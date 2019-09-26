# 检测是什么操作系统
ifeq ($(OS),Windows_NT)
uname_S := Windows
else
uname_S := $(shell uname -s)
endif

# windows
ifeq ($(uname_S), Windows)
DIR_BASE_SRC := .
#	system("dir /b /s $DIR_BASE_SRC\*.* >d:\\allfiles.txt")
endif
# linux
ifeq ($(uname_S), Linux)
DIR_BASE_SRC := .
endif
#ifeq ($(uname_S), .....) #See https://stackoverflow.com/a/27776822/938111
#	target = .....
#endif

###---输入变量

# 基目录
DIR_BASE_SRC := H:\tmp_H\001.work\002git\kdoc\003work\002memo
#DIR_BASE_SRC := H:\tmp_H\001.work\002git\kdoc\003work\002memo\001software\001install
DIR_BASE_OBJ := H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\tmp
DIR_BASE_COPYTO := H:\tmp_H\001.work\004.env\01prjsp\hexo\klBlog\source\_posts\kl_notes\002memo

###---生成变量

# 获得源.rst路径名。
# 利用dos命令dir获取当前目录及子目录下所有.rst路径文件名
SRC_PATH_RSTS := $(shell dir $(DIR_BASE_SRC)\*.rst /b /w /s)

# 利用dos命令dir获取当前目录及子目录下的所有子目录名
SRC_PATH_DIR := $(shell dir $(DIR_BASE_SRC)\ /aD /s /b)


# .rst路径文件名替换成.md路径文件名
SRC_PATH_MDS := $(patsubst %.rst,%.md,$(SRC_PATH_RSTS))
# 这是模式替换类似patsubst,和上面等价
#SRC_PATH_MDS := $(SRC_PATH_RSTS:.rst=.md)

# 获得目标.md路径文件名。
# 替换成目标基路径名，即保留源基路径下的路径，添加到目标基路径下面
OBJ_PATH_MDS := $(subst $(DIR_BASE_SRC),$(DIR_BASE_OBJ),$(SRC_PATH_MDS))

# 获得目标路径目录名
OBJ_PATH_DIR := $(subst $(DIR_BASE_SRC),$(DIR_BASE_OBJ),$(SRC_PATH_DIR))

OBJ_REL_PATH_MDS := $(subst $(DIR_BASE_SRC)\,,$(SRC_PATH_MDS))


###---生成目标
define def_dash :=
---
endef

define def_title :=
title:
endef

define def_toc :=
toc:
endef

define def_tag :=
tag:
endef

define def_categories :=
categories:
endef

define def_hexo_md_head
$(def_dash)
$(def_title) $(1)
$(def_toc) TRUE
$(def_tag)
- 自动生成
- 技术
- 笔记
$(def_categories)
- 技术
- 笔记
$(def_dash)

endef

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
#	@echo $$(TBFILENAME)+2
#	@echo $(subst .md,,$(notdir $(1)))+1#直接函数填入才能取到。
	@echo convert to utf8
	iconv -f GBK -t UTF-8 $$@.tmp >$$@
	@echo start pandoc ...
	pandoc $$< -o - >>$$@
	@echo delete .tmp file...
	del $$@.tmp
	@echo copy .md file to hexo post...
	xcopy $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) /y
endef

# 打散目标集合,一个一个送入命令集重组,同时用eval命令在makefile中使能。这样可以克服模式匹配依赖要一致的缺点(%只能匹配文件名,并且要规则一样)
$(foreach temp,$(OBJ_PATH_MDS),$(eval $(call PROGRAM_template,$(temp))))

###---伪目标

.phony: md
# OBJ_PATH_DIR保证目录存在，OBJ_PATH_MDS转换文件
rst2md: $(OBJ_PATH_DIR) $(OBJ_PATH_MDS)
#	@echo rst2md转换 $(DIR_BASE_SRC) 到 $(DIR_BASE_OBJ)
	@echo is updated. rst2md finished!!!
	
#	@move xxx xxx ## MOVE [/Y | /-Y] [drive:][path]filename1[,...] destination

#rst2pdf: $(OBJ_PATH_PDF)

# rst2pdf
#$(OBJ_PATH_PDF): %.pdf: %.md
# pandoc --template=./template.tex --latex-engine=xelatex  $< -o $@ 
#	mv *.pdf git/

###---help

