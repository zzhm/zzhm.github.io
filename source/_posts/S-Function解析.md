---
title: S-Function解析
mathjax: false
date: 2018-08-30 16:34:36
id: S-Function
tags:
- simulink
- 控制
- matlab
categories:
- 教程
---

S函数即系统函数System Function的意思，为什么要使用S函数呢？是因为在研究中，有时需要用到复杂的算法设计等，而这些算法因为其复杂性不适合用普通的Simulink模块来搭建，即matlab所提供的Simulink模块不能满足用户的需求，需要用编程的形式设计出S函数模块，将其嵌入到系统中。如果恰当地使用S函数，理论上，可以在Simulink下对任意复杂的系统进行仿真。

<!---more--->

S函数具有固定的程序格式，用matlab语言可以编写S函数，此外还允许用户使用C、C++、Fortran和Ada等语言进行编写，用非matlab语言进行编写时，需要采用编译器生成动态链接库DLL文件。在主窗口中输入sfundemos，或者点击Simulink->User-Defined Functions->S-Function Examples，即可出现如图1所示的界面，可以选择对应的编程语言查看演示文件。

Matlab为了用户使用方便，有一个S函数的模板sfuntmpl.m，一般来说，我们仅需要在sfuntmpl.m的基础上进行修改即可。在主窗口输入edit sfuntmpl即可出现模板函数的内容，可以详细地观察其帮助说明以便更好地了解S函数的工作原理。

模板函数的定义形式为function[sys,x0,str,ts]=sfuntmpl(t,x,u,flag)，一般来说，S函数的定义形式为[sys,x0,str,ts]=sfunc(t,x,u,flag,p1,…Pn)，其中的sfunc为自己定义的函数名称，以上参数中，t、x、u分别对应时间、状态、输入信号，flag为标志位，其取值不同，S函数执行的任务和返回的数据也是不同的，pn为额外的参数，sys为一个通用的返回参数值，其数值根据flag的不同而不同，x0为状态初始数值，str在目前为止的matlab版本中并没有什么作用，一般str=[]即可，ts为一个两列的矩阵，包含采样时间和偏移量两个参数，如果设置为[0 0]，那么每个连续的采样时间步都运行，[-1 0]则表示按照所连接的模块的采样速率进行，[0.25 0.1]表示仿真开始的0.1s后每0.25s运行一次，采样时间点为TimeHit=n*period+offset。 

S函数的使用过程中有2个概念值得注意：

1、direct feedthrough，系统的输出是否直接和输入相关联，即输入是否出现在输出端的标志，若是为1，否则为0，一般可以根据在flag=3的时候，mdlOutputs函数是否调用输入u来判断是否直接馈通。

2、dynamically sized inputs，主要给出连续状态的个数、离散状态的个数、输入数目、输出数目和直接馈通否。 

采样时间ts

仿真步长就是整个模型的基础采样时间，各个子系统或模块的采样时间，必须以这个步长为整数倍。连续信号和离散信号对计算机而言其实都是采样而来的，只是采样时间不同，连续信号采样时间可认为趋于0且基于微分方程，离散信号采样时间比较长基于差分方程。离散信号当前状态由前一个时刻的状态决定，连续信号可以通过微分方程计算得到。如果要将连续信号离散化还要考虑下信号能否恢复的问题，即香农定理。

采样时间点的确定：下一个采样时间=（n*采样间隔）+ 偏移量，n表示当前的仿真步，从0开始。对于连续采样时间，ts可以设置为[0 0]，其中偏移量为0；对于离散采样时间，ts假设为[0.25 0.1]，表示在S-函数仿真开始后0.1s开始每隔0.25s运行一次，当然每个采样时刻都会调用mdlOutPuts和mdlUpdate函数；对于变采样时间，即离散采样时间的两次采样时间间隔是可变的，每次仿真步开始时都需要用mdlGetTimeNextVarHit计算下一个采样时间的时刻值。ts可以设置为[-2 0]。对于多个任务，每个任务都可以以不同的采样速率执行S-函数，假设任务A在仿真开始每隔0.25s执行一次，任务B在仿真后0.1s每隔1s执行一次，那么ts设置为[0.25 0.1;1.0 0.1]，具体到S-函数的执行时间为[0 0.1 0.25 0.5 0.75 1.0 1.1…]。如果用户想继承被连接模块的采样时间，ts只要设置为[-1 0]。

在实际仿真过程中，Simulink会自动将flag设置为0，进行初始化过程，然后将flag的数值设置为3，计算模块的输出，一个仿真周期后，Simulink将flag的数值先后设置为1和2，更新系统的连续和离散状态，再将其设置为3，计算模块的输出，如此循环直至仿真结束条件满足。 

