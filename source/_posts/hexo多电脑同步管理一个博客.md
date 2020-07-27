---
title: hexo多电脑同步管理一个博客
mathjax: false
date: 2018-05-30 14:34:04
id: hexo-multi-pc
tags:
- 网站
- 生活
- hexo
categories:
- 生活
- 网站
---

主要的思路是利用git分支实现。hexo生成的静态博客文件默认放在master分支上。 hexo的源文件（部署环境文件）可以都放在hexo分支上（可以新创建一个hexo分支），换新电脑时，直接`git clone hexo分支`进行博客的书写和编译等工作 。

<!---more--->

在Github的username.github.io仓库上新建一个hexo分支

**A电脑备份博客内容到github** 

```
git init  #第一次可能需要
git add . #添加目录下所有文件 
git commit -m “更新说明” #提交并添加更新说明 
git remote add origin https://github.com/yourname/yourname.github.io.git 
git push -u origin hexo:hexo #推送更新到远程仓库，出错加  -f （强制推送） -u（设定默认）
```
**B电脑拉下远程仓库文件**

在B电脑上同样先安装好node、git、ssh、hexo，然后建好hexo文件夹，安装好插件，（然后选做：将备份到远程仓库的文件及文件夹删除），然后执行以下命令：

```
git init 
git remote add origin https://github.com/yourname/yourname.github.io.git 
git fetch --all    #下面这两句可以换成  git pull origin hexo:hexo 
git reset --hard origin/hexo    #忽略本地当前分支的更改，并将其指向origin/hexo

npm install #第一次下拉需要安装一下依赖项，后面如果更改仍然需要刷新
```

**发布博客后同步**

在B电脑发布完博客之后，记得将博客备份同步到远程仓库。 
执行以下命令：

```
git add #可以用git master 查看更改内容  
git commit -m "更新信息"  
git push -u origin hexo:hexo #以后每次提交可以直接git push
```

**平时同步管理**

每次想写博客时，先执行：

```
git pull  #git pull origin hexo:hexo
```

进行同步更新。 

发布完文章后同样按照上面的 发布博客后同步。 同步到远程仓库。

错误：fatal: remote origin already exists.  

先删除远程 Git 仓库

> $ git remote rm origin



参考命令

[Git push 命令](https://www.yiibai.com/git/git_push.html)

[Git pull 命令](https://www.yiibai.com/git/git_pull.html)

```
$ git push <远程主机名> <本地分支名>:<远程分支名>
$ git pull <远程主机名> <远程分支名>:<本地分支名>
$ git clone <版本库的网址>
$ git fetch origin master
$ git remote add [shortname] [url]
```

![img](https://www.yiibai.com/uploads/allimg/140613/0A025G34-0.jpg) 