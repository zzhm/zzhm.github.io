---
title: Windows系统用kodexplorer可道云搭建私有云
mathjax: false
date: 2018-10-16 20:09:41
id: windows-kodexplorer
tags:
- nas
categories:
- 生活
- nas
---

windows系统，基于Xampp和kodexplorer搭建私有云。

<!---more--->

1. 下载Xampp 安装包。主要官网现在访问不了，那到中文的官网下载 ：

2.安装Xampp 程序。

3.xmapp服务的开启。

（1）点击Apache 中的start开启服务；点击mysql中的start开启服务 ；

（2）点击Apache中的admin 访问 http://localhost/xampp/splash.php

（3）点击“中文”访问：http://localhost/xampp/index.php ，出现以下页面，基本完成了xampp的安装了。

4.配置数据库：phpMyAdmin操作数据库和通过doc界面连接数据库或是通过mysql客户端界面控制。

## KodExplorer可道云程序的下载、解压和配置

1.下载最新版本的KodExplorer程序

下载地址：http://kodcloud.com/download.html

2. Apache和MySQL正常启动后，点击Explorer,进入服务器目录

3. 找到htdocs文件夹，将里面的内容清空，然后将kodexplorer可道云文件解压后放置到此目录。

4. 设置kodexplorer可道云安装目录为读写权限（777）

5. 浏览器访问http://127.0.0.1/，可以开始使用了（点击Apache-->Admin浏览亦可）

## 局域网访问

在本机上装了一个XAMPP做开发环境,但同事不能访问我的phpmyadmin,记得以前开过XAMPP的局域网访问,觉得这次也可以.

但看网上的方案是把`httpd-xampp.conf`中的

```
<LocationMatch "^/(?i:(?:xampp|licenses|phpmyadmin|webalizer|server-status|server-info))">
    Order deny,allow
    Deny from all
    Allow from ::1 127.0.0.0/8 
    ErrorDocument 403 /error/HTTP_XAMPP_FORBIDDEN.html.var
</LocationMatch>
```

Deny from all注释掉就行了
但是我的conf文件是这么写的:

```
<LocationMatch "^/(?i:(?:xampp|security|licenses|phpmyadmin|webalizer|server-status|server-info))">
    Require local
    ErrorDocument 403 /error/XAMPP_FORBIDDEN.html.var
</LocationMatch>
```

按照上面的改法没用!!!
后来我将下面两行注释掉,换成Allow from all就好了

```
Require local
ErrorDocument 403 /error/XAMPP_FORBIDDEN.html.var
```

## 外网访问

- 局域网设置，如上

- 端口映射：可道云默认使用80端口，但是80端口一般是被封的，因此外部需要使用其他端口，比如说81.

- 防火墙

  `netsh advfirewall firewall add rule name=”kod” protocol=TCP dir=in localport=80 action=allow`



网上有这个[windows服务器安装XAMPP并绑定域名详解](https://www.weixing.me/webdesign/windows-cvm-xampp-domain/),未验证是否可行。