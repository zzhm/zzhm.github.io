---
title: markdown快速入门
mathjax: false
date: 2020-09-20 14:27:57
id: markdown-rumen
tags:
- 软件
- 教程
categories:
- 实用教程
---



### 段落和换行

一个段落只是一个或者多个连续的文本行。在Markdown源代码中，段落由多个空白行分隔。在Typora，你只需要按 `回车键`来创建一个新的段落。

按`Shift`+`Enter`创建一个换行符。然而，大多数的编辑器会忽略单行中端，为了让其它的Markdown编辑器识别你的换行符，可以在行尾留下两个空格或者插入` <br>`。

<!---more--->

### 标题

标题在行的开始使用1-6个散列字符，对应1-6的标题级别

### 嵌套区块引用

在typora中，只需输入`>`后跟引用内容就会生成一个块引用。 Typora将为您插入适当的`>`或换行符。 通过添加额外的`>`级别可以允许在另一个块引用内嵌一个引号。

```markdown
这是一个包含两段的blockquote。这是第一段

> 这是第二段。Vestibulum enim wisi, viverra nec,
>
> > 另一个有一个段落的blockquote。
> >
> > > 一个段落的blockquote。
```

> 这是一个包含两段的blockquote。这是第一段
>
> > 这是第二段。Vestibulum enim wisi, viverra nec,
> >
> > > 另一个有一个段落的blockquote。
> > >
> > > > 一个段落的blockquote。

### 列表

输入`* list item 1`将创建一个无序的列表，`*`符号可以使用`+`或者`-`代替。

输入`1. list item 1`将创建一个有序列表，他们的Markdown源代码如下：

```markdown
## un-ordered list
*   Red
*   Green
*   Blue

## ordered list
1.  Red
2.  Green
3.  Blue
```

> **Note**: 
>
> - +-*三者可以混用，但会导致行间距不一致。
>
> - 其一，将文字前的数字序号从`1. 2. 3.` 修改为 `1. 1. 1.` 并不影响最终的显示效果；
> - 其二，若希望有序列表从`8.` 开始编号，则第一行改写为 `8. 打开冰箱` 即可。
> - 若需缩进，只需在 `-` 前加两个空格或四个空格 (敲一个 `Tab` 键相当于四个空格)。

### 任务列表

任务列表是标有[ ] 或者[x] (未完成或者完成)的列表，可以通过单击项目之前的复选框来更改完成/未完成的状态。例如：

```markdown
- [x] 已完成记事
- [ ] 待办记事
  - [ ] 吃啥？
    - [ ] 去吃个 subway 吧？
```

- [x] 已完成记事
- [ ] 待办记事
  - [ ] 吃啥？
    - [ ] 去吃个 subway 吧？

### 代码块

Typora只支持Github Flavored Markdown中的栅栏。不支持原始代码块中的标记。

使用代码块很容易，输入```然后按下`entre`键。在```之后添加一个可选的语言标识符，我们将通过它进行语法高亮：

例如：

```gfm
function test(){
  console.log("notice the blank line before this function?");
}
```

语法高亮：

``` java
String str = new String("hello world!");
System.out.println(str)
```

### 数学公式

可以使用**MathJax**渲染*LaTeX*数学表达式。点`段落—>公式块`打开公式块。

输入`$$`，然后按下`Enter`键将触发一个接收*Tex/LaTeX*源码的输入范围。例如：
$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
 \mathbf{i} & \mathbf{j} & \mathbf{k} \
 \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \
 \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \
 \end{vmatrix}
$$

```markdown
$$
 \mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
 \mathbf{i} & \mathbf{j} & \mathbf{k} \
 \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \
 \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \
 \end{vmatrix}
$$
```

 在Markdown源代码文件中，数学公式是被`$$`标记的*LaTeX*表达式：

> 注意，Typora在渲染模式`shift+enter`,源代码模式用`enter`
>
> 

### 表格

输入`|第一个标题|第二个标题|`然后按下`enter`键讲话创建一个有两列的表格。

创建表之后，在该表上将弹出一个表的工具栏，您可以在其中调整大小，对齐或删除表。 还可以使用上下文菜单来复制和添加/删除列/行。

以下描述可以跳过，因为表的markdown源代码是由typora自动生成的。表格中可以使用链接、粗体、斜体、或删除线等格式。

```markdown
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```

