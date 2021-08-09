---
title: ABAQUS2020安装及错误处理-unsupport version ABAQUSLM
id: abaqus2020-install
date: 2020-03-28 21:20:11
tags:
- abaqus
- 有限元
categories:
- 实用教程
---

## 安装教程

1.下载安装包并解压缩，解压`SSQ_UniversalLicenseServer_Core_20180127074300.zip`
解压`SSQ_UniversalLicenseServer_Module_DSSimulia_20180127185300.zip`，复制Vendors到`SolidSQUAD_License_Servers`文件夹下合并文件夹

![ ](https://p9.pstatp.com/large/pgc-image/987cbfab61d744509fd0be256813d0ac)

2.复制SolidSQUAD_License_Servers文件夹到一个指定位置，右键管理员身份运行install_or_update.bat安装服务

![ ](https://p3.pstatp.com/large/pgc-image/e67a4ea8b1054e6bbbcf83b52101e712)

3.开始安装程序之前，可以通过创建下面的环境变量跳过FlexNET License server的安装
变量名：NOLICENSECHECK
变量值：true(这里千万别选错了，会导致后面无法使用)

![ ](https://p3.pstatp.com/large/pgc-image/3c31e5c97f9c48c0b5cc2f45f800e260)

4.加载DS.SIMULIA.SUITE.2020.WIN64.iso镜像文件，选择1文件夹，右键管理员身份运行Setup.exe开始安装

![ ](https://p3.pstatp.com/large/pgc-image/270e151b31624e00803b7c71a4416570)

5.选择需要安装的产品，（注意不要安装FlexNET License server）

![ ](https://p9.pstatp.com/large/pgc-image/3586e3d0ea9a4b00a4c8f3828461caeb)

6.由于软件安装包较大，安装过程中会提示选择不同的包格体，按照提示浏览加载的镜像里的文件夹即可

![ ](https://p3.pstatp.com/large/pgc-image/3eeb9afbebef48bc99a060d534f67045)

7.选择软件安装位置，点击浏览可自行更换安装路径

![ ](https://p1.pstatp.com/large/pgc-image/80c39d4173104a82a31c0608ae79cde3)

8.需要安装到目录下的部件

![ ](https://p3.pstatp.com/large/pgc-image/eaedd88200614ebfa41097b12e78b329)

9.安装过程中，在License Server Configuration许可证配置界面中，选择SIMULIAFLEXnet第一项

![ ](https://p1.pstatp.com/large/pgc-image/0a31eb0e5b4746ee847ab7bccde8e5d1)

10.在License Server 1中输入27800@localhost即可

![ ](https://p1.pstatp.com/large/pgc-image/e8f8c43503a54976a8a8ab3c1a595244)

11.一直点击下一步，点击安装

![ ](https://p1.pstatp.com/large/pgc-image/17ce513e87f14ea0b853f62bc70568e2)

12.正在安装中，请耐心等待一会，时间会稍微长一点

![ ](https://p3.pstatp.com/large/pgc-image/69e8a005f1a648eda8d191be65b921f1)

13.安装成功，点击关闭退出安装向导

![ ](https://p3.pstatp.com/large/pgc-image/65d9a23ff5914617b141c5c48e2f4e03)

14.运行软件即可免费使用了

![ ](https://p3.pstatp.com/large/pgc-image/6aef519a038c438997910333b544515a)



原文链接：https://www.52maicong.com/others/11292.html

## 错误处理

### unsupport version ABAQUSLM

原因就是这里没设置！！之前版本好像是没有的，导致在输入“27800@localhost”之后一直无法继续往后面安装。

```
3.开始安装程序之前，可以通过创建下面的环境变量跳过FlexNET License server的安装
变量名：NOLICENSECHECK
变量值：true(这里千万别选错了，会导致后面无法使用)
```

### IOError: abaqus.rpy: Permission denied

在`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2020`里找到“`Abaqus CAE`”的快捷方式，鼠标右键选择“属性”，在起始位置里设置个有读写权限的位置就行。

![](https://gitee.com/zihm/images/raw/master/hexo/20210809152515.png)