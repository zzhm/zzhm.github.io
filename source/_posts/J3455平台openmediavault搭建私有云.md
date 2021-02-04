---
title: J3455平台openmediavault(OMV)搭建私有云
mathjax: false
date: 2019-10-02 10:25:48
id: J3455搭建私有云
tags: 
- j3455
- omv
- nas
- 软件教程
categories:
- 实用教程
---

- 硬件平台：

J3455主板，4G金士顿DDR3 1600内存条，小机箱，ATX电源（长城BTX_450SE，低载荷风扇可以停转），4T西数红盘、120G固态硬盘

- 软件：

[Seafile](https://www.seafile.com)、[Kodexplorer](https://kodcloud.com/)、[Nextcloud](https://nextcloud.com/)、Onlyoffice、[Aria2](https://hub.docker.com/r/opengg/aria2/)、[阿里云DDNS](https://github.com/honwen/aliyun-ddns-cli)、HeidiSQL、PuTTY

<!---more--->

## U盘安装OMV

### 制作启动盘

制作工具[ether](https://www.balena.io/etcher/)、[源文件](https://sourceforge.net/projects/openmediavault/files/)

### 安装系统

#### 开机按F11，选择从U盘启动

进行安装 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa2.png) 	

选择中文安装，放心不像Ubuntu 16.04 安装的时候用中文还会报错，这个中文挺稳定的 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa3.png) 	

是 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa4.png) 	

大陆就选中国吧 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa5.png) 	

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa6.png) 	

#### 加载完成安装组件，进入初始设置界面  	

主机名我就用默认了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa8.png) 	

这里也默认了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa9.png) 	

输入系统底层的密码，不是web界面的密码 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa10.png) 	 	

#### 选择安装位置，这里装到8G的U盘里 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa12.png) 	

#### 设置镜像源 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa14.png) 	

我就选163了，随便你 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa15.png) 	

中间有一步是配置代理，我手快了没截图就按回车了，不过我想家里应该没人吃饱了去用代理上网吧  	 	

#### 设置启动位置

放sda中，因为这个就是u盘 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa18.png) 	

#### 安装完成重启 

#### 登陆信息

安装完成后，我们可以在机器界面上看到已经有ip地址192.168.2.120 下面一行显示登陆网页用户名admin 密码openmediavault。后面就全部用网页来管理了。 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa20.png) 	

## 配置OMV系统 

我们登陆OMV，输入密码就可以进入主界面 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa21.png) 	

这里就是主界面，很干净方便 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa22.png) 	

## 更新系统 

我们打开更新管理，先更新下系统，打下补丁，以后有更新都在这里可以看到 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa23.png) 	

等更新完成后就可以点击关闭，更新过程中无法关闭 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa24.png) 	

## 安装插件 

插件使用第三方的源，也是他们官方认证的 

http://omv-extras.org/joomla/index.php/guides 	

#### 下载插件包

我们登陆网站在下面有deb包，我们下载后上传到插件页面安装下就能看到其他的插件 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa25.png) 	

#### 上传插件到系统

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa26.png) 	

#### 安装 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa27.png) 	

安装完成后，会自动刷新页面，就会发现插件多了很多 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa28.png) 	

## 设置系统时间 

我们在时间和日期中设置下时区，然后保存下，让时间自动从网络同步 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa29.png) 	

## 常规设置 

在这个设置中，我们可以修改OMV的web端口，网页超时时间，默认5分钟太短了，我设置了长一点 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa30.png) 	

## 硬盘管理 

### S.M.A.R.T. 

开始SMART，这样硬盘出问题能自动检测 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa31.png) 	

这里可以看到硬盘的型号序列号，如果那块硬盘有问题，找起来也方便 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa32.png) 	

### RAID管理 

我们进入RAID管理，然后选下4块盘，设置下RADI 5，名字叫MD0 

linux下面都是用md这个来命名的，所以我也这么叫了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa33.png) 	

创建完成后会进行初始化，下面有初始化的百分比，等初始化完成后在创建文件结构。 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa34.png) 	

### 文件系统 

我们进入文件系统，选择创建，选下我们刚才创建的RAID，然后输下名字继续叫MD0，然后文件系统叫EXT4 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa35.png) 	

选是后会提示你，要被格式化了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa36.png) 	

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa37.png) 	

这时文件系统还是不能用的，我们要选择下挂载 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa38.png) 	

挂载完成 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa39.png) 	

