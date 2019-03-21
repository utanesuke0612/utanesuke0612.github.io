---
layout: post
title: Coursera-DeepLearning-U1-01-深度学习入门
date: 2019-05 まだ-18 01:01:00
categories: DeepLearning
tags: DeepLearning Coursera
---
* content
{:toc}

本套深度学习课程，共有5个单元:

1. [**Neural Networks and Deep Learning**](https://www.coursera.org/learn/neural-networks-deep-learning/home/welcome)，神经网络入门，能构建一个神经网络并通过数据训练它。
2. [Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization](https://www.coursera.org/learn/deep-neural-network/home/welcome)
3. [Structuring Machine Learning Projects](https://www.coursera.org/learn/machine-learning-projects/home/welcome)
4. [Convolutional Neural Networks](https://www.coursera.org/learn/convolutional-neural-networks/home/welcome)
5. [Sequence Models](https://www.coursera.org/learn/nlp-sequence-models/home/welcome)

第一单元分为四周：
- Week 1: Introduction
- Week 2: Basics of Neural Network programming 
- Week 3: One hidden layer Neural Networks
- Week 4: Deep Neural Networks


# 1. 神经网络中的监督学习

监督学习中，我们通过一组输入数据和已知标签的输出数据，得到这两者之间的关系。监督学习问题可以分为**回归问题**和**分类问题**。
- 回归问题：在一段连续值中预测结果，比如预测天气的温度
- 分类问题：预测出离散的结果，比如预测明天是晴天还是雨天。

下面是一些监督学习的例子：

![image](https://user-images.githubusercontent.com/18595935/53543709-ecf9af00-3b66-11e9-930e-49bb5884489c.png)

有不同类型的神经网络，比如：
1. 卷积神经网络CNN，常用于图片识别；
2. 以及递归神经网络RNN常用于一维序列数据，比如文本翻译等。
3. 在自动驾驶中，需要用到混合神经网络(Hybrid neural network)。
4. 广告点击或房价预测，使用标准神经网络

![image](https://user-images.githubusercontent.com/18595935/53544595-f9333b80-3b69-11e9-93c3-236553d6b431.png)

关于结构化数据与非结构化数据：

![image](https://user-images.githubusercontent.com/18595935/53543834-5a0d4480-3b67-11e9-8fb8-e91a03b82617.png)

# 2. 为什么深度学习会兴起？

主要是下面三个能力的提升：
1. 大数据量(带标签)
2. 计算力的增强
3. 算法的改善

从上往下依次为：
1. 绿色：大规模神经网络
2. 蓝色：中规模神经网络
3. 黄色：小规模神经网络
4. 红色：传统机器学习(SVM)

![image](https://user-images.githubusercontent.com/18595935/53544116-50d0a780-3b68-11e9-8097-3fc63dbdb411.png)

1. 有大量的数据数据可以训练神经网络
2. 有大量的带标签的数据

神经网络的训练是个迭代的过程：

更快的计算速度能更快迭代，更快改进新的算法：

![image](https://user-images.githubusercontent.com/18595935/53544132-5d550000-3b68-11e9-8cf5-3cd2bf6facda.png)


