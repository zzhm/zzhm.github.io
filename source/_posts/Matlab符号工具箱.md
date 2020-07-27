---
title: Matlab符号工具箱
mathjax: false
date: 2018-06-29 14:25:38
id: matlab-symbol-toolbox
tags:
- matlab
- 数学
categories:
- 学习
- 数学
---

Matlab的符号数学工具箱可以完成几乎所有得符号运算功能。这些功能主要包括：符号表达式的运算，符号表达式的复合、化简，符号矩阵的运算，符号微积分、符号函数画图，符号代数方程求解，符号微分方程求解等。此外，工具箱还支持可变精度运算，既支持符号运算并以指定的精度返回结果。

<!---more--->

在此也仅仅列出函数的名称和功能，至于其参数设置，可借助Matlab的帮助系统，可参见`help-〉Symbolic Math Toolbox-〉Functions -- Categorical List`，这里有详细的列表。

## 一、符号表达式的运算

[n,d]=numden(a) 提取符号表达式a的分子和分母，并将其存放在n和d中

n=numden(a) 提取符号表达式a的分子和分母，只将分子存放在n中

symadd(a,b) 返回符号表达式a和b的和，也可直接用a+b

symsub(a,b) 返回符号表达式a和b的差，也可直接用a-b

symmul(a,b) 返回符号表达式a和b的积，也可直接用a*b

symdiv(a,b) 返回符号表达式a和b的商，也可直接用a/b

sympow(a,b) 返回符号表达式a的b次幂，也可直接用a^b

compose(f,g) 返回复合函数f(g(y))

compose(f,g,z) 返回自变量为z的复合函数f(g(z))

compose(f,g,x,z) 返回复合函数f(g(z))，并使x成为f函数的独立变量。即，如果f=cos(x/t)，则compose(f,g,x,z)返回复合函数cos(g(z)/t)，而compose(f,g,t,z)返回cos(x/g(z))

compose(f,g,x,y,z) 返回复合函数f(g(z))，并且使x与y分别成为f与g函数的独立变量。即如果f=cos(x/t)，g=sin(y/u)，compose(f,g,x,y,z)返回cos(sin(z/u)/t)，而compose(f,g,x,u,z)返回cos(sin(y/z)/t)

finverse(f) 返回符号函数f的反函数

finverse(f,v) 返回自变量为v的符号函数f的反函数

symsum(s) 返回 Σ?10)(xxs

symsum(s,v) 返回Σ ?10)(xvs

symsum(s,a,b) 返回Σ baxs)(

symsum(s,v,a,b) 返回Σ bavs)(

## 二、符号与数值间的转换以及符号的可变精度计算

numeric(p) 将符号表达式p转化为数值表达式

eval(p) 将符号表达式p转化为数值表达式

sym2poly(p) 将符号多项式p转换成它的Matlab等价系数向量

digit 察看现在系统中的算术运算精度

digit(n) 将系统的运算精度调整为小数点后n位

subs(f,new,old) f为符号表达式，new与old是字符、字符串或其他的符号表达式，new字符串将替换符号表达式f中的old字符串

## 三、符号表达式的化简

pretty(f) 将符号表达式化简成与高等数学课本上显示符号表达式形式类似

collect(f) 合并符号表达式的同类项

horner(f) 将一般的符号表达式转换成嵌套形式的符号表达式

factor(f) 对符号表达式进行因式分解

expand(f) 对符号表达式进行展开

simplify(f) 对符号表达式进行化简，它利用各种类型的代数恒等式，包括求和、积分、三角函数、指数函数以及Bessel函数等来化简符号表达式

simple(f) 对符号表达式尝试多种不同的算法进行化简，以显示长度最短的符号表达式简化形式

[r,how]=simple(f) 返回的r为符号表达式进行化简后的形式，how为所采用的简化方法

## 四、符号矩阵

transpose(A) 符号矩阵的转置

determ(A) 符号矩阵的行列式

det(A) 符号矩阵的行列式

inv(A) 符号矩阵求逆

rank(A) 符号矩阵求秩

[B,C]=eig(A) B为A的特征向量，C为A特征值

[B,C]=eigensys(A) B为A的特征向量，C为A特征值

svd(A) 返回A的奇异值

singvals(A) 返回A的奇异值

[B,C]=jordan(A) B为转换矩阵，其列是特征向量，C为约当标准型，它是特征值的对角矩阵，即其对角线元素是特征值

## 五、符号微积分

Limit(f,x,a) 返回符号表达式f当x趋向于a时的极限

Limit(f,a) 返回符号表达式f由findsym(f)返回独立变量趋向于a时的极限

Limit(f) 返回符号表达式f由findsym(f)返回独立变量在a=0时的极限

Limit(f,x,a,’right’) 右极限

Limit(f,x,a,’left’) 左极限

Diff(f) 返回f的微分

Diff(f,’a’) 对a变量求微分

Diff(f,n) 对f求n次微分

Diff(f,’a’,n) 对变量a求n次微分

int(f) 对f求不定积分

int(f,v) 对v变量求不定积分

int(f,a,b) 对f求[a,b]上的定积分

int(f,v,a,b) 对变量v求[a,b]上的定积分

## 六、符号函数画图

ezplot(f) 在默认区间-2*pi<x<2*pi绘制f=f(x)的函数图

ezplot(f,[a,b]) 在区间a<x<b上绘制f=f(x)的函数图

## 七、符号方程的求解

solve(f) 求解线性符号方程f

solve(f,g) 求解线性符号方程组f,g

fsolve(fun,x0) 求解非线性方程，x0为所求解方程的初始向量或矩阵，fun为所要求解的符号方程

dsolve(‘eqn1’,’eqn2’,…) 求解符号微分方程，参数eqn1,eqn2…代表微分方程与初始条件