---
layout: post
title: Uda-DataAnalysis-22--R基础
date: 2017-10-21 02:00:03
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 8. R的安装与布局

首先，访问 http://cran.rstudio.com，下载并安装 R 编程语言。安装完成 R 后，从 http://www.rstudio.com 下载并安装 RStudio。

布局如下：

① 打开R Script / R notebook 等文件

② 命令行模式运行R命令

③ 显示当前空间的变量对象

④ 显示图形，或是notebook的viewer等。

![image](https://user-images.githubusercontent.com/18595935/31893251-0a6c1c6c-b846-11e7-8855-96c3f0cc7c36.png)

# 9. 揭秘R

建议所有 R 和 RStudio 的初学者尝试 Swirl（运用交互式 R 学习的统计学）。Swirl 是针对 R 统计编程语言的软件包，目的在于以交互方式教授统计学和 R 命令。控制台中输入如下命令:

```python
install.packages("swirl") 
library(swirl) 
swirl()
```

## 9.1 使用swirl()

## 9.2 运行`demystifying.R`

自带的一个示例程序，通过这个示例程序能大致了解R语言。

- 创建一个向量vector，vector是R中的一种数据类型，vector中的元素数据类型必须相同。

```python
udacious <- c("Chris Saden", "Lauren Castellano",
              "Sarah Spikes","Dean Eckles",
              "Andy Brown", "Moira Burke",
              "Kunal Chawla")
```

- 类似的，也可以创建number数值类型的vector

```python
> numbers <- c(1:10)
> numbers
 [1]  1  2  3  4  5  6  7  8  9 10
> 
> numbers <- c(numbers, 11:20)
> numbers
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
```

- 下面用`=`赋值，为什么？是两者都可以使用么？

```python
 > udacious <- c("Chris Saden", "Lauren Castellano",
+               "Sarah Spikes","Dean Eckles",
+               "Andy Brown", "Moira Burke",
+               "Kunal Chawla", "lijun")
> mystery = nchar(udacious)
> mystery
[1] 11 17 12 11 10 11 12  5
```

- 用`==`比较vector中的每个元素

```python
> mystery
[1] 11 17 12 11 10 11 12  5
> mystery == 11
[1]  TRUE FALSE FALSE  TRUE FALSE  TRUE FALSE FALSE
```

- 通过这种方式取出了所有长度为11的元素

```python
> udacious[mystery == 11]
[1] "Chris Saden" "Dean Eckles" "Moira Burke"
```

- 加载数据集`mtcars`

```python
data(mtcars)
```

- 取得数据集的名称 `names()`

```python
> names(mtcars)
 [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear" "carb"
```

-  获得帮助`?mtcars`，将在上图的第四部分显示帮助信息

-  打印数据集合概要信息`str()`

```python
> str(mtcars)
'data.frame':   32 obs. of  11 variables:
 $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
 $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
 $ disp: num  160 160 108 258 360 ...
 $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
 $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
 $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
 $ qsec: num  16.5 17 18.6 19.4 17 ...
 $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
 $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
 $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
 $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
```

- 获取数据集维度信息 `dim()`

```python
> dim(mtcars)
[1] 32 11
```

- 获取数据集的行的名称 `row.names()`,要取得帮助信息`？row.names()`

```python
> row.names(mtcars)
 [1] "Mazda RX4"           "Mazda RX4 Wag"       "Datsun 710"          "Hornet 4 Drive"     
 [5] "Hornet Sportabout"   "Valiant"             "Duster 360"          "Merc 240D"          
 [9] "Merc 230"            "Merc 280"            "Merc 280C"           "Merc 450SE"         
[13] "Merc 450SL"          "Merc 450SLC"         "Cadillac Fleetwood"  "Lincoln Continental"
[17] "Chrysler Imperial"   "Fiat 128"            "Honda Civic"         "Toyota Corolla"     
[21] "Toyota Corona"       "Dodge Challenger"    "AMC Javelin"         "Camaro Z28"         
[25] "Pontiac Firebird"    "Fiat X1-9"           "Porsche 914-2"       "Lotus Europa"       
[29] "Ford Pantera L"      "Ferrari Dino"        "Maserati Bora"       "Volvo 142E"

# 赋予新的行名称
> row.names(mtcars) <- c(1:32)
>     
```

- 查看数据集的若干条`head(mtcars,10)`，`tail(mtcars,3)`,默认是6条

- `mtcars$mpg` 取得数据集的指定行

- `mean(mtcars$mpg)`，指定行的平均值


# 11. 阅读并将数据子集化

```python
# 获取当前目录，设定当前目录
getwd()
setwd("C:/Users/utane/OneDrive/udacity/22-R basic")

# 读取数据集
statesInfo <- read.csv("stateData.csv")
str(statesInfo)

# 数据集的前6条数据
head(statesInfo)

# 方法1：获取数据集子集
subset(statesInfo,state.region == 1)

# 方法2：获取数据集子集
statesInfo[statesInfo$state.region == 1, ]
```



# 12. 练习: R Markdown 文档

使用` demystifyingR2.Rmd `练习。

## 12.1 获取数据集的概要`str()`和`summary()`

## 12.2 获取满足某个条件的额数据子集 `efficient <- subset(mtcars,mpg >= 23)`

## 12.3 更多复合条件查询数据子集

```python
subset(mtcars, mpg > 30 & hp > 100)

subset(mtcars, mpg < 14 | disp > 390)

```


## 12.4 给数据集新增一列

```python
mtcars$year <- 1974
```

## 12.5 删除数据集中指定的列

```python
mtcars <- subset(mtcars, select = -year)
```

## 12.6 通过vector给指定列赋值

给各个行的year列，依次赋值1974,1975,1976,1977，依次循环。

```python
mtcars$year <- c(1974, 1975,1976,1977)
```

