---
layout: post
title: Udacity-描述统计学-07-抽样分布
date: 2018-01-14 07:00:0
categories: 数学
tags: 统计学
---
* content
{:toc}

# 1. 比较样本均值

通过上面的标准正态分布，可以比较某个值在该分布中的位置，如果要比较多个样本之间的差异，可以使用样本的均值等进行比较：

![image](https://user-images.githubusercontent.com/18595935/34914174-73b8503c-f950-11e7-8203-1ec0bb0890bb.png)

# 3. 期望值

![image](https://user-images.githubusercontent.com/18595935/34914264-84dec3b2-f952-11e7-9c25-8ca36226a527.png)

# 6. 样本均值与分布

- 如下是连续两次后的可能均值：

![image](https://user-images.githubusercontent.com/18595935/34914314-9507bb08-f953-11e7-8922-a23bd9903f1a.png)

- 如何分布呢:

![image](https://user-images.githubusercontent.com/18595935/34914335-166a7636-f954-11e7-907f-b94f77fd10cf.png)

![image](https://user-images.githubusercontent.com/18595935/34914342-3b8d7c06-f954-11e7-87fb-d702ba9259bf.png)

# 11. 标准偏差之间的关系

![image](https://user-images.githubusercontent.com/18595935/34916577-e17faa52-f97d-11e7-9010-64f518ec264e.png)

- 关系如下:

![image](https://user-images.githubusercontent.com/18595935/34916620-8708e3b2-f97e-11e7-8df4-fe1e8eb2f17f.png)


![image](https://user-images.githubusercontent.com/18595935/34916655-09b845d2-f97f-11e7-9b2e-2bbd6fa1c70f.png)


# 12. 中心极限定理

中心极限定理是概率论中的一组定理。中心极限定理说明，在适当的条件下，大量相互独立随机变量的均值经适当标准化后依分布收敛于正态分布。
这组定理是数理统计学和误差分析的理论基础，指出了大量随机变量之和近似服从正态分布的条件。

![image](https://user-images.githubusercontent.com/18595935/34916798-015aed3e-f981-11e7-950c-d437c4e03b2a.png)

本图描绘了多次抛掷硬币实验中出现正面的平均比率，每次实验均抛掷了大量硬币。

- 抛100回骰子，每回抛一次骰子，最后得到的是平均分布的图形

![image](https://user-images.githubusercontent.com/18595935/34916867-0f677216-f982-11e7-8ba9-1e01f6daf2ca.png)

这是样本标准差与总体标准差相同，因为样本就是1，每回只抛一次骰子

- 类似，如果每回抛两次骰子，将呈现正态分布

# 17. 练习:标准误差

![image](https://user-images.githubusercontent.com/18595935/34917046-9b3c9828-f984-11e7-84ab-2cae13182a34.png)

如上图，每回抛两次骰子，故样本size是2，先求出总体的标准偏差，再根据中心极限定理，求出样本的标准偏差。

另外，样本的均值，与总体的均值相同，都是3.5，与样本的size无关。

# 18. 5次骰子

![image](https://user-images.githubusercontent.com/18595935/34944426-dcace678-fa42-11e7-91f4-020bbddd5855.png)

上图可以看出，样本的size从2变成5，分母变大，标准差变小，分布更窄。

# 24. M&M CLT

有个48个碟子，每个碟子中装了一包MM糖，一包有很多不同颜色的MM糖，从中选择蓝色的MM糖作为研究对象，48碟中蓝色MM糖的均值是11.25，标准差是3.49.
根据中心极限定理(`Central Limit Theorem`)，每次选择5个碟子，这5个碟子中的蓝色MM糖，重复50次，理论上平均值不变，SE(standard error)为1.56.

![image](https://user-images.githubusercontent.com/18595935/34945108-6fbb04e8-fa45-11e7-965d-141aa66534af.png)

# 29. klout抽样分布(标准偏差)

社交影响力的分布图：

![image](https://user-images.githubusercontent.com/18595935/34946397-0a3d2f74-fa4a-11e7-8037-aa560dff6b62.png)
