---
title: mathematica制作高质量图像
mathjax: false
date: 2020-07-22 15:00:31
id: mathematica-tupian
tags:
- mathematica
- 教程
categories:
- 实用教程
---

制作一个简单的三维图表：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105506.png)

<!---more--->

### 调整图像大小和样式

添加选项来改变样式和图像大小，使其符号出版要求：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110154.png)

Out[2]=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105543.png)

### 导出图形

把图形按 PDF 格式导出到文件中：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105551.png)

- 缺省情况下，[Export](https://reference.wolfram.com/language/ref/Export.html) 会在当前目录下（由 [SetDirectory](https://reference.wolfram.com/language/ref/SetDirectory.html) 设定）创建一个文件.
- [Export](https://reference.wolfram.com/language/ref/Export.html) 可以产生各种图形格式的文件，包括 GIF、JPEG 和 PNG. 请到[图形导入和导出](https://reference.wolfram.com/language/guide/GraphicsImportingAndExporting.html)查看更多信息.
- 对于出版级品质，不受分辨率影响的图形，["PDF"](https://reference.wolfram.com/language/ref/format/PDF.html) 是最可靠的格式. ["SVG"](https://reference.wolfram.com/language/ref/format/SVG.html) 也可用于二维图形，但三维图形可以在导出之前按屏幕分辨率进行光栅化，从而导致较低质量的图形.
- 光栅格式，如 ["PNG"](https://reference.wolfram.com/language/ref/format/PNG.html) 和 ["JPG"](https://reference.wolfram.com/language/ref/format/JPEG.html) 可用于出版级图形，但必须是非常高的分辨率（通常为每英寸 600 个像素或更多），这可能会导致非常大的图像文件.

### 在文档中包含导出图形

将图形文件拖放或插入到文档中.

在 TeX 源文件中，用 `\includegraphics` 嵌入图形:

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110032.png)

### 技术要点

绘图主题为图表提供了预先配置好的样式：

In[4]:=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110025.png)

```mathematica
Labeled[BubbleChart3D[RandomReal[1, {5, 5, 4}],     PlotTheme -> #], #] & /@ {"Classic", "Minimal", "Detailed",   "Monochrome", "Scientific", "Marketing"}
```

Out[4]=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105453.png)

用 面板 ▶ 图表元素方案 插入高级样式的选项：

In[5]:=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105603.png)

```mathematica
BubbleChart3D[RandomReal[1, {5, 5, 4}], PlotTheme -> "SolidGrid",  ChartElementFunction ->   ChartElementDataFunction["Cube", "Shape" -> "Square",    "Shading" -> "Fading", "TaperRatio" -> 1]]
```

Out[5]=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105609.png)

- 请到[自定义图表](https://reference.wolfram.com/language/workflow/CustomizeCharts.html)查看更多信息.

## 自定义图表--使用绘图主题...

绘图主题为图表和曲线图提供预先配置好的样式. 指定一个绘图主题以自定义图形的外观. 自动补全功能可以帮助你选择合适的主题：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110320.png)

在基本主题上添加“特色主题”改变绘图主题：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110232.png)

Out[2]=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110329.png)

- 到 [PlotTheme](https://reference.wolfram.com/language/ref/PlotTheme.html) 文档查看主题清单.

## 自定义图标-- 以互动方式...

###  制作一个图表

制作一个简单的三维条形图：

In[3]:=

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110242.png)

```mathematica
BarChart3D[{1, 2, 5, 4, 3}]
```

Out[3]=

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110335.png)

### 准备插入选项

在输入表达式的右方括号前面点击 (])，输入逗号，准备插入图表选项：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110402.png)

### 打开“图表元素方案”面板

选择 面板 ▶ 图表元素方案：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110421.png)

### 选择图表类型

选择想要定义的图表的类型：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110434.png)

### 选择图表样式

选择喜欢的图表样式：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110538.png)

### 调整图表外观

调整样式的参数：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110553.png)

### 插入图表外观选项并计算

点击“插入选项”重新计算输入：

![img](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722110609.png)

# PlotTheme