```matlab
function [sys,x0,str,ts,simStateCompliance] = sfuntmpl_c(t,x,u,flag)

%%%%Simulink中s函数模板的翻译版
%[sys,x0,str,ts,simStateCompliance] = sfuntmpl(t,x,u,flag，p1,…pn)

%在主窗口中输入sfundemos，或者点击Simulink->User-Defined Functions->S-Function Examples
%sfuntmpl 自定义函数名,p1,…pn自定义参数
% t、x、u分别对应时间、状态、输入信号，flag为标志位，其取值不同，S函数执行的任务和返回的数据也是不同的
%在实际仿真过程中，Simulink会自动将flag设置为0，进行初始化过程，然后将flag的数值设置为3，计算模块的输出，一个仿真周期后，Simulink将flag的数值先后设置为1和2，更新系统的连续和离散状态，再将其设置为3，计算模块的输出，如此循环直至仿真结束条件满足。 

% flag result 描述 
% 0 [sizes,x0,str,Ts] 调用mdlInitializeSizes函数，初始化，返回SYS的大小，初始状态x0,str,采样时间Ts 
% 1 DX 调用mdlDerivatives函数，进行连续状态变量的更新，返回连续状态微分SYS. 
% 2 DS 更新离散状态 SYS = X(n+1) 
% 3 Y  调用mdlOutputs函数，求取系统的输出信号。返回输出SYS. 
% 4 TNEXT 调用mdlGetTimeOfNextVarHit函数，计算下一仿真时刻，由sys返回R. 
% 5 Reserved for future (root finding). 
% 9 [] 结束 终止仿真过程，调用mdlTerminate函数。 perform any cleanup SYS=[].

% 当flag=0时，以下信息必须赋值回传 
% SYS(1) = 连续状态个数  sizes.NumContStates = 0;
% SYS(2) = 离散状态个数  sizes.NumDiscStates = 0; 
% SYS(3) = 输出量个数    sizes.NumOutputs = 0;
% SYS(4) = 输入量个数 注：上述4个变量可以赋值为-1，表示其值可变  sizes.NumInputs = 0; 
% SYS(5) = 保留值。为0.  
% SYS(6) = 直接馈通标志(1=yes, 0=no).如果u在flag=3时被使用，说明S函数是直接馈通，赋值为1. 否则为0
%                                   sizes.DirFeedthrough = 1; 
% SYS(7) = 采样时间个数，Ts的行数     sizes.NumSampleTimes = 1;

% X0 = 初始状态。没有则赋值为[].除flag=0外，被忽略。 
% STR = 系统保留，设为[]. 
% TS = m*2 矩阵。（采样周期，偏移量）如果设置为[0 0]，那么每个连续的采样时间步都运行 
% TS = [0 0] : 连续采样 ,比如[0 1]: 在1个Ts后连续采样;
% PERIOD OFFSET, : Discrete sample time where 
% PERIOD > 0 & OFFSET < PERIOD. 
% [-2 0]; : 变步长离散采样， 
% flag=4用于决定下一个采样时刻 
% 注： 
% 若希望每个时间步都运行，则设Ts=[0,0] 
% 若希望继承采样时间运行，则设Ts=[-1,0] 
% 若希望继承采样时间运行，且希望在微步内不变化，应该设Ts=[-1,1] 
% 若希望仿真开始0.1s后每隔0.25秒运行，则设Ts=[0.25,0.1] 
% 若希望按照不同速率执行不同任务，则Ts应按照升序排列。 
% 即：每隔0.25秒执行一个任务，同时在开始0.1秒后，每隔1秒执行另一个任务 
% Ts=[0.25,0; 1.0,0.1],则simulink将在下列时刻执行s函数[0,0.1,0.25,0.5,0.75,1,1.1,…]

% 以下是S函数的主函数 
switch flag, 
case 0, % 初始化 
[sys,x0,str,ts,simStateCompliance]=mdlInitializeSizes;
% // 解释说明
% flag=0表示当前处于初始化状态，此时调用函数mdlInitializeSizes进行初始化，此函数在该文件的第149行定义. 其中的参数sys是一个结构体，它用来设置模块的一些参数。

case 1, % 连续时间导数 
sys=mdlDerivatives(t,x,u);

% flag=1表示此时要计算连续状态的微分, 即上面提到的dx/dt=fc(t,x,u)中的dx/dt,
% 找到193行的函数mdlDerivatives, 如果设置连续状态变量个数为0, 此处只需sys=[]
% 就可以了, 按我们上述讨论的那个模型, 此处改成 sys=fc(t,x(1),u)或sys=A*x(1)+B*u, 
% 我们这儿x(1)是连续状态变量, 而x(2)是离散的, 这儿只用到连续的, 此时的输出sys就是

case 2, % 更新离散状态量 
sys=mdlUpdate(t,x,u);

%flag=2表示此时要计算下一个离散状态, 即上面提到的x(k+1)=fd(t,x,u), 找到mdlUpdate函数, 它这儿sys=[]表示没有离散状态, 我们这儿可以改成sys=fd(t,x(2),u)或sys=H*x(2)+G*u;%sys即为x(k+1)

case 3, % 计算输出 
sys=mdlOutputs(t,x,u);

%flag=3表示此时要计算输出, 即y=fo(t,x,u), 找到218行的mdlOutputs函数. 如果sys=[]表示没有输出, 我们改成sys=fo(t,x,u)或sys=C*x+D*u %sys此时为输出y

case 4, % 计算下一步采样时刻 
sys=mdlGetTimeOfNextVarHit(t,x,u);

%flag=4表示此时要计算下一次采样的时间, 只在离散采样系统中有用(即上文的mdlInitializeSizes中提到的ts设置ts(1)不为0), 连续系统中只需在mdlGetTimeOfNextVarHit函数中写上sys=[]. 这个函数主要用于变步长的设置, 具体实现大家可以用edit vsfunc看vsfunc.m这个例子

case 9, % 结束仿真 
sys=mdlTerminate(t,x,u);

%flag=9表示此时系统要结束，一般来说写上在mdlTerminate函数中写上sys=[]就可, 如果你在结束时还要设置什么，就在此函数中写完了.

otherwise % 未知flag值 
DAStudio.error('Simulink:blocks:unhandledFlag', num2str(flag)); 
end % S函数主程序结束

%============================================================================= 
% mdlInitializeSizes 
% 返回s函数的sizes、初始条件、采样时刻 
%============================================================================= 
function [sys,x0,str,ts,simStateCompliance]=mdlInitializeSizes 
% 调用simsizes函数为sizes结构赋值 
% simsizes函数是S函数模块特有的。它的结构和代码是固定的。

% size = simsizes;%用于设置模块参数的结构体用simsizes来生成 
% sizes.NumContStates = 0; %模块连续状态变量的个数 
% sizes.NumDiscStates = 0; %模块离散状态变量的个数 
% sizes.NumOutputs = 0; %模块输出变量的个数 
% sizes.NumInputs = 0; %模块输入变量的个数 
% sizes.DirFeedthrough = 1; %模块是否存在直接贯通
% sizes.NumSampleTimes = 1; %模块的采样时间个数, 至少是一个 
% sys = simsizes(sizes); %设置完后赋给sys输出
% 举个例子，考虑如下模型:
% dx/dt=fc(t,x,u) 也可以用连续状态方程描述：dx/dt=A*x+B*u
% x(k+1)=fd(t,x,u) 也可以用离散状态方程描述：x(k+1)=H*x(k)+G*u(k)
% y=fo(t,x,u) 也可以用输出状态方程描述：y=C*x+D*u
% 设上述模型连续状态变量、离散状态变量、输入变量、输出变量均为1个，我们就只需改上面那一段代码为(一般连续状态与离散状态不会一块用, 我这儿是为了方便说明):sizes.NumContStates=1;sizes.NumDiscStates=1;sizes.NumOutputs=1;sizes.NumInputs=1;
% 其他的可以不变。
% x0 = []; %状态变量设置为空，表示没有状态变量，以我们上面的假设，可改为x0=[0,0](离散和连续的状态变量我们都设它初值为0)

x0 = 0; % 状态初始化 
str = []; % str 始终为空 
ts = [0 0];% 初始化采样时间

% 指定simStateCompliance的值. 
% ‘UnknownSimState’, < 默认值; warn and assume DefaultSimState 
% ‘DefaultSimState’, < Same sim state as a built-in block 
% ‘HasNoSimState’, < No sim state 
% ‘DisallowSimState’ < Error out when saving or restoring the model sim state 
simStateCompliance = 'UnknownSimState'; 
% 子函数mdlInitializeSizes 结束

%============================================================================= 
% mdlDerivatives 
% 返回连续状态量的导数 
%============================================================================= 
function sys=mdlDerivatives(t,x,u)

sys = [];

% 子函数mdlDerivatives结束

%============================================================================= 
% mdlUpdate 
%更新离散时间状态，采样时刻和主时间步的要求。 
%============================================================================= 
function sys=mdlUpdate(t,x,u)

sys = []; 
% 子函数 mdlUpdate 结束

%============================================================================= 
% mdlOutputs 
% 计算并返回模块输出量 
%============================================================================= 
function sys=mdlOutputs(t,x,u)

sys = [];

% 子函数 mdlOutputs 结束

%============================================================================= 
% mdlGetTimeOfNextVarHit 
% 返回下一个采样时刻。注意返回结果是一个绝对时间，只在Ts=[-2,0]时使用。 
%============================================================================= 
function sys=mdlGetTimeOfNextVarHit(t,x,u)

sampleTime = 1; % 例子。设置下一个采样时刻为1s后。 
sys = t + sampleTime;

% 子函数 mdlGetTimeOfNextVarHit 结束

%============================================================================= 
% mdlTerminate 
% 仿真结束 
%============================================================================= 
% 
function sys=mdlTerminate(t,x,u)

sys = [];

% 子函数 mdlTerminate结束
```

