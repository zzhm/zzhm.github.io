---
title: HistCite文献分析软件使用教程
date: 2018-04-29 09:43:33
id: HistCite-paper-ansys
categories: 
- 实用教程
tags:
- 软件教程
- 文献管理
---

首先要了解一点，HistCite 这款软件是 Thomson Reuters （汤森路透）公司开发的，和 WOS 是一家公司，所以 **HistCite 只支持 WOS 数据库**，对于 Scopus 等数据库则无能为力，不过 Github 上面有人写了一个可以将 Scopus 导入 Histcite 进行分析的脚本——[Scopus2Histcite](https://link.zhihu.com/?target=https%3A//github.com/leoatchina/Scopus2Histcite)，有兴趣的同学可以去试试看。

2016年10月，汤森路透知识产权与科技业务被 Clarivate Analytics （**科睿唯安**）公司收购了，从此 WOS 也是归该公司所有，因此导出的数据纯文本也发生了些许[变化](https://link.zhihu.com/?target=https%3A//weibo.com/1757292001/FbpSXo10s)，从而不能直接导入 HistCite 进行分析。不过别担心，**HistCite Pro 完全兼容新的文件格式！**

打开WOS，注意数据库要选择**核心合集（Core Collection）**！

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/35b6a3eea278b8e0bcb0dc8ef2558865_hd.jpg)



例如简单检索一下石墨烯在锂离子电池负极中的应用：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1c0f54e6e334e3cbe48c393667b55503_hd.jpg)



检索结果不是太多，可以全部导出，如果文献太多的话，可以先**按照被引频次降序排列**，只导出前2000篇就差不多了。

![](assets/e56979a1d5c4432567b15c8851630847_hd.jpg)



下面开始导出文献信息，点击页面上的【保存至 Endnote Online】按钮右边的下拉按钮，选择【**保存为其他文件格式**】。

![](assets/dc6e7ab49f30d58498a46f342e8ee718_hd.jpg)



在弹出的菜单中，记录数填写1到500，因为**每次最多只能导出500篇文献**，所以上面的2819篇文献需要分成6次导出，后面导出的时候依次填写501到1000、1001到1500等等。。。记录内容选择【**全记录与引用的参考文献**】，文件格式选择【**纯文本**】，然后点击发送即可得到导出的 txt 文件，类似可以导出其他5个。

![](assets/a519cc84cb3f0642830efc6d41c690a4_hd.jpg)

**注意：含500个记录的txt文档一般是3M左右，如果你的只有几百K，请仔细按照上面这张图进行导出！！！**



下面使用 HistCite 来分析这6个txt格式的引文数据文件。由于 HistCite 多年不更新，现在存在各种 Bug，比如直接打开 HistCite，一加载文件就报错：**No such file or directory**。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/793bdbf672010434236dad6a9641ea7e_hd.jpg)



尝试第二种方法。选中所有的 txt 文件，然后拖到 HistCite 的图标上，放开鼠标，果然自动打开了软件。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/5418126ccc24fc10c4a6c0f790d97c41_hd.jpg)



但是，事情好像并没有那么简单，又出现了一个报错：**Format Unknown**。

![](assets/dedf4eb40f939a81afa616c18e35e16e_hd.jpg)



在受到这么多折磨之后，我用 **Python** 开发了一个方便使用的脚步，于是一个以 HistCite 源程序为核心的精简易用**免安装**版本问世了，就叫 **HistCite Pro** 吧。

![](assets/ea8a95e0d78b3a0d9c66e58a4692507e_hd.jpg)



由于 HistCite 源程序只支持 Windows 系统，**所以 Pro 版本也只能在 Windows 下使用！**

