---
title: hexo常用命令笔记
mathjax: false
date: 2018-11-29 11:13:08
id: hexo-commands
tags:
- 网站
- 博客
- 生活
categories:
- 生活
- 网站
---

## hexo

```
npm install hexo -g #安装  
npm update hexo -g #升级  
hexo init #初始化
```

<!---more--->

## 简写

```
hexo n "我的博客" == hexo new "我的博客"  #新建文章
hexo p == hexo publish
hexo g == hexo generate                #生成
hexo s == hexo server                  #启动服务预览
hexo d == hexo deploy                  #部署
```

## 服务器

```
hexo server                #Hexo 会监视文件变动并自动更新，您无须重启服务器。
hexo server -s             #静态模式
hexo server -p 5000        #更改端口
hexo server -i 192.168.1.1 #自定义 IP

hexo clean                 #清除缓存 网页正常情况下可以忽略此条命令
hexo g                     #生成静态网页
hexo d                     #开始部署

```

### 监视文件变动

```
hexo generate              #使用 Hexo 生成静态文件快速而且简单
hexo generate --watch      #监视文件变动
```

### 完成后部署

> 两个命令的作用是相同的
> `hexo generate --deploy`
> `hexo deploy --generate`

```
hexo deploy -g
hexo server -g
```

## 草稿

```
hexo publish [layout] <title>
```

## 模版

```
hexo new "postName" 		#新建文章
hexo new page "pageName" 	#新建页面
hexo generate 				#生成静态页面至public目录
hexo server			 		#开启预览访问端口（默认端口4000，'ctrl + c'关闭server）
hexo deploy 				#将.deploy目录部署到GitHub
```

```
hexo new [layout] <title>
hexo new photo "My Gallery"
hexo new "Hello World" --lang tw
```

| 变量   | 描述         |
| ------ | ------------ |
| layout | 布局         |
| title  | 标题         |
| date   | 文件建立日期 |

```
title: 使用Hexo搭建个人博客
layout: post
date: 2014-03-03 19:07:43
comments: true
categories: Blog
tags: [Hexo]
keywords: Hexo, Blog
description: 生命在于折腾，又把博客折腾到Hexo了。给Hexo点赞。
```

## 模版（Scaffold）

```
hexo new photo "My Gallery"
```

| 变量   | 描述         |
| ------ | ------------ |
| layout | 布局         |
| title  | 标题         |
| date   | 文件建立日期 |

## 设置文章摘要

```
以上是文章摘要 <!--more--> 以下是余下全文 
```

## 写作

```
hexo new page <title>
hexo new post <title>
```

| 变量     | 描述                       |
| -------- | -------------------------- |
| :title   | 标题                       |
| :year    | 建立的年份（4 位数）       |
| :month   | 建立的月份（2 位数）       |
| :i_month | 建立的月份（去掉开头的零） |
| :day     | 建立的日期（2 位数）       |
| :i_day   | 建立的日期（去掉开头的零） |

### 推送到服务器上

```
hexo n 			#写文章
hexo g 			#生成
hexo d 			#部署,可与 hexo g 合并为 hexo d -g
```

## 报错

### 1.找不到git部署

```
ERROR Deployer not found: git
```

**解决方法**

```
npm install hexo-deployer-git --save
```

### 3.部署类型设置git

hexo 3.0 部署类型不再是`github`，`_config.yml` 中修改

```
# Deployment
## Docs: http://hexo.io/docs/deployment.html
deploy:
  type: git
  repository: git@***.github.com:***/***.github.io.git
  branch: master
```