[PlotTheme](https://reference.wolfram.com/language/ref/PlotTheme.html)是绘图及相关函数的一个选项，用来指定图形元素和样式的外观主题.



[PlotTheme](https://reference.wolfram.com/language/ref/PlotTheme.html)->*theme* 将多个绘图选项设成默认值.

明确指定的绘图选项将重写由 *theme* 设定的值.

[PlotTheme](https://reference.wolfram.com/language/ref/PlotTheme.html)->{*theme*1,*theme*2,…} 会自动合并 *theme*1，*theme*2，等等.

[PlotTheme](https://reference.wolfram.com/language/ref/PlotTheme.html) 的可能设置为：

|      | [$PlotTheme](https://reference.wolfram.com/language/ref/$PlotTheme.html) | 系统主题设置             |
| ---- | ------------------------------------------------------------ | ------------------------ |
|      | [Automatic](https://reference.wolfram.com/language/ref/Automatic.html) | 根据背景和样式表自动调整 |
|      | "*name*"                                                     | 明确指定绘图的主题样式   |

基本主题的设置会影响到整体外观，一般单独使用. 想要达到特殊效果或特殊情况下，可将其和特殊主题联合使用.

常见基本主题包括：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105629.png)

特殊主题的设置会影响绘图的某个具体细节，一般和基本主题或其他特殊主题联合使用.

坐标轴特殊主题的设置会影响坐标轴、边框以及网格. 坐标轴特殊主题设置选择如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105633.png)

颜色特殊主题的设置会影响线和面. 颜色特殊主题设置选择如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105636.png)

字体特殊主题的设置会影响坐标轴的标记、绘图标记和图例. 字体特殊主题设置选择如下：

![](D:\Desktop\Mathematica制作出版级质量的图形.assets\image-20200722101945397.png)

尺寸特殊主题的设置会影响绘图的大小和形状. 尺寸特殊主题设置选择如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105639.png)

数据点标记符号特殊主题的设置会影响 [PlotMarkers](https://reference.wolfram.com/language/ref/PlotMarkers.html). 数据点标记符号特殊主题设置选择如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105643.png)

曲线特征主题影响绘图曲线. 主题包括：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105646.png)

表面网格特殊主题的设置会影响三维图形表面的网格. 主题设置选择如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105649.png)

图表元素方案特殊主题的设置会影响数据的图形样式. 主题设置选择如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105652.png)

体特征主题影响 3D 曲面，这对于 3D 打印很有用. 主题包括：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20200722105659.png)



# ImageResolution

