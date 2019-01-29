---
layout: post
title: 【书】深度学习入门-04-神经网络的学习
date: 2018-07-28 00:00:04
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

上一章神经网络中，使用给定的权重和偏置，对一组数据集进行了预测，并计算了其预测精度，但是**其权重和偏置都是预先设定的**。

本章的主题是神经网络的学习，即**从训练数据中自动获取最优权重参数**，为了使神经网络能学习，将导入**损失函数**，以损失函数为基准，**找出能使它的值达到最小的权重**，为了找出尽可能小的损失函数的值，本章将介绍**利用函数斜率的梯度法**。

**本章的结构如下**:

![image](https://user-images.githubusercontent.com/18595935/51435403-26164800-1cba-11e9-9773-11809fc2fd70.png)

# 1. 从数据中学习

神经网络的特征就是可以从数据中学习，指**由数据自动决定权重参数的值**，在层数很深的深度学习中，参数的数量可能上亿，人工不可能决定这些参数。

- 没有人为介入的方块用灰色表示：

![image](https://user-images.githubusercontent.com/18595935/43674200-db87d594-980a-11e8-822e-c5e33d477a68.png)

上面展示了三类方式:

1. 第一类完全**人为确定算法**
2. 第二类通过**机器学习**的方式，先从图像中提取特征量，使用这些特征量将图像数据转换为向量，然后对转换后的向量使用机器学习的SVM,KNN等分类器进行学习。但是这些特征量仍然是人为设计，不同问题，需要使用合适的特征量，才能得到好的结果。
3. 第三类通过**神经网络**，连图像中包含的重要特征量都由机器来学习，神经网络都是通过不断学习所提供的数据，尝试发现待求解问题的模式。也就是说，与待处理的问题无关，神经网络可以将数据直接作为原始数据，进行端对端的学习。

## 1.1 训练数据和测试数据

机器学习中，一般将数据分为`训练数据(也叫监督数据)`和`测试数据`两部分来学习和实验:
- 首先通过**训练数据**进行学习，寻找最优的参数
- 然后使用**测试数据**评价训练得到模型的实际能力。

为了正确评价模型的泛化能力，必须划分为训练数据和测试数据，泛化能力指处理未被观察过的数据的能力。获得泛化能力是机器学习的最终目标。

因此仅仅用一个数据集去学习和评价参数，是无法正确评价的，这样会导致可以顺利处理某个数据集，而无法处理其他数据集，这种只对某个数据集过度拟合的状态称为**过拟合**(over fitting)。

# 2. 损失函数(lost function)

神经网络以某个指标为线索寻找最优权重参数，神经网络学习中所用指标称为`损失函数(loss function)`。
损失函数是表示神经网络性能`恶劣程度`的指标，即当前的神经网络对监督数据在多大程度上不拟合，在多大程度上不一致。
这个损失函数可以使用任意函数，但一般用**均方误差**和**交叉熵误差**。

## 2.1 均方误差(mean squared error)

公式如下,yk表示神经网络的输出，tk表示监督数据，k表示数据维度:

![image](https://user-images.githubusercontent.com/18595935/43674374-2ce09e82-980e-11e8-850a-0e9eba572360.png)

```python
import numpy as np

def mean_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2)
```

```python
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
y1 = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
y2 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]) 

error1 = mean_squared_error(y1,t)
error2 = mean_squared_error(y2,t)

print("error1:",error1)
print("error2:",error2)
```

输出如下:

```python
error1: 0.0975
error2: 0.5975
```

神经网络的输出是10个元素构成的数组，数组元素的索引从第一个开始依次对应数字的0,1,2,3...，这里神经网络的输出y是softmax函数的输出，softmax函数的输出可以理解为概率，因为y1中表示，为0的概率为0.1，为1的概率为0.05,以此类推。

- 将正确标签表示为1，其他标签表示为0的表示方法称为**one-hot表示**。
- 可以看到y1的均方误差更小，输出结果与监督数据更加吻合。

## 2.2 交叉熵误差(cross entropy error)-评价

除了上面的均方误差外，交叉熵误差经常被用作损失函数

![image](https://user-images.githubusercontent.com/18595935/51816392-b4697a00-2309-11e9-88c1-80b08906b54a.png)

yk是神经网络的输出，tk是正确的解标签。

k是预测值的个数(比如上面一个手写图片，结果可能为10个数，则k为10)，yk是第k个的计算结果，tk是第k个的标签即正确结果(0或1)。

```python
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta)) 

error1 = cross_entropy_error(y1,t)
error2 = cross_entropy_error(y2,t)

print("error1:",error1)
print("error2:",error2)
```

输出结果如下:

```python
error1: 0.510825457099
error2: 2.30258409299
```

上面的函数中使用了`delta`，因为如何值为0的话，会导致`np.log(0)`为负无穷大，导致后续无法计算，作为一种保护对策，添加一个微小值可以防止负无限大的发生。

上面的结果也表明，第一个y1是更正确的结果。

```python
import numpy as np
import matplotlib.pylab as plt

x = np.arange(0.00000001,10,0.1)
y = np.log(x)
plt.plot(x,y)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43674601-91506cd2-9811-11e8-9d4d-7edba5a716c5.png)

## 2.3 mini-batch学习

上面的例子只有一个数据(一个输入即一副图，通过该神经网络后的输出结果)，如果训练数据有100个的话，就要把这100个损失函数的总和作为学习指标:

![image](https://user-images.githubusercontent.com/18595935/43674656-9c1fb1a8-9812-11e8-9051-cc000f22f0ba.png)

假设数据有N个，tnk表示第n个数据的第k个元素的值(ynk是神经网络的输出，tnk是监督数据)。

```python
import sys, os 
sys.path.append(os.pardir) 
import numpy as np 
from dataset.mnist import load_mnist 

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True) 

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size,batch_size)

print(batch_mask)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
print("x_batch:",x_batch.shape," t_batch:",t_batch.shape)
```

输出如下:

```python
(60000, 784)
(60000, 10)
[59210 46466 37135 27478 28881 31931 13282 56623 51142   377]
x_batch: (10, 784)  t_batch: (10, 10)
```

- **x_train**:(60000, 784)，全部的输入信号
- **t_train**:(60000, 10)，全部的标签数据，10表示0-9出现的概率个数
- **x_batch**:随机选择的10个输入信号
- **t_batch**:随机选择的输入信号，其对应的标签数据

通过上面的方式，选取了10个数据，这10个数据随机选取，索引号见如上的输出。

```python
print(t_batch)
```

输出这10个数据的标签:

```python
[[ 0.  0.  0.  0.  1.  0.  0.  0.  0.  0.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.  0.  0.  0.]]
```



## 2.4 mini-batch版交叉熵误差的实现

- 单个数据交叉熵误差代码：

```python
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta)) 

