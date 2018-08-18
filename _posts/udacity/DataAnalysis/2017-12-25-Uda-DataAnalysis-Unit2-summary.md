---
layout: post
title: Uda-DataAnalysis-Unit2--R统计分析总结
date: 2017-12-14 06:00:01
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}

经过近两个月的拉锯战，终于把第二部分R这一块的项目提交了，现在回过头来看这一部分其实不难，只是自己想一次就把R这一块都弄懂，所以这当然不太现实。
现在看来效率最高的就是跟着Udacity的节奏走，学习的过程中需要哪块补哪一块，而不是想一开始就把需要的补齐，难度太大也打击积极性。
下面将第二部分的R进行一个整理:

# [Uda-DataAnalysis-22-[扩展]-free R tutorial by datacamp](http://road2ai.info/2017/10/21/Uda-DataAnalysis-datacamp-22/)

介绍R语法的基本概念，包含数据类型，数据结构，以及运算符等。

- vector: `c(1, 10, 49)`,容器，可以混合不同的数据类型
- matrix： `matrix(1:9, byrow = TRUE, nrow = 3)`,矩阵表示一组相同数据类型元素的集合，给定一个固定的行和列，它是二维的
- factors: `factor()` 创建
- data frame： `data.frame()`，类似二维矩阵，但是可以混合多种数据类型，从CSV中读取的数据默认为data frame类型
- list: `list()`，list中可以存储完全不同的数据结构

# [Uda-DataAnalysis-22--R基础](http://road2ai.info/2017/11/21/Uda-DataAnalysis-22/)

与上面内容有重合，数据集的读取以及根据条件取子集，新增或删除一列,另外最后一节重点扩展了因子变量。

- `subset(mtcars, mpg < 14 | disp > 390)` 条件子集
- `mtcars <- subset(mtcars, select = -year)` 删除指定列
- `mtcars$year <- c(1974, 1975,1976,1977)` 通过vector给指定列赋值

# [Uda-DataAnalysis-23--探索单一变量](http://road2ai.info/2017/11/22/Uda-DataAnalysis-23/)

[练习](http://road2ai.info/2017/11/23/Uda-DataAnalysis-24/)

探讨如何通过单个变量对数据进行分析：
- 单一变量的直方图，y轴是x在不同范围下的count
- 在上面的基础上，再添加一个变量，切分为多个直方图，也叫分面`facet_wrap(~dob_month,ncol = 3)`
- 通过`scale_x_continuous`对轴进行限制，调整组距离
- 对数据集进行过滤，比如忽略NA观测值`!is.na(gender)`
- 使用`by(pf$friend_count,pf$gender,summary)`进行分类统计，中间gender是类别变量


# [Uda-DataAnalysis-25--探索两个变量](http://road2ai.info/2017/11/23/Uda-DataAnalysis-25/)

[练习](http://road2ai.info/2017/11/23/Uda-DataAnalysis-26/)

探讨两个变量之间分关系：
- 散点图`geom_point`，使用`alpha = 1/20`添加透明度避免过度绘制
- `geom_jitter`产生抖动
- 【重要】`summarise`产生新的数据集
- 将摘要与原始数据叠加，`geom_line(stat = "summary",fun.y = mean)`
- 两变量之间的相关性计算 `cor.test(pf$age,pf$friend_count,method="pearson")`
- 针对特定数据集计算相关性 `with(subset(pf,pf$age <= 70),cor.test(age,friend_count,method="pearson"))`
- 回归线 `geom_smooth(method="lm",color="red")`
- 使用 `grid.arrange(p2,p1,p3,ncol=1)`排列图形
- x轴变量或y轴变量，截取特定范围 `xlim(0,quantile(diamonds$carat,0.99))`
- 如何使用`group_by`和`summarise`

# [Uda-DataAnalysis-27--探索多个变量](http://road2ai.info/2017/12/09/Uda-DataAnalysis-27/)

[练习](http://road2ai.info/2017/12/09/Uda-DataAnalysis-28/)

针对三个以及以上的变量进行分析：
- 使用`dcast`重塑数据
- `geom_line(aes(color = gender), stat = 'summary', fun.y = median)`，根据gender种类描画多条曲线
- 去除数据中的噪音，比如以天为单位作为x轴，那可能会出现一些异常值，如果将天除以30，那会使曲线更加平滑
- 或是在数据中添加一条平滑曲线`geom_smooth(method="auto",color="red")`
- 或是直接描画成一条平滑曲线 `geom_smooth(aes(color = gender))`
- `unique(yo$price)` 查看数据中的唯一值
- `ggpairs` 绘制散点图矩阵
- 颜色分类 `scale_color_brewer(type = 'qual')`
- 使用`theme`控制轴的文本大小颜色位置等
- 将某一段范围的数据，按照指定的区间段进行切断，`cut`
- 保存图形 `ggsave`

# [Uda-DataAnalysis-29--钻石与价格预测](http://road2ai.info/2017/12/14/Uda-DataAnalysis-29/)

- `geom_point(fill=I("#F79420"),color=I("blue"),shape=21)` 设置散点图中的颜色和填充色以及大小
- 对x轴y轴取对数`scale_y_log10()`
- 构建线性模型 `m1 <- lm(I(log(price)) ~ I(carat^(1/3)),data = diamonds)`

# [项目报告](http://road2ai.info/2017/12/14/Uda-DataAnalysis-pj02/)