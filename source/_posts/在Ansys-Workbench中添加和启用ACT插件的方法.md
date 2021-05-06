---
title: 在Ansys Workbench中添加和启用ACT插件的方法
mathjax: false
date: 2019-07-11 13:37:22
id: ansys-act
tags:
- workbench
- 有限元
- 软件教程
categories:
- 实用教程
---

在Ansys Workbench中可以通过ACT插件来拓展Ansys的功能。在Workbench主界面中点击菜单Extensions - Install Extension...，在打开的文件选择对话框中找到ACT插件，点击打开进行ACT插件的安装。

<!---more--->

![](https://gitee.com/zihm/images/raw/master/hexo/20210506134059.png)

编译好的ACT插件的扩展名为.wbex，安装完成后会弹出如下对话框：“The extension *** was successfully installed.“，说明插件已成功安装。

![](https://gitee.com/zihm/images/raw/master/hexo/20210506134057.png)

安装完成后再次点击菜单Extensions - Manage Extensions...，打开Extensions Manager对话框，在对话框中勾选要加载的ACT插件，启用相应的Ansys Workbench ACT插件。

![](https://gitee.com/zihm/images/raw/master/hexo/20210506134054.png)

当ACT插件被启用后，在对应的环境中会显示相应的工具条，一般在对应位置右击时也可调出相应的快捷菜单（根据插件的开发不同，可能会有差异）。如下图所示为安装Ansys  Workbench ACT 16.0集成工具包中的HotKeys和FollowerLoads两个插件后工具栏中显示的对应命令按钮。

![](https://gitee.com/zihm/images/raw/master/hexo/20210506134052.png)

Ansys插件官方下载地址：https://catalog.ansys.com/?t=Mechanical

参考文章

几款插件：http://www.leanwind.com/archives/4732.html

本文来源：http://www.leanwind.com/archives/3801.html