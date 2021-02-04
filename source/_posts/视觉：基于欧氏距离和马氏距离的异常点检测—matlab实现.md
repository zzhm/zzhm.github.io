---
title: 基于欧氏距离和马氏距离的异常点检测—matlab实现
mathjax: false
date: 2018-05-03 15:00:33
id: anomaly-detection 
tags: 
- 机器视觉
- matlab
categories:
- 学习笔记
---

### 基于欧式距离的：

````
load data1.txt %导入数据，行为样本，列为特征
X=data1; %赋值给X
u=mean(X); %求均值
[m,n]=size(X);
for i=1:m
	dist(i)=sqrt(sum(X(i,:)-u).^2);
end

[a,b]=sort(dist);%对欧氏距离进行排序
T=ceil(m*0.02)%设置阀值
Threshold=a(m-T);%定为阀值
len=length(a);
for i = 1:len %遍历，如果小于阀值为正常点
	if a(i) < Threshold
		inlier(i) = [b(i)];
		s=b(i);
		disp(['正常点序列号：',num2str(s)])
	end
end

% inlier
for i = 1:len %遍历，如果大于等于阀值为正常点
    if a(i)>= Threshold
        outlier(i) = [b(i)];
        ns=b(i)
        disp(['离群点序列号：',num2str(ns)])
    end
end
% outlier
````

<!--- more --->

### 基于马氏距离的：

````
load data1.txt %导入数据，行为样本，列为特征
X=data1; %赋值给X
u=mean(X); %求均值
[m,n]=size(X);
for i=1:m
	newdata=[X(i,:);u]
	cov_w=cov(newdata);%求协方差矩阵
	dist(i)=(X(i,:)-u)cov_w(X(i,:)-u)'%求出每个样本到u的马氏距离
end
[a,b]=sort(dist);%对马氏距离进行排序
T=ceil(m*0.02)%设置阀值
Threshold=a(m-T);%定为阀值
clear T;
len=length(a);
for i = 1:len %遍历，如果小于阀值,为正常点
	if a(i) < Threshold
        inlier(i) = [b(i)];
        s=b(i);
        disp(['正常点序列号：',num2str(s)])
	end
end

% inlier
for i = 1:len %遍历，如果大于等于阀值为异常点
	if a(i)>= Threshold
		outlier(i) = [b(i)];
		l=b(i)
		disp(['离群点序列号：',num2str(l)])
	end
end
% outlier
````

原文链接：[直达](http://www.cnblogs.com/xiaohuahua108/p/6641629.html)