---
title: Windows Server 2016和J3455搭建私有云
mathjax: false
date: 2018-10-16 20:29:51
id: windows-J3455
tags:
- nas
categories:
- 生活
- nas
---

Windows Server 2016和J3455搭建私有云

<!---more--->

- 硬件平台

  J3455主板，4G金士顿DDR3 1600内存条

- 软件

  win server 2016 standard x64、xampp 3.2.2、python 2.7、Seafile 6.07、Kodexplore 4.36、小白文件管理器、小白播放器、daemon sync 

与win10类似。安装前更新一下J3455主板的Bois。从官网下载Win10 驱动。大白菜PE安装。

未遇到[教程](https://www.chiphell.com/thread-1845619-1-1.html)中说的网卡问题。整体按照上述教程进行。没搞软路由，注意点有：

- 计算机名和用户名不要一样
- IE增强的安全配置，一定要改
- 没搞软路由
- 媒体播放通过小白播放器和小白文件管理解决，很好用
- 远程桌面，映射3389端口并设置防火墙放行就行
- Seafile和Kodexplore做云盘，还在考察中

DDNS[方案一](https://github.com/kaedei/aliyun-ddns-client-csharp)

1. 在阿里云申请一个域名，将此域名添加一个子域（如`www`），并设置为A类型记录，IP地址随便填写一个（程序会自动修改）
2. 到阿里云域名控制台[申请AccessId Key和Secrect](https://ak-console.aliyun.com/#/accesskey)
3. Clone本项目代码到本机，使用VS2013或更高版本编译
4. 将程序exe和其他dll文件复制到服务器上。在exe文件同目录下创建一个文本文件并命名为`config.txt`
5. `config.txt`文件的内容有四行，请修改成对应的值：
   - 第一行：Access Id Key，例如 *DR2DPjKmg4ww0e79*
   - 第二行：Access Id Secret，例如 *ysHnd1dhWvoOmbdWKx04evlVEdXEW7*
   - 第三行：域名，例如 *google.com*
   - 第四行：子域名，例如 *www*

  6.在服务器上运行主exe即可.本程序依赖外部web服务来获取本机的公网IP地址，默认使用的公网IP地址查询服务来自ip138.com。您可以在`App.config`文件中修改对应的网址。

使用VS2013 + C#开发，支持.NET 3.5和.NET 4.5。建议通过任务计划定时调用（如每小时），程序会判断是否需要修改A记录



[方案二](https://www.52z.com/soft/600310.html)

[方案三](https://www.cnblogs.com/weapon/p/6772253.html?utm_source=itdadao&utm_medium=referral)