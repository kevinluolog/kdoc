vscode
=====


#package插件
##Markdown Preview Enhanced
vscode默认是支持markdown的，只需要装一个预览插件
特别两个功能：
1. 图像
Markdown Preview Enhanced 内部支持 mermaid, PlantUML, WaveDrom, GraphViz，Vega & Vega-lite，Ditaa 图像渲染。
你也可以通过使用 Code Chunk 来渲染 TikZ, Python Matplotlib, Plotly 等图像。
2. Code Chunk
Markdown Preview Enhanced 支持渲染代码的运行结果!!!

##latex公式，mardown+math插件
行内公式 $1+1=2 $
行外公式 
$ x=\frac{-b\pm\sqrt{b^2-4ac}}{2a} $


#tips

##JavaScript支持mathjax LaTex公式显示
文件开头加上以下代码即可，会自动获得MathJax的脚本支持
```
   <script type="text/javascript"
       src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```
在vs code中的插件转pdf的时候公式不生效，这时候建议转为html，再用了浏览器把html转为pdf，如果pdf有乱码，可以用nodepad++将html的编码改为utf-8后再转pdf；

##在线markdown编辑公式latex
[Markdown编辑数学公式的方法](https://blog.csdn.net/bryant_meng/article/details/78638456)
[Online LaTex Equation](http://latex.codecogs.com/eqneditor/editor.php)
```
1. 代表行内公式：
$ 公式代码 $ 
2.   代表块级公式：
$$ 公式代码 $$
```



