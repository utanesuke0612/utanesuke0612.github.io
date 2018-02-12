---
layout: post
title: Uda-DataAnalysis-45-机器学习-整体回顾
date: 2018-01-16 15:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

本部分学完了，但是感觉没有入门，知道了如何在sklearn中调用函数，但是背后的实现原理还是没有理解。后续的原理理解，通过机器学习西瓜书等其他资料来完成。

# 1. 机器学习整体处理流程

![image](https://user-images.githubusercontent.com/18595935/36089370-db845dac-101e-11e8-8008-b1e9686bddc3.png)

1. 整个处理流程分为如下四个部分
2. 第一个阶段中，需要思考数据是否足够，定义问题是否清晰，另外是有有足够和正确的特征来回答提出的问题
3. 特征阶段，通过各种方式对特征进行处理，比如主成分分析
4. 将处理后的特征提供给算法进行处理
5. 算法是机器学习的核心部分，如果有标签则是监督算法，没有标签则为非监督算法。
6. 监督算法中，根据输出的不同，如果是无序或是离散的输出，可以使用决策树以及SVM等算法。如果是连续或有序的输出，可以使用各种回归算法
7. 如果是无标签数据，采用非监督算法，比如K-mean聚类等
8. 使用算法计算出模型后，进行验证，验证有各种方式，如F1 score,SSE/r**2,以及k-fold等。
9. 注意上面的流程是不断迭代的过程，前面的过程，可能会根据后续过程的结果再次优化。


# 2. 内容回顾

## 2.1 朴素贝叶斯分类（Naive Bayesian classification)

参考[Uda-DataAnalysis-32-机器学习-朴素贝叶斯](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-32-Bayes/)

是一种输出数据为离散或无序的监督算法(标签数据)。

朴素贝叶斯分类是一种十分简单的分类算法，叫它朴素贝叶斯分类是因为这种方法的思想真的很朴素，朴素贝叶斯的思想基础是这样的：对于给出的待分类项，求解在此项出现的条件下各个类别出现的概率，哪个最大，就认为此待分类项属于哪个类别。通俗来说，就好比这么个道理，你在街上看到一个黑人，我问你你猜这哥们哪里来的，你十有八九猜非洲。为什么呢？因为黑人中非洲人的比率最高，当然人家也可能是美洲人或亚洲人，但在没有其它可用信息下，我们会选择条件概率最大的类别，这就是朴素贝叶斯的思想基础。

![image](https://user-images.githubusercontent.com/18595935/35101633-9679094e-fca3-11e7-9058-c3b51d3c7e8b.png)

利用上述公式进行解释的话:

- 需要求解 P(非洲|黑人)，即已知他是黑人，计算他来自非洲的概率
- 待求解：P(黑人|非洲)，非洲里黑人的概率
- 待求解：P(非洲)，即街上出现非洲人的概率
- 待求解：P(黑人)，即街上出现黑人的概率

如果考虑其他地区，如欧洲，美洲等，分别计算获取最高概率的地区。

- 示例代码：

```python
# 创建NB朴素贝叶斯分类器
clf = GaussianNB()

# 训练分类器
clf.fit(features_train,labels_train)

# 使用分类器预测
pred = clf.predict(features_test)
```

## 2.2 SVM(Support vector machine 支持向量机)

参考[Uda-DataAnalysis-33-机器学习-SVM(Support vector machine 支持向量机)](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-33-SVM/)

SVM与上面的朴素贝叶斯一样，是一种输出数据为离散或无序的监督算法(标签数据)。

**什么是SVM？**

Support Vector Machine，一个普通的SVM就是一条直线，用来完美划分linearly separable的两类，但这又不是一条普通的直线，这是无数条可以分类的直线中最完美的，因为它恰好在两个类的中间，距离两个类的点一样远。

![image](https://user-images.githubusercontent.com/18595935/36091973-0b60b7b4-1029-11e8-89be-155cdd22e973.png)

示例代码如下：

```python
>>> from sklearn import svm
>>> X = [[0, 0], [1, 1]]
>>> y = [0, 1]
>>> clf = svm.SVC()
>>> clf.fit(X, y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
>>> clf.predict([[2., 2.]])
array([1])
```

## 2.3 DecisionTrees(决策树)

参考[Uda-DataAnalysis-34-机器学习-DecisionTrees(决策树)](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-34-DecisionTrees/)

决策树与上面的朴素贝叶斯一样，是一种输出数据为离散或无序的监督算法(标签数据)。

决策树（decision tree）是一个树结构（可以是二叉树或非二叉树）。其每个非叶节点表示一个特征属性上的测试，每个分支代表这个特征属性在某个值域上的输出，而每个叶节点存放一个类别。使用决策树进行决策的过程就是从根节点开始，测试待分类项中相应的特征属性，并按照其值选择输出分支，直到到达叶子节点，将叶子节点存放的类别作为决策结果。

![image](https://user-images.githubusercontent.com/18595935/36092343-657bfcc6-102a-11e8-9420-2b3480bd466c.png)

示例代码如下：

```python
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
```

## 2.4 选择自己的算法(K近邻,random forest,adaboost)

参考[Uda-DataAnalysis-35-机器学习-选择自己的算法(K近邻,random forest,adaboost)](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-35-choose-algorithm/)

都属于监督分类算法。


## 2.5 数据集与问题

参考[Uda-DataAnalysis-36-机器学习-数据集与问题](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-36-dataset/)

## 2.6 回归(regression)

参考[Uda-DataAnalysis-37-机器学习-回归(regression)](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-37-regression/)

回归分析（regression analysis)是确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法。运用十分广泛，回归分析按照涉及的变量的多少，分为一元回归和多元回归分析；按照因变量的多少，可分为简单回归分析和多重回归分析；按照自变量和因变量之间的关系类型，可分为线性回归分析和非线性回归分析。如果在回归分析中，只包括一个自变量和一个因变量，且二者的关系可用一条直线近似表示，这种回归分析称为一元线性回归分析。如果回归分析中包括两个或两个以上的自变量，且自变量之间存在线性相关，则称为多重线性回归分析。

## 2.7 异常值

参考[Uda-DataAnalysis-38-机器学习-异常值](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-38-outlier/)

## 2.8 聚类

参考[Uda-DataAnalysis-39-机器学习-聚类](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-39-cluster/)

聚类分析(Clustering)是无监督学习的一种，目的是将一组数据点分类，但没有训练数据集，区别于有监督的分类分析(Classification)。


## 2.9 特征缩放

参考[Uda-DataAnalysis-40-机器学习-特征缩放](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-40-featureScaling/)

特征缩放是用来标准化数据特征的范围。特征缩放还可以使机器学习算法工作的更好。比如在K近邻算法中，分类器主要是计算两点之间的欧几里得距离，如果一个特征比其它的特征有更大的范围值，那么距离将会被这个特征值所主导。因此每个特征应该被归一化，比如将取值范围处理为0到1之间。

## 2.10 文本学习

参考[Uda-DataAnalysis-41-机器学习-文本学习](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-41-TextLearning/)

## 2.11 特征选择

参考[Uda-DataAnalysis-42-机器学习-特征选择](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-42-CreateFeature/)

特征选择( Feature Selection )也称特征子集选择( Feature Subset Selection , FSS )，或属性选择( Attribute Selection )。是指从已有的M个特征(Feature)中选择N个特征使得系统的特定指标最优化，是从原始特征中选择出一些最有效特征以降低数据集维度的过程,是提高学习算法性能的一个重要手段,也是模式识别中关键的数据预处理步骤。对于一个学习算法来说,好的学习样本是训练模型的关键。

## 2.12 主成分分析（PCA）

参考[Uda-DataAnalysis-43-机器学习-主成分分析（PCA）](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-43-PCA/)

主成分分析（Principal Component Analysis，PCA）， 是一种统计方法。通过正交变换将一组可能存在相关性的变量转换为一组线性不相关的变量，转换后的这组变量叫主成分。

## 2.13 交叉验证

参考[Uda-DataAnalysis-44-机器学习-交叉验证](http://road2autodrive.info/2018/01/16/Uda-DataAnalysis-44-cross-validation/)

交叉验证，有时亦称循环估计，是一种统计学上将数据样本切割成较小子集的实用方法。于是可以先在一个子集上做分析， 而其它子集则用来做后续对此分析的确认及验证。 一开始的子集被称为训练集。而其它的子集则被称为验证集或测试集。交叉验证的目标是定义一个数据集到“测试”的模型在训练阶段，以便减少像过拟合的问题，得到该模型将如何衍生到一个独立的数据集的提示。

