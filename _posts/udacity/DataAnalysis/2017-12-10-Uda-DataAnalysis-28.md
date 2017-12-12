---
layout: post
title: Uda-DataAnalysis-28--习题集：探索多个变量
date: 2017-12-09 04:00:01
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 1. 练习: 带有分面和颜色的价格直方图

- 要求：

```python
# Create a histogram of diamond prices.
# Facet the histogram by diamond color
# and use cut to color the histogram bars.

# The plot should look something like this.
# http://i.imgur.com/b5xyrOu.jpg

# Note: In the link, a color palette of type
# 'qual' was used to color the histogram using
# scale_fill_brewer(type = 'qual')
```

- 代码与图形，按`color`切割为多个面，即多个图，按照`cut`区分各个直方图中的颜色：

```{r}
ggplot(aes(x=price),data=diamonds) + 
	geom_histogram(aes(color=cut)) + 
	facet_wrap(~color,ncol = 2)
```

![image](https://user-images.githubusercontent.com/18595935/33805615-423ddc6e-ddff-11e7-970d-5f17f1bf4e6b.png)


# 2. 练习: 价格与按切工填色的table

```python
# Create a scatterplot of diamond price vs.
# table and color the points by the cut of
# the diamond.

# The plot should look something like this.
# http://i.imgur.com/rQF9jQr.jpg

# Note: In the link, a color palette of type
# 'qual' was used to color the scatterplot using
# scale_color_brewer(type = 'qual')
```

- 散点图，`scale_color_brewer(type = 'qual')`指描绘使用的颜色种类，通过`?scale_color_brewer`看帮助。

```{r}
ggplot(aes(x=price,y=table),data=diamonds) + geom_point(aes(color=cut)) + 
  scale_color_brewer(type = 'qual')
```

![image](https://user-images.githubusercontent.com/18595935/33805794-b42820f8-de01-11e7-82fb-94b3a8e92dd3.png)

`table` 的含义是：`width of top of diamond relative to widest point (43–95)`。


# 3. 练习: 典型表值

大多数完美切工钻石的典型表范围是多少？
大多数优质切工钻石的典型表范围是多少？在之前练习中创建的图表查看答案。无需进行汇总。

![image](https://user-images.githubusercontent.com/18595935/33805775-70f26fdc-de01-11e7-87ec-999c2cfc33a6.png)

# 4. 练习: 价格与体积和钻石净度

```python
# Create a scatterplot of diamond price vs.
# volume (x * y * z) and color the points by
# the clarity of diamonds. Use scale on the y-axis
# to take the log10 of price. You should also
# omit the top 1% of diamond volumes from the plot.

# Note: Volume is a very rough approximation of
# a diamond's actual volume.

# The plot should look something like this.
# http://i.imgur.com/excUpea.jpg

# Note: In the link, a color palette of type
# 'div' was used to color the scatterplot using
# scale_color_brewer(type = 'div')
```

```{r}
diamonds$volumn <- diamonds$x * diamonds$y * diamonds$z

ggplot(aes(x=diamonds$volumn,y=log10(price)),data=diamonds) + 
  geom_point(aes(color=clarity)) + 
  xlim(0,quantile(diamonds$volumn,0.99))
```

![image](https://user-images.githubusercontent.com/18595935/33833528-445c44da-dec3-11e7-9629-c0355162a528.png)



# 5. 练习：新建友谊的比例 (使用`ifelse`)

```{r}
# Your task is to create a new variable called 'prop_initiated'
# in the Pseudo-Facebook data set. The variable should contain
# the proportion of friendships that the user initiated.
```

```{r}
pf$prop_initiated <- ifelse(pf$friend_count>0,pf$friendships_initiated / pf$friend_count,0)
summary(pf$prop_initiated)
```

![image](https://user-images.githubusercontent.com/18595935/33834730-43db3274-dec7-11e7-8ea4-d03427dace44.png)


# 6. 练习: Prop_initiated 与使用时长

```python
# Create a line graph of the median proportion of
# friendships initiated ('prop_initiated') vs.
# tenure and color the line segment by
# year_joined.bucket.

# Recall, we created year_joined.bucket in Lesson 5
# by first creating year_joined from the variable tenure.
# Then, we used the cut function on year_joined to create
# four bins or cohorts of users.

# (2004, 2009]
# (2009, 2011]
# (2011, 2012]
# (2012, 2014]

# The plot should look something like this.
# http://i.imgur.com/vNjPtDh.jpg
# OR this
# http://i.imgur.com/IBN1ufQ.jpg
```


```{r}
library("dplyr")

# ①　按照tenure分组数据
tenure_groups <- group_by(subset(pf,!is.na(tenure)), tenure) 

# ②　针对tenure_groups数据集，重新组织数据，注意这里不要使用`pf$prop_initiated`.
pf.fc_by_tenure <- summarise(tenure_groups,
                             median_prop = median(prop_initiated),
                             n=n())

# 根据tenure天数，计算加入的年份
pf.fc_by_tenure$year_joined <- 2014 - ceiling(pf.fc_by_tenure$tenure / 365)

# ③ 切断数据
pf.fc_by_tenure$year_joined.bucket <- cut(pf.fc_by_tenure$year_joined,breaks = c(2004,2009,2011,2012,2014))


ggplot(aes(x=tenure,y=median_prop),data=pf.fc_by_tenure) + 
  geom_line(aes(color=pf.fc_by_tenure$year_joined.bucket)) +
  scale_x_continuous(breaks = seq(0, 3500, 500)) +
  theme(legend.text=element_text(size=10),legend.title=element_text(size=10)) + theme(legend.position="top")
```

![image](https://user-images.githubusercontent.com/18595935/33889036-406ea488-df92-11e7-800c-486eff3e3b1f.png)


- ①　按照tenure分组数据,比较分组后的数据和pf原始数据，分组后的数据再pf原始数据上增加了一些属性：

```
tenure_groups <- group_by(subset(pf,!is.na(tenure)), tenure) 
```

![image](https://user-images.githubusercontent.com/18595935/33889550-c465bffa-df93-11e7-8589-2342aa7b5f58.png)


- ②　针对tenure_groups数据集，重新组织数据

`prop_initiated` 参考上面一个问题

```
pf$prop_initiated <- ifelse(pf$friend_count>0,pf$friendships_initiated / pf$friend_count,0)
```

```
pf.fc_by_tenure <- summarise(tenure_groups,
                             median_prop = median(prop_initiated),
                             n=n())

head(pf.fc_by_tenure,1000)
```


![image](https://user-images.githubusercontent.com/18595935/33889802-a264ac12-df94-11e7-84eb-ea75f425a5df.png)


- ③ 切断数据

经过下面的数据后，数据结构变成：

```
pf.fc_by_tenure$year_joined <- 2014 - ceiling(pf.fc_by_tenure$tenure / 365)
pf.fc_by_tenure$year_joined.bucket <- cut(pf.fc_by_tenure$year_joined,breaks = c(2004,2009,2011,2012,2014))
head(pf.fc_by_tenure,1000)
```

![image](https://user-images.githubusercontent.com/18595935/33889873-da245bf2-df94-11e7-9a72-48d35137a47f.png)


# 7. 平滑化 prop_initiated 与使用时长


```python
# Smooth the last plot you created of
# of prop_initiated vs tenure colored by
# year_joined.bucket. You can bin together ranges
# of tenure or add a smoother to the plot.
```

基于前一部分产生的数据，使用如下代码得到一个平滑线：


```{r}
ggplot(aes(x=tenure,y=median_prop),data=pf.fc_by_tenure) + 
 
  scale_x_continuous(breaks = seq(0, 3500, 500)) +
  theme(legend.text=element_text(size=10),legend.title=element_text(size=10)) + theme(legend.position="top") +
  geom_smooth(aes(color = year_joined.bucket))
```


![image](https://user-images.githubusercontent.com/18595935/33890144-b344cf84-df95-11e7-86b6-f384d1d8253b.png)



