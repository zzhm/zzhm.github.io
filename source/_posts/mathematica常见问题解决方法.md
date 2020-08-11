---
title: mathematica常见问题解决方法
mathjax: false
date: 2020-08-11 09:52:42
id: mathematica-qa
tags:
- 软件
- mathematica
- 教程
categories:
- 学习
- 软件
---

如何在使用`PlotTheme->“Scientific”`选项的时候设置轴标签

I'm liking the new plot themes in Mathematica 10, but finding that I can't override the options it sets. For example,

```mma
Plot[x^2, {x, 0, 10}, AxesLabel -> {x}, PlotTheme -> "Scientific"]
```

returns the right plot but without the axis label. How do I fix this?



The theme generates a framed plot. You need to use `FrameLabel`,e.g.

```mma
Plot[x^2, {x, 0, 3}, FrameLabel -> {Style[x, 30], Style[y, 30]}, 
 PlotTheme -> "Scientific"]
```

![](https://i.stack.imgur.com/lqb35.png)