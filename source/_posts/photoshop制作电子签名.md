---
title: Photoshop制作电子签名
mathjax: false
date: 2020-09-20 14:24:08
id: photoshop-qianming
tags:
- 教程
- 软件
- 生活
categories:
- 实用教程
---

最近因为工作原因，需要在PDF文档中添加电子签名。因为以前没有接触过Photoshop软件，用的是简单易上手的某某秀秀，虽然也能实现功能，但总觉得有点Low，一些细节还是不够满意。所以就花了一晚上学习了一下用Photoshop制作电子签名的方法，完后做以总结并分享。

<!---more--->

## 签名并扫描

先在白纸上签上自己的名字，然后通过**扫描或者拍照**的方式储存为`.jpg`图片，再用Photoshop打开图片。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232235.png)

## 提取签字区域

通过Photoshop界面左下角的缩放工具，将页面缩放到签字部分，方便区域选取。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232236.png)

点击最上面的工具栏中的 **选择-色彩范围**。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232237.png)

用取色笔点击黑色的签名部分，提取出签字部分的大概轮廓后点击“**确定**”。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232238.png)

此时可以看到，签字的大致区域已经勾勒了出来，但还不够理想。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232239.png)

因此，点击最上面的工具栏中的 **选择-扩大选取**。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232240.png)

此时，可以看到选取范围非常理想了。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232241.png)

紧接着，按”**Ctrl+J**“，此时**会生成一个新的图层，并将选择区域自动粘贴到新的图层上去**。从右下角可以看见：此时新建了一个图层，名字叫“**图层1**”。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232242.png)

可以看到，在“图层1”下面还有一个叫“背景”的图层，该图层前有一个眼睛形状的图标，点击该图标，可以取消背景的显示，区域提取工作完成。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232243.png)



## 签名截取与尺寸设置

得到签名区域后，需要设置签名的大小，方便以后粘贴使用。

先通过框选工具将签字区域框选。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232244.png)

将光标置于框选区域内，按“**Ctrl+C**”将该区域复制。

接着点击最上面工具栏的 **文件-新建**。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232245.png)

在对话框中设置，宽度为600像素，高度为300像素（可根据自己的需要设定）。点击确定。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232246.png)

可以看到新建了一个文件。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232247.png)

通过按“**Ctrl+V**”，将刚刚复制的区域粘贴过来。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232248.png)

可以看到，右边自动多了一个“图层1”。

接着，按“**Ctrl+T**”，可以看到，刚刚粘贴过来部分的轮廓显现出来。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232249.png)

通过“**Shift键**”和**鼠标左键**的配合操作，不失真地调整签字的尺寸，使其能够适应背景的尺寸，**最后以回车确认**。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232218.png)

## 签字颜色调整

可以看到，此时签名的颜色偏淡，最好能加深一些。

点击最上面工具栏中的 **图像-调整-色阶**。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232250.png)

通过改变输入色阶的第二个参数，可以改变签字颜色的深浅。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232251.png)

将签字颜色深浅调整到自己满意为止，点击确定，并点击背景图层前的眼睛图标，隐藏背景显示。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232252.png)

## 填充黑色

点击最上面的工具栏中的 **选择-色彩范围**，选择字体轮廓。

点击最上面的工具栏中的 **编辑-填充**。

![](https://gitee.com/zihm/images/raw/master/hexo/20200517132034.png)

## 输出电子签名

在输出时需要注意的是输出格式，建议保存问`.PNG`格式文件，因为这样能够保证电子签名是无背景的。可以使用到任何含有背景的文件上。

![](https://gitee.com/zihm/images/raw/master/hexo/20200516232253.png)