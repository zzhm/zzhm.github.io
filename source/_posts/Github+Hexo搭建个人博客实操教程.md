---
title: Github+Hexo搭建个人博客实操教程
id: github-hexo-blog-construction
date: 2018-04-27 20:00:08
categories:
- 生活
- 网站
tags:
- 博客
- github
- hexo
---

## 准备工作

### 安装软件

需要安装的软件有[**Node.js**](https://nodejs.org/en/)、[**Git**](https://git-scm.com/downloads)、[**Pandoc**](http://www.softpedia.com/get/Programming/Other-Programming-Files/Pandoc.shtml)、[**Typora**](https://www.typora.io/#windows)、[**Word2Md**](http://www.writage.com/)

### 搭建环境

在电脑上找一个存放网站的地方，新建文件夹，以hexo为例，在hexo文件加上鼠标右键，选择“`Git Bash Here`”，打开命令窗口，输入命令。

- 安装hexo，`npm install hexo-cli -g`，输入`hexo -v`，检查hexo是否安装成功

- 初始化，`hexo init`

- 安装依赖组件，`npm install`
- 安装编译器，`npm install hexo-deployer-git --save`
- 本地查看

输入`hexo g`编译文件，输入`hexo s`，开启服务器，访问该网址，本地体验Hexo（http://localhost:4000/），假如页面一直无法跳转，那么可能端口被占用了。此时我们ctrl+c停止服务器，接着输入“`hexo server -p 端口号`”来改变端口号，比如5000 （`hexo s -p 5000`）

<!--- more --->

## 连接Github

### 配置Github

注册Github账户，并新建项目（repository），项目必须要遵守格式：**账户名.github.io**，不然接下来会有很多麻烦。并且需要勾选**Initialize this repository with a README**。

在建好的项目右侧有个settings按钮，点击它，向下拉到GitHub Pages，你会看到那边有个网址，访问它，你将会惊奇的发现该项目已经被部署到网络上，能够通过外网来访问它。

![](http://img.shihuidaren.cn/blog/1108615-20171021223928802-1978574025.png)

​

### 配置SSH

- 设置Git的user name和email（如果是第一次的话）,这里“xujun”可以替换成自己的用户名，邮箱可以替换成自己的邮箱

  ```
  git config --global user.name "xujun"
  git config --global user.email "gdutxiaoxu@163.com"
  ```

- 输入`ssh-keygen -t rsa -C “929762930@qq.com”`，连续三个回车，生成密钥，最后得到了两个文件：id_rsa和id_rsa.pub（默认存储路径是：`C:\Users\Administrator\.ssh`）。

- 输入`eval "$(ssh-agent -s)"`，添加密钥到ssh-agent

- 再输入`ssh-add ~/.ssh/id_rsa`，添加生成的SSH key到ssh-agent

- 登录Github，点击头像下的settings，添加ssh（新建一个new ssh key，将id_rsa.pub文件里的内容复制上去）

- 输入`ssh -T git@github.com`，测试添加ssh是否成功。如果看到Hi后面是你的用户名，就说明成功了

### 配置Deployment

* 在hexo文件夹中，找到_config.yml文件，修改repo值（在末尾）

  ![](http://img.shihuidaren.cn/blog/1108615-20171021235812974-84318377.png)

  repo值是你在github项目里的ssh（右下角）

  ![](http://img.shihuidaren.cn/blog/1108615-20171021235722365-818312042.png)

### 测试文章

* 新建一篇博客，执行命令：`hexo new post “博客名”`。这时候在文件夹_posts目录下将会看到已经创建的文件。
* 使用编辑器编好文章。
* 使用命令：`hexo d -g`，生成以及部署。
* 部署成功后访问你的地址：`http://用户名.github.io`。

##  主题安装

### 安装主题

安装NexT，在其文件夹中鼠标右键，点击Git Base Here。输入命令：

`git clone https://github.com/iissnan/hexo-theme-next themes/next`

[更多主题](https://hexo.io/themes/)

### 启用主题

启用主题，在站点目录中（blog），打开配置文件_config.yml，修改theme：next

### 主题设置

* 更换主题样式，在next主题目录下的_config.yml文件中将scheme设定为Pisces

* 语言设定，在**站点根目录下**修改配置文件_cofig.yml中的language为zh-Hans（简体中文）

* 修改菜单项，在**主题目录下**修改配置文件_cofig.yml中的menu，增添一个something（注：千万不要在这设置中文，后面的值那是查找文件的地方！若你的站点运行在子目录中，请将链接前缀的 `/` 去掉）

  ![](http://img.shihuidaren.cn/blog/1108615-20171022141652959-1002921163.png)

  这些配置都要与你主题目录下的languages文件中对应的yml文档里配置相关联。比如你在站点根目录中的配置文件设置language为zh-Hans，那么就要进入到主题目录下的languages文件中修改zh-Hans.yml，这样才能显示出菜单项新增的中文内容（以something为例子）

  ![](http://img.shihuidaren.cn/blog/1108615-20171022113026318-265709135.png)

* 设置菜单项图标，对应的字段是menu_icons。格式为item name：icon name，其中item name与所配置的菜单名字对应，icon name是Font Awesome图标的名字。而 enable 可用于控制是否显示图标，你可以设置成 false 来去掉图标。（本机出问题，无法显示icon，还未解决，求指导）

  ![](http://img.shihuidaren.cn/blog/1108615-20171022172514318-965544980.png)

* 设置侧栏位置，修改主题目录下sidebar的position值

* 设置头像，在站点根目录下载配置文件中新增avatar，值设置为头像的链接地址。地址可以是网络地址，也可以是本地地址（放置在source/images/ 目录下）

  ![](http://img.shihuidaren.cn/blog/1108615-20171022131752974-1304180995.png)

* 设置文章代码主题，在主题目录下修改配置文件highlight_theme，默认值为nomal。可以设置为night

* 添加标签页面，前面通过修改next主题下的`_config.yml`文件中的menu选项，可以在主页面的菜单栏添加标签选项，但是此时点击标签，跳转的页面会显示page not found。此时我们要新建一个页面`hexo new page tags`

  在新建的index.md文件中添加type: "tags"

  ![](http://img.shihuidaren.cn/blog/1108615-20171022134821896-1919728091.png)

  当要为某一篇文章添加标签，只需在b`log/source/_post`目录下的具体文章的tags中添加标签即可，如：

  ![](http://img.shihuidaren.cn/blog/1108615-20171022135128006-180948588.png)

  

* 添加关于我页面，步骤和以上差不多`hexo new page about`

  在新建的index.md文件中添加如下内容

![](http://img.shihuidaren.cn/blog/1108615-20171022153607990-455892762.png)

## 公式渲染

Hexo 默认选用是 Markdown 渲染引擎是 [marked](https://github.com/chjj/marked) ([hexo-renderer-marked](https://github.com/hexojs/hexo-renderer-marked))。除了默认的 marked，目前在 Hexo 上已有的其它比较好且还在维护的 Markdown 渲染引擎也就有 [hexo-renderer-markdown-it](https://github.com/celsomiranda/hexo-renderer-markdown-it) 和 [hexo-renderer-pandoc](https://github.com/wzpan/hexo-renderer-pandoc)，其中前者 markdown-it 支持 [`CommonMark`](http://commonmark.org/) 标准，后者则支持 [`Pandoc`](http://pandoc.org/)。

写公式的话可以试下 MathJax 吧，MathJax 渲染器在 Hexo 上的实现也有的。具体自行谷歌：[Hexo MathJax](https://www.google.com/?q=Hexo+MathJax)。

如何使用别的 Markdown 渲染引擎。先安装Pandoc，然后把 hexo 里 `package.json` 的 Markdown 渲染器依赖换掉，比如 `hexo-renderer-marked` 换成 `hexo-renderer-pandoc`。然后重新编译一下文件就可以了。

## 域名绑定

当然，你不绑定域名肯定也是可以的，就用默认的 `xxx.github.io` 来访问，如果你想更个性一点，想拥有一个属于自己的域名，那也是OK的。

首先你要注册一个域名，域名注册以前总是推荐去`godaddy`，现在觉得其实国内的阿里云也挺不错的，价格也不贵，毕竟是大公司，放心！

绑定域名分2种情况：带www和不带www的。

域名配置最常见有2种方式，CNAME和A记录，CNAME填写域名，A记录填写IP，由于不带www方式只能采用A记录，所以必须先ping一下`你的用户名.github.io`的IP，然后到你的域名DNS设置页，将A记录指向你ping出来的IP，将CNAME指向`你的用户名.github.io`，这样可以保证无论是否添加www都可以访问，如下：

![](http://img.shihuidaren.cn/blog/20160823_191336_238_8683.png)

然后到你的github项目根目录新建一个名为CNAME的文件（无后缀），里面填写你的域名，加不加www看你自己喜好，因为经测试：

- 如果你填写的是没有www的，比如 mygit.me，那么无论是访问 [http://www.mygit.me](http://www.mygit.me/) 还是 [http://mygit.me](http://mygit.me/) ，都会自动跳转到 [http://mygit.me](http://mygit.me/)
- 如果你填写的是带www的，比如 www.mygit.me ，那么无论是访问 [http://www.mygit.me](http://www.mygit.me/) 还是 [http://mygit.me](http://mygit.me/) ，都会自动跳转到 [http://www.mygit.me](http://www.mygit.me/)
- 如果你填写的是其它子域名，比如 abc.mygit.me，那么访问 [http://abc.mygit.me](http://abc.mygit.me/) 没问题，但是访问 [http://mygit.me](http://mygit.me/) ，不会自动跳转到 [http://abc.mygit.me](http://abc.mygit.me/)

另外说一句，在你绑定了新域名之后，原来的`你的用户名.github.io`并没有失效，而是会自动跳转到你的新域名。

## 永久链接

一般来说，URL只能使用英文和数字和一些标点符号表示。这是因为网络标准RFC 1738 做了硬性规定。虽然在Hexo中引用`:title`可以显示中文的网址，但是复制粘贴到记事本会发现得到的是一大串百分号之类的“乱码”（其实这并不是乱码，而是中文被转码成十六进制编码的结果），看起来不怎么好看。

**在permalink中使用文章id替代“:title”**

在官方文档[永久链接（Permalinks） | Hexo](https://hexo.io/zh-cn/docs/permalinks.html)一章中有这样一段描述：

![](http://img.shihuidaren.cn/blog/5069493.jpg)

`permalink`的变量就这几个，其中**文章id**这个变量非常有用。

我们可以在博客根目录的配置文件（`_config.yml`）中这样修改：

```
#permalink: :year/:month/:day/:title # 这是原配置
permalink: :year/:id.html # 替换为此新配置12
```

并且在`.\scaffolds\post.md`中修改为：**（注意新增了一个`id:`）**

```
---
title: {{ title }}
id: 
date: {{ date }}
updated: {{ date }}
categories:
tags:
permalink: 
---123456789
```

在我们的具体文章中，你可以使用**任意字符串**作为此文章的id，例如：

```
---
title: 如何让你的Hexo博客网址使用全英文路径
id: 123456789-abcd
date: 2017-12-30 20:57:46
updated: 2017-12-30
categories: 后台01 文档管理
tags:
permalink:
---
```

### 清理Git缓存

```
#清空git缓存
git rm -r --cached .
git add .
git commit -m 'update'
```



### 参考文章

[1] http://blog.haoji.me/build-blog-website-by-hexo-github.html

[2] http://www.cnblogs.com/fengxiongZz/p/7707568.html

[3] https://www.cnblogs.com/fengxiongZz/p/7707219.html

[4] http://theme-next.iissnan.com/third-party-services.html

[5] https://hexo.io/zh-cn/docs/index.html

[6] https://www.cnblogs.com/MuYunyun/p/5927491.html

[7] https://blog.csdn.net/likianta/article/details/79343427