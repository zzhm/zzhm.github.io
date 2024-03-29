---
title: Abaqus2018简单入门
mathjax: true
date: 2019-06-27 15:22:10
id: abaqus-simple
tags:
- abaqus
- 有限元
- 软件
- 学习
- 教程
categories:
- 实用教程
---

ABAQUS是国际上公认的最优秀的非线性分析软件，如果分析对象是接触、大变形或非线性材料（例如橡胶、土体）等复杂问题，建议优先考虑选择ABAQUS作为分析软件。

<!---more--->

## 关于单位制

ABAQUS中没有固定的单位制， 读者选用相互匹配的单位即可， 最后得出的计算结果的单位与所采用的单位制相对应。在Sketch功能模块中，ABAQUS能够接受的模型尺寸范围是$10^{-3}~10^5$因此读者在建立模型之前应该根据模型尺寸选择一套合适的单位制，使模型的大小在上述范围内。一般可 以选择国际单位制（长度单位为m或mm),如果模型的尺寸很小（微细观结构），就必须更改单位制，选择长度单位为纳米或者微米，所有其他单位也要进行相应的换算，以保待量纲一致。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561621164753.png)

## 关于仿真时间

### 两种时间计量方法
1)总分析时间(total time)计景法：从第1个分析步开始， 所有分析步的时间累加起来（包括重启动分析中的分析步时间）。
2)分析步时间(step time)计量法：每个分析步的开始为0时刻（线性摄动分析步除外， 它不考虑时间影响）。
图所示的例子可以说明这两种时间计量法的差异。在这个例子中， 共包含三个分析步(step) , 每个分析步步长为50s。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561625314899.png)

在静力分析中， 如果模型中不包含阻尼或与速率相关的材料时间就没有实际的物理意义。为方便起见， 一般把分析步时间设置为默认值1。动力分析中涉及到爆炸、冲击等与时间有关的效应， 应根据实际情况选择合适的时间计措方法。

在ABAQUS/CAE中建模时，除了需要在Step功能模块中设置时间之外。在Load功能模块和Interaction功能模块中还可以创建与时间有关的幅值曲线，具体方法是：选择菜单`Tools->Amplitude->Create`, 选择幅值曲线的类型，将Time Span设为Step time或Total time, 在定义载荷和边界条件时可以使用上述幅值曲线。

### 影响仿真时间的因素

提高求解精度和缩短计算时间是有限元分析的两个重要目标， 而这二者又是互相矛盾的， 缩短计算时间往往要以牺牲计算梢度作为代价。 如何根据不同的问题类型和求解要求建立最合 理的模型， 用尽卅短的计算时间得到足够精确的结果， 是有限元分析过程中的一个重要间题。

影响分析时间的主要因素包括下列几个方面。

1)分析类型：一维平面应力、 平面应变和轴对称问题要比三维问题的模型规模小得多， 如果所分析的问题符合二维模型的特征， 就没有必要建立三维模型。《实例详解》中的很多实例都使用了维模型，研究者可以仔细思考一下在什么情况下可以选择二维模型。另外， 非线性问题比线性问题迭代收敛难度大， 如果在模犁中定义了接触、 几何非线性、弹塑性材料等非线性参数，计算时间也会大大增加。

2)	网格密度：网格越细化，单元和节点数目就越多，计算时间也就越长。

3)	单元类型：对千同样的网格，二次单元（例如C3D20R)比线性单元（例如C3D8R)增加了很多内部节点，因此计算时间会大大增加。完全积分单元（例如C3D8)和 非协调单元（例如C3D81)的积分点比减缩积分单元（例如C3D8R)多，计算时间也相对更长一些。

4)接触的定义：接触面上的节点越多，计算时间就越长。有限滑移接触算法(finite sliding)比小滑移接触算法(smallsliding)计算量大，计算时间也更长。

5)分析步时间、增量步和迭代步：在静力分析中，分析步时间没有实际的物理含􀃈， 计算时间取决千迭代步和增益步的数世。问题越复杂，收敛难度越大，增量步长就越小， 需要的迭代次数也就越多，计算时间就会越长。在动力分析中，分析步时间对应实际的物理时间，分析步时间越长，则求解时间越􀁤。 一般情况下，在ABAQUS/Explicit分析中都只定义很短的分析步时间（例如0. 02 s) , 否则 可能计算时间过长。另外，影响ABAQUS/Explicit分析时间的关键因素是稳定极限值，它取决于最小单元尺寸、材料性质、材料密度、单元类型等因素，详见本书第15.4.2节ABAQUS/Explicit分析的增量步长。

6)计算机的性能：增大内存可以大大缩短 ABAQUS/Standard分析的计算时间，而对 ABAQUS/Explicit分析影响不大。提高CPU的主频、使用多CPU或并行计算对于加快 ABAQUS/Standard和ABAQUS/Explicit的分析速度都很有效。

## 关于部件类型

部件类型：可变形体、离散刚体、解析刚体（为接触分析提供刚性表面）、欧拉体。

如果模型中某个部件的刚度远远大于其他部件，其变形远远小千其他部件，就可以将其定义为刚体部件。在分析过程中刚体部件不发生变形（即整个部件上各点之间的距离保持 不变）， 而只发生整休的平动或转动。
刚体部件是一个相对的概念， 例如在冲压、 轧制等金属成形分析中， 模具或轧棍的刚度 远远大千还料， 如果模具或轧棍本身的应力和变形不是所关心的对象， 就可以将其定义为刚 体部件。
由于刚体部件只发生整体的平动或转动， 因此可以用一个点的运动情况来控制整个刚体的运动情况， 这个点即刚体参考点(rigid part reference point)。 创建刚体部件时， 需要为其定义刚体参考点（单击菜单Tools- Reference Point) , 刚体部件上的所有边界条件和载荷都要施加在这个刚体参考点上。
与变形体部件相比，刚体部件最大的优点是计算效率高。 在分析作业运行过程中，刚体部件不参与所有基本单元的计算(例如生成单元刚度矩阵、单元质量矩阵、总体刚度矩阵等），因此可以节省大量的分析时间。 另外， 在接触分析中， 如果接触对的主面是刚体部件的面，分析就更容易收敛。

## 仿真的基本流程

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561622118424.png)

## 界面与工具箱

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561691977714.png)

<center>部件工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692238946.png)

<center>属性工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692443443.png)

<center>装配工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692594056.png)

<center>分析步工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692706141.png)

<center>相互作用工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692815577.png)

<center>载荷工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561698786627.png)

<center>网格工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692898081.png)

<center>作业工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561693037595.png)

<center>可视化工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1561692079138.png)

<center>草图工具栏</center>
![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1567394289377.png)

<center>功能模块使用顺序</center>