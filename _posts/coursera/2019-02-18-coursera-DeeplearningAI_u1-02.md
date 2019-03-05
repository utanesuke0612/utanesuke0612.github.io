---
layout: post
title: Coursera-DeepLearning-U1-02-神经网络基础
date: 2019-02-18 01:02:00
categories: DeepLearning
tags: DeepLearning Coursera
---
* content
{:toc}

# 0. 小结

# 1. 二元分类

二元分类问题中，结果是一个离散的值，比如肿瘤是良性还是恶性。
比如下图中，通过输入图片数据，得到结果：是猫还是不是猫：

![image](https://user-images.githubusercontent.com/18595935/53550028-1a4f5880-3b79-11e9-937e-48cacdabcf3e.png)

- 图片通过三个独自的矩阵存储，分别代表红蓝绿三个颜色通道。
- 三个矩阵有相同的size，比如如果分辨率是64×64的，那么矩阵就是64×64大小

将图片像素值展开存储在x中，其维度为64×64×3 = 12288，nx=12288表示输入特征向量的维度：

![image](https://user-images.githubusercontent.com/18595935/53550421-ff311880-3b79-11e9-9204-aa4be528d19b.png)

在二元分类问题中，我们的目标是学习到这样一个分类器，输入一副以特征向量x表示的图像，预测对应的结果是0或1.

# 2. 逻辑回归

逻辑回归是一种应用在监督学习中的学习算法，其输出结果y是0或1，逻辑回归的目的就是最小化预测与训练数据之间的差。

比如下面通过给定特征向量x，通过算法计算其为猫的概率：

![image](https://user-images.githubusercontent.com/18595935/53551300-4f10df00-3b7c-11e9-8bfe-872c18fe6fa5.png)

最终的结果通过一个线性函数 y = w(T)*x + b(w是权重，b是偏置)，但是需要的是0到1的概率，所以要用sigmoid函数进行处理：

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

# 3. 逻辑回归代价函数

为了优化逻辑回归模型的参数w和b，需要定义一个代价函数：

我们希望找到使预测结果y^与实际标签y尽可能相等的w和b。

![image](https://user-images.githubusercontent.com/18595935/53552074-e9bded80-3b7d-11e9-8ce9-4a18a1f91c1e.png)

**损失函数：**针对单个数据集

损失函数衡量某个数据集(这里是x(i))，其预测结果与理想结果的偏离：

下面的两个损失函数，分别是均方误差和交叉熵误差函数，其代码和公式如下：

![image](https://user-images.githubusercontent.com/18595935/53552109-f6424600-3b7d-11e9-9894-e5a68de55a2e.png)

```python
def mean_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2)
```

```python
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta)) 
```

损失函数适用于像这样单一的优化示例，反映的是其参数成本。

**代价函数：**针对所有数据集

代价函数，是整个训练数据集上，损失函数结果的平均值，我们要找到合适的参数w和b，使得代价函数值最小。

![image](https://user-images.githubusercontent.com/18595935/53552122-fe9a8100-3b7d-11e9-910c-8118955c642e.png)

# 4. 梯度下降

上面讲解了如何衡量参数的好坏，下面介绍如何通过梯度下降训练和学习参数w和b。

先总结下，通过J(w,b)即代价函数可以反映w和b在训练集上的效果，简化如下面的曲面图，就是找到使J(w,b)最小的那个点(w,b)，这里J(w,b)是一个凸函数，像一个碗一样，有一个最优解。
另一种波浪线的，它是非凸的，并且有很多不同的局部最优。

因此，成本函数J(w,b)，之所以被定义为凸函数，一个重要原因是我们使用对于逻辑回归这个特殊代价函数J造成的。

![image](https://user-images.githubusercontent.com/18595935/53553590-5ab2d480-3b81-11e9-95ed-1d25f4b5caf8.png)

为了找到最优的参数，我们将会用一些初始值来初始化w和b，通常用0或随机初始化。因为这里函数是凸函数，无论在哪里初始化，应该到达同一个点。

1. 梯度下降法以初始点开始，然后朝最陡的下坡方向走一步
2. 上面的步骤多次跌打后，就能收敛到全局最优值

下面用一个简化后的一维曲线来描述梯度下降：

![image](https://user-images.githubusercontent.com/18595935/53553604-63a3a600-3b81-11e9-9875-309a2ffb8f46.png)

1. 重复执行更新权值w的操作，在算法收敛之前进行迭代更新。
2. 上图右上角的公式，α表示学习率，学习率可以控制我们每一次迭代中的步长大小。
3. dJ(w)/dw，表示w的导数，导数的含义，是函数J(w)在这个点w上的斜率，即相切于J(w)处的斜率
4. `w = w - α*dw` 上图中，因为斜率为正，所以更新后的w变小，即朝向左方移动，至到收敛到最低处

# 5. 求导

导数就是函数的斜率，如果该函数是线性函数，那么斜率不会随x的位置变化而变化，如果该函数是非线性函数，则需要考虑x所在位置。

![image](https://user-images.githubusercontent.com/18595935/53570907-f147bb80-3baa-11e9-8a2a-d23cbf71414b.png)

如上图导数就是3，表示a无论增加多少，y的值都是增加3倍。

# 6. 更多求导的例子

上面是线性函数例子，下面看一个非线性例子，我们说f(a)的斜率即f(a)在a=2的导数，这里f(a)=a××2的导数为2a：

![image](https://user-images.githubusercontent.com/18595935/53571193-a4181980-3bab-11e9-80ee-4c65a95443d6.png)

![image](https://user-images.githubusercontent.com/18595935/53571215-b003db80-3bab-11e9-8993-83360c15bcd0.png)

1. 函数的导数，就是函数的斜率，函数的斜率在函数不同的取值处，可能不同。
2. 如果要查找一个函数的导数，可以google一下得到这个函数的导数公式。

# 7. 计算图

可以参考[第一部分计算图](http://road2ai.info/2018/07/28/Deeplearning_05/)

神经网络的计算过程，通过正向传播来进行前向计算，计算神经网络的输出；通过反向传播计算梯度或导数。

![image](https://user-images.githubusercontent.com/18595935/53572626-07577b00-3baf-11e9-9db8-a6448840aaec.png)

# 8. 计算图求导

与上面类似，使用链式法则，某个值如b或c改变后，对J的影响有多大，这个影响通过链式法则可以传递：

![image](https://user-images.githubusercontent.com/18595935/53621685-a6758480-3c3a-11e9-8fd7-64b40e305d0f.png)

# 9. 逻辑回归梯度下降

介绍在实现逻辑回归时，如何计算导数来实现梯度下降。

![image](https://user-images.githubusercontent.com/18595935/53621940-94481600-3c3b-11e9-9ea9-07b7d7bcbe42.png)

- y是sigmoid函数求出的概率
- L(a,y)即损失函数，这里就是要修改参数w和b来减少损失函数

现在介绍如何反向计算导数：

![image](https://user-images.githubusercontent.com/18595935/53623235-ce1b1b80-3c3f-11e9-91ec-ab4464a71f9e.png)

注意上面da/dz 等于 a(1-a)是因为这里激活函数是sigmoid函数，故其导数为`a(1-a)`。最后使用求得的导数，去逐步更新权重w和偏置b。

# 10. 梯度下降例子(多个训练数据)

上面介绍了一个训练数据的导数，下面是m个训练数据的导数：
1. 执行m次循环，分别计算各个权重和偏置的导数
2. 将m次求得的导数累加
3. 将累加的导数求平均值
4. 最后用平均值去更新权值

上面就是训练数据的batch处理，但是上面会涉及到两次for循环，会影响计算速度，通过python中的vectorization(向量化)化可以加快计算速度。

![image](https://user-images.githubusercontent.com/18595935/53735088-3df00700-3ec9-11e9-99a6-3814ce14bf10.png)

# 11. 向量化

深度学习中涉及到大量的计算，如下图，左边是普通的for循环，右边是通过numpy实现的向量化运算，通过向量化运算能充分发挥CPU等的并行计算特性。

![image](https://user-images.githubusercontent.com/18595935/53735603-b4d9cf80-3eca-11e9-9482-a15931e9e28a.png)

```python
import time

a = np.random.rand(100000000)
b = np.random.rand(100000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("vectorizaed version:" + str(1000*(toc-tic)) + "ms")

c = 0
tic = time.time()
for i in range(100000000):
    c += a[i] * b[i]
toc = time.time()

print(c)
print("non-vectorizaed version:" + str(1000*(toc-tic)) + "ms")

```


输出：

```
24997247.2444
vectorizaed version:137.09306716918945ms
24997247.2444
non-vectorizaed version:54061.56229972839ms
```

上面的结果可以看到，向量化版本，比普通版提高了速度300多倍。

**原则就是：尽量不要用 for 进行循环计算！**

# 12. 向量化示例

如下图中，u是向量A和v的乘积，左边是for循环版本，右边是向量化版本，其指数运算也是类似：

![image](https://user-images.githubusercontent.com/18595935/53736825-2ebf8800-3ece-11e9-9fe9-077ab3ced185.png)

下面将m个训练数据求导数的做法，用向量化的方式实现：
![image](https://user-images.githubusercontent.com/18595935/53736844-3b43e080-3ece-11e9-890c-1797127b7a84.png)


# 13. 逻辑回归向量化

- X是一个矩阵，行数为nx，即单个训练数据中输入元素的个数; 列数为m，即m个训练数据。
- Z是z1,z2,...zm的乘积，通过python的广播，可以写成公式`Z = np.dot(w.T,x) + b`

![image](https://user-images.githubusercontent.com/18595935/53737404-ca052d00-3ecf-11e9-9158-37fab4a20d03.png)

# 14. 逻辑回归梯度输出

![image](https://user-images.githubusercontent.com/18595935/53737448-e99c5580-3ecf-11e9-9589-17aeba9513f0.png)
![image](https://user-images.githubusercontent.com/18595935/53737470-f620ae00-3ecf-11e9-99c4-13f90839bc48.png)

# 15. python中的广播

![image](https://user-images.githubusercontent.com/18595935/53775264-39613800-3f35-11e9-9c25-d9d4cdcf9159.png)

```python
import numpy as np

A = np.array([[56.0,0.0,4.4,68.0],
             [1.2,104.0,52.0,8.0],
             [1.8,135.0,99.0,0.9]])

print(A)
```

```
[[  56.     0.     4.4   68. ]
 [   1.2  104.    52.     8. ]
 [   1.8  135.    99.     0.9]]
```

```python
cal = A.sum(axis=0)
print(cal)
```

```
[  59.   239.   155.4   76.9]
```

```python
percentage = 100*(A/cal.reshape(1,4))
print(percentage)
```

```
[[ 94.91525424   0.           2.83140283  88.42652796]
 [  2.03389831  43.51464435  33.46203346  10.40312094]
 [  3.05084746  56.48535565  63.70656371   1.17035111]]
```

![image](https://user-images.githubusercontent.com/18595935/53775278-47af5400-3f35-11e9-9381-9e86df31a942.png)

```python
B = np.array([1,2,3,4])
C = np.array(100)

print(B+C)
```

```
[101 102 103 104]
```

```python
D = np.array([[1,2,3],
             [4,5,6]])
E = np.array([100,200,300])

print(D+E)

F = np.array([[100],
             [200]])
print(D+F)
```

```
[[101 202 303]
 [104 205 306]]
[[101 102 103]
 [204 205 206]]
```

- **General Principe：**

![image](https://user-images.githubusercontent.com/18595935/53775284-4f6ef880-3f35-11e9-99ef-398693a8811c.png)

# 16. python和numpy中的vector

一些python的tips：

```python
import numpy as np
a = np.random.rand(5)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a,a))
```

```
[ 0.31682703  0.98449876  0.507501    0.17019278  0.32181775]
(5,)
[ 0.31682703  0.98449876  0.507501    0.17019278  0.32181775]
1.45970668077
```

建议在编写神经网络时，不要使用上述的数据结构，形如(5,)或(n,)这样秩为1的数组。

下面的方式，可以使a称为一个5×1的列向量：

```python
a = np.random.randn(5,1)  # 5行1列
print(a)
print(a.shape)
print(a.T)
print(a.T.shape)
print(np.dot(a,a.T))
```

```
[[ 0.95921552]
 [-1.03511353]
 [ 1.06840642]
 [ 0.64497186]
 [ 0.44434781]]
(5, 1)
[[ 0.95921552 -1.03511353  1.06840642  0.64497186  0.44434781]]
(1, 5)
[[ 0.92009441 -0.99289696  1.02483202  0.61866702  0.42622531]
 [-0.99289696  1.07146003 -1.10592195 -0.66761911 -0.45995043]
 [ 1.02483202 -1.10592195  1.14149229  0.68909208  0.47474405]
 [ 0.61866702 -0.66761911  0.68909208  0.41598871  0.28659183]
 [ 0.42622531 -0.45995043  0.47474405  0.28659183  0.19744497]]
```

![image](https://user-images.githubusercontent.com/18595935/53776783-77ad2600-3f3a-11e9-8598-c1362549f199.png)

1. 不要使用秩为1的数组
2. 使用1×n或n×1的向量来代替
3. 使用reshape来确保矩阵和向量是所需要的维度
4. 通过断言assert来复查矩阵的维度

# 17. 如何使用Phthon notebooks

# 18. 逻辑回归成本函数

这里解释为什么我们在逻辑回归里使用代价函数

# 练习1：Python Basics with numpy (optional)

- Learn how to use numpy.
- Implement some basic core deep learning functions such as the softmax, sigmoid, dsigmoid, etc...
- Learn how to handle data by normalizing inputs and reshaping images.
- Recognize the importance of vectorization.
- Understand how python broadcasting works.

Welcome to your first assignment. This exercise gives you a brief introduction to Python. Even if you've used Python before, this will help familiarize you with functions we'll need.  

**Instructions:**
- You will be using Python 3.
- Avoid using for-loops and while-loops, unless you are explicitly told to do so.
- Do not modify the (# GRADED FUNCTION [function name]) comment in some cells. Your work would not be graded if you change this. Each cell containing that comment should only contain one function.
- After coding your function, run the cell right below it to check if your result is correct.

**After this assignment you will:**
- Be able to use iPython Notebooks
- Be able to use numpy functions and numpy matrix/vector operations
- Understand the concept of "broadcasting"
- Be able to vectorize code

Let's get started!

## 1 - Building basic functions with numpy ##

Numpy is the main package for scientific computing in Python. It is maintained by a large community (www.numpy.org). In this exercise you will learn several key numpy functions such as np.exp, np.log, and np.reshape. You will need to know how to use these functions for future assignments.

### 1.1 - sigmoid function, np.exp() ###

Before using np.exp(), you will use math.exp() to implement the sigmoid function. You will then see why np.exp() is preferable to math.exp().

**Exercise**: Build a function that returns the sigmoid of a real number x. Use math.exp(x) for the exponential function.

```python
# GRADED FUNCTION: basic_sigmoid

import math

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + math.exp(-x))
    ### END CODE HERE ###
    
    return s
```

```python
basic_sigmoid(3)
```

输出`0.9525741268224334`

Actually, we rarely use the "math" library in deep learning because the inputs of the functions are real numbers. In deep learning we mostly use matrices and vectors. This is why numpy is more useful. 

```python
import numpy as np

# example of np.exp
x = np.array([1, 2, 3])
print(np.exp(x)) # result is (exp(1), exp(2), exp(3))
```

输出`[  2.71828183   7.3890561   20.08553692]`

```python
# example of vector operation
x = np.array([1, 2, 3])
print (x + 3)
```

输出`[4 5 6]`

**Exercise**: Implement the sigmoid function using numpy. 

![image](https://user-images.githubusercontent.com/18595935/53780472-070d0600-3f48-11e9-9ac7-4e352eae13d8.png)

```python
# GRADED FUNCTION: sigmoid

import numpy as np # this means you can access numpy functions by writing np.function() instead of numpy.function()

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = s = 1 / (1 + np.exp(-x))
    ### END CODE HERE ###
    
    return s

x = np.array([1, 2, 3])
sigmoid(x)
```

```
array([ 0.73105858,  0.88079708,  0.95257413])
```

### 1.2 - Sigmoid gradient

As you've seen in lecture, you will need to compute gradients to optimize loss functions using backpropagation. Let's code your first gradient function.

![image](https://user-images.githubusercontent.com/18595935/53780525-391e6800-3f48-11e9-8f2d-a89c48d12c3c.png)

```python
# GRADED FUNCTION: sigmoid_derivative

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    s = sigmoid(x)
    ds = s*(1-s)
    ### END CODE HERE ###
    
    return ds
```

```python
x = np.array([1, 2, 3])
print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))
```

```
sigmoid_derivative(x) = [ 0.19661193  0.10499359  0.04517666]
```

### 1.3 - Reshaping arrays ###

Two common numpy functions used in deep learning are [np.shape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html) and [np.reshape()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html). 
- X.shape is used to get the shape (dimension) of a matrix/vector X. 
- X.reshape(...) is used to reshape X into some other dimension. 

![image](https://user-images.githubusercontent.com/18595935/53780645-b3e78300-3f48-11e9-8b8c-aa50053f4b0b.png)

**Exercise**: Implement `image2vector()` that takes an input of shape (length, height, 3) and returns a vector of shape (length\*height\*3, 1). For example, if you would like to reshape an array v of shape (a, b, c) into a vector of shape (a*b,c) you would do:
``` python
v = v.reshape((v.shape[0]*v.shape[1], v.shape[2])) # v.shape[0] = a ; v.shape[1] = b ; v.shape[2] = c
```
- Please don't hardcode the dimensions of image as a constant. Instead look up the quantities you need with `image.shape[0]`, etc. 

```python
# GRADED FUNCTION: image2vector
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    v = image.reshape((image.shape[0]*image.shape[1]*image.shape[2]),1)
    ### END CODE HERE ###
    
    return v
```

```python
# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values
image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])
print(image.shape)
print ("image2vector(image) = " + str(image2vector(image)))
print(image2vector(image).shape)
```

```
(3, 3, 2)
image2vector(image) = [[ 0.67826139]
 [ 0.29380381]
 [ 0.90714982]
 [ 0.52835647]
 [ 0.4215251 ]
 [ 0.45017551]
 [ 0.92814219]
 [ 0.96677647]
 [ 0.85304703]
 [ 0.52351845]
 [ 0.19981397]
 [ 0.27417313]
 [ 0.60659855]
 [ 0.00533165]
 [ 0.10820313]
 [ 0.49978937]
 [ 0.34144279]
 [ 0.94630077]]
(18, 1)
```

### 1.4 - Normalizing rows

![image](https://user-images.githubusercontent.com/18595935/53780885-b8606b80-3f49-11e9-93c5-20f48b6a152c.png)


```python
# GRADED FUNCTION: normalizeRows

def normalizeRows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x, ord = 2, axis = 1, keepdims = True)
    
    # Divide x by its norm.
    x = x / x_norm
    ### END CODE HERE ###

    return x
```

```python
x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("normalizeRows(x) = " + str(normalizeRows(x)))
```

```
normalizeRows(x) = [[ 0.          0.6         0.8       ]
 [ 0.13736056  0.82416338  0.54944226]]
```

### 1.5 - Broadcasting and the softmax function ####
A very important concept to understand in numpy is "broadcasting". It is very useful for performing mathematical operations between arrays of different shapes. For the full details on broadcasting, you can read the official [broadcasting documentation](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

**Exercise**: Implement a softmax function using numpy. You can think of softmax as a normalizing function used when your algorithm needs to classify two or more classes. You will learn more about softmax in the second course of this specialization.

![image](https://user-images.githubusercontent.com/18595935/53783309-696c0380-3f54-11e9-92e2-bc36987d4564.png)

```python
# GRADED FUNCTION: softmax

def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (n, m).

    Argument:
    x -- A numpy matrix of shape (n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    
    ### START CODE HERE ### (≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    x_sum = np.sum(x_exp,axis=1, keepdims = True)
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    s = x_exp/x_sum

    ### END CODE HERE ###
    
    return s
```

```python
x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])
print("softmax(x) = " + str(softmax(x)))
```

```
softmax(x) = [[  9.80897665e-01   8.94462891e-04   1.79657674e-02   1.21052389e-04
    1.21052389e-04]
 [  8.78679856e-01   1.18916387e-01   8.01252314e-04   8.01252314e-04
    8.01252314e-04]]
```

<font color='blue'>
**What you need to remember:**
- np.exp(x) works for any np.array x and applies the exponential function to every coordinate
- the sigmoid function and its gradient
- image2vector is commonly used in deep learning
- np.reshape is widely used. In the future, you'll see that keeping your matrix/vector dimensions straight will go toward eliminating a lot of bugs. 
- numpy has efficient built-in functions
- broadcasting is extremely useful


## 2) Vectorization

In deep learning, you deal with very large datasets. Hence, a non-computationally-optimal function can become a huge bottleneck in your algorithm and can result in a model that takes ages to run. To make sure that your code is  computationally efficient, you will use vectorization. For example, try to tell the difference between the following implementations of the dot/outer/elementwise product.

比较下面两个版本，for循环版和向量计算版本：

```python
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

### CLASSIC DOT PRODUCT OF VECTORS IMPLEMENTATION ###
tic = time.process_time()
dot = 0
for i in range(len(x1)):
    dot+= x1[i]*x2[i]
toc = time.process_time()
print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### CLASSIC OUTER PRODUCT IMPLEMENTATION ###
tic = time.process_time()
outer = np.zeros((len(x1),len(x2))) # we create a len(x1)*len(x2) matrix with only zeros
for i in range(len(x1)):
    for j in range(len(x2)):
        outer[i,j] = x1[i]*x2[j]
toc = time.process_time()
print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### CLASSIC ELEMENTWISE IMPLEMENTATION ###
tic = time.process_time()
mul = np.zeros(len(x1))
for i in range(len(x1)):
    mul[i] = x1[i]*x2[i]
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### CLASSIC GENERAL DOT PRODUCT IMPLEMENTATION ###
W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array
tic = time.process_time()
gdot = np.zeros(W.shape[0])
for i in range(W.shape[0]):
    for j in range(len(x1)):
        gdot[i] += W[i,j]*x1[j]
toc = time.process_time()
print ("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")
```

```python
x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

### VECTORIZED DOT PRODUCT OF VECTORS ###
tic = time.process_time()
dot = np.dot(x1,x2)
toc = time.process_time()
print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED OUTER PRODUCT ###
tic = time.process_time()
outer = np.outer(x1,x2)
toc = time.process_time()
print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED ELEMENTWISE MULTIPLICATION ###
tic = time.process_time()
mul = np.multiply(x1,x2)
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED GENERAL DOT PRODUCT ###
tic = time.process_time()
dot = np.dot(W,x1)
toc = time.process_time()
print ("gdot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")
```

**Note** that `np.dot()` performs a matrix-matrix or matrix-vector multiplication. This is different from `np.multiply()` and the `*` operator (which is equivalent to  `.*` in Matlab/Octave), which performs an element-wise multiplication.

### 2.1 Implement the L1 and L2 loss functions

**Exercise**: Implement the numpy vectorized version of the L1 loss. You may find the function abs(x) (absolute value of x) useful.

![image](https://user-images.githubusercontent.com/18595935/53783950-f748ee00-3f56-11e9-936a-21e378a4ec6b.png)

```python
# GRADED FUNCTION: L1

def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    loss = np.sum(np.abs(yhat-y))
    ### END CODE HERE ###
    
    return loss
```

```python
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))
```

输出`L1 = 1.1`

![image](https://user-images.githubusercontent.com/18595935/53784019-35dea880-3f57-11e9-92af-76ab73216e35.png)

```python
# GRADED FUNCTION: L2

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    loss = np.sum((yhat-y)**2)
    ### END CODE HERE ###
    
    return loss
```

```python
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))
```

输出`L2 = 0.43`

<font color='blue'>
**What to remember:**
- Vectorization is very important in deep learning. It provides computational efficiency and clarity.
- You have reviewed the L1 and L2 loss.
- You are familiar with many numpy functions such as np.sum, np.dot, np.multiply, np.maximum, etc...


# 练习2：ogistic Regression with a Neural Network mindset

In this notebook you will build your first image recognition algorithm. You will build a cat classifier that recognizes cats with 70% accuracy!

As you keep learning new techniques you will increase it to 80+ % accuracy on cat vs. non-cat datasets. By completing this assignment you will:
- Work with logistic regression in a way that builds intuition relevant to neural networks.
- Learn how to minimize the cost function.
- Understand how derivatives of the cost are used to update parameters.



