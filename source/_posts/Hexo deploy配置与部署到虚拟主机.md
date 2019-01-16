---
title: Hexo与阿里云虚拟主机搭建博客
mathjax: false
date: 2019-01-08 21:05:44
id: hexo-vps
tag:
- hexo
- 网站
- 博客
- OMV
category:
- 博客
---

发布到虚拟主机有很多方法，我们当然挑简单的来

### 配置Hexo

[官方文档配置说明](https://link.jianshu.com?t=https://hexo.io/zh-cn/docs/configuration.html)
 设置博客标题，作者，主题等信息已经足够详细了，我主要说一下 deploy部分,使用FTP的方式把网站内容推送到虚拟主机上

新版hexo取消了默认安装ftpsync， 会报错 `ERROR Deployer not found: ftpsync` 手动安装即可

```
$ npm install -g hexo-cli  
$ npm install hexo-deployer-ftpsync --save

$ mkdir newHexo
$ cd newHexo
$ hexo init  

$ hexo new "文章标题"
```
<!---more--->
### 推送配置
```
deploy:
  type: ftpsync
  host: bxu******.my3w.com //主机地址
  user: bxu******          //用户名
  pass: *********          //密码
  remote: /htdocs          //目录，应该所有阿里云虚拟主机的网站内容目录都是这个，不是根目录 /
  port: 
  ignore: .DS_Store
  connections: 
  verbose: true 
```

### 生成发布文件

```
$ hexo generate
```

此时如果你要手动部署（那我们还配置deploy搞毛用）， 使用你的FTP工具直接将 public 下的文件放进 虚拟主机的 htdocs 目录下，刷新你的网站，就看到效果了

### 一键发布

```
$ hexo deploy
```

刷新网站， 就可以看到你写的东西了

 

 参考

https://www.jianshu.com/p/8c55f103e8b4

https://zymin.cn/arcticle/github-hexo-blog-construction.html

 

 