```

- 改良一下之前的代码，下面的代码可以同时处理单个数据和批量数据

```python
def cross_entropy_error(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size 
```

1. 当是单个数据时，即y.ndim=1时，需要处理成二维的，其shape从(10,) 转换reshape成了(1, 10)。
2. batch_size即数据的第一维大小

## 2.5 为何要设定损失函数

神经网络的学习中，寻找最优参数(权重和偏置)时，要寻找使损失函数值尽可能小的参数，为了找到使损失函数尽可能小的地方，需要计算参数的导数(确切说是梯度)，然后以这个导数为指引，逐步更新参数的值。

假设有一个神经网络，对该神经网络中的权重参数的损失函数求导，表示的是**如果稍微改变这个权重参数的值，损失函数的值会如何变化**:

- 如果导数的值为负，通过使该权重参数向正方向改变，可以减小损失函数的值
- 如果导数的值为正，则通过使该权重参数向负方向改变，可以减小损失函数的值
- 如果导数的值为0，无论权重参数向哪个方向变化，损失函数的值都不会改变，此时该权重参数的更新会停在此处

在进行神经网络的学习时，不能将识别精度作为指标。因为如果以 识别精度为指标，则参数的导数在绝大多数地方都会变为0。 

- **为什么不能用识别精度作为指标？**

识别精度对微小的参数变化基本没有什么反应，即便有反应，它的值也是不连续的，突然的变化。

![image](https://user-images.githubusercontent.com/18595935/43675198-1777d3be-981b-11e8-82c8-047dd2c130c5.png)

# 3. 数值微分

## 3.1 导数

导数表示的是某个瞬间的变化率，可以定义为下面的式子:

![image](https://user-images.githubusercontent.com/18595935/43684732-6a90895e-98e0-11e8-93cf-41d694a31d1f.png)

```python
def numerical_diff(f,x):
    h = 10e-50
    return (f(x+h) - f(x)) / h
```

真的导数对应函数在x处的斜率(切线)，但上述实现中计算的导数对应的是(x+h)和x之间的斜率，因此，真的导数和上述得到的导数的值在严格意义上并不一致。

为了减少误差，我们可以计算函数f在x+h和x-h之间的差分，这种也叫做`中心差分`，上面的叫做`前向差分`。

函数改进之后:

```python
def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
```
- **数值微分**: 利用微小的差分求导数的过程
- **解析性求导**： 基于数学式的推导求导数的过程，比如 y=x**2导数，可以通过dy/dx = 2x解析性的求解，因此，当x=2时，y的导数为4

通过上面的函数，对`f(x) = 0.01*x**2 + 0.1*x`函数，在x=5和x=10处求导，结果为`0.1999999999990898`和 `0.2999999999986347`，解析求导是`0.02*x + 0.1`，结果为`0.2`和`0.3`。



## 3.2 数值微分的例子

先看下面的2次函数: `y=0.01x**2 +0.1x`，实现代码如下:

```python
# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x 


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
     
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf2 = tangent_line(function_1, 5)
y2 = tf2(x)

tf3 = tangent_line(function_1, 10)
y3 = tf3(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
```

图形如下:

![image](https://user-images.githubusercontent.com/18595935/43684896-e6cfce0a-98e3-11e8-8a5c-87706d673f9e.png)

注意上面的`tangent_line`函数返回的是一个lambda表达式。

- 蓝色曲线，表示function_1(x)函数
- 绿色曲线，表示在该函数在x为5的切线
- 黄色曲线，表示在该函数在x为10的切线


## 3.2 偏导数

上面的导数只有一个计算参数，下面有两个变量:

![image](https://user-images.githubusercontent.com/18595935/43684951-ee6df154-98e4-11e8-9cbf-7ffef4a0e3b1.png)

```python
def function_2(x):
    return x[0]**2 + x[1]**2
```

如果画一下这个函数的画像，结果如下:

![image](https://user-images.githubusercontent.com/18595935/43684996-bba8d03a-98e5-11e8-9035-afddf14daea3.png)

上面的函数有两个变量，所以有必要区分对哪个变量求导数，即对x0和x1两个变量中的哪一个求导数，对多个变量的函数求导称为`偏导数`，可以记为如下:

![image](https://user-images.githubusercontent.com/18595935/43685011-2c6c1c14-98e6-11e8-8dd5-78fe98c5c713.png)

偏导数和单变量的导数一样，都是求某个地方的斜率，不过偏导数需要将多个变量中的某一个变量定为目标变量，并将其他变量固定为某个值，得到一个新函数，然后对新定义的函数应用了之前的求数值微分的函数，得到偏导数。

比如下面，求解x0=3，x1=4时，x0的偏导数时，就是将x1的值代入函数，然后求解x0的普通导数。

多个变量，如两个变量的情况下，是一个三维图像，三维空间某个地点，求解在不同方向(x0或x1)上的切线斜率:

![image](https://user-images.githubusercontent.com/18595935/43685044-c4cefab2-98e6-11e8-863c-0d0146f76703.png)

# 4. 梯度(gradient)

将全部变量的偏导数汇总而成的向量称为**梯度**，可以用如下代码实现:

```python
def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x) # 生成一个形状和x相同、所有元素都为0的数组。
    
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        print("x + h :",x)
        print("fxh1 :",fxh1)
        
        #f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        print("x - h :",x)
        print("fxh2 :",fxh2)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
        print("------")
        
    return grad
```

```python
numerical_gradient(function_2, np.array([3.0, 4.0])) 
```

输出如下，可以看到循环计算x数组内的元素时，另一个元素是固定的值，当前求导数的值被加上了h(0.0001)：

```python
x + h : [ 3.0001  4.    ]
fxh1 : 25.00060001
x - h : [ 2.9999  4.    ]
fxh2 : 24.99940001
------
x + h : [ 3.      4.0001]
fxh1 : 25.00080001
x - h : [ 3.      3.9999]
fxh2 : 24.99920001
------
```

结果为`array([ 6.,  8.])`，为了更好的理解，我们把`f(x0+x1) = x0**2 + x1**2`的梯度画在图上，代码如下:

```python
# coding: utf-8
# cf.http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 还原值
        
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad


def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)


