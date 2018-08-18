---
layout: post
title: Uda-DataAnalysis-33-机器学习-SVM(Support vector machine 支持向量机)
date: 2018-01-16 02:00:01
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}


# 4. 好的分割线有什么特点

![image](https://user-images.githubusercontent.com/18595935/35180789-3f68801e-fdfa-11e7-8cb0-e6fba9c90530.png)

SVM就是找出这个分割线的过程，这个分割线离双方距离越远，这个分割线越好，越健壮，不容易出现分类误差。

# 6. SVMs 和棘手的数据分布

![image](https://user-images.githubusercontent.com/18595935/35182625-ed4da454-fe1b-11e7-9362-64bc2f80e62d.png)

SVM的首要目标是保证分类正确，在分类正确的前提下，对间隔进行最大化。

# 7. SVM 对异常值的响应

![image](https://user-images.githubusercontent.com/18595935/35182667-82d0e07c-fe1c-11e7-8c91-862c28348be9.png)

尽力给出最接近的结果，允许少量的异常值 (Outliers)

# 10. SKlearn 中的 SVM

参考官网[1.4. Support Vector Machines](http://scikit-learn.org/stable/modules/svm.html)

示例代码中显示，使用流程也与上面贝叶斯的类似，先创建分类器，再训练，最后进行预测。

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

# 12. SVM编码

- 创建分类器 -> 拟合 -> 预测 -> 评价精度：

```python
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(kernel="linear")

#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
clf.fit(features_train,labels_train)

#### store your predictions in a list named pred
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

def submitAccuracy():
    return acc
```

- 输出结果为：

```python
Good job! Your output matches our solution.
Here's your output:
0.92
```

# 13. 非线性SVM

![image](https://user-images.githubusercontent.com/18595935/35183037-cd4f0eac-fe22-11e7-80b2-65e30904cd3f.png)

如上图所示，SVM能做出很复杂的分类。


# 16. 可视化新特征

![image](https://user-images.githubusercontent.com/18595935/35183095-b55729a0-fe23-11e7-947a-4aae5da5df84.png)

如上图，添加了一个新的特征 z，即原始的sqrt(x*x + y*y)，表示原点到点之间的距离，通过新加的特征z和原始特征x，可以用svm画出一条分割线。

# 18. 练习创建新特征

如下图，与上面一样，直接通过原始特征无法得到线性分离线，通过添加新的特征`|x|`，得到线性分离线。

![image](https://user-images.githubusercontent.com/18595935/35189524-67b84cd0-fe8f-11e7-9620-90737b5d21ed.png)


# 19. 核函数

上面的16和18的示例所示，通过添加新特征可以得到特征分离线，但是多数情况下不知道要添加什么样的新特征。
通过核函数可以实现这一过来，如下图:

![image](https://user-images.githubusercontent.com/18595935/35189502-0433345e-fe8f-11e7-9e87-d875a89b5a4a.png)

# 20. 尝试选择各种核

上面的示例中创建了线性核，在SVM中还有多种核，比如poly(二项式),rbf(径向基函数),sigmoid等，详细参考[1.4. Support Vector Machines](http://scikit-learn.org/stable/modules/svm.html)

```python
from sklearn.svm import SVC
clf = SVC(kernel="linear")
```

例如下图就分别是由linear线性和rbf径向基函数创建：

![image](https://user-images.githubusercontent.com/18595935/35183037-cd4f0eac-fe22-11e7-80b2-65e30904cd3f.png)

对于SVM来说，有三种参数需要调整：
- kernel (linear,rbf,poly...)
- C:Controls tradeoff between smooth decision boundary and classifying training points correctly,控制平滑边界与正确分类的平衡
- gamma

# 22. 练习: SVM C参数

利用上一讲19的示例，将分类器修改为SVM的rbf方式，根据不同的C参数，求解出不同的分割线，如下图：

![image](https://user-images.githubusercontent.com/18595935/35194468-626cd24c-fef7-11e7-9ed2-4c62455ad402.png)

可以看出C越大，就越能切分到更多的正确的点。

# 23. 过拟合

![image](https://user-images.githubusercontent.com/18595935/35194521-51008174-fef8-11e7-8e15-d6dcfdc22287.png)

上面黑色的曲线，虽然正确的进行了分类，但是曲线非常奇怪，这种情况就叫做过拟合，通过调整kernel,C,gamma可以避免过度拟合。

# 27. SVM 作者 ID 准确率 / 耗时

转到 svm 目录，查找初始代码 (svm/svm_author_id.py)。使用 sklearn SVC分类器进行导入、创建、训练和预测。在创建分类器时使用线性内核，分类器的准确率是多少？


```python
from sklearn.svm import SVC
clf = SVC(kernel="linear")

#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
t0 = time()
clf.fit(features_train,labels_train)
print "fit training time:", round(time()-t0, 3), "s"

#### store your predictions in a list named pred
t0 = time()
pred = clf.predict(features_test)
print "predict training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print acc
```

- 输出结果如下:

```python
no. of Chris training emails: 7936
no. of Sara training emails: 7884
fit training time: 187.351 s
predict training time: 19.866 s
0.984072810011
```

通过上面的计时，与上一节的42(naive_bayes)对比，耗时上比朴素贝叶斯大大增加:

Exact times may vary a bit, but in general, the SVM is MUCH slower to train and use for predicting.

# 29. 更小的训练集

加快算法速度的一种方式是在一个较小的训练数据集上训练它。这样做换来的是准确率几乎肯定会下降。让我们更具体地探讨这个问题：在训练分类器之前，立即加入以下两行。 

```python
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
```

这两行有效地将训练数据集切割至原始大小的 1%，丢弃掉 99% 的训练数据。你可以使其他所有代码保持不变。

再次运行代码，输出结果为：

```python
fit training time: 0.1 s
predict training time: 1.094 s
0.884527872582
```

运行时间缩短不少，但是精度也同时降低了。精度与速度的平衡，需要根据不同的业务要求进行选取：

Voice recognition and transaction blocking need to happen in real time, with almost no delay.  There's no obvious need to predict an email author instantly.

# 31. 部署 RBF 内核 / 优化C参数

如果修改为rbf内核，`clf = SVC(kernel="rbf")`

```python
fit training time: 0.12 s
predict training time: 1.313 s
0.616040955631
```

下面通过调整C参数，看看正确率的变化：

- C=10

```python
fit training time: 0.124 s
predict training time: 1.295 s
0.616040955631
```

- C=100

```python
fit training time: 0.124 s
predict training time: 1.295 s
0.616040955631
```

- C=1000

```python
fit training time: 0.118 s
predict training time: 1.246 s
0.821387940842
```

- C=10000

```python
fit training time: 0.117 s
predict training time: 1.062 s
0.892491467577
```


上面都是使用的1/100的数据集，现在恢复为完整数据集，使用rbf内核，以及C为10000的参数，得到的结果如下，其准确率大大提升：

```python
fit training time: 120.092 s
predict training time: 11.973 s
0.990898748578
```

# 35. 从 SVM 提取预测

添加如下，输出预测结果，得到结果为`1 0 1`，1代表Chris，0代表Sara。

```python
print pred[10],pred[26],pred[50]
```


# 36. 预测有多少 Chris 的邮件？

添加如下判断代码, 判断属于“Chris”(1)的邮件数目：

```python
n = 0
for result in pred:
	if result == 1:
		n = n + 1

print "Chris:",n
```

输出结果为：

```python
fit training time: 125.144 s
predict training time: 12.211 s
Chris 877
0.990898748578
```

# 39. 部署 SVM 最后提醒

对于这一具体问题，朴素贝叶斯不仅更快，而且通常比 SVM 更出色。当然，SVM 更适合许多其他问题。你在第一次求解问题时就知道该尝试哪个算法，这是机器学习艺术和科学性的一个体现。除了选择算法外，视你尝试的算法而定，你还需要考虑相应的参数调整以及过拟合的可能性（特别是在你没有大量训练数据的情况下）。

我们通常建议你尝试一些不同的算法来求解每个问题。调整参数的工作量很大，但你现在只需要听完这堂课，我们将向你介绍 GridCV，一种几乎能自动查找最优参数调整的优秀 sklearn 工具。