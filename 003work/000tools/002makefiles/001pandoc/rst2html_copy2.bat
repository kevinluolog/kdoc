REM pushd "%~dp0" popd
REM enter directory where running file is located，push old DIR into DIR Stack，popd popup old DIR from DIR Stack.
pushd %~dp0

.\..\..\001make\gnumake startconv -f makefile ^
DIR_BASE_SRC=H:\tmp_H\001.work\002git\kdoc\003work\002memo ^
DIR_BASE_OBJ=H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\tmp2 ^
DIR_BASE_COPYTO=H:\tmp_H\001.work\004.env\01prjsp\04make\01rst2md\copy2 ^
SUFFIX_FROM=.rst ^
SUFFIX_TO=.html ^
DIR_TEMPLATE=

popd