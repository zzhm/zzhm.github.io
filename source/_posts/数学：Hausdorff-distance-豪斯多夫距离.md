---
title: hausdorff distance 豪斯多夫距离
mathjax: false
date: 2018-04-30 11:27:29
id: hausdorff-distance
tags: 
- 数学
- 距离
- hausdorff distance
categories: 
- 学习笔记
---

Hausdorff距离是描述两组点集之间相似程度的一种量度，它是两个点集之间距离的一种定义形式：假设有两组集合A={a1,…,ap},B={b1,…,bq},则这两个点集合之间的Hausdorff距离定义为

　　H(A,B)=max(h(A,B),h(B,A))                            (1)

　　其中,

　　h(A,B)=max（a∈A）min（b∈B）‖a-b‖     (2)

　　h(B,A)=max（b∈B）min（a∈A）‖b-a‖     (3)

　　‖·‖是点集A和B点集间的距离范式(如:L2或Euclidean距离).

　<!--- more --->

这里,式(1)称为双向Hausdorff距离,是Hausdorff距离的最基本形式;式(2)中的h(A,B)和h(B,A)分别称为从A集合到B集合和从B集合到A集合的单向Hausdorff距离.即h(A,B)实际上首先对点集A中的每个点ai到距离此点ai最近的B集合中点bj之间的距离‖ai-bj‖进行排序,然后取该距离中的最大值作为h(A,B)的值.h(B,A)同理可得.

由式(1)知,双向Hausdorff距离H(A,B)是单向距离h(A,B)和h(B,A)两者中的较大者,它度量了两个点集间的最大不匹配程度.

<center>
![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155801968-1361698747.png) ![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155719093-1949884193.png) ![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155815171-1358998697.png) ![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155830359-1992187318.png) ![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155839437-239038889.png)![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155846780-241591623.png)![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155854140-458635263.png)![img](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/Hausdorff_distance/276683-20160510155901421-1693927402.png)
</center>


参考：http://cgm.cs.mcgill.ca/~godfried/teaching/cg-projects/98/normand/main.html