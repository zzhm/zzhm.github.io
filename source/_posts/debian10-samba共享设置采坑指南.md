---
title: debian 10 + samba共享设置采坑指南
mathjax: false
date: 2020-04-30 14:47:22
id: debian10-samba
tags:
- nas
- 私有云
categories:
- 生活
- 博客
---

> 用root账户安装，以免权限问题

- 安装

  ```
  apt-get install samba
  ```

> 注意：若提示有依赖问题，就把相应的软件卸载掉先，apt-get autoremove 

<!---more--->

- 新建账户

```
smbpasswd -a username   #然后输入密码，
pdbedit -w -L #列出现有的Samba用户列表
```

> 注意这个账户必须是系统已经有的！！！！

- 新建目录

```
mkdir -p  /srv/smbshare
chmod -R 777 /srv/smbshare  #可以有问题的时候再给权限，有人说给600更安全,不懂
chown username:usergroup  -R  /srv/smbshare 
```

> 目录提前建好，不然会显示网络路径找不到。

- 配置`smb.conf`文件

  目录：`nano /etc/samba/smb.conf`

  在文件的最后按照下述格式添加文件夹就行。

  ```
  [disk1]  # 显示的名称
  path = /srv/smbshare/disk1  #文件在服务器上的路径
  writable = yes
  guest ok = yes
  write list = username
  validusers = username
  display charset = UTF-8
  unix charset = UTF-8
  dos charset = cp936
  ```

> 默认会显示一个名为用户名的文件夹，若不想显示，注释掉smb.conf中[homes]项就可以

- 设置启动服务

```
service smbd restart  #重启 
systemctl enable nmbd.service  #设置开机服务
```

另附共享选项及说明

```
[共享名称]:共享中看到的共享目录名
comment = 共享的描述. 
path = 共享目录路径(可以用%u、%m这样的宏来代替路径如:/home/share/%u) 
browseable = yes/no指定该共享是否在“网上邻居”中可见。
writable = yes/no指定该共享路径是否可写。
read only = yes/no设置共享目录为只读(注意设置不要与writable有冲突) 
available = yes/no指定该共享资源是否可用。
admin users = bobyuan，jane指定该共享的管理员,用户验证方式为“security=share”时，此项无效。 
valid users = bobyuan，jane允许访问该共享的用户或组-“@+组名” 
invalid users = 禁止访问该共享的用户与组(同上) 
write list = 允许写入该共享的用户
public = yes/no共享是否允许guest账户访问。 
guest ok = yes/no意义同“public”。
create mask = 0700指定用户通过Samba在该共享目录中创建文件的默认权限。0600代表创建文件的权限为rw-------
directory mask = 0700指定用户通过Samba在该共享目录中创建目录的默认权限。0600代表创建目录的权限为rwx---
```



