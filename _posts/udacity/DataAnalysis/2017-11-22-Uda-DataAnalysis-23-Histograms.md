---
layout: post
title: Uda-DataAnalysis-23-【扩展】如何读懂直方图并在 R 中进行使用
date: 2017-11-22 02:00:03
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}


翻译 [How to Read and Use Histograms in R](http://flowingdata.com/2014/02/27/how-to-read-histograms-and-use-them-in-r/)

# 1. 直方图不是柱状图

大多数人都有一个误区，会混淆直方图和柱状图，确实从形状上来说，两者非常类似，但是从表现意义上差异很大。
最主要的差异参考下图:
1. 柱状图的X轴表示种类数据，或是时间序列数据，然而直方图的X轴表示连续的变量。
2. 柱状图中，用柱子的高度表示value，而直方图用面积表示value。
3. 柱状图表示各个种类中明确的值的对比，比如不同国籍人口数量的对比；而直方图表示不同变量中值的分布。

![image](https://user-images.githubusercontent.com/18595935/33163865-c67a344e-d073-11e7-8bd2-c041358540d4.png)

所以两种类型的图是表示不同的目的，后者即直方图表示的是单一变量的分布状况，如果是标准正态分布，如不同年龄段的人口分布，可能是两边底，中间高的形状，根据不同的数据集表现不同。

最后，因为直方图使用面积而不是高度表示，所以柱子的宽度是可变化的。


# 2. 柱状图

选取一组NBA球员的身高作为例子：

```python

> list.files()
[1] "lesson3_student.nb.html" "lesson3_student.rmd"     "NBA-Census.csv"          "pseudo_facebook.tsv"    

> nba <- read.csv("NBA-Census.csv",stringsAsFactors=FALSE)

> names(nba)
 [1] "Name"                               "Age"                               
 [3] "Team"                               "POS"                               
 [5] "X."                                 "X2013.."                           
 [7] "Ht"                          		  "WT"                                
 [9] "EXP"                                "X1st.Year"                         
[11] "DOB"                                "School"                            
[13] "City"                               "State..Province..Territory..Etc..."
[15] "Country"                            "Race"                              
[17] "HS.Only"                           

> warriors <- subset(players, Team=="Warriors")

> warriors.o <- warriors[order(warriors$Ht),]

> par(mar=c(5,10,5,5))

# 因为barplot中必选参数 height必须是数值型，所以要讲char转换到numeric
> myht <- as.numeric(as.character(warriors.o$Ht))
> barplot(myht, names.arg=warriors.o$Name, horiz=TRUE, border=NA, las=1, main="Heights of Golden State Warriors")
```

下面就是一个典型的柱状图，更多关于barplot函数的解释，参考 http://data-science.gr.jp/implementation/ida_r_barplot.html

![image](https://user-images.githubusercontent.com/18595935/33163896-df51db0c-d073-11e7-8be7-62cf4a5d60a7.png)


# 3. 直方图

```python
> par(mfrow=c(1,3), mar=c(3,3,3,3))
> hist(myht, main="NBA Player Heights", xlab="inches", breaks=seq(65, 90, 1))
> hist(myht, main="NBA Player Heights", xlab="inches", breaks=seq(65, 90, 2))
> hist(myht, main="NBA Player Heights", xlab="inches", breaks=seq(65, 90, 5))
```

用三种不同的表现形式来表现一个数据：

![image](https://user-images.githubusercontent.com/18595935/33163953-1af9dcea-d074-11e7-88a2-a1110f71b7ad.png)


直方图的X轴上的标度可以是不同宽度

```python
> hist(myht, main="NBA Player Heights", xlab="inches", breaks=c(seq(65, 75, 2), 80, 90))
> hist(myht, main="NBA Player Heights", xlab="inches", breaks=c(65, 75, seq(80, 90, 2)))
> hist(myht, main="NBA Player Heights", xlab="inches", breaks=c(65, seq(70, 80, 1), 90))
```

![image](https://user-images.githubusercontent.com/18595935/33164174-0f478af4-d075-11e7-8b8a-c76c3ea36cff.png)


