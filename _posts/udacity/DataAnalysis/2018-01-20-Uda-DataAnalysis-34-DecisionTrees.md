---
layout: post
title: Uda-DataAnalysis-34-机器学习-【ing】-DecisionTrees(决策树)
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