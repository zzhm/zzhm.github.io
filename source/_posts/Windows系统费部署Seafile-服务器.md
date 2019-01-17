---
title: Windows系统费部署Seafile 服务器
mathjax: false
date: 2018-10-16 19:50:40
id: Windows-seafile
tags:
- seafile
- nas
- win10
- 网站
categories:
- 生活
- nas
---

本教程说明了Windows系统下部署Seafile服务器的问题。

<!---more--->

### 安装 Python 2.7.11 32 位版本

下载并安装 [python 2.7.11 32 位版本](http://python.org/ftp/python/2.7.11/python-2.7.11.msi)。将 python2.7 的安装路径添加到系统的环境变量中 (PATH 变量)。比如：如果您将 python 2.7.11 安装在`C:\Python27`路径下，那么就将`C:\Python27`添加到环境变量中。

**注意**：一定要使用 Python 2.7.11 32 位版本。64 位版本或不是 2.7.11 的版本不能工作。

### 下载并解压 Seafile 服务器

获取 [Seafile 服务器](http://seafile.com/download/)的最新版本。为 Seafile 服务器程序创建一个新的文件夹，比如`C:\SeafileProgram\`。请记住此文件夹的位置，我们将在以后用到它。将**seafile-server_5.0.3_win32.tar.gz**解压到`C:\SeafileProgram\`目录下。现在，您的目录结构应该像如下这样：

```
C:\SeafileProgram
         |__ seafile-server-5.0.3
```

## 启动与初始化

### 启动 Seafile 服务器

在`C:\SeafileProgram\seafile-server-5.0.3\`文件夹下，找到**run.bat**文件并双击，以启动 Seafile 服务器。此时，您应该注意到 Seafile 服务器的图标已经出现在您的系统托盘中。

### 选择一个磁盘作为 Seafile 服务器数据的存储位置

现在，您可以在弹出的对话框中选择一个磁盘，以便存储 Seafile 服务器的数据：请确保选择的磁盘拥有足够的剩余空间。点击*确认*按钮后， Seafile 将会在您选择的磁盘下为您创建一个名为`seafile-server`的文件夹。这个文件夹就是 Seafile 服务器的数据文件夹。如果您选择*D*盘，那么数据文件夹为`D:\seafile-server`

### 添加管理员帐号

右击 Seafile 服务器的系统托盘图标， 选择"**添加管理员帐号**"选项。在弹出的对话框中输入您的管理员用户名和密码。如果操作成功， Seafile 服务器托盘图标处会弹出一个气泡提示您"添加 Seahub 管理员账户成功"

### 配置 Seafile 服务器

初始化服务器之后，还需配置以下选项，否则不能进行文件的上传下载:

- 访问服务器的 Web 界面 (打开 `http://<您的 IP 地址>:8000`)，用管理员账号登录

- 点击左上角的扳手图标，进入管理员界面，在进入"设置"标签

- 将**SERVICE_URL**的值配置成`http://<您的 IP 地址>:8000`。比如您的 Windows 服务器地址为 *192.168.1.100*， 那么配置成`SERVICE_URL = http://192.168.1.100:8000`

- 将**FILE_SERVER_ROOT**的值配置成`http://<您的 IP 地址>:8082`。比如您的 Windows 服务器地址为 *192.168.1.100*， 那么配置成`SERVICE_URL = http://192.168.1.100:8082`

  不能通过 Web 端上传或下载文件时，请先确保您已经正确设置了 `SERVICE_URL` 和 `FILE_SERVER_ROOT`。这可以通过 Web 端"管理员界面->设置"中更改。

### 安装 Seafile 为 Windows 服务

将 Seafile 服务器作为 Windows 服务安可在您的所有用户注销后 Seafile 服务器能够继续保持运行，系统启动时，即使没有用户登录， Seafile 服务器也会开始运行。如何作为 Windows 服务安装？

- 右击 Seafile 服务器托盘图标，选择"安装为 Windows 服务"选项
- 在弹出的对话框中，点击*是*按钮

如果操作成功，将会弹出一个对话框提示您"已经成功安装 Seafile 服务"。

### 所用端口说明

Seafile 服务器由两个组件组成，默认情况下用到 8000, 8082 两个端口号 (TCP)。所有端口的相关配置都记录在`ccnet.conf`文件和`seafile.conf`文件中。`seahub` 是 Seafile 服务器的 Web 端。 端口号可改，但`seafile.conf `文件和"管理员界面->设置" 中的 SERVICE_URL需要同时改动。seafile fileserver负责为 Seahub 处理文件的上传和下载。桌面客户端会连接这个端口来同步文件，所以不要修改这个端口。 

### windows下seafile fsck工具使用方法

关于windows如何使用fsck工具导出数据这个功能，官网上可以说是介绍的很不详细，帮助手册里说的`seaf-fsck.sh`翻遍了整个文件夹也没有找到。以下是自己花了一下午时间琢磨出来的：

1、找到`seaf-fsck.exe`所在目录，在我电脑上的路径是`D:\Seafile\seafile-server-6.0.7\seafile\bin`。在空白位置按住shift点击鼠标右键，选择”在此处打开命令窗口“

2、输入以下指令 `seaf-fsck.exe -E E:\a  -c D:\seafile-server\ccnet -d D:\seafile-server\seafile-data -F D:\seafile-server\conf`

​     seafile服务器内的文件就会导出到E盘内名字为a的文件夹内，其中`D:\seafile-server`是我电脑内服务器的路径，视你的实际情况修改该路径。

另外，再附赠一个修复的指令

`seaf-fsck.exe -r  -c D:\seafile-server\ccnet -d D:\seafile-server\seafile-data -F D:\seafile-server\conf`

### 外网访问

- 路由器端口映射：8000和8082口

- 添加防火墙

  `netsh advfirewall firewall add rule name=”seafile web” protocol=TCP dir=in localport=8000 action=allow`

  `netsh advfirewall firewall add rule name=”seafile trans” protocol=TCP dir=in localport=8082 action=allow`

- 访问时须带有端口号8000