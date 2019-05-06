---
title: EDEM快速填充颗粒的方法
mathjax: false
date: 2019-03-06 16:07:46
id: edem-particles
tags:
- edem
- 离散元
- 学习
- api开发
categories:
- 学习
- 离散元
---

利用离散元方法做仿真实验的过程中，所用的模型并非都是单一的颗粒体，很多时候要用到颗粒群模型。小体积的模型可以用聚合法将多个颗粒填充在颗粒模板里面，从而组成所需要的非规则模型。然而，大体积的模型通过聚合法逐个布置颗粒位置显然是工作量相当大的一种做法。本文简介两种快速生成颗粒群的方法，以供交流学习。

<!---more--->

一种利用fluent中udf库文件进行快速填充的方法，这种方法针对结构化网格适用性很强，可以很方便控制颗粒粒径，而对于非结构化网格就相对很尴尬，粒径不好控制。

## 一、快速填充模型

### 基本思路

- 建立模型，划分网格。利用网格前处理软件对模型区域划分网格，另存为“.msh”文件。（网格划分软件Gambit、ICEM CFD、Ansys等）

- Fluent加载udf库文件，获取网格坐标信息。将生成的`.msh`导入fluent，加载udf库文件，编译源文件`CalcRadius.c`，最后执行`CalcRadiusVolume`，会在文件夹里面生成`point.txt`网格坐标文件。

- 对网格坐标信息进行编辑，准备颗粒工厂dll文件。将`point.txt`里面的数据粘贴进`Block_Factory_Data.txt`文件，覆盖原来数据。

- 进入edem设置模型参数，并在Factory面板加载通过`VC++`编译好的`BlockFactory_x64.dll`文件。

- Edem中进行快速填充。进行仿真填充。

（如需利用填充好的颗粒模型做类似三轴应力压缩、切割、破碎实验，在后处理面板导出填充好的模型即可使用，此时请务必将时间置0）

### 操作步骤

下面以一个立方体为例进行操作说明：

本文利用Ansys workbench进行建模，划分网格。

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72Xy2Kkof5f&690.jpg)

#### 建模与网格划分

在Component Systems找到Mesh模块，拖动到右侧区域，然后双击Geometry模块。

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72Xy5A2Nlab&690.jpg)

建立一个`40x40x20mm`的立方体。之后保存，打开meshing模块。

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72Xy7uRhL21&690.jpg)



Meshing模块中左侧单击mesh，在下方明细表中选择Fluent求解器，CFD特性，并设置最大、最小网格尺寸都为4mm，之后对模型进行自动网格划分，生成结构网格；

#### 导出msh文件

在Geomtry里点击实体，设置模型材料为fluid，导出msh文件。

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72XyjJRnXe9&690.jpg)

#### 编译接口文件

打开`GUI_compilation.exe`，设置相应版本

![1551880388956](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551880388956.png)

#### 加载耦合接口文件

打开fluent，依次选择`file->Read->Journal..`，载入`“load_edem_coupling.jou”`(耦合2.0接口，耦合1.0接口依次选择`Define->User Defined->Fuctions->Complied`载入udf库文件路径)

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72Xyn1Bjq30&690.jpg)

#### 编译udf文件

依次选择`file->Read->Mesh`，读入msh文件，并对`.c`的udf文件进行编译。`User Defined->Functions->Compiled->add`,载入`CalcRadius.c`文件，点Build,在信息提示窗口无错误提示下最后Load。

![1551923055983](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551923055983.png)

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72XyoDHsb47&690.jpg)

#### 计算坐标信息

在`User Defined`面板点`Execute on Demand`,在弹出的窗口里选择`CalcRadiusVolume`,执行后会在`CalcRadius.c`文件夹中生成一个`point.txt`文件，里面便是网格的坐标信息。如下图。

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551923011110.png)

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72Xyx5vFadc&690.jpg)

#### 修改`point.txt`

对`point.txt`文件里最后一列数字全部替换为1.（最后一列是颗粒粒径比例）

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72XyCwkYGe2&690.jpg)

#### 拷贝数据

将`point.txt`中的坐标信息拷贝在`Block_Factory_Data.txt中`，其中第一行是颗粒填充开始时间，第二行是总体的颗粒数量，也就是网格坐标信息数量。

![关于EDEM中快速填充一定区域的操作步骤简介](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/002l9cF3zy72XyIhiPn71&690.jpg)

