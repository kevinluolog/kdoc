vscode
=====

# 1. package插件

## 插件汇总

## vscode插件

01. HTML Snippets，提示初级的h5代码片段，标签等
02. HTML CSS Support，让html标签写上class，智能提示当前项目所支持的样式。
03. view in browers，ctrl+f1在默认浏览器中，运行当前的html
04. vscode-icon，让vscode的文件夹目录添加上对应的图标。（如果不生效，在【文件-首选项-文件图标主题】重新选择设置）
05. path intellisense，文件路径自动补齐。
06. npm intellisense，require引用包的补齐
07. bracket pair colorizer，让括号有独立的颜色
08. auto rename tag ，修改标签闭合
09. vetur，vue插件，语法高亮、智能感知、emmet
10. tortoiseSvn，svn插件
11. auto close tag，自动添加html、xml关闭标签
12. beautify，格式化代码
13. change-case，修改文本的更多明明格式，驼峰命名，下划线分割命名等等
14. chinese(Simplified)Language Pack for Visual Studio，vscode看不习惯英文的同学，可以下载安装这个，中文简体语言包
15. color info，在颜色上悬停光标，就可以预览色块中色彩模型的详细信息、
16. css peek，追踪至样式表中css类和id定义的地方。在html文件右键菜单，单击选择器时，选择“go to definition ”，会跳转到css样式代码段
17. debugger for chrome，前端调试
18. eslint,检查js编程中的语法错误
19. html boilerplate，html模板插件，一键创建html文件
20. htmlHint，html代码格式检测
21. image preview，鼠标防在image路劲上，显示图像预览
22. intelliSense for CSS class names in HTML，把项目中css文件里的名称，智能提示在html中
23. JavaScript (ES6) code snippets ，es6代码片段提示

## 1-1. Markdown Preview Enhanced

vscode默认是支持markdown的，只需要装一个预览插件特别两个功能：

1. 图像

    Markdown Preview Enhanced 内部支持 mermaid, PlantUML, WaveDrom, GraphViz，Vega & Vega-lite，Ditaa 图像渲染。
    
    你也可以通过使用 Code Chunk 来渲染 TikZ, Python Matplotlib, Plotly 等图像。

2. Code Chunk

    Markdown Preview Enhanced 支持渲染代码的运行结果!!!

## 1-2. latex公式，mardown+math插件

行内公式 $1+1=2 $
行外公式 
$ x=\frac{-b\pm\sqrt{b^2-4ac}}{2a} $

# 2. tips

## 2-1. JavaScript支持mathjax LaTex公式显示

文件开头加上以下代码即可，会自动获得MathJax的脚本支持

    <script type="text/javascript"
       src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

在vs code中的插件转pdf的时候公式不生效，这时候建议转为html，再用了浏览器把html转为pdf，如果pdf有乱码，可以用nodepad++将html的编码改为utf-8后再转pdf；

## 2-2. 在线markdown编辑公式latex

[Markdown编辑数学公式的方法](https://blog.csdn.net/bryant_meng/article/details/78638456)

[Online LaTex Equation](http://latex.codecogs.com/eqneditor/editor.php)

    1. 代表行内公式：
    $ 公式代码 $ 
    2.   代表块级公式：
    $$ 公式代码 $$

