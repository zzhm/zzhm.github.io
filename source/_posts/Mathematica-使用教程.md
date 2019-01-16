---
title: Mathematica核心内容提示
mathjax: false
date: 2018-12-29 14:37:39
id: Mathematica 
tag:
- mathematica 
- 学习
- 数学
category:
- 学习
---

- Mathematica中大写小写是有区别的，如Name、name、NAME等是不同的变量名或函数名。 
- 系统所提供的功能大部分以系统函数的形式给出，内部函数一般写全称，而且一定是以大写英文字母开头，如`Sin[x],Conjugate[z]`等。 
- 乘法即可以用`*`，又可以用空格表示，如`2 3＝2*3＝6 ,x y,2 Sin[x]`等；乘幂可以用`^`表示，如`x^0.5,Tan[x]^y`。 
- 自定义的变量可以取几乎任意的名称，长度不限，但不可以数字开头。注意不要与系统变量冲突。不要小看这些简单的符号，它们包含的信息远远大于我们所熟知的它们的近似值，它们的精度也是无限的。 

<!---more--->

```
Pi 3.1415....的无限精度数值 
E 2.17828...的无限精度数值 
Catalan 0.915966..卡塔兰常数 
EulerGamma 0.5772....高斯常数 
GoldenRatio 1.61803...黄金分割数 
Degree Pi/180角度弧度换算 
I 复数单位 
Infinity 无穷大 
-Infinity 负无穷大 
ComplexInfinity 复无穷大 
Indeterminate 不定式 
```
## 基本概念

### 符号与变量

- 自定义的变量可以取几乎任意的名称，长度不限，但不可以数字开头。
- 当你赋予变量任何一个值，除非你明显地改变该值或使用Clear[变量名]或“变量名=.”取消该值为止，它将始终保持原值不变。(多个打开的文档中符号是可以相互调用的？)

- 全局赋值用等号`=`，局部赋值用箭头`->`。利用`%n`可以引用第`Out[n]`行结果，利用`%。。。%（k个）`可以引用倒数第k个计算结果。
- 自定义函数格式`g[x_,y_]:=(x-y)^2/y`。自定义函数表达式左边的自变量要写在[  ]号内，且后面跟随“_”（下划线），右边则不需要。
- 一定要注意四种括号的用法：
  - ()圆括号表示项的结合顺序，如`(x+(y^x+1/(2x)))`;
  - []方括号表示函数，如`Log[x],BesselJ[x,1]`；
  - {}大括号表示一个“表”(一组数字、任意表达式、函数等的集合)，如`{2x,Sin[12 Pi],{1+A,y*x}}`；
  - [[]]双方括号表示“表”或“表达式”的下标，如`a[[2,3]]、{1,2,3}[[1]]=1`。
- 可以使用`? 符号名`或`??符号名`来获得关于该符号(函数名或其他)的粗略或详细介绍。符号名中还可以使用通配符，例如`?M*`，则系统将给出所有以M开头的关键词和函数名，再如`??For`将会得到关于For语句的格式和用法的详细情况。
- 另外，在程序中书写注释可以用一对`(*　 *)`括起来，注释可以嵌套。 

### 计算精度

- 在Mathematica中你不必考虑数的精确度，因为除非你指定输出精度，Mathematica总会以绝对精确的形式输出结果。例如：你输入 `In[1]:=378/123`，系统会输出`Out[1]:=126/41`，如果想得到近似解，则应输入 `In[2]:=N[378/123,5]`,即求其5位有效数字的数值解，系统会输出`Out[2]:=3.073` 
- 另外Mathematica还可以根据你前面使用的数字的精度自动地设定精度。 Mathematica与众不同之处还在于它可以处理任意大、任意小及任意位精度的数值，如`100^7000,2^(-2000)`等数值可以很快地求出，但在其他语言或系统中这是不可想象的，你不妨试一试`N[Pi,1000]`。  
- 若想获得计算结果的近似值，可按如下格式输入：`表达式//N`或者`N[表达式]`。要求符合任意精度要求的结果，其格式如下：`N[表达式,n]`  （结果保留n位精度）

### 格式与语句 