def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
     
if __name__ == '__main__':
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)
    
    X = X.flatten()
    Y = Y.flatten()
    
    grad = numerical_gradient(function_2, np.array([X, Y]) )
    
    plt.figure()
    plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43685194-8dff6910-98e9-11e8-91a5-c667ecf6cd96.png)

- 梯度指向函数f(x0,x1)的最低处(最小值)，离最低处越远，箭头越大。
- 上面仍是比较简单的case，实际上，梯度会指向各个点处的函数值降低的方向，更严格的讲，梯度指示的方向是各点处的函数值减小最多的方向。


## 4.1  梯度法

神经网络在学习时任务是**找到最优参数**，即使得损失函数取最小值时的**权重和偏置**。但是一般而言，损失函数很复杂，参数空间庞大，我们不知道它在何处能取得最小值，而通过巧妙地使用梯度来寻找函数最小值的方法就是**梯度法**。

梯度表示的是各点处的函数值减少最多的方向，因此无法保证梯度所指的方向就是函数的最小值或真正应该前进的方向，实际上在复杂的函数中，梯度指示的方向基本都不是函数值最小处。

在梯度法中，函数的取值从当前位置沿着梯度方向前进一定距离，然后在新的地方重新求梯度，再沿着新梯度方向前进，如此反复，不断沿着梯度方向前进，逐渐减少函数值的过程就是`梯度法(gradient method)`。

