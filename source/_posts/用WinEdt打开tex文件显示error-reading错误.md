---
title: 用WinEdt打开tex文件显示error reading错误
mathjax: false
date: 2021-10-18 13:01:19
id: winedt-error
tags:
- latex
- 论文写作
categories:
- 实用教程
---

是因为`.tex`文件中包含了`utf-8`字符，而在打开的时候并没有指明`utf-8`打开方式。

- 解决方法一

![](https://gitee.com/zihm/images/raw/master/hexo/20211018113940.jpg)

在WinEdt中，【File】-【Open】（或使用快捷键`Ctrl+O`），在弹出的打开对话框中，右下角【文件名】右侧有一个打开扩展名方式，默认是`default(*.*)`形式，点击下三角号，选择`UTF-8(*.*)`形式。再选择相应的`.tex`文件打开即可。

- 解决方法二

就是在`.tex`源文件内容的开头加上一行

```tex
% !Mode:: "TeX:UTF-8" 或者
%# -*- coding:utf-8 -*-
```

- 解决方法三

在【Options】 -【 Preference】 -  Wrapping 选项卡中加上Tex，改成

```tex
Tex;UTF-8|ACP;EDT;INI
```

![](https://gitee.com/zihm/images/raw/master/hexo/20211018125255.png)

就可以了。这样所有的`.tex`文档都被默认是`utf-8`文档打开。但是WinEdt还没有办法很好支持两种以上的`utf-8`文档，比如同时输入中文和韩语。这方案我基本不用，建议使用第二方案！

此时，WinEdt可以正常打开包含`utf-8`字符的`.tex`文件了。

