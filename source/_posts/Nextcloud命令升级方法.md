---
title: Nextcloud命令升级方法
mathjax: false
date: 2019-08-27 13:41:32
id: nextcloud-update
tags:
- nextcloud
categories:
- 实用教程
---

较大的NextCloud实例更新系统版本时可能出现如下错误：

> **Verifying integrity**
>
> Parsing response failed. <html> <head><title>504 Gateway Time-out</title></head>
>  <body bgcolor="white"> <center><h1>504 Gateway 
> Time-out</h1></center> 
> <hr><center>nginx/1.12.2</center> </body> 
> </html>

<!---more--->

查找官方论坛发现[解决方案。](https://help.nextcloud.com/t/updater-app-runs-into-timeout/12891/3)

由于php执行有时间限制，较大的nextcloud实例在更新操作时容易出现超时而报错；

对此可修改超时参数，或在命令行中执行更新操作（命令行中没有超时限制）。

具体更新操作如下：

在bash终端中执行：

> sudo -u www-data php /path/to/nextcloud/updater/updater.phar

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/1566884676438.png)

进行命令更新，并使用occ进行更新系统，并关闭维护模式：

> sudo -u www-data php /path/to/nextcloud/occ upgrade 
> sudo -u www-data php /path/to/nextcloud/occ maintenance:mode --off

（其中路径需改为nextcloud的绝对路径，www-data改为php进程使用的账户。）