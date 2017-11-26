---
layout: post
title: Uda-DataAnalysis-24--习题集：探索单一变量
date: 2017-11-23 02:00:03
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 1. 练习：钻石

```{r}
library(ggplot2)
data(diamonds)
summary(diamonds)
```

在environment中可以查看到diamond中的相关信息。

```{r}
?diamonds
```

查看对应的帮助文件。


# 2. 练习：价格直方图

```{r}
ggplot(aes(x = price), data = diamonds) + geom_histogram(binwidth = 10)
```

![image](https://user-images.githubusercontent.com/18595935/33240479-ab3e50ec-d2f9-11e7-9173-2e925147388e.png)

# 3. 练习：价格直方图小结

```{r}
summary(diamonds$price)
```

   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     950    2401    3933    5324   18823 

# 4. 练习：钻石数量

```{r}
summary(diamonds$price >= 15000)
```

使用上述代码，取出符合条件的数据。

# 5. 练习：廉价钻石


```{r}
ggplot(aes(x = price), data = diamonds) + geom_histogram(binwidth = 10) + scale_x_continuous(breaks = 1:1000) 
                                                            
```

![image](https://user-images.githubusercontent.com/18595935/33240507-202f5aa4-d2fa-11e7-947d-012532b1e64b.png)


# 6. 练习：切工-价格直方图

```{r}
ggplot(aes(x = price), data = diamonds) + geom_histogram(binwidth = 10) + scale_x_continuous(breaks = 1:15000) + facet_wrap(~cut,ncol = 2)
```

根据cut进行分面。


![image](https://user-images.githubusercontent.com/18595935/33240521-4fee90ac-d2fa-11e7-8332-8cd1037645a1.png)


# 7. 练习：切工-价格

按照cut进行区分，将价格price的summary输出：

```{r}
by(diamonds$price,diamonds$cut,summary)
```

diamonds$cut: Fair
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    337    2050    3282    4359    5206   18574 

--------------------------------------------------------------------------------------- 

diamonds$cut: Good
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    327    1145    3050    3929    5028   18788 

--------------------------------------------------------------------------------------- 

diamonds$cut: Very Good
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    336     912    2648    3982    5373   18818 

--------------------------------------------------------------------------------------- 

diamonds$cut: Premium
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326    1046    3185    4584    6296   18823 

--------------------------------------------------------------------------------------- 

diamonds$cut: Ideal
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     878    1810    3458    4678   18806 

# 8. 练习：标尺和多直方图

```{r}
qplot(x = price, data = diamonds) + facet_wrap(~cut)
```

![image](https://user-images.githubusercontent.com/18595935/33240544-c53b09d0-d2fa-11e7-90cf-220019c584b8.png)


# 9. 练习：由切工决定的每克拉价格

```{r}
ggplot(aes(x = price/carat), data = diamonds) + geom_histogram(binwidth = 1) + scale_x_continuous(breaks = 1:15000) + facet_wrap(~cut,ncol = 2) + scale_x_log10()
```

![image](https://user-images.githubusercontent.com/18595935/33240549-db229a88-d2fa-11e7-9fe8-fd950c8e8601.png)


# 10. 练习：价格箱线图

```{r}
qplot(x=color,y=price,
      data = subset(diamonds,!is.na(cut)),
      geom = "boxplot") + 
scale_y_continuous(lim = c(0,15000),breaks = seq(0,15000,500))
```

![image](https://user-images.githubusercontent.com/18595935/33240556-f205f83a-d2fa-11e7-92d3-c6b6173ad600.png)



# 11. 练习：四分位数间距-IQR

```{r}
by(diamonds$price,diamonds$color,summary)
```

diamonds$color: D
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    357     911    1838    3170    4214   18693 

--------------------------------------------------------------------------------------- 

diamonds$color: E
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    326     882    1739    3077    4003   18731 

--------------------------------------------------------------------------------------- 

diamonds$color: F
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    342     982    2344    3725    4868   18791 

--------------------------------------------------------------------------------------- 

diamonds$color: G
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    354     931    2242    3999    6048   18818 

--------------------------------------------------------------------------------------- 

diamonds$color: H
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    337     984    3460    4487    5980   18803 

--------------------------------------------------------------------------------------- 

diamonds$color: I
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    334    1120    3730    5092    7202   18823 

--------------------------------------------------------------------------------------- 

diamonds$color: J
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    335    1860    4234    5324    7695   18710 

# 12. 练习：由颜色表示的每克拉箱线图

```{r}
qplot(x=color,y=price/carat,
      data = subset(diamonds,!is.na(cut)),
      geom = "boxplot") + 
scale_y_continuous(lim = c(0,10000),breaks = seq(0,10000,500))
```

![image](https://user-images.githubusercontent.com/18595935/33240570-3fadc978-d2fb-11e7-8e2e-9ba134305e83.png)


# 13. 练习：克拉频率多边形

```{r}
qplot(x = carat,data = subset(diamonds,!is.na(carat)),
binwidth = 0.1,geom = "freqpoly") +
scale_x_continuous(lim = c(0,5),breaks = seq(0,5,0.5)) +
scale_y_continuous(lim = c(0,3000),breaks = seq(0,3000,500))

```

![image](https://user-images.githubusercontent.com/18595935/33240772-fd96c36a-d2fe-11e7-9e3c-997557b7ead2.png)


```{r}
table(diamonds$carat)
```

上述代码可以列举出各个carat中对应的个数。

# 14. 练习：用 R 进行数据整理

数据加工或数据整理占用数据科学家或数据分析员大量的时间，而 tidyr 和 dplyr 两种 R 包可使 R 中的这些任务更加简单。

- tidyr ： 用于重塑数据布局的包
- dplyr ： 用于帮助转换整洁的表格数据的包

# 15. 练习：Gapminder 数据

# 16. 练习：探索你的好友的生日



