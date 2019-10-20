###---伪目标
all: startconv
.phony: all startconv
# OBJ_PATH_DIR保证目录存在，OBJ_PATH_MDS转换文件
startconv: 
#	@echo 转换 $(DIR_BASE_SRC)/$(SUFFIX_FROM) 到 $(DIR_BASE_OBJ)/$(SUFFIX_TO)
	@echo is updated.
	
#	@move xxx xxx ## MOVE [/Y | /-Y] [drive:][path]filename1[,...] destination

###---help

