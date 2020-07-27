---
title: J3455平台安装OMV及nextcloud的安装和配置说明-nginx插件版
mathjax: false
date: 2018-12-17 09:55:25
id: omv
tags:
- omv
- nas
- 网站
- nextcloud
- j3455
categories:
- 生活
- nas
---

安装参考该教程：[使用Open Media Vault和NextCloud构建家庭私有云](http://www.azurew.com/6350.html)

这里增加一些需要注意的点的说明

### OMV 安装

1.安装完成后，我们可以在机器界面上看到已经有ip地址192.168.2.120 下面一行显示登陆网页用户名admin 密码openmediavault。后面就全部用网页来管理了。如果不显示，则登录系统后输入`ip addr` 寻找ip地址。

<!---more--->

2.使用网页界面安装更新和插件容易卡住，实际是网速慢。可以用命令安装更新。

```
apt-get update
apt-get upgrade
```

3.SAMBA共享共享慢的问题

4.每次更改后等一会，选择应用配置。

5.我在网络接口里设置了固定ip，出现故障，原因不明。

6.SSL证书可以自己在阿里云/腾讯云等网站申请。格式不对可以在腾讯云中转换，基本思路是，在腾讯云中上传证书，再下载即可得到crt格式的证书。

> 这个就不用说太多，在阿里云申请的证书就去阿里云下载，下载Nginx服务器的证书 获得两个文件，一个是.kye后缀的，一个是.pem后缀的。登录腾讯云ssl管理（https://console.cloud.tencent.com/ssl），点击上传证书，将.pem文件中的内容复制到证书中，.key证书中的内容复制到私钥中，最后点击上传上传完成后，可以重新在腾讯云下载Nginx服务器，即为crt文件的证书。

### nextcloud 配置

````
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
````

### 文件夹权限设置

```
# 切成 root 用户， 不切换的话下面所有命令都要在前面加 sudo
sudo su

# 解压镜像
unzip nextcloud-12.0.4.zip

# 创建目录并移动程序到你要的目录里
mkdir /www && mv nextcloud /www/nextcloud

# 修改权限相关
cd /www
chmod -R 0770 nextcloud/
chown -R www-data nextcloud/
chgrp -R  www-data nextcloud/

# 创建数据目录并修改权限
mkdir nextcloud.data
chmod -R 0770 nextcloud.data/
chown -R www-data nextcloud.data/
chgrp -R  www-data nextcloud.data/
```

### 缓存设置,修复opcache错误

修改 `/etc/php/7.0/fpm/php.ini` 文件内容： 

```
opcache.enable=1
opcache.enable_cli=1
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=10000
opcache.memory_consumption=128
opcache.save_comments=1
opcache.revalidate_freq=1
```

### 数据库操作

````
# 设置 root 密码
mysqladmin -u root -p password YOUR_PASSWORD_HERE

# 用 root 登入
mysql -u root -p

# 这下面的所有命令都在 SQL Shell 里面执行：

# 创建数据库
create database nextcloud;

# 创建用户及加权限
create user 'www'@'localhost' identified by 'YOUR_PASSWORD_HERE';
grant all privileges on nextcloud.* to 'www'@'localhost' identified by 'YOUR_PASSWORD_HERE';
````

### You are using a fallback implementation of the intl extension

```
apt-get install php7.0-intl
systemctl restart php7.0-fpm
```

### PHP 的设置似乎有问题, 无法获取系统环境变量. 使用 getenv(\”PATH\”) 测试时仅返回空结果.

从宝塔文件管理，打开/www/server/php/72/etc/php-fpm.conf，在其尾部添加一行

```
env[PATH] = /usr/local/bin:/usr/bin:/bin:/usr/local/php/bin
```

保存并重启PHP即可解决该问题

### 参考资料

[用Nextcloud在树莓派上布置你的个人网盘NAS](https://www.jianshu.com/p/bbf24ac2fac1)

[腾讯云第三方SSL证书托管将阿里云pem格式转换成crt](https://www.4xseo.com/blog/3804/)