梯度法用数学式表示如下:

![image](https://user-images.githubusercontent.com/18595935/43685906-efeaa2e0-98f6-11e8-9cbb-b635c97cea68.png)

η表示更新量，在神经网络学习中，称为`学习率(learning rate)`,学习率决定在一次学习中，应该学习多少，以及多大程度上更新参数。
学习率不同于权重和偏置，后者可以通过机器学习得到，学习率必须要手动设定，一般会一边改变学习率的值，一边确认学习是否正确进行。

python的实现代码如下:

```python
def gradient_descent(f,init_x,lr=0.01,step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad
    
    return x
```

- `init_x`是初始值
- `lr`是学习率learning rate
- `step_num`是梯度法的重复次数
- `numerical_gradient(f,x)`会求函数的梯度，用该梯度乘以学习率得到的值进行更新，由`step_num`指定重复次数。

求函数梯度的代码如下：

```python
def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x) # 生成一个形状和x相同、所有元素都为0的数组。
    
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        print("x + h :",x)
        print("fxh1 :",fxh1)
        
        #f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        print("x - h :",x)
        print("fxh2 :",fxh2)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
        print("------")
        
    return grad
```

添加print后，可以看到每次更新后的值，输出部分如下：

```python

x + h : [-2.9999  4.    ]
fxh1 : 24.99940001
x - h : [-3.0001  4.    ]
fxh2 : 25.00060001
------
x + h : [-3.      4.0001]
fxh1 : 25.00080001
x - h : [-3.      3.9999]
fxh2 : 24.99920001
------
x + h : [-2.3999  3.2   ]
fxh1 : 15.99952001
x - h : [-2.4001  3.2   ]
fxh2 : 16.00048001
------
x + h : [-2.4     3.2001]
fxh1 : 16.00064001
x - h : [-2.4     3.1999]
fxh2 : 15.99936001

...

------
x + h : [  9.99992361e-05   1.01851799e-09]
fxh1 : 9.99984722392e-09
x - h : [ -1.00000764e-04   1.01851799e-09]
fxh2 : 1.00001527793e-08
------
x + h : [ -7.63888491e-10   1.00001019e-04]
fxh1 : 1.00002037052e-08
x - h : [ -7.63888491e-10  -9.99989815e-05]
fxh2 : 9.99979629802e-09
```

```python
def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0]) 
gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100) 
```

设定初始值为(-3,4),开始用梯度法寻找最小值，最终输出为`array([ -6.11110793e-10,   8.14814391e-10])`，非常接近(0,0)了，实际上，真的最小值就是(0,0)

在


- 下面用图来表示梯度法的更新过程，可以发现原点处是最低的地方，函数的取值在逐步逼近。

```python
# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
from gradient_2d import numerical_gradient


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])    

lr = 0.1
step_num = 20
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()

```

![image](https://user-images.githubusercontent.com/18595935/43686052-36e4af62-98fa-11e8-86c5-20cf63afaf8a.png)

上图可以看出，设定的初始值为(-3,4),开始使用梯度法寻找最小值，最终的结果为array([ -6.11110793e-10,   8.14814391e-10])，非常接近(0,0),所以说通过梯度法我们得到了正确结果。

**调整学习率：**

前面说过，学习率过大或者霍骁都无法得到好的结果：

- 学习率过大，会发散成一个很大的值：

```python
init_x = np.array([-3.0, 4.0])    

lr = 10
step_num = 20
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)
print(x)
```

```python
[ -2.58983747e+13  -1.29524862e+12]
```

- 学习率过小，基本上没怎么更新就结束了：

```python
init_x = np.array([-3.0, 4.0])    

lr = 1e-10
step_num = 20
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)
print(x)
```

```python
[-2.99999999  3.99999998]
```

> 像学习率这样的参数称为**超参数**，这是一种和神经网络参数(权重偏置)不同的参数，权重参数可以通过训练数据和学习算法自动获得，学习率这样的超参数则是人工设定的。


## 4.2 神经网络的梯度

神经网络也要求梯度，这里所说的梯度指损失函数关于权重函数的梯度。

![image](https://user-images.githubusercontent.com/18595935/43776678-834dd3fa-9a8b-11e8-8a1b-b37572403bb0.png)

下面以一个简单的神经网络为例，来实现求解梯度的代码:

### 4.2.1 一个简单的神经网络类

这里实现一个简单的神经网络的类，只有一个实例变量，即形状为2*3的权重参数

```python
import sys,os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax,cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)
        
    # 预测，将输入矩阵与权重矩阵做点积
    def predict(self,x):
        return np.dot(x,self.W)
    
    # 求损失值
    def loss(self,x,t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y,t)
        
        return loss
```

- `loss`函数，z是预测结果，softmax是激活函数，最后调用交叉熵误差函数，得到最终误差结果，相关函数如下:

```python
def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # 溢出对策
    return np.exp(x) / np.sum(np.exp(x))


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size    
```

### 4.2.2 使用上面的神经网络类

预测并根据标签计算损失值

```python
# 初始化神经网络
net = simpleNet()
print("1. net.W",net.W)

# 输入x，利用神经网络预测
x = np.array([0.6,0.9])
p = net.predict(x)
print("2. predict:",p)

# 得到最大的值的索引
idx = np.argmax(p)
print("3. index for max:",idx)

# 根据标签计算损失
t = np.array([0,0,1]) # 正确的标签
loss = net.loss(x,t)
print("4. loss:",loss)
```

输出结果如下:

```python
1. net.W [[ 0.16042481  0.89547429  3.01478025]
 [-1.68381034 -1.74616755  0.05227519]]
2. predict: [-1.41917443 -1.03426622  1.85591582]
3. index for max: 2
4. loss: 0.0892732979033
```

### 4.2.3 计算梯度

用两种方式，计算损失函数关于权重参数的梯度:

这里函数f(W)的参数W是一个伪参数，因为`numerical_gradient(f,x)`会在内部执行f(x)，为了与之兼容而定义了f(W).
`numerical_gradient(f,x)`的参数f是函数，x是传给函数f的参数，因此这里x取net.W，并定义一个计算损失函数的新函数f。

```python
def f(W):
    return net.loss(x,t)

dW = numerical_gradient(f,net.W)
print("5. dW:",dW)

# method2
f2 = lambda w:net.loss(x,t)
dW2 = numerical_gradient(f2,net.W)
print("6. dW2:",dW2)
```

输出结果如下:

```python
5. dW: [[ 0.02075041  0.0304923  -0.05124271]
 [ 0.03112561  0.04573845 -0.07686406]]
6. dW2: [[ 0.02075041  0.0304923  -0.05124271]
 [ 0.03112561  0.04573845 -0.07686406]]
```

上面dw的结果与W权重的形状一致，都是2*3的二维数组，观察上面dw的结果，第一行第一列为0.02，表示如果将w11增加h，那么损失函数值增加0.2h，负数则为减小。

> 参考:

```python
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)
```


# 5. 学习算法的实现

神经网络存在合适的权重和偏置，调整权重和偏置以便拟合训练数据的过程，成为`学习`，神经网络的学习如下图所示:

![image](https://user-images.githubusercontent.com/18595935/43780253-21e4b188-9a95-11e8-8b25-dc1cf505694e.png)

## 5.1 2层神经网络的类

上面第4节的只有一层神经网络，下面是一个二层神经网络的类

```python
import sys,os
sys.path.append(os.pardir)
from common.functions import *
from common.gradient import numerical_gradient

class TwoLayerNet:
    def __init__(self,input_size,hidden_size,output_size,weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * \
                            np.random.randn(input_size,hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * \
                            np.random.randn(hidden_size,output_size)
        self.params["b2"] = np.zeros(output_size)        
        
    
    def predict(self,x):
        W1,W2 = self.params["W1"], self.params["W2"]
        b1,b2 = self.params["b1"], self.params["b2"]
        
        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1,W2)
        y = softmax(a2)
        
        return y
    
    # x为输入数据，t为监督数据
    def loss(self,x,t):
        y = self.predict(x)
        
        return cross_entropy_error(y,t)
    
    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        t = np.argmax(t,axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        
        return accuracy
    
    
    # x输入数据，t为监督数据
    def numerical_gradient(self,x,t):
        loss_W = lambda W:self.loss(x,t)
        
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads
```

- TwolayerNet类中使用的变量

|变量|说明|
|:--|--:|
|params |保存神经网络的参数的字典性变量(实例变量) |
||W1/W2 分别表示第一层第二层的权重，b1/b2表示第一层第二层的偏置 |
|grads |保存梯度的字典性变量 |


- TwoLayerNet类的方法

|变量|说明|
|:--|--:|
|__init__(self, input_size, hidden_size, output_size) | 进行初始化，参数分别为输入层，隐藏层，输入层神经元数|
|predict(self, x) |进行识别，参数X是图像数据，即像素数据 |
|loss(self, x, t) |计算损失函数的值，参数x是图像数据，t是正确解标签，下同 |
|accuracy(self, x, t) |计算识别精度 |
|numerical_gradient(self, x, t) |计算权重参数的梯度 |

- 初始化一个神经网络，查看权重矩阵的维度

```python
net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10) 
print("W1:",net.params['W1'].shape)
print("b1:",net.params['b1'].shape)
print("W2:",net.params['W2'].shape)
print("b2:",net.params['b2'].shape)
```

输出如下，输入图像大小是784(28*28)，输出为10个类别:

```python
W1: (784, 100)
b1: (100,)
W2: (100, 10)
b2: (10,)
```

- 根据输入数据，计算梯度

```python
x = np.random.rand(100, 784) # 伪输入数据（100笔）
t = np.random.rand(100, 10)  # 伪正确解标签（100笔） 
grads = net.numerical_gradient(x, t)  # 计算梯度 

print("grads-W1:",grads['W1'].shape)
print("grads-b1:",grads['b1'].shape)
print("grads-W2:",grads['W2'].shape)
print("grads-b2:",grads['b2'].shape)
```

```python
grads-W1: (784, 100)
grads-b1: (100,)
grads-W2: (100, 10)
grads-b2: (10,)
```

## 5.2 mini-batch的实现

从训练数据中随机选择一部分数据，再以这些mini-batch为对象，使用梯度法更新参数的过程，这里mini-batch大小100，需要每次从60000个训练数据中随机取100个数据(图像数据和正确解标签数据)，然后对着100笔数据求梯度，使用随机梯度下降法SGD更新参数。

另外，梯度法的更新次数是1000，每更新一次都对训练数据计算损失函数的值，并把该值添加到数组中。


```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# 读入数据
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 1000  # 适当设定循环的次数
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 计算梯度
    grad = network.numerical_gradient(x_batch, t_batch) # 数值微分法
    #grad = network.gradient(x_batch, t_batch) # 反向传播法
    
    # 更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    # 记录学习过程
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    

# 绘制图形
markers = {'train': 'o', 'test': 's'}
x = np.arange(iters_num)
plt.plot(x, train_loss_list)
plt.xlabel("loss")
plt.ylabel("iteration")
plt.ylim(0, 5)
plt.show()
```


![image](https://user-images.githubusercontent.com/18595935/43807609-371e80a2-9ae4-11e8-99bf-3007183e35e9.png)

可以发现随着学习的进行，损失函数的值在不断减小。这是学习正常进行的信号，表示神经网络的权重参数在逐渐拟合数据。也就是 说，神经网络的确在学习！通过反复地向它浇灌（输入）数据，神经网络正在逐渐向最优参数靠近。

## 5.3 基于测试数据的评价

神经网络的学习中，必须确认是否能够识别训练数据以外的其他数据，即确认是否会发生过拟合。神经网络学习的最终目标是掌握泛化能力，要评价神经网络的泛化能力，就必须使用不包含在训练数据中的数据，下面的代码在进行学习过程中，会定期对训练数据和测试数据记录识别精度，这里每经过一个epoch，都会记录下训练数据和测试数据的识别精度。

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# 读入数据
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000  # 适当设定循环的次数
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 计算梯度,这里使用数值微分法
    grad = network.numerical_gradient(x_batch, t_batch) # 数值微分法
    #grad = network.gradient(x_batch, t_batch) # 反向传播法
    
    # 更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

# 绘制图形
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
```

输出如下:

```python
0.1043 , 0.1041
0.904633333333 , 0.9079
0.921 , 0.9236
0.9321 , 0.9338
0.9436 , 0.9426
0.95025 , 0.9494
0.956133333333 , 0.9531
0.960166666667 , 0.9564
0.9638 , 0.959
0.965933333333 , 0.9607
0.9682 , 0.9619
0.970266666667 , 0.9621
0.97075 , 0.9641
0.973583333333 , 0.9669
0.974083333333 , 0.9663
0.975666666667 , 0.9664
0.9777 , 0.9683
```

![image](https://user-images.githubusercontent.com/18595935/51892759-36c76c00-23e6-11e9-9a50-3d26f3242b75.png)

# 6. 小结

本章介绍了神经网络的学习，为了能顺利进行神经网络的学习，导入了损失函数这个指标，以这个损失函数为基准，找出使它的值达到最小的权重参数，就是神经网络学习的目标，为了找到尽可能小的损失函数值，我们使用函数斜率的梯度法。

- 机器学习使用的数据集分为训练数据和测试数据
- 神经网络用训练数据进行学习，并用测试数据评价学习到的模型的泛化能力
- 神经网络的学习以损失函数为指标，更新权重参数，以使损失函数的值减少
- 利用某个给定的微小值的差分求导数的过程，称为数值微分
- 利用数值微分，可以计算权重参数的梯度
- 数据微分虽然费时间，但是实现简单