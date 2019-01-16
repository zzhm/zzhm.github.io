---
title: Matlab 2017a与Visual Studio 2015混编环境配置
mathjax: false
date: 2018-08-27 14:48:56
id: opencv342-vs2015-matlab2017
tags:
- 视觉
- 学习
categories:
- 学习
- 视觉
---

## 一、程序安装

- 先安装Visual Studio 2015，安装选项选择自定义，勾选编程语言C++，（默认是不安装C++的编译器的，因此如果不勾选，后面找不到编译器）
- 然后安装Matlab 2017a ，没有特别注意的事情
- 如果是先安装的matlab，若matlab找不到编译器，可以重新安装一下matlab的主程序
- 安装opencv 3.42，使用vs，直接下载编译好的文件即可

<!----more--->

## 二、Visual Studio 2015环境配置

我们知道要在VS中使用外部的类库的话，需要进行引入的一下配置，这个配置就包括：外部库目录指定和外部包含文件指定。

- 打开VS 2015，新建一个空白的win32的控制台工程：  
- 选择语言为C++，Win32类型中的控制台工程，并设置工程名称：
- 指定建立的工程为空白工程：
- 建立完工程之后，我们选中解决方案栏中的Resource Files目录（即源码目录），然后新建一个C++源码文件：
- 设置源码的文件名，例如：Main，然后创建此源码文件到工程中： 

- 在VS中有个叫做“属性管理器”的工具，用于进行VS整体参数的配置，配置一次之后，以后所有新建项目都能应用改配置，不用再一一进行配置操作，使用起来也非常方便。点击工具栏中的：`View—>Other Windows—>Property Manger`打开属性管理器：

- 在新出现的属性管理器栏中，展开目录，选中`Debug|Win64`中的`Microsoft.Cpp.x64.user`，并右键点击属性（Properties）进入属性界面：

1）配置包含目录：

在通用属性`（Common Properties）—>VC ++目录—>包含目录`，然后点击右侧三角标志选中Edit进入编辑：

向其中添加下面三个路径：

```
E:\OpenCV\opencv\build\include
E:\OpenCV\opencv\build\include\opencv
E:\OpenCV\opencv\build\include\opencv2
```

2）配置库文件目录：

- 完成上面的包含目录配置之后，我们还需要进行库文件的配置：回到属性界面，选择包含目录下面的`Library Directories（库文件目录）`：

- 向库文件目录下添加OpenCV的库文件目录：`E:\OpenCV\opencv\build\x64\vc14\lib`，这个目录根据每个人自己在第一步安装OpenCV中选择的目录进行选定

3）配置动态链接库：

- 我们可以查看步骤2）中添加的库文件目录下面.lib文件列表，发现在3.1.0版本的OpenCV中，仅剩下两个库文件，分别是：`opencv_world310.lib`和`opencv_world310d.lib`，这里两个库文件的区别就是：`opencv_world310.lib`是Release模式版本，而`opencv_world310d.lib`是Debug模式版本：

- 跟上述两个步骤相似，在属性界面中打开`Linker(链接库)—>Input(输入)—>Additional Dependencies(添加依赖)`：

- 将我们刚刚在OpenCV库文件目录下看到的两个库文件其中一个添加到这里（根据模式需求Release模式或Debug模式）：

其实，对已经发行和未来即将发布的新版OpenCV，只需看`opencv\build\x86\vc10\lib`下的库是哪几个，添加成依赖项就可以了。

## 三、Matlab 环境配置

- 配置文件位置

在matlab中新建一个`helloworld.cpp`文件，输入命令`mex -v helloworld.cpp`命令来编译该文件。在控制台输出的详细信息中可以找到配置文件的位置：

`Options file:C:\Users\yufei\AppData\Roaming\MathWorks\MATLAB\R2016a\mex_C++_win64.xml`

于是，`mex_C++_win64.xml`就是我们要找的配置文件。

- 如何修改配置文件

在`mex_C++_win64.xml`的最后可以设置环境变量，我们需要修改的是环境变量的`path，include，lib，libpath`属性，各个属性具体值自行百度，下面是我修改好的配置文件。

```
<env       
PATH="原属性值;E:\download\opencv\build\x64\vc12\bin"      
INCLUDE="原属性值;E:\download\opencv\build\include;E:\download\opencv\build\include\opencv2;E:\download\opencv\build\include\opencv"      
LIB="原属性值;E:\download\opencv\build\x64\vc12\lib"      
LIBPATH="原属性值;E:\download\opencv\build\x64\vc12\lib" />
```