## 设置SAMBA共享 

我家里的NAS我准备建立一个SAMBA的用户，我自己用，然后共享文件3个一个叫**NAS**，包括NextCloud都装在里面，这样我可以方便的直接上去管理，然后一个叫**Download**的文件夹，脱机下载插件下载的文件就放里面，然后一个叫**Software**，我自己的软件都在里面，其他包括我老婆都不用SAMBA，都用NextCloud上面，我尽量让自己的NextCloud上保存的都是轻量级的文件，大容量的就放在SAMBA上。 

你自己想如何设置还是每个人不同的，不用照我的来。 

### 建立用户 

我们先建立一个用户，用于SAMBA共享 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa40.png) 	

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa41.png) 	

### 建立共享文件夹 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa42.png) 	

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa43.png) 	

对每个文件夹添加下用户权限 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa44.png)

### 设置SAMBA 

我们开启下SAMBA，不知道的选项就不用改了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa45.png)	

添加共享文件夹 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa46.png)
	
![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa47.png)

设置好后我发现访问共享不行，然后重启了下服务器ok了，都能看到了，可能是因为我是虚拟机的关系，我朋友直接设置好就可以使用了。我们可以进去然后新建下文件，看看权限是否正确 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa48.png)

# 安装NextCloud 

由于NextCloud没加入OMV 4的官方插件列表中，我们只能手动来了，哎好疼苦 

## 建立SSL证书 

OMV自带了证书功能，所以我们直接使用自带的创建一个证书即可，我直接创建了25年的，这样就不会过期了 

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1570168249650.png)

## 安装Nginx插件 

我们在插件中搜索nginx，然后安装下 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa51.png)	

安装完成我们就能在服务中看到Nginx 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa52.png)

### 添加池 

我们加个池，然后用户名和组选择下，我就用我一开始创建的那个samba的wang这个用户了 

![ ](https://www.azurew.com/wp-content/uploads/2017/07/072717_1509_OpenMediaVa53.png)

在扩展选项中添加下面的内容 

`env[PATH] = /usr/local/bin:/usr/bin:/bin ` 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa54.png)

### 添加服务器 

这里目录就选我前面创建的那个nas目录，端口可以看到我已经变成灰色了，因为我后面一部选择了only ssl，只用ssl了不用普通的端口了，如果你不选只用ssl的话记得把这个端口改掉，80端口和omv的端口冲突了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa55.png)

开启SSL，然后端口可以自己修改下，我们上海电信好像都封掉正常的80和443端口的，证书就是前面创建的证书 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa56.png)

开始php，然后池就选择NextCloud，添加个index.php 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa57.png)

扩展选项把下面的东西都黏贴进去 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa58.png)

```
## 更多选项里粘贴一下内容

client_max_body_size 10G; # set max upload size
fastcgi_buffers 64 4K;

rewrite ^/caldav(.*)$ /remote.php/caldav$1 redirect;
rewrite ^/carddav(.*)$ /remote.php/carddav$1 redirect;
rewrite ^/webdav(.*)$ /remote.php/webdav$1 redirect;

index index.php;
error_page 403 /core/templates/403.php;
error_page 404 /core/templates/404.php;

location = /robots.txt {
allow all;
log_not_found off;
access_log off;
}

location ~ ^/(data|config|\.ht|db_structure\.xml|README) {
deny all;
} 

location / {

# The following 2 rules are only needed with webfinger
rewrite ^/.well-known/host-meta /public.php?service=host-meta last;
rewrite ^/.well-known/host-meta.json /public.php?service=host-meta-json last; 
rewrite ^/.well-known/carddav /remote.php/carddav/ redirect;
rewrite ^/.well-known/caldav /remote.php/caldav/ redirect; 
rewrite ^(/core/doc/[^\/]+/)$ $1/index.html;
try_files $uri $uri/ index.php;
}

location ~ ^(.+?\.php)(/.*)?$ {
try_files $1 = 404;
include fastcgi_params;
fastcgi_param SCRIPT_FILENAME $document_root$1;
fastcgi_param PATH_INFO $2;
fastcgi_param HTTPS on;
fastcgi_pass $socket;
}

 
# Optional: set long EXPIRES header on static assets
location ~* ^.+\.(jpg|jpeg|gif|bmp|ico|png|css|js|swf)$ {
expires 30d;

# Optional: Don’t log access to assets
access_log off;
}
add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";
#add_header Strict-Transport-Security “max-age=15768000; includeSubDomains; preload;”;
```

