---
title: python中的数学函数
mathjax: false
date: 2021-03-03 09:28:46
id: python-math
tags:
- 资源分享
categories:
- 实用教程
---

**不需要引入math模块的有：**

```python
abs(),cmp(),max(),min(),pow(),round()
```

**需要引入math模块的：**

三角函数，及其他数学函数，fabs(),

需要特别注意：

1、abs()是一个内置函数，而fabs()在math模块中定义的。
2、fabs()函数只适用于float和integer类型，而 abs() 也适用于复数。



- `math.ceil(x)`

返回x的上限，即大于或者等于x的最小整数。如果x不是一个浮点数，则委托 `x.__ceil__()`, 返回一个 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral) 类的值。

- `math.comb(n, k)`

返回不重复且无顺序地从  n  项中选择  k  项的方式总数。当 `k <= n` 时取值为 `n! / (k!   (n - k)!)`；当 `k > n` 时取值为零。也称为二项式系数，因为它等价于表达式 `(1 + x)^n` 的多项式展开中第 k 项的系数。如果任一参数不为整数则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。 如果任一参数为负数则会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。 

- `math.copysign(x,y)`

返回一个基于x的绝对值和  y  的符号的浮点数。在支持带符号零的平台上，`copysign(1.0, -0.0)` 返回  -1.0 .

- `math.fabs(x) `

返回x的绝对值。

- `math.factorial(x) `

以一个整数返回x的阶乘。 如果x不是整数或为负数时则将引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。 

- `math.floor(x) `

返回x的向下取整，小于或等于x的最大整数。如果x不是浮点数，则委托 `x.__floor__()` ，它应返回 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral) 值。

- `math.fmod(x,y)`

