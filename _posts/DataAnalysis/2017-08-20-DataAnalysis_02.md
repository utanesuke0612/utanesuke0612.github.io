---
layout: post
title: PythonDataAnalysis-01-Numpy库入门
date: 2017-08-19 20:45:59
categories: 数据分析
tags: Python 北理 DataAnalysis
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


# 1. 数据维度的概念
- 一维数据:
一维数据由对等关系的有序或无序数据构成，采用线性方式组织。可以使用列表/集合等数据结构进行组织。
如`一个学生`的语文，数学，英语等`各科成绩`。

>列表和数组都是一组数据的有序结构,但是列表的数据类型可以不同，而数组的数据类型相同。


- 二维数据:
是一维数据的组合形式。表格是典型的二维数据，可使用多维列表表示数据。
如`多个学生`的`各科成绩`。

- 多维数据:
由一维或二维数据在新维度上扩展而成，可使用多维列表表示数据。。
如`多个学生`的`各科成绩`，并添加`时间维度`，2016年和2017年的对比。

- 高维数据：
利用最基本的`二元关系`展示数据间的复杂结构。利用`键值对`将数据组织起来形成的数据,可以使用`字典类型`或是`数据格式(如Jason/XML/YAML)`来进行表示。
示例:

```python
# 字典
dict = {
	 "firstName":"Tian",
	 "lastName":"Song",
	}
```
Jason数据格式

```python
{
  "firstName":"Tian",
  "lastName":"Song",
  "address":{
		"city":"Beijing",
		"ZipCode":"10000"
	     }
}
```


# 2. Numpy的数组对象:ndarray
- 引入numpy库
`import numpy as np`：引入模块别名，尽管可以修改别名，但建议使用约定俗成的名称。

- 为什么需要一个额外的数组？
使用数组，当维度相同的时候，将数组当作一个普通数据类型，能够直接处理。另外，Numpy采用C语言实现，经过优化了的可以提高运算速度。

```python
import numpy as np

def npSum():
    a = np.array([0,1,2,3,4])
    b = np.array([9,8,7,6,5])
    c = a**2 + b**3
    return c

print(npSum())

def pySum():
    a = [0,1,2,3,4]
    b = [9,8,7,6,5]
    c = []

    for i in range(len(a)):
        c.append(a[i]**2 + b[i]**3)

    return c

print(pySum())
```
输出结果为:
```
[729 513 347 225 141]
[729, 513, 347, 225, 141]
```
1. ndarray使用空格进行数据隔离，list使用`,`隔离。
2. 注意ndarray的数据定义方式`a = np.array(list)`
3. `npSum()`，将ndarray当作了普通类型进行处理。
4. 如果修改a这个ndarry的维度如`a = np.array([0,1,2,3,4,5])`，再与b一起进行普通运算的时候，会出现错误:`ValueError: operands could not be broadcast together with shapes (6,) (5,) `，即一维维度为6和5的两个ndarry是不能进行运算的。
5. 如果将`a`中的某个元素如4修改为4.0,那么运算出来的结果都变成浮点数，如`[ 729.  513.  347.  225.  141.]`。
> 科学计算中，一个维度所有数据的类型往往相同，数组对象采用相同数据类型，有助于节省运算和存储空间。

- ndarray对象的属性

| 属性 | 说明 |
|:-----------|:-----------|
| .ndim | 维度 |
| .shape | ndarray对象的尺度，对于矩阵，n行m列 |
| .size | ndarray对象元素个数，n*m的值 |
| .dtype | ndarray对象的元素类型 |
| .itemsize | ndarray对象中每个元素的大小，字节为单位 |


示例如下:

```python
a = np.array([[0,1,2,3,4],
             [9,8,7,6,5]])

print(a.ndim) # 输出 2
print(a.shape) # 输出 (2, 5)
print(a.size) # 输出 10
print(a.dtype) # 输出 int32
print(a.itemsize) # 输出 4
```
如果修改a中某个维度，如修改为`[0,1,2,3,4,5]`，则输出如下的结果:

