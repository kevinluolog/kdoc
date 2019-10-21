###---输入变量

# 基目录
DIR_BASE_SRC := /H/tmp_H/001.work/002git/kdoc/003work/002memo
DIR_BASE_OBJ := /H/tmp_H/001.work/004.env/01prjsp/04make/01rst2md/tmp
#DIR_BASE_COPYTO := 
DIR_BASE_COPYTO :=

# template directory for xelatext to create PDF, 
DIR_TEMPLATE := /H/tmp_H/001.work/002git/kdoc/003work/000tools/002makefiles/001pandoc/templates

# 后缀名，文件类型
SUFFIX_FROM := .rst
SUFFIX_TO := .md

# 控制是否加入hexo需要的frontmatter meta数据,只在rst2md的模式中用到，其它可以任意值
ADD_HEXO_HEAD := TRUE
# 控制输入TAG的模式: =,空表示自动从所在最后一级目录来 =xxx,非空值则直接填入这个值
ADD_HEXO_TAG_FROM_DIR := 技术
###---生成变量

# 获得源$(SUFFIX_FROM)路径名。
# 利用find命令取得目录名
SRC_PATH_DIR := $(shell find $(DIR_BASE_SRC) -type d)

# 取得源文件名,包括路径
#SRC_PATH_RSTS := $(foreach dir,$(SRC_PATH_DIR),$(addprefix $(dir)/,$(wildcard $(dir)/*.rst)))
# $(wildcard $(dir)/*.rst) 的返回，已经包含了目录，所以不用再addprefix加上目录名，要不重复了。
SRC_PATH_RSTS := $(foreach dir,$(SRC_PATH_DIR),$(wildcard $(dir)/*.rst))


# $(SUFFIX_FROM)路径文件名替换成$(SUFFIX_TO)路径文件名
SRC_PATH_MDS := $(patsubst %$(SUFFIX_FROM),%$(SUFFIX_TO),$(SRC_PATH_RSTS))
# 这是模式替换类似patsubst,和上面等价
#SRC_PATH_MDS := $(SRC_PATH_RSTS:$(SUFFIX_FROM)=$(SUFFIX_TO))

# 获得目标$(SUFFIX_TO)路径文件名。
# 替换成目标基路径名，即保留源基路径下的路径，添加到目标基路径下面
OBJ_PATH_MDS := $(subst $(DIR_BASE_SRC),$(DIR_BASE_OBJ),$(SRC_PATH_MDS))

# 获得目标路径目录名
OBJ_PATH_DIR := $(subst $(DIR_BASE_SRC),$(DIR_BASE_OBJ),$(SRC_PATH_DIR))

OBJ_REL_PATH_MDS := $(subst $(DIR_BASE_SRC)/,,$(SRC_PATH_MDS))


###---生成目标

#【参数1:title =没有后缀的光文件名 】
#【参数2:tag =技术...(ifdef ADD_HEXO_TAG_FROM_DIR) =最后目录名(ifudef ADD_HEXO_TAG_FROM_DIR)】 
#【参数3:categories =最后目录名】
define def_hexo_md_head
---
title: $(1)
tag: 
- $(2)
- 笔记
categories:
- $(3)
- 自动生成
toc: TRUE
---
endef

$(OBJ_PATH_DIR):
#因为mkdir支持多目录同时写在一起,所以不用再用模式来拆开成一个一个了。
	@echo "   MKDIR $@  ..." 
	@mkdir -p $@
#	@echo "SRC_PATH_DIR %%%"
#	@echo $(SRC_PATH_DIR)
#	@echo "OBJ_PATH_MDS %%%"
#	@echo $(OBJ_PATH_MDS)
#	@echo "SRC_PATH_MDS %%%"
#	@echo $(SRC_PATH_MDS)


##定义一个命令包, 来重新组合【目标:依赖】关系, 配合$(eval ) 和foreach 来使用。eval用来二次展开命令包，使用真正成为makefile的一部分，命令包只是一堆makefile标识文本。foreach用来展开目标集的每一个目标，并送入命令包进行替换重组。
##此处要注意的是，二次展开才用到的变量或函数要用$$,譬如自动变量$@等。
##define a function
#$(info $(TBFILENAME))

define PROGRAM_template
#下面两行在引用DIR_STEM时会取到foreach中的最后一个变量值，不理解为何。据现在的理解eval双$二次展开后，用:=赋值的应该是每次循环的值。留待以后解决吧。现在先直接赋值绕过去。
#DIR_WORDS := $(subst /, ,$(dir $(1)))
#DIR_LAST := $(word $(words $$(DIR_WORDS)),$$(DIR_WORDS))
#DIR_STEM := $(subst $(DIR_BASE_OBJ),,$(basename $(1)))
#TBFILENAME := $(subst $(SUFFIX_TO),,$(notdir $(1)))
#$(1): $(DIR_BASE_SRC)$$(DIR_STEM)$(SUFFIX_FROM)
#dep := $(patsubst %$(SUFFIX_TO),%$(SUFFIX_FROM),$(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1)))
dep := $(basename $(subst $(DIR_BASE_OBJ),$(DIR_BASE_SRC),$(1)))$(SUFFIX_FROM)
$(1): $$(dep)
# rst2md: with hexo head and deploy copy
ifeq ($(SUFFIX_FROM),.rst)
ifeq ($(SUFFIX_TO),.md)
ifeq ($(ADD_HEXO_HEAD),TRUE)
	@echo start hexo head output...
ifdef ADD_HEXO_TAG_FROM_DIR
	$$(file >$$@.tmp,\
$$(call def_hexo_md_head,$(subst $(SUFFIX_TO),,$(notdir $(1)))\
,$(ADD_HEXO_TAG_FROM_DIR)\
,$(word $(words $(subst /, ,$(dir $(1)))),$(subst /, ,$(dir $(1))))\
)\
)
else
	$$(file >$$@.tmp,
$$(call def_hexo_md_head\
,$(subst $(SUFFIX_TO),,$(notdir $(1)))\
,$(word $(words $(subst /, ,$(dir $(1)))),$(subst /, ,$(dir $(1))))\
,$(word $(words $(subst /, ,$(dir $(1)))),$(subst /, ,$(dir $(1))))\
)\
)
endif
#	@echo $$(TBFILENAME)+2
#	@echo $(subst $(SUFFIX_TO),,$(notdir $(1)))+1#直接函数填入才能取到。
	@echo convert to utf8
	iconv -f GBK -t UTF-8 $$@.tmp >$$@
#用cp来替代iconv，以为linux下，gnumake的file命令输出的是UTF8文件类型。
#	cp $$@.tmp $$@
	@echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
	pandoc $$< -o - >>$$@
	@echo delete .tmp file...
	rm $$@.tmp
else
	@echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
	pandoc $$< -o $$@
endif
ifdef DIR_BASE_COPYTO
	@echo copy $(SUFFIX_TO) file to {hexo post}$(DIR_BASE_COPYTO) ...
#	cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) 
#因copy目标目录如果不存在，不能直接用cp命令，会出错，所以分两步，先mkdir, 再CP
	mkdir -p $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) 
	cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1)))
endif
endif
endif
# rst2pdf
ifeq ($(SUFFIX_FROM),.rst)
ifeq ($(SUFFIX_TO),.pdf)
	@echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
#	pandoc $$< -o - >>$$@
ifdef DIR_TEMPLATE
	pandoc $$< --metadata-file $(DIR_TEMPLATE)/metadata.yaml -o $$@ \
--pdf-engine=xelatex -s -N \
--toc --toc-depth=6 \
--template=$(DIR_TEMPLATE)/default.latex
ifdef DIR_BASE_COPYTO
	@echo copy $(SUFFIX_TO) file to $(DIR_BASE_COPYTO) ...
	cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1)))
endif
endif
endif
endif
# rst2html
ifeq ($(SUFFIX_FROM),.rst)
ifeq ($(SUFFIX_TO),.html)
#	@echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
	pandoc $$< -o $$@
ifdef DIR_BASE_COPYTO
	@echo copy $(SUFFIX_TO) file to $(DIR_BASE_COPYTO) ...
	cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) 
endif
endif
endif
# md2rst
ifeq ($(SUFFIX_FROM),.md)
ifeq ($(SUFFIX_TO),.rst)
	@echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
	pandoc $$< -o $$@
ifdef DIR_BASE_COPYTO
	@echo copy $(SUFFIX_TO) file to $(DIR_BASE_COPYTO) ...
	cp $$@ $(dir $(subst $(DIR_BASE_OBJ),$(DIR_BASE_COPYTO),$(1))) 
endif
endif
endif
	@echo $(SUFFIX_FROM)2$(SUFFIX_TO) finished!!!
endef

# 打散目标集合,一个一个送入命令集重组,同时用eval命令在makefile中使能。这样可以克服模式匹配依赖要一致的缺点(%只能匹配文件名,并且要规则一样)
$(foreach temp,$(OBJ_PATH_MDS),$(eval $(call PROGRAM_template,$(temp))))

###---伪目标
all: startconv
.phony: all startconv
# OBJ_PATH_DIR保证目录存在，OBJ_PATH_MDS转换文件
startconv: $(OBJ_PATH_DIR) $(OBJ_PATH_MDS)
#	@echo 转换 $(DIR_BASE_SRC)/$(SUFFIX_FROM) 到 $(DIR_BASE_OBJ)/$(SUFFIX_TO)
	@echo is updated.
	
#	@move xxx xxx ## MOVE [/Y | /-Y] [drive:][path]filename1[,...] destination

###---help

