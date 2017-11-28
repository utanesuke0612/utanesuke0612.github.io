---
layout: post
title: Uda-DataAnalysis-25--探索两个变量
date: 2017-11-23 03:00:03
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 3. 练习：散点图

使用散点图，表示两个连续变量之间的关联关系。

- 准备工作

```{r}
setwd("C:/Users/utane/OneDrive/udacity/24-R")
getwd()
library(ggplot2)
pf <- read.csv("pseudo_facebook.tsv",sep='\t')
```

- 绘图

```{r}
qplot(x = age,y = friend_count,data=pf)
```

![image](https://user-images.githubusercontent.com/18595935/33324031-a530995a-d491-11e7-88e0-d9992230e279.png)

# 4. ggplot 语法

- 查看age的范围

```{r}
summary(pf$age)
```

- 使用ggplot画图

```{r}
ggplot(aes(x=age,y=friend_count),data = pf) + geom_point() + 
  xlim(13,113)
```

![image](https://user-images.githubusercontent.com/18595935/33324276-87956d7a-d492-11e7-8df0-d7294c74cfd9.png)

上面使用ggplot绘制了相同的图，与qplot相比，ggplot有如下特点：
1. 需要自己制定图形类型，如geom_point()
2. xy轴，需要外面有一个wrapper
3. 使用layer的概念，每添加一个layer会改变图形形状


# 5. 过度绘制

上面的图，会发现大部分的数据集中在左下角，重叠了很多，所以很难分辨真实的数据分布，这时可以将之前的20个普通黑点当作一个黑点，之前的一个黑点当作1/20个，即接近透明的点，实现方式如下，改进后的图，看起来年轻人的好友就没有以前多了，这是正确的：

下图的分布与[19. 练习：用户年龄](http://localhost:4000/2017/11/22/Uda-DataAnalysis-23/#19-练习用户年龄)中吻合

```{r}
ggplot(aes(x=age,y=friend_count),data = pf) + 
  geom_point(alpha = 1/20) + 
  xlim(13,113)
```

![image](https://user-images.githubusercontent.com/18595935/33325270-24e014f2-d495-11e7-9d79-d167b67d5ee9.png)


年龄应该是连续的，但是上图给人的感觉是分段的，下面代码给数据加一点噪音：

```{r}
ggplot(aes(x=age,y=friend_count),data = pf) + 
  geom_jitter(alpha = 1/20) + 
  xlim(13,113)
```

![image](https://user-images.githubusercontent.com/18595935/33325359-59fb13b2-d495-11e7-9a6e-81b67cf10be2.png)


# 6. 练习：coord_trans()