- Mathematica的语句书写十分方便，一个语句可以分为多行写，同一行可以写多个语句（但要以分号间隔）。当语句以分号结束时，语句计算后不做输出（输出语句除外），否则将输出计算的结果。 
- 在Mathematica的编辑界面中输入语句和函数，确认光标处于编辑状态(不断闪烁)，然后按Insert键来对这一段语句进行求值。如果语句有错，系统将用红色字体给出出错信息，你可以对已输入的语句进行修改，再运行。如果运行时间太长，你可以通过`Alt+.`(Alt+句号)来中止求值。 　 
- 对函数名不确定的，可先输入前面几个字母(开头一定要大写)，然后按`Ctrl+K`，系统会自动补全该函数名。
- 按下小键盘区的`Enter` 会进行计算，按下字母区的`Enter`出现换行。

### “表”及其用法

“表”是Mathematica中一个相当有用的数据类型，它即可以作为数组，又可以作为矩阵；除此以外，你可以把任意一组表达式用一个或一组{}括起来，进行运算、存储。可以说表是任意对象的一个集合。它可以动态地分配内存，可以方便地进行插入、删除、排序、翻转等等几乎所有可以想象到的操作。 

如果你建立了一个表，你可以通过下表操作符[[]](双方括号)来访问它的每一个元素，索引标号从1开始。如我们定义table={2,Pi ,{aaa,A}}为一个表，那么table[[1]]就为2，table[[2]]就是Pi，而table[[3,1]]表示嵌套在table中的子表{aaa,A}的第一个元素即aaa，table[[3,2]]表示{aaa,A}第二个元素即A。总之，表每一层次上并列的部分用逗号分割，表可以无穷嵌套。 

### 程序流程控制

循环语句有For[赋初值，循环条件，增量语句，语句块]表示如果满足循环条件，则执行语句块和增量语句，直到不满足条件为止，While[test,block]表明如果满足条件test则反复执行语句块block,否则跳出循环，Do[block,{i,imin,imax,istep}]与前者功能是相同的。还有Goto[lab], Label[lab]提供了程序中无条件跳转，Continue[]和Break[]提供了继续循环或跳出循环的控制，Catch[语句块1]和Throw[语句块2]提供了运算中对异常情况的处理。

## 常用函数

### 表函数

```
Append[表,表达式]或Prepend[表,表达式]把表达式添加到表的最前面或最后面，如Append[{1,2,3},a]表示{1,2,3,a}。
Union[表1，表2，......],Jion[表1,表2,......]来把几个表合并为一个表，二者不同在于Union在合并时删除了各表中重复的元素，而后者仅是简单的合并；
Flatten[表]把表中所有子表"抹平"合并成一个表，如Flatten[{1,2,{Sin[x],dog},{{y}}}]表示{1,2,Sin[x],dog,y}。
Patition[表，整数n]把表按每n个元素分段作为子表，集合成的表。Partition[{1,2,Sin[x],y},2]把表每两个分段，结果为{{1,2},{Sin[x],y}}；
Delete[表，位置]、Insert[表，位置]来向表中按位置插入或删除元素，如要删除上面提到的table中的aaa,你可以用Delete[table,{3,1}]来实现；
Sort[表]给出了表中各元素的大小顺序；
Reverse[表]、RotateLeft[表，整数n]、RotateRight[表，整数n]可以分别将一个表进行翻转、左转n个元素、右转n个元素等操作；
Length[表]给出了表第一个层次上的元素个数；
Position[表，表达式]给出了表中出现该表达式的位置，Count[表，表达式]则给出表达式出现的次数。
```

### 图形函数

图形函数中最有代表性的函数为**Plot[表达式，{变量，下限，上限}，可选项]**，(其中表达式还可以是一个"表达式表"，这样可以在一个图里画多个函数)；变量为自变量；上限和下限确定了作图的范围；可选项可要可不要，不写系统会按默认值作图，它表示对作图的具体要求。

例如`Plot[Sin[x],{x,0,2*Pi},AspectRatio-1]`表示在0<x<2Pi的范围内作函数Sin[x]的图象，AspectRatio为可选项，表示图的x向y向比例，AspectRatio-1表示纵横比例为1:1，如果不写这一项，系统默认比例为1:GodenRatio,即黄金分割的比例(注意，**可选项的写法为可选项名-可选项值**)，Plot还有很多可选项，如PlotRange表示作图的值域，PlotPoint表画图中取样点的个数，越大则图越精细，PlotStyle来确定所画图形的线宽、线型、颜色等特性，AxesLabel表式在坐标轴上作标记等等。 

