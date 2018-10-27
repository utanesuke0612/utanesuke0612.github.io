---
layout: post
title: Uda-DeepLearning-U1-01-课程介绍
date: 2018-05-03 00:01:00
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

本套深度学习课程，共有6个单元:

- 深度学习简介
- 神经网络
- 卷积神经网络
- 循环神经网络
- 生成对抗网络
- 深度强化学习

本单元深度学习简介，包含5个部分：

- 欢迎学习此课程
- 应用深度学习
- Anaconda
- Jupyter notebook
- 矩阵数学和NumPy复习

# 5. 你将构建哪些项目

## 5.1 术语

- [卷积神经网络](http://neuralnetworksanddeeplearning.com/chap6.html)
- [递归神经网络](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [生成对抗网络](https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Generative-Adversarial-Networks)

## 5.2 构建项目

- 项目 1 - 你的第一个神经网络
> 构建一个简单的网络，帮助预测共享单车使用情况。

- 项目 2 - 图像识别
> 利用卷积神经网络对 CIFAR-10 数据库中的图像进行分类

- 项目 3 - 生成电视剧台词
> 利用循环神经网络生成新的电视剧台词。

- 项目 4 - 生成对抗网络项目
> 一个关于生成对抗网络 (GAN) 的项目。

- 项目 5 - 深度强化学习项目
> 设计一个可以在模拟环境中进行决策的系统。把强化学习应用到电子游戏和机器人开发等复杂的领域中。

# 6. 认识 Mat 和 Siraj

- Sampyl - [用 Python 编写的 MCMC Samplers](http://matatat.org/sampyl/index.html)。
- Siraj Raval 的[个人网站主页](http://www.sirajraval.com/)。

# 7. 课程结构大纲

**每周课程表**

下面是这门基石纳米学位会涵盖的学习内容。每一期课程，我们都根据上一期课程的经验调整我们的课程进度。我们了解每个学员都会有个性化的学习进度，我们在提供推荐的课程进度基础上，也同样提供更灵活、个性化的学习服务。在后面的介绍中你会了解到我们所有的学习服务。

- 第 1 周：深度学习简介

我们将首先简要介绍线性回归和机器学习，帮助你了解一些基本词汇，以便理解该领域的最新发展，并且让你明白深度学习在机器学习这一更宽泛领域中所处的位置。

- 第 2 周：搭建第一个神经网络

这一周你将学习如何使用 Numpy 从零开始搭建简单的神经网络。我们会介绍训练神经网络经常会用到的一些算法，例如梯度下降和反向传播算法。

本周，你将实践 第一个项目。在此项目中，你将使用一个简单的神经网络预测单车使用情况。

![image](https://user-images.githubusercontent.com/18595935/38199407-ad6b80d4-36cb-11e8-9a5a-6a4ba967a767.png)

- 第 3 周： 模型评估与验证

本周，你将跟随 我们的讲师学习深度学习中的数据准备技术，以及模型训练之后所需要的评估与验证手段。

- 第 4 周：情感分析与图形计算

本周，你将通过 Siraj 和我们的特邀讲师 Andrew Trask 的课程学习情感分析。你将使用神经网络预测某文本是正面的还是负面的。Andrew 将在项目一的基础上，向你展示如何预处理数据、做搭建网络的准备，来提高网络效率。

另外，TensorFlow 是最热门的搭建深度学习网络的框架。它基于图像计算，能高效地表达和完成训练网络中的矩阵运算。本课程中，你将搭建你自己的一个迷你版本的 TensorFlow，称为 MiniFlow，以帮助你深入理解反向传播，为使用 TensorFlow 做准备。

- 第 5 周： TensorFlow 入门

本课程中，你将学习 TensorFlow, 这是有 Google 开发的一个非常热门的深度学习框架。你将使用它来搭建一个简单的神经网络。

- 第 6 周：深度神经网络

本周中，首先你将了解到如何使用 AWS 和 FloydHub 等云计算工具，在 GPU 上运行你的网络。

其次，介绍深度神经网络。深度神经网络为众多领域带来了颠覆性的改变，包括计算机视觉、自然语言处理、人工智能等。本课程中，你将学习如何使用 TensorFlow 来搭建深度网络，对手写体数字进行分类。我们将介绍一些改进网络训练表现的常用方法，包括使用 dropout。

![image](https://user-images.githubusercontent.com/18595935/38199431-c4a25c50-36cb-11e8-87a2-48093391d477.png)


- 第 7 周：卷积神经网络

卷积神经网络是目前计算机视觉领域最佳的方法。这些网络可以检测和识别图像中的物体。你将学习如何在 TensorFlow 中构建卷积神经网络。

- 第 8 周 ：图像分类

你将要完成 第二个项目 ，在此项目中，你将构建一个卷积网络，以分类青蛙、飞机、汽车等图像。

![image](https://user-images.githubusercontent.com/18595935/38199438-c90eaa1e-36cb-11e8-9688-1f5b4a91d3bc.png)


- 第 9 周 ：自编码器

就像 Google 最近演示的那样，深度学习还可以用于大幅提升压缩技术。在本课程中，我们将使用深度学习构建自动编码器，发现数据的稀疏表示。

- 第 10周：迁移学习

深度学习的常见技术之一就是利用预先训练好的网络来解决新问题。例如，你可以使用已经经过巨大数据集训练的卷积网络，在一个小数据集上进行图像分类。这种方法称为迁移学习。本课程中，你将学习如何利用迁移学习对花卉图像进行分类，而无需从头开始训练整个网络。

- 第 11 周：循环神经网络

本课程中，你将了解循环神经网络——一种网络架构，特别适合处理序列型数据，如文本、音乐、时间序列数据等。你将构建一个循环神经网络，能够一字一字生成一段新的文本。

![image](https://user-images.githubusercontent.com/18595935/38199443-cd958ec2-36cb-11e8-9c78-32325a088720.png)


- 第 12 周：文字嵌入

在处理自然语言问题时，你总是会要处理海量的词汇。最终，这会导致计算效率低下。因此，我们会用较少的特征性表达来表示所有的词汇，成为词嵌入。词汇用向量表示，向量中包含该词语的实际语义信息。如想进一步了解词嵌入，你可以使用一个名为 Word2vec 的模型。


![image](https://user-images.githubusercontent.com/18595935/38199449-d23d0928-36cb-11e8-967b-6c99ef684c59.png)

- 第 13 周：用 RNN 进行情绪预测

本周中，你将学习如何使用循环神经网络预测文本情感。

- 第 14 周：

你也将开始着手完成 第三个项目， 使用循环神经网络生成电视剧台词。

- 第 15 周：序列到序列

神经网络是近年来推动机器翻译发展的重要基石。谷歌翻译和百度翻译的最新版本都使用了深度学习架构，可以自动将文本从一种语言翻译成另一种语言。这是通过一种称为“序列到序列学习”的过程而完成的。这也是我们本课中将要探讨的内容。

我们也将进一步研究序列到序列学习，构建我们自己的聊天机器人问答系统，可以回答用户的随机查询提问。

![image](https://user-images.githubusercontent.com/18595935/38199489-ee21af68-36cb-11e8-8f2c-c0976901cf86.png)

![image](https://user-images.githubusercontent.com/18595935/38199494-f116a17e-36cb-11e8-85eb-5ff613e772f2.png)

- 第 16 周：语言翻译

本周中你会在 第四个项目 中构建一个可以翻译文本的网络。

- 第 17 周：生成对抗网络（GAN）

生成对抗网络 (GANs) 是深入学习领域的一颗新星, 它是最前沿的图像生成模型。GAN 的发明者 Ian Goodfellow 将教你如何自己搭建生成对抗网络。

- 第 18 周： 图像生成

正如 Yann LeCun 所说，生成对抗网络是深度学习最根本的进步之一。你将探索这一当下最前沿的概念，生成一些可以以假乱真的图片，让人们不相信这些都是计算机生成的。

![image](https://user-images.githubusercontent.com/18595935/38199507-f839d66a-36cb-11e8-8a5d-0586adaf6b7c.png)


- 第 19 周：生成人脸

在第五个项目中，你将使用生成对抗网络来生成人脸图像。

- 第 20 周：使用 TensorBoard与强化学习

TensorBoard 是一种可视化工具，可用于检查你的网络。我们将向你展示如何使用 TensorBoard 来将你用 TensorFlow 中构建的图形，以及如何找到模型中的最佳参数。

深入学习领域出现的一些最有意思的进展就在强化学习领域。在强化学习中，网络并非对已有的数据库进行训练，而是在训练中根据实时接收的数据进行学习调整。我们将看看如何运用强化学习构建一个简单的玩游戏 AI ，让它能够打赢许多 Atari 游戏。

![image](https://user-images.githubusercontent.com/18595935/38199517-ff60f23e-36cb-11e8-8100-94c241c63b4f.png)

# 8. 课程结构

- 课程结构
深度学习基石纳米学位分为五个项目，每个项目都包含不同的主题。在开始这门纳米学位后，前两个项目可以立即查看。其它项目每两周开启一个。

- 简介
第一个项目是这个纳米学位的简介，会提及你将在课程中使用的一些工具。你也有机会应用一些深度学习模型去做超酷的事情，像转变某幅艺术品的风格，使其成为另一张图片。

我们将首先简要介绍线性回归和机器学习，帮助你了解一些基本词汇，以便理解该领域的最新发展，并且让你明白深度学习在机器学习这一更宽泛领域中所处的位置。

- 神经网络
在这个项目中，你将学习如何使用 Numpy 从零开始搭建简单的神经网络。我们会介绍训练神经网络经常会用到的一些算法，例如梯度下降和反向传播算法。

本周，第一个项目 已经上线了。在此项目中，你将使用一个简单的神经网络预测单车使用情况。

![image](https://user-images.githubusercontent.com/18595935/38199650-77e8cd62-36cc-11e8-8340-e37dd47768ee.png)

你将学习模型评估与验证，一个用于训练和评估神经网络的重要技巧。我们特邀了Grokking Deep Learning的作者 Andrew Trask 做讲师，开发一个用于处理文本和预测情绪的神经网络。

- 卷积神经网络
卷积神经网络是目前计算机视觉领域最佳的方法。这些网络可以检测和识别图像中的物体。你将学习如何在 TensorFlow 中构建卷积神经网络。你将要完成 第二个项目 ，在此项目中，你将构建一个卷积网络，以分类青蛙、飞机、汽车等图像。

![image](https://user-images.githubusercontent.com/18595935/38199652-7f47204a-36cc-11e8-957e-439b9b7c6a13.png)

你将会使用卷积神经网络去构建一个 自动编码器, 用于图片压缩和去噪的神经网络架构。然后你将使用预训练神经网络(VGGnet)， 对神经网络从未见过的花进行分类,，这个技术被称为迁移学习。

- 循环神经网络
本课程中，你将了解循环神经网络——一种网络架构，特别适合处理序列型数据，如文本、音乐、时间序列数据等。你将构建一个循环神经网络，能够一字一字生成一段新的文本。

![image](https://user-images.githubusercontent.com/18595935/38199684-9dcb6ad0-36cc-11e8-922f-173c96b42426.png)

From Andrej Karpthy's blog post on RNNs

然后，你将会学习词嵌入和实施 Word2Vec 模型，一个可以学习不同词汇间语义关系的神经网络。这将会提高神经网络处理文本的效率。

![image](https://user-images.githubusercontent.com/18595935/38199690-a1fef234-36cc-11e8-9251-cfe27338bec5.png)

你将结合词嵌入和循环神经网络预测电影评论的情感，一个自然语言处理里的常用案例。

在 第三个项目中，你将使用循环神经网络从中生成辛普森情节的电视剧台词。

![image](https://user-images.githubusercontent.com/18595935/38199697-a5dd93c4-36cc-11e8-83b5-ee2fd6de1d53.png)


第四个项目 将会让你使用序列到序列的模型去训练一个可以从英语翻译为法语的神经网络。这是循环神经网络的一个特别类型，它能读取一序列的数据，然后生成另一序列。

- 生成对抗网络（GAN）
生成对抗网络 (GANs) 是深入学习领域的一颗新星, 它是最前沿的图像生成模型，对理解真实世界的数据展现出难以置信的能力。这个网络可以用来构建生成图片的项目。如： CycleGAN

![image](https://user-images.githubusercontent.com/18595935/38199736-c8ac094e-36cc-11e8-8c57-5ee5496fb2a6.png)

GAN example from the pix2pix project.

GAN 的发明者 Ian Goodfellow 将教你如何自己搭建生成对抗网络。你将会学到半监督学习，一个用于训练分类缺失标签数据的技术。

在第五个项目中，你将使用生成对抗网络来生成人脸图像。

![image](https://user-images.githubusercontent.com/18595935/38199760-dbbb571a-36cc-11e8-8a1e-8f4a29f5c09d.png)

一个学生在第五个项目中生成的图片！

- 附加课程
在这个项目中，你将会学习可视化 TensorFlow 图形的 TensorBoard，也会使用强化学习训练一个玩电脑游戏的神经网络这样的主题。这个项目也会包含一些在未来深度学习的课程中有趣的主题。

# 10. 先修要求

对于这门课程，你只需具备以下先修条件：

- 必修条件
[中级 Python 经验](https://www.udacity.com/course/programming-foundations-with-python--ud036)。

- 选修条件
了解[多变量微积分](https://www.khanacademy.org/math/multivariable-calculus)和[线性代数](https://www.khanacademy.org/math/linear-algebra)。

不过，我们也提供了详细的数学资料，如果你们想深入了解这些概念背后的理论，可以参考。这类内容是选修知识，不妨碍你完成项目。但是，它可以帮助你丰富理论知识。

# 13. 第一周

**week1**

- Regression Models(Scikit-Learn)
- Intro to neural networks(perceptrons / Train networks)
- Your first neural network(numpy)

另外关于涉及到的概念:

- [Scikit-learn](http://scikit-learn.org/stable/)
一种非常热门的 Python 机器学习库。

- [感知器](https://en.wikipedia.org/wiki/Perceptron)
神经网络最简单的形式。

- [梯度下降](https://en.wikipedia.org/wiki/Gradient_descent)
机器学习算法根据预测结果的准确度进行自我改进的流程。你将在后续课程中详细了解这一概念。

- [反向传播](http://neuralnetworksanddeeplearning.com/chap2.html)
神经网络学习如何改善单个参数的流程。你将在后续课程中详细了解这一概念。

- [Numpy](http://www.numpy.org/)
一种非常热门的 Python 科学计算库。

- [TensorFlow](https://www.tensorflow.org/)
当下最热门的 Python 神经网络创建库之一，由 Google 维护。
