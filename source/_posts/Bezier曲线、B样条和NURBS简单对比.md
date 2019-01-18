---
title:  Bezier曲线、B样条和NURBS简单对比
mathjax: false
date: 2018-11-30 20:05:46
id: bezier_nurbs_relation
tags:
- 曲线
- 学习
categories:
- 学习
- 曲线
---

 Bezier曲线、B样条和NURBS都是根据控制点来生成曲线的，那么他们有什么区别了？

<!---more--->

简单来说，就是:

- Bezier曲线中的每个控制点都会影响整个曲线的形状，而B样条中的控制点只会影响整个曲线的一部分，显然B样条提供了更多的灵活性；

- Bezier和B样条都是多项式参数曲线，不能表示一些基本的曲线，比如圆，所以引入了NURBS，即非均匀有理B样条来解决这个问题；

- Bezier曲线只是B样条的一个特例而已，而B样条又是NURBS的一个特例，它们的关系可以图示为：

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1543579993403.png)

B样条克服了Bezier曲线的一些缺点，Bezier曲线的每个控制点对整条曲线都有影响，也就是说，改变一个控制点的位置，整条曲线的形状都会发生变化，而B样条中的每个控制点只会影响曲线的一段参数范围，从而实现了局部修改；