---
title: Abqaus支持中文界面和中文路径的配置方法
date: 2021-02-26 16:11:05
id: abaqus-zhcn
tags:
- 软件教程
categories:
- 实用教程
---

Abaqus只需完成3步即可切换为中文界面，并支持中文路径，只需操作TXT文件，极度简单！

（1）关闭ABAQUS 软件，

（2）找到`C:\SIMULIA\EstProducts\2020\win_b64\SMA\Configuration\locale.txt`。不同电脑的安装文件夹不同，关键是找到`win_b64\SMA\Configuration\locale.txt`

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1561619839492.png)

（3）把`locale.txt`中，在图中位置，`Chinese_People's Republic of China.936 = zh_CN`和`
Chinese (Simplified)_People's Republic of China.936 = zh_CN`后面加上`Chinese (Simplified)_China.936 = zh_CN`，此时便已经可以支持中文路径了！

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1561619897524.png)

（4）如果需要把界面显示成中文的，则`把locale.txt`中，第三串长######################之前的`zh_CN = 0`改为`zh_CN = 1`。

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1561619992412.png)



注意：

（1）若不希望汉化abaqus界面，又希望软件能够支持中文路径，可以只修改（3）中的内容。

（2）2018和2020版本测试可用。