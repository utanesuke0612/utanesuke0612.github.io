---
layout: post
title: PythonDataAnalysis-08-Pandas数据特征分析
date: 2017-08-19 21:50:59
categories: 数据分析
tags: DataAnalysis
---
* content
{:toc}

> [PythonDataAnalysis-XX...]系列，参考[**Python数据分析与展示 嵩天@北京理工**](http://www.icourse163.org/course/BIT-1001870002)

根据第三方库内容特点，课程共分8个内容单元和4个实战单元：
 - 单元1：NumPy库入门：一维、二维、N维、高维数据表示和操作
 - 单元2：NumPy数据存取与函数：多维数据存储、随机数函数、统计函数、梯度函数
 - 单元3：**实战**：图像的手绘效果
 - 单元4：Matplotlib库的入门和基本使用
 - 单元5：Matplotlib基础绘图函数：饼图、直方图、极坐标图、散点图
 - 单元6：**实战**：引力波的绘制
 - 单元7：Pandas库入门：Series、DataFrame类型、基本操作
 - 单元8：Pandas数据特征分析：数据排序、基本统计分析、累计分析、相关分析

---
# 1. 数据的排序

通过对一组数据进行摘要，能过获得:
- 基本统计（含排序）
- 分布与累计统计
- 数据特征（相关性，周期性）
- 数据挖掘
> 什么是摘要，有损的提取数据特征的过程

# 1.1 sort_index() 索引排序
.sort_index()方法在指定轴上根据索引进行排序，默认升序 ，
.sort_index(axis=0, ascending=True)

```python
In [9]: b = pd.DataFrame(np.arange(20).reshape(4,5),index=["c","a","d","b"])

In [10]: b
Out[10]:
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

# 比如a,b,c,d代表考试科目，0,1,2,3,4代表班次，实际的值代表平均分
# 默认按第一维即考试科目排序
In [11]: b.sort_index()
Out[11]:
    0   1   2   3   4
a   5   6   7   8   9
b  15  16  17  18  19
c   0   1   2   3   4
d  10  11  12  13  14

# 按第二维班次的索引进行降序排序
In [12]: b.sort_index(axis=1,ascending=False)
Out[12]:
    4   3   2   1   0
c   4   3   2   1   0
a   9   8   7   6   5
d  14  13  12  11  10
b  19  18  17  16  15
```

## 1.2 sort_values()属性值的排序
.sort_values()方法在指定轴上根据数值进行排序，默认升序
- Series.sort_values(axis=0, ascending=True)
- DataFrame.sort_values(by, axis=0, ascending=True)
by :axis轴上的某个索引或索引列表

```python
In [17]: b
Out[17]:
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

# 1轴上，索引为“a”的行进行排序，b[a][0],b[a][1]..b[a][4]的值排序
In [18]: b.sort_values("a",axis=1,ascending=False)
Out[18]:
    4   3   2   1   0
c   4   3   2   1   0
a   9   8   7   6   5
d  14  13  12  11  10
b  19  18  17  16  15

# 后面的axis=0也可以省略，默认在0轴即第一维上进行排序
# 0轴上，索引为3的列进行排序，b[a][3],b[b][3]..b[c][3]进行排序
In [19]: b.sort_values(3,axis=0,ascending=False)
Out[19]:
    0   1   2   3   4
b  15  16  17  18  19
d  10  11  12  13  14
a   5   6   7   8   9
c   0   1   2   3   4
```


# 2. 数据的基本分析

- 适用于Series和DataFrame类型

|       方法        |                                   说明                                    |
|:----------------- |:------------------------------------------------------------------------- |
| .sum()            | 计算数据总和，按0轴计算(求列上的值，列上的值有共同的属性，才有意义)，下同 |
| .count()          | 非NaN值的数量                                                             |
| .mean(),.median() | 数据的算术平均值，算术中位数                                              |
| .var(),.std()     | 数据的方差和标准差                                                        |
| .min(),.max()     | 数据的最小值，最大值                                                      |
| .describe()       | 数据的所有属性                                                            |
|                   |                                                                           |

- 只适用于Series类型

|        方法         |                   说明                    |
|:------------------- |:----------------------------------------- |
| .argmin(),.argmax() | 计算最大值，最小值所在位置的索引-自动索引 |
| .idxmin(),.idxmax() | 自定义索引                                          |


```python
In [20]: b
Out[20]:
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

In [21]: b.describe()
Out[21]:
               0          1          2          3          4
count   4.000000   4.000000   4.000000   4.000000   4.000000
mean    7.500000   8.500000   9.500000  10.500000  11.500000
std     6.454972   6.454972   6.454972   6.454972   6.454972
min     0.000000   1.000000   2.000000   3.000000   4.000000
25%     3.750000   4.750000   5.750000   6.750000   7.750000
50%     7.500000   8.500000   9.500000  10.500000  11.500000
75%    11.250000  12.250000  13.250000  14.250000  15.250000
max    15.000000  16.000000  17.000000  18.000000  19.000000

# 获取某一行上的数据
In [197]: b.describe().loc['max']
Out[197]:
0    15.0
1    16.0
2    17.0
3    18.0
4    19.0
Name: max, dtype: float64

# 获取第二列的值

In [198]: b.describe()[2]
Out[198]:
count     4.000000
mean      9.500000
std       6.454972
min       2.000000
25%       5.750000
50%       9.500000
75%      13.250000
max      17.000000
Name: 2, dtype: float64

```

## 2.1 累计统计分析函数
对数列中的前N个数，进行累积运算，能减少for循环的使用

|    方法    |    说明     |
|:---------- |:----------- |
| .cumsum()  | 前N个数的和 |
| .cumprod() | 积          |
| .cummax()  | 最大值      |
| .cummin()  | 最小值      |


```python
In [23]: b
Out[23]:
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

In [22]: b.cumsum()
Out[22]:
    0   1   2   3   4
c   0   1   2   3   4
a   5   7   9  11  13
d  15  18  21  24  27
b  30  34  38  42  46
```

- 另外还提供了适用于Series和DataFrame类型的滚动计算(窗口计算)

|           方法           |                说明                 |
|:------------------------ |:----------------------------------- |
| .rolling(w).sum()        | 依次计算相邻w个元素的和             |
| .rolling(w).mean()       | 依次计算相邻w个元素的算术平均值     |
| .rolling(w).var()        | 依次计算相邻w个元素的方差           |
| .rolling(w).std()        | 依次计算相邻w个元素的标准差         |
| .rolling(w).min() .max() | 依次计算相邻w个元素的最小值和最大值 |
|                          |                                     |

```python
In [199]: b
Out[199]:
    0   1   2   3   4
c   0   1   2   3   4
a   5   6   7   8   9
d  10  11  12  13  14
b  15  16  17  18  19

In [200]: b.rolling(2).sum()
Out[200]:
      0     1     2     3     4
c   NaN   NaN   NaN   NaN   NaN
a   5.0   7.0   9.0  11.0  13.0
d  15.0  17.0  19.0  21.0  23.0
b  25.0  27.0  29.0  31.0  33.0

In [201]: b.rolling(3).mean()
Out[201]:
      0     1     2     3     4
c   NaN   NaN   NaN   NaN   NaN
a   NaN   NaN   NaN   NaN   NaN
d   5.0   6.0   7.0   8.0   9.0
b  10.0  11.0  12.0  13.0  14.0

```

## 2.2 相关分析
两个事物，表示为X和Y，如何判断它们之间存在的相关性呢？
相关性:
- X增大，Y增大，两个变量 正相关
- X增大，Y减少，两个变量 负相关
- X增大，Y无视，两个变量 不相关

### 1. 协方差
具体定义参考[wiki-协方差](https://zh.wikipedia.org/zh-cn/%E5%8D%8F%E6%96%B9%E5%B7%AE)
上面是协方差公式，下面是方差公式。

![image](https://user-images.githubusercontent.com/18595935/30768682-5758ef40-a046-11e7-84ce-f20a40e77eb6.png)

- 协方差 > 0 ,X和Y正相关
- 协方差 < 0 ,X和Y负相关
- 协方差 = 0 ,X和Y不相关

### 2. Pearson相关系数
在统计学中，皮尔逊积矩相关系数（英语：Pearson product-moment correlation coefficient，又称作 PPMCC或PCCs[1], 文章中常用r或Pearson's r表示）用于度量两个变量X和Y之间的相关（线性相关），其值介于-1与1之间。在自然科学领域中，该系数广泛用于度量两个变量之间的相关程度
>参考[wiki:Pearson相关系数](https://zh.wikipedia.org/wiki/%E7%9A%AE%E5%B0%94%E9%80%8A%E7%A7%AF%E7%9F%A9%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0)

计算公式如下:

![image](https://user-images.githubusercontent.com/18595935/30768754-e231c1b8-a047-11e7-949b-8d5597d3a2ad.png)

- r取值范围为[-1,1]
- 0.8-1.0 极强相关
- 0.6-0.8 强相关
- 0.4-0.6 中等程度相关
- 0.2-0.4 弱相关
- 0.0-0.2 极弱相关或无关

### 3. 相关分析函数

|  方法   |    说明    |
|:------- |:---------- |
| .cov()  | 协方差矩阵 |
| .corr() | 计算相关系数矩阵, Pearson,Spearma,Kendall等系数 |


```python
import matplotlib.pyplot as plt
import pandas as pd

hprice = pd.Series([3.04,22.93,12.75,22.6,12.33],index=['2008','2009','2010','2011','2012'])
m2 = pd.Series([8.18,18.38,9.13,7.82,6.69],index=['2008','2009','2010','2011','2012'])

# Series用values获取属性值
plt.plot(hprice.index,hprice.values,'go-',m2.index,m2.values,'b-.')
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/30768997-c6f9b4d8-a04b-11e7-93ce-17a6a1c40a41.png)


# 3. 小结
本节简单讲述了如何对数据进行摘要：

|     功能     |             函数             |
|:------------ |:---------------------------- |
| 排序         | .sort_index(),.sort_values() |
| 基本统计函数 | .describe()                  |
| 累计统计函数 | .cum*(),.rolling().*()       |
| 相关性分析   | .corr(),.cov()                             |