[ImageResolution](https://reference.wolfram.com/language/ref/ImageResolution.html)是 [Export](https://reference.wolfram.com/language/ref/Export.html)、[Rasterize](https://reference.wolfram.com/language/ref/Rasterize.html) 和相关函数的一个选项，用于指定绘制位图图像所使用的分辨率.

- `ImageResolution->r`指定位图应当在 *r* dpi 的分辨率下绘制.
- `ImageResolution` 仅和像 "PNG"这样的位图图形格式有关，和 "SVG"这样的独立于分辨率的格式无关.
- 默认设置 `ImageResolution->Automatic`通常对位图格式使用 72 dpi 的分辨率.

导出图形和声音

Wolfram语言允许您以多种格式导出图形和声音。如果将笔记本前端用于Wolfram语言，则通常可以使用计算机系统上可用的标准机制，直接将图形和声音复制并粘贴到其他程序中。

| [Export](https://reference.wolfram.com/language/ref/Export.html)["*name*.*ext*",*graphics*] | 以从文件名推导出的格式将图形导出到文件 |
| ------------------------------------------------------------ | -------------------------------------- |
| [Export](https://reference.wolfram.com/language/ref/Export.html)["*file*",*graphics*,"*format*"] | 以指定格式导出图形                     |
| [Export](https://reference.wolfram.com/language/ref/Export.html)["!*command*",*graphics*,"*format*"] | 将图形导出到外部命令                   |
| [Export](https://reference.wolfram.com/language/ref/Export.html)["*file*",{*g*1,*g*2,…},…] | 导出动画的图形序列                     |
| [ExportString](https://reference.wolfram.com/language/ref/ExportString.html)[*graphics*,"*format*"] | 生成导出图形的字符串表示形式           |

导出Wolfram语言的图形和声音。

| [“ EPS”](https://reference.wolfram.com/language/ref/format/EPS.html) | 封装的PostScript （ .eps ）           |
| ------------------------------------------------------------ | ------------------------------------- |
| [“ PDF”](https://reference.wolfram.com/language/ref/format/PDF.html) | Adobe Acrobat便携式文档格式（ .pdf ） |
| [“ SVG”](https://reference.wolfram.com/language/ref/format/SVG.html) | 可缩放矢量图形（ .svg ）              |
| [“ PICT”](https://reference.wolfram.com/language/ref/format/PICT.html) | Macintosh PICT                        |
| [“ WMF”](https://reference.wolfram.com/language/ref/format/WMF.html) | Windows图元文件格式（ .wmf ）         |
| [“ TIFF”](https://reference.wolfram.com/language/ref/format/TIFF.html) | TIFF （ .tif , .tiff ）               |
| [“ GIF”](https://reference.wolfram.com/language/ref/format/GIF.html) | GIF和动画GIF （ .gif ）               |
| [“ JPEG”](https://reference.wolfram.com/language/ref/format/JPEG.html) | JPEG （ .jpg , .jpeg ）               |
| [“ PNG”](https://reference.wolfram.com/language/ref/format/PNG.html) | PNG格式（ .png ）                     |
| [“ BMP”](https://reference.wolfram.com/language/ref/format/BMP.html) | Microsoft位图格式（ .bmp ）           |
| [“ PCX”](https://reference.wolfram.com/language/ref/format/PCX.html) | PCX格式（ .pcx ）                     |
| [“ XBM”](https://reference.wolfram.com/language/ref/format/XBM.html) | X视窗系统位图（ .xbm ）               |
| [“ PBM”](https://reference.wolfram.com/language/ref/format/PBM.html) | 可移植位图格式（ .pbm ）              |
| [“ PPM”](https://reference.wolfram.com/language/ref/format/PPM.html) | 便携式像素图格式（ .ppm ）            |
| [“ PGM”](https://reference.wolfram.com/language/ref/format/PGM.html) | 便携式灰度图格式（ .pgm ）            |
| [“ PNM”](https://reference.wolfram.com/language/ref/format/PNM.html) | 可移植的Anymap格式（ .pnm ）          |
| [“ DICOM”](https://reference.wolfram.com/language/ref/format/DICOM.html) | DICOM医学成像格式（ .dcm , .dic ）    |
| [“ AVI”](https://reference.wolfram.com/language/ref/format/AVI.html) | 音频视频交错格式（ .avi ）            |

Wolfram语言支持的典型图形格式。第一组（前5个）中的格式与分辨率无关。

在Wolfram语言之外导出图形时，通常必须指定图形呈现的绝对大小。您可以使用[Export](https://reference.wolfram.com/language/ref/Export.html)的[ImageSize](https://reference.wolfram.com/language/ref/ImageSize.html)选项来执行此操作。

`ImageSize- > x`使图形的宽度成为 *x*打印机的点；`ImageSize- > 72xi`因此使宽度 *xi*英寸。默认设置是产生四英寸宽的图像。 `ImageSize->{x,y}`缩放图形，以使其在一个适合`x*y`区域。

| [ImageSize](https://reference.wolfram.com/language/ref/ImageSize.html) | [Automatic](https://reference.wolfram.com/language/ref/Automatic.html) | absolute image size in printer's points |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------- |
| "ImageTopOrientation"                                        | [Top](https://reference.wolfram.com/language/ref/Top.html)   | how the image is oriented in the file   |
| [ImageResolution](https://reference.wolfram.com/language/ref/ImageResolution.html) | [Automatic](https://reference.wolfram.com/language/ref/Automatic.html) | resolution in dpi for the image         |

Options for [Export](https://reference.wolfram.com/language/ref/Export.html).

[出口](https://reference.wolfram.com/language/ref/Export.html)选项。

在Wolfram语言中，以完全独立于最终将在其上呈现图形的计算机屏幕或其他输出设备的分辨率的方式来处理图形。

许多程序和设备接受高分辨率的图形-独立的格式，如内嵌的PostScript（EPS）。但是有些要求将图形转换为具有特定分辨率的栅格或位图。该[ImageResolution](https://reference.wolfram.com/language/ref/ImageResolution.html)的选项[导出](https://reference.wolfram.com/language/ref/Export.html)允许你确定应该用什么分辨率为每英寸点数（dpi）。设置的分辨率越低，获得的图像质量越低，但是存储图像所需的内存也越少。对于屏幕显示，典型分辨率为72 dpi或更高；适用于300 dpi及以上的打印机。

Wolfram语言支持的典型3D几何格式:

| [“ DXF”](https://reference.wolfram.com/language/ref/format/DXF.html) | AutoCAD图形交换格式（ .dxf ） |
| ------------------------------------------------------------ | ----------------------------- |
| [“ STL”](https://reference.wolfram.com/language/ref/format/STL.html) | STL立体光刻格式（ .stl ）     |

Wolfram语言支持的典型声音格式：

| [“ WAV”](https://reference.wolfram.com/language/ref/format/WAV.html) | Microsoft Wave格式（ .wav ） |
| ------------------------------------------------------------ | ---------------------------- |
| [“ AU”](https://reference.wolfram.com/language/ref/format/AU.html) | μ 法则编码（ .au ）          |
| [“ SND”](https://reference.wolfram.com/language/ref/format/SND.html) | 声音文件格式（ .snd ）       |
| [“ AIFF”](https://reference.wolfram.com/language/ref/format/AIFF.html) | AIFF格式（ .aif , .a ）      |

例子

```mathematica
Export["testplot600.pdf", plot, ImageResolution -> 600]
```



参考：https://reference.wolfram.com/language/