---
layout: post
title: Uda-DataAnalysis-32-机器学习-朴素贝叶斯
date: 2018-01-16 01:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 3. 练习：监督分类示例

![image](https://user-images.githubusercontent.com/18595935/35045549-889b9c50-fbd7-11e7-93ad-e2fd9f754b2a.png)

- 监督分类

又称训练场地法、训练分类法，是以建立统计识别函数为理论基础、依据典型样本训练方法进行分类的技术，即根据已知训练区提供的样本，通过选择特征参数，求出特征参数作为决策规则，建立判别函数以对各待分类影像进行的图像分类，是模式识别的一种方法。

- 非监督分类

指人们事先对分类过程不施加任何的先验知识，而仅凭数据（遥感影像地物的光谱特征的分布规律），即自然聚类的特性，进行“盲目”的分类。

银行数据中寻找欺诈，以及学生分组属于分监督分类。

# 7. 地形数据分类：坡度和颠簸度

![image](https://user-images.githubusercontent.com/18595935/35046312-ef34478a-fbd9-11e7-9f06-323035e5ce01.png)

地形数据常用来进行速度的控制。

# 13. 从散点图到决策面

![image](https://user-images.githubusercontent.com/18595935/35046579-c5565ccc-fbda-11e7-93ae-3c0df9c3330f.png)

本课就是希望通过朴素贝叶斯方法，找到这个决策面。

# 18. GaussianNB使用示例

```python
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> Y = np.array([1, 1, 1, 2, 2, 2])
>>> from sklearn.naive_bayes import GaussianNB

# 创建一个分类器
>>> clf = GaussianNB()

# 训练分类器
>>> clf.fit(X, Y)
GaussianNB(priors=None)

# 预测结果
>>> print(clf.predict([[-0.8, -1]]))
[1]
```

# 19. 有关地形数据的GaussianNB 部署

```python
def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    ### your code goes here!
    
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train,labels_train)
    return clf

```

运行测试程序后得到结果:

![image](https://user-images.githubusercontent.com/18595935/35048460-7b178324-fbe0-11e7-8784-17e971398186.png)

# 20. 计算 GaussianNB 准确性

```python
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train,labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    
    from sklearn.metrics import accuracy_score
    
    accuracy = accuracy_score(labels_test, pred)
    return accuracy
```

计算结果为:

```python
Good job! Your output matches our solution.
Here's your output:
0.884
```



# 99. 术语

- `supervised classification`: 监督分类
- `emulate`:模仿
