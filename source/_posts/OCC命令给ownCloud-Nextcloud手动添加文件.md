---
title: OCC命令给ownCloud/Nextcloud手动添加文件
mathjax: false
date: 2019-01-03 14:17:12
id: nextcloud-file-scan
tag:
- nextcloud
- 网站
- 生活
- nas
category:
- 生活
---

有时候，直接通过Web页面上传文件并不那么方便，于是有的朋友就直接把文件上传到服务器里，然后拷贝到data目录下，打开ownCloud，却还是之前的文件。这是因为虽然上传了文件，但是ownCloud/Nextcloud的数据库里并没有这个文件的信息。文件信息都被存储在数据库的oc_filecache表中。此时，需要使用OCC命令手动更新文件目录。

<!---more--->

## 使用OCC命令更新文件索引

occ有三个用于管理Nextcloud中文件的命令：

```
files files:cleanup #清楚文件缓存 
files:scan #重新扫描文件系统 
files:transfer-ownership #将所有文件和文件夹都移动到另一个文件夹
```

我们需要使用`files:scan` 来扫描新文件。

```
 格式: files:scan [-p|--path="..."] [-q|--quiet] [-v|vv|vvv --verbose] [--all] [user_id1] ... [user_idN]
参数: user_id #扫描所指定的用户（一个或多个，多个用户ID之间要使用空格分开）的所有文件
选项: --path #限制扫描路径 --all #扫描所有已知用户的所有文件 --quiet #不输出统计信息 --verbose #在扫描过程中显示正在处理的文件和目录 --unscanned #仅扫描以前未扫描过的文件
```

以下是一个具体的命令示例：

```
cd /path/to/nextcloud
sudo -u www-data php occ files:scan --all #扫描所有用户的所有文件
```

如果不想显示扫描信息，可以在后面加上`--quiet` ，如下：

```
sudo -u www-data php occ files:scan --all --quiet
```

## 指定扫描的用户

列出所有用户：

```
sudo -u www-data php occ user:list
```

为用户ChengYe扫描文件：

```
sudo -u www-data php occ files:scan ChengYe
```

## 指定扫描目录

当使用`--path` 选项时，该路径必须包含以下部分：

```
"user_id/files/path" 或
"user_id/files/mount_name" 或
"user_id/files/mount_name/path"
```

其中，`/files/`是必须要加上的，不可忽略。

示例：

```
sudo -u www-data php occ files:scan --path="/ChengYe/files/Photos" #指向用户ChengYe的Photos文件夹
```