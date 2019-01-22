---
title: 科研：使用ipv6访问google
mathjax: false
date: 2018-05-11 19:27:26
id: ipv6-google
tags:
- ipv6
- 生活
- 工具
categories:
- 科研
- 工具
---

华科是网络是教育网，且具有ipv6/ipv4双栈协议，就是联网时会自动给你分配ipv4和ipv6地址。 
配置步骤： 

1. win+R ,输入 cmd,点击enter ,进入命令框 
2. 输入 ipconfig/all 查看你是否有ipv6地址,如下图所示。 

若有则继续执行以下步骤，否则参考[华科ipv6服务](http://ncc.hust.edu.cn/xsfw/IPV6fw.htm) 

3. 点击你的ipv6协议，将dns服务器修改为google的ipv6 dns服务器地址

<!---more--->

```
2001:4860:4860::8888
2001:4860:4860::8844
修改后如下图所示，点击确定。
```

4. 重新联网即可。 

**备注：**用浏览器访问时，请关闭浏览器的代理之类插件



[lennylxx/ipv6-hosts](https://link.zhihu.com/?target=https%3A//github.com/lennylxx/ipv6-hosts)，在这个链接上下载hosts，替换自己电脑上的hosts，就能上网了。前提是能用ipv6。而且看youtube视频超级快。 （[另外一个](https://github.com/XX-net/XX-Net)）

什么？？？你那里上不了谷歌和谷歌学术？

目前很多科研院校都开放了 IPv6 通道，可以高速访问 Google、Google Scholar、Youtube 等网站，具体可以咨询相关技术人员。https://ipv6.google.com.hk

如果 IPv6 方案不可行，你可以选择使用 Google 的镜像网站，推荐一个非常稳定的谷歌学术镜像网站（**https://scholar.glgoo.org**），访问速度特别快，检索结果也和原版完全一样。

或者使用这个网站（**ac.scmor.com**）查看实时可用的谷歌搜索镜像和谷歌学术镜像网站，点击链接即可访问。

对于文献全文后面的参考文献列表中的文献，一般直接复制单条到谷歌学术中检索就能找到对应的文献，要注意复制之后可能会产生多余的空格把期刊名隔开，这时要先删除多余的空格或者乱码，保证期刊名、年份、页码都正常显示，而且中间用空格间隔即可。

 

**教育网DNS服务器:**

北京邮电大学DNS服务器 
2001:da8:202:10::36 

2001:da8:202:10::37

北京科技大学DNS服务器 
2001:da8:208:10::6

**加入”Google Over IPv6”计划的DNS:**

Hurricane Electric DNS

ordns.he.net 2001:470:20::2 74.82.42.42

tserv1.fmt2.he.net 2001:470:0:45::2 72.52.104.74

tserv1.dal1.he.net 2001:470:0:78::2 216.218.224.42

tserv1.ams1.he.net 2001:470:0:7d::2 216.66.84.46

tserv1.mia1.he.net 2001:470:0:8c::2 209.51.161.58

tserv1.tor1.he.net 2001:470:0:c0::2 216.66.38.58

ns.ipv6.uni-leipzig.de 2001:638:902:1::10 139.18.25.34

**Google Public DNS**

google-public-dns-a.google.com 2001:4860:4860::8888 8.8.8.8

google-public-dns-b.google.com 2001:4860:4860::8844 8.8.4.4