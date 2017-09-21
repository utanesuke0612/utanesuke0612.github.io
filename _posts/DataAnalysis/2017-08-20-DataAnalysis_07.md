---
layout: post
title: PythonDataAnalysis-07-Panda库入门
date: 2017-08-19 20:50:59
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

# 1. Pandas库的理解
Pandas是Python第三方库，提供高性能易用数据类型和分析工具，`import pandas as pd`。
Pandas基于NumPy实现，常与NumPy和Matplotlib一同使用。

```python
In [6]: import pandas as pd

In [7]: d = pd.Series(range(5))

In [8]: d
Out[8]:
0    0
1    1
2    2
3    3
4    4
dtype: int32

# 计算前N 项累加和
In [9]: d.cumsum()
Out[9]:
0     0
1     1
2     3
3     6
4    10
dtype: int32

```

有两个数据类型，`Series`和`DataFrame`，基于上述数据类型的各类操作:
- 基本操作
- 运算操作
- 特征类操作
- 关联类操作

|       NumPy        |       Pandas       |
|:------------------ |:------------------ |
| 基础数据类型       | 扩展数据类型       |
| 关注数据的结构表达 | 关注数据的应用表达 |
| 维度:数据间关系    | 数据与索引间的关系                   |


# 2. Pandas库的Series类型
Series类型由一组数据及与之相关的数据索引组成。

|  索引   |  数据  |
|:------- |:------ |
| index_0 | data_a |
| index_1 | data_b |
| index_2 | data_c |

```python
In [12]: import pandas as pd

In [13]: a = pd.Series([6,7,8,9])

In [14]: a
Out[14]:
0    6
1    7
2    8
3    9
dtype: int64
```
- 前面是0,1,2,3是自动索引，也可以自定义索引`a = pd.Series([6,7,8,9],index=['a','b','c','d'])`，作为第二个参数可以index，直接用`a = pd.Series([6,7,8,9],['a','b','c','d'])`。

# 2.1 Series类型的创建
可以由如下类型创建:
- Python列表，index与列表元素个数一致
- 标量值，index表达Series类型的尺寸
- Python字典，键值对中键是索引，index从字典中进行选择操作
- ndarray，索引和数据都可以通过ndarray类型创建
- 其他函数，如range()函数

```python

# 标量值创建
In [24]: a = pd.Series(8,['a','b','c'])

In [25]: a
Out[25]:
a    8
b    8
c    8
dtype: int64

# 字典创建
In [27]: mydict = {'a':9,'b':10,'c':12}

In [28]: d = pd.Series(mydict)

In [29]: d
Out[29]:
a     9
b    10
c    12
dtype: int64

# index从字典中进行选择操作
In [30]: d = pd.Series(mydict,['a','c'])

In [31]: d
Out[31]:
a     9
c    12
dtype: int64

# ndarry进行创建，后面的index是从9到6，步长为-1，则为9，8，7
In [36]: n = pd.Series(np.arange(3),index=np.arange(9,6,-1))

In [37]: n
Out[37]:
9    0
8    1
7    2
dtype: int32

```



# 3. Series类型的基本操作
Series是一维带“标签”数组，Series基本操作类似ndarray和字典，根据索引对齐。

## 3.1 获取Series的索引和数据

```python
In [47]: n.index
Out[47]: Index(['a', 'b', 'c'], dtype='object')

In [48]: n.values
Out[48]: array([0, 1, 2])

```

## 3.2 自动索引和自定义索引

```python
# 自定义索引
In [53]: n[['a','b']]
Out[53]:
a    0
b    1
dtype: int32

# 自定义索引
In [54]: n['a']
Out[54]: 0

# 自动索引
In [55]: n[[0,1]]
Out[55]:
a    0
b    1
dtype: int32

# 但是自动索引与自定义索引不能混用
In [56]: n[['a','b',0]]
Out[56]:
a    0.0
b    1.0
0    NaN
dtype: float64

# 是个迭代对象能切片
In [57]: n[:]
Out[57]:
a    0
b    1
c    2
dtype: int32

In [58]: n[:1]
Out[58]:
a    0
dtype: int32

```

```python
In [60]: b = pd.Series([9,8,7,6],['a','b','c','d'])
#
In [62]: b[b > b.median()]
Out[62]:
a    9
b    8
dtype: int64

In [63]: np.exp(b)
Out[63]:
a    8103.083928
b    2980.957987
c    1096.633158
d     403.428793
dtype: float64

# 能使用in判断
In [64]: 'c' in b
Out[64]: True

In [65]: 0 in b
Out[65]: False

# 能使用get方法，获取不到就返回默认值100
In [66]: b.get('b',100)
Out[66]: 8

In [67]: b.get('f',100)
Out[67]: 100
```