```
Plot[函数f，{x，xmin，xmax}，选项] :在区间{x，xmin，xmax}上，按选项的要求画出函数f的图形 
Plot[{函数1，函数2}，{x，xmin，xmax}，选项] :在区间{x，xmin，xmax}上，按选项的要求画出几个函数的图形 
Plot3D[二维函数表达式，{变量1，下限，上限}, {变量2，下限，上限}，可选项}]Plot3D[二维函数表达式，{变量1，下限，上限}, {变量2，下限，上限}，可选项}] 
二维参数方程作图：ParametricPlot[{x(t),y(t)},{t,下限,上限}，可选项]
三维参数方程作图：ParametricPlot3D[{x(u,v),y(u,v),z(u,v)},{u,下限,上限},{v,下限,上限}，可选项]
二维等高线图：ContourPlot[二元表达式，{变量1，下限，上限}, {变量2，下限，上限}，可选项}]
二维密度图：DensityPlot[二元表达式，{变量1，下限，上限}, {变量2，下限，上限}，可选项}]
```

除使用上述函数作图以外，Mathematica还可以象其他语言一样使用图形元语言作图，如画点函数Point[x,y],画线函数Line[x1,y1,x2,y2],画圆的Circle[x,y,r]，画矩形和多边形的Rectangle和Polygon,字符输出的Text[字符串,输出坐标]，还有颜色函数RGBColor[red,green,blue]、Hue[],GrayLevel[gray]来描述颜色的亮度、灰度、饱和度，用PointSize[相对尺度]、Thickness[相对尺度]来表示点和线的宽度。总之Mathematica可以精确地调节图形的每一个特征。 

### 数学函数

Mathematica系统内核提供了丰富的数学计算的函数，包括极限、积分、微分、最值、极值、统计、规划等数学的各个领域，复杂的数学问题简化为对函数的调用，极大地提高了解决问题的效率。

```
D[f, x] 求f[x]的微分 
D[f, {x, n}] 求f[x]的n阶微分 
D[f,x1,x2..] 求f[x]对x1,x2...偏微分 
Dt[f, x] 求f[x]的全微分df/dx 
Dt[f] 求f[x]的全微分df 
Dt[f, {x, n}] n阶全微分df^n/dx^n 
Dt[f,x1,x2..] 对x1,x2..的偏微分 

Integrate[f, x] f[x]对x在的不定积分 
Integrate[f, {x, xmin, xmax}] f[x]对x在区间(xmin,xmax)的定积分 
Integrate[f, {x, xmin, xmax}, {y, ymin, ymax}] f[x,y]的二重积分 

Limit[expr, x->x0] x趋近于x0时expr的极限 
Residue[expr, {x,x0}] expr在x0处的留数 
Series[f, {x, x0, n}] 给出f[x]在x0处的幂级数展开 
Series[f, {x, x0,nx}, {y, y0, ny}]先对y幂级数展开，再对x 
Normal[expr] 化简并给出最常见的表达式 
SeriesCoefficient[series, n] 给出级数中第n次项的系数 
SeriesCoefficient[series, {n1,n2...}] 
'或Derivative[n1,n2...][f] 一阶导数 
InverseSeries[s, x] 给出逆函数的级数 
ComposeSeries[serie1,serie2...] 给出两个基数的组合 
SeriesData[x,x0,{a0,a1,..},nmin,nmax,den]表示一个在x0处x的幂级数，其中aii为系数 

O[x]^n n阶小量x^n 
O[x, x0]^n n阶小量(x-x0)^n 
Dt[f, x] 求f[x]的全微分df/dx 
Dt[f] 求f[x]的全微分df 
Dt[f, {x, n}] n阶全微分df^n/dx^n 
Dt[f,x1,x2..] 对x1,x2..的偏微分 
```

不定积分Integreate函数主要计算只含有“简单函数”的被积函数. “简单函数”包括有理函数、指数函数、对数函数和三角函数与反三角函数。