返回 `fmod(x, y)` ，由平台C库定义。请注意，Python表达式 `x % y` 可能不会返回相同的结果。C标准的目的是 `fmod(x, y)` 完全（数学上；到无限精度）等于 `x - n y` 对于某个整数  n  ，使得结果具有 与x相同的符号和小于 `abs(y)` 的幅度。Python的 `x % y` 返回带有  y  符号的结果，并且可能不能完全计算浮点参数。 例如， `fmod(-1e-100, 1e100)` 是 `-1e-100` ，但Python的 `-1e-100 % 1e100` 的结果是 `1e100-1e-100` ，它不能完全表示为浮点数，并且取整为令人惊讶的 `1e100` 。 出于这个原因，函数 [`fmod()`](https://docs.python.org/zh-cn/3/library/math.html#math.fmod) 在使用浮点数时通常是首选，而Python的 `x % y` 在使用整数时是首选。

- `math.frexp(x) `

以 `(m, e)` 对的形式返回x的尾数和指数。  m  是一个浮点数，  e  是一个整数，正好是 `x == m*2**e` 。 如果x为零，则返回 `(0.0,0)` ，否则返回 `0.5<=abs(m)<1` 。这用于以可移植方式“分离”浮点数的内部表示。

- `math.fsum(iterable)`

返回迭代中的精确浮点值。通过跟踪多个中间部分和来避免精度损失:

  ```python
  >>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) 
  0.9999999999999999 
  >>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) 
  1.0
  ```

该算法的准确性取决于IEEE-754算术保证和舍入模式为半偶的典型情况。在某些非Windows版本中，底层C库使用扩展精度添加，并且有时可能会使中间和加倍，导致它在最低有效位中关闭。有关待进一步讨论和两种替代方法，参见 [ASPN cookbook recipes for accurate floating point summation](https://code.activestate.com/recipes/393090/)。

- `math.gcd(integers)`

返回给定的整数参数的最大公约数。 如果有一个参数非零，则返回值将是能同时整除所有参数的最大正整数。 如果所有参数为零，则返回值为 `0`。 不带参数的 `gcd()` 返回 `0`。 3.5 新版功能.  在 3.9 版更改:  添加了对任意数量的参数的支持。 之前的版本只支持两个参数。

- `math.isclose(a,b,*, rel_tol=1e-09, abs_tol=0.0)`

若a和b的值比较接近则返回 `True`，否则返回 `False`。根据给定的绝对和相对容差确定两个值是否被认为是接近的。 rel_tol  是相对容差 —— 它是  a  和  b  之间允许的最大差值，相对于  a  或  b  的较大绝对值。例如，要设置5％的容差，请传递 `rel_tol=0.05` 。默认容差为 `1e-09`，确保两个值在大约9位十进制数字内相同。  rel_tol  必须大于零。 abs_tol  是最小绝对容差 —— 对于接近零的比较很有用。  abs_tol  必须至少为零。如果没有错误发生，结果将是： `abs(a-b) <= max(rel_tol   max(abs(a), abs(b)), abs_tol)` 。IEEE 754特殊值 `NaN` ， `inf` 和 `-inf` 将根据IEEE规则处理。具体来说， `NaN` 不被认为接近任何其他值，包括 `NaN` 。 `inf` 和 `-inf` 只被认为接近自己。 参见 [  PEP 485  ](https://www.python.org/dev/peps/pep-0485) —— 用于测试近似相等的函数

- `math.isfinite(x)`

如果x既不是无穷大也不是NaN，则返回 `True` ，否则返回 `False` 。 （注意 `0.0` 被认为  是  有限的。） 3.2 新版功能. 

- `math.isinf(x) `

如果x是正或负无穷大，则返回 `True` ，否则返回 `False` 。

- `math.isnan(x) `

如果x是 NaN（不是数字），则返回 `True` ，否则返回 `False` 。

- `math.isqrt(n)`

返回非负整数n的整数平方根。 这就是对n的实际平方根向下取整，或者相当于使得 a² ≤ n  的最大整数a 。

对于某些应用来说，可以更适合取值为使得n  ≤  a ² 的最小整数  a  ，或者换句话说就是 n的实际平方根向上取整。 对于正数n ，这可以使用`a = 1 + isqrt(n - 1)` 来计算。 

- `math.lcm(integers)`

返回给定的整数参数的最小公倍数。 如果所有参数均非零，则返回值将是为所有参数的整数倍的最小正整数。 如果参数之一为零，则返回值为 `0`。 不带参数的 `lcm()` 返回 `1`。 3.9 新版功能. 

- `math.ldexp(x,i)`

返回 `x*(2**i)` 。 这基本上是函数 [`frexp()`](https://docs.python.org/zh-cn/3/library/math.html#math.frexp) 的反函数。

- `math.modf(x) `

返回x的小数和整数部分。两个结果都带有x的符号并且是浮点数。

- `math.nextafter`(x,y)

返回x趋向于y的最接近的浮点数值。如果x等于y则返回y 。

示例：

`math.nextafter(x, math.inf)` 的方向朝上：趋向于正无穷。

`math.nextafter(x, -math.inf)` 的方向朝下：趋向于负无穷。

`math.nextafter(x, 0.0)` 趋向于零。

`math.nextafter(x, math.copysign(math.inf, x))` 趋向于零的反方向。

另请参阅 [`math.ulp()`](https://docs.python.org/zh-cn/3/library/math.html#math.ulp)。 

- `math.perm(n,k=None)`

返回不重复且有顺序地从  n  项中选择  k  项的方式总数。当 `k <= n` 时取值为 `n!/(n - k)!`；当 `k > n` 时取值为零。如果  k  未指定或为 None，则  k  默认值为  n  并且函数将返回 `n!`。如果任一参数不为整数则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。 如果任一参数为负数则会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。 3.8 新版功能. 

- `math.prod(iterable,*,start=1)`

计算输入的  iterable  中所有元素的积。 积的默认  start  值为 `1`。当可迭代对象为空时，返回起始值。 此函数特别针对数字值使用，并会拒绝非数字类型。 3.8 新版功能. 

- `math.remainder(x,y)`

返回 IEEE 754 风格的x相对于y的余数。对于有限x和有限非零y  ，这是差异 `x-ny` ，其中 `n` 是与商 `x/y` 的精确值最接近的整数。如果 `x/y` 恰好位于两个连续整数之间，则最近的   even  整数用于 `n` 。 余数 `r = remainder(x,y)` 因此总是满足 `abs(r) <= 0.5 abs(y)` 。特殊情况遵循IEEE 754：特别是 `remainder(x, math.inf)` 对于任何有限x都是x，而 `remainder(x, 0)` 和 `remainder(math.inf, x)` 引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 适用于任何非NaN的x。如果余数运算的结果为零，则该零将具有与x相同的符号。在使用IEEE 754二进制浮点的平台上，此操作的结果始终可以完全表示：不会引入舍入错误。 

- `math.trunc(x) `

返回 [`Real`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Real) 值x截断为 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral) （通常是整数）。 委托给 [`x.__trunc__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__trunc__)。

- `math.ulp(x) `

返回浮点数x的最小有效比特位的值:如果x是 NaN (非数字)，则返回  x 。如果x为负数，则返回 `ulp(-x)`。如果x为正数，则返回  x 。如果x等于，则返回  去正规化的  可表示最小正浮点数 (小于  正规化的  最小正浮点数 [`sys.float_info.min`](https://docs.python.org/zh-cn/3/library/sys.html#sys.float_info))。如果x等于可表示最大正浮点数，则返回x的最低有效比特位的值，使得小于x的第一个浮点数为 `x - ulp(x)`。在其他情况下 ( x  是一个有限的正数)，则返回x的最低有效比特位的值，使得大于x的第一个浮点数为 `x + ulp(x)`。ULP 即 "Unit in the Last Place" 的缩写。另请参阅 [`math.nextafter()`](https://docs.python.org/zh-cn/3/library/math.html#math.nextafter) 和 [`sys.float_info.epsilon`](https://docs.python.org/zh-cn/3/library/sys.html#sys.float_info)。

注意 [`frexp()`](https://docs.python.org/zh-cn/3/library/math.html#math.frexp) 和 [`modf()`](https://docs.python.org/zh-cn/3/library/math.html#math.modf) 具有与它们的C等价函数不同的调用/返回模式：它们采用单个参数并返回一对值，而不是通过 '输出形参' 返回它们的第二个返回参数（Python中没有这样的东西）。

对于 [`ceil()`](https://docs.python.org/zh-cn/3/library/math.html#math.ceil) ， [`floor()`](https://docs.python.org/zh-cn/3/library/math.html#math.floor) 和 [`modf()`](https://docs.python.org/zh-cn/3/library/math.html#math.modf) 函数，请注意  所有  足够大的浮点数都是精确整数。Python浮点数通常不超过53位的精度（与平台C double类型相同），在这种情况下，任何浮点x与 `abs(x) >= 2**52` 必然没有小数位。

## 幂函数与对数函数

- `math.exp(x) `

返回e次x幂，其中 `e = 2.718281...` 是自然对数的基数。这通常比 `math.e**x` 或 `pow(math.e, x)` 更精确。

- `math.expm1(x) `

返回e的x次幂，减1。这里e是自然对数的基数。对于小浮点数x， `exp(x)-1` 中的减法可能导致 [significant loss of precision](https://en.wikipedia.org/wiki/Loss_of_significance)； [`expm1()`](https://docs.python.org/zh-cn/3/library/math.html#math.expm1) 函数提供了一种将此数量计算为全精度的方法:

  ```python
  >>> from math import exp, expm1 
  >>> exp(1e-5) - 1  # gives result accurate to 11 places 
  1.0000050000069649e-05 
  >>> expm1(1e-5)    # result accurate to full precision 
  1.0000050000166668e-05 
  ```

- `math.log( x [*, base])`

使用一个参数，返回x的自然对数（底为  e  ）。使用两个参数，返回给定的  base  的对数x，计算为 `log(x)/log(base)` 。

- `math.log1p(x) `

返回  `1+x (base e )` 的自然对数。以对于接近零的x精确的方式计算结果。

- `math.log2(x) `

返回x以2为底的对数。这通常比 `log(x,2)` 更准确。 参见 [`int.bit_length()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#int.bit_length) 返回表示二进制整数所需的位数，不包括符号和前导零。

- `math.log10(x) `

返回x底为10的对数。这通常比 `log(x,10)` 更准确。

- `math.pow(x,y)`

将返回 `x` 的 `y` 次幂。特殊情况尽可能遵循C99标准的附录'F'。特别是， `pow(1.0,x)` 和 `pow(x,0.0)` 总是返回 `1.0` ，即使 `x` 是零或NaN。 如果 `x` 和 `y` 都是有限的， `x` 是负数， `y` 不是整数那么 `pow(x,y)` 是未定义的，并且引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 。与内置的 ` **` 运算符不同， [`math.pow()`](https://docs.python.org/zh-cn/3/library/math.html#math.pow) 将其参数转换为 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float) 类型。使用 `**` 或内置的 [`pow()`](https://docs.python.org/zh-cn/3/library/functions.html#pow) 函数来计算精确的整数幂。

- `math.sqrt(x)`

返回x的平方根。

## 三角函数

- `math.acos(x)`

返回以弧度为单位的x的反余弦值。 结果范围在 `0` 到 `pi` 之间。

- `math.asin(x)`

返回以弧度为单位的x的反正弦值。 结果范围在 `-pi/2` 到 `pi/2` 之间。

- `math.atan(x)`

返回以弧度为单位的x的反正切值。 结果范围在 `-pi/2` 到 `pi/2` 之间。.

- `math.atan2(y,x)`

以弧度为单位返回`atan(y/x)`。结果是在`-pi` 和`pi`之间。从原点到点`(x, y)`的平面矢量使该角度与正X轴成正比。 [`atan2()`](https://docs.python.org/zh-cn/3/library/math.html#math.atan2) 的点的两个输入的符号都是已知的，因此它可以计算角度的正确象限。 例如， `atan(1)` 和 `atan2(1, 1)` 都是 `pi/4` ，但 `atan2(-1, -1)` 是 `-3 pi/4` 。

- `math.cos(x) `

返回x弧度的余弦值。

- `math.dist(p,q)`

返回p与q两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。大致相当于：`sqrt(sum((px-qx)**2.0 for px, qx in zip(p, q))) ` 

- `math.hypot(coordinates)`

返回欧几里得范数，`sqrt(sum(x**2 for x in coordinates))`。 这是从原点到坐标给定点的向量长度。对于一个二维点 `(x,y)`，这等价于使用毕达哥拉斯定义 `sqrt(x x + y y)` 计算一个直角三角形的斜边。 在 3.8 版更改:  添加了对 n 维点的支持。 之前的版本只支持二维点。

- `math.sin(x) `

返回x弧度的正弦值。

- `math.tan(x) `

返回x弧度的正切值。

## 角度转换

- `math.degrees(x) `

将角度x从弧度转换为度数。

- `math.radians(x) `

将角度x从度数转换为弧度。

## 双曲函数

[双曲函数](https://en.wikipedia.org/wiki/Hyperbolic_function) 是基于双曲线而非圆来对三角函数进行模拟。

- `math.acosh(x) `

返回x的反双曲余弦值。

- `math.asinh(x) `

返回x的反双曲正弦值。

- `math.atanh(x) `

返回x的反双曲正切值。

- `math.cosh(x) `

返回x的双曲余弦值。

- `math.sinh(x) `

返回x的双曲正弦值。

- `math.tanh(x) `

返回x的双曲正切值。

## 特殊函数

- `math.erf(x) `

返回x处的 [error function](https://en.wikipedia.org/wiki/Error_function) 。[`erf()`](https://docs.python.org/zh-cn/3/library/math.html#math.erf) 函数可用于计算传统的统计函数，如 [累积标准正态分布](https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function)`def phi(x):    'Cumulative distribution function for the standard normal distribution'    return (1.0 + erf(x / sqrt(2.0))) / 2.0 ` 

- `math.erfc(x) `

返回x处的互补误差函数。 [互补错误函数](https://en.wikipedia.org/wiki/Error_function) 定义为 `1.0 - erf(x)`。 它用于x的大值，从其中减去一个会导致 [有效位数损失](https://en.wikipedia.org/wiki/Loss_of_significance)。 

- `math.gamma(x) `

返回x处[伽马函数](https://en.wikipedia.org/wiki/Gamma_function) 值。 

- `math.lgamma(x) `

返回Gamma函数在x绝对值的自然对数。 

## 常数

- `math.pi`

数学常数`π  = 3.141592...`，精确到可用精度。

- `math.e`

数学常数`e  = 2.718281...`，精确到可用精度。

- `math.tau`

数学常数 `τ= 6.283185...`，精确到可用精度。T 是一个圆周常数，等于2π ，圆的周长与半径之比。更多关于 Tau 的信息可参考 Vi Hart 的视频 [Pi is (still) Wrong](https://www.youtube.com/watch?v=jG7vhMMXagQ)。吃两倍多的派来庆祝 [Tau 日](https://tauday.com/) 吧！ 

- `math.inf`

浮点正无穷大。 （对于负无穷大，使用 `-math.inf`。）相当于 `float('inf')` 的输出。

- `math.nan`

浮点“非数字”（NaN）值。 相当于 `float('nan')` 的输出。

CPython implementation detail:   [`math`](https://docs.python.org/zh-cn/3/library/math.html#module-math) 模块主要包含围绕平台C数学库函数的简单包装器。特殊情况下的行为在适当情况下遵循C99标准的附录F。当前的实现将引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 用于无效操作，如 `sqrt(-1.0)` 或 `log(0.0)` （其中C99附件F建议发出无效操作信号或被零除）， 和 [`OverflowError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OverflowError) 用于溢出的结果（例如， `exp(1000.0)` ）。除非一个或多个输入参数是NaN，否则不会从上述任何函数返回NaN；在这种情况下，大多数函数将返回一个NaN，但是（再次遵循C99附件F）这个规则有一些例外，例如 `pow(float('nan'), 0.0)` 或 `hypot(float('nan'), float('inf'))` 。

请注意，Python不会将显式NaN与静默NaN区分开来，并且显式NaN的行为仍未明确。典型的行为是将所有NaN视为静默的。

参见

- [`cmath`](https://docs.python.org/zh-cn/3/library/cmath.html#module-cmath) 模块

  这里很多函数的复数版本。
