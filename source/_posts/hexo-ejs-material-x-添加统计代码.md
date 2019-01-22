---
title: hexo+ejs+material x 添加CNZZ统计代码
date: 2019-01-17 15:34:11
id: hexo+ejs+material
tags:
- hexo
- 博客
- j3455
category:
- 生活
---

Hexo博客+ejs+material x 主题，添加统计代码。

先要在博客主题配置文件`D:\hexo\themes\material-x\_config.yml`添加一行代码：

> cnzz: true

<!---more--->

这里这个cnzz的名字可以自己取；然后在`D:\hexo\themes\pacman\layout\_partial `里面创建一个 `cnzz.ejs`文件；把cnzz给的代码复制进去；

```
<% if (theme.cnzz){ %> //前面要添加的代码

//这里添加复制的CNZZ代码

<% } %> //后面要添加的
```

把中间的代码换了就行；然后再在scripts.ejs的后面添加上一行代码就可以显示了（这里的位置可以自己换，可以不是`footer.ejs`，或者是`head.ejs`，看自己的喜好）

> <%- partial('cnzz') %>

对百度统计也可以进行同样的处理；

```
<% if (theme.cnzz){ %>//前面要添加的代码
//百度统计的代码
<% } %>
```


与上面的操作基本一致只是取得名字不一样。

上面的是一种方法；

如果嫌麻烦的话直接就在`footer.ejs`的后面添加cnzz的代码；直接就可以显示了（同理，可以添加在其他位置），貌似添加在这里速度最快。

````
<% if (theme.cnzz){ %> //前面要添加的代码

//这里添加复制的CNZZ代码

<% } %> //后面要添加的
````



参考链接：https://blog.csdn.net/whjkm/article/details/37884563 