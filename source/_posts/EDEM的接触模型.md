---
title: EDEM的接触模型
mathjax: false
date: 2019-03-06 12:13:49
id: edem-contact-models
tags:
- edem
- 学习
- 接触模型
- 离散元
categories:
- 学习
- 离散元
---

1. Hertz-Mindlin模型。基本的颗粒接触模型，用于常规颗粒的接触作用。

2. Hertz-Mindlin with RVD RollingFriction模型。在基本的Hertz-Mindlin模型基础上调整了滚动摩擦力的计算方式，适于强旋转体系对物料滚动特性有严格要求的问题。

   <!---more--->

3. Hertz-Mindlin with JKR模型，又称JKR Cohesion模型。适用于药粉等粉体颗粒和农作物、矿石、泥土等含湿物料，颗粒间因静电力、含湿水分等原因发生明显粘结和团聚。

4. Hertz-Mindlin with bonding模型。用于模拟破碎、断裂等问题，采用小颗粒粘结成大块物料，外力作用下颗粒间粘结力会发生破坏，从而产生破碎及断裂效果。

5. Hertz-Mindlin with Heat Conduction模型。带有热传导的基本接触模型，用于要求温度分析的场合，颗粒接触后会因温度差而产生热传导。

6. Hysteretic Spring模型。用于颗粒受到较大压力后产生塑性形变的场合，如：注塑充模、压路、捣固等。

7. Linear Cohesion模型。传统的颗粒粘结模型，用于一般性粘结颗粒的快速计算，亦可用于含湿物料。但与JKR Cohesion模型的区别是：JKR Cohesion模型计算的粘性力同时存在于颗粒接触的法向和切向上，而Linear Cohesion模型的粘性力只存在于法向。

8. Linear Spring模型。基本颗粒接触模型，用于常规颗粒的快速计算及定性分析。

9. Moving Plane模型。用于模拟传送带等具有表面滑移速度的结构体。
  以上接触模型可以满足大多数工程应用需要，然而实际问题千变万化，不可能涵盖所有情况。因此，EDEM提供了API (Application Programming Interface) 二次开发接口，使用户可以根据特殊问题定制模型，最大程度满足仿真模拟的要求。