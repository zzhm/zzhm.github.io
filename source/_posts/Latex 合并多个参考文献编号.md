---
title: LaTeX 把连续引用的参考文献合并
mathjax: false
date: 2021-07-27 10:23:52
id: latex-reference-with-bib
tags:
- latex
- 文献
- 论文
- 技能
categories:
- 实用教程
---

用Latex写论文的时候需要把连续引用的参考文献合并，例如：

`[1][2][3`]合并为`[1-3]`

方法很简单，引入包即可：

```tex
\usepackage{cite}
\cite{文献1,文献2,...}
```

这样有可能得到的效果是`[1,2,3]`

如果要达到`[1-3]`的效果，可以加入下列语句：

```tex
\usepackage[numbers,sort&compress]{natbib}
```

其中compress代表将一组文献索引“压缩”。

但使用elsarticle模板时出现报错：

```tex
option clash for package natbib
```

应该是重复引入natbib包了，因此可以不用显式引入natbib包，在开头位置添加即可：

```tex
\documentclass[compress]{elsarticle}
```

