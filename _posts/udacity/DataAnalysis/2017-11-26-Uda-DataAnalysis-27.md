---
layout: post
title: Uda-DataAnalysis-27--探索多个变量
date: 2017-12-9 03:00:01
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}


# 3. 练习: 第三个定性变量

观察男女的好友数：

```{r}
qplot(x = friend_count,data = subset(pf,!is.na(gender)),
 binwidth = 10) +
 scale_x_continuous(lim = c(0,1000),breaks = seq(0,1000,50)) +
 facet_wrap(~gender)
```

![image](https://user-images.githubusercontent.com/18595935/33793750-e89009de-dd00-11e7-944d-045f24982049.png)

发现女性的好友数，明显多于男性，有可能是因为女性用户的年龄分布，与男性用户的年龄分布不同导致，
下面观察男女用户的年龄分布：


```{r}
ggplot(aes(x = gender, y = age),
       data = subset(pf, !is.na(gender))) + geom_boxplot() +
  stat_summary(fun.y = mean,geom = "point",shape = 4)
```

![image](https://user-images.githubusercontent.com/18595935/33793763-338c5e88-dd01-11e7-9e6e-fd581aae0321.png)


女性用户的年龄层，比男性用户更大。

- `观察各个年龄层上，男女用户的好友数量`，取的是好友数目的中位数：


```{r}
ggplot(aes(x=age,y=friend_count),
       data = subset(pf,!is.na(gender))) + 
    geom_line(aes(color=gender),stat="summary",fun.y=median)
```


![image](https://user-images.githubusercontent.com/18595935/33793773-583d3b9e-dd01-11e7-9a9b-fbe3084b4b2f.png)

- 根据年龄和性别同时分组：

```{r}
library("dplyr")
age_gender_groups <- group_by(subset(pf,!is.na(gender)), age, gender) 
pf.fc_by_age_gender <- summarise(age_gender_groups,
                          mean_friend_count = mean(friend_count),
                          median_friend_count = median(friend_count),
                          n = n())

head(pf.fc_by_age_gender,100)
```

![image](https://user-images.githubusercontent.com/18595935/33793833-baddb16a-dd02-11e7-806a-cc9ac53997a8.png)



# 4. 练习: 绘制条件小结

要得到的图形，与上面的类似，都是通过年龄和gender分组，得到好友的分布图：
但是这个利用了上面的分组数据集，实现方式不同：

```{r}
ggplot(aes(x=age,y=median_friend_count),data=pf.fc_by_age_gender) + 
  geom_line(aes(color=gender))
```


![image](https://user-images.githubusercontent.com/18595935/33793858-26c33f08-dd03-11e7-8c99-71c598891447.png)

# 6. 宽格式和长格式

观察上面生成的数据集`pf.fc_by_age_gender`，在继续后续的分析之前，还要对数据进行重组，将数据从长格式转换为宽格式：

![image](https://user-images.githubusercontent.com/18595935/33793952-09429bde-dd05-11e7-917e-60345f445bd6.png)

- 使用`tidyr`包重组数据：

```{r}
#install.packages("tidyr")
library(tidyr)
spread(subset(pf.fc_by_age_gender, select = c('gender', 'age', 'median_friend_count')), gender, median_friend_count)
```

重组后数据结构如下：

![image](https://user-images.githubusercontent.com/18595935/33793960-508ed714-dd05-11e7-841f-68cc5a5ad604.png)


# 7. 重塑数据

视频的示例使用的是另一个包`reshape2`进行数据重组：

```{r}

#install.packages("reshape2")
library(reshape2)

pf.fc_by_age_gender.wide <- dcast(pf.fc_by_age_gender,
                                  age ~ gender,
                                  value.var = "median_friend_count")

head(pf.fc_by_age_gender.wide,100)
```


![image](https://user-images.githubusercontent.com/18595935/33793999-13fa50c0-dd06-11e7-9c32-2b2e9ddc0aee.png)

可以得到与上面相同的数据集。


# 8. 练习：比率图

Plot the ratio of the female to male median friend counts using the data frame pf.fc_by_age_gender.wide.

Think about what geom you should use. Add a horizontal line to the plot with a y intercept of 1, which will be the base line. Look up the documentation for geom_hline to do that. Use the parameter linetype in geom_hline to make the line dashed.


```{r}
ggplot(aes(x=age,y=female/male),data=pf.fc_by_age_gender.wide) + geom_hline(yintercept = 1,linetype=2,alpha = 0.3) +
  geom_line(aes(color=age))
```

![image](https://user-images.githubusercontent.com/18595935/33794145-0e50a752-dd09-11e7-827f-f7049947c7c8.png)



# 9. 练习: 第三个定量变量

通过使用的天数，计算加入Facebook的年份

```{r}
pf$year_joined <- 2014 - ceiling(pf$tenure / 365)
```


# 10. 练习: 切割一个变量

上面得到了用户的加入年份数据，数据概要如下：

```{r}
summary(pf$year_joined)
```

输出如下：

![image](https://user-images.githubusercontent.com/18595935/33805418-e0569fc0-ddfb-11e7-840d-4ac6870370ac.png)

汇总数据输出：

```{r}
table(pf$year_joined)
```

![image](https://user-images.githubusercontent.com/18595935/33805421-f0a3879e-ddfb-11e7-8cc1-5470d20ed53d.png)


- 练习：需要将上述数据，按照 `(2004, 2009]` /  `(2009, 2011]` /  `(2011, 2012]` /  `(2012, 2014]`进行分割汇总：

```{r}
pf$year_joined.bucket <- cut(pf$year_joined,breaks = c(2004,2009,2011,2012,2014))
table(pf$year_joined.bucket)
```

![image](https://user-images.githubusercontent.com/18595935/33805530-d253281a-ddfd-11e7-9439-03f953b229f8.png)



- 注意`$`与`.`的差别：

```{r}
pf.test1.test12 <- "test1.test12"  # 当前内存中创建一个变量`pf.test1.test2`
pf$test1 <- "test1" # pf数据框中，创建一个字段`test1`
pf$test1.test12 <- "test1.test12" # pf数据框中，创建一个字段`test1.test12`
```


![image](https://user-images.githubusercontent.com/18595935/33800770-b43bcdc8-dd8a-11e7-86ea-5b41dae8ed00.png)


关于cut函数的使用，可以`?cut`查看帮助。

# 11. 练习: 绘制在一起

类似于上面的`4. 练习`，这里根据加入facebook的时间段，分段描述age与好友数的更关系：


```{r}
ggplot(aes(x = age, y = friend_count), 
              data = subset(pf, !is.na(year_joined.bucket))) + 
#  geom_line(aes(color = gender), stat = 'summary', fun.y = median) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = median)

```


![image](https://user-images.githubusercontent.com/18595935/33800786-1c09d81e-dd8b-11e7-9a74-53b115e9653b.png)

# 12. 练习: 绘制总均值

根据加入年份，绘制age与平均好友数的分组图，另外叠加一个总体的平均好友数线。

```{r}
ggplot(aes(x = age, y = friend_count), 
              data = subset(pf, !is.na(year_joined.bucket))) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) + 
  geom_line(stat="summary",fun.y=mean,linetype=2)
```

![image](https://user-images.githubusercontent.com/18595935/33800969-e4d35ea6-dd8f-11e7-86fe-e22ae7ac915a.png)

# 13. 练习: 好友率

求好友数与加入facebook天数的比率：

- 我自己的方式，很繁琐，还创建了一个新的数据集，浪费内存：

```{r}
tenureover0 <- subset(pf,pf$tenure>0)
tenureover0$tenure_count <- tenureover0$friend_count / tenureover0$tenure
summary(tenureover0$tenure_count)
```

- 视频中的方式：

```{r}
with(subset(pf,tenure >=1),summary(friend_count / tenure))
```

最终结构都是相同的：

![image](https://user-images.githubusercontent.com/18595935/33805434-4516b652-ddfc-11e7-8197-43acdd8bc363.png)


# 14. 练习: 申请好友数

- x轴是加入facebook的天数，y是平均每天加入的好友数目

```{r}
ggplot(aes(x = tenure, y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) 
```

通过下图发现随着使用时间的增加，新增好友数目会急剧减少。

![image](https://user-images.githubusercontent.com/18595935/33801083-a41e855e-dd92-11e7-8667-ca68df1192c0.png)


# 15. 练习: 偏差方差折衷

上面的图形中有很多噪音，通过下面的方式可以手动去除噪音：


```{r}
p0 <- ggplot(aes(x = tenure, y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) 

p1 <- ggplot(aes(x = 7*round(tenure/7), y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) 

p2 <- ggplot(aes(x = 30*round(tenure/30), y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) 

p3 <- ggplot(aes(x = 90*round(tenure/90), y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) 

library(gridExtra)

grid.arrange(p0,p1,p2,p3,ncol=1)
```

![image](https://user-images.githubusercontent.com/18595935/33801127-464642c6-dd94-11e7-8c1c-fa908589f2d3.png)


或是叠加一个平滑线：


```{r}
ggplot(aes(x = tenure, y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = mean) +
  geom_smooth(method="auto",color="red")
```

![image](https://user-images.githubusercontent.com/18595935/33801132-6048e6ce-dd94-11e7-890b-af330f1cdf3f.png)

- 视频中的方式，使用`geom_smooth`函数：

```{r}
ggplot(aes(x = tenure, y = friendships_initiated / tenure), 
              data = subset(pf, tenure >= 1)) + 
  geom_smooth(aes(color = year_joined.bucket))
```

![image](https://user-images.githubusercontent.com/18595935/33801134-7c3bde68-dd94-11e7-9169-c62fc743e79e.png)


# 17. 酸奶数据集简介


```{r}
yo <- read.csv("yogurt.csv")
str(yo)
```

![image](https://user-images.githubusercontent.com/18595935/33805445-8a316aa2-ddfc-11e7-8f7a-eedc9ceb2178.png)



- 将id转换为factor：

```{r}
yo$id <- factor(yo$id)
str(yo)
```

![image](https://user-images.githubusercontent.com/18595935/33805442-70fc89f4-ddfc-11e7-8e07-8b15ac2c58bf.png)


# 18. 练习: 重访直方图

- 构建一个价格的直方图：

```{r}
p1 <- ggplot(aes(x = price), data = yo) + geom_histogram(binwidth = 1)
p2 <- ggplot(aes(x = price), data = yo) + geom_histogram(binwidth = 10)

library(gridExtra)
grid.arrange(p1,p2,ncol=1)
```

![image](https://user-images.githubusercontent.com/18595935/33804695-a4cbed24-dded-11e7-80e6-1280117d779d.png)

上面的图中，可以看出价格的设置是有一定规律的，差不多以10为单位，所以下面的图将binwidth设置为10，可以看到其对比。

# 19. 练习: 购买数量

- 继续探索数据-汇总数据

```{r}
summary(yo)
```

![image](https://user-images.githubusercontent.com/18595935/33804718-40bd9b38-ddee-11e7-8a8b-2fb2b697f41c.png)

上面的price的第三个四分位与最大值是相同的。


- 查看价格的种类

```{r}
unique(yo$price)
length(unique(yo$price))
```

输出分别为：

![image](https://user-images.githubusercontent.com/18595935/33804735-da1568f6-ddee-11e7-8a23-1b861e39f667.png)


- 将数据集按照price汇总：

```{r}
table(yo$price)
```

![image](https://user-images.githubusercontent.com/18595935/33804737-f13362b8-ddee-11e7-8eac-79a32de912d5.png)

- 练习：

一条数据中，客户可能购买了多种口味的酸奶，现在需要将各种口味的酸奶汇总成一个新的变量：

使用`transform()`变形函数：

```{r}
yo <- transform(yo,all.purchases=(strawberry + blueberry + pina.colada + plain + mixed.berry))
head(yo,20)
```

两种方式都可以：

```{r}
yo$all.purchases + yo$strawberry + yo$blueberry + yo$pina.colada + yo$plain + yo$mixed.berry

head(yo,20)
```

![image](https://user-images.githubusercontent.com/18595935/33804864-2c663f5c-ddf1-11e7-9187-d00baafa43eb.png)

# 20. 练习: 随时间变化的价格

- 随时间变化的价格图：

```{r}
ggplot(aes(x=time,y=price),data=yo) + geom_jitter(alpha=0.25,shape=21,fill=I("#F79420"))
```

![image](https://user-images.githubusercontent.com/18595935/33804953-5ab63860-ddf3-11e7-82c3-df40dbfa596a.png)

上图可以看出，价格在一段时间内是一定的，另外偶尔有一些不同的价格出现，可能是商家促销，或是用户用了打折券。

# 22. 练习: 查看家庭样本

- 首先创建随机数种子，随机选取16个家庭，注意语法 `%in%`

```{r}
set.seed(4230)
sample.ids <- sample(levels(yo$id),16)

ggplot(aes(x=time,y=price),
       data=subset(yo,id %in% sample.ids)) + 
       facet_wrap(~id) +
       geom_line() + 
       geom_point(aes(size=all.purchases),pch=1)
```

![image](https://user-images.githubusercontent.com/18595935/33805030-f15708f2-ddf4-11e7-8ab3-4da98a8c967d.png)

# 23. 截面数据的限制

比较一下facebook数据集，facebook数据集只是某个时间点时，其好友数等信息。而酸奶数据集，有某个家庭在一段时间内的购买记录，更适合进行纵向分析。


# 25. 练习: 散点图矩阵

- 创建变量与变量之间的散点图，最终形成一个散点图矩阵

```{r}
#install.packages("GGally")
library(GGally)
theme_set(theme_minimal(20))

set.seed(1836)
pf_subset <- pf[,c(2:5)]
names(pf_subset)
ggpairs(pf_subset[sample.int(nrow(pf_subset),1000),])
```

![image](https://user-images.githubusercontent.com/18595935/33805212-5c55553e-ddf8-11e7-9a2c-7f7fc0f4b854.png)


# 26. 更多变量

导入另一个数据集，基因数据集：

```{r}
nci <- read.table("nci.tsv")
colnames(nci) <- c(1:64)
head(nci)
```

# 27. 热图

```{r}
library(reshape2)

nci.long.samp <- melt(as.matrix(nci[1:200,]))

names(nci.long.samp) <- c("gene","case","value")
#head(nci.long.samp)

ggplot(aes(y=gene,x=case,fill=value),
       data=nci.long.samp) +
  geom_tile() +
  scale_fill_gradientn(colors=colorRampPalette(c("blue","red"))(100))
```


![image](https://user-images.githubusercontent.com/18595935/33805352-c0fb8934-ddfa-11e7-8398-37423f152e0d.png)

# 28. 【总结】练习: 分析三个或更多变量

本节中学习了：

1. 使用前几课的技巧并进行了扩展，以便一次调查多个变量的模式。
2. 从散点图的扩展开始，为多个组添加汇总。
3. 采用一些技术来一次检查大量的变量，例如散点图和热图。
4. 重塑了数据，将每种情况一行的长数据，组合为一行的宽数据(list.7)