---
layout: post
title: Uda-DataAnalysis-37-机器学习-回归(regression)
date: 2018-01-16 07:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 2. 连续输出

输出必须是连续的：

![image](https://user-images.githubusercontent.com/18595935/35568691-2468df00-060d-11e8-8d28-90eecee0b8f4.png)

# 10. 回归线性方程

![image](https://user-images.githubusercontent.com/18595935/35737428-c26f3d12-086e-11e8-997f-51ea36475262.png)

# 17. 编码

参考[1.1. Generalized Linear Models](http://scikit-learn.org/stable/modules/linear_model.html)

```python
>>> from sklearn import linear_model
>>> reg = linear_model.LinearRegression()
>>> reg.fit([[0,0],[1,1],[2,2]],[0,1,2])
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
>>> reg.coef_
array([ 0.5,  0.5])
```

# 18. sklearn 中的年龄/净值回归

- `studentMain.py`


```python
#!/usr/bin/python

import numpy
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from studentRegression import studentReg
from class_vis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

reg = studentReg(ages_train, net_worths_train)

plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")

plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
```


- `studentRegression.py`

```python
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    
    ### your code goes here!
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    
    reg.fit(ages_train,net_worths_train)
    
    return reg
```

- 输出结果：

![image](https://user-images.githubusercontent.com/18595935/35764053-4cbfc85a-08fc-11e8-869e-15c6f3016635.png)



# 19. 通过sklearn提取信息

```python
...
reg.fit(ages_train,net_worths_train)

# 根据训练后的回归模型，预测27岁人的收入
print reg.predict([27])

# 回归模型的斜率
print reg.coef_

# 回归模型的截距
print reg.intercept_

# 计算r平方分数（r-squared score）,最大值1，越大越精确
print reg.score(ages_test,net_worths_test)
```

# 21. 现在你练习提取信息

- 从回归中提取预测、斜率和截距，以及训练和测试分数。

```python
import numpy
import matplotlib.pyplot as plt

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(ages_train, net_worths_train)

### get Katie's net worth (she's 27)
### sklearn predictions are returned in an array, so you'll want to index into
### the output to get what you want, e.g. net_worth = predict([[27]])[0][0] (not
### exact syntax, the point is the [0] at the end). In addition, make sure the
### argument to your prediction function is in the expected format - if you get
### a warning about needing a 2d array for your data, a list of lists will be
### interpreted by sklearn as such (e.g. [[27]]).
km_net_worth = reg.predict([27])[0][0] ### fill in the line of code to get the right value

### get the slope
### again, you'll get a 2-D array, so stick the [0][0] at the end
slope = reg.coef_[0][0] ### fill in the line of code to get the right value

### get the intercept
### here you get a 1-D array, so stick [0] on the end to access
### the info we want
intercept = reg.intercept_[0] ### fill in the line of code to get the right value

### get the score on test data
test_score = reg.score(ages_test,net_worths_test) ### fill in the line of code to get the right value


### get the score on the training data
training_score = reg.score(ages_train,net_worths_train) ### fill in the line of code to get the right value

def submitFit():
    # all of the values in the returned dictionary are expected to be
    # numbers for the purpose of the grader.
    return {"networth":km_net_worth,
            "slope":slope,
            "intercept":intercept,
            "stats on test":test_score,
            "stats on training": training_score}
```

- 输出

```python
{"slope": 6.473549549577059, "stats on training": 0.8745882358217186, "intercept": -14.35378330775552, "stats on test": 0.812365729230847, "networth": 160.43205453082507}
```

# 22. 线性回归误差

![image](https://user-images.githubusercontent.com/18595935/35765153-bf163e34-0901-11e8-82dc-358dd050e9c8.png)

# 25. 最小化误差平方和

好的线性回归模型，就是找到最合适的m和b，使得误差平方和最小化：

![image](https://user-images.githubusercontent.com/18595935/35765206-b4961b7c-0902-11e8-9568-046875f8ebb9.png)

有两种算法计算最小的误差平方和：

- ordinary least squares(OLS) 最小二乘法，sklearn使用该算法进行线性回归

- gradient descent 梯度下降法

# 27. 为何最小化 SSE

下面的示例能解释为什么最好的回归模型，是误差的平方最小：


![image](https://user-images.githubusercontent.com/18595935/35765294-fc129498-0903-11e8-8a01-25e800e4d6c8.png)


# 28. 最小化误差的问题

左右两个图形中，线性回归模型质量是一样好，但是右边的数据集更大，所以最后SSE即最小化误差更大，显得拟合的质量比左边差，最小化误差的问题，就是不同的数据集之间对比可能会存在问题。

![image](https://user-images.githubusercontent.com/18595935/35765342-eaaae7ae-0904-11e8-89f4-fdaabdf9d3a4.png)

# 31. 回归的 R 平方指标

为了回避上面最小化误差的问题，引入了R平方指标来评价回归的质量，R值在0-1之间，0最差，1最好，由于其值固定在0-1之间，所以避免了数据集数量的问题：

![image](https://user-images.githubusercontent.com/18595935/35765380-dad7f83e-0905-11e8-897b-da861c3959e7.png)

```python
# 计算r平方分数（r-squared score）,最大值1，越大越精确
print reg.score(ages_test,net_worths_test)
```

# 34. 什么数据适用于线性回归

![image](https://user-images.githubusercontent.com/18595935/35765481-d6af36f8-0907-11e8-9fa6-cfaf9e661345.png)

第一幅图选错了的，这里y的值并不随x的变化而变化，就是说不能通过x对y进行预测。

第四幅图，其中m为0，b为固定值，即y为定值，无论x如何变化都是定值。


# 35. 比较分类与回归

![image](https://user-images.githubusercontent.com/18595935/35766573-5454beb4-091e-11e8-964a-b96a386cac73.png)

- 监督分类(朴素贝叶斯/SVM/决策树)

![image](https://user-images.githubusercontent.com/18595935/35225464-b6b01b78-ffcb-11e7-9907-eb7d398a206d.png)

- 回归

![image](https://user-images.githubusercontent.com/18595935/35764053-4cbfc85a-08fc-11e8-869e-15c6f3016635.png)

# 36. 多元回归(Multi-Variate Regression)

前面的例子是一个变量，一个预测值，如果多个变量来进行预测的话，属于多元回归。

![image](https://user-images.githubusercontent.com/18595935/35766622-11dd27fa-091f-11e8-8681-71d898518334.png)

# 37. 回归迷你项目

```python

#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    

import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "long_term_incentive"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"

### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(feature_train,target_train)
print "slope:",reg.coef_
print "intercept:",reg.intercept_
print "score train:",reg.score(feature_train,target_train)
print "score test:",reg.score(feature_test,target_test)

### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")

### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
```

- 输出结果与图形

![image](https://user-images.githubusercontent.com/18595935/35767016-fda3a608-0926-11e8-9586-a78bea8884f9.png)

使用salary预测结果：

```python
slope: [ 5.44814029]
intercept: -102360.543294
score train: 0.0455091926995
score test: -1.48499241737
```

使用long_term_incentive预测结果：

```python
slope: [ 1.19214699]
intercept: 554478.756215
score train: 0.217085971258
score test: -0.59271289995
```

# 47. 异常值破坏回归

这是下节课的内容简介，关于异常值的识别和删除。返回至之前的一个设置，你在其中使用工资预测奖金，并且重新运行代码来回顾数据。你可能注意到，少量数据点落在了主趋势之外，即某人拿到高工资（超过 1 百万美元！）却拿到相对较少的奖金。此为异常值的一个示例，我们将在下节课中重点讲述它们。

类似的这种点可以对回归造成很大的影响：如果它落在训练集内，它可能显著影响斜率/截距。如果它落在测试集内，它可能比落在测试集外要使分数低得多。就目前情况来看，此点落在测试集内（而且最终很可能降低分数）。让我们做一些处理，看看它落在训练集内会发生什么。在 finance_regression.py 底部附近并且在 plt.xlabel(features_list[1]) 之前添加这两行代码：

reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b")

现在，我们将绘制两条回归线，一条在测试数据上拟合（有异常值），一条在训练数据上拟合（无异常值）。来看看现在的图形，有很大差别，对吧？单一的异常值会引起很大的差异。

新的回归线斜率是多少？

```python
reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="y")
print "test slope:",reg.coef_
```

输出图形如下：

![image](https://user-images.githubusercontent.com/18595935/35767120-42f09f20-0929-11e8-93b2-95226fc6275a.png)


- 蓝色斜线，使用训练数据进行回归训练，用测试数据预测
- 黄色斜线，使用测试数据进行回归训练，用训练数据预测
- 其中测试数据上有异常值，所以最终拟合的

输出斜率，截距，以及测试分数如下：

```python
train slope: [ 5.44814029]
train intercept: -102360.543294
train score train: 0.0455091926995
train score test: -1.48499241737
#############
test slope: [ 2.27410114]
test intercept: 124444.388866
test score train: -0.123597985403
test score test: 0.251488150398
```
