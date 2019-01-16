---
title: 快速搭建一个本地的FTP服务器
mathjax: false
date: 2018-10-16 19:31:08
id: ftp-server-on-windows
tags:
- ftp
- nas
categories:
- 生活
- nas
---

****

  如果需要开发FTP文件上传下载功能，那么需要在本机上搭建一个本地FTP服务器，方便调试。

<!---more--->

**第一步：配置IIS Web服务器**

**1.1 控制面板中找到“程序”并打开**

![](http://img.shihuidaren.cn/nas/5c905b2d8d6292e50d0cc4319575e101.jpg)

**1.2 程序界面找到“启用或关闭Windows功能”并打开**

![](http://img.shihuidaren.cn/nas/3874a45f0df9405dfb19c90b1e8bc0dd.jpg)

**1.3 上面两步也可以简化为一步：按【Win +R】快捷键打开运行对话框，输入“optionalfeatures”后，按回车键**

![](http://img.shihuidaren.cn/nas/af3a6cc4a982fc337b3fe906546d31d3.png)

**1.4 从“启用或关闭Windows功能”弹窗中找到Internet Information Services(或者中文版Internet信息服务)并打开**

![](http://img.shihuidaren.cn/nas/ece8ab31c6ff669953ecfd9829bd3c5c.jpg)

**1.5 配置IIS并点击确定**

![](http://img.shihuidaren.cn/nas/40e9b37676141739fb8768e1665e756f.png)

**第二步：配置IIS Web站点**

**2.1 开始菜单搜索“IIS”并点击进入IIS管理器**

![](http://img.shihuidaren.cn/nas/8d90171ba5b75ce52578aecacd4f3af2.png)

**2.2 新建FTP站点**

**2.2.1 新建FTP服务器根目录文件夹**

![](http://img.shihuidaren.cn/nas/e354c1271f3672d15e3028895634fab8.png)

**2.2.2 查看本机ip地址，后续访问Ftp地址需要用到（打开cmd输入ipconfig）**

![](http://img.shihuidaren.cn/nas/974aa7f2ee8c41c4fc34ea98fcfd366b.png)

**2.2.3 IIS网站管理器界面左边导航栏找到“网站”，右键弹出菜单**

![](http://img.shihuidaren.cn/nas/4a61920418220d86a15ee0986880364b.png)

**2.2.4 IIS网站管理器“网站”右键弹出菜单点击“添加FTP站点”**

![](http://img.shihuidaren.cn/nas/3d3d2fcd955cec574ad0ff5d006e4141.png)

**2.2.5 配置网站（网站名称：FtpSite 物理路径：E:\\ftpserver 本机IP地址(从下拉菜单选择)：192.168.0.105）**

**Ftp站点名称和物理路径设置**

![](http://img.shihuidaren.cn/nas/c1206bb880655aa50c4d40a1e1bdfe78.png)

**IP 端口号 SSL设置**

![](http://img.shihuidaren.cn/nas/802eb1e5de9ace52cf5bb0a9cc2e412e.png)

**身份验证和授权信息设置**

![](http://img.shihuidaren.cn/nas/4e9b08650842dd6d2a5856b029c7023d.png)

**第三步：测试FTP站点（先在物理路径：E:\\ftpserver随便放一个文件）**

**3.1 浏览器或者文件管理器地址栏输入ftp地址（ftp://192.168.0.105）**

![](http://img.shihuidaren.cn/nas/a7262543a5b8022aaf0d3c9d78c480b9.png)

  输入FTP地址时发现需要用户和密码（这个看情况，有些默认就可以直接访问了），可是配置的过程中好像没有看到设置用户和密码的步骤，没关系，我们可以自己设置。

**3.2 IIS管理器中的FTP身份验证里面配置启用匿名身份认证（无密码）**

![](http://img.shihuidaren.cn/nas/8758100297fa74954fa14fd034239ea0.png)

![](http://img.shihuidaren.cn/nas/7758b5be62481b84748afb1101401232.png)

**3.3 再次测试，浏览器或者文件管理器地址栏输入ftp地址（ftp://192.168.0.105）**

![](http://img.shihuidaren.cn/nas/969a12bc00c8c4af04ca912b8581d50f.png)

**3.4 配置FTP站点用户名和密码**

**3.4.1IIS管理器中的FTP身份验证里面配置禁用匿名身份认证同时启用基本身份认证（再次访问就会要求输入用户名和密码）**

![](http://img.shihuidaren.cn/nas/7210a4ee2d54b9f084f058e87e47d5fe.png)

**3.4.2此电脑（桌面计算机图标右键）—\>管理-\>本地用户和组-\>用户-\>新建一个用户，并设置密码**

![](http://img.shihuidaren.cn/nas/fc31619dd0ba0b79033719d8b589a137.png)

![](http://img.shihuidaren.cn/nas/d9fba0d58016f4d67bf04a4131409420.png)

![](http://img.shihuidaren.cn/nas/10259389f6dde8116962af402fea7dd3.png)

![](http://img.shihuidaren.cn/nas/dbac29e54e591acf8b4e3f7fa9ef3ed2.png)

**备注：**细心的你可以能已经发现这里的账户就是我们计算机的账户，所以说我们应该可以使用自己登录电脑的用户名和密码来登录FTP站点，不用新建这个test用户都可以。

**3.4.3再次测试，浏览器或者文件管理器地址栏输入ftp地址，输入用户名:test，密:test（ftp://192.168.0.105）**

![](http://img.shihuidaren.cn/nas/a7262543a5b8022aaf0d3c9d78c480b9.png)

![](http://img.shihuidaren.cn/nas/969a12bc00c8c4af04ca912b8581d50f.png)

  到此一个简单的FTP服务器搭建成功，同一个局域网内其他人可以访问到你的电脑了，可以相互传输文件。传输文件是一个用途，本文主要是想用来当做一个java
上传下载项目的测试服务器。



错误处理：参考系列文章，注意更换非IE浏览器尝试连接或专门软件连接，可能问题就不存在了。还可以尝试关闭IE浏览器的保护模式。有文章说20/21端口均需要映射到外网。端口需要添加防火墙。

[FTP文件夹打开错误，Windows无法访问此文件夹](https://jingyan.baidu.com/article/b7001fe1829deb0e7282ddb7.html)

[外网无法内网FTP （200 Type set to A）](https://blog.csdn.net/qq_31698883/article/details/53856474)

