---
title: Endnote使用技巧|经验|陷阱
mathjax: false
date: 2018-05-02 10:43:09
updated:
id: endnote-skills
tags: 
- 工具
- endnote
- 文献
- 科研
categories: 
- 科研
- 工具
---

### 1. 安装版本问题。

安装版本问题（Windows-Office-EndNote）。最新版Endnote X8 只能安装在 windows 7 以上，XP 不支持。Word 2016 只能关联 X8。EndNote  X7 可以关联 Word 2010, Word 2013，EndNote  X5 只能关联 Word 2010。建议 X8-Word 2016/2013 或 X7-Word 2013 或 X5-Word 2010，X5 与 X7，X8 会有版本兼容问题而导致显示不正常。目前推荐 X7-Word 2013 组合，功能够用强大,是最常见的配制工。但 X5-Word 2010 速度更快，配置低的电脑建议使用。

<!--- more --->

### 2. 与 Word 关联问题。

一般安装马上完成时，会有提示是否对 Word 进行配置，选择是，一般都会成功，安装好后 Word 中会出现工具条。安装完后有的小伙伴的word中不会显示endnote这个插件，可按照下述步骤手动关联：

- 依次点击文件--选项--加载--com加载项--转到
- 之后找到你endnote的安装目录，在里面找到configuration endnote.exe这个可执行文件，双击
- 选中configuration endnote component，单击next
- 在cite while you write复选框前打钩，单击next
- 等待一会就会出现一个提示窗口，单击finish即可，在打开你的温word就关联起来了

<center>
![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/endnote-skill/endmoteword.png)
</center>

### 3. Endnote 库的问题。

安装好后新建一个库，这个库的文件名自己取，把它保存到方便找到的盘和目录。**【敲黑板！重点！】**这个库包括名称相同的一个文件和一个文件夹，这两个你必须同时拷贝，放在 U 盘随身携带，只要在安装有 Endnote 的电脑上，打开「自己取名字.enl」，里面包含你所有的文献。
注：网上还有 Endnote X7 绿色免安装版，放 U 盘里，配合自己的文献库，移动办公那就一个爽字。

### 4. 建立 Group 的问题。

每个作者不止一篇论文，那么可以建立不同的 Group，对应一篇论文，把所有这篇论文相关的文献全部放在这个 Group 里面，方便管理，相当于 Windows 的一个文件夹，所有的 Groups 全部在上面的「自己取名字.enl」和「自己取名字.Data」这两个之中。

### 5. 性能提升秘籍，增加实用

5.1 写 SCI 文献，一般不会少于 20 篇参考文献，我们在插入文献或者修改论文时，必然伴随着文献在论文中顺序的改变，每次改动就会出现如此画风（图 X）。这个等待时间随着插入文献数的增加而增加，此时电脑进入假死状态，相当使人抓狂，如果你没耐心而乱点鼠标，企图妄想加快速度，Duang，就会变成真死机，Word 文档被破坏，如果还没有保存，那就要彻底爆走了。
想解决这个问题，第一种方法是关闭即时格式化.

<center>
![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/endnote-skill/closee.png)
</center>

5.2 关于参考文献格式的修改，想补充一点以进一步提升性能。Endnote 所有文献格式文件均放在安装目录的Styles文件夹下。

常规有近 6 000 个格式文件，在选择时会有比较长的读取等待时间，老机器又会造成假死机，建议把这个目录里的文件全部移出到备份目录，仅留下需要用的格式文件，本人留下的是 Numberd.ens，这个格式最常见。

需要另外格式时，查看杂志社网站，均会有说明用哪种格式，找到对应文件，拷贝到 Styles 目录中，再在 Endnote 中选择就 OK 了，如果要作少量修改，可以点击 Edit - Output Style – Edit 「…」，修改后的格式文件也放在这个目录里，你可以拷贝出来，放 U 盘随身携带。这些工作都可以在论文全部完成后集中进行，以免写作时分心。

5.3 欧洲杂志投稿时要求把表图都放在论文的最后，作为附录形式，那么插入的参考文献就在所有的图表后面了，而我们想把参考文献放在论文文本的最后面，但是要在附录图表之前。

这个问题 Endnote 配合 Word 完美解决。我们只需要在 Word 表图附录的第一页开头位置插入一个分节符号， 再在 Endnote 中编辑相应的格式文件，点击 sections（分节设置），选择其中的 「Create a bibliography for each section」，这样 Endnote 就会把参考文献插入在分节符的前面那一页的最后，即表图附录的前面。分节同样特别适合于编撰书籍，因为每一个章节最后都要附上参考文献。

<center>
![](https://zymin-1255632454.cos.ap-shanghai.myqcloud.com/endnote-skill/fenjie.png)
</center>

5.4 **【敲黑板！重点！】**论文中插入文献之前必须去除重复文献，最好在导入文献库后马上进行，在菜单中选择 references – find duplicates，会自动查找重复的文献，弹出对话框，选择保留其中一个。
6.一般选择「#数字」小的那个，因为那是最早加入的文献，很有可能已经被引用，把它删除就会出现错误。如果没有去除文献，很容易出现问题，即同一篇当成两篇不同的文献在论文不同位置被引用，最后的参考文献列表中出现两篇相同的文献。这种低级错误投稿时必须避免。

**下载地址：**

````
链接：https://pan.baidu.com/s/1wXJGCxPdNm236ZJKWe0StQ 密码：904n
````