需要注意的是在设置xml属性的值时由于字符串太长可以自动切换，但是不能人为输入回车，否则会出错。出现“`fatal error C1083: 无法打开包括文件: “opencv2/opencv.hpp”: No such file or directory”`，请检查这一步。

- 添加相关库

`#pragma comment( lib, "opencv_world342.lib") `   %我只包含了这一个 `#pragma comment( lib, "opencv_ts300.lib")`

在`helloworld.cpp`中添加以上两行代码，可以增加需要的lib库，`opencv3.42`只需要包含上面两个库，不像之前版本需要包含一大堆。出现`“error LNK2019: 无法解析的外部符号”`,请检查这一步是否有问题。

- 注意编译平台选择

`mex -largeArrayDims -v helloworld.cpp`， `largeArrayDims` 指令意味着编译器采用64位平台，默认为32位平台。

## 四、混合编译

`mex -setup` 选择编译器

`mex XXXXX.cpp`  把这个cpp文件编译成库，生成的文件，32位系统中是mexw32，64位系统中是mexw64。

都是matlab专用，不是dll

`mex X1.cpp X2.cpp X3.cpp`生成的库名字叫X1

`mex -O X1.cpp` 大写O选项，优化编译，跑得嗷嗷快，以前都没发现呀

32位windows系统，matlab给我们赠送了编译器lcc，不用自己装。64位系统下 还要自己找，麻烦

在isomap里边有个dijkstra算法的cpp文件要编译，readme里边告诉我们要用

`mex -O dijkstra.cpp`

但是在64位系统里边是不行滴，一定要用

`mex -O -largeArrayDims dijkstra.cpp`

另外irs和jcs也不能用int * 类型，为了保证兼容性必须要用mwIndex *

都是因为稀疏矩阵的原因，稀疏矩阵在32位系统和64位系统下的下标类型是不一样滴

## 五、mexFunction

MEX文件的源代码一般由两部分组成：

- 计算过程。该过程包含了MEX文件实现计算功能的代码，是标准的C语言子程序。

- 入口过程。该过程提供计算过程与MATLAB之间的接口，以入口函数mxFunction实现。在该过程中，通常所做的工作是检测输入、输出参数个数和类型的正确性，然后利用mx-函数得到MATLAB传递过来的变量(比如矩阵的维数、向量的地址等)，传递给计算过程。

MEX文件的计算过程和入口过程也可以合并在一起。但不管那种情况，都要包含`#include "mex.h"`，以保证入口点和接口过程的正确声明。注意，入口过程的名称必须是mexFunction，并且包含四个参数，即：

`void mexFunction(int nlhs,mxArray *plhs[],int nrhs,const mxArray *prhs[])`

其中，参数nlhs和nrhs表示MATLAB在调用该MEX文件时等式左端和右端变量的个数，例如在MATLAB命令窗口中输入以下命令：

`[a,b,c]=Matlab_1(d,e,f,g)`

则nlhs为3，nrhs为4。

MATLAB在调用MEX文件时，输入和输出参数保存在两个mxArray*类型的指针数组中，分别为prhs[]和plhs[]。prhs[0]表示第一个输入参数，prhs[1]表示第二个输入参数，…，以此类推。如上例中，`d→prhs[0]，e→prhs[1]，f→prhs[2]，f→prhs[3]`。同时注意，这些参数的类型都是`mxArray *`。

接口过程要把参数传递给计算过程，还需要从prhs中读出矩阵的信息，这就要用到下面的mx-函数和mex-函数。

## 关于数据存储的说明

Matlab中的数据是按列存储的。例如，a=[1,2;3,4;5,6]，a的数据在内存中的存储顺序是：1、3、5、2、4、6。在C\C++中使用Matlab传来的变量时，一定要注意数据的存储顺序。

## 参考文献

VS和opencv配置：<https://www.cnblogs.com/linshuhe/p/5764394.html>

Matlab环境配置：<https://blog.csdn.net/zjsmdchen/article/details/78317366>

混合编程：<https://blog.csdn.net/weixin_41923961/article/details/81430607>

混合编程初探：<https://blog.csdn.net/bendanban/article/details/37830495#>

另外一种混合编程环境的配置思路：<https://github.com/kyamagu/mexopencv>