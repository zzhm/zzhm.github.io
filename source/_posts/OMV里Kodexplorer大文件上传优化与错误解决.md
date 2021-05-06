---
title: OMV里Kodexplorer大文件上传优化与错误解决
mathjax: false
date: 2020-03-29 12:00:26
id: omv-kodexplorer
tags:
- omv
- nas
categories:
- 实用教程
---

最近停了Nextcloud，打算用作为主力了，因此优化了一波。基本情况：OMV+nginx插件搭建的kodexplorer。

上传大文件时发现，基本超过1G以上的大文件上传，经过合并等待时间之后，基本都会显示上传失败。但是多等待一会儿之后，刷新文件夹，文件实际是上传成功了的。据人指点“最后合并上传失败很可能是登录超时引起的”。

![](https://gitee.com/zihm/images/raw/master/hexo/20210506133935.jpeg)

<!---more--->

首先明确可道云没有对上传下载做任何限制，速度快慢和网络环境有关。可道云是基于http上传，所以和其他http上传速度基本一致；可以对比其他web系统或网站说附件上传速度。同其他例如webdav、FTP、QQ传输等软件底层协议不一样；传输速度也会不一样。

传输速度受三方面影响：

**本机客户端**：网卡、连接方式(有线、无线)、本机磁盘IO负载情况；
**网络环境**：网络带宽、wifi还是网线等造成的影响；网络环境复杂、或使用人多时路由器或交换机处理速度也都会是瓶颈之一。
**服务器**：受服务器负载、磁盘IO、服务器网络带宽等影响。同时受并发影响；比如20M上行带宽,10个人同时在上传或下载,那么每个人平均就是2M/s
可道云为了能在更多的服务器环境下良好运行，各方面配置是以兼容性为主，可能并不是最优配置。性能调优可以参考配置如下。

**修改php.ini上传限制**

```
max_execution_time = 3600
max_input_time = 3600
post_max_size = '150M'
upload_max_filesize = '150M'
```

注意：这个可以在kod的config文件夹里的`config.php`中修改。

```nginx
define('GLOBAL_DEBUG',0);//0 or 1
define('GLOBAL_DEBUG_HOOK',0);//0 or 1
@date_default_timezone_set(@date_default_timezone_get());
@set_time_limit(3600);//20min pathInfoMuti,search,upload,download...
@ini_set("max_execution_time",3600);
@ini_set("max_input_time",3600);
@ini_set("post_max_size",'150M');
@ini_set("upload_max_filesize",'150M');
@ini_set('memory_limit','500M');//
@ini_set('session.cache_expire',1800);
```

![](https://gitee.com/zihm/images/raw/master/hexo/20210506133946.png)

**修改可道云配置**

在config/下新建 setting_user.php文件;粘贴如下内容；(已存在则略过)

```
<?php
//分片上传: 每个切片5M,需要php.ini 中upload_max_filesize大于此值
$GLOBALS['config']['settings']['updloadChunkSize'] = 1024*1024*5;
//上传并发数量; 推荐15个并发;
$GLOBALS['config']['settings']['updloadThreads'] = 15;
```

**nginx + php-fpm上传优化**

在nginx.conf中添加如下代码，参考,更多nginx优化
使用共享内存做临时存贮提高上传速度，共享内存需要大一些，否则上传大文件内存不足

```
client_body_in_file_only clean;
client_body_temp_path /dev/shm 1 2;
fastcgi_param REQUEST_BODY_FILE $request_body_file;
```

参考：http://bbs.kodcloud.com/d/60





需要注意的是，根据这个网址:http://blog.lovecatcat.com/index.php/archives/17/，我在OMV里设置池和服务器的时候添加了代码。起没起作用我也不确定，因为没有重启服务器。如果上面的操作不行可以加上再试试。

添加池的页面添加了如下代码

```
env[PATH] = /usr/local/bin:/usr/bin:/bin
```

添加服务器的页面的拓展选项里添加了如下代码

```
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
location ~ ^/(data|config|.ht|db_structure.xml|README) {
deny all;
}
location / {
# The following 2 rules are only needed with webfinger
rewrite ^/.well-known/host-meta /public.php?service=host-meta last;
rewrite ^/.well-known/host-meta.json /public.php?service=host-meta-json last;
rewrite ^/.well-known/carddav /remote.php/carddav/ redirect;
rewrite ^/.well-known/caldav /remote.php/caldav/ redirect;
rewrite ^(/core/doc/[^/]+/)$ $1/index.html;
try_files $uri $uri/ index.php;
}
location ~ ^(.+?.php)(/.*)?$ {
try_files $1 = 404;
include fastcgi_params;
fastcgi_param SCRIPT_FILENAME $document_root$1;
fastcgi_param PATH_INFO $2;
fastcgi_param HTTPS on;
fastcgi_pass $socket;
}
# Optional: set long EXPIRES header on static assets
location ~* ^.+.(jpg|jpeg|gif|bmp|ico|png|css|js|swf)$ {
expires 30d;
# Optional: Don't log access to assets
access_log off;
}
add_header Strict-Transport-Security "max-age=15768000; includeSubDomains; preload;";
```

另外附：通过设置nginx的client_max_body_size解决nginx+php上传大文件的问题 

用nginx来做webserver的时，上传大文件时需要特别注意client_max_body_size这个参数,否则会中断在nginx的请求中,在php中是无法记录到访问的. 
一般上传大文件流程： 
首先修改php.ini文件： 

```
file_uploads on 是否允许通过HTTP上传文件的开关。默认为ON即是开 
upload_tmp_dir – 文件上传至服务器上存储临时文件的地方，如果没指定就会用系统默认的临时文件夹 
upload_max_filesize 8m 望文生意，即允许上传文件大小的最大值。默认为2M 
post_max_size 8m 指通过表单POST给PHP的所能接收的最大值，包括表单里的所有值。默认为8M 
```

一般来说，设置好上述四个参数后，在网络正常的情况下，上传<=8M的文件是不成问题的 
但如果要上传>8M的大文件的话，只设置上述四项还不一定能行的通。除非你的网络真有100M/S的上传高速，否则你还得继续设置下面的参数。 

```
max_execution_time 600 每个PHP页面运行的最大时间值(秒)，默认30秒 
max_input_time 600 每个PHP页面接收数据所需的最大时间，默认60秒 
memory_limit 8m 每个PHP页面所吃掉的最大内存，默认8M 
```

但是还是不行，因为的webserver用的是nginx， google了一下，发现在nginx的conf中添加了一个参数： 在nginx.conf中增加一句，重启即可 。默认是1M，需要增大的话。30m表示最大上传30M，需要多大设置多大。

```
client_max_body_size 30m; 
```






