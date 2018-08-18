---
layout: post
title: Uda-DataAnalysis-32-机器学习-朴素贝叶斯(Naive Bayesian)
date: 2018-01-16 01:00:01
categories: 数据分析
tags: R DataAnalysis 
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

# 23. 贝叶斯定理

![image](https://user-images.githubusercontent.com/18595935/35101633-9679094e-fca3-11e7-9058-c3b51d3c7e8b.png)

即如上的公式，推导过程参考[贝叶斯推断及其互联网应用（一）：定理简介](http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_one.html)

 贝叶斯定理之所以有用，是因为我们在生活中经常遇到这种情况：我们可以很容易直接得出P(B|A)，P(A|B)则很难直接得出，但我们更关心P(A|B)，贝叶斯定理就为我们打通从P(B|A)获得P(A|B)的道路。
 (P(A|B)表示事件B已经发生的前提下，事件A发生的概率，叫做事件B发生下事件A的条件概率)

# 24. 练习: 癌症测试

![image](https://user-images.githubusercontent.com/18595935/35101124-af26640c-fca1-11e7-9219-a3d715380428.png)

示例: 得癌症的几率是0.01，另外癌症的情况下阳性的概率是0.9，如果不是癌症是阴性的概率是0.9.
某个人的测试结果是阳性，请问其为癌症的概率是多少？

- 贝叶斯规则

![image](https://user-images.githubusercontent.com/18595935/35101259-3bbf7e76-fca2-11e7-8aa2-1f5882db7dfa.png)

先验概率 * 测试得到的结论 => 后验概率

![image](https://user-images.githubusercontent.com/18595935/35101508-2cad0470-fca3-11e7-9ddd-abe1f71f9406.png)

小圆圈表示癌症，大圆圈表示阳性，中间重叠部分表示阳性且癌症，所以在阳性下得癌症的几率是 `0.009 / (0.009 + 0.099) = 0.0833`。

如果根据贝叶斯定理进行计算的话：

```python
# 已知
P(C) = 0.01
P(P|C) = 0.9
P(N|not C) = 0.9

# 贝叶斯定理
P(P|C) = P(C|P)*P(P) / P(C)

# 要计算P(C|P)，需要先求解P(P)，即阳性的概率，其计算依据下图的公式
P(P) = P(C)*P(P|C) + P(not C)*P(P|not C) = 0.01*0.9 + 0.99*(1-0.9) = 0.09 + 0.099 = 0.108

# 将已知概率和求解出来的概率代入，得到阳性下癌症的概率
0.9 = P(C|P) * 0.108 /0.01

P(C|P) = 0.009/0.108 = 0.0833
```

![image](https://user-images.githubusercontent.com/18595935/35102256-b93c5524-fca5-11e7-88bf-8e5a87dc5e34.png)

# 28. 规范化

![image](https://user-images.githubusercontent.com/18595935/35103430-277360fc-fca9-11e7-9416-9fa6ad841ef0.png)

同样根据贝叶斯原理计算：

- `0.009 / 0.108 = 0.0833`
- `0.099 / 0.108 = 0.9167`

# 30. 贝叶斯规则图

![image](https://user-images.githubusercontent.com/18595935/35103715-0a4d1634-fcaa-11e7-8933-bbce12f3537b.png)

# 31. 用于分类的贝叶斯规则

![image](https://user-images.githubusercontent.com/18595935/35180478-a03b6768-fdf4-11e7-8a6f-845cbd6bc043.png)

计算概率:

```
CHRIS = 0.1 * 0.1 * 0.5 = 0.005
SARA = 0.3 * 0.3 * 0.5 = 0.03
```

# 33. 后验概率

![image](https://user-images.githubusercontent.com/18595935/35180495-18929d3a-fdf5-11e7-9fe5-b3cde8138205.png)

根据贝叶斯定理计算:

```python
P(CHRIS | "LIFE DEAL") = P("LIFE DEAL" | CHRIS)*P(CHRIS) / P("LIFE DEAL")

= P("LIFE DEAL" | CHRIS)*P(CHRIS) / P("LIFE DEAL" | CHRIS)*P(CHRIS) + P("LIFE DEAL" | SARA)*P(SARA)

= 0.08*0.5 / (0.08*0.5 + 0.06*0.5)

= 0.04 / 0.07 =  0.57

```

类似，

![image](https://user-images.githubusercontent.com/18595935/35180507-5728d41a-fdf5-11e7-892d-227e6986ad04.png)

```python
P(CHRIS |"LOVE DEAL") = P("LOVE DEAL" | CHRIS)*P(CHRIS) / P("LOVE DEAL")

= P("LOVE DEAL" | CHRIS)*P(CHRIS) / P("LOVE DEAL" | CHRIS)*P(CHRIS) + P("LOVE DEAL" | SARA)*P(SARA)

= 0.08*0.5 / (0.08*0.5 + 0.1*0.5)

= 0.04 / 0.09 =  0.44

```


# 35. 为什么叫做朴素贝叶斯

![image](https://user-images.githubusercontent.com/18595935/35180489-0562375c-fdf5-11e7-88cc-46c805be1544.png)

Label A和Lable B中，有每个词出现的频率，给定一段文字，计算各个单词出现的概率，比较大小。
在这个概率的计算中，没有考虑单词的顺序，所以叫做朴素贝叶斯。


# 41. 迷你项目 - 准备工作

1. cmd中安装 `pip install scikit-learn` 和 `pip install nltk`
2. `C:\python2.7`中打开python2.7,使用`import sklearn`和`import nltk`确定是否import成功
3. 下载`https://github.com/udacity/ud120-projects.git`，基础代码包含所有迷你项目的初始代码。
4. 进入 tools/ 目录，运行 startup.py。（cmd中操作，需要将python2.7设定为默认python环境，如果要将python环境还原为python3,在环境变量的Path中将python2.7的路径删除），运行比较耗时。

```
E:\udacity\32-ML\ud120-projects-master\tools>python startup.py

checking for nltk
checking for numpy
checking for scipy
checking for sklearn
...
```

# 42. 作者身份准确率

在 naive_bayes/nb_author_id.py 中创建和训练朴素贝叶斯分类器，用其为测试集进行预测。准确率是多少？

```python
#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

# 创建分类器
clf = GaussianNB()

t0 = time()
# 训练分类器
clf.fit(features_train,labels_train)
print "fit training time:", round(time()-t0, 3), "s"

t0 = time()
# 使用分类器预测
pred = clf.predict(features_test)
print "predict training time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score

# 计算精度
accuracy = accuracy_score(labels_test, pred)

print accuracy

#########################################################
```


- 得到结果为:

```python
no. of Chris training emails: 7936
no. of Sara training emails: 7884
fit training time: 1.151 s
predict training time: 0.157 s
0.973265073948
```


# 98. 参考
1. [贝叶斯推断及其互联网应用（一）：定理简介](http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_one.html)
2. [贝叶斯推断及其互联网应用（二）：过滤垃圾邮件](http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_two.html)

# 99. 术语

- `supervised classification`: 监督分类
- `emulate`:模仿
