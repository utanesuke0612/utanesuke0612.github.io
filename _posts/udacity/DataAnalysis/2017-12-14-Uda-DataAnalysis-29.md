---
layout: post
title: Uda-DataAnalysis-29--钻石与价格预测
date: 2017-12-14 05:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 3. 练习：散点图回顾


```python
# Let's consider the price of a diamond and it's carat weight.
# Create a scatterplot of price (y) vs carat weight (x).

# Limit the x-axis and y-axis to omit the top 1% of values.
```

```{r}
ggplot(aes(x=diamonds$carat,y=diamonds$price),data=diamonds) + 
  geom_point(fill=I("#F79420"),color=I("blue"),shape=21) + 
  xlim(0,quantile(diamonds$carat,0.99)) + 
  ylim(0,quantile(diamonds$price,0.99))
```


![image](https://user-images.githubusercontent.com/18595935/33993422-cfacfa54-e119-11e7-91a8-b30d151e93d0.png)


# 4. 练习：价格与克拉的关系

- 上图的基础上添加了一个平滑曲线，但是如果用这个曲线去做预测的话，会丢失很多信息。

```{r}
ggplot(aes(x=diamonds$carat,y=diamonds$price),data=diamonds) + 
  geom_point(fill=I("#F79420"),color=I("blue"),shape=21) + 
  xlim(0,quantile(diamonds$carat,0.99)) + 
  ylim(0,quantile(diamonds$price,0.99)) +
  stat_smooth(method = "lm")
```


![image](https://user-images.githubusercontent.com/18595935/33993521-35193fe2-e11a-11e7-8092-00285d80483a.png)

# 7. 练习: Ggpairs 函数

```{r}
#install these if necessary
#install.packages('GGally')
#install.packages('scales')
#install.packages('memisc')
#install.packages('lattice')
#install.packages('MASS')
#install.packages('car')
#install.packages('reshape2')
#install.packages('dplyr')

# load the ggplot graphics package and the others
library("ggplot2")
library("GGally")
library("scales")
library("memisc")

# sample 10,000 diamonds from the data set
set.seed(20022012)
diamond_samp <- diamonds[sample(1:length(diamonds$price), 10000), ]
ggpairs(diamond_samp)
ggsave("diamond_samp")
```

运行上述代码时出错了，使用如下的方式解决了：

```{r}
remove.packages(c("ggplot2", "data.table"))
install.packages('Rcpp', dependencies = TRUE)
install.packages('ggplot2', dependencies = TRUE)
install.packages('data.table', dependencies = TRUE)
```


最终图形如下，可以看到price与x/y/z有很强的相关性：

![image](https://user-images.githubusercontent.com/18595935/33994554-4860a762-e11e-11e7-926c-face0880dc66.png)


# 8. 练习: 对钻石的需求


```python
# Create two histograms of the price variable
# and place them side by side on one output image.

# We’ve put some code below to get you started.

# The first plot should be a histogram of price
# and the second plot should transform
# the price variable using log10.

# Set appropriate bin widths for each plot.
# ggtitle() will add a title to each histogram.
```

- 按照视频中的代码，没办法将两个plot排列起来，只能分开了，这里使用的是qplot描绘

```{r}
qplot(data=diamonds,x=price,binwidth=100,fill=I("#099DD9")) + 
  ggtitle('Price')
```

![image](https://user-images.githubusercontent.com/18595935/33995807-75b8e3ec-e122-11e7-8d55-60af286f962a.png)


```{r}
qplot(data=diamonds,x=price,binwidth=0.01,fill=I("#F79420")) + 
  ggtitle('Price (log10)') + scale_x_log10()
```

![image](https://user-images.githubusercontent.com/18595935/33996008-1ff6d756-e123-11e7-8481-a64a5ff91791.png)


- 使用`ggplot`描画：

```{r}
p1 <- ggplot(aes(x = diamonds$price), data = diamonds) + 
  geom_histogram(binwidth = 100,fill=I("#099DD9"),color=I("blue")) +
  ggtitle('Price') 
  
p2 <- ggplot(aes(x = log10(diamonds$price)), data = diamonds) +
  geom_histogram(binwidth = 0.01,fill=I("#F79420"),color=I("blue")) +
  ggtitle('Price (log10)') 

library(gridExtra)
grid.arrange(p1,p2,ncol=1)
```


![image](https://user-images.githubusercontent.com/18595935/33996038-3a999166-e123-11e7-8bae-1882ff314b49.png)


# 9. 将需求与价格分布联系起来

```{r}
qplot(data=diamonds,x=price,binwidth=0.05,fill=I("#F79420")) + 
  ggtitle('Price (log10)') + scale_x_log10() + facet_wrap(~cut)
```

- 下图可以看出，价格较低，但是成色最好的钻石，有最好的销量。

![image](https://user-images.githubusercontent.com/18595935/33996416-7c33782a-e124-11e7-86db-166c80ecfde9.png)


# 10. 散点图转换

- x轴是carat，y轴是price的对数(使用视频中的`trans=log10_trans()`出错了)：

```{r}
qplot(carat,price,data=diamonds) + ggtitle("Price log10 by carat") +scale_y_log10()
```

![image](https://user-images.githubusercontent.com/18595935/33997004-500d142a-e126-11e7-85d0-f29871210a02.png)

- 没有使用自定义函数，下图跟视频要求不一致：

```{r}
ggplot(aes(x = carat,price),data=diamonds) + 
  geom_point() + 
  scale_x_continuous(limits = c(0.2,3),
                     breaks = c(0.2,0.5,1,2,3)) +
  scale_y_continuous(limits = c(350,15000),
                     breaks = c(350,1000,5000,10000,15000)) +
  scale_y_log10() +
  ggtitle("Price (log10) by Cube-Root of Carat")
```


![image](https://user-images.githubusercontent.com/18595935/33997973-805c8edc-e129-11e7-9e10-2038c46959c0.png)

# 11. 练习: 复习过度绘制

观察上面一个图形，由于所有的点都堆积在一起，无法看出分布规律，调整一下绘图方式：

```{r}
ggplot(aes(x = carat,price),data=diamonds) + 
  geom_point(alpha=0.1,size=0.75,position ="jitter") + 
  scale_x_continuous(limits = c(0.2,3),
                     breaks = c(0.2,0.5,1,2,3)) +
  scale_y_continuous(limits = c(350,15000),
                     breaks = c(350,1000,5000,10000,15000)) +
  scale_y_log10() +
  ggtitle("Price (log10) by Cube-Root of Carat")
```

![image](https://user-images.githubusercontent.com/18595935/34045123-fa706da8-e1ea-11e7-804f-5c5d3ee3e9b4.png)

通过上面的图就能看到关键区域和疏密程度了。

# 13. 练习: 价格与克拉和净度

上面考察了克拉与价格的关系，价格除了与克拉有关系外，与净度也有关系，下面使用净度来上色：


```{r}
ggplot(aes(x = carat,price),data=diamonds) + 
  geom_point(alpha=0.5,size=0.75,position ="jitter",aes(color=diamonds$clarity)) + 
  scale_color_brewer(type="div",
                     guide = guide_legend(title="Clarity",reverse = TRUE,
                                          override.aes = list(alpha=1,size=2))) +
  scale_x_continuous(limits = c(0.2,3),
                     breaks = c(0.2,0.5,1,2,3)) +
  scale_y_continuous(limits = c(350,15000),
                     breaks = c(350,1000,5000,10000,15000)) +
  scale_y_log10() +
  ggtitle("Price (log10) by Cube-Root of Carat") + 
  theme(legend.position="right") 
```


![image](https://user-images.githubusercontent.com/18595935/34045532-9e5a4a82-e1ec-11e7-8f46-5b8778cfe175.png)



# 15. 价格与克拉和切工

- 与上面的绘制方式完全一致，只是将净度控制颜色换成了cut即切工控制颜色。

```{r}
ggplot(aes(x = carat,price),data=diamonds) + 
  geom_point(alpha=0.5,size=0.75,position ="jitter",aes(color=diamonds$cut)) + 
  scale_color_brewer(type="div",
                     guide = guide_legend(title="Clarity",reverse = TRUE,
                                          override.aes = list(alpha=1,size=2))) +
  scale_x_continuous(limits = c(0.2,3),
                     breaks = c(0.2,0.5,1,2,3)) +
  scale_y_continuous(limits = c(350,15000),
                     breaks = c(350,1000,5000,10000,15000)) +
  scale_y_log10() +
  ggtitle("Price (log10) by Cube-Root of Cut") + 
  theme(legend.position="right") 
```

![image](https://user-images.githubusercontent.com/18595935/34046023-d2f63be6-e1ee-11e7-9114-5f22d5ab7496.png)

# 17. 价格与克拉和颜色

```{r}
ggplot(aes(x = carat,price),data=diamonds) + 
  geom_point(alpha=0.5,size=0.75,position ="jitter",aes(color=diamonds$color)) + 
  scale_color_brewer(type="div",
                     guide = guide_legend(title="Clarity",reverse = TRUE,
                                          override.aes = list(alpha=1,size=2))) +
  scale_x_continuous(limits = c(0.2,3),
                     breaks = c(0.2,0.5,1,2,3)) +
  scale_y_continuous(limits = c(350,15000),
                     breaks = c(350,1000,5000,10000,15000)) +
  scale_y_log10() +
  ggtitle("Price (log10) by Cube-Root of color") + 
  theme(legend.position="right") 
```

![image](https://user-images.githubusercontent.com/18595935/34046185-86af1414-e1ef-11e7-84bc-6369d4ddefdf.png)

# 20. 构建线性模型

参照資料：[R 中的线性模型和运算符](http://data.princeton.edu/R/linearModels.html)

```{r}
m1 <- lm(I(log(price)) ~ I(carat^(1/3)),data = diamonds)
m2 <- update(m1,~ . + carat)
m3 <- update(m2,~ . + cut)
m4 <- update(m3,~ . + color)
m5 <- update(m4,~ . + clarity)

mtable(m1,m2,m3,m4,m5)
```

- 输出：

```
Calls:
m1: lm(formula = I(log(price)) ~ I(carat^(1/3)), data = diamonds)
m2: lm(formula = I(log(price)) ~ I(carat^(1/3)) + carat, data = diamonds)
m3: lm(formula = I(log(price)) ~ I(carat^(1/3)) + carat + cut, data = diamonds)
m4: lm(formula = I(log(price)) ~ I(carat^(1/3)) + carat + cut + color, 
    data = diamonds)
m5: lm(formula = I(log(price)) ~ I(carat^(1/3)) + carat + cut + color + 
    clarity, data = diamonds)
```

![image](https://user-images.githubusercontent.com/18595935/34074513-26fa1e14-e2f4-11e7-8a92-40cc8d613a98.png)


# 22. 练习: 更大、更好的数据集

从  https://github.com/solomonm/diamonds-data   下载 ，然后加载`load("BigDiamonds.rda")`。
过滤了1万美元以上的，以及限定鉴定机构为GIA。

```{r}
diamondsbig$logprice = log(diamondsbig$price)


m1 <- lm(logprice ~ I(carat^(1/3)),
  data=diamondsbig[diamondsbig$price<10000 & 
                     diamondsbig$cert == "GIA",]
)
m2 <- update(m1,~ . + carat)
m3 <- update(m2,~ . + cut)
m4 <- update(m3,~ . + color)
m5 <- update(m4,~ . + clarity)

suppressMessages(library(lattice))
suppressMessages(library(MASS))
suppressMessages(library(memisc))
mtable(m1, m2, m3, m4, m5)
```

`结果输出略`

# 23. 预测

```{r}
thisDiamond = data.frame(carat = 1.00,cut="V.Good",
                         color="I",clarity="VS1")

modelEstimate = predict(m5,newdata = thisDiamond,
                        interval = "prediction",level=.95)

exp(modelEstimate)
```

- 输出：

fit 1 5040.436 
lwr 3730.34 
upr 6810.638