---
layout: post
title: Uda-DataAnalysis-23--探索单一变量
date: 2017-11-22 02:00:03
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 3. 伪Facebook用户数据

```python
> getwd()
[1] "C:/Users/utane/Documents"
> setwd("C:/Users/utane/OneDrive/udacity/23-R")
> getwd()
[1] "C:/Users/utane/OneDrive/udacity/23-R"

# 列出当前目录下的文件名
> list.files()
[1] "lesson3_student.nb.html" "lesson3_student.rmd"     "pseudo_facebook.tsv"   

# 导入数据后，显示有99003行数据，15个变量 
> pf <- read.csv("pseudo_facebook.tsv",sep='\t')

# 该数据集中的变量名
> names(pf)
 [1] "userid"                "age"                   "dob_day"               "dob_year"             
 [5] "dob_month"             "gender"                "tenure"                "friend_count"         
 [9] "friendships_initiated" "likes"                 "likes_received"        "mobile_likes"         
[13] "mobile_likes_received" "www_likes"             "www_likes_received"   
```

# 4. 练习:用户生日直方图

更多关于直方图的参考 [如何读懂直方图并在 R 中进行使用]()

```python

# 安装并加载图形库
install.packages('ggplot2')
library(ggplot2)

ggplot(aes(x = dob_day), data = pf) + 
  geom_histogram(binwidth = 1) + 
  scale_x_continuous(breaks = 1:31)

```

显示图形如下:

