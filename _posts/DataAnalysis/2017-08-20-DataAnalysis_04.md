---
layout: post
title: PythonDataAnalysis-03-图像的手绘效果
date: 2017-08-19 20:47:59
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
 - 单元9：**实战**：房价趋势的关联因素分析
 - 单元10：Pandas数据清洗和规约：数据清洗、缺失值处理、属性规约、主成分分析
 - 单元11：Pandas时序数据处理与展示
 - 单元12：**实战**：股票数据的趋势分析曲线

---

# 1. 图像的数组表示
图像一般使用RGB色彩模式，即每个像素点的颜色由红(R)、绿(G)、蓝(B)组成。
RGB三个颜色通道的变化和叠加得到各种颜色，其中
- R 红色，取值范围，0‐255
- G 绿色，取值范围，0‐255
- B 蓝色，取值范围，0‐255

RGB形成的颜色包括了人类视力所能感知的所有颜色。

## 1.1 PIL库
PIL， Python Image Library，PIL库是一个具有强大图像处理能力的第三方库。
在命令行下的安装方法： `pip install pillow`。

- from PIL import Image ，Image是PIL库中代表一个图像的类（对象）

![image](https://user-images.githubusercontent.com/18595935/30544707-5e9fe84e-9cc2-11e7-8a6f-d3aebea7226a.png)
图像是一个由像素组成的二维矩阵，每个元素是一个RGB值。

```python
In [102]: from PIL import Image

In [103]: import numpy as np

In [104]: im = np.array(Image.open('01.jpg'))

In [105]: print(im.shape,im.dtype)
(372, 672, 3) uint8
```
图像是一个三维数组，维度分别是高度、宽度和像素RGB值。

```python
In [135]: a
Out[135]:
array([[[160, 193, 228],
        ...,
        [239, 235, 226]]], dtype=uint8)
```

# 2. 图像的变换：

```python
In [123]: a = np.array(Image.open('01.jpg').convert('L'))

In [124]: a.shape
Out[124]: (372, 672)

In [125]: b = 255-a

In [126]: im = Image.fromarray(b.astype('uint8'))

In [127]: im.save('03.jpeg')

In [128]: im = Image.fromarray(a.astype('uint8'))

In [129]: im.save('04.jpeg')

```
下面分别是1,2,3,4处理后的图片
- 1是原始图片
- 2是RGB取补后的图片
- 3是处理成灰度后取补的图片
- 4是处理成灰度后的图片

![image](https://user-images.githubusercontent.com/18595935/30545610-17762df4-9cc5-11e7-82ca-b801d6839d96.png)


通过对RGB值二维数组的处理，可以实现更多的图像处理。


# 3. 手绘效果示例分析
手绘效果的几个特征：黑白灰色 / 边界线条较重 / 相同或相近色彩趋于白色 / 略有光源效果


```python
from PIL import Image
import numpy as np

a = np.asarray(Image.open('01.jpg').convert('L')).astype('float')

depth = 10.                      # (0-100)
grad = np.gradient(a)             #取图像灰度的梯度值
grad_x, grad_y = grad               #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
vec_az = np.pi/4.                    # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
dz = np.sin(vec_el)              #光源对z 轴的影响

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))  #重构图像
im.save('01-1.jpg')

```

实现效果如下:

![image](https://user-images.githubusercontent.com/18595935/30546478-acd36d1a-9cc7-11e7-8d02-0be897b1f426.png)

## 3.1 代码解析 - 梯度的重构
利用像素之间的梯度值和虚拟深度值对图像进行重构，根据灰度变化来模拟人类视觉的远近程度 。

```python
depth = 10.                      # 预设深度值为10 取值范围0‐100
grad = np.gradient(a)             #取图像灰度的梯度值
grad_x, grad_y = grad               #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.  # 根据深度调整x和y方向的梯度值

```

## 3.2 代码解析 - 光源效果
根据灰度变化来模拟人类视觉的远近程度。

![image](https://user-images.githubusercontent.com/18595935/30546861-bde43dcc-9cc8-11e7-9e82-fefb546a90a8.png)

```python
vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
vec_az = np.pi/4.                    # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
dz = np.sin(vec_el)              #光源对z 轴的影响

```

- np.cos(vec_el)为单位光线在地平面上的投影长度
- dx, dy, dz是光源对x/y/z三方向的影响程度


## 3.3 代码解析 - 梯度归一化

```python
# 构造x和y轴梯度的三维归一化单位坐标系
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

# 梯度与光源相互作用，将梯度转化为灰度
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
```

## 3.4 代码解析 - 图像生成

```python
# 为避免数据越界，将生成的灰度值裁剪至0‐255区间
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))  #重构图像
im.save('01-1.jpg')
```

> 上面代码还是不够理解，只知道应用了梯度等概念。详细的应该在计算机图形学中去了解。
