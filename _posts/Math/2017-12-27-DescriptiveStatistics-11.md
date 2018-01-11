---
layout: post
title: Udacity-描述统计学-4-可变性
date: 2017-12-27 04:00:0
categories: 数学
tags: 统计学
---
* content
{:toc}

# 9. 练习 Q3-Q1

![image](https://user-images.githubusercontent.com/18595935/34774024-31c2d596-f651-11e7-8764-69d226f224c0.png)

四分位差的计算：

1. 先求中位数，将数据分成两个部分。
2. 针对分成的两个部分，对每个部分求中位数，得到Q1和Q3.

# 12. 定义异常值

![image](https://user-images.githubusercontent.com/18595935/34777919-292dbbea-f65f-11e7-8b86-e2b42f9cf9ee.png)

# 15. IQR的不足

完全不同的数据集，也有可能有相同的boxplot即箱线图

![image](https://user-images.githubusercontent.com/18595935/34778269-31701702-f660-11e7-998f-99b6d0bc5fab.png)

# 35. 标准偏差的重要性

标准正态分布，西格玛表示一个标准偏差范围。

![image](https://user-images.githubusercontent.com/18595935/34829660-c58de008-f724-11e7-9814-b83655b64a7c.png)

# 38. 贝塞尔校正

在进行样本选取的时候，通常会选取到居中的值，特别是标准正态分布时，会更加倾向于选取靠近中心的值，这样就会缩小标准偏差，故需要采用贝塞尔校正，即使用n-1而不是n进行平均值计算。

![image](https://user-images.githubusercontent.com/18595935/34829901-892cf40e-f725-11e7-9947-fd733d3f4ed0.png)

# 99. 术语

- `deviation`：离均差
- `average deviation`：平均偏差
- `variance`：平方偏差
- `standard deviation`：标准差