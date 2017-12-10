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

```{r}
ggplot(aes(x=volumn,y=price),data=subset(diamonds,diamonds$volumn > 0 & diamonds$volumn <= 800)) + geom_point(alpha = 1/20) + geom_smooth()
```

![image](https://user-images.githubusercontent.com/18595935/33767033-6934f278-dc63-11e7-88ad-c22937a84aaa.png)


# 13. 练习: 平均价格 - 净度

Use the function dplyr package to create a new data frame containing info on diamonds by clarity.
- Name the data frame diamondsByClarity
- The data frame should contain the following,variables in this order.
(1) mean_price
(2) median_price
(3) min_price
(4) max_price
(5) n
- where n is the number of diamonds in each level of clarity.


- 方案1

```{r}
suppressMessages(library(ggplot2))
suppressMessages(library(dplyr))

data(diamonds)
diamonds.diamondsByClarity <- diamonds %>%
  group_by(clarity) %>%
  summarise(mean_price = mean(price),
            median_price = median(price),
            min_price = min(price),
            max_price = max(price),
            n = n()) %>%
  arrange(clarity)
head(diamonds.diamondsByClarity,100)
```

- 方案2

```{r}
suppressMessages(library(ggplot2))
suppressMessages(library(dplyr))

data(diamonds)
clarity_groups <- group_by(diamonds,clarity)
diamonds.diamondsByClarity <- summarise(clarity_groups,
                          mean_price = mean(price),
            median_price = median(price),
            min_price = min(price),
            max_price = max(price),
            n = n())
head(diamonds.diamondsByClarity,10)
```

- 最终得到相同的数据集：通过clarity分组，然后计算各组的描述统计量：

![image](https://user-images.githubusercontent.com/18595935/33788852-f56dcf18-dcb7-11e7-9c79-f7f6523d23cd.png)


# 14. 练习: 平均价格柱状图

We’ve created summary data frames with the mean price　by clarity and color. You can run the code in R to　verify what data is in the variables diamonds_mp_by_clarity　and diamonds_mp_by_color.

Your task is to write additional code to create two bar plots　on one output image using the grid.arrange() function from the package　gridExtra.



```{r}
diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))

diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))

```

通过上面的代码，将数据进行分组，上面数据是如下的构成：

![image](https://user-images.githubusercontent.com/18595935/33789172-18e39c3c-dcba-11e7-92a6-a4d43c9dce8e.png)

通过上面的group_by后没有改变原始数据的行数和列数，只是在其中追加了一些变量，为后面的summarise做准备：

![image](https://user-images.githubusercontent.com/18595935/33789326-1a67bde4-dcbb-11e7-9407-7e559d90cc12.png)


最终得到的分组汇总后数据如下：

![image](https://user-images.githubusercontent.com/18595935/33789368-54c18b28-dcbb-11e7-9ada-6cfe9ade7b8d.png)

- 练习：

```{r}
p1 <- ggplot(aes(x=clarity,y=mean_price),data=diamonds_mp_by_clarity) + geom_boxplot()
p2 <- ggplot(aes(x=color,y=mean_price),data=diamonds_mp_by_color) + geom_boxplot()

library(gridExtra)
grid.arrange(p1,p2,ncol=1)
```

![image](https://user-images.githubusercontent.com/18595935/33789397-72828720-dcbb-11e7-9da0-75d867eb4c76.png)


# 15. 练习: 平均价格的趋势

We think something odd is going here. These trends seem to go against our intuition.
Mean price tends to decrease as clarity improves. The same can be said for color.
We encourage you to look into the mean price across cut.


```{r}
diamonds_by_cut <- group_by(diamonds, cut)
diamonds_mp_by_cut <- summarise(diamonds_by_cut, mean_price = mean(price))
ggplot(aes(x=cut,y=mean_price),data=diamonds_mp_by_cut) + geom_boxplot()
```


![image](https://user-images.githubusercontent.com/18595935/33789532-686fddc2-dcbc-11e7-9331-8e0fffbb16d0.png)

感觉还是哪里不对，为什么最好成分的钻石其价格还不是最高呢？可能跟克拉数有关，按照钻石成分对克拉数做个分析：

```{r}
diamonds_by_cut <- group_by(diamonds, cut)
diamonds_mp_by_cut <- summarise(diamonds_by_cut, mean_carat = mean(carat))
ggplot(aes(x=cut,y=mean_carat),data=diamonds_mp_by_cut) + geom_boxplot()
```

![image](https://user-images.githubusercontent.com/18595935/33789577-dfa9e4be-dcbc-11e7-88ce-cbb2e3973716.png)


果然，成分最好的钻石克拉数少，而Fair成分最差的钻石其克拉数多，所以价格呈现上面一幅图的状态。


# 16. 练习: 重访 Gapminder

The Gapminder website contains over 500 data sets with information about the world's population. Your task is to continue the investigation you did at the end of Problem Set 3 or you can start fresh and choose a different data set from Gapminder.

If you’re feeling adventurous or want to try some data munging see if you can find a data set or scrape one from the web.

In your investigation, examine pairs of variable and create 2-5 plots that make use of the techniques from Lesson 4.

You can find a link to the Gapminder website in the Instructor Notes.

Once you've completed your investigation, create a post in the discussions that includes:

1. the variable(s) you investigated, your observations, and any summary statistics
2. snippets of code that created the plots
3. links to the images of your plots


`略`

