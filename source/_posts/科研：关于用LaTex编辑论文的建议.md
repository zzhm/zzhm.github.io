---
title: 关于用LaTex编辑论文的建议
mathjax: false
date: 2018-05-04 10:49:59
id: latex-advice-for-paper-writing
tags:
- 论文写作
- latex
- 软件教程
categories:
- 学习笔记
---

## 关于LaTeX版本的选择

Windows下的LaTeX最有名的TeX系统莫过于MikTeX与TeXLive，选择任意一个均可，推荐最新版的TeXLive。CTeX网站的CTeX套装只不过是把MikTeX捆绑上了Ghostscript、GSview以及编辑软件WinEdt而已，现在的MikTeX和TeXLive已经足够好用了，对中文的支持已经相当完善了，所以个人认为CTeX套装已经没有存在的必要了，用户也没有必要再对新版CTeX套装有什么期待了。

<!--- more --->

## 关于TeX系统的更新

建议不要盲目更新也不要因循守旧，特别是MikTeX更新时很容易出问题，除非很有必要一般一年更新一次即可。现在还有人在用着十年以前的TeX系统，其中一个原因就是他们还在使用CCT这种过时的、落后的技术。

## 关于编辑器的选择

 Windows下最好用的编辑器莫过于WinEdt了，可惜不是免费的，未注册的可以使用31天。WinEdt可在下面网址下载：`http://www.winedt.com/download.html`。另外用新版的MikTeX或TeXLive自带的TeXworks也可以，只是功能没有WinEdt强大。

## 关于文件编码的选择

新版本的WinEdt对UTF8编码的支持已经相当好了，并且默认把文件保存为UTF8编码。建议TeX文档都采用UTF8编码。

## 关于编译方式的选择

推荐使用XeLaTeX。十年以前我一般用LaTeX编译出dvi文件，再用yap预览，因为yap的正反向搜索很强大，用它很容易找到源文件中要修改的位置。现在我已经不用LaTeX编译了，一般采用PDFLaTeX、XeLaTeX、LuaLaTeX来编译LaTeX文档，SumatraPDF配合WinEdt使用正反向搜索很强大，而且PDF文件预览比dvi文件要快得多。

SumatraPDF在`https://pan.baidu.com/s/1dEWFSRn`下载。在系统升级，安装&删除字体后，使用XeLaTeX有时会卡在eu1lmr.fd较长时间，这时只要清空 `D:\texlive\2016\texmf-var\fonts\cache`中的文件，再运行`fc-cache -rv`即可。

行内公式用`$…$`，行间公式用`\[…\]`。这是因为有的杂志要求用word投稿(主要是某些中文杂志)，当你用LaTeX写好论文后杂志社却要求你提供word格式的论文，这时你会想到用mathtype把LaTeX文档转换成word文档，mathtype要求行内公式用`$…$`，行间公式用`\[…\]`。当然，如果你没有这方面的需求可以无视这条。

### 注意事项

尽量不要在源文件里用`“\def, \newcommand,\renewcommand”`等等命令缩写，你可以在WinEdt里自定义缩写输入的方式。在WinEdt里自定义缩写输入的方法如下:在菜单栏依次点击Options，Option Interface...，再打开Abbreviations，将其中的ENABLED=0改为ENABLED=1，然后在SUB="END_LIST"下面添加上你的自定义缩写命令，如: `"\SN"  -> "\mathbb{S}\^{n}"`,保存以后在左边的Abbreviations处点鼠标右键再点击Load Script即可。你也可以不改变其中的ENABLED=0而使用组合键Alt+Enter输入你的自定义缩写命令。



原文来自：数学控制club