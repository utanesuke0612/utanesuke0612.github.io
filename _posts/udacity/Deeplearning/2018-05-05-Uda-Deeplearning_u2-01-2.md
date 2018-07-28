---
layout: post
title: Uda-DeepLearning-U2-01-神经网络简介(下)
date: 2018-05-04 00:00:02
categories: DeepLearning
tags: Udacity DeepLearning
---
* content
{:toc}


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

该函数将帮助我们通过所有数据来迭代梯度下降算法，用于多个 epoch。 它还将绘制数据，以及在我们运行算法时绘制出一些边界线。

```python
np.random.seed(44)

epochs = 100
learnrate = 0.01

def train(features, targets, epochs, learnrate, graph_lines=False):
    
    errors = []
    n_records, n_features = features.shape
    last_loss = None
    weights = np.random.normal(scale=1 / n_features**.5, size=n_features)
    #print(weights)
    bias = 0
    for e in range(epochs):
        del_w = np.zeros(weights.shape)
        for x, y in zip(features, targets):
            output = output_formula(x, weights, bias)
            error = error_formula(y, output)
            weights, bias = update_weights(x, y, weights, bias, learnrate)
        
        # Printing out the log-loss error on the training set
        out = output_formula(features, weights, bias)
        loss = np.mean(error_formula(targets, out))
        errors.append(loss)
        if e % (epochs / 10) == 0:
            print("\n========== Epoch", e,"==========")
            if last_loss and last_loss < loss:
                print("Train loss: ", loss, "  WARNING - Loss Increasing")
            else:
                print("Train loss: ", loss)
            last_loss = loss
            predictions = out > 0.5
            accuracy = np.mean(predictions == targets)
            print("Accuracy: ", accuracy)
        if graph_lines and e % (epochs / 100) == 0:
            display(-weights[0]/weights[1], -bias/weights[1])
            

    # Plotting the solution boundary
    plt.title("Solution boundary")
    display(-weights[0]/weights[1], -bias/weights[1], 'black')

    # Plotting the data
    plot_points(features, targets)
    plt.show()

    # Plotting the error
    plt.title("Error Plot")
    plt.xlabel('Number of epochs')
    plt.ylabel('Error')
    plt.plot(errors)
    plt.show()
```

## 26.4 训练结果

当我们运行该函数时，我们将获得以下内容：
- 目前的训练损失与准确性的 10 次更新
- 获取的数据图和一些边界线的图。 最后一个是黑色的。请注意，随着我们遍历更多的 epoch ，线会越来越接近最佳状态。
- 误差函数的图。 请留意，随着我们遍历更多的 epoch，它会如何降低。

```python
train(X, y, epochs, learnrate, True)
```

结果如下:

```python
========== Epoch 0 ==========
Train loss:  0.713584519538
Accuracy:  0.4

========== Epoch 10 ==========
Train loss:  0.622583521045
Accuracy:  0.59

========== Epoch 20 ==========
Train loss:  0.554874408367
Accuracy:  0.74

========== Epoch 30 ==========
Train loss:  0.501606141872
Accuracy:  0.84

========== Epoch 40 ==========
Train loss:  0.459333464186
Accuracy:  0.86

========== Epoch 50 ==========
Train loss:  0.425255434335
Accuracy:  0.93

========== Epoch 60 ==========
Train loss:  0.397346157167
Accuracy:  0.93

========== Epoch 70 ==========
Train loss:  0.374146976524
Accuracy:  0.93

========== Epoch 80 ==========
Train loss:  0.354599733682
Accuracy:  0.94

========== Epoch 90 ==========
Train loss:  0.337927365888
Accuracy:  0.94
```

![image](https://user-images.githubusercontent.com/18595935/43356892-ee31a9ba-92b3-11e8-9f79-7d8ce4ebc9db.png)

# 27. Logistic(对数概率)感知器和梯度下降

![image](https://user-images.githubusercontent.com/18595935/43357047-8d91bfe8-92b6-11e8-87ba-020e8f277a8a.png)

具体可以参考之间的感知器和梯度下降算法。

# 28. 连续型感知器

![image](https://user-images.githubusercontent.com/18595935/43357076-0edc5054-92b7-11e8-9761-2da82aae3f37.png)

# 30. 非线性数据

现实中很多情况下并不是线性的，如下图:

![image](https://user-images.githubusercontent.com/18595935/43357137-0147837c-92b8-11e8-84c5-730cb3c2edad.png)

# 31. 神经网络结构

现在可以将这些构建基石组合到一起了，并构建出色的神经网络！（或者你愿意，也可以叫做多层级感知器。）
第一个视频将演示如何将两个感知器组合成第三个更复杂的感知器。

## 31.1 神经网络架构

![image](https://user-images.githubusercontent.com/18595935/43357491-7588de3e-92bd-11e8-845d-9cad7b93def7.png)

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

print(sigmoid(1.5))
print(sigmoid(2.9))
```

输出为`0.817574476194`和`0.947846436922`。

![image](https://user-images.githubusercontent.com/18595935/43357754-5e44a614-92c1-11e8-9b1e-9c8e1c4d43e9.png)

## 31.2 多层级

并非所有神经网络都看起像上面的那样。可能会复杂的多！尤其是，我们可以执行以下操作：
- 向输入、隐藏和输出层添加更多节点。
- 添加更多层级。



# 32. 前向反馈

# 33. 反向传播

# 34. [Lab准备]分析学生数据

# 35. [Lab]分析学生数据