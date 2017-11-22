---
layout: post
title: Uda-DataAnalysis-22--R基础
date: 2017-11-21 02:00:03
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

# 13/14. 因子变量/有序因子

查看并修改当前路径:

```python
> getwd()
[1] "C:/Users/utane/Documents"
> setwd("C:/Users/utane/OneDrive/udacity/22-R basic")
> getwd()
[1] "C:/Users/utane/OneDrive/udacity/22-R basic"

# 导入数据
> reddit <- read.csv("reddit.csv")
```

查看数据概要：

```python   
# 查看各个status中的记录数目
> table(reddit$employment.status)

                   Employed full time                             Freelance 
                                14814                                  1948 
Not employed and not looking for work    Not employed, but looking for work 
                                  682                                  2087 
                              Retired                               Student 
                                   85                                 12987 

> summary(reddit)
       id            gender          age.range                                      marital.status 
 Min.   :    1   Min.   :0.0000   18-24   :15802   Engaged                                 : 1109  
 1st Qu.: 8189   1st Qu.:0.0000   25-34   :11575   Forever Alone                           : 5850  
 Median :16380   Median :0.0000   Under 18: 2330   In a relationship                       : 9828  
 Mean   :16379   Mean   :0.1885   35-44   : 2257   Married/civil union/domestic partnership: 5490  
 3rd Qu.:24568   3rd Qu.:0.0000   45-54   :  502   Single                                  :10428  
 Max.   :32756   Max.   :1.0000   (Other) :  200   Widowed                                 :   44  
 ...
```


安装图形包，并显示图形:

```
> install.packages('ggplot2', dependencies = T) 
> library(ggplot2)
> levels(reddit$age.range)
[1] "18-24"       "25-34"       "35-44"       "45-54"       "55-64"       "65 or Above" "Under 18"   
> qplot(data = reddit,x=age.range)
```

显示图形如下:

