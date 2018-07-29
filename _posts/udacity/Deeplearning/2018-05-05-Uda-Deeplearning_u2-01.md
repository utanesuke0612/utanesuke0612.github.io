---
layout: post
title: Uda-DeepLearning-U2-01-神经网络简介
date: 2018-05-04 00:00:00
categories: DeepLearning
tags: Udacity DeepLearning
---
* content
{:toc}


# 1. 简介

通过深层神经网络，寻找能够分开这些点的复杂界线。

![image](https://user-images.githubusercontent.com/18595935/39668969-08cc0bda-5119-11e8-96fc-8e33e47374ad.png)


# 2. 分类问题

下面只是先肉眼识别判断:

![image](https://user-images.githubusercontent.com/18595935/39668982-c97b5f8e-5119-11e8-862f-5599728abb72.png)

# 4. 线性界线

X1是横轴，X2是纵轴，W1是横轴的权重，W2是纵轴的权重，b是偏差，W是w1和w2的向量，x是X1和X2的向量，那么Wx是矩阵（w1,w2）和(x1,x2)的乘积。

![image](https://user-images.githubusercontent.com/18595935/39669029-31930472-511b-11e8-90a4-e3f3908d54e9.png)

# 5. 更高维度

上面的评测标准是二维的，只有平时成绩和最终成绩，如果再加上一维，最终图示如下，仍可以用`Wx + b = 0`表示，只不过W和x的向量多了一个元素。

![image](https://user-images.githubusercontent.com/18595935/39669072-3f6030a6-511c-11e8-9c35-2734ff313636.png)

同理，扩展到N维:

![image](https://user-images.githubusercontent.com/18595935/39669091-b11d5412-511c-11e8-834e-e046083a54a0.png)

# 6. 感知器

感知器Perceptron是神经网络的重要部件。

![image](https://user-images.githubusercontent.com/18595935/39669581-d81f9e2c-512a-11e8-9e82-a2033118e100.png)

还有另外一种表示方式:

![image](https://user-images.githubusercontent.com/18595935/39669590-184d66f0-512b-11e8-9208-c8899d68348a.png)

# 7. 为何是神经网络？

- 感知器的结构与大脑神经元的结构很相似。
- 左图中是一个带有四个input的感知器，感知器所做得是根据方程式和输入，决定是返回0还是1.
- 右图中，类似的大脑神经元从树突中获得输入，这些输入都是神经冲动(nervous impulses)

![image](https://user-images.githubusercontent.com/18595935/39669654-67af6714-512d-11e8-8a26-b81d0f0e0b84.png)

# 8. 作为逻辑运算符的感知器

作为逻辑运算符的感知器，本节中将学习感知器的很多强大应用之一。

## 8.1 AND 感知器

![image](https://user-images.githubusercontent.com/18595935/39669789-c0c8563c-5130-11e8-939a-f514ed6ff665.png)

```python


import pandas as pd

# TODO: Set weight1, weight2, and bias
weight1 = 1.0
weight2 = 1.0
bias = -1.5


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, False, False, True]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))

```

输出如下:

```python
Nice!  You got it all correct.

Input 1    Input 2    Linear Combination    Activation Output   Is Correct
      0          0                  -1.5                    0          Yes
      0          1                  -0.5                    0          Yes
      1          0                  -0.5                    0          Yes
      1          1                   0.5                    1          Yes
```

## 8.2 OR 感知器

![image](https://user-images.githubusercontent.com/18595935/39669803-1884f77c-5131-11e8-9d1e-c6dd2a9621f7.png)

从 AND 感知器变成 OR 感知器的两种方法是什么？
- 增大权重
- 减小偏差大小

![image](https://user-images.githubusercontent.com/18595935/39669834-4ef67424-5132-11e8-9f22-73533206b786.png)

## 8.3 NOT 感知器

NOT 感知器
和我们刚刚研究的其他感知器不一样，NOT 运算仅关心一个输入。如果输入是 1，则运算返回 0，如果输入是 0，则返回 1。感知器的其他输入被忽略了。

在此测验中，你将设置权重（weight1、weight2）和偏差 bias，以便对第二个输入进行 NOT 运算，并忽略第一个输入。

```python
import pandas as pd

# TODO: Set weight1, weight2, and bias
weight1 = 0
weight2 = -1
bias = 0.5


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [True, False, True, False]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
```

- 输出如下(Linear Combination是计算出来的结果，Activation Output是判断后的结果-大于等于0则为1，小于0则为0):

```python
Nice!  You got it all correct.

Input 1    Input 2    Linear Combination    Activation Output   Is Correct
      0          0                   0.5                    1          Yes
      0          1                  -0.5                    0          Yes
      1          0                   0.5                    1          Yes
      1          1                  -0.5                    0          Yes
```

## 8.4 XOR 感知器

![image](https://user-images.githubusercontent.com/18595935/39669997-9e33feec-5134-11e8-9ffe-f542c13b90b4.png)

测验：构建一个 XOR 多层感知器
现在我们使用 AND、NOT 和 OR 感知器构建一个多层感知器，以便创建 XOR 逻辑！

下面的神经网络包含三个感知器：A、B 和 C。最后一个 (AND) 已经提供给你了。神经网络的输入来自第一个节点。输出来自最后一个节点。

上面的多层感知器计算出 XOR。每个感知器都是 AND、OR 和 NOT 的逻辑运算。但是，感知器 A、B、C 和 D 并不表明它们的运算。在下面的测验中，请为四个感知器设置正确的运算，以便计算 XOR。

![image](https://user-images.githubusercontent.com/18595935/39670001-cfabf862-5134-11e8-82b2-6d3e8cce0698.png)

如果将 AND 和 NOT 相结合引入 NAND 运算符，那么我们得出下面的两层感知器，表示 XOR 模型。这是我们的首个神经网络！

![image](https://user-images.githubusercontent.com/18595935/39670199-58a72560-513a-11e8-87f6-eebb7e572933.png)

在 XOR 神经网络中为感知器设置运算。

![image](https://user-images.githubusercontent.com/18595935/39670238-041cd890-513b-11e8-9baf-6ca794e0f0b3.png)

NOT 运算仅关心一个输入，类似于程序语言中的一元运算符。

# 9. 感知器技巧

如下是不断调整已有的方程式，将例外的点放到正确的区域中，`learning rate`是为了保证不要一次移动太多而影响到现有的分类。

![image](https://user-images.githubusercontent.com/18595935/39671580-f8ee2b7a-5155-11e8-9a73-f40d09bfe982.png)

# 10. 感知器算法

下面是调整感知器的伪码:

从一个带有随机初始参数的方程开始，它定义了一条直线以及划分出的两个区域，也就是正区域与负区域，我们通过不断移动该直线，使分类结果更加准确。

![image](https://user-images.githubusercontent.com/18595935/39671646-03873864-5157-11e8-9d9b-1e36d2a7d525.png)

1. 生成随机的weight和bias
2. 计算分类结果
3. 循环处理所有错误分类的点
4. 如果处于负区域，则调整每个weight为`wi + axi`，调整bias为`b + a`
5. 如果处理正区域，则调整每个weight为`wi - axi`，调整bias为`b - a`

## 10.1 编写感知器算法

下面是`data.csv`生成的图形。

![image](https://user-images.githubusercontent.com/18595935/39671994-21a353ea-515d-11e8-847b-55761ccef0e4.png)

![image](https://user-images.githubusercontent.com/18595935/39672004-5bf38a7e-515d-11e8-87a4-bab768130e62.png)

- `data.csv`

```python
0.78051,-0.063669,1
0.28774,0.29139,1
0.40714,0.17878,1
0.44274,0.59205,0
0.85176,0.6612,0
0.60436,0.86605,0
0.68243,0.48301,0
...
```

- `perceptron.py`

```python
import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines

```

画出一组虚线，显示算法如何接近最佳解决方案（用黑色实线表示）。

![image](https://user-images.githubusercontent.com/18595935/39672019-a2e2fc8a-515d-11e8-87ce-2c228164a9d3.png)

# 11. 非线性数据

![image](https://user-images.githubusercontent.com/18595935/39672075-63bc143c-515e-11e8-9c77-ec39b245859c.png)

我们需要重新定义感知器算法，使其能够泛化到非直线的曲线上。

# 12. 误差函数

误差函数(Error Function)可以告诉我们与正确答案之间的差别有多大，借助误差函数能够完成上面泛化感知器的任务。


# 13. 对数损失误差函数

关于损失函数，参考[机器学习-损失函数](http://www.csuldw.com/2016/03/26/2016-03-26-loss-function/)

损失函数（loss function）是用来估量你模型的预测值f(x)与真实值Y的不一致程度，它是一个非负实值函数,通常使用L(Y, f(x))来表示，损失函数越小，模型的鲁棒性就越好。损失函数是经验风险函数的核心部分，也是结构风险函数重要组成部分。模型的结构风险函数包括了经验风险项和正则项，通常可以表示成如下式子：

![image](https://user-images.githubusercontent.com/18595935/41298251-ea17771a-6e9b-11e8-966c-ab48deb2f476.png)

其中，前面的均值函数表示的是经验风险函数，L代表的是损失函数，后面的Φ是正则化项（regularizer）或者叫惩罚项（penalty term），它可以是L1，也可以是L2，或者其他的正则函数。整个式子表示的意思是找到使目标函数最小时的θ值。下面主要列出几种常见的损失函数。

# 14. 离散型与连续型

对于优化而言，连续型误差函数比离散型函数更好。为此，我们需要从离散型预测变成连续型预测。

如下图，离散型与连续性函数的预测结果:

![image](https://user-images.githubusercontent.com/18595935/41494278-d97a60c2-714b-11e8-83a2-0ea2afbdc817.png)

离散型与连续性的激活函数:

![image](https://user-images.githubusercontent.com/18595935/41494288-fc51ae02-714b-11e8-933d-d1fbe953c7cf.png)

连续性激活函数，根据x为0时，即介于中介分割线时，两者几率一样，离分割线正无穷大时，几率为1,反之为0.


# 15. 多类别分类和 Softmax

将各个动物的得分，通过softmax函数转换成了概率:

![image](https://user-images.githubusercontent.com/18595935/41494454-1e6bf130-714e-11e8-8b39-b928a13d6785.png)

下面是softmax函数，另外softmax函数当个数为2的时候，与上面的sigmoid函数(S曲线函数)是相同的，可以自行推导。

![image](https://user-images.githubusercontent.com/18595935/41494485-74ea61cc-714e-11e8-8a19-99a22f9daf0b.png)


```python

import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())

L = np.array([5,6,7,8,9])
print(softmax(L))

```

输出 `[0.011656230956039607, 0.031684920796124269, 0.086128544436268703, 0.23412165725273665, 0.63640864655883089]`。


# 16. One-Hot 编码

参考[机器学习实战：数据预处理之独热编码（One-Hot Encoding）](https://www.cnblogs.com/lzh-cnblogs/p/3764749.html)

独热编码即 One-Hot 编码，又称一位有效编码，其方法是使用N位状态寄存器来对N个状态进行编码，每个状态都由他独立的寄存器位，并且在任意时候，其中只有一位有效。

![image](https://user-images.githubusercontent.com/18595935/41494629-cbab4aec-7150-11e8-906a-b1f46d248927.png)

如上图，各种动物出现的状况，三种动物表示三种状态，用3位状态寄存器编码，任意时候，只有一个寄存器是1，其他都是0.


# 17. 最大似然率

参考[最大似然估计(Maximum likelihood estimation)](https://www.cnblogs.com/liliu/archive/2010/11/22/1883702.html)

下面是点颜色的概率分布，中间的线表示模型:

![image](https://user-images.githubusercontent.com/18595935/41494795-0aff0596-7154-11e8-9e8c-d9b71b1c871c.png)

对比另一个模型，计算其最大似然率，显然右边模型更好:

![image](https://user-images.githubusercontent.com/18595935/41494802-35705a96-7154-11e8-83a3-a45eac71f391.png)

# 18. 最大化概率

上面的最大似然率是通过概率的乘积得到，如果存在上千个概率相乘，最终结果会非常小，不便于计算与比较，这里需要将其转换为求和。

利用log(ab) = log(a) + log(b)的特性:

![image](https://user-images.githubusercontent.com/18595935/41494891-57bbb2ce-7156-11e8-9af9-2139bd7fb2ac.png)

交叉熵(Cross Entropy)可以告诉我们模型的好坏，所以我们现在的目标从最大化概率，变成了最小化交叉熵，我们要寻找的误差函数，就是这个交叉熵。


# 20. 交叉熵(cross entropy)

概率和误差函数之间肯定有一定的联系，这种联系叫做交叉熵。这个概念在很多领域都非常流行，包括机器学习领域。我们将详细了解该公式，并编写代码！

假设有一系列事件event,以及一系列概率probabilities，这一系列事件发生的概率很大，则交叉熵很小，反之交叉熵很大。

![image](https://user-images.githubusercontent.com/18595935/41495961-ca0f1bb4-716e-11e8-812e-a9acceffdd07.png)

如上图，0.69是最有可能发生的，概率为0.504，而5.12的交叉熵是最不可能发生，概率为0.006.

通过公式计算如下:

![image](https://user-images.githubusercontent.com/18595935/41495998-a0548d6c-716f-11e8-9dc7-22c083dd9319.png)

- 参考代码如下:

```python
import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

```

计算:

```python
Y = np.array([1,1,0])
P = np.array([0.8,0.7,0.1])
print(cross_entropy(Y,P))
```

```python
Y = np.array([0,0,1])
P = np.array([0.8,0.7,0.1])
print(cross_entropy(Y,P))
```

分别为`0.685179010911`和`5.11599580975`。


# 21. 多类别交叉熵

![image](https://user-images.githubusercontent.com/18595935/41496382-bd94fc18-7179-11e8-8a94-674f75681877.png)


# 22. Logistic 回归

机器学习的基石——对数几率回归算法，基本上是这样的：

- 获得数据
- 选择一个随机模型
- 计算误差
- 最小化误差，获得更好的模型

## 22.1 计算误差函数

下面的Error Function表示所有点在该模型下的误差之和的平均数。

![image](https://user-images.githubusercontent.com/18595935/41542493-0d962b7e-7350-11e8-8917-345563914975.png)

另外上面只是一个二元分类问题，如果有多个类别的分类问题，那么误差将是多类别交叉熵。

![image](https://user-images.githubusercontent.com/18595935/41542673-735b07c2-7350-11e8-8e69-30758bf97709.png)


## 22.2 最小化误差函数

首先随机选取权重w和b，构成误差函数，利用梯度下降法，不断调整权重，最后达到一个最合适的位置，即误差最小的模型。

![image](https://user-images.githubusercontent.com/18595935/41543147-5d768a8e-7351-11e8-9a9c-1443877cf55a.png)

# 23. 梯度下降

![image](https://user-images.githubusercontent.com/18595935/43356263-259955f8-92a8-11e8-971b-6684aea6e14d.png)
![image](https://user-images.githubusercontent.com/18595935/43356264-27c00c00-92a8-11e8-8f18-402a07c650e5.png)

# 24. 梯度下降算法

![image](https://user-images.githubusercontent.com/18595935/43356095-4900bbc4-92a5-11e8-8f37-3f94408ac1a2.png)

# 25. [Lab准备]梯度下降

# 26. [Lab]梯度下降

在这个notebook中，你将实现构建梯度下降算法的功能，即：

- sigmoid: sigmoid激活函数。
- output_formula: 输出（预测）公式
- error_formula: 误差函数。
- update_weights: 更新权重的函数。

当你执行它们时，运行 train 函数，这将绘制连续梯度下降步骤中的几条直线。 它还会绘制误差函数，随着 epoch 数量的增加，你可以看到它正在降低。

在这里实现一个单层的神经网络，来完成分类器的正确分类。

## 26.1 读取与绘制数据

在该 Lab 中，我们将实现梯度下降算法的基本函数，以便在小数据集中查找数据边界。 首先，我们将从一些函数开始，帮助我们绘制和可视化数据。

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Some helper functions for plotting and drawing lines

def plot_points(X, y):
    admitted = X[np.argwhere(y==1)]
    rejected = X[np.argwhere(y==0)]
    plt.scatter([s[0][0] for s in rejected], [s[0][1] for s in rejected], s = 25, color = 'blue', edgecolor = 'k')
    plt.scatter([s[0][0] for s in admitted], [s[0][1] for s in admitted], s = 25, color = 'red', edgecolor = 'k')

def display(m, b, color='g--'):
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, m*x+b, color)
```

```python
data = pd.read_csv('data.csv', header=None)
X = np.array(data[[0,1]])
y = np.array(data[2])
plot_points(X,y)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43356656-b8f2231e-92af-11e8-95a0-7dec01135ad5.png)

## 26.2 实现基本函数

实现以下基本函数。

![image](https://user-images.githubusercontent.com/18595935/43356678-0af2b69c-92b0-11e8-917c-03a87f4fb716.png)

```python
# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def output_formula(features, weights, bias):
    return sigmoid(np.dot(features, weights) + bias)

def error_formula(y, output):
    return - y*np.log(output) - (1 - y) * np.log(1-output)

def update_weights(x, y, weights, bias, learnrate):
    output = output_formula(x, weights, bias)
    d_error = -(y - output)
    weights -= learnrate * d_error * x
    bias -= learnrate * d_error
    return weights, bias
```

## 26.3 训练函数




# 27. Logistic(对数概率)感知器和梯度下降

# 28. 连续型感知器

# 29. 非线性数据1

# 30. 非线性数据2

# 31. 神经网络结构

# 32. 前向反馈

# 33. 反向传播

# 34. [Lab准备]分析学生数据

# 35. [Lab]分析学生数据