你只需要下载 HistCite Pro 的压缩包（**下载链接见文末**）并解压（建议解压到 C 盘或者 D 盘的根目录下，**保证路径中不含中文**），就可以直接用，**不需要安装**，同时去掉了很多没用的文件，大大缩小了软件体积。对于从WOS上导出的txt数据文件，**不用做任何修改**，只要把全部的txt放到 **TXT 文件夹**里面，然后双击 **main.exe** 并**输入数字 1** 即可**一键完成加载**，非常方便。（下面是整个操作过程的动图，点击播放）

![](assets/v2-b8a30ba06c7a1757f359f8d7c99468a4_b.jpg)



如果输入数字 1 发现**没有自动打开浏览器窗口**，或者**打开的是一个空白网页**，或者**可以打开网页之后显示的条目数为0**，**首先检查一下前面的导出操作没有错误**，然后**看一下自己的 IE 浏览器能不能正常打开百度等网页**，如果 IE 浏览器有故障，可以参考[这个链接](https://link.zhihu.com/?target=https%3A//jingyan.baidu.com/article/6b97984dc1d9ab1ca2b0bf0c.html)进行修复。

如果还不行，那就是 HistCite 内核本身存在的设计缺陷（毕竟这么多年没有官方更新了），在少部分电脑上会出现**兼容性问题**。所以我采用 Python 的多线程成功实现了**Advanced 模式**，基本可以解决绝大部分兼容性问题，即**输入数字 3**。

注意：在该模式下，**程序所在路径中的所有文件夹和文件的命名都不能含有中文**。

![](assets/v2-e344c18f310133e0a3f430ecd2f0e920_hd.jpg)



该模式启动之后会**自动打开两个浏览器窗口**，先打开默认的 IE 浏览器窗口（记为 A 窗口），一般显示的 Records 数量为 0，然后 5 秒之后会调用**系统默认浏览器（推荐安装 Chrome 浏览器并设置为默认）**打开另一个窗口（记为 B 窗口），一般在 B 窗口就可以正常进行数据的导入。等导入完成之后，你可以将 A 窗口关闭，在 B 窗口里面分析数据，或者刷新 A 窗口也是可以分析数据的。

![](assets/v2-5e8f0e49b6ec56a9ffc3489e9ecf6855_hd.jpg)



好了，数据加载完毕，下面开始分析数据吧，点击 Tools 菜单下的 **Graph Maker**。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/51ec673cdbbccebdfc3f33a8c1555a4c_hd.jpg)



在弹出的页面上点击 Make Graph 即可得到一张引文关系图，包含了最有价值的前 **30** 篇文章的完整引文关系，**这个数字 30 是可以自行修改的**。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/3bb493c02c999157efdddfa1b1993586_hd.jpg)



这张图看起来不是很清楚，在左边的Size选项中选择 **Full** 模式，重新绘制一张高清图，然后右击图片“**另存为**”一张图片即可。

![](assets/a1b3418bf31c6f707f8cdc39e84de86d_hd.jpg)

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/3c2944fdf7a3071103fdf2b3c70a024f_hd.jpg)

图上有 30 个圆圈，每个圆圈表示一篇文献，中间的数字是这篇文献在数据库中的序号。圆圈越大，表示被引用次数越多。不同圆圈之间有箭头相连，箭头表示文献之间的引用关系。多数情况下，你会看到最上面有一个圆圈较大，并有很多箭头指向这篇文章。那么这篇文章很可能就是这个领域的**开山之作**。

通过我绘制出的这张关系图，我们发现标号为29、49、56、60的四个大圆圈非常显眼，可见这四篇文献的被引次数都是非常高的，我们对全部文献进行**按照 LCS 排序**，发现前四位刚好就是这 4 篇文献。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/8debe218aa75ffa2f7fb0fc941b2619a_hd.jpg)



再回到那张圆圈箭头关系图，可见石墨烯在锂离子电池负极材料中的应用研究主要起源于2008年（29号文献），其通讯作者Honma来自日本，看来日本在石墨烯电池方面的研究开展得相当早。之后，在2010年，很多原创性的成功迸发而出，具有代表性的就是49、56、60、48号文献，非常有趣的是，2010年诺贝尔物理学奖的获奖项目刚好是石墨烯，其中的关联显而易见。之后的几年，石墨烯在锂离子电池负极方面的研究越来越多，方向约越来越细。



