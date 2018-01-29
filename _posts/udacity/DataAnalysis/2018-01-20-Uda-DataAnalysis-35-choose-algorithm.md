---
layout: post
title: Uda-DataAnalysis-35-机器学习-选择自己的算法(K近邻,random forest,adaboost)
date: 2018-01-16 05:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 2. 为何要独自学习新算法？

任何数据分析师具备的一项关键技能就是不断从机器学习中得到新的认识，这也是本节课的学习目标。
这节课的内容是一个迷你项目。目标是用你选择的算法来做地形分类，并由你自己进行研究和部署。

可选的算法(都属于监督分类算法)如下：

- k nearest neighbors（k 最近邻 或 KNN）
- random forest（随机森林）
- adaboost（有时也叫“被提升的决策树”）

可以对比上一个算法（朴素贝叶斯、SVM、决策树）所得出的准确率，并自行评估新的算法是否更好。

在` choose_your_own/your_algorithm.py `文件中寻找初始代码来准备你的数据。以下视频还给出了更多你应该遵循的算法和过程的细节，不过你需要自行去发现。

# 5. 调查过程

1. do some research! - get a general understanding

2. find sklearn documentation

3. deploy it 

4. use it to make predictions

5. evaluate it - what is the accuracy?

## 5.1 K近邻算法(k nearest neighbors)

k-近邻算法采用测量不同特征值之间的距离方法进行分类，它的工作原理是:
1. 存在一个样本数据集合，也称作训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一数据与所属分类的对应关系。
2. 输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本集中特征最相似数据(最近邻)的分类标签。

一般来说，我们只寻找样本数据集中前K个最相似的数据，这就是K-近邻算法中k的出处，通常K是不大于20的整数，最后选择出现次数最多的分类，作为新数据的分类。

k-近邻算法的优缺点如下：

- 优点: 精度高，对异常值不敏感，无数据输入假定
- 缺点： 计算复杂度高，空间复杂度高
- 适用数据范围： 数值型和标称型

示例，每部电影的打斗镜头数、接吻镜头数以及电影评估类型

![image](https://user-images.githubusercontent.com/18595935/35471239-8c6973be-039a-11e8-997a-50c79014c4f0.png)

如果有一部新电影，通过其特征值，计算出该电影与上面的电影的距离，距离值如下：

- California Man 20.5
- He's Not Really into Dudes 18.7
- Beautiful Woman 19.2
- Kevin Longblade 115.3
- Robo Slayer 3000 117.4
- Amped II 118.9

如果K为3，则最上面三部电影为最近距离，其分类都是爱情片，所以新电影也是爱情片。

### 5.1.1 示例

参考[sklearn.neighbors.KNeighborsClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

```python
X = [[0], [1], [2], [3],[4],[4.2]]
y = [0, 0, 1, 1,2,3]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=4)
neigh.fit(X, y) 
print(neigh.predict([[3.1]]))
print(neigh.predict_proba([[3.1]]))
```

输出为：
```python
[1]
[[ 0.    0.5   0.25  0.25]]
```

1. `predict_proba(X)`: Return probability estimates for the test data X.

## 5.2 随机森林算法

参考[随机森林算法原理、源码分析及案例实战](https://www.ibm.com/developerworks/cn/opensource/os-cn-spark-random-forest/)

由多个决策树构成的森林，算法分类结果由这些决策树投票得到，决策树在生成的过程当中分别在行方向和列方向上添加随机过程，行方向上构建决策树时采用放回抽样（bootstraping）得到训练数据，列方向上采用无放回随机抽样得到特征子集，并据此得到其最优切分点，这便是随机森林算法的基本原理。下图给出了随机森林算法分类原理，从图中可以看到，随机森林是一个组合模型，内部仍然是基于决策树，同单一的决策树分类不同的是，随机森林通过多个决策树投票结果进行分类，算法不容易出现过度拟合问题。

![image](https://user-images.githubusercontent.com/18595935/35471558-aa56f026-03a0-11e8-86aa-a44b96b41702.png)

### 5.2.1 示例

参考[3.2.4.3.1. sklearn.ensemble.RandomForestClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

```python
from sklearn.ensemble import RandomForestClassifier

from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
print clf.feature_importances_
print clf.predict([[0, 0, 0, 0]])
```

输出如下:

```python
[ 0.17287856  0.80608704  0.01884792  0.00218648]
[1]
```

1. `feature_importances_`:Return the feature importances (the higher, the more important the
feature).

## 5.3 adaboost(被提升的决策树)

Adaboost是一种迭代算法，其核心思想是针对同一个训练集训练不同的分类器(弱分类器)，然后把这些弱分类器集合起来，构成一个更强的最终分类器（强分类器）。

其算法本身是通过改变数据分布来实现的，它根据每次训练集之中每个样本的分类是否正确，以及上次的总体分类的准确率，来确定每个样本的权值。将修改过权值的新数据集送给下层分类器进行训练，最后将每次训练得到的分类器最后融合起来，作为最后的决策分类器。使用adaboost分类器可以排除一些不必要的训练数据特征，并放在关键的训练数据上面。

### 5.3.1 示例

参考[sklearn.ensemble.AdaBoostClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)

```python
from sklearn.ensemble import AdaBoostClassifier

from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)
clf = AdaBoostClassifier()
clf.fit(X, y)
print clf.feature_importances_
print clf.predict([[0, 0, 0, 0]])
```

输出结果为:

```python
[ 0.32  0.44  0.08  0.16]
[1]
```

# 6. 使用上面的三类算法

将上面的三类算法，应用到地形数据中去：

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from time import time

################
print "\n#### KNeighbors"
t0 = time()

clf = KNeighborsClassifier(n_neighbors=16)
clf.fit(features_train,labels_train)
print "fit training time:", round(time()-t0, 3), "s"


t0 = time()

pred = clf.predict(features_test)
print "predict training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, pred)

print accuracy

################
print "\n#### RandomForest"

t0 = time()

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(features_train,labels_train)
print "fit training time:", round(time()-t0, 3), "s"


t0 = time()

pred = clf.predict(features_test)
print "predict training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, pred)

print accuracy

################
print "\n#### AdaBoost"

t0 = time()

clf = AdaBoostClassifier()
clf.fit(features_train,labels_train)
print "fit training time:", round(time()-t0, 3), "s"


t0 = time()

pred = clf.predict(features_test)
print "predict training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, pred)

print accuracy
```

输出结果如下:

```python
#### KNeighbors
fit training time: 0.003 s
predict training time: 0.002 s
0.94

#### RandomForest
fit training time: 0.021 s
predict training time: 0.005 s
0.92

#### AdaBoost
fit training time: 0.082 s
predict training time: 0.004 s
0.924
```

