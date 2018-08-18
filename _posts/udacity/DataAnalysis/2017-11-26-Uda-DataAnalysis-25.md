---
layout: post
title: Uda-DataAnalysis-25--探索两个变量
date: 2017-11-23 03:00:03
categories: 数据分析
tags: R DataAnalysis 
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

```python
ggplot(aes(x=age,y=friend_count),data = pf) + 
  geom_point(alpha = 1/20) + 
  xlim(13,113) + coord_trans(y = "sqrt")
```

![image](https://user-images.githubusercontent.com/18595935/33380299-f6ad76a0-d55d-11e7-9d94-751625fe09a1.png)

因为使用了sqrt函数，图中不能加入jitter抖动了，抖动后会使得y产生负数，那如果负数使用sqrt的话就会成为虚数。。。

# 7. Alpha 和 Jitter

- 自己的实现，使用facet_wrap进行了分面，区分的男和女的情况

```python
ggplot(aes(x=age,y=friendships_initiated),data = pf) +
  geom_jitter(alpha = 1/20) +
xlim(13,113) + facet_wrap(~gender,ncol = 2)
  
```

![image](https://user-images.githubusercontent.com/18595935/33380823-a932d328-d55f-11e7-9608-2c34861e30e7.png)

- 课程示例，上面的6说明了jitter的情况下不能使用sqrt分层，如果使用下面的形式，可以使得sqrt下使用抖动：

```python
ggplot(aes(x=age,y=friendships_initiated),data = pf) +
  geom_point(alpha = 1/10,position = position_jitter( h = 0 )) +
coord_trans(y="sqrt")

```

![image](https://user-images.githubusercontent.com/18595935/33381163-8fdc93ae-d560-11e7-8f71-2f7464b04b43.png)


# 9. 条件均值

本节中使用dplyr包，需要另外安装：


```{r}
install.packages("dplyr")
library("dplyr")
```

- 有下面两种方式对数据重新组织，最终都得到相同的结果集：

```{r}
age_groups <- group_by(pf,age)
pf.fc_by_age <- summarise(age_groups,
                          friend_count_mean = mean(friend_count),
                          friend_count_median = median(friend_count),
                          n = n())
head(pf.fc_by_age,10)
```



```{r}
pf.fc_by_age <- pf %>%
  group_by(age) %>%
  summarise(friend_count_mean = mean(friend_count),
            friend_count_median = median(friend_count),
            n = n()) %>%
  arrange(age)
head(pf.fc_by_age,100)
  
```


![image](https://user-images.githubusercontent.com/18595935/33609400-4773995a-da0b-11e7-9982-17c61c8d7460.png)


- 练习：


```{r}
ggplot(aes(x=age,y=friend_count_mean),data = pf.fc_by_age) + 
  geom_line() 
```


![image](https://user-images.githubusercontent.com/18595935/33609432-713a25a6-da0b-11e7-9324-6f31f44f8671.png)



# 10. 练习: 将摘要与原始数据叠加

将多个图叠加到一起了：

```{r}
ggplot(aes(x=age,y=friend_count),data=pf) + 
   coord_cartesian(xlim = c(13, 90)) + 
  geom_point(alpha = 0.05,
             position = position_jitter(h=0),
             color="orange") +
  coord_trans(y="sqrt") + 
  geom_line(stat = "summary",fun.y = mean) + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .1),
            linetype = 2,color = "red") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .5),
            color = "green") + 
  geom_line(stat = "summary",fun.y = quantile,fun.args = list(probs = .9),
            linetype = 2,color = "blue")
```


![image](https://user-images.githubusercontent.com/18595935/33610927-1d3cc206-da10-11e7-91b6-5045ef9f7822.png)


注意`coord_cartesian`函数也可以添加ylim的值范围。


# 12. 相关性

默认使用pearson相关：

```{r}
cor(pf$age,pf$friend_count)
```

结果为`-0.02740737`。

视频中使用的是另一种方式，先查看对应的帮助：

```{r}
?cor.test
```


```{r}
cor.test(x, ...)

## Default S3 method:
cor.test(x, y,
         alternative = c("two.sided", "less", "greater"),
         method = c("pearson", "kendall", "spearman"),
         exact = NULL, conf.level = 0.95, continuity = FALSE, ...)
```


```{r}
cor.test(pf$age,pf$friend_count,method="pearson")
```

或

```{r}
with(pf,cor.test(age,friend_count,method="pearson"))
```

得到相同的结果：

```{r}
-0.02740737 
```


# 13. 子集相关性

观察上面的图形，年龄与好友数量的关系并不是线性的，在70岁之后呈现上涨趋势，可能是错误数据，如果要计算70岁以下数据集的相关性，


```{r}
with(subset(pf,pf$age <= 70),cor.test(age,friend_count,method="pearson"))
```

得到相同的结果：

```{r}
-0.1712144  
```

# 15. 创建散点图

```{r}
ggplot(aes(x=www_likes_received,y=likes_received),data = pf) + geom_point()
```

![image](https://user-images.githubusercontent.com/18595935/33612209-378b8a3a-da14-11e7-8f02-7453a05cc4c2.png)


# 16. 强相关

忽略了x和y轴上的前5%的数据。
相关系数在 X 或 Y 的线性转换下是不变的，并且当 X 和 Y 都被转换为 z 分数时，回归线的斜率就是相关系数。

```{r}
ggplot(aes(x=www_likes_received,y=likes_received),data = pf) +
  geom_point() + 
  xlim(0,quantile(pf$www_likes_received,0.95)) +
  ylim(0,quantile(pf$likes_received,0.95)) +
  geom_smooth(method="lm",color="red")
```


![image](https://user-images.githubusercontent.com/18595935/33666055-2c0b2080-dadc-11e7-8300-d772f257d62a.png)


```{r}
with(pf,
     cor.test(www_likes_received,likes_received,method="pearson"))
```

结果为` 0.9479902 `。

# 18. 相关系数的更多注意事项

- 先安装对应的包，并查看示例数据的帮助

```{r}
install.packages("alr3")
library(alr3)
```


```{r}
data(Mitchell)
?Mitchell
```


```{r}
ggplot(aes(x=Month,y=Temp),data = Mitchell) +
  geom_point() 
```


![image](https://user-images.githubusercontent.com/18595935/33667086-36c7408c-dadf-11e7-95eb-9b9208464b12.png)


# 19. 噪声散点图

查看月份与温度的相关度：

```{r}
with(Mitchell,
     cor.test(Month,Temp,method="pearson"))
```

# 20. 理解数据

```{r}
ggplot(aes(x=Month,y=Temp),data = Mitchell) +
  geom_point() + scale_x_continuous(breaks = seq(0,203,12))
```


![image](https://user-images.githubusercontent.com/18595935/33667196-9658c9d0-dadf-11e7-8a3e-802b2fb7b6e6.png)


# 21. 新的视角

将每一年的数据相互叠加，构建出一个清晰的常规正弦曲线图。你可以在代码中使用 R 的模数运算符 %% 来这样做。尝试运行以下代码！

```{r}
ggplot(aes(x=Month%%12,y=Temp),data = Mitchell) +
  geom_point() + scale_x_continuous(breaks = seq(0,203,12))
```

![image](https://user-images.githubusercontent.com/18595935/33715520-34b6df3e-db96-11e7-9378-20108deeda49.png)


# 22. 练习: 了解噪声：年龄到月龄

之前的图形中，只有age，现在讲月份考虑进去：

```{r}
pf$age_with_months <- pf$age + (1 - pf$dob_month / 12) 
head(pf$age_with_months)
```

# 23. 练习: 带有月均值的年龄

通过上面22的代码，已经给pf追加了新的属性`age_with_months`，pf的当前结构如下：

```{r}
names(pf)
```

[1] "userid"                "age"                   "dob_day"               "dob_year"              "dob_month"            
 [6] "gender"                "tenure"                "friend_count"          "friendships_initiated" "likes"                
[11] "likes_received"        "mobile_likes"          "mobile_likes_received" "www_likes"             "www_likes_received"   
[16] "age_with_months"   


- 练习：产生新的dataframe

```{r}
age_month_groups <- group_by(pf, age_with_months) 

pf.fc_by_age_months <- summarise(age_month_groups, 
    friend_count_mean = mean(friend_count), 
    friend_count_median = median(friend_count), 
    n = n()) 

pf.fc_by_age_months <- arrange(pf.fc_by_age_months, age_with_months) 

head(pf.fc_by_age_months)

```

![image](https://user-images.githubusercontent.com/18595935/33717039-cee365b4-db9b-11e7-956e-1ef015eb709f.png)



# 24. 练习: 条件均值中的噪声



```{r}
ggplot(aes(x=age_with_months,y=friend_count_mean),data=subset(pf.fc_by_age,age_with_months <= 70)) + 
  geom_line()
```


![image](https://user-images.githubusercontent.com/18595935/33717256-96b3bd82-db9c-11e7-9034-4ef14287f01d.png)


# 25. 平滑化条件均值

```{r}

p1 <- ggplot(aes(x=age,y=friend_count_mean),data=subset(pf.fc_by_age,age<71)) + 
  geom_line()+ geom_smooth()


p2 <- ggplot(aes(x=age_with_months,y=friend_count_mean),data=subset(pf.fc_by_age_months,age_with_months <= 71)) + 
  geom_line() + geom_smooth()

p3 <- ggplot(aes(x=round(age/5)*5,y=friend_count_mean),data=subset(pf.fc_by_age,age<71)) + 
  geom_line(stat = "summary",fun.y=mean)

library(gridExtra)

grid.arrange(p2,p1,p3,ncol=1)

```


![image](https://user-images.githubusercontent.com/18595935/33717877-e64f9ff8-db9e-11e7-87b4-a06260f472f2.png)

