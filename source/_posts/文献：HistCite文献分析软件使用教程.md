---
title: HistCite文献分析软件使用教程
date: 2018-04-29 09:43:33
id: HistCite-paper-ansys
categories: 
- 科研
- 文献
tags:
- 工具
- 文献
- 科研
---

### 准备工作

HistCite 这款软件是 Thomson Reuters （汤森路透）公司开发的，和 WOS 是一家公司，所以 **HistCite 只支持 WOS 数据库**，对于 Scopus 等数据库则无能为力，不过 Github 上面有人写了一个可以将 Scopus 导入 Histcite 进行分析的脚本——[Scopus2Histcite](https://link.zhihu.com/?target=https%3A//github.com/leoatchina/Scopus2Histcite)，有兴趣的同学可以去试试看。
打开WOS，注意数据库要选择**核心合集**（Core Collection）！

<center>
![img](http://img.shihuidaren.cn/histcite/35b6a3eea278b8e0bcb0dc8ef2558865_hd.jpg)
</center>

<!--- more --->

例如简单检索一下石墨烯在锂离子电池负极中的应用：

<center>
![](http://img.shihuidaren.cn/histcite/1c0f54e6e334e3cbe48c393667b55503_hd.jpg)
</center>

检索结果不是太多，可以全部导出，如果文献太多的话，可以先**按照被引频次降序排列**，只导出前2000篇就差不多了。

<center>
![img](http://img.shihuidaren.cn/histcite/e56979a1d5c4432567b15c8851630847_hd.jpg)
</center>

下面开始导出文献信息，点击页面上的【保存至 Endnote Online】按钮右边的下拉按钮，选择【**保存为其他文件格式**】。

<center>
![img](http://img.shihuidaren.cn/histcite/dc6e7ab49f30d58498a46f342e8ee718_hd.jpg)
</center>

在弹出的菜单中，记录数填写1到500，因为**每次最多只能导出500篇文献**，所以上面的2819篇文献需要分成6次导出，后面导出的时候依次填写501到1000、1001到1500等等。。。记录内容选择【**全记录与引用的参考文献**】，文件格式选择【**纯文本**】，然后点击发送即可得到导出的 txt 文件，类似可以导出其他5个。

<center>
![img](http://img.shihuidaren.cn/histcite/a519cc84cb3f0642830efc6d41c690a4_hd.jpg)
</center>

**注意：含500个记录的txt文档一般是3M左右，如果你的只有几百K，请仔细按照上面这张图进行导出！！！**

### HistCite分析

你只需要下载 HistCite Pro 的压缩包（[**下载链接**](http://pan.baidu.com/s/1hsIwJzQ?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&traceid=#list/path=%2F)）并解压（建议解压到 C 盘或者 D 盘的根目录下，**保证路径中不含中文**），就可以直接用，**不需要安装**。对于从WOS上导出的txt数据文件，**不用做任何修改**，只要把全部的txt放到 **TXT 文件夹**里面，然后双击 **main.exe** 即可**一键完成加载**，非常方便。

<center>
![img](http://img.shihuidaren.cn/histcite/f639c7bdf108839dfc47ec8b5794c5ea_hd.jpg)</center>

好了，数据加载完毕，下面开始分析数据吧，点击 Tools 菜单下的 **Graph Maker**。

<center>
![img](http://img.shihuidaren.cn/histcite/51ec673cdbbccebdfc3f33a8c1555a4c_hd.jpg)
</center>

在弹出的页面上点击 Make Graph 即可得到一张引文关系图，包含了最有价值的前 **30** 篇文章的完整引文关系。

<center>
![img](http://img.shihuidaren.cn/histcite/3bb493c02c999157efdddfa1b1993586_hd.jpg)
</center>

这张图看起来不是很清楚，在左边的Size选项中选择 **Full** 模式，重新绘制一张高清图，然后右击图片“**另存为**”一张图片即可。

<center>
![img](http://img.shihuidaren.cn/histcite/a1b3418bf31c6f707f8cdc39e84de86d_hd.jpg)
</center>

<center>
![img](http://img.shihuidaren.cn/histcite/3c2944fdf7a3071103fdf2b3c70a024f_hd.jpg)
</center>

图上有 30 个圆圈，每个圆圈表示一篇文献，中间的数字是这篇文献在数据库中的序号。圆圈越大，表示被引用次数越多。不同圆圈之间有箭头相连，箭头表示文献之间的引用关系。多数情况下，你会看到最上面有一个圆圈较大，并有很多箭头指向这篇文章。那么这篇文章很可能就是这个领域的**开山之作**。

通过我绘制出的这张关系图，我们发现标号为29、49、56、60的四个大圆圈非常显眼，可见这四篇文献的被引次数都是非常高的，我们对全部文献进行按照 LCS 排序，发现前四位刚好就是这 4 篇文献。

<center>
![img](http://img.shihuidaren.cn/histcite/8debe218aa75ffa2f7fb0fc941b2619a_hd.jpg)
</center>

再回到那张圆圈箭头关系图，可见石墨烯在锂离子电池负极材料中的应用研究主要起源于2008年（29号文献），其通讯作者Honma来自日本，看来日本在石墨烯电池方面的研究开展得相当早。之后，在2010年，很多原创性的成功迸发而出，具有代表性的就是49、56、60、48号文献，非常有趣的是，2010年诺贝尔物理学奖的获奖项目刚好是石墨烯，其中的关联显而易见。之后的几年，石墨烯在锂离子电池负极方面的研究越来越多，方向约越来越细。
好了，前面提到HistCite可以找到某些具有开创性成果的无指定关键词的论文，我们来看看是怎么办到的。点击页面上的【**Cited References**】，然后就可以看到本地库中文献参考的全部文献信息，后面带有加号的表示本地txt库中没有包含，这些往往就是**被遗漏的重要文献**。

<center>
![img](http://img.shihuidaren.cn/histcite/a4ba6cd3cfe2af54e3cd824e1a2de7bc_hd.jpg)
</center>

同样的，我们点击上面的【Authors】按钮，可以找到本领域的一些大牛，具体的操作步骤读者可以自己去摸索。

那么我们怎么把文献记录**导出到Endnote**呢？首先点击菜单栏中【Tools】下的【Mark&Tag】选项，调出标记选择工具栏。

<center>
![img](http://img.shihuidaren.cn/histcite/12d26826fab54afa05cfb0425b838b45_hd.jpg)
</center>

下图红框内就是标记选择工具栏。左边栏用于指定选择范围，可以选择当前列表中的全部文献，也可以按照序号（#）、LCS、LCR等数值的区间来选择文献，还可以手动勾选需要的文献。中间栏表示的是需要导出的信息范围，可以只导出记录本身，也可以选择导出引用的文献或者被引的文献。右边栏的【**Mark**】按钮就是确认选择按钮。

<center>
![img](http://img.shihuidaren.cn/histcite/27a5cdc8ac64eea38323f72510ac5180_hd.jpg)
</center>

所以，我们选择好了需要导出的文献记录，**点击【Mark】按钮**。

<center>
![img](http://img.shihuidaren.cn/histcite/fafb447f009bfa46c794cf79dcf4d77a_hd.jpg)
</center>

然后，我们就会发现上面出现了一个新的标签【Marks】，后面的数字就是我们选中的记录条数，如果发现这个数字不正确，点击【Mark】按钮旁边的【Unmark】来重新选择。确认无误之后，**点击图示的【Marks】标签链接**，即可显示全部被选的文献记录。

<center>
![img](http://img.shihuidaren.cn/histcite/8ede4dc74af5a43b22c66010f6243bf4_hd.jpg)
</center>

好的，下面依次点击【File】、【Export】、【Records...】来导出选中的文献记录。

<center>
![img](http://img.shihuidaren.cn/histcite/3a08ebe920dc4933a5f4e8a8d5e2834f_hd.jpg)
</center>

成功导出后得到一个 **.hci** 格式的文本文件，直接修改后缀为 **txt**。如果导出不成功，一般多尝试几次就可以。

<center>
![img](http://img.shihuidaren.cn/histcite/061712ba82106c3479ecf0c2f6200f41_hd.jpg)</center>
好的，现在我们打开Endnote，依次点击【File】、【Import】、【File...】按钮。

<center>
![img](http://img.shihuidaren.cn/histcite/ace68f07346e8e4ce88c85cbdf193108_hd.jpg)
</center>

在弹出的对话框中通过【Choose...】找到刚才的txt文件，【Import Option】选择 **Multi-Filter (Special)**，【Duplicates】选择 **Import All**，然后点击【Import】按钮即可导入。

<center>
![img](http://img.shihuidaren.cn/histcite/92f2753aab51a35d2fa8b9a90b0446b7_hd.jpg)
</center>

评论中沈曦同学提到了将 HistCite 选好的文献导入到 **Noteexpress** 软件里的方法，具体操作是在导入时将**过滤器选择为 web of science。**

### HistCite里面几个重要的英文缩写

**GCS**（global citation score）， 某一文献在WOS数据库中的总被引用次数。有些引用这篇参考文献的文章可能和你的研究方向毫无关系，但GCS还是会把这个引用数据记录下来。 

**LCS**（local citation score），某一文献在本地数据集中的被引用次数。因为你导入Histcite的文章都是和你检索词有关系的，可以认为这些文章是你的研究同行，因此如果某一篇文献的LCS值很高，就意味着它是你研究领域内的重要文献，很有可能是你领域内的开创性文章，注意LCS高的文献和GCS高的文献不一定是同一篇！ 

**LCR**（local cited references）， 某一文献引用本地数据集中参考文献的数目。根据LCR值的排序，可以快速定位近期关注该领域的重要文献，因为某一篇文献引用当前数据集中的文献数越多，说明它非常关注你检索的这个研究方向的文献，和你的研究肯定有相似或者可参考之处，可以从该文章中发现新动向。

**CR**（cited references）， 某一文献引用WOS数据库中参考文献的数目。这个值越高，说明这篇文献很可能是综述性文献，可根据该值的排序，也可快速定位综述文献。 

### 问题解决

如果你的电脑不存在上述兼容性问题，你不用在乎这个 ADV 模式，直接输入YES即可完成数据的读取。如果你的电脑出现了上述导入不成功的问题，你就可以**输入ADV**，**回车**之后会读取 txt 文件，然后自动启动 HistCite 内核。

<center>
![img](http://img.shihuidaren.cn/histcite/893bd536d09de6bb27df1f279e74a0ba_hd.jpg)</center>

HistCite 启动之后会自动打开一个IE内核的浏览器窗口（记为 **A** 窗口），而这个窗口显示我们导入的 Records 数量为0，即没有成功导入数据。所以在 ADV 模式下，HistCite Pro 会自动调用系统默认浏览器在 5 秒后**再打开一个窗口**（记为**B**窗口）进行数据的导入，等导入完成之后，你可以将 A 窗口关闭，在 B 窗口里面分析数据，或者按 F5 键**刷新 A 窗口**也是可以分析数据的。

<center>
![img](http://img.shihuidaren.cn/histcite/e854c4660f57de8c7c2e23cb8eb33720_hd.jpg)
</center>

**注意**：在ADV模式下，程序所在路径中的所有文件夹和文件的命名都**不能含有中文**。

### 说明

原文链接：http://zhuanlan.zhihu.com/p/20902898

