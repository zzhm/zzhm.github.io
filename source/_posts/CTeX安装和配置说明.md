---
title: CTeX安装和配置说明及注意事项
mathjax: false
date: 2018-07-05 15:02:39
id: ctex-install-and-update
tags:
- latex
- ctex
- 技能
- 写作
categories:
- 科研
- 技能
---

CTex套装安装，把WinEdt7.0换成了WinEdt10.3，并完美注册码破解。接下来需要对宏包进行更新，不然你会发现网上下载的很多模板都不能用。

<!---more--->

## 准备材料

1.CTex套装，当前最新稳定版本[CTeX_2.9.2.164_Full.exe](http://www.ctex.org/CTeXDownload)，下载速度因人而异，可选[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/ctex/legacy/2.9/ )和[中科大镜像](http://mirrors.ustc.edu.cn/ctex/legacy/2.9/ )、[百度网盘](https://pan.baidu.com/s/1jHQVq2U )。

2.[WinEdt10.3](http://www.winedt.com/download.html),这个是目前最新的版本，个人感觉比7.0好用不少，界面非常友好。

## 安装软件

1.选择想要安装的硬盘，然后新建文件夹并命名，比如CTex，最好使用英文文件名，然后将CTeX_2.9.2.164_Full.exe放到该文件夹下，双击即可，然后根据提示一步一步来就行，但要注意选择安装目录，我是直接安装在刚创建的文件夹了，当然也可以放到其他文件夹，这个无所谓的。安装过程会持续较长时间，耐心等待即可。

2.安装完成后，默认是WinEdt7.0，但作为IDE，必须美观漂亮简洁又清爽，于是我下载了最新版的安装包（32位安装包），然后放到原CTex套装安装目录下的WinEdt文件夹下，双击安装包，根据提示选择该文件夹为安装目录，**覆盖安装**即可(有人说先卸载在安装有问题)。此外，在安装界面需要勾选关联WinEdt与CTeX。

## 破解过程

WinEdt并不是免费的，这是大家都知道的，这里可以选择Texlive或者其他免费的IDE，由于本人打算一条道走到底，就查了不少破解的资料，这里给出两种常见的破解方法：

1. 注册码破解，源自于某位不认识大神的贡献，亲测有效，非常感谢。

- 打开WinEdt，找到如下路径

```
  help-->Register WinEdt
  
  在弹出的窗口中填写：
  Name：Cracker TeCHiScy
  Code:1130140925535334280
  
  点击OK，注册完毕
```

引用网址：[网址1](http://blog.csdn.net/sdujava2011/article/details/57409399)、[网址2](https://www.52pojie.cn/thread-595351-1-1.html)

2.无限延长试用期的方法，这也是应用最多的方法，通过修改WinEdt里的exit文件，使得每次退出都会清除当前的试用时间，具体方法：

- 打开WinEdt，找到如下路径

```
  option-->option interface-->Advanced Configuration-->Event Handlers-->Exit
```

- 双击Exit子项，弹出一个名为Exit.edt的配置文件，在配置文件Exit.edt最后一句“END;”前面一行加入 

  ```
  RegDeleteValue('HKEY_CURRENT_USER', 'Software\WinEdt 10', 'Inst');
  ```

   然后单击保存。

注意：将需要添加语句  `RegDeleteValue('HKEY_CURRENT_USER', 'Software\WinEdt 8', 'Inst');` 的版本号改为自己的版本号，比如上面是8，如果用的是10.2的话，改为10就行。

最终破解成功。

## CTEX 改变默认 pdf viewer

打开WinEdt，找到如下路径

```
Options -> Excution Modes… -> PDF viewer选项卡
```

在 PDF Viewer Excutable 下填入你想要 PDF 阅读器的路径。比如，`“C:\CTeX\ctex\bin\SumatraPDF.exe”`。

若要更新SumatraPDF版本可在上述目录下找到阅读器，打开后在`帮助->更新版本 `处，查找更新，覆盖安装即可。

## 更新宏包

### 方法一

近日在更新宏包之时，发现其因为版本过旧，不能连接到合适的服务器。而在编译 tex 文档时有时候需要新的宏包，放弃一些旧的宏包等等，不能每一次都通过手动下载安装完成。那么解决办法是另外再单独安装一个 MiKTeX，使 TeX 编译环境仍能正常更新。 

在更新宏包时，需要预先选择一个服务器，国内稳定的就几个可选，国外一般都不稳定，容易断。我一直使用清华的服务器 `mirrors.tuna.tsinghua.edu.cn`，注意服务器的更新时间，越新越好 。

到最近的服务器镜像下载最新的 [MiKTeX](http://mirrors.zju.edu.cn/CTAN/systems/win32/miktex/setup/) 版本 。注意不要下载 64 位版本的，因为 CTeX 自身安装的组件都是 32 位的，所以下载一个 32 位的 MiKTeX 兼容性会更好。

先将原 CTeX 目录下的 MiKTeX 文件夹删除（如果不放心的话，可以先重命名为 MiKTeX-old），然后直接将新下载的miktex 直接安装在这里，代替旧版本的 MiKTeX （注意文件夹名字在安装时就改为MiKTeX 可以避免后续的麻烦，而不是 MikTeX 2.9，因为这会涉及到环境变量）。

注意到新安装的 MiKTeX 容量比 CTeX 自带的小了很多，并没有那么臃肿。有很多包没有安装好，需要后续手动安装。

刚安装完，需要打开 Update MikTeX (Admin) 对目录下的宏包进行更新，确保其处于最新的状态，旧的宏包可以淘汰，新的宏包可以安装，第一次可能需要较长时间更新同步，之后再编译其他 tex 文档时，只需要安装几个欠缺的宏包就可以了。几个快捷方式如果查找不到，可以直接打开它们指向的原文件

- Package Manager (Admin) -> D:\CTEX\MiKTeX\miktex\bin\mpm_mfc_admin.exe
- Settings (Admin) -> D:\CTEX\MiKTeX\miktex\bin\mo_admin.exe
- Update (Admin) -> D:\CTEX\MiKTeX\miktex\bin\internal\miktex-update_admin.exe

当更新完所有 package 之后，再次打开 Update MiKTeX，会发现已经是最新状态，没有宏包需要安装了。在编译某一些 tex 文档时需要的宏包本地如果没有， MiKTeX 会提示你是否从服务器下载，点击确认即可， 如果希望系统能自动下载，而不需要手动确认，只需要将对话框中最后一行的勾去掉即可。 

### 离线更新

1、首先你需要知道一个可用的CTAN镜像，理想的镜像应当是位于大陆的，地理上与你较近的，最好是同一ISP的。

**目前大陆最驰名的应该是中科大的开源镜像，其网址是http://mirrors.ustc.edu.cn

其同时收录了N个开源软件的镜像，也包括CTAN。

下文均以中科大开源镜像为例。

2、下载所需的Package

**打开**CTAN镜像下的systems/win32/miktex/tm/packages/目录，例如：

``http://mirrors.ustc.edu.cn/CTAN/systems/win32/miktex/tm/packages/``

首先需要下载索引文件：``miktex-zzdb1-2.9.tar.lzma``和``miktex-zzdb2-2.9.tar.lzma`` 

以上两个索引文件是必须下载的，而且每次你手动更新或者安装Package的时候都需要下载最新的索引文件。

然后，下载所需的Package。(后缀是.cab、.tar.lzma、.tar.bz2)，或者下载此目录下的全部文件。(一些浏览器或者下载软件提供批量下载功能，可批量下载当前页面下的所有链接。)

> 下载方法：
>
> 资源管理器->输入ftp://mirrors.ustc.edu.cn/CTAN/systems/win32/miktex/tm/packages/
>
> 复制文件夹下的所有文件出来即可，复制过程中不要关闭资源管理器的窗口（packages）
>
> 在http://mirrors.ustc.edu.cn/CTAN/systems/win32/miktex/support/update/miktex-update_admin.exe 下载，更新文件

然后，点击开始菜单，选择所有程序，选择CTEX(如果你安装的是CTEX)，选择Miktex，右键点击Maintenance (Admin)选择打开，这样会打开一个文件管理器窗口，方便后面点选。

然后选择Settings (Admin)，打开设置窗口。在最右面的Package选项卡，选择Change，然后选择Package Shell be installed from a local directory.，点击下一步，选择你本地Package源的文件夹(放着很多.tar.lzma的那个文件夹)。

此时Package源已经设置为使用本地源。此时如果你希望安装新的Package，请选择Package Manager (Admin)，如果你希望更新已有Package，请选择Update (Admin)。‘

附各大学开源软件镜像站：

复旦大学：http://fs.fudan.edu.cn/

东北大学：http://mirror.neu.edu.cn/

中国科大：http://mirrors.ustc.edu.cn/

电子科大：http://mirrors.stuhome.net/

华中科大：http://mirrors.hust.edu.cn/

北京交大：http://mirror.bjtu.edu.cn/

CTEX：http://ftp.ctex.org/mirrors/

## 模板

中文报告模板，另附中科院模板，[论文](https://github.com/mohuangrui/ucasthesis)、[开题报告](https://github.com/mohuangrui/ucasproposal)、[书脊](https://github.com/mohuangrui/latexspine)

```latex
\documentclass[a4paper, 11pt]{article}

%%%%%% 导入包 %%%%%%
\usepackage{CJKutf8}
\usepackage{graphicx}
\usepackage[unicode]{hyperref}
\usepackage{xcolor}
\usepackage{cite}
\usepackage{indentfirst}

%%%%%% 设置字号 %%%%%%
\newcommand{\chuhao}{\fontsize{42pt}{\baselineskip}\selectfont}
\newcommand{\xiaochuhao}{\fontsize{36pt}{\baselineskip}\selectfont}
\newcommand{\yihao}{\fontsize{28pt}{\baselineskip}\selectfont}
\newcommand{\erhao}{\fontsize{21pt}{\baselineskip}\selectfont}
\newcommand{\xiaoerhao}{\fontsize{18pt}{\baselineskip}\selectfont}
\newcommand{\sanhao}{\fontsize{15.75pt}{\baselineskip}\selectfont}
\newcommand{\sihao}{\fontsize{14pt}{\baselineskip}\selectfont}
\newcommand{\xiaosihao}{\fontsize{12pt}{\baselineskip}\selectfont}
\newcommand{\wuhao}{\fontsize{10.5pt}{\baselineskip}\selectfont}
\newcommand{\xiaowuhao}{\fontsize{9pt}{\baselineskip}\selectfont}
\newcommand{\liuhao}{\fontsize{7.875pt}{\baselineskip}\selectfont}
\newcommand{\qihao}{\fontsize{5.25pt}{\baselineskip}\selectfont}

%%%% 设置 section 属性 %%%%
\makeatletter
\renewcommand\section{\@startsection{section}{1}{\z@}%
{-1.5ex \@plus -.5ex \@minus -.2ex}%
{.5ex \@plus .1ex}%
{\normalfont\sihao\CJKfamily{hei}}}
\makeatother

%%%% 设置 subsection 属性 %%%%
\makeatletter
\renewcommand\subsection{\@startsection{subsection}{1}{\z@}%
{-1.25ex \@plus -.5ex \@minus -.2ex}%
{.4ex \@plus .1ex}%
{\normalfont\xiaosihao\CJKfamily{hei}}}
\makeatother

%%%% 设置 subsubsection 属性 %%%%
\makeatletter
\renewcommand\subsubsection{\@startsection{subsubsection}{1}{\z@}%
{-1ex \@plus -.5ex \@minus -.2ex}%
{.3ex \@plus .1ex}%
{\normalfont\xiaosihao\CJKfamily{hei}}}
\makeatother

%%%% 段落首行缩进两个字 %%%%
\makeatletter
\let\@afterindentfalse\@afterindenttrue
\@afterindenttrue
\makeatother
\setlength{\parindent}{2em}  %中文缩进两个汉字位


%%%% 下面的命令重定义页面边距，使其符合中文刊物习惯 %%%%
\addtolength{\topmargin}{-54pt}
\setlength{\oddsidemargin}{0.63cm}  % 3.17cm - 1 inch
\setlength{\evensidemargin}{\oddsidemargin}
\setlength{\textwidth}{14.66cm}
\setlength{\textheight}{24.00cm}    % 24.62

%%%% 下面的命令设置行间距与段落间距 %%%%
\linespread{1.4}
% \setlength{\parskip}{1ex}
\setlength{\parskip}{0.5\baselineskip}

%%%% 正文开始 %%%%
\begin{document}
\begin{CJK}{UTF8}{gbsn}

%%%% 定理类环境的定义 %%%%
\newtheorem{example}{例}             % 整体编号
\newtheorem{algorithm}{算法}
\newtheorem{theorem}{定理}[section]  % 按 section 编号
\newtheorem{definition}{定义}
\newtheorem{axiom}{公理}
\newtheorem{property}{性质}
\newtheorem{proposition}{命题}
\newtheorem{lemma}{引理}
\newtheorem{corollary}{推论}
\newtheorem{remark}{注解}
\newtheorem{condition}{条件}
\newtheorem{conclusion}{结论}
\newtheorem{assumption}{假设}

%%%% 重定义 %%%%
\renewcommand{\contentsname}{目录}  % 将Contents改为目录
\renewcommand{\abstractname}{摘要}  % 将Abstract改为摘要
\renewcommand{\refname}{参考文献}   % 将References改为参考文献
\renewcommand{\indexname}{索引}
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}
\renewcommand{\appendixname}{附录}
\renewcommand{\algorithm}{算法}


%%%% 定义标题格式，包括title，author，affiliation，email等 %%%%
\title{大规模分布式系统环境下的性能监测与跟踪调试工具的\\研究成果综述}
\author{傅海平\footnote{电子邮件: haipingf@gmail.com，学号: 201128013229018}\\[2ex]
\xiaosihao 中国科学院计算技术研究所\\[2ex]
}
\date{2012年5月}


%%%% 以下部分是正文 %%%%  
\maketitle

\tableofcontents
\newpage
在此输入正文，中英文均可。
\end{CJK}
\end{document}
```

## 其它

编译出错，先更编译器尝试一下，让后更下一下宏包（针对undefined control sequence）。

由于CTeX长期不更新。因此，并不推荐使用CTeX，而是推荐使用TeX Live，[官方网站](http://tug.org/texlive/)，[镜像下载地址](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlihttps://zymin-1255632454.cos.ap-shanghai.myqcloud.com/0newblog/)