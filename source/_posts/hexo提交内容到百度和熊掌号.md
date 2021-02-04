---
title: hexo提交内容到百度和熊掌号
mathjax: false
date: 2019-01-08 20:42:11
id: hexo-baidu-submits
tag:
- hexo
- 网站
- 博客
category:
- 实用教程
---

某些主机，比如Github，禁止百度爬虫访问博客，导致博客无法被百度收录。多亏百度提供了主动提交的接口，这才有了个补救的方法。

除此之外， 使用主动推送还会达到如下功效：

- 及时发现：可以缩短百度爬虫发现您站点新链接的时间，使新发布的页面可以在第一时间被百度收录
- 保护原创：对于网站的最新原创内容，使用主动推送功能可以快速通知到百度，使内容可以在转发之前被百度发现

<!---more--->

## hexo-baidu-url-submit

首先，在Hexo根目录下，安装本插件：
`npm install hexo-baidu-url-submit --save`

## baidu_url_submit 配置

```
baidu_url_submit:
  count: 1000 ## 提交最新的一个链接
  host: alili.tech ## 在百度站长平台中注册的域名
  token: xxxxx ## 请注意这是您的秘钥， 所以请不要把博客源代码发布在公众仓库里!
  path: baidu_urls.txt ## 文本文档的地址， 新链接会保存在此文本文档里
  xz_appid: 'xxxxxx' ## 你的熊掌号 appid
  xz_token: 'xxxxxx' ## 你的熊掌号 token
  xz_count: 10 ## 从所有的提交的数据当中选取最新的10条,该数量跟你的熊掌号而定
```

## deploy 配置

```
deploy:
- type: baidu_url_submitter # 百度
- type: baidu_xz_url_submitter # 百度熊掌号
```

### 参考

[Hexo Baidu URL Submit](https://github.com/huiwang/hexo-baidu-url-submit/blob/master/README.md#baidu_url_submit-配置)