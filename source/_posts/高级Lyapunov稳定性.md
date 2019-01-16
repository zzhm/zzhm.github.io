---
title: 高级Lyapunov稳定性
mathjax: true
date: 2018-06-28 20:20:14
id: Lyapunov-stability-advanced
tags:
- 稳定性
- 控制
- 学习
categories:
- 学习
- 控制
---
## 基本概念

### 函数及其导数的渐进性质

- $\dot{f( t)}\rightarrow 0 \nRightarrow f( t)$收敛 

几何上，导数趋近于零意味着切线越来越平，但是并不意味着函数收敛。比如$f( t) =sin( Ln( t))$，$f( t) =\sqrt{t} sin( Ln( t))$

- $f( t)$收敛$\nRightarrow\dot{f( t)}\rightarrow 0$，比如$f( t) =e^{-t} sin^{2}\left( e^{2t}\right)$



说明：可微函数一致连续的充分条件是其导数有界

<!---more--->

### Barbalat引理

如果可微函数$f(t)$(一阶连续可导)，当$t\rightarrow\infty$时存在有界极限，且$\dot{f( t)}$一致连续，则$t\rightarrow\infty$时$\dot{f( t)}\rightarrow 0$

#### 推论1

如果可微函数 $f( t) $(一阶连续可导)，当$t\rightarrow \infty$时存在有界极限，且$f( t)$的二阶导数存在且有界，则$t\rightarrow \infty$时$\dot{f( t)}\rightarrow 0$

#### 推论2

如果函数 $f( t) $一致连续，并且$\lim_{t\rightarrow\infty}\int^{t}_{0} f( x) dx$存在且有界，那么 $\lim_{t\rightarrow \infty } f( t) =0$

### Barbalat引理扩展

Barbalat引理不易与Lyapunov理论相结合，故在实际应用中具有一定的局限性，为了对Barbalat基本形式进行延展和变形，得到如下几种Barbalat引理的表达式

$$L_{P} =\left\{f\ |\ f:[ 0,\infty ]\rightarrow R,\left(\int ^{\infty }_{0} |f( t) |^{p} dt\right)^{\frac{1}{p}} < \infty \right\} ,p\in [ 1,\infty ]$$

#### 引理1

若函数 $f( t)$ 一致连续，且存在 $p\in [ 1,\infty ]$，使得 $f( t) \in L_{P} $，则 $d\lim _{t\rightarrow \infty } f( t) =0$

以下形式的Barbalat引理因易与Lyapunov理论建立直接的联系，故在自适应控制和参数估计等领域得到了广泛的应用 

#### 引理2

设 $f(t)$ 平方可积，即 $\lim_{t\rightarrow \infty }\int ^{t}_{0} |f( t) |^{2} dt< \infty$，则如果$ \dot{f( t)}$ 存在且有界，那么 $\lim_{t\rightarrow \infty } f( t) =0$

适应性更广泛的引理 

#### 引理3

如果 $f( t) \in L_{P}，p\in [ 1,\infty ]$，且$\dot{f( t)}$ 存在且有界，那么 $\lim _{t\rightarrow \infty } f( t) =0$

### Barbalat引理在分析稳定性中的应用

Lyapunov稳定性定理虽然在实际系统稳定性分析和理论研究中得到了广泛的应用，但是应用该定理分析系统的渐进稳定性时，导数为负定的Lyapunov函数时有时难以找到，尽管LaSalle不变集原理可以处理Lyapunov函数的导数为半负定的情况，但是只适用于自治系统 

Barbalat引理弥补了Lyapunov稳定性定理和Lasalle不变集原理的不足，在分析非自治系统稳定性方面起到了十分关键的作用

#### 引理

如果连续可导的二元函数$V:R^{n} \times [ 0,\infty )\rightarrow R$有下界，$\dot{V}( x,t)$ 半负定，且 $\dot{V}( x,t)$关于时间 t 是一致连续的，那么 $\lim_{t\rightarrow \infty }\dot{V}( x,t) =0$

类Lyapunov引理

如果存在标量函数，满足 
1. $V(x,t)$有下界 
2. $\dot{V}(x,t)$半负定 
3. $\dot{V}(x,t)$对时间一致连续

则当$t\rightarrow 0$，$\dot{V}( x,t)\rightarrow 0$

补充说明

函数有极限，则函数比有界，但是函数有界并不代表函数有极限。有极限说明函数最终会趋于一定定值，有界表示函数不会趋于无穷大，但不一定会趋于一个定值，可以在某些位置上来回波动

例子
考虑如下系统

$$\begin{cases} \dot{x}_{1} =-x_{1} +x_{2} w( t) & \\\dot{x}_{2} =-x_{1} w( t) &\end{cases}$$

$w( t)$为有界函数
选取Lyapunov函数 $V=x^{2}_{1} +x^{2}_{2}$，则$\dot{V} =2x_{1}[ -x_{1} +x_{2} w( t)] +2x_{2}[ -x_{1} w( t)]=-2x^{2}_{1}\leq 0$

由于 $\dot{V} \ \leq 0$，因此$\underset{t\geq 0}{sup} V( t) \leq V( 0)$，且 $V\geq 0$ ，因此 $V=x^{2}_{1} +x^{2}_{2}$有界，从而推得$x_{1} ,x_{2}$为有界的。

$\ddot{V} =-4x_{1}( -x_{1} +x_{2} w)$中$w( t), x_{1}, x_{2}$均为有界的，因此$\ddot{V}$为有界的，所以 $\dot{V}$一致连续，因此 $\dot{V}( x,t)\rightarrow 0$
由于$\dot{V} =-2x^{2}_{1}$，所以推得 $x_{1}\rightarrow0$

虽然推得$ x_{1}$ 最终收敛于0，但是整个系统不是渐进稳定的，因为上述推导，只能推得 $x_{2}$ 为有界的，并不能保证$x_{2}$ 的收敛性