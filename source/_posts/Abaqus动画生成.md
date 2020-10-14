---
title: Abaqus动画生成
mathjax: false
date: 2019-09-02 09:42:00
id: abaqus
tags:
- abaqus
- 教程
- 动画
- 后处理
- 仿真
categories:
- 教程
---

在visualization模式中，在播放动画的状态下，点击animate--->save as  然后存成AVI格式，（同时可以调节播放速度frame rate）就可以保存动画了。保存在默认的temp文件夹里。

<!---more--->

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1567394814636.png)

用Abaqus生成动画，但是生成后动画不动，只有一帧:

（1）更改动画输出格式，选`.mov`(在Abaqus中是选QuickTime)；

（2）修改压缩编码方式为`Microsoft Video 1`；

（3）要保存动画，必须让图像动起来再保存。

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1567389270658.png)

官方文档：https://help.3ds.com/2018/English/DSSIMULIA_Established/SIMACAECAERefMap/simacae-m-Animation-sb.htm?ContextScope=all&id=0dee094d033b41c9aede92dfaac4ad0b#Pg0