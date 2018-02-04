---
layout: post
title: Uda-DataAnalysis-38-机器学习-异常值
date: 2018-01-16 08:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 7. 异常值删除策略的小结

outlier-rejection

1. 训练 - Train
2. 去除最大残差的点(该点到拟合回归线的距离) - Remove points with largest residual error
3. 再训练 - Re-train

# 9. 异常值迷你项目

```python
#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle

from outlier_cleaner import outlierCleaner


### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )



### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.cross_validation import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(ages_train,net_worths_train)
print "train slope:",reg.coef_
print "train intercept:",reg.intercept_
print "train score train:",reg.score(ages_train,net_worths_train)
print "train score test:",reg.score(ages_test,net_worths_test)

try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
plt.show()


### identify and remove the most outlier-y points
cleaned_data = []
try:
    predictions = reg.predict(ages_train)
    cleaned_data = outlierCleaner( predictions, ages_train, net_worths_train )
except NameError:
    print "your regression object doesn't exist, or isn't name reg"
    print "can't make predictions to use in identifying outliers"


### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)

        print "new train slope:",reg.coef_
        print "new train intercept:",reg.intercept_
        print "new train score train:",reg.score(ages_train,net_worths_train)
        print "new train score test:",reg.score(ages_test,net_worths_test)

        plt.plot(ages, reg.predict(ages), color="red")
    except NameError:
        print "you don't seem to have regression imported/created,"
        print "   or else your regression object isn't named reg"
        print "   either way, only draw the scatter plot of the cleaned data"
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()


else:
    print "outlierCleaner() is returning an empty list, no refitting to be done"


```

输出结果为：

```python
train slope: [[ 5.07793064]]
train intercept: [ 25.21002155]
train score train: 0.489872596175
train score test: 0.878262470366
```

图形为：

![image](https://user-images.githubusercontent.com/18595935/35767488-71df84de-0930-11e8-9952-bc2d982a18c3.png)


# 12. 清理后的斜率

在 outliers/outlier_cleaner.py 中找到 outlierCleaner() 函数的骨架并向其填充清理算法。用到的三个参数是：predictions 是一个列表，包含回归的预测目标；ages 也是一个列表，包含训练集内的年龄；net_worths 是训练集内净值的实际值。每个列表中应有 90 个元素（因为训练集内有 90 个点）。你的工作是返回一个名叫cleaned_data 的列表，该列表中只有 81 个元素，也即预测值和实际值 (net_worths) 具有最小误差的 81 个训练点 (90 * 0.9 = 81)。cleaned_data 的格式应为一个元组列表，其中每个元组的形式均为 (age, net_worth, error)。


```python
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import math
    
    cleaned_data = []
    diffs = []

    ### your code goes here
    # 求解差值
    for i in range(len(predictions)):
        prediction = predictions[i]
        net_worth = net_worths[i]

        diff = math.fabs(prediction - net_worth)
        diffs.append((diff,i))

    # 对差值进行排序
    diffs.sort()
    # 排序后取90%的数据，存储到新的diffs中
    maxlens = int(0.9*len(diffs))
    new_diffs = diffs[0:maxlens]

    # 根据new_diffs中存储的index，取出这90%的正确数据
    for new_diff in new_diffs:
        prediction = predictions[new_diff[1]]
        net_worth = net_worths[new_diff[1]]
        age = ages[new_diff[1]]

        cleaned_data.append((age[0],net_worth[0],new_diff[0]))

    print len(cleaned_data)

    return cleaned_data
```

输出结果为：

```python
train slope: [[ 5.07793064]]
train intercept: [ 25.21002155]
train score train: 0.489872596175
train score test: 0.878262470366
##############
new train slope: [[ 6.36859481]]
new train intercept: [-6.91861069]
new train score train: 0.409325454478
new train score test: 0.983189455396
```


图形为，红色的回归线是去除异常值之后的：

![image](https://user-images.githubusercontent.com/18595935/35767894-6295f272-0937-11e8-981b-26450d55869b.png)

# 15. 识别最大的安然异常值


```python
#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
data.sort()
print data[len(data)-3]

salarys = []
bonus = []
for mydata in data:
	salarys.append(mydata[0])
	bonus.append(mydata[1])

salarys.sort()
bonus.sort()

print salarys
print bonus

```

- 第一个显然是因为数据录入错误，将TOTAL作为一个员工了，而实际上是总计的金额。
- 通过` dictionary.pop( key, 0 )` 可以移除异常值。