好了，前面提到HistCite可以找到某些**具有开创性成果的无指定关键词的论文**，我们来看看是怎么办到的。点击页面上的【**Cited References**】，然后就可以看到本地库中的文献参考的全部文献信息，后面**带有加号的表示本地txt库中没有包含**。如果然后**按照 Recs 数排序**，可以看到有几篇 Recs 数很大的文献并没有在分析范围之内，这些往往就是**被遗漏的重要文献**。正常情况下**点击加号（+）后的 WOS** 就可以自动通过 WOS 将文献载入分析。

![](assets/v2-8ee996bdf74b61771a99d1947bb386ad_hd.jpg)



如果点击之后**网页报错**，内容是：Routing Error。Error massage：cannot process request with unsupported DestLinkType:CitedLookup。

![](assets/v2-44789aa0a0e17bb1284f59a6dee5895d_hd.jpg)



这是由于 WOS 地址解析错误，可以按照以下方法来解决。

首先在任何网页浏览器中**打开 Web of Science 网页**，点击【**被引参考文献检索**】标签（英文版是【Cited Reference Search】）。**复制当前页面的网址**，后面要用。网址格式为：[http://apps.webofknowledge.com/UA_CitedReferenceSearch_input.do?SID=******&product=UA&search_mode=CitedReferenceSearch](https://link.zhihu.com/?target=http%3A//apps.webofknowledge.com/UA_CitedReferenceSearch_input.do%3FSID%3D7CNzOGIKMcsWFOdDoqK%26product%3DUA%26search_mode%3DCitedReferenceSearch)，注意最后**以 CitedReferenceSearch 结尾**。

![](assets/v2-fec3c303aac7420ae393d3157d7e9120_hd.jpg)



然后在 Histcite 工具栏 tools下拉菜单中选择 **Settings** 点击。

![](assets/v2-7c2cec2e11ccfc927d6e621db1d54db8_hd.jpg)



在弹出的对话框中，往下找到 **WoS link** 这一栏，默认选择是 Universal setup，改选 **Manual setup version 4**，然后在 **ISI web of knowledge 4 location URL** 下面的框里**粘贴刚才复制的网址**，再点击【Set】即可。

![](https://pic4.zhimg.com/80/v2-8ce7e05262d0fa465f0a1208f9945ef7_hd.jpg)



然后再点击遗漏文献后面**加号（+）后的 WOS** 就可以打开 WOS 并**自动将文献信息填进去**，然后点击【检索】。

![](assets/v2-aea5bc33ed4e7b6f9dc023d25ce782cf_hd.jpg)



在搜索结果中找到所需要的文献（**一般被引次数最多的那个就是**），点击【完成检索】即可显示**引用了该篇文献的**所有文献，同样可以导出 txt 加入 Histcite 进行分析。

![](assets/v2-be17317b4ef023863e05199a5a0fe672_hd.jpg)



同样的，我们点击 Histcite 页面的【Authors】按钮，可以找到本领域的一些大牛，具体的操作步骤读者可以自己去摸索。



那么我们怎么把文献记录**导出到Endnote**呢？首先点击菜单栏中【Tools】下的【Mark&Tag】选项，调出标记选择工具栏。

![](https://pic2.zhimg.com/80/12d26826fab54afa05cfb0425b838b45_hd.jpg)



下图红框内就是标记选择工具栏。左边栏用于指定选择范围，可以选择当前列表中的全部文献，也可以按照序号（#）、LCS、LCR等数值的区间来选择文献，还可以手动勾选需要的文献。中间栏表示的是需要导出的信息范围，可以只导出记录本身，也可以选择导出引用的文献或者被引的文献。右边栏的【**Mark**】按钮就是确认选择按钮。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/27a5cdc8ac64eea38323f72510ac5180_hd.jpg)



所以，我们选择好了需要导出的文献记录，**点击【Mark】按钮**。

![](assets/fafb447f009bfa46c794cf79dcf4d77a_hd.jpg)



然后，我们就会发现上面出现了一个新的标签【Marks】，后面的数字就是我们选中的记录条数，如果发现这个数字不正确，点击【Mark】按钮旁边的【Unmark】来重新选择。确认无误之后，**点击图示的【Marks】标签链接**，即可显示全部被选的文献记录。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/8ede4dc74af5a43b22c66010f6243bf4_hd.jpg)



好的，下面依次点击【File】、【Export】、【Records...】来导出选中的文献记录。

![](https://pic4.zhimg.com/80/3a08ebe920dc4933a5f4e8a8d5e2834f_hd.jpg)



成功导出后得到一个 **.hci** 格式的文本文件，直接修改后缀为 **txt**。如果导出不成功，一般多尝试几次就可以。

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/061712ba82106c3479ecf0c2f6200f41_hd.jpg)



好的，现在我们打开Endnote，依次点击【File】、【Import】、【File...】按钮。

![](assets/ace68f07346e8e4ce88c85cbdf193108_hd.jpg)



在弹出的对话框中通过【Choose...】找到刚才的txt文件，【Import Option】选择 **Multi-Filter (Special)**，【Duplicates】选择 **Import All**，然后点击【Import】按钮即可导入。

![](https://pic4.zhimg.com/80/92f2753aab51a35d2fa8b9a90b0446b7_hd.jpg)



评论中沈曦同学提到了将 HistCite 选好的文献导入到 **Noteexpress** 软件里的方法，具体操作是在导入时将**过滤器选择为 web of science。**

最后附上HistCite里面几个重要的英文缩写（感谢Dingledodies同学）：

**GCS**（global citation score）， 某一文献在WOS数据库中的总被引用次数。有些引用这篇参考文献的文章可能和你的研究方向毫无关系，但GCS还是会把这个引用数据记录下来。

**LCS**（local citation score），某一文献在本地数据集中的被引用次数。因为你导入Histcite的文章都是和你检索词有关系的，可以认为这些文章是你的研究同行，因此如果某一篇文献的LCS值很高，就意味着它是你研究领域内的重要文献，很有可能是你领域内的开创性文章，注意LCS高的文献和GCS高的文献不一定是同一篇！

**LCR**（local cited references）， 某一文献引用本地数据集中参考文献的数目。根据LCR值的排序，可以快速定位近期关注该领域的重要文献，因为某一篇文献引用当前数据集中的文献数越多，说明它非常关注你检索的这个研究方向的文献，和你的研究肯定有相似或者可参考之处，可以从该文章中发现新动向。

**CR**（cited references）， 某一文献引用WOS数据库中参考文献的数目。这个值越高，说明这篇文献很可能是综述性文献，可根据该值的排序，也可快速定位综述文献。

------

## **重要的补充说明：**

有很多人反馈的使用故障，其实都是由于自己**操作不当**导致的，要么是 WOS 数据库没有选择【**核心合集**】，要么是导出txt的时候没有选择【**全记录与引用的参考文献**】，或者**根本不看使用说明就想当然操作**，例如自己到 core 文件夹中打开内核文件或者把 main.exe 单独拿出来运行。

## **HistCite Pro 网盘下载链接：**[http://pan.baidu.com/s/1hsIwJzQ](https://link.zhihu.com/?target=http%3A//pan.baidu.com/s/1hsIwJzQ)

备用下载源：[https://www.lanzous.com/i2jvwba](https://link.zhihu.com/?target=https%3A//www.lanzous.com/i2jvwba)

原文链接：**https://zhuanlan.zhihu.com/p/20902898**，感谢您在版权保护方面做出的努力！