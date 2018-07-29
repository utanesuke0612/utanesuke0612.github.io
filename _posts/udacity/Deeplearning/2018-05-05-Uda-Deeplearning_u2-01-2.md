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

- 1.向输入、隐藏和输出层添加更多节点
- 
![image](https://user-images.githubusercontent.com/18595935/43358377-8186b446-92cb-11e8-81f7-d0b039e41467.png)

隐藏层中的感知器也可以是一个面:

![image](https://user-images.githubusercontent.com/18595935/43358380-8bfdab32-92cb-11e8-9e56-1e58b3e17c20.png)

- 2.添加更多层级

![image](https://user-images.githubusercontent.com/18595935/43358386-ae474d38-92cb-11e8-83db-a0c99949a1f6.png)

# 32. 前向反馈

## 32.1 前向反馈-feedforward

前向反馈是神经网络用来将输入变成输出的流程。我们仔细研究下这一概念，然后详细了解如何训练网络。

- 最简单的神经网络，只有一个隐藏层

![image](https://user-images.githubusercontent.com/18595935/43362276-6de54b36-9321-11e8-9e95-f87799d01c1f.png)

- 追加一个隐藏层节点

![image](https://user-images.githubusercontent.com/18595935/43362279-8961a6f2-9321-11e8-8efc-c455d7017469.png)

-  一个隐藏层的神经网络预测函数

![image](https://user-images.githubusercontent.com/18595935/43362327-82d1ee2c-9322-11e8-8f6d-5edaa5c1509c.png)

- 两个隐藏层的神经网络预测函数

![image](https://user-images.githubusercontent.com/18595935/43362337-b0cafd0a-9322-11e8-98cd-4c8b23da2575.png)

## 32.2 误差函数

- 一层隐藏层下的预测函数和误差函数

![image](https://user-images.githubusercontent.com/18595935/43362395-039956de-9324-11e8-9e8f-3493e3b6ef43.png)

- 二层隐藏层下的预测函数和误差函数

![image](https://user-images.githubusercontent.com/18595935/43362401-1a75b4ce-9324-11e8-99bd-6c93f3802768.png)

# 33. 反向传播 - Backpropagation

反向传播将包括：

1. 进行前向反馈运算。
2. 将模型的输出与期望的输出进行比较。
3. 计算误差。
4. 向后运行前向反馈运算（反向传播），将误差分散到每个权重上。
5. 更新权重，并获得更好的模型。
6. 继续此流程，直到获得很好的模型。

-  反向传播，更新权重获得更好的模型

![image](https://user-images.githubusercontent.com/18595935/43362573-bd7f8ea2-9328-11e8-8f11-ba713b0774cf.png)

![image](https://user-images.githubusercontent.com/18595935/43362576-e51fba72-9328-11e8-9dd0-8c6672e1c2f0.png)


- 调整各个层上的权重，获得更好的模型

![image](https://user-images.githubusercontent.com/18595935/43362590-16485898-9329-11e8-9ca2-469e681bb973.png)

# 35. [Lab]分析学生数据

分析以下加州大学洛杉矶分校的学生录取的数据。在这个 notebook 中，执行神经网络训练的一些步骤，即：
- One-hot 编码数据
- 缩放数据
- 编写反向传播步骤

在该 notebook 中，我们基于以下三条数据预测了加州大学洛杉矶分校 (UCLA) 的研究生录取情况：
- GRE 分数（测试）即 GRE Scores (Test)
- GPA 分数（成绩）即 GPA Scores (Grades)
- 评级（1-4）即 Class rank (1-4)

## 35.1 加载数据

为了加载数据并很好地进行格式化，我们将使用两个非常有用的包，即 Pandas 和 Numpy。 你可以在这里阅读文档：

- https://pandas.pydata.org/pandas-docs/stable/
- https://docs.scipy.org/

```python
# Importing pandas and numpy
import pandas as pd
import numpy as np

# Reading the csv file into a pandas DataFrame
data = pd.read_csv('student_data.csv')

# Printing out the first 10 rows of our data
data[:10]
```

结果如下图:

![image](https://user-images.githubusercontent.com/18595935/43362728-609799ce-932c-11e8-80b1-df5a5d70e3d4.png)

## 35.2 绘制数据

首先让我们对数据进行绘图，看看它是什么样的。为了绘制二维图，让我们先忽略评级 (rank)。

```python
# Importing matplotlib
import matplotlib.pyplot as plt

# Function to help us plot
def plot_points(data):
    X = np.array(data[["gre","gpa"]])
    y = np.array(data["admit"])
    admitted = X[np.argwhere(y==1)]
    rejected = X[np.argwhere(y==0)]
    plt.scatter([s[0][0] for s in rejected], [s[0][1] for s in rejected], s = 25, color = 'red', edgecolor = 'k')
    plt.scatter([s[0][0] for s in admitted], [s[0][1] for s in admitted], s = 25, color = 'cyan', edgecolor = 'k')
    plt.xlabel('Test (GRE)')
    plt.ylabel('Grades (GPA)')
    
# Plotting the points
plot_points(data)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43362735-8f09ab30-932c-11e8-9524-3bd4fe440db2.png)


粗略来说，它看起来像是，成绩 （grades) 和测试 (test) 分数高的学生通过了，而得分低的学生却没有，但数据并没有如我们所希望的那样，很好地分离。 也许将评级 (rank) 考虑进来会有帮助？ 接下来我们将绘制 4 个图，每个图代表一个级别。

```python
# Separating the ranks
data_rank1 = data[data["rank"]==1]
data_rank2 = data[data["rank"]==2]
data_rank3 = data[data["rank"]==3]
data_rank4 = data[data["rank"]==4]

# Plotting the graphs
plot_points(data_rank1)
plt.title("Rank 1")
plt.show()
plot_points(data_rank2)
plt.title("Rank 2")
plt.show()
plot_points(data_rank3)
plt.title("Rank 3")
plt.show()
plot_points(data_rank4)
plt.title("Rank 4")
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43362751-ccf2765c-932c-11e8-8348-c62c3e89d3c4.png)
![image](https://user-images.githubusercontent.com/18595935/43362754-d815a6f8-932c-11e8-93b1-a1d704e2bd14.png)


现在看起来更棒啦，看上去评级越低，录取率越高。 让我们使用评级 (rank) 作为我们的输入之一。 为了做到这一点，我们应该对它进行一次one-hot 编码。

## 35.3 将评级进行 One-hot 编码
我们将在 Pandas 中使用 `get_dummies` 函数。

```python
# Make dummy variables for rank
one_hot_data = pd.concat([data, pd.get_dummies(data['rank'], prefix='rank')], axis=1)

# Drop the previous rank column
one_hot_data = one_hot_data.drop('rank', axis=1)

# Print the first 10 rows of our data
one_hot_data[:10]
```

![image](https://user-images.githubusercontent.com/18595935/43362762-0ca44a1e-932d-11e8-9996-e1b9a11392e2.png)

## 35.4 缩放数据

下一步是缩放数据。 我们注意到成绩 (grades) 的范围是 1.0-4.0，而测试分数 （test scores) 的范围大概是 200-800，这个范围要大得多。 这意味着我们的数据存在偏差，使得神经网络很难处理。 让我们将两个特征放在 0-1 的范围内，将分数除以 4.0，将测试分数除以 800。


```python
# Copying our data
processed_data = one_hot_data[:]

# Scaling the columns
processed_data['gre'] = processed_data['gre']/800
processed_data['gpa'] = processed_data['gpa']/4.0
processed_data[:10]
```

![image](https://user-images.githubusercontent.com/18595935/43362767-2e0414fa-932d-11e8-97d2-11dae4db419c.png)


## 35.5 将数据分成训练集和测试集

为了测试我们的算法，我们将数据分为训练集和测试集。 测试集的大小将占总数据的 10％。

```python
sample = np.random.choice(processed_data.index, size=int(len(processed_data)*0.9), replace=False)
train_data, test_data = processed_data.iloc[sample], processed_data.drop(sample)

print("Number of training samples is", len(train_data))
print("Number of testing samples is", len(test_data))
print(train_data[:10])
print(test_data[:10])

```

![image](https://user-images.githubusercontent.com/18595935/43362774-4af8d758-932d-11e8-9b7f-6ded77b183fb.png)


## 35.6 将数据分成特征和目标（标签）
现在，在训练前的最后一步，我们将把数据分为特征 (features)（X）和目标 (targets)（y）。

```python
features = train_data.drop('admit', axis=1)
targets = train_data['admit']
features_test = test_data.drop('admit', axis=1)
targets_test = test_data['admit']

print(features[:10])
print(targets[:10])
```

![image](https://user-images.githubusercontent.com/18595935/43362782-70f0d2e4-932d-11e8-8448-fc97f57f6e72.png)


## 35.7 训练二层神经网络
下列函数会训练二层神经网络。 首先，我们将写一些 helper 函数。

```python
# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_prime(x):
    return sigmoid(x) * (1-sigmoid(x))
def error_formula(y, output):
    return - y*np.log(output) - (1 - y) * np.log(1-output)
```

## 35.8 误差反向传播

现在轮到你来练习，编写误差项，公式为:

![image](https://user-images.githubusercontent.com/18595935/43362793-bc56a45c-932d-11e8-970b-7fbd9304c067.png)

```python
def error_term_formula(y, output):
    return (y-output) * output * (1 - output)
```

```python
# Neural Network hyperparameters
epochs = 1000
learnrate = 0.5

# Training function
def train_nn(features, targets, epochs, learnrate):
    
    # Use to same seed to make debugging easier
    np.random.seed(42)

    n_records, n_features = features.shape
    last_loss = None

    # Initialize weights
    weights = np.random.normal(scale=1 / n_features**.5, size=n_features)

    for e in range(epochs):
        del_w = np.zeros(weights.shape)
        for x, y in zip(features.values, targets):
            # Loop through all records, x is the input, y is the target

            # Activation of the output unit
            #   Notice we multiply the inputs and the weights here 
            #   rather than storing h as a separate variable 
            output = sigmoid(np.dot(x, weights))

            # The error, the target minus the network output
            error = error_formula(y, output)

            # The error term
            #   Notice we calulate f'(h) here instead of defining a separate
            #   sigmoid_prime function. This just makes it faster because we
            #   can re-use the result of the sigmoid function stored in
            #   the output variable
            error_term = error_term_formula(y, output)

            # The gradient descent step, the error times the gradient times the inputs
            del_w += error_term * x

        # Update the weights here. The learning rate times the 
        # change in weights, divided by the number of records to average
        weights += learnrate * del_w / n_records

        # Printing out the mean square error on the training set
        if e % (epochs / 10) == 0:
            out = sigmoid(np.dot(features, weights))
            loss = np.mean((out - targets) ** 2)
            print("Epoch:", e)
            if last_loss and last_loss < loss:
                print("Train loss: ", loss, "  WARNING - Loss Increasing")
            else:
                print("Train loss: ", loss)
            last_loss = loss
            print("=========")
    print("Finished training!")
    return weights
    
weights = train_nn(features, targets, epochs, learnrate)
```

![image](https://user-images.githubusercontent.com/18595935/43362803-e188758e-932d-11e8-9afd-7d283b6cdd30.png)

## 35.9 计算测试 (Test) 数据的精确度

```python
# Calculate accuracy on test data
tes_out = sigmoid(np.dot(features_test, weights))
predictions = tes_out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))
```

输出结果为`Prediction accuracy: 0.825 `