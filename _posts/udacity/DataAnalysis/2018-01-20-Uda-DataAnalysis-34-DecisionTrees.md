---
layout: post
title: Uda-DataAnalysis-34-机器学习-DecisionTrees(决策树)
date: 2018-01-16 03:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 3. 多元线性问题

决策树就是要构造右边的图形的过程：

![image](https://user-images.githubusercontent.com/18595935/35224773-7b9070a8-ffc9-11e7-9f24-4df75dbb25e9.png)

# 7. 构建决策树

![image](https://user-images.githubusercontent.com/18595935/35225048-9029dff8-ffca-11e7-94ac-ecb7fdce9add.png)

# 8. 决策树编码

参考 [1.10. Decision Trees](http://scikit-learn.org/stable/modules/tree.html)

- studentMain.py

```python
#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

#### grader code, do not modify below this line
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())

```

- classifyDT.py (练习代码)

```python
def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)
    
    return clf
```

最后输出图形如下:

![image](https://user-images.githubusercontent.com/18595935/35225464-b6b01b78-ffcb-11e7-9907-eb7d398a206d.png)

# 9. 决策树准确性

```python
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

#### your code goes here

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

# 计算精度
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

### be sure to compute the accuracy on the test set
    
def submitAccuracies():
  return {"acc":round(acc,3)}
```

输出结果如下:

```python
Good job! Your output matches our solution.
Here's your output:
{'acc': 0.912}
```

# 10. 决策树参数

参考 [sklearn.tree.DecisionTreeClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)

因为最小sample分割数为2，所以红色的leaf无法继续分割了

![image](https://user-images.githubusercontent.com/18595935/35226090-9553c46e-ffcd-11e7-861c-7215966c596b.png)


# 11. 最小样本分割

可以看出，`min_samples_split`越小，决策树分割越详细：

![image](https://user-images.githubusercontent.com/18595935/35226444-ae135e14-ffce-11e7-86ed-c456f0926cf4.png)

# 12. 决策树准确性

根据上面的参数，创建两个分类器，分布进行预测后计算其精度：

```python
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn import tree
# 第一个分类器
clf_split_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf_split_2 = clf_split_2.fit(features_train, labels_train)
pred_split_2 = clf_split_2.predict(features_test)

# 第二个分类器
clf_split_50 = tree.DecisionTreeClassifier(min_samples_split=50)
clf_split_50 = clf_split_50.fit(features_train, labels_train)
pred_split_50 = clf_split_50.predict(features_test)

# 计算预测精度
from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(pred_split_2, labels_test)
acc_min_samples_split_50 = accuracy_score(pred_split_50, labels_test)

def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}

```

输出结果如下：

```python
{"message": "{'acc_min_samples_split_50': 0.912, 'acc_min_samples_split_2': 0.908}"}
```

# 13. 数据杂质与熵

Entropy(熵)是确定在何处分割数据的概念。

definition: measure of impurity（杂质） in a bunch of examples.

- 定义公式如下，Pi是在某个类i中样本的数量的比例(`该分类数目 / 总样本数目`)。

1. 如果所有样本都属于同一个类，则`entropy = 0`
2. 如果所有样本,被平均分配到各个类别中，则`entropy = 1`，这是熵的数学最大值。

![image](https://user-images.githubusercontent.com/18595935/35278604-ed32ee38-008d-11e8-91ae-1c6322f33f40.png)

# 16. 熵计算

![image](https://user-images.githubusercontent.com/18595935/35279552-b81e8880-0090-11e8-97c2-7472bed3c45b.png)

最终得到的熵是1.0,即最不纯的状态。
If we have two class labels,the most impure situation we could have is where the examples are evenly split between the two class labels.（被平均分配到两个class中）

```python
>>> import math
>>> -0.5*math.log(0.5,2) - 0.5*math.log(0.5,2)
1.0
```

另外，回顾下log的概念，就是求幂的过程：

```python
>>> math.log(10,10)
1.0
>>>
>>> math.log(10,100)
0.5
>>> math.log(100,10)
2.0
>>> math.log(0.5,2)
-1.0
```

# 21. 信息增益(information gain)

信息增益的计算公式参考下图。

# 24. 信息增益计算（第 3 部分）

![image](https://user-images.githubusercontent.com/18595935/35336262-1db8c474-015b-11e8-9037-63b4804a92d3.png)

参照上面的定义，该分支下只有一个类别，故熵为0

# 25. 信息增益计算（第 5 部分）

![image](https://user-images.githubusercontent.com/18595935/35336648-69b36dd8-015c-11e8-8e16-629cc4c80a61.png)


# 26. 信息增益计算（第 6 部分）

![image](https://user-images.githubusercontent.com/18595935/35336895-1fd0a7f2-015d-11e8-8034-1a044e8a43d8.png)


# 29. 信息增益计算（第 8 部分）

![image](https://user-images.githubusercontent.com/18595935/35337103-abe4b97c-015d-11e8-8388-f5d86e08ef4f.png)

类似的，参考上面第16部分，bumpy被平均分配在slow和fast下，熵结果为1，smooth同理。

# 30. 信息增益计算（第 9 部分）

这时计算出来的信息增益为：

`entropy(parent) - [weighted average]entropy(children) = 1 - ( (1/2)*1 + (1/2)*1 ) = 0`

# 31. 信息增益计算（第 10 部分）

![image](https://user-images.githubusercontent.com/18595935/35337521-cbad8972-015e-11e8-8d8a-0175cebe96f5.png)

两个yes都分配在同一个class中，两个no也都分配在同一个class中，所以其熵都是0，所以最后得到的信息增益是1.0，这是最好的信息增益，所以应该在这里进行分割。

# 33. 偏差方差(bias-variance)困境

- 高偏差机器学习算法会忽略数据，无论通过何种方式，它的操作都不会有任何区别。

- 高方差:对数据极度敏感，只能复制曾经见过的东西，新的状况无法处理

机器学习的艺术在于平衡上述的偏差与方差。

决策树的缺点是容易过度拟合，尤其是在有大量特征数据的时候，所以对特征数据的适当选取十分重要。

# 37. 计算准确率和确定特征数量

控制算法复杂度的另一种方法是通过你在训练/测试时用到的特征数量。算法可用的特征数越多，越有可能发生复杂拟合。
数据中的特征数：` len(features_train[0])`。

```python
from sklearn import tree

t0 = time()
clf = tree.DecisionTreeClassifier(min_samples_split=40)
print "fit training time:", round(time()-t0, 3), "s"

clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "predict training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print acc
print len(features_train[0])
```

输出为：

```python
fit training time: 0.0 s
predict training time: 37.511 s
0.977815699659
3785
```

# 39. 更改特征数量

进入 ../tools/email_preprocess.py，然后找到类似此处所示的一行代码： 

```python
selector = SelectPercentile(f_classif, percentile=10)
```

将百分位数从 10 改为 1，然后运行 dt_author_id.py，输出为如下，其特征数量减少为了1/10，另外训练时间也大大减少，但是精度变小：

```python
fit training time: 0.0 s
predict training time: 3.22 s
0.967007963595
379
```