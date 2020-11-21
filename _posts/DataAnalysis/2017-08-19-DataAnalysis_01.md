---
layout: post
title: PythonDataAnalysis-00-数据分析准备工作
date: 2017-08-18 08:45:59
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

# 1. 导读

## 1. 课程目标:
1. 通过本系列的学习，掌握对数据的表示，清洗，统计和展示全过程。
![image](https://user-images.githubusercontent.com/18595935/29481941-c3e391be-84c2-11e7-85b0-ec45766c96f4.png)
 - Numpy：存取数据，操作数据
 - Matplotlib：图形的绘制
 - Pandas：数据分析

2. 掌握如下工具使用：　Conda / Spyder/Ipython

## 2. 什么是数据分析:
数据分析的主题思想，就是摘要，有损地提取数据特征的过程。通过对大量数据的摘要，进行基本统计，分布/累计统计，数据特征提取，数据挖掘，最后形成知识。


# 2. AnacondaIDE的基本使用
## 1. 下载[Anaconda](https://www.continuum.io/downloads)软件
这个工具主要用于数据分析和科学计算，包含多个主流工具，支持800多个第三方库。
Anacoda本身并不是一个开发环境，它是一个包管理和环境管理工具，类似于python自带的pip，管理python第三方库，环境管理能够允许用户使用不同版本的Python，并灵活切换。

支撑Anacoda的几个重要工具为：
- spyder:编程工具,包含编辑区/文件导航/Ipython
- IPython:交互式的编程环境

## 2. Ipython
是一个功能强大的交互式shell，适合进行交互式数据可视化和GUI相关应用。

- `变量名或函数名?`加上问号后，能显示其属性，非常方便如下:

```python
In [1]: a = [1,"2",4]

In [2]: a?
Type:        list
String form: [1, '2', 4]
Length:      3
Docstring:  
list() -> new empty list
list(iterable) -> new list initialized from iterable's items

In [3]: def m():
   ...:     print("hello")
   ...:     

In [4]: m?
Signature: m()
Docstring: <no docstring>
File:      c:\users\utane\<ipython-input-3-6146f003c976>
Type:      function
```

- `%run demo.py`用于运行.py程序
> 注意：%run在一个空的命名空间 执行%，所以所有的lib都要在py中引入

- 如下是常用的魔术命令:

![image](https://user-images.githubusercontent.com/18595935/29481930-9c0538f0-84c2-11e7-8294-252677b064ea.png)

- 下面展示下上面魔术命令的使用

```python
In [21]: import numpy

In [22]: a =  numpy.random.randn(100,100)

In [23]: %timeit numpy.dot(a,a)
The slowest run took 5.88 times longer than the fastest. This could mean that an intermediate result is being cached.
10000 loops, best of 3: 27.6 µs per loop

In [24]: %who
a        numpy   

In [25]: %hist
import numpy
a =  numpy.random.randn(100,100)
%timeit numpy.dot(a,a)
%who
%hist

In [26]:
```
> 首先导入numpy包，%timeit计算多次的执行时间
