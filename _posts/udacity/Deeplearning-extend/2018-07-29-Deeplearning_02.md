---
layout: post
title: 深度学习入门-02-感知机(perceptron)
date: 2018-07-28 00:00:02
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

感知机是神经网络(深度学习)的起源算法，学习感知机的构造，就是学习深度学习的一种重要思想。

下图是接收两个输入信号的感知机例子，输入信号被送往神经元时，会被分别乘以固定权重，神经元会计算传送过来信号的总和，当总和超过某个界限值时，才会输出1，这也称为`神经元被激活`，这里将这个界限值称为阈值，用符合`θ`表示。
- 权重w是控制输入信号的重要性的参数
- 阈值`θ`是调整神经元被激活的容易程度的参数

![image](https://user-images.githubusercontent.com/18595935/43525940-0082e368-95de-11e8-820a-00246e9319c1.png)

# 1. 简单逻辑电路

![image](https://user-images.githubusercontent.com/18595935/43527991-e311a74c-95e2-11e8-8ee4-fabb865e2d5b.png)

三个线性的感知器，只有参数，即权重和阈值不同，其结构都是相同的，都可以用上面的公式来表示，但是第四个异或感知器，没有一条线性能够同时划分0和1，为非线性结构。

# 2. 感知机的实现

```python
import numpy as np
# 一般的实现
def AND1(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1*w2 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
# numpy矩阵实现
def AND2(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp<=0:
        return 0
    else:
        return 1
```

其他两个感知器的实现方式一样，只是参数和阈值不同。

```python
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp<=0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp<=0:
        return 0
    else:
        return 1
```

# 3. 感知机的局限性

上面的四个感知器中，有三个线性，一个非线性，非线性无法用一条直线分开，如下图所示用一条曲线分割而成的空间称为非线性空间。

![image](https://user-images.githubusercontent.com/18595935/43528817-cf45a95a-95e4-11e8-97f7-a82b421c90c2.png)

# 4. 多层感知机

如何实现上述的非线性呢，可以通过感知机的叠加层，如下图可以实现上述非线性的空间。


![image](https://user-images.githubusercontent.com/18595935/43529463-53ceb620-95e6-11e8-88b6-070cdb5d3f1e.png)

```python
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND2(s1,s2)
    return y

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))

```

输出为:

```python
0
1
1
0
```

叠加了多层的感知机也称为多层感知机(multi-layered perceptron)，通过叠加层，感知机能进行更加灵活的表示:

![image](https://user-images.githubusercontent.com/18595935/43529835-1a88ea92-95e7-11e8-8636-4651f5af00fb.png)


# 5. 小结

感知机是一种非常简单的算法，是学习神经网络的基础，通过叠加感知机能够进行复杂的非线性表示，理论上还可以表示计算机进行的处理。

- 感知机是具有输入和输出的算法，给定一个输入后，将输出一个既定的值。
- 感知机将权重和阈值设定为参数。
- 使用感知机可以表示与/或等逻辑电路。
- 异或无法通过单层感知机来表示，可以通过二层感知机表示异或门。
- 单层感知器只能表示非线性空间，而多层感知机可以表示非线性空间。