## 3.3 Series类型对齐操作
Series类型在运算中会自动对齐不同索引的数据

```python

In [69]: b = pd.Series([9,8,7,6],['a','b','c','d'])

In [70]: a = pd.Series([1,2,3],['b','c','e'])

In [71]: c = a + b

In [72]: c
Out[72]:
a    NaN
b    9.0
c    9.0
d    NaN
e    NaN
dtype: float64

```

## 3.4 Series类型的name属性

```python
In [73]: b.name='Series Object'

In [74]: b.index.name='index'

In [76]: b
Out[76]:
index
a    9
b    8
c    7
d    6
Name: Series Object, dtype: int64

```

## 3.5 Series类型的修改
Series对象可以随时修改并即 刻生效

```python
In [77]: b['a'] = 99

In [78]: b
Out[78]:
index
a    99
b     8
c     7
d     6
Name: Series Object, dtype: int64

```

# 4. Pandas库的DataFrame类型
DataFrame类型由共用相同索引的一组列组成。

|  索引   |       多列数据       |
|:------- |:-------------------- |
| index_0 | data_a data_1 data_x |
| index_1 | data_b data_2 data_y |

![image](https://user-images.githubusercontent.com/18595935/30697261-5037f9f0-9f19-11e7-8149-c1400fa4c7b6.png)

DataFrame是一个表格类型的数据类型，每列值类型可以不同，既有行索引，也有列索引。一般用来表示二维数据，也可以表示多维数据。

可以由如下数据类似创建:
- 二维ndarray
- 一维ndarray,列表，字典，元组或series构成的字典
- Series类型
- 其他DataFrame类型

```python

# 注意下面的out中，最左边和最上边都是index
In [79]: pd.DataFrame(np.arange(9).reshape(3,3))
Out[79]:
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8

# 通过一维ndarray对象字典创建
In [81]: dt = {'one':pd.Series([1,2,3],index=['a','b','c']),
    ...:        'two':pd.Series([9,8,7,6],index=['a','b','c','d'])}

In [82]: d = pd.DataFrame(dt)
# 注意哪个是行，哪个是列，另外数据会自动补齐
In [83]: d
Out[83]:
   one  two
a  1.0    9
b  2.0    8
c  3.0    7
d  NaN    6
```

```python

# 从列表类型的字典创建
In [85]: d1 = {'one':[1,2,3,4],'two':[9,8,7,6]}

In [86]: d = pd.DataFrame(d1)

In [87]: d
Out[87]:
   one  two
0    1    9
1    2    8
2    3    7
3    4    6

In [88]: d = pd.DataFrame(d1,index=['a','b','c','d'])

In [89]: d
Out[89]:
   one  two
a    1    9
b    2    8
c    3    7
d    4    6

```


```python
In [90]: d.index
Out[90]: Index(['a', 'b', 'c', 'd'], dtype='object')

In [92]: d.columns
Out[92]: Index(['one', 'two'], dtype='object')

In [91]: d.values
Out[91]:
array([[1, 9],
       [2, 8],
       [3, 7],
       [4, 6]], dtype=int64)
```

- 索引数据
```python
# 列索引去数据
In [101]: d['one']
Out[101]:
a    1
b    2
c    3
d    4
Name: one, dtype: int64

# 按行索引取数据
In [102]: d.loc['a']
Out[102]:
one    1
two    9
Name: a, dtype: int64
```

# 5. Pandas库的数据类型操作
如何改变Series和DataFrame对象？比如增加或重排等重新索引，或删除drop等。

```python
In [109]: d
Out[109]:
   one  two
a    1    9
b    2    8
c    3    7
d    4    6

# 重排列数据
In [110]: d = d.reindex(columns=['two','one'])

In [111]: d
Out[111]:
   two  one
a    9    1
b    8    2
c    7    3
d    6    4

# 重排行数据
In [112]: d = d.reindex(index=['b','c','a','d'])

In [113]: d
Out[113]:
   two  one
b    8    2
c    7    3
a    9    1
d    6    4

```

## 5.1 重新索引
.reindex(index=None,columns=None,...)的参数表如下:

|     参数      |                       说明                        |
|:------------- |:------------------------------------------------- |
| index,columns | 新的行列自定义索引                                |
| fill_value    | 重新索引中，用于填充缺失位置的值                  |
| method        | 填充方法，ffill为当前值向前填充，bfill为向后填充  |
| limit         | 最大填充量                                        |
| copy          | 默认为True，生成新的对象，False时，新旧相等不复制 |
|               |                                                   |

```python
In [114]: newc = d.columns.insert(2,'add-three')

In [115]: newd = d.reindex(columns=newc,fill_value=999)

In [116]: newd
Out[116]:
   two  one  add-three
b    8    2        999
c    7    3        999
a    9    1        999
d    6    4        999

In [117]: d
Out[117]:
   two  one
b    8    2
c    7    3
a    9    1
d    6    4

```

Series和DataFrame的索引是Index类型 `Index对象是不可修改类型`。



# 6. 索引类型的常用方法
- .append(idx) 连接另一个Index对象，产生新的Index对象
- .diff(idx)计算差集，产生新的Index对象
- .intersection(idx)计算交集
- .union(idx) 计算并集
- .delete(loc) 删除loc位置处的元素
- .insert(loc,e) 在loc位置增加一个元素e

```python
In [133]: d1 = {'one':[1,2,3,4],'two':[9,8,7,6]}

In [134]: d = pd.DataFrame(d1)

In [135]: d
Out[135]:
   one  two
0    1    9
1    2    8
2    3    7
3    4    6

In [136]: ni = d.index.drop(2)

In [137]: nc = d.columns.insert(2,'add-three')

In [138]: nd = d.reindex(index=ni,columns=nc,method='ffill')

In [139]: nd
Out[139]:
   one  two  add-three
0    1    9        NaN
1    2    8        NaN
3    4    6        NaN

```

- .drop()能够删除Series和DataFrame指定行或列索引

```python
In [140]: nd.drop(3)
Out[140]:
   one  two  add-three
0    1    9        NaN
1    2    8        NaN

In [141]: nd
Out[141]:
   one  two  add-three
0    1    9        NaN
1    2    8        NaN
3    4    6        NaN

In [143]: nd.drop('two',axis=1)
Out[143]:
   one  add-three
0    1        NaN
1    2        NaN
3    4        NaN

```



# 7. Pandas库的数据类型运算

算术运算根据行列索引，补齐后运算，运算默认产生浮点数，补齐时缺项填充NaN(空值)。
采用+ ‐ * /符号进行的二元运算产生新的对象。

## 7.1 数据类型的算术运算(1)

```python
In [149]: a = pd.DataFrame(np.arange(12).reshape(3,4))

In [150]: b = pd.DataFrame(np.arange(20).reshape(4,5))

In [151]: a
Out[151]:
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

In [152]: b
Out[152]:
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19

In [153]: a + b
Out[153]:
      0     1     2     3   4
0   0.0   2.0   4.0   6.0 NaN
1   9.0  11.0  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN

In [154]: a * b
Out[154]:
      0     1      2      3   4
0   0.0   1.0    4.0    9.0 NaN
1  20.0  30.0   42.0   56.0 NaN
2  80.0  99.0  120.0  143.0 NaN
3   NaN   NaN    NaN    NaN NaN
```

## 7.2 数据类型的算术运算(2)

|      方法       |      说明      |
|:--------------- |:-------------- |
| .add(d,**argws) | 类型间加法运算 |
| .sub(d,**argws) | 类型间减法运算 |
| .mul(d,**argws) | 类型间乘法运算 |
| .div(d,**argws) | 类型间除法运算 |


- fill_value参数替代NaN，替代后参与运算

```python

In [161]: a
Out[161]:
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

In [162]: b
Out[162]:
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19



In [159]: a.add(b,fill_value=10)
Out[159]:
      0     1     2     3     4
0   0.0   2.0   4.0   6.0  14.0
1   9.0  11.0  13.0  15.0  19.0
2  18.0  20.0  22.0  24.0  24.0
3  25.0  26.0  27.0  28.0  29.0

In [160]: a.mul(b,fill_value=10)
Out[160]:
       0      1      2      3      4
0    0.0    1.0    4.0    9.0   40.0
1   20.0   30.0   42.0   56.0   90.0
2   80.0   99.0  120.0  143.0  140.0
3  150.0  160.0  170.0  180.0  190.0


```

## 7.3 比较运算法则
比较运算只能比较相同索引的元素，不进行补齐。

```python
In [163]: b = pd.DataFrame(np.arange(20).reshape(4,5))

In [166]: a = pd.DataFrame(np.arange(40,0,-2).reshape(4,5))

In [167]: b
Out[167]:
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19

In [168]: a
Out[168]:
    0   1   2   3   4
0  40  38  36  34  32
1  30  28  26  24  22
2  20  18  16  14  12
3  10   8   6   4   2

In [169]: b > a
Out[169]:
       0      1      2      3      4
0  False  False  False  False  False
1  False  False  False  False  False
2  False  False  False  False   True
3   True   True   True   True   True

```


# 8. Pandas库入门小结
- Series = 索引 + 一维数据
- DataFrame = 行列索引 + 二维数据
- 理解数据类型与索引的关系，操作索引即操作数据
- 重新索引、数据删除、算术运算、比较运算
- 像对待单一数据一样对待Series和DataFrame对象