最后，通过冒号`：`在标题行中，可以定义文本对齐方式，最左侧的冒号表示左对齐，最右侧的冒号表示右对齐，两次都有冒号表示中心对齐。

### 脚注

```markdown
标注：你可以使用脚注像这样[^脚注]

引用：[^脚注]: 这里写脚注的*文本*
```

实现效果：

这里需要参考[^脚注1]

[^脚注1]: 脚注1的内容.

### 链接

Markdown支持两种风格的链接：内联和引用。在两种样式中，链接文本由[方括号]分隔。

要创建内联链接，请在链接文本的关闭方括号后立即使用一组常规括号。 在括号内，将链接所在的网址与链接的可选标题一起放在引号中。 例如：

```markdown
This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.
```

实现效果：

This is [an example](https://link.jianshu.com?t=http://example.com/"Title") inline link. (`This is [`](http://example.com/))

[This link](https://link.jianshu.com?t=http://example.net/) has no title attribute. (`[This link](http://example.net/) has no`)

#### 内部链接

你可以将标题设置为一个连接，我们会创建一个书签，允许你点击标题后，跳转到文章中指定的部分，例如：

Ctrl(On Mac：Command) + Click[This link](#内部链接)会跳转到块元素标题的位置 。

```
[This link](#内部链接标题)
```

#### 参考链接

参考样式链接使用第二组方括号，您可以在其中放置您选择的标签来标识链接：

```markdown
This is [an example][id] reference-style link.

Then, anywhere in the document, you define your link label like this, on a line by itself:

[id]: http://example.com/  "Optional Title Here"
```

在typora中，他们会被渲染为：

This is [an example][id1] reference-style link. Then, anywhere in the document, you define your link label like this, on a line by itself:

[id1]: http://example.com/  "Optional Title Here"

隐式链接名称快捷方式允许您省略链接的名称，在这种情况下，将链接文本本身用作名称。 只需使用一组空白方括号 - 例如将Google“Google”链接到google.com网站，您可以简单地写：
$$
[Google][]
And then define the link:

[Google]: http://google.com/
$$
[Google][]
And then define the link:

[Google]: http://google.com/

### URL地址

Typora允许插入URL作为链接，用尖括号包起来，`<`尖括号`>`，就变成了[i@typora.io](https://link.jianshu.com?t=mailto:i@typora.io).

Typora也会自动链接标准的URLs，例如：[www.google.com](https://link.jianshu.com?t=http://www.google.com)

### 分割线

在空白行输入`***`或者`---` 然后按`enter`键会出现分割线

### 目录

输入`[toc]`，然后按`enter`键将创建一个“目录”部分，从一个人的写作中提取所有标题，其内容将自动更新。

### 删除线

GFM添加了标准Markdown语法没有的下划线语法。

`~~Mistaken text.~~` 会变成~~Mistaken text.~~

### 下划线

下划线由原始的HTML提供。

`Underline` 变成<u>Underline</u>.

### emoji表情：happy

输入emoji语法：`:smile:`:smile:

用户可以通过按“ESC”键触发表情符号的自动完成建议，或在首选面板上启用后自动触发。 此外，还支持从菜单栏中的`Edit - >Emoji＆Symbols`直接输入UTF8表情符号。

### HTML

Typora无法呈现HTML片段。 但是Typora可以解析并渲染非常有限的HTML片段，作为Markdown的扩展，包括：

- 下划线Underline: `underline`
- 图片Image: `![](http://upload-images.jianshu.io/upload_images/2018694-1074db4f76d21622.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)` (And `width`, `height` attribute in HTML tag, and `width`, `height`, `zoom` style in `style` attribute will be applied.)
- 注释Comments: ``
- 超链接Hyperlink: `[link](http://typora.io)`.

他们的大部分属性，样式或类将被忽略。 对于其他标签，typora会将其作为原始HTML片段呈现。

但是这些HTML将被导出打印或导出。



### 下标和上标

为了使用这个特性，请先在`Preference`面板中的`Markdwn`选择开启。

- 使用`~`来包裹下标内容，例如：`H~2~O`,H2O， `X~long\ text~`/，Xlong text
- 使用`^`包裹上标内容，例如`X^2^`,X2

### 高亮

为了使用这个特性，请先在`Preference`面板中的`Markdwn`选择开启。

使用`==`包裹突出的内容，例如：`==highlight==`，显示为：==highlight==





作者：RenS_
链接：https://www.jianshu.com/p/b30955885e6d