```python
1
(2,)
2
object
8
```
这时因为两个元素的维度不同，故都当作object处理，类似于`a = np.array([object1,object2])`，即变成了1维数据，含2个元素，每个item占用8个byte，这里应该只是存储了指向object的地址。
> 这是64位机器，那地址值就是8个byte。如果在公司执行，应该就是4.

ndarray数组可以由`非同质对象`构成，`非同质ndarray元素`为对象类型，它无法有效发挥Numpy优势，尽量避免使用。


- ndarray的元素类型

![image](https://user-images.githubusercontent.com/18595935/29492851-6b88a5e2-85c4-11e7-9f6a-1e68e3d15ef8.png)

![image](https://user-images.githubusercontent.com/18595935/29492857-ade9c7d6-85c4-11e7-963e-ab27f2ee7baf.png)

![image](https://user-images.githubusercontent.com/18595935/29492865-e4732a72-85c4-11e7-9ada-f6e1baa75645.png)


# 3. ndarray的创建和变换
## 3.1 ndarray的创建

- 从python列表，元组等类型创建ndarray数组，例如 `x = np.array(list/tuple,dtype=np.float32)`,不指定dtype时，Numpy将根据数据关联一个dtype类型。
- 使用Numpy中函数创建ndarray数组，如:`arange`,`ones`,`zeros`等。

![image](https://user-images.githubusercontent.com/18595935/29492951-b4bbdee4-85c6-11e7-97a7-9bc60e1c65b1.png)

```python
In [2]: import numpy as np

In [4]: print(np.arange(10))
[0 1 2 3 4 5 6 7 8 9]

In [5]: print(np.ones(10))
[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]

In [6]: print(np.zeros(10))
[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]

In [7]: print(np.full(10,3))
[3 3 3 3 3 3 3 3 3 3]

In [10]: print(np.eye(3))
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

```

上面的方式中，产生的都是一维，可以使用元组作为参数，产生多维ndarray。比如：

```python
In [9]: x = np.full((2,4),3)

In [10]: print(x)
[[3 3 3 3]
 [3 3 3 3]]

In [11]: x.shape
Out[11]: (2, 4)
```

另外，还有`np.ones_like(a)`,`np.zeros_like(a)`，`np.full_like(a,val)`，根据a的形状，生成一个对应的ndarray。

- 使用Numpy中其他函数创建ndarray数组：

① `np.linspace()`:根据起止数据等间距填充数据，形成数组

② `np.concatenate()`:将两个或多个数组合并成一个新的数组

```python
In [21]: a = np.linspace(1,10,4)

In [22]: print(a)
[  1.   4.   7.  10.]

In [23]: b = np.linspace(1,10,4,endpoint=False)

In [24]: print(b)
[ 1.    3.25  5.5   7.75]

In [25]: c = np.concatenate((a,b))

In [26]: print(c)
[  1.     4.     7.    10.     1.     3.25   5.5    7.75]
```
> 注意上面endpoint的作用，设置为False的话，则不包含最后的数。
> linspace使用的浮点数，科学计算中大多使用浮点数。Numpy绝大部分使用浮点数。

- 从字节流(raw bytes)中创建ndarray数组。(略)

- 从文件读取特定格式，创建ndarray数组。(略)

## 3.2 ndarray的变换
对于创建后的ndarray，可以对其进行维度和元素类型的变换。
示例代码:
```python
In [28]: x = np.ones((2,3,4),dtype=np.int32)

In [29]: print(x)
[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]

In [30]: y = x.flatten()

In [32]: print(y)
[1 1 1 ..., 1 1 1]

In [33]: m = x.astype(np.float32)

In [34]: print(m)
[[[ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]]

 [[ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]
  [ 1.  1.  1.  1.]]]

In [36]: l = x.tolist()

In [37]: print(l)
[[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]]

```
- 改变维度`y = x.flatten()`，生成一个一维的ndarray。
- 改变类型`m = x.astype(np.float32)`。
- 转换为列表 `l = x.tolist()`，python中的list数据类型，比起Numpy在性能上会降低很多。转变后的list，其维度与ndarray保持一致。

# 4. ndarray数组操作

**索引**:获取数组中特定位置元素的过程。

**切片**:获取数组元素子集的过程。

## 4.1 一维数组的索引和切片

```python
In [39]: a = np.array([5,6,7,8,9])

In [40]: print(a[2])
7

In [41]: b = a[1:4:2]

In [42]: print(b)
[6 8]

In [43]: b = a[1:4:1]

In [44]: print(b)
[6 7 8]

```
> 索引,与python固有类似。另外，切片的a[1:4:2]，三个元素分别是起始编号，终止编号(不含)，步长，3元素用冒号分隔。

## 4.2 多维数组的索引和切片

- 示例1

```python
In [47]: m = np.arange(24).reshape((2,3,4))

In [48]: print(m)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]

In [50]: print(m[1,2,3])
23

In [51]: print(m[0,1,2])
6

In [52]: print(m[-1,-2,-3])
17

```

- 示例2(上述的扩展)

```python
In [53]: print(m[:,1,-3])
[ 5 17]

In [54]: print(m[:,1:3,:])
[[[ 4  5  6  7]
  [ 8  9 10 11]]

 [[16 17 18 19]
  [20 21 22 23]]]

In [55]: print(m[:,:,::2])
[[[ 0  2]
  [ 4  6]
  [ 8 10]]

 [[12 14]
  [16 18]
  [20 22]]]
```
① `m[:,1,-3]`:选取一个维度用：，外层(第一维)全选，第二维选第二个元素，第三维选倒数第三个，最终分别是5和7。

② `m[:,1:3,:]`:每个维度切片方法与一维数组相同，第一维全选，第二维为第2和第3个元素，第三维全选。

③ `m[:,:,::2]`：每个维度可以使用步长跳跃切片。

# 5. ndarray数组运算
- 数组与标量之间的运算，作用于数组的每一个元素。

```python
In [64]: a = np.arange(24).reshape((2,3,4))

In [65]: a.mean()
Out[65]: 11.5

# 取平均值
In [66]: b = a / a.mean()

In [67]: print(a)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]

In [68]: print(b)
[[[ 0.          0.08695652  0.17391304  0.26086957]
  [ 0.34782609  0.43478261  0.52173913  0.60869565]
  [ 0.69565217  0.7826087   0.86956522  0.95652174]]

 [[ 1.04347826  1.13043478  1.2173913   1.30434783]
  [ 1.39130435  1.47826087  1.56521739  1.65217391]
  [ 1.73913043  1.82608696  1.91304348  2.        ]]]

```
> 注意函数是新生成一个数组，还是改变原始数据。几乎所有的议员数组都是新生成一个数组。

Numpy的设计理念，就是将数组当作普通类型使用。

- 常用运算函数:

![image](https://user-images.githubusercontent.com/18595935/29494259-430cc02c-85e1-11e7-8e62-d063f8760715.png)
![image](https://user-images.githubusercontent.com/18595935/29494269-631fc8e6-85e1-11e7-98ba-b1965e359ab7.png)
![image](https://user-images.githubusercontent.com/18595935/29494285-a812c61a-85e1-11e7-8ce6-8c968f203a93.png)


# 6. 小结
本章内容较多，没有太多需要理解的东西，需要用的时候直接查就OK，但需要大致了解，否则都不知道要查什么。
主要包含了如下的内容:
1. 数据的维度
2. `ndarray`类型的属性，创建以及变换
3. 数组的索引和切片
4. 数组的运算：一元函数和二元函数

总结下常见的ndarray类型的属性,创建和变换：
- 属性： `ndim`,`shape`,`size`,`dtype`,`itemsize`
- 方法：

  ①　`np.arange(n)`,`np.ones(shape)`,`np.zeros(shapes)`,`np.full(shape,val)`,`np.eye(n)`,`np.ones_like(a)`,
`np.zeros_like(a)`,`np.full_like(a,val)`

  ②　`.reshape(shape)`, `.resize(shape)`, `.swapaxes(ax1,ax2)`, `.flatten()`　→ `ndarray`调用这些函数

**这些方法和属性要多使用，才能灵活应用。**
