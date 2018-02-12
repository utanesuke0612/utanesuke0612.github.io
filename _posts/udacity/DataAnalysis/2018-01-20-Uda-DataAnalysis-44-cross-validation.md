---
layout: post
title: Uda-DataAnalysis-44-机器学习-交叉验证
date: 2018-01-16 14:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 3. 在 Sklearn 中训练/测试分离

参考[3.1. Cross-validation: evaluating estimator performance](http://scikit-learn.org/stable/modules/cross_validation.html)


```python
# 
>>> import numpy as np
>>> from sklearn.model_selection import train_test_split
>>> from sklearn import datasets
>>> from sklearn import svm

# 
>>> iris = datasets.load_iris()
>>> iris.data.shape, iris.target.shape
((150L, 4L), (150L,))

>>> X_train, X_test, y_train, y_test = train_test_split(
... iris.data, iris.target, test_size=0.4, random_state=0)

>>> X_train.shape, y_train.shape
((90L, 4L), (90L,))
>>> X_test.shape, y_test.shape
((60L, 4L), (60L,))

# 
>>> clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
>>> clf.score(X_test, y_test)
0.96666666666666667

```

# 4. 练习4-7 何处使用训练与测试数据

- 下面是一个整体的流程，以及各个流程中所需要使用到的数据：

![image](https://user-images.githubusercontent.com/18595935/36073928-b63fe03c-0f7b-11e8-8b18-73e4c5b3b20b.png)

# 8. K 折交叉验证

1. 将数据分成K份，比如10份
2. 取1份作为验证数据集，其余9份作为训练数据集，进行训练
3. 循环将剩下的9份数据中，每份数据都作为一次验证数据集进行训练
4. 将训练完毕的数据取平均

![image](https://user-images.githubusercontent.com/18595935/36074048-b35ae0f4-0f7d-11e8-874c-bbcb1f8e3e55.png)

||Train/Test|10-fold C.V.|
|:--|--:|:--:|
|min.training time|`⭕`|`☓`|
|min run time|`☓`|`⭕`|
|max accuracy|`☓`|`⭕`|

# 9. Sklearn 中的 K 折 CV

- 参考代码：

![image](https://user-images.githubusercontent.com/18595935/36074225-87a4d3e0-0f80-11e8-9528-d87d367ef3bb.png)

# 12. Sklearn 中的 GridSearchCV

GridSearchCV 用于系统地遍历多种参数组合，通过交叉验证确定最佳效果参数。它的好处是，只需增加几行代码，就能遍历多种组合。

```python
>>> from sklearn import svm, grid_search, datasets
>>> iris = datasets.load_iris()

# 参数字典以及他们可取的值，会自动生成一个不同（kernel、C）参数值组成的“网格”:
>>> parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

# 分类器创建好了，传达算法 (svr) 和参数 (parameters) 字典来尝试，它生成一个网格的参数组合进行尝试。
>>> svr = svm.SVC()
>>> clf = grid_search.GridSearchCV(svr, parameters)

# 拟合函数现在尝试了所有的参数组合，并返回一个合适的分类器，自动调整至最佳参数组合。
>>> clf.fit(iris.data, iris.target)
GridSearchCV(cv=None, error_score='raise',
       estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False),
       fit_params={}, iid=True, n_jobs=1,
       param_grid={'kernel': ('linear', 'rbf'), 'C': [1, 10]},
       pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)

# 通过 clf.best_params_ 来获得参数值
>>> clf.best_params_
{'kernel': 'linear', 'C': 1}

```

# 13. 练习：Sklearn 中的 GridSearchCV

参考[Faces recognition example using eigenfaces and SVMs](http://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

```python

# #############################################################################
# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)
```

参考上述代码中的`param_grid`，对`C`和`gamma`进行了训练。

# 17. 第一个（过拟合）POI 识别符

创建决策树分类器（仅使用默认参数），在所有数据（你将在下一部分中修复这个问题！）上训练它，并打印出准确率。 

```python
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
pred = clf.predict(features)

# 
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels)

print acc
```

结果是`0.989473684211`

# 18. 部署训练/测试机制

参考[3.1. Cross-validation: evaluating estimator performance](http://scikit-learn.org/stable/modules/cross_validation.html)

现在，你将添加训练和测试，以便获得一个可靠的准确率数字。 使用 sklearn.cross_validation 中的 train_test_split 验证； 将 30% 的数据用于测试，并设置 random_state 参数为 42（random_state 控制哪些点进入训练集，哪些点用于测试；将其设置为 42 意味着我们确切地知道哪些事件在哪个集中； 并且可以检查你得到的结果）。更新后的准确率是多少？

- 全代码如下：

```python
#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### it's all yours from here forward!  
# 练习17：第一个（过拟合）POI 识别符
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
pred = clf.predict(features)


from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels)

print "before:",acc

print "##########:",len(labels)
print "##########:",len(features)

## 练习18：部署训练/测试机制
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features,labels,test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
pred = clf.predict(X_test)

acc = accuracy_score(pred, y_test)

print "After:",acc
```

- 输出结果如下：

```python
before: 0.989473684211
##########: 95
##########: 95
After: 0.724137931034
```