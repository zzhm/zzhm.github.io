---
title: 教程：Win10共享打印机设置（无需密码访问）
mathjax: false
date: 2018-05-13 18:10:34
id: win10-printer-share
tags:
- win10
- 教程
- 生活
categories:
- 教程
---

升级到Win10系统后，很多朋友在打印机共享方面遇到了问题，如Win10共享打印机，别的电脑不能访问，访问要密码，XP访问需要凭据，输入密码也无法连接等种种情况，下面小编分享下Win10共享打印机所需要的一些设置，通过连接测试。可以帮助用户实现打印机共享无需密码连接，有兴趣的朋友不妨看看。

<!---more--->

## 预备工作

安装打印机驱动，确定打印机在本地可以使用。

## 开启共享

开始里面搜索打印机，按照下图顺序，进入管理打印机属性界面

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/059444f1f0acda38a443db35da0b3b38.png)

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/347acc1481496145b89b3a30cd2d845d.png)

勾选共享此打印机
![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/a187765572e06ccd0dfc45fb41af0c23.png)

## 修改本地安全策略

（这里的修改很重要，win7和win8【拒绝从网络访问这台计算机】默认为空，只有win10默认添加了guest）

1、WIN+R然后“运行”里输入secpol.msc，打开本地安全策略

【本地策略】—【安全选项】—【网络访问：本地账户的共享和安全模型】---改来宾

【本地策略】—【安全选项】—【账户：来宾账户状态】---改启用

【本地策略】—【用户权限分配】—【拒绝从网络访问这台计算机】---删除guest

如下三图所示：

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/222414472d8b8641df3770779e0ab17a.jpg)

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/4e00efd6b519da2dcbf76f8317ec984b.jpg)

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/953c315575e567dff9452d154bf497e5.jpg)

## 修改高级共享设置

```
控制面板--->网络和共享中心--->选择家庭组和共享选项--->更改高级共享设置
<当前配置文件>
```

- 启用网络发现

- 启用文件和打印机共享


![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/4c890d9a9701515ae9230bf22b947770.jpg)

\<所有网络\>

- 关闭公用文件夹共享

- 为使用40位或56位加密的设备启用文件共享
- 关闭密码保护共享

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/0eeaf62d499f9204b88168c0e0cb513b.jpg)

在需要局域网共享的文件夹右键菜单选择：共享—特定用户
添加everybody，按实际修改everybody权限，【读取】或者【读写】（添加guest也应该可以滴）
无需用户密码的文件夹共享搞好，打印机的共享应该就OK了。
ps.一般在专用网络启用共享，如果第一次发现网络的时候没有配置成共享的话，默认被配置成公用网络。
修改成专用方法：打开你的网络设置 ——选择你正在使用的网络——查找设备和内容——【开】

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/4803ff39764b60487259877d1058e9d7.jpg)

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/ec559bfece262151b413b83dd4b3715e.png)

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/win10-printer/835d2c6698b11def7372d2f6d2cf6125.png)

相信通过上面的设置后，大家就能成功的实现Win10打印机共享,并无障碍访问了\~希望对大家有帮助。



[更多Win10 相关文章阅读](https://zymin.cn/tags/win10/)