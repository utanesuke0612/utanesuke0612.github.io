---
layout: post
title: Uda-DataAnalysis-pj02--红葡萄酒数据质量分析报告
date: 2017-12-14 06:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

最终提交的报告和rmd文件见：[here](https://1drv.ms/f/s!Ald1cKESY1BDgc4jOOnYTkzjYI28MA)

预先按照和加载需要的包：

```python
# 加载你最终使用的所有组件
# 在这个代码块的分析中。

# 注意，在这个代码块中，将参数 "echo" 设为假。
# This prevents the code from displaying in the knitted HTML output.这可以避免代码混入 HTML 输出显示。
# 应当在文件中，对所有代码块设为 echo=FALSE 。
#install.packages('ggplot2')
library(ggplot2)
#install.packages("GGally")
library(GGally)
```

# 1. 目的

根据红葡萄酒的各个性质参数(如酸度,pH值等)，分析这些参数是如何影响红酒的质量。

# 2. 数据集介绍

该数据集有1599条记录，12个变量，数据集中各字段的意义如下：

- fixed acidity：固定酸度
- volatile acidity：挥发性酸度，太高的酸度会导致红酒味道变差
- citric acid：柠檬酸，少量的柠檬酸能增加红酒的鲜度
- residual sugar：残糖,也即酒精发酵后未被发酵而残余的糖分
- chlorides：氯化物，红酒中的盐分
- free sulfur dioxide：游离二氧化硫，能防止微生物和被氧化
- total sulfur dioxide：总二氧化硫量，包含游离二氧化硫和结合二氧化硫，如果游离二氧化硫浓度超过50 ppm的话，就能从红酒中感受到二氧化硫的味道
- density：密度，水的密度，即水减去酒精和糖的容量后计算得到
- pH: 酸碱度，0 (very acidic酸) to 14 (very basic碱); 大部分集中在3-4的ph值之间
- sulphates：硫酸盐，一种会产生二氧化硫添加剂，有抗菌剂和抗氧化剂的作用
- alcohol：酒精度
- quality：从低到高，评分0-10

## 2.1 数据集结构-变量的类型和示例数据

```python
# 加载数据
wine <- read.csv("wineQualityReds.csv")
```

通过`str`查看数据结构:

```python
str(wine)
```

![image](https://user-images.githubusercontent.com/18595935/34340246-f86d96bc-e9c3-11e7-8e43-12d767f65c1a.png)


## 2.2 数据集结构-各变量的四分位值

```python
summary(wine)
```

![image](https://user-images.githubusercontent.com/18595935/34340252-2d2584e6-e9c4-11e7-953d-543f59561cb9.png)

# 3. 单变量绘图与分析

分析红葡萄酒中各变量的分布情况并绘图。

## 3.1 单变量绘图

- 红酒质量的分布状况

大部分葡萄酒质量分布集中在5和6之间，即中等及中等偏上，品质很好和品质很差的红酒都很少，红酒品质呈正态分布。

```python
table(wine$quality)
```

![image](https://user-images.githubusercontent.com/18595935/34340260-4326e320-e9c4-11e7-90d3-14ef260ced7d.png)

```python
# 因为单变量分析中一般使用直方图，下面创建一个直方图的公用函数
univ_histogram <- function(feature,width) {
    ggplot(data=wine, aes_string(x = feature)) + 
    geom_histogram(binwidth = width)
}
```


```python
ggplot(wine, aes(x=quality, fill=..x..)) + 
  geom_histogram(binwidth=1) + 
  scale_fill_gradient("Quality",low = "green", high = "blue")

```

![image](https://user-images.githubusercontent.com/18595935/34340264-63695b9a-e9c4-11e7-9d9a-e013dd4360d2.png)


- 酒精含量分布

红酒酒精含量普遍不高，属于低度酒，大概在9%~12%之间。

```python
univ_histogram("alcohol",0.1)+
  scale_x_continuous(breaks = seq(8,15,1))
```

![image](https://user-images.githubusercontent.com/18595935/34340271-78f42332-e9c4-11e7-8285-199de3f6e8e3.png)

选取水密度`wine$density`在25%以下的样本，其酒精浓度`alcohol`的分布于上面的总体数据酒精度数分布不同。
相对于总体数据的酒精度数分布，高度数的红酒更多。
可以看到水密度与酒精浓度是相关的，具体的相关系数后续继续分析。

```python
ggplot(aes(x = alcohol), data = 
         subset(wine,wine$density < quantile(wine$density,0.25))) + 
  geom_histogram(binwidth = 0.1) 
```

![image](https://user-images.githubusercontent.com/18595935/34340276-8ab0a302-e9c4-11e7-9465-83c8645ecaaf.png)

- ph值分布

大部分pH值在3.0-3.5之间。

```python
univ_histogram("pH",0.01)
```

![image](https://user-images.githubusercontent.com/18595935/34340281-9ab5357e-e9c4-11e7-9455-043530002aa3.png)


- sugar值分布

sugar值大部分集中在1-3之间。

```python
univ_histogram("residual.sugar",0.1)
```

![image](https://user-images.githubusercontent.com/18595935/34340282-9d8fef46-e9c4-11e7-8f45-849bd393fb39.png)



- fixed acidity分布

固定酸度大部分集中在6-8之间。

```python
univ_histogram("fixed.acidity",0.1)
```

![image](https://user-images.githubusercontent.com/18595935/34340283-a00ec6fc-e9c4-11e7-8934-8b6617f5b583.png)



- chlorides分布

盐分浓度集中在0.05-0.1之间。

```python
univ_histogram("chlorides",0.01)
```

![image](https://user-images.githubusercontent.com/18595935/34340284-a262ecda-e9c4-11e7-813f-bc6c14b9926e.png)


- 二氧化硫对红酒品质的影响

总二氧化硫中包含了游离二氧化硫和结合二氧化硫，数据集中只有游离二氧化硫数据，考虑到结合二氧化硫可能会影响到红酒品质，为了方便，添加一个新的变量：`结合二氧化硫 bound.sulfur.dioxide `

```python
wine$bound.sulfur.dioxide <- 
  wine$total.sulfur.dioxide - wine$free.sulfur.dioxide
```

从数据集中的介绍中了解到如果`total sulfur dioxide`即总二氧化硫量大于50ppm的话，就会感受到二氧化硫的味道，但是看下图的分布，即使选取的样本的游离二氧化硫量大于50ppm，其品质也没有特别低，但是样本量太小，所以并不能说明二氧化硫大于50这种性质，与品质之间相关度低。具体还要后续分析。

```python
ggplot(aes(x = quality, fill=..x..), 
       data = subset(wine,wine$free.sulfur.dioxide > 50)) + 
  geom_histogram(binwidth = 1) + 
  scale_fill_gradient("Quality",low = "green", high = "blue")
```

![image](https://user-images.githubusercontent.com/18595935/34340286-a5e38b26-e9c4-11e7-8cf7-dbaa11e23999.png)


下图可以发现游离二氧化硫浓度，大部分介于2-40之间。

```python
univ_histogram("free.sulfur.dioxide",1)
```

![image](https://user-images.githubusercontent.com/18595935/34340287-a84b1ce4-e9c4-11e7-8feb-8a24f7729c3a.png)

- 红葡萄酒的密度分布

红葡萄酒的密度与水十分接近,呈现正态分布

```python
univ_histogram("density",0.001)
```
![image](https://user-images.githubusercontent.com/18595935/34340309-0b31b502-e9c5-11e7-9dac-9e00c18238d1.png)

- sulphates浓度分析

红酒中的硫酸盐添加剂主要分布在0.4~0.8之间，近似正态分布。

```python
univ_histogram("sulphates",0.01)
```
![image](https://user-images.githubusercontent.com/18595935/34340310-0d5f56c2-e9c5-11e7-8040-4e90f09d4d57.png)


## 3.2 单变量分析

### 你的数据集内感兴趣的主要特性有哪些？

本数据集中最主要的特性是红酒品质`quality`，希望能通过探索红酒的其他属性如酸度，残糖以及pH值等元素，来建立一个模型预测红酒的品质。

### 你认为数据集内哪些其他特征可以帮助你探索兴趣特点？

对葡萄酒的平衡起着关键性影响的元素，包括：甜度、酸度、果味、酒精以及单宁。这些影响元素在数据集中呈现为：

1. 甜度：残留糖分`residual.sugar`，残留糖分较高的葡萄酒，尝起来会有甜腻的口感，但是如果糖分不足又会使得葡萄酒变得尖酸干涩难以下咽。
2. 酸度：柠檬酸`citric.acid`
3. 酒精：`alcohol`,过高的酒精度会给喉咙带来烧灼感

优先分析上述元素对红酒品质的影响。

### 根据数据集内已有变量，你是否创建了任何新变量？

为了后续分析方便，通过`total.sulfur.dioxide`总二氧化硫量和`free.sulfur.dioxide`游离二氧化硫，计算得到`bound.sulfur.dioxide`结合二氧化硫。

### 在已经探究的特性中，是否存在任何异常分布？你是否对数据进行一些操作，如清洁、调整或改变数据的形式？如果是，你为什么会这样做？

暂未发现异常分布的数据，数据也是完整无丢失的。


# 4. 双变量绘图与分析

## 4.1 双变量绘图

- 柠檬酸`citric.acid`与红酒品质`quality`之间的点阵图

之前凭直觉认为柠檬酸与红酒品质关联性强，但是通过下面的图形和输出的相关度分析，存在关联但是关联性不强。


```python
# 因为geom_point使用较多，下面创建一个公用函数
univ_point <- function(featureX,featureY,alphaValue) {
  ggplot(aes_string(x=featureX,y=featureY),data = wine) + geom_point(alpha=alphaValue)
}
```


```python
ggplot(aes(x=wine$citric.acid,y=wine$quality),data = wine) + geom_jitter(alpha=1/5)
```

![image](https://user-images.githubusercontent.com/18595935/34340325-5856c4b2-e9c5-11e7-85a5-98ae04d04108.png)

```python
cor.test(wine$citric.acid, wine$quality)
```
![image](https://user-images.githubusercontent.com/18595935/34340329-69eee66e-e9c5-11e7-8751-b456895c571f.png)

- 硫酸盐`sulphates`与二氧化硫量之间的关联


```python
univ_point("wine$sulphates","wine$free.sulfur.dioxide",1/5)
```

![image](https://user-images.githubusercontent.com/18595935/34340332-84e9ae9a-e9c5-11e7-9ce4-63825080705d.png)

```python
univ_point("sulphates","total.sulfur.dioxide",1/5)
```

![image](https://user-images.githubusercontent.com/18595935/34340333-87a4f6ee-e9c5-11e7-950d-c62e9c35af7a.png)

从上图看，两者似乎没有关联关系，为了进一步验证，计算两者之间的相关系数，分别为0.04和0.05，可以知道硫酸盐对二氧化硫的影响不大：

```python
cor.test(wine$free.sulfur.dioxide, wine$sulphates)
```

![image](https://user-images.githubusercontent.com/18595935/34340337-99edd852-e9c5-11e7-8ef9-746404e63307.png)

```python
cor.test(wine$total.sulfur.dioxide, wine$sulphates)
```

![image](https://user-images.githubusercontent.com/18595935/34340339-a6e8c6ac-e9c5-11e7-9cbe-dc78784cda26.png)

- 酒精度数`alcohol`与密度`density`之间的关系

```python
univ_point("alcohol","density",1/5) + geom_smooth(method = 'lm', color='red')
```

![image](https://user-images.githubusercontent.com/18595935/34340353-fcdbad0e-e9c5-11e7-9b55-f1f549c4b5d5.png)
从上图看两者存在较强相关性，酒精度数越高，密度就越低，其相关系数为`-0.496`，存在较强的相关关系：

```python
cor.test(wine$alcohol, wine$density)
```

![image](https://user-images.githubusercontent.com/18595935/34340356-06f06096-e9c6-11e7-9a30-9515f664d941.png)

- 各种酸度与pH值之间的关系

```python
p1 <- univ_point("fixed.acidity","pH",1/5)+  
  geom_smooth(method = 'lm', color='red')

p2 <- univ_point("volatile.acidity","pH",1/5)+  
  geom_smooth(method = 'lm', color='red')

p3 <- univ_point("citric.acid","pH",1/5)+  
  geom_smooth(method = 'lm', color='red')

#install.packages("gridExtra")
library(gridExtra)

grid.arrange(p1,p2,p3,ncol=2)
```

![image](https://user-images.githubusercontent.com/18595935/34340357-09b546e8-e9c6-11e7-9291-7dfd4d28a970.png)



从上述图形上看，pH值越高挥发性酸度就越大，固定酸度和柠檬酸度越小。


- 不同品质下酒精浓度和红酒数量的分布

如下是不同红酒品质下，不同酒精度数红酒的数量分布，从下面的分布图中可以看出:
- 大部分红酒品质在5-6之间
- 随着度数增加，品质高的红酒比例增加

```python
ggplot(wine, aes(x=alcohol, color=factor(quality), fill=factor(quality))) +
  geom_histogram( position="identity", alpha=0.2,binwidth = 0.2)
```

![image](https://user-images.githubusercontent.com/18595935/34340359-0ca4dbfc-e9c6-11e7-8a8b-09a598cb7563.png)

- 不同红酒品质`quality`下，观察柠檬酸度`citric acid`的数据概要

根据数据集的介绍了解到，`citric acid`会增加红酒的鲜度，观察下面的统计结果，随着红酒品质的提升，其柠檬酸度整体也在增加。

```python
by(wine$citric.acid,wine$quality,summary)
```

![image](https://user-images.githubusercontent.com/18595935/34340380-32c632cc-e9c6-11e7-9736-7ebde3342341.png)


从下图可以看到，品质一般的红酒(quality为5和6)，其柠檬酸度低的较多，而quality为7和8的红酒，相对来说，柠檬酸度高的比例较高。

```python
univ_histogram("citric.acid",0.01) + 
  facet_wrap(~quality,ncol = 3)
```

![image](https://user-images.githubusercontent.com/18595935/34340381-35e6ce1c-e9c6-11e7-9bbe-b6fa1cedb393.png)

- 各变量的散点矩阵图

```python
theme_set(theme_minimal(20))

wine_subset <- wine[,c(2:13)]
ggp = ggpairs(wine_subset[sample.int(nrow(wine_subset), 1000),],
        lower = list(continuous = wrap(ggally_points, size = 0.5, color = "blue")),
        upper = list(continuous = wrap("cor", size = 6)))
print(ggp, progress = F)  # no progress bar

#ggsave("all.jpeg")
```

![image](https://user-images.githubusercontent.com/18595935/34340382-38f6d28c-e9c6-11e7-81b5-d5314de6c793.png)


分析上面的散点矩阵图，质量`quality`与挥发性酸度`volatile.acidity`相关系数为0.405 ，与酒精度数`alcohol`的相关度为0.436，有较强的相关关系。

下面分别进行双变量分析：

(1). 质量与酒精度数的图如下，下图可以看出，品质好的红酒，其度数普遍高于品质差的红酒。
从上到下的虚线分别表示，不同百分比处酒精浓度的变化曲线图：
- 蓝色:90%
- 绿色:50%
- 黄色:平均值
- 红色:10%

```python
ggplot(aes(x=quality,y=alcohol, color=..x..),data=wine) + geom_jitter(alpha=0.3) +
  geom_line(stat = "summary",fun.y = mean,color = "yellow") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .1),
            linetype = 2,color = "red") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .5),
            color = "green") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .9),
            linetype = 2,color = "blue") +
  ggtitle("quality/alcohol(plot-1)") + scale_fill_gradient("Quality",low = "green", high = "blue")

```

![image](https://user-images.githubusercontent.com/18595935/34340384-3ec9104e-e9c6-11e7-84c5-3c4eb306449a.png)



```python
ggplot(wine,aes(factor(quality), alcohol,color=..x..) ) + 
  geom_jitter(alpha=0.3) +
  geom_boxplot( alpha = 0.5,color = 'blue')+
  stat_summary(fun.y = "mean", 
      geom = "point", 
      color = "red")+
  geom_smooth(method='lm', aes(group = 1)) + 
  ggtitle("quality/alcohol(plot-2)")+ scale_fill_gradient("Quality",low = "green", high = "blue")
```

![image](https://user-images.githubusercontent.com/18595935/34340385-40e9ea38-e9c6-11e7-8f53-e9d9510fcc31.png)



(2). 上面相同的方式，质量与挥发性酸度的图如下，从图上可以看出，品质好的红酒其挥发性酸度普遍低于品质低的红酒。

从上到下的虚线分别表示，不同百分比处挥发性酸度的变化曲线图：
- 蓝色:90%
- 绿色:50%
- 黄色:平均值
- 红色:10%

```python
ggplot(aes(x=quality,y=volatile.acidity,color=..x..),data=wine) + 
  geom_jitter(alpha=0.3) +
  geom_line(stat = "summary",fun.y = mean,color = "yellow") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .1),
            linetype = 2,color = "red") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .5),
            color = "green") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .9),
            linetype = 2,color = "blue") +
  ggtitle("quality/volatile.acidity(plot-1)")+ 
  scale_fill_gradient("Quality",low = "green", high = "blue")

```

![image](https://user-images.githubusercontent.com/18595935/34340386-4336c126-e9c6-11e7-92ed-2b5df627f72b.png)



```python
ggplot(wine,aes(factor(quality), volatile.acidity,color=..x..)) + 
  geom_jitter(alpha=0.3) +
  geom_boxplot( alpha = 0.5,color = 'blue')+
  stat_summary(fun.y = "mean", 
      geom = "point", 
      color = "red")+
  geom_smooth(method='lm', aes(group = 1)) + 
  ggtitle("quality/volatile.acidity(plot-2)")+ scale_fill_gradient("Quality",low = "green", high = "blue")
```

![image](https://user-images.githubusercontent.com/18595935/34340388-45346f0a-e9c6-11e7-9921-5758a2fe287b.png)

## 4.2 双变量分析

### 探讨在这部分探究中观察到的一些关系。这些感兴趣的特性与数据集内其他特性有什么区别？
这部分集中探索了两个变量的分布关系，例如
- 柠檬酸与红酒品质的分布，硫酸盐与二氧化硫的分布，之前凭直觉认为两者的关联性很强，但经过绘图与分析发现直觉是错误的，并没有太强的关联关系。
- 酒精度数与密度的分布，以及各种酸度与PH的分布，与预想的结果类似，这些分布的两个变量之间存在较强的相关性。
- 酒精度数与红酒品质的分布，这个结果是没有料到的，从图形上看，酒精度数对红酒品质的影响很大。

通过数据集中的介绍，以及主观的判断，觉得关联关系强的变量，经过分析，事实上没有太强的关联关系。说明在数据分析过程中，不能凭主观的判断，必须通过客观的统计分析才能得出正确的结论。

### 你是否观察到主要特性与其他特性之间的有趣关系？
从数据集的介绍中了解到，硫酸盐是一种用于产生二氧化硫的添加剂，但是经过绘图和分析，硫酸盐与总二氧化硫，硫酸盐与游离二氧化硫之间相关关系非常小，这一点比较意外。

### 你发现最强的关系是什么？
最强的关系是酒精度数与密度的关系。

# 5. 多变量绘图与分析

## 5.1 挥发性酸/酒精度/硫酸盐等与红酒品质的多变量绘图

从上面双变量分析中可知，挥发性酸度和酒精度对红酒品质影响较大，下面将这三个变量放在一个图中进行分析，从下图可以看出，随着红酒品质的升高，分布逐渐集中到左上区域，即品质越高，酒精度约高，挥发性酸越低。

```python
univ_point("volatile.acidity","alcohol",0.3)+
  facet_wrap(~quality,ncol = 3)
```

![image](https://user-images.githubusercontent.com/18595935/34340409-8b5fb836-e9c6-11e7-9931-dba34e255c07.png)

下面再加一个变量硫酸盐：


```python
ggplot(aes(x=volatile.acidity,y=alcohol),data=wine) + 
  geom_point(aes(colour=wine$sulphates),alpha=0.3) + 
  facet_wrap(~quality,ncol = 3) +
  theme(legend.position="top") + scale_fill_gradientn(colours = terrain.colors(10))
```

![image](https://user-images.githubusercontent.com/18595935/34340411-8dddd3ea-e9c6-11e7-9c7b-a5d93c9d7620.png)

从上面的图形很难看出硫酸盐对品质的影响。下面将通过quality再生成一个变量grade，分成三个level，分别为low(4分以及以下)，medium(5和6),high(7分及以上)，再重新绘图：

```python
wine$grade <-  cut(wine$quality,breaks = c(0,4,6,8))
levels(wine$grade) <- list(low="(0,4]", medium="(4,6]", high="(6,8]")
table(wine$grade)
```
low medium   high 
63   1319    217 


```python
ggplot(aes(x=volatile.acidity,y=alcohol),data=wine) + 
  geom_point(aes(color=wine$sulphates),alpha=0.3) + 
  facet_wrap(~grade,ncol = 3)+
  theme(legend.position="top") + scale_fill_gradientn(colours = terrain.colors(10))
```

![image](https://user-images.githubusercontent.com/18595935/34340413-9008330e-e9c6-11e7-8901-6729185061ac.png)



上图中，在红酒等级为high时，其冷色调的点密度较等级为low和medium时高，说明从整体上，硫酸盐高的红酒，其品质也更高。

## 5.2 硫酸盐/游离二氧化硫/总二氧化硫量/品质的多变量绘图

根据数据集介绍，硫酸盐是一种会产生二氧化硫的添加剂，但是经过下图的分析，各个品质的红酒中，游离二氧化硫与总二氧化硫有很强的正相关，但是硫酸盐与游离二氧化硫和总二氧化硫之间并无明显相关性。

```python
ggplot(aes(x=free.sulfur.dioxide,y=total.sulfur.dioxide),data=wine) + 
  geom_point(aes(color=sulphates),alpha=0.3) + geom_smooth(method = 'lm', color='red') + 
  theme(legend.position="top") + 
  scale_fill_gradientn(colours = terrain.colors(10)) + facet_wrap(~quality,ncol = 3)
```

![image](https://user-images.githubusercontent.com/18595935/34340414-930b42da-e9c6-11e7-8a24-4feb4f85ccc3.png)

## 5.3 酒精浓度/密度/红酒品质之间的多变量分布图

根据数据集介绍，密度与酒精浓度有关，下面是在不同品质下，酒精度数与水密度之间的分布图:
- 红酒品质越高，酒精度数整体越高
- 酒精度数越高，水密度整体越低

```python
ggplot(aes(x = alcohol, y = density, color =quality), data = wine) +
  geom_point(alpha = 0.3, size = 1, position = 'jitter') +
  geom_smooth(method = "lm", se = FALSE,size=1) + 
  scale_fill_gradient("Quality",low = "green", high = "blue")
```
![image](https://user-images.githubusercontent.com/18595935/34340415-959c7cee-e9c6-11e7-9923-d874632b8b03.png)

## 5.4 线性模型

通过线性模型，能基于红酒的各种化学特征，对红酒品质进行预测。
按照特征与品质之间的相关强度，递增的方式建立模型。

```python
m1 <- lm(formula = quality ~ volatile.acidity, data = wine)
m2 <- update(m1,~ . + alcohol)
m3 <- update(m2,~ . + sulphates)
m4 <- update(m3,~ . + citric.acid)
m5 <- update(m4,~ . + total.sulfur.dioxide)
m6 <- update(m5,~ . + chlorides)
m7 <- update(m6,~ . + density)

#install.packages("memisc")
suppressMessages(library(lattice))
suppressMessages(library(MASS))
suppressMessages(library(memisc))
mtable(m1,m2,m3,m4,m5,m6,m7)
```


![image](https://user-images.githubusercontent.com/18595935/34340420-a0a8f4fa-e9c6-11e7-944d-f6c2c1685a3b.png)

当模型选取6个参数时有最小的AIC值，加入第七个参数后其AIC又开始增加。

最终模型应该是如下：
`quality = 2.985 - 1.104*volatile.acidity + 0.276*alcohol +
0.908*sulphates + 0.065*citric.acid - 
0.002*total.sulfur.dioxide - 1.763*chlorides`


## 5.5 多变量分析

### 探讨你在这部分探究中观察到的一些关系。通过观察感兴趣的特性，是否存在相互促进的特性？

通过上面的单变量和双变量分析，都没有发现对红酒品质产生决定性影响的变量，通过对多变量的分析，观察到了如下影响到红酒品质的关系：
- 挥发性酸越低，红酒品质越高
- 硫酸盐越高，红酒品质也越高
- 酒精浓度越高，红酒品质也越高

另外，存在如下的相互促进的特性:
- 酒精浓度越高，密度越低
- 游离二氧化硫越高，总二氧化硫越高
因为这些特性之间存在某种关联，会构成相互促进的特性也合乎逻辑。


### 这些特性之间是否存在有趣或惊人的联系呢？

通过上面的分析，了解到挥发性酸,硫酸盐,以及酒精浓度是对红酒品质影响最大的变量，前两种分别是酸味和咸味，后一种作为酒类最重要的组成元素，这三类味觉对红酒品质影响最大，这也符合常识。


### 选项：你是否创建过数据集的任何模型？讨论你模型的优缺点。

创建了一个线性模型，递增使用了7个变量，选取了AIC值最小时的6个变量建立的线性模型，这6个变量没有经过任何处理，所以红酒品质预测结果与这6个变量完全是线性关系，所以最终结果可能不是很准确。


------

# 6. 定稿图与总结

## 6.1 描述一
针对上面的quality/alcohol(plot-2)和quality/volatile.acidity(plot-2)，能够发现quality与alcohol和volatile.acidity之间的一些变化趋势，下面将红酒品质处理成了三个等级分别为low(0,4], medium(4,6], high(6,8]，另外对density和citric.acid也做同样的绘图。
从四个图形中能得到如下结论：
- 大部分的红酒其品质居中
- 红酒品质越高，挥发性酸`volatile.acidity`整体上越低
- 红酒品质越高，酒精度数`alcohol`，柠檬酸 `citric.acid`和硫酸盐`sulphates`整体上越低

## 6.2 绘图一:

```python
# 公用函数
univ_boxplot_grade <- function(featureY,title,ylab) {
    ggplot(wine,aes_string(x="grade", y=featureY)) + 
    geom_jitter(alpha=0.2,aes(color = quality)) +
    geom_boxplot( alpha = 0.5,aes(fill = quality)) +
    scale_fill_gradient("Quality",low = "green", high = "blue") +
    stat_summary(fun.y = "mean", 
      geom = "point", 
      color = "red")+
    geom_smooth(method='lm', aes(group = 1)) + 
    ggtitle(title) + 
    ylab(ylab)+
    theme(legend.text=element_text(size=10),legend.title=element_text(size=10)) + 
    theme(legend.position="top")     + 
    theme(plot.title = element_text(size = 14, face = "bold")) + 
    theme(axis.text=element_text(size=12),
        axis.title=element_text(size=12))
}
```

```python
p1 <- univ_boxplot_grade("volatile.acidity","Volatile.acidity vs Wine quality",
                         "density(g/ml)")

p2 <- univ_boxplot_grade("alcohol","Alcohol vs Wine quality","alcohol(°)")

p3 <- univ_boxplot_grade("citric.acid","Citric.acid vs Wine quality",
                         "citric.acid(g/ml)")

p4 <- univ_boxplot_grade("alcohol","Sulphates vs Wine quality",
                         "sulphates(g/ml)")

library(gridExtra)
grid.arrange(p1,p2,ncol=2)
grid.arrange(p3,p4,ncol=2)

```

![image](https://user-images.githubusercontent.com/18595935/34340452-095ab650-e9c7-11e7-94bc-fd113bf4c5b7.png)

![image](https://user-images.githubusercontent.com/18595935/34340453-0bad4a6c-e9c7-11e7-82b9-1e0d911ab5e5.png)

## 6.3 描述二
在不同品质下，酒精度数与水密度之间的分布图，从图中可以看出:
- 红酒品质越高，酒精度数整体越高
- 酒精度数越高，水密度整体越低

## 6.4 绘图二

```python
ggplot(aes(x = alcohol, y = density, color = factor(quality)), data = wine) +
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  geom_smooth(method = "lm", se = FALSE,size=1) +
  scale_color_brewer(palette = "Blues") +
 ggtitle("Alcohol vs Density")+
 ylab("density (g/ml)")+
 xlab("alcohol content (mg/L)")+
  theme(legend.text=element_text(size=10),legend.title=element_text(size=10)) + 
  theme(legend.position="right") + 
  theme(plot.title = element_text(size = 14, face = "bold")) + 
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=12))
```

![image](https://user-images.githubusercontent.com/18595935/34340454-0e6dc29a-e9c7-11e7-8e10-29df1b849a20.png)



## 6.5 描述三

在上面的双变量分析中，探讨了红酒品质与酒精浓度的关系，但是该图红酒品质分级过多，不是一目了然。下面使用综合后的品质属性grade，与酒精浓度进行绘图。

如下是不同红酒品质下，不同酒精度数红酒的数量分布，从下面的分布图中可以看出:
- 大部分红酒品质居中
- 随着度数增加，品质高的红酒增加

## 6.6 绘图三

```python
ggplot(wine, aes(x=alcohol, color=grade, fill=grade)) +
  geom_histogram( position="identity", alpha=0.2,binwidth = 0.2)+
  geom_density(alpha=0.6)+
  scale_color_manual(values=c("#7CB9E8", "#72A0C1", "#00308F"))+
  scale_fill_manual(values=c("#7CB9E8", "#72A0C1", "#00308F"))+
  labs(title="Alcohol vs Count",x="Alcohol(°)", y = "Count") +
  theme(legend.text=element_text(size=10),legend.title=element_text(size=10)) + 
  theme(legend.position="right") + 
  theme(plot.title = element_text(size = 14, face = "bold")) + 
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=12))
```

![image](https://user-images.githubusercontent.com/18595935/34340455-10bb23e4-e9c7-11e7-877c-93d18d4edf36.png)

------

# 7. 反思

本数据集包含了1599条记录，11个变量，通过分析这些变量与品质之间的相关关系，判断变量是如何影响红酒品质的。
但是这些变量中没有哪种变量能够决定性的影响红酒品质，最终通过多个变量的分析，判断如下四种变量最能影响红酒品质：
- 酒精度数，与品质呈正相关关系，度数越高品质趋向升高
- 挥发性酸，与品质呈负相关关系，酸度越高品质趋向降低
- 硫酸盐，与品质呈正相关关系，硫酸盐越多品质趋向升高
- 柠檬酸，与品质呈正相关关系，酸度越高品质趋向降低,通过数据分析之前，认为柠檬酸与品质应该是强相关的，但是经过分析之后发现其相关度并不高

另外，同样影响味觉的甜味和咸味，即变量残糖`residual.sugar`和氯化物`chlorides`，其对品质的影响微弱，可见得到一个结论需要科学的分析，不能凭直觉判断。

后续如果引入机器学习进行分析，另外加大数据量，应该能更精确的分析哪些变量对红酒品质的影响。另外，对于颜色的应用再更深入的话，应该能使整个分析的图形更加美观协调。

# 参考资料：

1. [是什么，影响了葡萄酒的“平衡”](http://wap.lookvin.com/news/46115.html)
2. [overlay histogram by certain order of fill color
](https://stackoverflow.com/questions/31216130/overlay-histogram-by-certain-order-of-fill-color)
3. [Quick start guide - R software and data visualization](http://www.sthda.com/english/wiki/ggplot2-histogram-plot-quick-start-guide-r-software-and-data-visualization) 
4. [R语言对红酒各因素进行探索性分析](http://blog.csdn.net/einstellung/article/details/76228099)