计算定积分的命令和计算不定积分是同一个Integrate函数，在计算定积分时，除了要给出变量外还要给出积分的上下限。当定积分算不出准确结果时，用N[%]命令总能得到其数值解.Nintegrate也是计算定积分的函数,其使用方法和形式和Integrate函数相同.用Integrate函数计算定积分得到的是准确解,Nintegrate函数计算定积分得到的是近似数值解.计算多重积分时,第一个自变量相应于最外层积分放在最后计算. 

### 解方程

```
Solve[eqns, vars] 从方程组eqns中解出vars 
Solve[eqns, vars, elims] 从方程组eqns中削去变量elims,解出vars 
DSolve[eqn, y, x] 解微分方程，其中y是x的函数 
DSolve[{eqn1,eqn2,...},{y1,y2...},x]解微分方程组，其中yi是x的函数 
DSolve[eqn, y, {x1,x2...}] 解偏微分方程 
Eliminate[eqns, vars] 把方程组eqns中变量vars约去 
SolveAlways[eqns, vars] 给出等式成立的所有参数满足的条件 
Reduce[eqns, vars] 化简并给出所有可能解的条件 
LogicalExpand[expr] 用&&和||将逻辑表达式展开 
InverseFunction[f] 求函数f的逆函数 
Root[f, k] 求多项式函数的第k个根 
Roots[lhs==rhs, var] 得到多项式方程的所有根 
```

### 代数运算

```
Expand[expr] 展开表达式 
Factor[expr] 展开表达式 
Simplify[expr] 化简表达式 
FullSimplify[expr] 将特殊函数等也进行化简 
PowerExpand[expr] 展开所有的幂次形式 
ComplexExpand[expr,{x1,x2...}] 按复数实部虚部展开 
FunctionExpand[expr] 化简expr中的特殊函数 
Collect[expr, x] 合并同次项 
Collect[expr, {x1,x2,...}] 合并x1,x2,...的同次项 
Together[expr] 通分 
Apart[expr] 部分分式展开 
Apart[expr, var] 对var的部分分式展开 
Cancel[expr] 约分 
ExpandAll[expr] 展开表达式 
ExpandAll[expr, patt] 展开表达式 
FactorTerms[poly] 提出共有的数字因子 
FactorTerms[poly, x] 提出与x无关的数字因子 
FactorTerms[poly, {x1,x2...}] 提出与xi无关的数字因子 
Coefficient[expr, form] 多项式expr中form的系数 
Coefficient[expr, form, n] 多项式expr中form^n的系数 
Exponent[expr, form] 表达式expr中form的最高指数 
Numerator[expr] 表达式expr的分子 
Denominator[expr] 表达式expr的分母 
ExpandNumerator[expr] 展开expr的分子部分 
ExpandDenominator[expr] 展开expr的分母部分 
ExpandDenominator[expr] 展开expr的分母部分 

TrigExpand[expr] 展开表达式中的三角函数 
TrigFactor[expr] 给出表达式中的三角函数因子 
TrigFactorList[expr] 给出表达式中的三角函数因子的表 
TrigReduce[expr] 对表达式中的三角函数化简 
TrigToExp[expr] 三角到指数的转化 
ExpToTrig[expr] 指数到三角的转化 
RootReduce[expr] 
ToRadicals[expr]
```

#### 矩阵的运算符号和函数

```
A+c A为矩阵,c为标量,c与A中的每一个元素相加 
A+B A,B为同阶矩阵或向量,A与B的对应元素相加 
cA A为矩阵,c为标量,c与A中的每个元素相乘 
U.V 向量U与V的内积 
A.B 矩阵A与矩阵B相乘,要求A的列数等于B的行数 
Det[M] 计算矩阵M的行列式的值 
Transepose[M] M的转置矩阵( 或 ) 
Inverse[M] 计算矩阵M的逆矩阵( ) 
Eigenvalus[A] 计算矩阵A的全部(准确解)特征值 
Eigenvalus[N[A]] 计算矩阵A的全部(数值解)特征值 
Eigenvectors[A] 计算矩阵A的全部(准确解)特征向量 
Eigenvectors[N[A]] 计算矩阵A的全部(数值解)特征向量 
Eigensystem[A] 计算矩阵A的所有(准确解)特征值和特征向量 
Eigensystem[N[A]] 计算矩阵A的所有(数值解)特征值和和特征向量 
```