![image](https://user-images.githubusercontent.com/18595935/33155957-5a268c60-d038-11e7-9e5f-df0eeed193f9.png)



# 8. 练习:分面

通过下面的代码，可以实现通过月份分面：

```python
ggplot(aes(x = dob_day), data = pf) + 
   geom_histogram(binwidth = 1) + 
   scale_x_continuous(breaks = 1:31) + facet_wrap(~dob_month,ncol = 3)
```

![image](https://user-images.githubusercontent.com/18595935/33165869-b49e24b2-d07b-11e7-97ea-3e7c2242b081.png)

`facet_wrap`和`facet_grid`用于切面

![image](https://user-images.githubusercontent.com/18595935/33166124-7cd425ee-d07c-11e7-80eb-616f0a664fff.png)


关于Facets更多介绍，可以参考[Facets (ggplot2)](http://www.cookbook-r.com/Graphs/Facets_(ggplot2)/)

# 11. 练习:好友数量

```python
> pf <- read.csv("pseudo_facebook.tsv",sep='\t')
> names(pf)
 [1] "userid"                "age"                   "dob_day"               "dob_year"             
 [5] "dob_month"             "gender"                "tenure"                "friend_count"         
 [9] "friendships_initiated" "likes"                 "likes_received"        "mobile_likes"         
[13] "mobile_likes_received" "www_likes"             "www_likes_received"   
> ggplot(aes(x = friend_count), data = pf) + 
+   geom_histogram(binwidth = 1)
```

![image](https://user-images.githubusercontent.com/18595935/33166758-b56b8594-d07e-11e7-851e-c0fb43108a90.png)

这种数据叫做long tail data,长尾数据，即有某个非常大的值，我们要研究的是大部分1000人以下好友的用户，所以要对其进行限制。

# 12. 限制轴

上面出现了一个5000的值，导致1000以下的图形看不清楚，需要对X轴的值进行限制：

```python
> ggplot(aes(x = friend_count), data = pf) + 
+   geom_histogram() + 
+   scale_x_continuous(limits = c(0, 1000))
```

![image](https://user-images.githubusercontent.com/18595935/33166982-6ef70ff6-d07f-11e7-9dd7-12211f11a283.png)

# 14. 调整组距

上面的图形以125为组距，不是很容易看清差异，通过调整组距能更好反应数据变化。

```python

# 添加组距，即0到1000，以50为步长
> ggplot(aes(x = friend_count), data = pf) + 
+    geom_histogram() + 
+    scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50))

# 以性别gender进行分面
> ggplot(aes(x = friend_count), data = pf) + 
+    geom_histogram() + 
+    scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +  facet_wrap(~gender)
```

图形分别如下所示:

![image](https://user-images.githubusercontent.com/18595935/33175425-1d57934e-d09f-11e7-9491-ed9202ff915f.png)

![image](https://user-images.githubusercontent.com/18595935/33175438-29ef49d0-d09f-11e7-8ef3-3a6a71676b92.png)


# 15. 忽略NA观测值

观察上面gender进行分面后，最后一组是无效值组，需要将该组过滤掉。
即将data变量进行过滤，如下:

```python
> ggplot(aes(x = friend_count), data = subset(pf, !is.na(gender))) + 
+    geom_histogram() + 
+    scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +  facet_wrap(~gender)
```

![image](https://user-images.githubusercontent.com/18595935/33175600-9ad232de-d09f-11e7-8830-6e6b2daa785f.png)


# 16. 按性别划分的统计学(by())

通过by函数获得统计值，by函数接收三个参数
- 变量
- 类别变量，用于划分子集的指标列表
- 函数

```python
> table(pf$gender)
female   male 
 40254  58574 

> by(pf$friend_count,pf$gender,summary)
pf$gender: female
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      0      37      96     242     244    4923 
----------------------------------------------------------------------------------- 
pf$gender: male
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      0      27      74     165     182    4917 
> 

```


# 17. 使用时长

用户使用时长的直方图，第一个图的单位是天，后面是年，注意binwidth的区别，是以x轴上的为基准。


```python

>  ggplot(aes(x = tenure), data = pf) + 
+    geom_histogram(binwidth = 30, color = 'black', fill = '#099DD9')

> ggplot(aes(x = tenure/365), data = pf) + 
+     geom_histogram(binwidth = .25, color = 'black', fill = '#F79420')

```

![image](https://user-images.githubusercontent.com/18595935/33177479-0bce9224-d0a6-11e7-9b72-7a892d8e0c08.png)

![image](https://user-images.githubusercontent.com/18595935/33177498-1a076adc-d0a6-11e7-841b-af2f21696e99.png)

还可以给X轴限定范围和步长：

```python
> ggplot(aes(x = tenure/365), data = pf) + 
+     geom_histogram(binwidth = .25, color = 'black', fill = '#F79420') + 
+ scale_x_continuous(breaks = seq(1,7,1),limits=c(0,7))
```

![image](https://user-images.githubusercontent.com/18595935/33177599-8ae08536-d0a6-11e7-997d-f9e2e66f1788.png)


# 19. 练习：用户年龄

组距: binwidth / 间断：break / 标签:label

```python
> ggplot(aes(x = age),data = pf) +  geom_histogram(binwidth = 1, color = 'black', fill = '#F79420') +
  scale_x_continuous(breaks = seq(1,150,5),limits=c(0,150))
```

![image](https://user-images.githubusercontent.com/18595935/33178096-3dcf61b6-d0a8-11e7-941a-7760d48b7fed.png)

注意上面binwidth为1，即每个bar的宽度为1，而breaks是X轴上数字的标度，以1到150岁之间，5岁为一个标度。

# 22. 转换数据


```python
> setwd("C:/Users/utane/OneDrive/udacity/23-R")
> pf <- read.csv("pseudo_facebook.tsv",sep='\t')
> names(pf)
 [1] "userid"                "age"                   "dob_day"              
 [4] "dob_year"              "dob_month"             "gender"               
 [7] "tenure"                "friend_count"          "friendships_initiated"
[10] "likes"                 "likes_received"        "mobile_likes"         
[13] "mobile_likes_received" "www_likes"             "www_likes_received"   


> 
> library(ggplot2)
> qplot(x=friend_count,data=pf)
> 
```

创建包含以下三个直方图的 1 个列： • 好友数 • 使用 log10 转化的好友数 • 使用 sqrt 转化的好友数 
在一个图中创建所有三个直方图之前，你需要运行以下代码安装： 

```python
install.packages('gridExtra') 
library(gridExtra) 
```

```python
> summary(pf$friend_count)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    0.0    31.0    82.0   196.4   206.0  4923.0 
> summary(log10(pf$friend_count))
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   -Inf   1.491   1.914    -Inf   2.314   3.692 
> summary(log10(pf$friend_count+1))
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  0.000   1.505   1.919   1.868   2.316   3.692 
> summary(sqrt(pf$friend_count))
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  0.000   5.568   9.055  11.088  14.353  70.164 
> library(gridExtra) 
> 
> q1 = qplot(x=friend_count,data=pf)
> q2 = qplot(x=log10(pf$friend_count+1),data=pf)
> q3 = qplot(x=sqrt(pf$friend_count),data=pf)
> 
> grid.arrange(q1, q2, q3,ncol=1)
```


- 另一种方式也可以画出相同的图形：

```python
> p1 <- ggplot(aes(x = friend_count),data=pf) + geom_histogram()
> p2 <- p1 + scale_x_log10()
> p3 <- p1 + scale_x_sqrt()

> grid.arrange(p1, p2, p3,ncol=1)
```

图形如下：

![image](https://user-images.githubusercontent.com/18595935/33227062-a3bf6584-d1de-11e7-86d1-0734ea21cc8b.png)

# 23. 添加定标层

```python
> logScale <- qplot(x = log10(friend_count),data = pf)
> countScale <- ggplot(aes(x=friend_count),data = pf) + 
+ geom_histogram() + scale_x_log10()

> library(ggplot2)
> library(gridExtra) 

> grid.arrange(logScale,countScale,ncol = 2)

```

![image](https://user-images.githubusercontent.com/18595935/33228379-400c6284-d1fd-11e7-86b3-1c8dde81ce10.png)


# 24. 频率多边形

```python
> qplot(x = friend_count,data = subset(pf,!is.na(gender)),
+ binwidth = 10) +
+ scale_x_continuous(lim = c(0,1000),breaks = seq(0,1000,50)) +
+ facet_wrap(~gender)
```

![image](https://user-images.githubusercontent.com/18595935/33228556-8a0533c6-d201-11e7-9248-256d45e5038b.png)


```{r}
qplot(x = friend_count,data = subset(pf,!is.na(gender)),
binwidth = 10,geom = "freqpoly",color = gender) +
scale_x_continuous(lim = c(0,1000),breaks = seq(0,1000,50))
```

![image](https://user-images.githubusercontent.com/18595935/33228597-7c94127e-d202-11e7-97ec-4551b89d9701.png)

- 使用频数多边形确定哪个性别在万维网 (www_likes) 上获得的点赞数量更多

```{r}
qplot(x = www_likes,data = subset(pf,!is.na(gender)),
      geom = "freqpoly",color=gender) + 
      scale_x_continuous() + 
      scale_x_log10()
```

![image](https://user-images.githubusercontent.com/18595935/33228713-01db09e0-d205-11e7-8f36-88498ecbddb9.png)


# 25. 练习:网页端上的“点赞”数

```{r}
by(pf$www_likes,pf$gender,sum)
```


pf$gender: female
[1] 3507665

--------------------------------------------------------------------------------------- 

pf$gender: male
[1] 1430175


```{r}
by(pf$www_likes,pf$gender,summary)
```

pf$gender: female
    Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
    0.00     0.00     0.00    87.14    25.00 14865.00 

--------------------------------------------------------------------------------------- 

pf$gender: male
    Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
    0.00     0.00     0.00    24.42     2.00 12903.00 


# 26. 箱线图

- 方法1

```{r}
qplot(x=gender,y=friend_count,
      data = subset(pf,!is.na(gender)),
      geom = "boxplot") + 
scale_y_continuous(lim = c(0,1000),breaks = seq(0,1000,50))

```
![image](https://user-images.githubusercontent.com/18595935/33228849-48698538-d207-11e7-8495-4f53d6798a16.png)

- 方法2

```{r}
qplot(x=gender,y=friend_count,
      data = subset(pf,!is.na(gender)),
      geom = "boxplot",ylim = c(0,1000))
```

![image](https://user-images.githubusercontent.com/18595935/33228851-510595a6-d207-11e7-8469-5626953845af.png)

# 27. 练习:箱线图、四分位数和友谊

```{r}
qplot(x=gender,y=friend_count,
      data = subset(pf,!is.na(gender)),
      geom = "boxplot") +
  coord_cartesian(ylim = c(0,250))

by(pf$friend_count,pf$gender,summary)
```

![image](https://user-images.githubusercontent.com/18595935/33229573-7f2d390e-d214-11e7-8c89-0762514fc69b.png)


pf$gender: female
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      0      37      96     242     244    4923 

--------------------------------------------------------------------------------------- 

pf$gender: male
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      0      27      74     165     182    4917 

- 问题`谁发起了更多的交友请求，男士还是女士？`

```{r}
qplot(x=gender,y=friendships_initiated,
      data = subset(pf,!is.na(gender)),geom="boxplot") +
  coord_cartesian(ylim = c(0,150))

by(pf$friendships_initiated,pf$gender,summary)
```

![image](https://user-images.githubusercontent.com/18595935/33230406-2939e74c-d226-11e7-89ed-8ac75da89b10.png)

pf$gender: female
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    0.0    19.0    49.0   113.9   124.8  3654.0 

--------------------------------------------------------------------------------------- 

pf$gender: male
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    0.0    15.0    44.0   103.1   111.0  4144.0 



# 28. 练习:符合逻辑

```{r}
summary(pf$mobile_likes)

mobile_check_in <- NA
pf$mobile_check_in <- ifelse(pf$mobile_likes >0,1,0)
pf$mobile_check_in <- factor(pf$mobile_check_in)
summary(pf$mobile_check_in)

```

Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
0.0     0.0     4.0   106.1    46.0 25111.0 

  0     1 
35056 63947 



由于 mobile_check_in 是一个因子变量，因此 sum() 函数将无法运行。你可以使用 length() 函数来确定向量中的值数量。
可以创建 mobile_check_in 来保存布尔值。sum() 函数可处理布尔值（true 为 1，false 为 0）。

- 求用手机登录人数的百分比

```{r}
sum(pf$mobile_check_in == 1) / length(pf$mobile_check_in)
```