## 安装MySQL插件 

NextCloud需要用到MySQL数据库，所以我们安装下MySQL的插件 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa59.png)

安装完成后，启用下，然后下面的SQL management也启用下，那个是网页管理数据库的功能，好了之后我们就可以点击重设边上的SHOW来网页管理数据库 

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1570168444858.png)	
### 重设MySQL密码

默认的MySQL用户名是root，密码为空，我们设置一个安全一点，点击reset password重设密码 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa61.png)	

然后我们点击show，然后输入用户名密码登陆数据库 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa62.png)

### 创建nextcloud数据库

我们新建一个数据库专门用于nextcloud 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa63.png)

 	

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa64.png) 	

创建完成 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa65.png) 	

## 安装PHP插件

我们安装NextCloud时还需要几个php的插件，我们安装下 

我们使用ssh工具，登陆下服务器，然后执行下面的命令 

安装php5-gd模块：`apt-get install php5-gd `

安装php5-curl模块：`apt-get install php5-curl `

安装php-pclzip模块：`apt-get install php-pclzip `

## 下载并安装NextCloud

https://download.nextcloud.com/server/releases/nextcloud-12.0.0.zip 	

我们直接下载nextcloud，然后解压，之后敲到我们前面SAMBA创建的那个nas的目录下 

![ ](https://www.azurew.com/wp-content/uploads/2017/07/072717_1509_OpenMediaVa70.png) 	 	

输入https://nas的ip加上前面我设置的86端口，来进行安装 

我是这个，你可以根据自己的来https://192.168.2.120:86/index.php 	

输入你的信息包括数据库，和默认的管理员密码  	

安装完成 

然后我们通过samba，可以看到下面的data路径里admin账户，files文件里面都是我们上传到nas上的文件， 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa74.png) 	

不过需要说明的是，我们直接把文件放到这个目录下是不行的，在nextcloud界面看不到，只能通过nextcloud的网页上传上来才能看到，不过看到的文件就是原文件  	

### 安装apc插件

`root@server:~# apt-get install php-apc `	

在NextCloud的`config.php`配置文件中加入

`‘memcache.local’ => ‘\OC\Memcache\APCu’, `

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1570167539410.png)

重启 php-fpm:
`root@server:~# /etc/init.d/php5-fpm restart`

### 修复opcache错误

## 设置外网访问 

我们需要在我们的路由器上设置下外网访问，这样才能让外部访问我们，就开放下86端口即可，这部我就不截图了，很简单的，而且每个路由器不同，懂的自然知道怎么加端口，不懂的我路由器和你不同我加了你也不知道怎么弄。 

另外我们要修改下网站的代码，否则打开会有问题 

我们打开nextcloud的config目录中的config.php文件 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa79.png)

我们要在哪个array中加入我们的域名，另外下面的https后面原来也是内网的ip地址，改成域名，这样外网访问过来就不会有问题了 

![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/1570168635826.png)

当然请在自己的路由器上设置好ddns，这样外网都用域名访问就ok了 

# 安装客户端

下面的页面中有app的下载地址，ios是收费的6块钱好像，其他不收费，我这里就测试下windows pc的客户端，手机我就不测试了 

[https://nextcloud.com/install/#install-clients](https://nextcloud.com/install/) 	 	

安装完成后我们输入域名 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa82.png) 	

跳出来证书不安全，因为是我们自己创建的，不管继续点ok，记得勾下总是信任该证书 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa83.png) 	

输入用户名密码 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa84.png) 	

这里可以选要同步的内容，我因为会把视频也放上面，太大了，所以就手动选择同步内容 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa85.png) 	

选择同步个小的文件夹测试 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa86.png) 	

下面有个本地存放这个文件夹的位置，可以自行修改到需要的位置，然后点连接 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa87.png) 	

完成了 

![ ](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/072717_1509_OpenMediaVa88.png) 	

手机客户端官方的是收费的6块，下面这个是免费的第三方的 

# 其他 

## 注意事项见[此文](https://zymin.cn/arcticle/omv.html)

参考文章

[官方文档](https://openmediavault.readthedocs.io/en/latest/installation/index.html)

[TechnoDadLife](https://forum.openmediavault.org/index.php/Thread/23005-Installation-and-Setup-Videos-Beginning-Intermediate-and-Advanced/?postID=175857#post175857)

[王哥哥](https://www.azurew.com/6350.html)