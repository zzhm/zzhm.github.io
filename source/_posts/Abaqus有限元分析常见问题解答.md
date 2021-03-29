---
title: Abaqus有限元分析常见问题解答与错误处理
id: abaqus2020-qa
date: 2021-02-27 11:20:11
tags:
- 软件教程
- 有限元
categories:
- 实用教程
---

## 常见问题解答

### 如何求一个面的反力

反力是对约束而言的，你把这个面约束住，就可以在step模块的Field Output里面设置输出反力（Reaction Force），对于有些问题，设置输出截面力（Section Force）也可以得到面上的合力，人为通过应力*面积来计算合力不实际，除非应力是均匀的或者规律分布。所有点的力对面积积分就是总力。但这是很难计算的，所以建议你创建一个参考点，把需要求反力的面与参考点耦合起来，然后把原来对面的约束都加在参考点上，这样参考点上的反力就是截面的总反力了。

### 内力查看的两种方式

有些时候，不止是想知道部件的应力分布状况，也想知道部件某个截面的内力状况怎么办？除了外力接触力，也想知道Tie约束的面之间的作用力怎么办？

有点困惑了，不知道结果在哪了？通常我们会想到用节点力的输出来合成，可是节点力似乎不够便捷直观，怎么办？这些确实不是一般状况我们需要了解或者查看的结果，不过当我们需要这些结果的时候我们也得有相关技能，现在来GET这些技能吧：



方式一: Free Body Cut

在后处理模块(Visualization)下的使用Free Body Cut选项，可以基于View Cut的切面查看内力，也可基于网格边或者节点定义任意切面查看截面的内力：

![](https://gitee.com/zihm/images/raw/master/hexo/20210307104905.jpg)

 

![](https://gitee.com/zihm/images/raw/master/hexo/20210307104909.jpg)

 

![](https://gitee.com/zihm/images/raw/master/hexo/20210307104913.jpg)


Figure-1:  Free Body Cut                                

创建Free Body Cut后，也可在Create XY Data 中选择Free body创建相关截面内力的曲线。

![](https://gitee.com/zihm/images/raw/master/hexo/20210307104923.jpg) 

 Figure-2:  Free Body Force Output                    

方式二: Integrated Output Sections

在Step模块的菜单，Output选项Integrated Output Sections 创建一个截面I-section，然后在History Output中定义截面I-section上合力/合力矩的输出（SOF、SOM）；从结果文件中我们就能在历史输出变量中绘制所指定截面的合力曲线了：

![](https://gitee.com/zihm/images/raw/master/hexo/20210307104926.jpg) 

![](https://gitee.com/zihm/images/raw/master/hexo/20210307104931.jpg) 
Figure-3:  Integrated Output Sections                 

从结果文件中我们就能在历史输出变量中绘制所指定截面的合力曲线了。



## 常见错误处理

### abaqus.rpy file permission denied

安装完成ABAQUS2020后打开软件出现

```
IOerror: abaqus.rpy file permission denied
```

原因：软件默认的起始位置在与系统相关的文件夹`system32`，软件无法在相应的文件夹里创建文件`abaqus.rpy`。

![](https://gitee.com/zihm/images/raw/master/hexo/20210227104009.png)



解决方法：

先找到Abqaus CAE的快捷方式所在的文件夹，比如

```
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2020
```

点击`鼠标右键-->属性`

![](https://gitee.com/zihm/images/raw/master/hexo/20210227104743.png)

下面有两种解决方法。

方法一：设置起始位置，比如下图中的`C:\temp`。而默认文件夹也修改为相应文件夹。生成的`abaqus.rpy`等文件会默认保存在此文件夹中。

![](https://gitee.com/zihm/images/raw/master/hexo/20210227104145.png)



方法二：设置使用管理员身份运行。不建议！

![](https://gitee.com/zihm/images/raw/master/hexo/20210227104258.png)

如果以管理员方式启动会发现临时文件全部存在了`system32`目录下。

### 单元过度变形（Excessive distortion ）

使用 Abaqus 模拟分析大变形情况时一个经常出现又不容易解决的错误就是单元过度变形（Excessive Element Distortion）。出现该错误模型就会中止运行。虽然 Abaqus 会具体地给出出现过度变形的那些单元（[ErrElemExcessDistortion](https://cnzhx.net/fe/2015/01/29/view-errelemexcessdistortion-elements/)），然而这些信息往往对解决问题并没有多少帮助。

按照一般的经验，可以考虑检查下面的模型设置，

- **开启 NlGeom**。该设置在配置分析步（Step）的时候设置，就是要在模拟过程中考虑几何非线性（[Geometric Nonlinearity](https://www.comsol.com/blogs/what-is-geometric-nonlinearity/)），也就是使用 large-displacement formulation。该设置在 Explicit 的分析步中是默认开启的，但是在 Standard 的分析步中需要自己开启。
- 检查**材料**设置（material property)。看看材料属性设置的是否有明显错误。
- 检查分析步和增量步的**时长**是否合理。
- 单元化的尺寸（seed size）。调大/小一点 seed size 也许就可以避免这个问题。但是 discretisation 通常对结果会有影响，需要综合考虑。
- **单元类型**。单元类型中有很多设置，比如对 hourglass 的控制方式。可以试着换用不同的方式。还可以考虑换个单元类型试试看。

以上几点也不一定就能解决单元过度变形的问题，还需要慢慢积累经验。也欢迎有经验的朋友留言补充。



### Too many attempts made for this increment

作业（Job）时提示Error in job xxx:Too many attempts made for this increment。

这是因为：某一个分析步缺少边界条件。

在一个边界条件中，建立多个面的约束，很有可能计算错误！这可能是因为程序的设计问题，所以，尽量在每一个边界条件中，只建立关于一个面的约束。