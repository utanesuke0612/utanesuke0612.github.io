---
layout: post
title: 深度学习入门-04-神经网络的学习
date: 2018-07-28 00:00:04
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

上一章神经网络中，使用给定的权重和偏置，对一组数据集进行了预测，并计算了其预测精度，但是其权重和偏置都是预先设定的。
本章的主题是神经网络的学习，即从训练数据中自动获取最优权重参数，为了使神经网络能学习，将导入损失函数，以损失函数为基准，找出能使它的值达到最小的权重，为了找出尽可能小的损失函数的值，本章将介绍利用函数斜率的梯度法。

# 1. 从数据中学习

神经网络的特征就是可以从数据中学习，指由数据自动决定权重，在层数很深的深度学习中，参数的数量可能上亿，人工不可能决定这些参数。

- 没有人为介入的方块用灰色表示：

![image](https://user-images.githubusercontent.com/18595935/43674200-db87d594-980a-11e8-822e-c5e33d477a68.png)

上面展示了三类方式:

1. 第一类完全人为确定算法
2. 第二类通过机器学习的方式，先从图像中提取特征量，使用这些特征量将图像数据转换为向量，然后对转换后的向量使用机器学习的SVM,KNN等分类器进行学习。但是这些特征量仍然是人为设计，不同问题，需要使用合适的特征量，才能得到好的结果。
3. 第三类通过神经网络，连图像中包含的重要特征量都由机器来学习，神经网络都是通过不断学习所提供的数据，尝试发现待求解问题的模式。也就是说，与待处理的问题无关，神经网络可以将数据直接作为原始数据，进行端对端的学习。

## 1.1 训练数据和测试数据

机器学习中，一般将数据分为`训练数据(也叫监督数据)`和`测试数据`两部分来学习和实验，首先通过训练数据进行学习，寻找最优的参数，然后使用测试数据评价训练得到模型的实际能力。

为了正确评价模型的泛华能力，必须划分为训练数据和测试数据，泛华能力指处理未被观察过的数据的能力。获得泛华能力是机器学习的最终目标。

因此仅仅用一个数据集去学习和评价参数，是无法正确评价的，这样会导致可以顺利处理某个数据集，而无法处理其他数据集，这种只对某个数据集过度拟合的状态称为**过拟合**(over fitting)。

# 2. 损失函数(lost function)

神经网络以某个指标为线索寻找最优权重参数，神经网络学习中所用指标称为`损失函数(loss function)`，损失函数是表示神经网络性能`恶劣程度`的指标，即当前的神经网络对监督数据在多大程度上不拟合，在多大程度上不一致。这个损失函数可以使用任意函数，但一般用均方误差和交叉熵误差。

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

- 上面的t，类似之前手写数据集的标签，即one-hot编码数据，0-9共10个数据，用1表示正确的标签数据。
- 可以看到y1的均方误差更小，输出结果与监督数据更加吻合。

## 2.2 交叉熵误差(cross entropy error)

除了上面的均方误差外，交叉熵误差经常被用作损失函数

![image](https://user-images.githubusercontent.com/18595935/43674498-fdb53ddc-980f-11e8-99f5-69240fca0ad1.png)

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

上面的例子只有一个数据，如果训练数据有100个的话，就要把这100个损失函数的总和作为学习指标:

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

通过上面的方式，选取了10个数据，这10个数据随机选取，索引号见如上的输出。

## 2.4 mini-batch版交叉熵误差的实现

```python
def cross_entropy_error(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,t.size)
    
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size 
```

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
        
        #f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
    return grad
```

```python
numerical_gradient(function_2, np.array([3.0, 4.0])) 
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

神经网络在学习时任务时找到最优参数，即使损失函数取最小值时的权重和偏置。但是一般而言，损失函数很复杂，参数空间庞大，我们不知道它在何处能取得最小值，而通过巧妙地使用梯度来寻找函数最小值的方法就是**梯度法**。

梯度表示的是各点处的函数值减少最多的方向，因此无法保证梯度所指的方向就是函数的最小值或真正应该前进的方向，实际上在复杂的函数中，梯度指示的方向基本都不是函数值最小处。

在梯度法中，函数的取值从当前位置沿着梯度方向前进一定距离，然后在新的地方重新求梯度，再沿着新梯度方向前进，如此反复，不断沿着梯度方向前进，逐渐减少函数值的过程就是`梯度法(gradient method)`。

梯度法用数学式表示如下:

![image](https://user-images.githubusercontent.com/18595935/43685906-efeaa2e0-98f6-11e8-9cbb-b635c97cea68.png)

η表示更新量，在神经网络学习中，称为`学习率(learning rate)`,学习率决定在一次学习中，应该学习多少，以及多大程度上更新参数。
学习率不同于权重和偏置可以通过机器学习得到，学习率必须要手动设定，一般会一边改变学习率的值，一边确认学习是否正确进行。

python的实现代码如下:

```python
def gradient_descent(f,init_x,lr=0.01,step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad
    
    return x
```

`init_x`是初始值，`lr`是学习率learning rate，`step_num`是梯度法的重复次数，`numerical_gradient(f,x)`会求函数的梯度，用该梯度乘以学习率得到的值进行更新，由`step_num`指定重复次数。

```python
def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0]) 
gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100) 
```

设定初始值为(-3,4),开始用梯度法寻找最小值，最终输出为`array([ -6.11110793e-10,   8.14814391e-10])`，非常接近(0,0)了，实际上，真的最小值就是(0,0)


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

## 4.2 神经网络的梯度




# 5. 学习算法的实现