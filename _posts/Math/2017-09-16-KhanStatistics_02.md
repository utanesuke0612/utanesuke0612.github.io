---
layout: post
title: KhanStatistics-02-集中趋势与方差
date: 2017-09-16 00:00:02
categories: 数学
tags: 数学
---
* content
{:toc}

> [KhanStatistics-XX...]系列，参考[**可汗学院公开课：统计学**](http://open.163.com/special/Khan/khstatistics.html)

---
# 1. 统计：集中趋势
统计学大体可分为2类:

1.描述性统计 discriptive：假设有一大堆数据，却希望在不告诉别人所有数据的情况下，可以找一些指示性的数据来代表所有数据，而无需将所有数据都说一次。

2.推断性统计 inferential：运用数据来对实物做结论， 假设从总体得到一些样本，从分析这些样本而推断出总体。

- Mean (Arithmatic) 算术平均数\ Median 中位数 \ Mode 众数.
引入集中趋势的概念, 使用中位数和众数不会受最大数的影响，更有代表性
 .
- outlier--离群值，与其它数不一样的数，有此数时，中位数和众数比算术平均数更能体现该组数的集中趋势。


# 2. 统计：样本sample和总体population

- μ = population mean 总体均值
- x = sample mean 样本均值
- Σ：sigma 求所有样本Xn之和。

![image](https://user-images.githubusercontent.com/18595935/30510395-e0bd2060-9afd-11e7-8033-439b3031a072.png)



# 3. 统计：总体方差 variance of population
measures of dispersion：离中趋势的衡量
如下有两组值，分别是 2,2,3,3 和 0,0,5,5，其平均值都是2.5。
总体方差是通过每个值与总体均值之间差值平方之和，然后求平均得到。
公式参考下图:

![image](https://user-images.githubusercontent.com/18595935/30512069-452f9672-9b21-11e7-8856-28eee48492fe.png)

# 4. 统计：样本方差 variance of sample
上面讲述了总体方差，样本方差与之类似，只是统计的对象是总体中抽取的样本。
推论统计就是对样本进行描述性统计，然后推论统计得到总体。
![image](https://user-images.githubusercontent.com/18595935/30517570-fccacb76-9b9e-11e7-957d-4d3d5112cf12.png)

但是上面的样本方差是由偏差的，样本的无偏方差公式如下:
![image](https://user-images.githubusercontent.com/18595935/30517599-f4458c06-9b9f-11e7-86f0-b4ebc6d43ab8.png)

为什么分母是 n-1而不是n呢，这是因为:
![image](https://user-images.githubusercontent.com/18595935/30517688-2c63eec8-9ba2-11e7-83ad-b9e8571e4ea5.png)

所以样本方差通常都会比总体方差要小，除非样本平均X与总体平均u正好相等。
那么，在不知道随机变量真实数学期望的前提下，如何“正确”的估计方差呢？答案是把上式中的分母n换成n-1，通过这种方法把原来的偏小的估计“放大”一点点，我们就能获得对方差的正确估计了：
![image](https://user-images.githubusercontent.com/18595935/30517718-1360de12-9ba3-11e7-8d69-71d1d9ff7cac.png)

详细可以参考 [知乎:为什么样本方差（sample variance）的分母是 n-1？](https://www.zhihu.com/question/20099757)

# 5. 统计：标准差
标准差（英语：Standard Deviation，SD），数学符号 σ（sigma），在概率统计中最常使用作为测量一组数值的离散程度之用。标准差定义：为方差开算术平方根，反映组内个体间的离散程度；标准差与期望值之比为标准离差率。

![image](https://user-images.githubusercontent.com/18595935/30517745-c8d326c4-9ba3-11e7-9dde-bda36386092e.png)

![image](https://user-images.githubusercontent.com/18595935/30517748-de8e4002-9ba3-11e7-8e82-cbb136c76647.png)
