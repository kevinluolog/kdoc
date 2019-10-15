***************
memo of debug
***************

.. contents:: 目录
.. section-numbering::

.. 
 :Author: kevinluo
 :Contact: kevinluo_72@163.com

.. 
 .. contents:: 目录
 .. section-numbering::

makefile
===========

ELSE 应该小写。
-------------------

现象：

编译seprator错误。同时指向行号为后面的foreach处

解决：

ELSE 应该小写。

::

  ifeq ($(ADD_HEXO_HEAD),TRUE)
    @echo start hexo head output...
    $$(file >$$@.tmp,$$(call def_hexo_md_head,$(subst $(SUFFIX_TO),,$(notdir $(1)))))
  # @echo $$(TBFILENAME)+2
  # @echo $(subst $(SUFFIX_TO),,$(notdir $(1)))+1#直接函数填入才能取到。
    @echo convert to utf8
    iconv -f GBK -t UTF-8 $$@.tmp >$$@
    @echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
    pandoc $$< -o - >>$$@
    @echo delete .tmp file...
    del $$@.tmp
  ELSE
    @echo start pandoc $(SUFFIX_FROM)2$(SUFFIX_TO)...
    pandoc $$< -o $$@
  endif
  $(foreach temp,$(OBJ_PATH_MDS),$(eval $(call PROGRAM_template,$(temp))))