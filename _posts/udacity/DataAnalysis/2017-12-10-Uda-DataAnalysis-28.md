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