![image](https://user-images.githubusercontent.com/18595935/33074756-aa9fbb32-cf0a-11e7-8c3b-638aa702d9d3.png)

`age.range` 是有序因子。

# 15. 设置有序因子的水平

观察上图，下面的年龄没有按顺序排列，理想情况应该是按照 "Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above" 进行排列。

下面例子会更加明显，X轴是按照字母顺序排序的：

```python
qplot(data = reddit,x=income.range)
```

![image](https://user-images.githubusercontent.com/18595935/33076147-3da3d680-cf0f-11e7-95d5-4bcfa367ce3b.png)


下面是排序后的图形：

```python

# 设置有序因子

age.orderd <- ordered(reddit$age, levels = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))

qplot(data = reddit,x=age.orderd)
```

![image](https://user-images.githubusercontent.com/18595935/33076283-ac1a689a-cf0f-11e7-8f30-e97db89fdf53.png)


# 15. 【扩展】 因子变量

> 本节来自 参考资料的 [学习如何设置和排列因子水平](https://stats.idre.ucla.edu/r/modules/factor-variables/).

## 15.1 生成一个因子变量（Creating factor variables）

因子变量是一类可以是数值型或是字符型的分类变量(categorical variables)，将分类变量转换为因子变量如下优点:
1. 便于统计处理
2. 便于图形展示
3. 将字符串变量作为因子变量存储的话，内存使用更高效

使用`factor`函数可以生成因子变量，输入参数(must)是一个存储了数值或是字符串的vector，输入参数(可选)有一个levels，存储的是该因子变量的种类。

```python
# 设置一个随机数种子，后续能生成相同的随机数
> set.seed(124)
> schtyp <- sample(0:1, 20, replace = TRUE)
> schtyp
 [1] 0 0 1 0 0 0 1 0 1 0 1 1 1 1 0 0 1 1 1 0
```

判断其类型，可以看到该变量只是普通的数值型：

```python
> is.factor(schtyp)
[1] FALSE
> is.numeric(schtyp)
[1] TRUE
```

下一步用这个vecotr创建一个因子变量，其Levels是`private/public`：

```python
> schtyp.f <- factor(schtyp, labels = c("private", "public"))
> schtyp.f
 [1] private private public  private private private public  private public  private public  public  public 
[14] public  private private public  public  public  private
Levels: private public
```

判断其类型：

```python
> is.factor(schtyp.f)
[1] TRUE
```

上面的factor函数中，有labels函数，即手动指定了level，如果不指定的话，原始vector中的值作为level，如下：

```python
> schtyp.nof <- factor(schtyp)
> schtyp.nof
 [1] 0 0 1 0 0 0 1 0 1 0 1 1 1 1 0 0 1 1 1 0
Levels: 0 1
```

**再看另一个例子：**，如果不指定levels的话，其顺序就是字母的排序：

```python
> ses <- c("low", "middle", "low", "low", "low", "low", "middle", "low", "middle",
+          "middle", "middle", "middle", "middle", "high", "high", "low", "middle",
+          "middle", "low", "high")
> 
> ses.f.bad.order <- factor(ses)
> 
> is.factor(ses.f.bad.order)
[1] TRUE
> 
> levels(ses.f.bad.order)
[1] "high"   "low"    "middle"
```


需要在定义factor variables的时候指定levels：

```python
> ses.f <- factor(ses, levels = c("low", "middle", "high"))
> is.factor(ses.f)
[1] TRUE
> levels(ses.f)
[1] "low"    "middle" "high"  
```


## 15.2 创建有序因子变量

使用`ordered`函数创建有序因子变量，与`factor`函数需要的参数列表相同。


```python
> ses.order <- ordered(ses, levels = c("low", "middle", "high"))
> ses.order
 [1] low    middle low    low    low    low    middle low    middle middle middle middle middle high   high  
[16] low    middle middle low    high  
Levels: low < middle < high

> is.factor(ses.order)
[1] TRUE

```

## 15.3 添加或是删除因子变量中的levels

### 15.3.1 添加levels

`ses.f`是上面生成的一个因子变量，f[21]表示其第21个元素，要给第21个元素添加levels为`very.high`

```python
> ses.f
 [1] low    middle low    low    low    low    middle low    middle middle middle middle
[13] middle high   high   low    middle middle low    high   <NA>  
Levels: low middle high
> 
> ses.f[21] <- "very.high"
Warning message:
In `[<-.factor`(`*tmp*`, 21, value = "very.high") :
  invalid factor level, NA generated
> 
> ses.f
 [1] low    middle low    low    low    low    middle low    middle middle middle middle
[13] middle high   high   low    middle middle low    high   <NA>  
Levels: low middle high
```

上面给出了警告信息，提示无效的factor level，添加后的ses.f中的第21个元素是<NA>，即无效值。

只有通过下面的操作才能添加levels，先创建一个有`very.high`的factor，再给factor的第21个添加值。

```python
> ses.f <- factor(ses.f, levels = c(levels(ses.f), "very.high"))
> 
> ses.f[21] <- "very.high"
> 
> ses.f
 [1] low       middle    low       low       low       low       middle    low      
 [9] middle    middle    middle    middle    middle    high      high      low      
[17] middle    middle    low       high      very.high
Levels: low middle high very.high
```

### 15.3.2 删除levels

```python

# 不会删除level中的值
> ses.f.new <- ses.f[ses.f != "very.high"]
> 
> ses.f.new
 [1] low    middle low    low    low    low    middle low    middle middle middle middle
[13] middle high   high   low    middle middle low    high  
Levels: low middle high very.high


# 重新创建的factor，删除了没有被引用的levels
> ses.f.new <- factor(ses.f.new)
> 
> ses.f.new
 [1] low    middle low    low    low    low    middle low    middle middle middle middle
[13] middle high   high   low    middle middle low    high  
Levels: low middle high
```

## 15.4 示例

为了说明因子变量的用处，我们要创建一个data frame：

```python
> 
> read <- c(34, 39, 63, 44, 47, 47, 57, 39, 48, 47, 34, 37, 47, 47, 39, 47,
+           47, 50, 28, 60)
> 
> 
> combo <- data.frame(schtyp, schtyp.f, ses, ses.f, read)
> combo
   	schtyp schtyp.f    ses  ses.f read
1       0  private    low    low   34
2       0  private middle middle   39
3       1   public    low    low   63
4       0  private    low    low   44
5       0  private    low    low   47
6       0  private    low    low   47
7       1   public middle middle   57
8       0  private    low    low   39
9       1   public middle middle   48
10      0  private middle middle   47
11      1   public middle middle   34
12      1   public middle middle   37
13      1   public middle middle   47
14      1   public   high   high   47
15      0  private   high   high   39
16      0  private    low    low   47
17      1   public middle middle   47
18      1   public middle middle   50
19      1   public    low    low   28
20      0  private   high   high   60

```



```python
> table(ses, schtyp)
        schtyp
ses      0 1
  high   2 1
  low    6 2
  middle 2 7
> 
> table(ses.f, schtyp.f)
        schtyp.f
ses.f    private public
  low          6      2
  middle       2      7
  high         2      1
> 
```


```python
> bwplot(schtyp ~ read | ses, data = combo, layout = c(2, 2))
```

![image](https://user-images.githubusercontent.com/18595935/33079878-0d1f7536-cf1a-11e7-9017-203378af7723.png)


- As in the tables the factor variable will indicate a better ordering of the graphs as well as add useful labels.

```python
bwplot(schtyp.f ~ read | ses.f, data = combo, layout = c(2, 2))
```

![image](https://user-images.githubusercontent.com/18595935/33079929-2b12d2f4-cf1a-11e7-9cd2-ad445571686e.png)