#### EDEM仿真

新建一个EDEM文件，在几何体面板导入`.msh`文件，在全局面板设置颗粒材料跟几何体材料参数，在颗粒面板设置粒径大小（半径2 mm）,在颗粒工厂面板读入`Block_Factory_Data.dll文件`。最后设置风格单元大小及时间步长进行计算，填充完成效果如上图。

> 需要特别注意的问题：
>
> 1.txt文件里颗粒名称（第一列的字符）要与颗粒面板中设置的颗粒名称相同。
>
> 2.需要在EDEM里面设置自定义颗粒插件的文件夹。虽然把dll文件放入项目所在的文件夹也能导入插件，但是在运行的时候会出错，直接退出。
>
> 3.注意划分的网格的默认单位是米，因此在导入`.msh`模型的时候单位应当选择米，这一点与导入CAD模型有所差异（此处巨坑！！）。主要网格尺寸、edem导入尺寸、颗粒尺寸的单位。
>
> 4.直接打开Fluent和从Ansys里的Fluent模块打开并不一样，应当直接打开。（此处也巨坑）
>
> 5.如果没生成颗粒，或者生成颗粒瞬间炸开了，将仿真的Time Step 改小点！（此处也巨坑）

>在一定的仿真条件下，粒子的速度可能会变得过大，导致周围粒子的行为不规律:例如，仿真时间步长过大。有两种方法可以帮助解决这个问题。粒子速度可以限制在指定的极限，也可以从模拟中去除超过该极限的粒子。粒子速度和角速度可以分别处理。

### 制作颗粒模板

#### 导出xml模板文件

> xml文件是记录仿真配置和状态的文档，之所以要仿真时间归0，因为如果不是0，会包含很多仿真的运算结果，而我们只是单纯的想填充颗粒。

仿真时间归0，切换到`分析`选型卡，`File->Export`，选择输出`Simulation Deck`文件，输出文件的后缀名需为`.xml`。`Export Options` 里面只勾选`Particle Data`，点击OK完成数据导出。

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551935714644.png)

![Export Options](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551935764440.png)

#### 导出结果数据文件

> 如果在Tools->Options里面改过单位的话，记得改回国际单位制，引入貌似导入后默认是国际单位制的。

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551941538343.png)

仿真时间归0，切换到`分析`选型卡，`File->Export`，选择输出`Result Data`文件，设置Filename（图中为`0512.csv`），General选项卡中 Time Steps 选择从1到1（这里1是仿真完成的时间）。

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551936470265.png)

在Queries选项卡里设置需要导出的内容。点击图中+号增加导出项目；在下方选择导出变量，导出变量有分量的在下方的Component里面选取；右侧Type里面选择particle；选择完成后点击左下角Export导出数据。

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551936866395.png)

#### 修改`.xml`文件

在EXCEL里面将数据按照下述格式进行组合，最终效果见图

><sphere y="0" name="sphere 0" x="0" id="0" z="0" contact_radius="0.002" physical_radius="0.002"/>

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551939125636.png)

将数据复制粘贴到上述的`.xml`格式文件中，

修改前

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551939226475.png)

修改后

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0imp/1551939382214.png)



#### 使用方法

在设置颗粒的时候使用快捷键`Ctrl+i`,选择上述的`.xml`文件即可。

## 二、颗粒替换

- 建立颗粒模板，用颗粒填充，（利用模型体积除单个颗粒体积得到所要生成的颗粒数量）导出位置信息并规整格式。

- Api读取颗粒模板数据。

- 替换原始颗粒为新颗粒群，此时用到`ParticleReplacement_v2_x64.dll`（已编译完成）文件。

- Bonding 模型触发产生粘结。

以上两种方法思路有所同，又有所不同。第一种方法利用Api实现快速填充，适合一些关于大块物料破碎类仿真。  第二种方法利用Api实现单个颗粒快速替换为颗粒群，适合小块物料破碎类仿真。

## 参考资料

[海基龚明教程](https://v.youku.com/v_show/id_XNzM5OTkzNTI0.html?spm=a2h0k.11417342.soresults.dtitle)

海基杨格

[关于EDEM中快速填充一定区域的操作步骤简介](http://blog.sina.com.cn/s/blog_7fd679e90102x7bm.html)

[浅析EDEM中两种快速生成颗粒群的方法](http://blog.sina.com.cn/s/blog_7fd679e90102wtkh.html)