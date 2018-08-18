---
layout: post
title: Uda-DataAnalysis-22-[扩展]-R语言实战(第二版)-07-基本统计分析
date: 2017-10-21 01:00:07
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}

# 第七章 基本统计分析

本章重点放在生成基本的描述统计量和推论统计量的R函数。

- 描述性统计分析（定量变量的位置和尺度的衡量方式）
- 频数表和列联表（与类别性变量相关）
- 相关系数和协方差(连续性变量和有序性变量相关)
- t检验(参数检验)
- 非参数统计 

# 1. 描述性统计分析

主要分析连续性变量的中心趋势/变化性/分布形状等，使用数据集mtcars进行示例。

```python
myvars <- c("mpg", "hp", "wt")  
head(mtcars[myvars])
```

【样例数据】

上面的变量的意义分别是 每加仑汽 油行驶英里数（mpg） 、马力（hp）和车重（wt）。

先查看不同车型的各种描述性变量，再按照变速箱类型（am）和汽缸数（cyl）来描述性统计量。
- 变速箱类型是一个以0表示自动挡、1表示手动挡来编码的二分变量。
- 汽缸数可为4、5或6。

## 1.1 方法集

- `summary()`计算描述性统计量

```python
summary(mtcars[myvars]) 
```


- `sapply()`函数计算描述性统计量

```python
sapply(x, FUN, options) 

- x为数据框
- FUN指函数，有mean(),sd(),var(),min(),max()等，后续的options作为参数传递给FUN函数。另外也可以是自己定义的函数。
```

如下是计算偏度(skew)和峰度(kurtosis)的自定义函数，以及该函数的使用

```python

mystats <- function(x, na.omit=FALSE){ 
	if (na.omit)  
		x <- x[!is.na(x)] 
		m <- mean(x) 
		n <- length(x) 
		s <- sd(x) 
		skew <- sum((x-m)^3/s^3)/n 
		kurt <- sum((x-m)^4/s^4)/n - 3 
		return(c(n=n, mean=m, stdev=s, skew=skew, kurtosis=kurt)) 
}

sapply(mtcars[myvars], mystats) 

# 忽略空值的使用方式
sapply(mtcars[myvars], mystats, na.omit=TRUE)
```


## 1.2 更多的方法

有许多其他包也提供描述统计量的计算，如Hmisc、pastecs和psych，需要时查询相关文档。


## 1.3 分组计算描述性统计量

- aggregate()函数可以用于分组获取描述性统计量。

```python
aggregate(mtcars[myvars], by=list(am=mtcars$am), mean) 
```

```python
aggregate(mtcars[myvars], by=list(am=mtcars$am), sd) 
```

如果有多个分组变量，可以 使用`by=list(name1=groupvar1, name2=groupvar2, ... , nameN=groupvarN)`这样的语句，其中name1，name2是分组的标签。

- by()返回若干个统计量

```python
by(data, INDICES, FUN) 
- NDICES是一个因子或因子组成的列表，定义了分组，FUN是任 意函数
```

```python
dstats <- function(x)sapply(x, mystats) 
myvars <- c("mpg", "hp", "wt") 

by(mtcars[myvars], mtcars$am, dstats) 

```

## 1.4 分组计算的扩展

`doBy`包和`psych`包也提供了分组计算描述性统计量的函数.


```python
summaryBy(formula, data=dataframe, FUN=function) 

- formula：var1 + var2 + ... + varN ~ groupvar1 +... + groupvarN
- ~左侧的变量是需要分析的数值型变量
- 右侧的变量是类别型的分组变 
```


```python
library(doBy)
summaryBy(mpg+hp+wt~am, data=mtcars, FUN=mystats) 
```

`psych`包中也有类似的函数，使用方法不同，需要使用时再查阅。

# 2. 频数表和列联表

着眼于类别型变量的频数表和列联表，以及相应的独立性检验、相关性的度量、图形化展示结果的方法。

先熟悉数据：

```python
library(vcd)
head(Arthritis)
```


数据均为类别型因子：
- 治疗情况（安慰剂治疗、用药治疗） 
- 性别（男性、女性）
- 改善情况（无改善、一定程度 的改善、显著改善）

## 2.1 生成频数表 


|函数|描述|
|:--|--:|
|table(var1, var2, ..., varN) |使用N个类别型变量（因子）创建一个N维列联表 |
|xtabs(formula, data) |根据一个公式和一个矩阵或数据框创建一个N维列联表 |
|prop.table(table, margins) |依margins定义的边际列表将表中条目表示为分数形式 |
|margin.table(table, margins) |依margins定义的边际列表计算表中条目的和 |
|addmargins(table, margins) |将概述边margins（默认是求和结果）放入表中 |
|ftable(table)|创建一个紧凑的“平铺”式列联表 |


- 一维连表

```python
mytable <- with(Arthritis, table(Improved)) 
mytable
```


```python
prop.table(mytable) 
```

- 二维联表

```python
mytable <- table(A, B) 
- A为行变量
- B为列变量
```


```python
mytable <- xtabs(~ A + B, data=mydata) 
- 要进行交叉分类的变量应出现在公式的右侧（即 ~符号的右方） ，以+作为分隔
```


```python
mytable <- xtabs(~ Treatment+Improved, data=Arthritis) 
mytable
```

```python
margin.table(mytable, 1) 
prop.table(mytable, 1) 
```

# 3. 相关

# 4. t检验


# 5. 组间差异的非参数检验

# 6. 组间差异

