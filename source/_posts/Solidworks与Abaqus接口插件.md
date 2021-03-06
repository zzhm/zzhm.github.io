---
title: Solidworks与Abaqus接口插件
mathjax: false
date: 2021-02-26 11:28:46
id: solidworks-abaqus
tags:
- 软件教程
- 资源分享
categories:
- 实用教程
---

ABAQUS非线性功能强大，但是建模能力有限，对于复杂的结构模型，ABAQUS的建模功能不足，solidworks与abaqus接口插件解决了复杂模型的建立过程，实现solidworks和abaqus之间模型的关联导入，保持SolidWorks模型和Abaqus模型间的关系。

1、安装插件（分为32位和64位）

[Sw2AbqPlugin_64.rar](https://oss.jishulink.com/upload/201911/bd4c259ff8a64a3294126ca685bc66fe.rar)

[Sw2AbqPlugin_V1.4_32.zip](https://oss.jishulink.com/upload/201911/91e28be2880e4cc293943aa383097ef1.zip)

2、具体操作，以64为为例说明。

解压64位插件，打开solidworks，`文件-打开-Sw2AbqPlugin_64.dll`，插件安装成功后在工具选项中出现abaqus选项。

3、在abaqus中操作

选择`装配模块—>tools—>CAD interfaces—>SolidWorks`进入接口设置，保持默认设置点Enable即可。Abaqus命令提示区，提示与solidworks 接口已建立。

4、使用

在solidworks中建立好模型，`工具-abaqus-Export to Abaqus/CAE`，一般来讲，这个时候在abaqus中就会自动出现cae模型，这是自动导入。如果不行可以用abaqus手动输入，`abaqus—>import—>*.assembly—>*.eaf file`。注意导出导入文件名字必须是英文

5、这样就可以Solidworks与Abaqus就相互关联了，非常方便。