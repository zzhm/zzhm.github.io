---
title: LaTeX与bib添加参考文献
mathjax: false
date: 2018-07-06 12:23:52
id: latex-reference-with-bib
tags:
- latex
- 文献
- 论文
- 技能
categories:
- 实用教程
---

LaTeX参考文献添加的2中方式。

<!---more--->

## 方法一

Latex`中有多种添加参考文献的方式`，一种是

```
\begin{thebibliography}
\bibitem{Li2016}  % i2016为标签
Y. Lee, S. H. Kim and C. C. Chung, ``Integral sliding mode control with a disturbance observer for next-generation servo track writing,''~\emph{Mechatronics}, vol. 40, pp. 106--114, 2016.
.....
\end{thebibliography}
```

这种方式参考文献按照期刊规定的格式直接写在`.tex`文件中，在引用处直接`\cite{}`该文件。 

## 方法二

另一种我比较熟悉的引用方式是把参考文献写在`.bib`文件中，然后和.tex放在同一文件夹下，`.tex`直接引用`.bib`中的参考文献。这种方法比较简单，不需要你根据期刊的格式每个都改动，只需要你找到相关的文件，按照Bibtex格式放到`.bib`文件中，在tex文件中会按照指定的参考文献格式现实。接下来就介绍这种方法：

### 在tex文件前面添加使用cite包

```latex
\documentclass{article}
\usepackage{cite}  %添加此处，begin{document}之前
\begin{document}
...
```

### Bibtex格式

首先从google学术或者百度学术上找到参考文采用，然后引用->导出Bibtex格式文件，就会显示如下格式：

```
@article{Sniffen1992A, 
title={A net carbohydrate and protein system for evaluating cattle diets: II. Carbohydrate and protein availability.}, 
author={Sniffen, C. J. and O’Connor, J. D. and Van Soest, P. J. and Fox, D. G. and Russell, J. B.}, 
journal={Journal of Animal Science}, 
volume={70}, 
number={11}, 
pages={3562-77}, 
year={1992}, 
} 
```

解释如下： 

```
@article{name1, 
title = {标题}, 
author = {作者, 多个作者用 and 连接}, 
journal = {期刊名}, 
volume = {卷20}, 
number = {页码}, 
pages={}, 
year = {年份}, 
}
```

将上述生成的文件拷贝到`.tex`文件夹下。或者新建一个txt文件，将后缀名改为bib，即创建了一个BibTex参考文献库，如创建的BibTex库的名字为：`ref.bib`。把要引用的文献的BibTex格式内容的复制到`ref.bib`里面。

### 在.tex文件中引用文献

在Latex文档里面添加包引用：`\usepackage{cite}`。在文章中使用 `\cite{name1}`（name1为参考文献Bibtex名称）引用文章。

### 生成参考文献列表

在Latex文档里面添加BibTex库的引用，要在哪里显示参考文献，就在哪里添加如下内容：

```
\bibliographystyle{plain}  %设置参考文献类型
\bibliography{ref}      %声明参考文献文件名称
```

`\bibliography{ref}`命令用于指定之前生成的.bib库。

参考文献的呈现方式，常见的预设样式的可选项有8种，分别是：

```
   plain，按字母的顺序排列，比较次序为作者、年度和标题；
   unsrt，样式同plain，只是按照引用的先后排序；
   alpha，用作者名首字母+年份后两位作标号，以字母顺序排序；
   abbrv，类似plain，将月份全拼改为缩写，更显紧凑；
   ieeetr，国际电气电子工程师协会期刊样式；
   acm，美国计算机学会期刊样式；
   siam，美国工业和应用数学学会期刊样式；
   apalike，美国心理学学会期刊样式；
```

### 编译过程

- 用`pdfLaTeX/xelatex`编译你的 `.tex `文件 , 这是生成一个` .aux` 的文件, 这告诉 BibTeX 将使用那些应用.
- 用BibTeX 编译 `.bib`文件.
- 再次用`pdfLaTeX/xelatex` 编译你的 `.tex` 文件, 这个时候在文档中已经包含了参考文献, 但此时引用的编号可能不正确.最后用 再再次`pdfLaTeX/xelatex` 编译你的 `.tex` 文件, 如果一切顺利的话, 这是所有东西都已正常了.

这样就可以了，不需要自己每个参考文献都调整。