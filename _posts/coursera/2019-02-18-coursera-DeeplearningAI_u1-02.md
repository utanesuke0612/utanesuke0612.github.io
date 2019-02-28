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

# 9. 逻辑回归梯度下降

# 10. 梯度下降例子

# 11. 向量化

# 12. 向量化示例

# 13. 逻辑回归向量化

# 14. 逻辑回归梯度输出

# 15. python中的广播

# 16. python和numpy中的vector

# 17. 如何使用Phthon notebooks

# 18. 逻辑回归成本函数


