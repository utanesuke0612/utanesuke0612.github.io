---
layout: post
title: Uda-DataAnalysis-26--练习：探索两个变量
date: 2017-11-23 03:00:04
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 1. 练习: 价格与 X

```{r}
ggplot(aes(x=x,y=price),data = diamonds) + geom_point()
```

![image](https://user-images.githubusercontent.com/18595935/33719302-a4301274-dba3-11e7-882f-1615299be7d8.png)


# 2. 发现 - 价格与 x

some outliers and an exponential relationship between price and x。

# 3. 练习: 相关性

```{r}
cor(diamonds$x,diamonds$price)
cor(diamonds$y,diamonds$price)
cor(diamonds$z,diamonds$price)
```

# 4. 练习: 价格与深度

```{r}
ggplot(aes(x=depth,y=price),data = diamonds) + geom_point()
```

![image](https://user-images.githubusercontent.com/18595935/33719670-e16c17b8-dba4-11e7-8536-5733e067a4c3.png)

# 8. 练习: 价格与克拉

Create a scatterplot of price vs carat and omit the top 1% of price and carat values.

```{r}
ggplot(aes(x=carat,y=price),data = diamonds) +
  geom_point() + 
  xlim(0,quantile(diamonds$carat,0.99)) +
  ylim(0,quantile(diamonds$price,0.99)) +
  geom_smooth(method="lm",color="red")
```

![image](https://user-images.githubusercontent.com/18595935/33720475-656f3df4-dba7-11e7-9a46-865b16f120d5.png)



# 9. 价格与体积
Create a scatterplot of price vs. volume (x * y * z).This is a very rough approximation for a diamond's volume.
Create a new variable for volume in the diamonds data frame.

存在异常值，所以去除了1%的数据。

```{r}
diamonds$volumn = diamonds$x * diamonds$y * diamonds$z

ggplot(aes(x=volumn,y=price),data = diamonds) +
  geom_point() +
  xlim(0,quantile(diamonds$volumn,0.99))
```

![image](https://user-images.githubusercontent.com/18595935/33720537-9b3554fa-dba7-11e7-9b9c-3cea8615f0e0.png)

观察上面的图形，有不少volume为0的点，通过下面的方法可以找到这个异常点的个数：

```{r}
library(plyr)
count(diamonds$volumn == 0)
```

![image](https://user-images.githubusercontent.com/18595935/33720724-370b8c96-dba8-11e7-98fe-b1dc207d2bbc.png)



# 11. 子集相关性

排除体积大于或等于 800 的钻石，以及为0的钻石，求price与体积的相关性：
提示:当你子集化原始数据框时，在两个条件之间使用`&`符号。

```{r}
with(subset(diamonds,diamonds$volumn > 0 & diamonds$volumn <= 800),cor.test(price,volumn,method="pearson"))
```


结果为：


```python
Pearson's product-moment correlation

data:  price and volumn
t = 486.33, df = 53938, p-value < 2.2e-16
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 0.9008054 0.9039398
sample estimates:
      cor 
0.9023845 
```


# 12. 练习: 调整 - 价格与体积







