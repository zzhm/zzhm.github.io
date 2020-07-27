---
title: Abaqus 2018 支持中文路径和中文界面的方法
mathjax: false
date: 2019-06-27 15:11:54
id: abaqus-cn
tags:
- abaqus
- 学习
categories:
- 学习
- 软件
---

Abaqus2018只需完成3步即可切换为中文界面，并支持中文路径，只需操作TXT文件，极度简单！

<!---more--->

找到`C:\ABAQUS\CAE\win_b64\SMA\Configuration\locale.txt`。不同电脑的安装文件夹不同，关键是找到`win_b64\SMA\Configuration\locale.txt`

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1561619839492.png)

把`locale.txt`中，在图中位置，加上`Chinese (Simplified)_China.936 = zh_CN`

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1561619897524.png)

`把locale.txt`中，第三串长######################之前的`zh_CN = 0`改为`zh_CN = 1`

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1561619992412.png)