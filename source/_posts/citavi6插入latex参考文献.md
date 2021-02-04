---
title: citavi6插入latex参考文献
mathjax: false
date: 2020-06-23 16:08:14
id: citavi-latex
tags:
- citavi
- 科研
- 文献
- 论文
categories:
- 实用教程
---

You are using LaTeX to write a thesis or journal submission. With Citavi you can insert your sources and quotations with the corresponding BibTeX-Key into your TeX document. Citavi will automatically create the BibTeX file that your TeX program needs in order to create the final version of your document.

Do you want to create a publication using an Online LaTeX editor like [Overleaf](https://www.overleaf.com/)? [Our video shows how to do so](https://vimeo.com/283962071).

The formatting depends on the LaTeX style you select; Citavi has no influence on the appearance of your footnotes and bibliography.

<!---more--->

**1** Under **Tools** > **Options** > **Citation**, enable the **LaTeX support** checkbox.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455.png)

**2** Select your TeX editor. In the LaTeX project folder box, select the folder that your editor uses for LaTeX projects. Citavi needs to use this folder in order to make images available to your editor. Click **OK**. Citavi creates BibTeX keys for all of the references in your project. You can [define BibTeX keys](https://www1.citavi.com/sub/manual6/en/bibtex_keys.html).

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-1.png)

**3** Open the LaTeX Assistant. Click **Citation** > **LaTeX Assistant**.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-2.png)

**4** Double-clicking a reference in the LaTeX Assistant inserts \cite{} into your TeX document.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-3.png)

**5** Knowledge items are inserted the same way.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-4.png)

**6** To create a BibTeX file, in Citavi, on the **File** menu, click **Export**. Export all of the references in your project as a BibTeX file. Select **BibTeX** as the format. Click **Next**. If necessary, select a different package (such as jurabib or natbib). To do so, click **Add export filter**.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-5.png)

**7** Save the BibTeX file in your LaTeX project folder.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-6.png)

**8** Enter the style and name of the BibTeX file, for example:

```
COPY*\bibliographystyle{plain}*
*\bibliography{information-literacy}*
```

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-7.png)

**9** You may need to run the output command (pdfLaTeX, MakeIndex, BibTeX) several times until the compilation routine is complete.

![img](https://gitee.com/zihm/images/raw/master/hexo/20200623193455-8.png)

## See also:

[Citavi in Detail: Creating Publications with LaTeX](https://www1.citavi.com/sub/manual6/en/creating_a_publication_with_tex.html)

[Questions? Ask us!](https://www1.citavi.com/sub/machform/view.php?id=154149&element_1=Creating a Publication with LaTeX) | [Print](javascript:print();) | [Deutsch](https://www1.citavi.com/sub/manual6/de/index.html?101_creating_a_publication_with_latex.html) | [Español](https://www1.citavi.com/sub/manual6/es/index.html?101_creating_a_publication_with_latex.html) | [Citavi Homepage](https://www.citavi.com/) | [Privacy Policy](https://www.citavi.com/privacy) | [Legal](https://www.citavi.com/legal)

URL: https://www1.citavi.com/sub/manual6/en/index.html?101_creating_a_publication_with_latex.html, updated: 2019-04-15