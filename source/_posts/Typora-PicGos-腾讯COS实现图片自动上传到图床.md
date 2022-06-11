---
title: Typora+PicGo+腾讯COS实现图片自动上传到图床
mathjax: false
date: 2020-03-30 11:52:34
id: picgo
tags:
- hexo
- 博客
- 图床
categories:
- 实用教程
---

Hexo博客，利用Typora+PicGo+腾讯COS实现图片自动上传到图床。

windows用户请下载最新版本的`exe`文件.

网址：https://github.com/Molunerfinn/PicGo/releases

注意：请确保你安装了 Node.js， 并且版本 >= 8。

<!---more--->

## PicGo设置

打开PicGo，找到图床设置，界面如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200330124015976.png)

密钥获取

![picgo设置界面](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200330124725478.png)



图中参数含义：

#### V4版本说明

v4版本是这个：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200330124659890.png)

需要登录腾讯云控制台。打开[密钥管理](https://console.qcloud.com/cos4/secret)

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200330124820795.png)

按照对应的提示找到自己的`APPID`、`SecretId`、`SecretKey`。

存储的空间名是你的bucket名字。

存储的区域需要额外注意，请到bucket列表里打开需要上传的bucket空间，然后如图可以看到对应的区域以及区域代码，比如我的是`tj`：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200330124746932.png)

对应的区域代码如下：

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200330122625126.png)

如果你想把图片上传到你的bucket空间的某个文件夹下，则需要在PicGo里的`指定存储路径`里加上你的文件夹路径。比如`temp/`（注意一定要加`/`）

#### [#](https://picgo.github.io/PicGo-Doc/zh/guide/config.html#v5版本说明)V5版本说明

**1.** 获取你的APPID、SecretId和SecretKey

访问：https://console.cloud.tencent.com/cam/capi

![img](https://raw.githubusercontent.com/Molunerfinn/test/master/picgo/get_key_id_secret.png)

**2.** 获取bucket名以及存储区域代号

访问：https://console.cloud.tencent.com/cos5/bucket

创建一个存储桶。然后找到你的存储桶名和存储区域代号：

![img](https://raw.githubusercontent.com/Molunerfinn/test/master/picgo/get_bucket_area.png)

v5版本的存储桶名称格式是`bucket-appId`，类似于`xxxx-12312313`。存储区域代码和v4版本的也有所区别，v5版本的如我的是`ap-beijing`，别复制错了。

**3.** 选择v5版本并点击确定

![img](https://raw.githubusercontent.com/Molunerfinn/test/master/picgo/choose_v5.png)

然后记得点击`设为默认图床`，这样上传才会默认走的是腾讯云COS。

## Typora设置图片设置

```
文件==>偏好设置==>设置图片插入模式
```

直接粘贴从网站复制的图片提醒自动上传失败，原因不明。新建了一个`tmp`文件夹作为过渡，现在应该是复制网站的图片先保存到`tmp`文件夹，然后由PicGo上传。

![Typora设置](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/picgo-2.0.gif)



## 手动上传方式

单张图片：

```
图片上右键->上传图片
```

多张图片：

```
格式->图像->上传全部图片
```



### 一个问题

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200401124823836.png)

```
你这个是PicGo Server的端口不是36677，去PicGo设置里调整一下Server的端口吧。改成36677才可以。
```

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/image-20200401124907544.png)



Typora：https://support.typora.io/Upload-Image/

官方指南：https://picgo.github.io/PicGo-Doc/zh/guide/

据说还有很多插件：https://github.com/PicGo/Awesome-PicGo