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