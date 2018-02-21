---
layout: post
title: Uda-DataAnalysis-46-机器学习-进阶项目3：从安然公司邮件中发现欺诈证据
date: 2018-01-16 16:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# [分析报告]从安然公司邮件中发现欺诈证据

安然公司（Enron Corporation），曾是一家位于美国的德克萨斯州休斯敦市的能源类公司。在2001年宣告破产之前，安然拥有约21000名雇员，是世界上最大的电力、天然气以及电讯公司之一，2000年披露的营业额达1010亿美元之巨。公司连续六年被《财富》杂志评选为“美国最具创新精神公司”，然而真正使安然公司在全世界声名大噪的，却是这个拥有上千亿资产的公司2002年在几周内破产，持续多年精心策划、乃至制度化、系统化的财务造假丑闻。

# 1. 目标

>1.向我们总结此项目的目标以及机器学习对于实现此目标有何帮助。

本项目的目标是，基于公开的安然数据集(财务和邮件数据)，构建一个预测模型，最终通过模型识别出有欺诈嫌疑的雇员。

# 2. 数据集介绍

>1.作为答案的部分，提供一些数据集背景信息以及这些信息如何用于回答项目问题。

本数据集中，包含了146条记录，每条记录中包含了雇员的财务和邮件相关信息，另外数据中包含20个特征。进一步分析数据中的每条记录的`poi`特征，发现共有18条记录可能是嫌疑人。

>1.你在获得数据时它们是否包含任何异常值，你是如何进行处理的？

另外，通过对数据的可视化，以及将`无效值(NaN)`的记录输出，发现了如下的异常记录，并进行清除：

- `TOTAL`:存在名字为`TOTAL`的记录，显然这个并不是一条雇员的记录，而是列表中所有数据的一条汇总记录。
- `THE TRAVEL AGENCY IN THE PARK`：显然这个并不是一条雇员记录，而是一家旅行代理公司。
- `LOCKHART EUGENE E`：该记录的所有特征都是`NaN`，无有效数据。

清除上述3条数据后，还有143条有效记录，如下是移除了异常记录后的对比图：

![image](https://user-images.githubusercontent.com/18595935/36312317-66e9dd72-1371-11e8-869f-b58d8f39d09c.png)

![image](https://user-images.githubusercontent.com/18595935/36312327-71cab2d4-1371-11e8-8671-db33f795274c.png)


# 3. 数据特征

## 3.1 当前数据集特征和标签

数据中的特征分为三大类，即财务特征、邮件特征和 POI 标签。

- 财务特征 : ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees'] (单位均是美元）

- 邮件特征 : ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi'] (单位通常是电子邮件的数量，明显的例外是 'email_address'，这是一个字符串）

- POI 标签 : ['poi'], boolean类型

另外，这些特征中存在无效值`NaN`，如下是特征中数据缺失数目和比率列表，下表可以看出数据非常不均衡：

|特征名|有效件数|无效件数|无效件数比率|
|:--|--:|:--:|:--:|
|salary|94|49|34%|
|to_messages|86|57|40%|
|deferral_payments|38|105|73%|
|total_payments|123|20|73%|
|exercised_stock_options|101|42|29%|
|bonus|81|62|43%|
|restricted_stock|109|34|24%|
|shared_receipt_with_poi|86|57|40%|
|restricted_stock_deferred|17|126|88%|
|total_stock_value|125|18|88%|
|expenses|94|49|34%|
|loan_advances|3|140|98%|
|from_messages|86|57|40%|
|other|91|52|36%|
|from_this_person_to_poi|86|57|40%|
|director_fees|16|127|89%|
|deferred_income|48|95|66%|
|long_term_incentive|65|78|66%|
|email_address|111|32|22%|
|from_poi_to_this_person|86|57|40%|

## 3.2 添加新的特征

> 2.作为任务的一部分，你应该尝试设计自己的特征，而非使用数据集中现成的——解释你尝试创建的特征及其基本原理。

当前数据集中，`from_poi_to_this_person`和`from_this_person_to_poi`分别反映了该雇员接收到嫌疑人员，以及发送给嫌疑人员的邮件数目。将这两个特征与`poi`标签可视化后如下图所示(红色表示POI雇员，蓝色表示非POI雇员)：

![image](https://user-images.githubusercontent.com/18595935/36315978-6430d44a-137c-11e8-8c08-e5327beb5bed.png)

并没有发现明显的规律，由于每个人处理邮件的数目不同，考虑将上述与嫌疑人员之间的邮件绝对件数，转换为该人员发送和接收自嫌疑人员与自身总发送接收邮件数目的比例：

- `fraction_from_poi = from_poi_to_this_person / to_messages `
- `fraction_to_poi = from_this_person_to_poi / from_messages`

将这两个新的特征与`poi`标签可视化后如下图所示(红色表示POI雇员，蓝色表示非POI雇员)：

![image](https://user-images.githubusercontent.com/18595935/36316003-7487a120-137c-11e8-9d38-35dfdb58c47e.png)

可以看出，如果某个雇员的上述两个新特征值在低于某个值后，该雇员有欺诈嫌疑的概率就很小。


## 3.3 特征选取

>2.你最终在你的 POI 标识符中使用了什么特征，你使用了什么筛选过程来挑选它们？如果你使用了自动特征选择函数（如 SelectBest），请报告特征得分及你所选的参数值的原因。

创建了新的特征后，下一步要选取最能传递信息给预测模型的特征。
本数据集中，一共有20个特征，但是这些特征并不是都对创建预测模型有用，在这里使用 Scikit-Learn中的`SelectKBest`算法，评判得分，选取最好的5个feature。

|feature|score|
|:--|--:|
|exercised_stock_options|24.815079733218194|
|total_stock_value|24.182898678566879|
|bonus|20.792252047181535|
|salary|18.289684043404513|
|fraction_to_poi|16.409712548035799|

## 3.4 特征缩放

>2.你是否需要进行任何缩放？为什么？

上述5个特征中，前4个是该雇员的收入，而最后一个是发送给POI雇员的邮件占比，值的大小不在一个维度上，这里采用Scikit-Learn中的`MinMaxScaler`进行特征缩放，将值缩放到[0,1]之间。


# 4. 选择和调试机器学习算法

>3.你还尝试了其他什么算法？

选取好用于评价的特征后，下一步就是选用一系列机器学习算法，建立模型进行预测，并评价那个模型给出了最好的评价结果。本项目中尝试用如下的算法，并使用`GridSearchCV`来调整算法的参数：

- `Gaussian Naïve-Bayes`朴素贝叶斯
- `Decision Tree Classifier`决策树
- `Support Vector Machines`支持向量机
- `RandomForest`随机森林
- `AdaBoost`

>3.不同算法之间的模型性能有何差异？

- 时间消耗

从下表的时间消耗上看，`GaussianNB`算法速度最快。

|算法|耗时(s)|
|:--|--:|
|GaussianNB|0.021|
|Decision Tree|1.492|
|SVM|0.056|
|RandomForest|54.018|
|AdaBoost|7.314|

- 评分

参考scikit-learn.org上的定义`score(X, y, sample_weight=None)：Returns the mean accuracy on the given test data and labels.`，
score表示的是accuracy，但是由于数据的不平衡，说明accuracy并不是很好的评估指标，选择precision和recall及F1更好一些。

|算法|Score|
|:--|--:|
|GaussianNB|0.857142857143|
|Decision Tree|0.868131868132|
|SVM|0.879120879121|
|RandomForest|1.0|
|AdaBoost|0.901098901099|

## 4.1 最终选定的算法

>3.你最终使用了什么算法？

通过对上面评分结果(Precision,Recall,F1,ie.)的分析，判断`GaussianNB classifier`给出了最好的预测结果。

## 4.2 调试算法

>4.调整算法的参数是什么意思，如果你不这样做会发生什么？你是如何调整特定算法的参数的？

数据样本比较少，故使用GridSearchCV来进行参数调整，如果较大的数据则会花费较长的时间，可以考虑使用RandomizedSearchCV.

在代码中，使用了`GridSearchCV()`来调试各个算法的参数，另外通过`test_classifier()`测试了算法并给出了判断结果，经过调试最好的结果来自`GaussianNB classifier`。

对参数的调试是机器学习中很重要的一环，因为不同的算法函数和初始设定会对最终结果产生很多影响。在某些情况下，为算法选择了错误的参数，会造成过拟合。

# 5. 验证与评价

>5.什么是验证，未正确执行情况下的典型错误是什么？你是如何验证你的分析的？

验证是将训练出得模型，用测试数据进行评价的过程，验证中的典型错误是没有将数据分成训练和测试两部分，从而导致过拟合。

在交叉验证的时候，因为数据的不平衡性，选用StratifiedShuffle Split，StratifiedShuffleSplit是一种交叉验证的方式，通过对数据进行多次洗牌和分割，能够确保训练集和测试集中POI与非POI的比例，比较适合于该数据。
最终得到评价结果如下：

||GaussianNB|Decision Tree|SVM|RandomForest|AdaBoost|
|:--|--:|:--:|:--:|:--:|:--:|
|Accuracy|0.84879|0.85493|0.86543|0.83329|0.86193|
|Precision|0.45558|0.47446|0.79897|0.38370|0.56238|
|Recall|0.30000|0.14400|0.07750| 0.27550 |0.15100|
|F1|0.36177|0.22094|0.14129|0.32072|0.23808|
|F2|0.32199|0.16731|0.09458|0.29197|0.17688|
|Total predictions| 14000|14000|14000 |14000 |14000 |
|True positives|600|288|155|551| 302|
|False positives|717|319|39|885| 235|
|False negatives|1400|1712|1845|1449|1698|
|True negatives|11283|11681|11961|11115|11765|

>6.给出至少2个评估度量并说明每个的平均性能。解释对用简单的语言表明算法性能的度量的解读。

最终选取的算法是朴素贝叶斯`GaussianNB`，主要基于准确率`Precision`,召回率`Recall`和综合评价指标`F1`等进行的判断。

如下是上述表中最后四个参数的意义：

- True Positive(真正，TP)：将正类预测为正类数
- True Negative(真负，TN)：将负类预测为负类数
- False Positive(假正，FP)：将负类预测为正类数误报 (Type I error)
- False Negative(假负，FN)：将正类预测为负类数→漏报 (Type II error)

如下是对应的预测类别表：

||Yes|No|总计|
|:--|--:|:--:|:--:|
|Yes|TP|FN|P(实际为Yes)|
|No|FP|TN|N(实际为NO)|
|总计|P'(被分为Yes)|N'(被分为No)|P+N|

- 关于精确率`Precision`:
精确率(Precision)计算公式为： `P = (TP) / (TP+FP)`，表示被分为正例的示例中实际为正例的比例。在本项目中，精确率指的是模型预测出的POI中，真正为POI的比率。

- 关于召回率`Recall`：
召回率是覆盖面的度量，度量有多个正例被分为正例，`recall=TP/(TP+FN)=TP/P=sensitive`，可以看到召回率与灵敏度是一样的。在本项目中，指的是所有真正的POI雇员中，有多少被真正的识别出来了。

- 关于综合评价指标`F1`：
Precision与Recall有时候会出现矛盾，如上表所示，这时就需要综合考虑他们，最常见的方法是F-Measure,F-Measure的计算公式如下：

```python
F = (a**2 + 1)*P*R / a**2(P+R)
```

F是Precision与Recall的加权调和评价，当a=1时，就是最常见的F1，公式为 `F1 = 2*P*R / (P+R)`，可见F1综合了P和R的结果，当F1较高时则能说明该模型效果不错，上表中也显示`GaussianNB`的F1为其中的最高值，为`0.36177`。


# 9. 参考
1. [wiki-安然公司](https://zh.wikipedia.org/wiki/%E5%AE%89%E7%84%B6%E5%85%AC%E5%8F%B8)
2. [Identify Fraud From Enron Data](https://arjan-hada.github.io/enron-fraud.html)
3. [sample code](https://jefflirion.github.io/udacity/Intro_to_Machine_Learning/Lesson5.html)
4. [Investigating the Enron Fraud with Machine Learning](http://luizschiller.com/enron/)
5. [机器学习安然数据集分析报告](http://blog.csdn.net/Einstellung/article/details/78387849)
6. [机器学习：准确率(Precision)、召回率(Recall)、F值(F-Measure)、ROC曲线、PR曲线](http://blog.csdn.net/quiet_girl/article/details/70830796)

# 10. 参考代码

## 10.1 全体代码-`poi_id.py`

```python
#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from time import time

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','bonus','total_payments','deferral_payments','exercised_stock_options',\
                     'restricted_stock','restricted_stock_deferred','total_stock_value','expenses',\
                     'other','director_fees','loan_advances','deferred_income','long_term_incentive',\
                     'from_poi_to_this_person','from_this_person_to_poi','to_messages','from_messages',\
                     'shared_receipt_with_poi','fraction_from_poi','fraction_to_poi'] 
                      # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### add by @lj 
import matplotlib.pyplot as plt

print "\n","######### total numbers of data point:"
print len(data_dict)

print "\n","######### total numbers of features:"
for features in data_dict.values():
    print len(features)
    print features
    break

print "\n","######### total number of poi:"
pois = [x for x, y in data_dict.items() if y['poi']]
print len(pois)

print ""
print "######### check the nan data:"
for key,value in data_dict.items():
	nan_num = 0
	for i in value.values():
		if i == "NaN":
			nan_num = nan_num + 1

	if nan_num > 15:
		print key,":",nan_num


print "\n","######### find the outliers:"
salary_list = []
bonus_list = []

for features in data_dict.values():
	#plt.scatter(features["salary"], features["bonus"])

	# 
	if features["salary"] == "NaN" or features["bonus"] == "NaN":
		continue
	salary_list.append(features["salary"])
	bonus_list.append(features["bonus"])

# 
bonus_list.sort()
salary_list.sort()

print "\n","######### the top five:"
print salary_list[-5:]
print bonus_list[-5:]

print "\n","######### the bottom five:"
print salary_list[0:5]
print bonus_list[0:5]

# 
#plt.title('The original dataset:')
#plt.xlabel("salary")
#plt.ylabel("bonus")

# 
print "\n","######### top of the salary and bonus:"
print "######### show the problem data point:"
for key,value in data_dict.items():
	if value["salary"] == salary_list[-1]:
		print ""
		print key,"'s salary : ",value["salary"]

	if value["bonus"] == bonus_list[-1]:
		print ""
		print key,"'s bonus : ",value["bonus"]

	if key == "THE TRAVEL AGENCY IN THE PARK" or key == "LOCKHART EUGENE E":
		print ""
		print key,":"
		print value


# 

### end by @lj

### Task 2: Remove outliers

### Store to my_dataset for easy export below.
my_dataset = data_dict

### add by lj
my_dataset.pop("TOTAL")
my_dataset.pop("THE TRAVEL AGENCY IN THE PARK")
my_dataset.pop("LOCKHART EUGENE E")
print "\n","after(remove outliers), the total number of the dataset:"
print len(my_dataset)

#
#for features in my_dataset.values():
#	plt.scatter(features["salary"], features["bonus"])

#plt.title('After removing the outliers:')
#plt.xlabel("salary")
#plt.ylabel("bonus")
#plt.show()

#
import numpy as np
import pandas as pd
df = pd.DataFrame.from_dict(data_dict, orient='index')
df.replace('NaN', np.nan, inplace = True)

df.info()

# 
#for features in my_dataset.values():
#	colors = features["poi"]
#	if colors == True:
#		colors = "red"
#	else:
#		colors = "blue"
#	plt.scatter(features["from_poi_to_this_person"], features["from_this_person_to_poi"], c=colors,alpha=0.5)

#plt.xlabel("from_poi_to_this_person")
#plt.ylabel("from_this_person_to_poi")
#plt.show()

### Task 3: Create new feature(s)
def computeFraction( poi_messages, all_messages ):
    fraction = 0.
    
    if poi_messages == "NaN" or all_messages == "NaN":
        return 0

    fraction = float(poi_messages)/all_messages
    
    return fraction

for i in data_dict:
    my_dataset[i]['fraction_from_poi'] = computeFraction(my_dataset[i]['from_poi_to_this_person'],my_dataset[i]['to_messages'])
    my_dataset[i]['fraction_to_poi'] = computeFraction(my_dataset[i]['from_this_person_to_poi'],my_dataset[i]['from_messages'])

#for features in my_dataset.values():
#	colors = features["poi"]
#	if colors == True:
#		colors = "red"
#	else:
#		colors = "blue"
#	plt.scatter(features["fraction_from_poi"], features["fraction_to_poi"], c=colors,alpha=0.5)

#plt.xlabel("fraction_from_poi")
#plt.ylabel("fraction_to_poi")
#plt.show()

##
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
from sklearn.feature_selection import SelectPercentile,SelectKBest

def Select_K_Best(data_dict, features_list, k):

    data_array = featureFormat(data_dict, features_list)
    labels, features = targetFeatureSplit(data_array)

    k_best = SelectKBest(k=k)
    k_best.fit(features, labels)
    scores = k_best.scores_
    tuples = zip(features_list[1:], scores)
    k_best_features = sorted(tuples, key=lambda x: x[1], reverse=True)

    return k_best_features[:k]

print "\n",Select_K_Best(my_dataset,features_list,5)

features_list = ["poi"] + [x[0] for x in Select_K_Best(my_dataset,features_list,5)] 

print "\n",features_list

### end by @lj

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

## 
from sklearn.preprocessing import MinMaxScaler

print "\n",features[0:3]

scaler = MinMaxScaler()
features_new = scaler.fit_transform(features)

print "\n",features_new[0:3]

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

labels = np.asarray(labels)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

## 1. GaussianNB
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

t1 = time()

clf_NB = GaussianNB()
parm = {}

clf_NB = Pipeline([('scaler',scaler),('gnb',clf_NB)])
gs = GridSearchCV(clf_NB,parm)
gs.fit(features_train,labels_train)

clf_NB = gs.best_estimator_

print "\nGaussianNB score:\n",clf_NB.score(features_train,labels_train)
print "GaussianNB score time:", round(time()-t1, 3), "s"

##  Test Point
from tester import dump_classifier_and_data,test_classifier

print "\nGaussianNB:\n",test_classifier(clf_NB,my_dataset,features_list)

## 2. Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

t2 = time()

parms = {'criterion': ['gini', 'entropy'], \
			'min_samples_split': [2, 5, 10, 20], \
			'max_depth': [None, 2, 5, 10], \
			'splitter': ['random', 'best'], \
			'max_leaf_nodes': [None, 5, 10, 20]   }

clf_DT = tree.DecisionTreeClassifier()

gs = GridSearchCV(clf_DT,parms)
gs.fit(features_train,labels_train)

clf_DT = gs.best_estimator_

print "\nDecision Tree Classifier\n",clf_DT.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t2, 3), "s"

##  Test Point
print "\nDecision Tree Classifier Test Point:\n",test_classifier(clf_DT,my_dataset,features_list)

## 3. SVM

from sklearn.svm import SVC
parms = {'svc__kernel':('linear','rbf'),'svc__C':[1.0,2.0]}

t3 = time()
clf_SVC = SVC()

pipeline2 = Pipeline([('scaler',scaler),('svc',clf_SVC)])
# a = pipeline.fit(features_train,labels_train)
gs = GridSearchCV(pipeline2,parms)
gs.fit(features_train,labels_train)

clf_SVC = gs.best_estimator_

print "\nSVM \n",clf_SVC.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t3, 3), "s"

##  Test Point
print "\nSVM:\n",test_classifier(clf_SVC,my_dataset,features_list)


### 4. RandomForest
from sklearn.ensemble import RandomForestClassifier

t4 = time()

print '\nRandomForest\n'
clf_RF = RandomForestClassifier()
parameters = {'criterion': ['gini', 'entropy'], \
			'max_depth': [None, 2, 5, 10], \
			'max_leaf_nodes': [None, 5, 10, 20], \
			'n_estimators': [1, 5, 10, 50, 100]}
gs = GridSearchCV(clf_RF, parameters)
gs.fit(features_train,labels_train)

clf_RF = gs.best_estimator_

print "\nRandomForest:\n",clf_RF.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t4, 3), "s"

##  Test Point
print "\nRandomForest:\n",test_classifier(clf_RF,my_dataset,features_list)

### 5. AdaBoost
from sklearn.ensemble import AdaBoostClassifier

t5 = time()

clf_AB = AdaBoostClassifier(algorithm='SAMME')
parameters = {'learning_rate': [0.1, 0.5, 1.0, 5.0], \
			'algorithm': ['SAMME', 'SAMME.R'], \
			'n_estimators': [1, 5, 10, 50, 100]}
gs = GridSearchCV(clf_AB, parameters)
gs.fit(features_train,labels_train)

clf_AB = gs.best_estimator_

print "\nAdaBoost:\n",clf_AB.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t5, 3), "s"

##  Test Point
print "\nAdaBoost:\n",test_classifier(clf_AB,my_dataset,features_list)


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

clf = clf_NB

dump_classifier_and_data(clf, my_dataset, features_list)
```

## 10.2 全体代码-`tester.py`


```python
#!/usr/bin/pickle

""" a basic script for importing student's POI identifier,
    and checking the results that they get from it 
 
    requires that the algorithm, dataset, and features list
    be written to my_classifier.pkl, my_dataset.pkl, and
    my_feature_list.pkl, respectively

    that process should happen at the end of poi_id.py
"""

import pickle
import sys
from sklearn.cross_validation import StratifiedShuffleSplit
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

PERF_FORMAT_STRING = "\
\tAccuracy: {:>0.{display_precision}f}\tPrecision: {:>0.{display_precision}f}\t\
Recall: {:>0.{display_precision}f}\tF1: {:>0.{display_precision}f}\tF2: {:>0.{display_precision}f}"
RESULTS_FORMAT_STRING = "\tTotal predictions: {:4d}\tTrue positives: {:4d}\tFalse positives: {:4d}\
\tFalse negatives: {:4d}\tTrue negatives: {:4d}"

def test_classifier(clf, dataset, feature_list, folds = 1000):
    data = featureFormat(dataset, feature_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    cv = StratifiedShuffleSplit(labels, folds, random_state = 42)
    true_negatives = 0
    false_negatives = 0
    true_positives = 0
    false_positives = 0
    for train_idx, test_idx in cv: 
        features_train = []
        features_test  = []
        labels_train   = []
        labels_test    = []
        for ii in train_idx:
            features_train.append( features[ii] )
            labels_train.append( labels[ii] )
        for jj in test_idx:
            features_test.append( features[jj] )
            labels_test.append( labels[jj] )
        
        ### fit the classifier using training set, and test on test set
        clf.fit(features_train, labels_train)
        predictions = clf.predict(features_test)
        for prediction, truth in zip(predictions, labels_test):
            if prediction == 0 and truth == 0:
                true_negatives += 1
            elif prediction == 0 and truth == 1:
                false_negatives += 1
            elif prediction == 1 and truth == 0:
                false_positives += 1
            elif prediction == 1 and truth == 1:
                true_positives += 1
            else:
                print "Warning: Found a predicted label not == 0 or 1."
                print "All predictions should take value 0 or 1."
                print "Evaluating performance for processed predictions:"
                break
    try:
        total_predictions = true_negatives + false_negatives + false_positives + true_positives
        accuracy = 1.0*(true_positives + true_negatives)/total_predictions
        precision = 1.0*true_positives/(true_positives+false_positives)
        recall = 1.0*true_positives/(true_positives+false_negatives)
        f1 = 2.0 * true_positives/(2*true_positives + false_positives+false_negatives)
        f2 = (1+2.0*2.0) * precision*recall/(4*precision + recall)
        print clf
        print PERF_FORMAT_STRING.format(accuracy, precision, recall, f1, f2, display_precision = 5)
        print RESULTS_FORMAT_STRING.format(total_predictions, true_positives, false_positives, false_negatives, true_negatives)
        print ""
    except:
        print "Got a divide by zero when trying out:", clf
        print "Precision or recall may be undefined due to a lack of true positive predicitons."

CLF_PICKLE_FILENAME = "my_classifier.pkl"
DATASET_PICKLE_FILENAME = "my_dataset.pkl"
FEATURE_LIST_FILENAME = "my_feature_list.pkl"

def dump_classifier_and_data(clf, dataset, feature_list):
    with open(CLF_PICKLE_FILENAME, "w") as clf_outfile:
        pickle.dump(clf, clf_outfile)
    with open(DATASET_PICKLE_FILENAME, "w") as dataset_outfile:
        pickle.dump(dataset, dataset_outfile)
    with open(FEATURE_LIST_FILENAME, "w") as featurelist_outfile:
        pickle.dump(feature_list, featurelist_outfile)

def load_classifier_and_data():
    with open(CLF_PICKLE_FILENAME, "r") as clf_infile:
        clf = pickle.load(clf_infile)
    with open(DATASET_PICKLE_FILENAME, "r") as dataset_infile:
        dataset = pickle.load(dataset_infile)
    with open(FEATURE_LIST_FILENAME, "r") as featurelist_infile:
        feature_list = pickle.load(featurelist_infile)
    return clf, dataset, feature_list

def main():
    ### load up student's classifier, dataset, and feature_list
    clf, dataset, feature_list = load_classifier_and_data()
    ### Run testing script
    test_classifier(clf, dataset, feature_list)

if __name__ == '__main__':
    main()
```

## 10.3 获取数据特征

```python
import matplotlib.pyplot as plt

print "\n","######### total numbers of data point:"
print len(data_dict)

# 获取所有的feature总数以及名称，注意第一个是label，所以最后feature数是len(features)-1
print "\n","######### total numbers of features:"
for features in data_dict.values():
    print len(features)
    print features
    break

# 检查数据中poi的数目
print "\n","######### total number of poi:"
pois = [x for x, y in data_dict.items() if y['poi']]
print len(pois)
```

## 10.4 检查数据中的无效值

```python
print "######### check the nan data:"
for key,value in data_dict.items():
	nan_num = 0
	for i in value.values():
		if i == "NaN":
			nan_num = nan_num + 1

	if nan_num > 15:
		print key,":",nan_num
```

## 10.5 绘图并寻找异常值

```python
print "\n","######### find the outliers:"
salary_list = []
bonus_list = []

for features in data_dict.values():
	plt.scatter(features["salary"], features["bonus"])

	# 只有当非无效值时才加入list
	if features["salary"] == "NaN" or features["bonus"] == "NaN":
		continue
	salary_list.append(features["salary"])
	bonus_list.append(features["bonus"])

# 排序
bonus_list.sort()
salary_list.sort()

# 输出最大的前5位
print "\n","######### the top five:"
print salary_list[-5:]
print bonus_list[-5:]

print "\n","######### the bottom five:"
print salary_list[0:5]
print bonus_list[0:5]


# 描画salary与bonus的点阵图，这是未处理异常值时的原始数据
plt.title('The original dataset:')
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

# 打印出异常数据
print "\n","######### top of the salary and bonus:"
print "######### show the problem data point:"
for key,value in data_dict.items():
	if value["salary"] == salary_list[-1]:
		print ""
		print key,"'s salary : ",value["salary"]

	if value["bonus"] == bonus_list[-1]:
		print ""
		print key,"'s bonus : ",value["bonus"]

	# 这部分数据是通过输出无效值时，目视得到的异常数据
	if key == "THE TRAVEL AGENCY IN THE PARK" or key == "LOCKHART EUGENE E":
		print ""
		print key,":"
		print value
```

## 10.6 删除异常数据并再次绘图

```python
my_dataset = data_dict

### add by lj
# 将异常数据删除
my_dataset.pop("TOTAL")
my_dataset.pop("THE TRAVEL AGENCY IN THE PARK")
my_dataset.pop("LOCKHART EUGENE E")
print "\n","after(remove outliers), the total number of the dataset:"
print len(my_dataset)

# 重新绘图
for features in my_dataset.values():
	plt.scatter(features["salary"], features["bonus"])

plt.title('After removing the outliers:')
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
```

## 10.7 输出数据的基本信息

```python
import numpy as np
import pandas as pd

# 输出每个feature的信息，仅供自己参考用，非要求
df = pd.DataFrame.from_dict(data_dict, orient='index')
df.replace('NaN', np.nan, inplace = True)

df.info()
```

## 10.8 绘图(from_poi_to_this_person/from_this_person_to_poi)

```python
for features in my_dataset.values():
	colors = features["poi"]
	# 根据是否是POI，决定点的颜色
	if colors == True:
		colors = "red"
	else:
		colors = "blue"
	plt.scatter(features["from_poi_to_this_person"], features["from_this_person_to_poi"], c=colors,alpha=0.5)

plt.xlabel("from_poi_to_this_person")
plt.ylabel("from_this_person_to_poi")
plt.show()
```

## 10.9 添加新的特征

```python
def computeFraction( poi_messages, all_messages ):
    fraction = 0.
    if poi_messages == "NaN" or all_messages == "NaN":
        return 0

    fraction = float(poi_messages)/all_messages
    
    return fraction

# 添加新的特征
for i in data_dict:
    my_dataset[i]['fraction_from_poi'] = computeFraction(my_dataset[i]['from_poi_to_this_person'],my_dataset[i]['to_messages'])
    my_dataset[i]['fraction_to_poi'] = computeFraction(my_dataset[i]['from_this_person_to_poi'],my_dataset[i]['from_messages'])
```

## 10.10 利用新的特征绘图

```python
for features in my_dataset.values():
	colors = features["poi"]
	if colors == True:
		colors = "red"
	else:
		colors = "blue"
	plt.scatter(features["fraction_from_poi"], features["fraction_to_poi"], c=colors,alpha=0.5)

plt.xlabel("fraction_from_poi")
plt.ylabel("fraction_to_poi")
plt.show()
```

## 10.11 Select_K_Best算法计算特征的得分

```python
from sklearn.feature_selection import SelectPercentile,SelectKBest

def Select_K_Best(data_dict, features_list, k):

    data_array = featureFormat(data_dict, features_list)
    labels, features = targetFeatureSplit(data_array)

    k_best = SelectKBest(k=k)
    k_best.fit(features, labels)
    scores = k_best.scores_
    tuples = zip(features_list[1:], scores)
    k_best_features = sorted(tuples, key=lambda x: x[1], reverse=True)

    return k_best_features[:k]

print "\n",Select_K_Best(my_dataset,features_list,5)

# 选取最高得分的5个特征，以及POI label
features_list = ["poi"] + [x[0] for x in Select_K_Best(my_dataset,features_list,5)] 

print "\n",features_list
```

## 10.12 特征缩放

```python
from sklearn.preprocessing import MinMaxScaler

print "\n",features[0:3]

scaler = MinMaxScaler()
features_new = scaler.fit_transform(features)

print "\n",features_new[0:3]
```

## 10.13 使用5种机器学习算法并评分

```python
labels = np.asarray(labels)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

## 1. GaussianNB
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

t1 = time()

clf_NB = GaussianNB()
parm = {}

clf_NB = Pipeline([('scaler',scaler),('gnb',clf_NB)])
gs = GridSearchCV(clf_NB,parm)
gs.fit(features_train,labels_train)

clf_NB = gs.best_estimator_

print "\nGaussianNB score:\n",clf_NB.score(features_train,labels_train)
print "GaussianNB score time:", round(time()-t1, 3), "s"

##  Test Point
from tester import dump_classifier_and_data,test_classifier

# 使用的是tester.py中的test_classifier函数评分
print "\nGaussianNB:\n",test_classifier(clf_NB,my_dataset,features_list)

## 2. Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

t2 = time()

parms = {'criterion': ['gini', 'entropy'], \
			'min_samples_split': [2, 5, 10, 20], \
			'max_depth': [None, 2, 5, 10], \
			'splitter': ['random', 'best'], \
			'max_leaf_nodes': [None, 5, 10, 20]   }

clf_DT = tree.DecisionTreeClassifier()

gs = GridSearchCV(clf_DT,parms)
gs.fit(features_train,labels_train)

clf_DT = gs.best_estimator_

print "\nDecision Tree Classifier\n",clf_DT.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t2, 3), "s"

##  Test Point
print "\nDecision Tree Classifier Test Point:\n",test_classifier(clf_DT,my_dataset,features_list)

## 3. SVM

from sklearn.svm import SVC
parms = {'svc__kernel':('linear','rbf'),'svc__C':[1.0,2.0]}

t3 = time()
clf_SVC = SVC()

pipeline2 = Pipeline([('scaler',scaler),('svc',clf_SVC)])
# a = pipeline.fit(features_train,labels_train)
gs = GridSearchCV(pipeline2,parms)
gs.fit(features_train,labels_train)

clf_SVC = gs.best_estimator_

print "\nSVM \n",clf_SVC.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t3, 3), "s"

##  Test Point
print "\nSVM:\n",test_classifier(clf_SVC,my_dataset,features_list)


### 4. RandomForest
from sklearn.ensemble import RandomForestClassifier

t4 = time()

print '\nRandomForest\n'
clf_RF = RandomForestClassifier()
parameters = {'criterion': ['gini', 'entropy'], \
			'max_depth': [None, 2, 5, 10], \
			'max_leaf_nodes': [None, 5, 10, 20], \
			'n_estimators': [1, 5, 10, 50, 100]}
gs = GridSearchCV(clf_RF, parameters)
gs.fit(features_train,labels_train)

clf_RF = gs.best_estimator_

print "\nRandomForest:\n",clf_RF.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t4, 3), "s"

##  Test Point
print "\nRandomForest:\n",test_classifier(clf_RF,my_dataset,features_list)


### 5. AdaBoost
from sklearn.ensemble import AdaBoostClassifier

t5 = time()

clf_AB = AdaBoostClassifier(algorithm='SAMME')
parameters = {'learning_rate': [0.1, 0.5, 1.0, 5.0], \
			'algorithm': ['SAMME', 'SAMME.R'], \
			'n_estimators': [1, 5, 10, 50, 100]}
gs = GridSearchCV(clf_AB, parameters)
gs.fit(features_train,labels_train)

clf_AB = gs.best_estimator_

print "\nAdaBoost:\n",clf_AB.score(features_train,labels_train)
print "Decision Tree Classifier:", round(time()-t5, 3), "s"

##  Test Point
print "\nAdaBoost:\n",test_classifier(clf_AB,my_dataset,features_list)
```


# 11. 代码输出

上述代码输出结果如下：

```
E:\udacity\32-ML\the project for summiting\ud120-projects-master\final_project>python poi_id.py

######### total numbers of data point:
146

######### total numbers of features:
21
{'salary': 365788, 'to_messages': 807, 'deferral_payments': 'NaN', 'total_payments': 1061827, 'exercised_stock_options': 'NaN', 'bonus': 600000, 'restricted_stock': 585062, 'shared_receipt_with_poi': 702, 'restricted_stock_deferred': 'NaN', 'total_stock_value': 585062, 'expenses': 94299, 'loan_advances': 'NaN', 'from_messages': 29, 'other': 1740, 'from_this_person_to_poi': 1, 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN', 'email_address': 'mark.metts@enron.com', 'from_poi_to_this_person': 38}

######### total number of poi:
18

######### check the nan data:
LOWRY CHARLES P : 16
CHAN RONNIE : 16
WODRASKA JOHN : 17
URQUHART JOHN A : 16
WHALEY DAVID A : 18
MENDELSOHN JOHN : 16
CLINE KENNETH W : 17
WAKEHAM JOHN : 17
WROBEL BRUCE : 18
MEYER JEROME J : 16
SCRIMSHAW MATTHEW : 17
GATHMANN WILLIAM D : 16
GILLIS JOHN : 17
LOCKHART EUGENE E : 20
PEREIRA PAULO V. FERRAZ : 16
BLAKE JR. NORMAN P : 16
THE TRAVEL AGENCY IN THE PARK : 18
CHRISTODOULOU DIOMEDES : 16
WINOKUR JR. HERBERT S : 16
YEAP SOON : 16
FUGH JOHN L : 16
SAVAGE FRANK : 17
GRAMM WENDY L : 18

######### find the outliers:

######### the top five:
[655037, 1060932, 1072321, 1111258, 26704229]
[5249999, 5600000, 7000000, 8000000, 97343619]

######### the bottom five:
[76399, 162779, 170941, 182245, 184899]
[70000, 100000, 100000, 200000, 200000]

######### top of the salary and bonus:
######### show the problem data point:

LOCKHART EUGENE E :
{'salary': 'NaN', 'to_messages': 'NaN', 'deferral_payments': 'NaN', 'total_payments': 'NaN', 'exercised_stock_options': 'NaN', 'bonus': 'NaN', 'restricted_stock': 'NaN', 'shared_receipt_with_poi': 'NaN', 'restricted_stock_deferred': 'NaN', 'total_stock_value': 'NaN', 'expenses': 'NaN', 'loan_advances': 'NaN', 'from_messages': 'NaN', 'other': 'NaN', 'from_this_person_to_poi': 'NaN', 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN', 'email_address': 'NaN', 'from_poi_to_this_person': 'NaN'}

THE TRAVEL AGENCY IN THE PARK :
{'salary': 'NaN', 'to_messages': 'NaN', 'deferral_payments': 'NaN', 'total_payments': 362096, 'exercised_stock_options': 'NaN', 'bonus': 'NaN', 'restricted_stock': 'NaN', 'shared_receipt_with_poi': 'NaN', 'restricted_stock_deferred': 'NaN', 'total_stock_value': 'NaN', 'expenses': 'NaN', 'loan_advances': 'NaN', 'from_messages': 'NaN', 'other': 362096, 'from_this_person_to_poi': 'NaN', 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN', 'email_address': 'NaN', 'from_poi_to_this_person': 'NaN'}

TOTAL 's salary :  26704229

TOTAL 's bonus :  97343619

after(remove outliers), the total number of the dataset:
143
<class 'pandas.core.frame.DataFrame'>
Index: 143 entries, ALLEN PHILLIP K to YEAP SOON
Data columns (total 21 columns):
salary                       94 non-null float64
to_messages                  86 non-null float64
deferral_payments            38 non-null float64
total_payments               123 non-null float64
exercised_stock_options      101 non-null float64
bonus                        81 non-null float64
restricted_stock             109 non-null float64
shared_receipt_with_poi      86 non-null float64
restricted_stock_deferred    17 non-null float64
total_stock_value            125 non-null float64
expenses                     94 non-null float64
loan_advances                3 non-null float64
from_messages                86 non-null float64
other                        91 non-null float64
from_this_person_to_poi      86 non-null float64
poi                          143 non-null bool
director_fees                16 non-null float64
deferred_income              48 non-null float64
long_term_incentive          65 non-null float64
email_address                111 non-null object
from_poi_to_this_person      86 non-null float64
dtypes: bool(1), float64(19), object(1)
memory usage: 23.6+ KB

[('exercised_stock_options', 24.815079733218194), ('total_stock_value', 24.182898678566879), ('bonus', 20.792252047181535), ('salary', 18.289684043404513), ('fraction_to_poi', 16.409712548035799)]

['poi', 'exercised_stock_options', 'total_stock_value', 'bonus', 'salary', 'fraction_to_poi']

[array([  1.72954100e+06,   1.72954100e+06,   4.17500000e+06,
         2.01955000e+05,   2.96127563e-02]), array([ 257817.,  257817.,       0.,       0.,       0.]), array([  4.04615700e+06,   5.24348700e+06,   0.00000000e+00,
         4.77000000e+02,   0.00000000e+00])]

[[  5.03529074e-02   3.60830823e-02   5.21875000e-01   1.81735475e-01
    2.96127563e-02]
 [  7.50594264e-03   6.14210338e-03   0.00000000e+00   0.00000000e+00
    0.00000000e+00]
 [  1.17797594e-01   1.07571339e-01   0.00000000e+00   4.29243254e-04
    0.00000000e+00]]

GaussianNB score:
0.857142857143
GaussianNB score time: 0.017 s

GaussianNB:
Pipeline(steps=[('scaler', MinMaxScaler(copy=True, feature_range=(0, 1))), ('gnb', GaussianNB(priors=None))])
        Accuracy: 0.84879       Precision: 0.45558      Recall: 0.30000 F1: 0.36177     F2: 0.32199
        Total predictions: 14000        True positives:  600    False positives:  717   False negatives: 1400   True negatives: 11283

None

Decision Tree Classifier
0.868131868132
Decision Tree Classifier: 1.496 s

Decision Tree Classifier Test Point:
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=10, min_impurity_split=1e-07,
            min_samples_leaf=1, min_samples_split=20,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='random')
        Accuracy: 0.85050       Precision: 0.43906      Recall: 0.16750 F1: 0.24249     F2: 0.19114
        Total predictions: 14000        True positives:  335    False positives:  428   False negatives: 1665   True negatives: 11572

None

SVM
0.879120879121
Decision Tree Classifier: 0.061 s

SVM:
Pipeline(steps=[('scaler', MinMaxScaler(copy=True, feature_range=(0, 1))), ('svc', SVC(C=2.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False))])
        Accuracy: 0.86543       Precision: 0.79897      Recall: 0.07750 F1: 0.14129     F2: 0.09458
        Total predictions: 14000        True positives:  155    False positives:   39   False negatives: 1845   True negatives: 11961

None

RandomForest


RandomForest:
1.0
Decision Tree Classifier: 50.931 s

RandomForest:
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=10, max_features='auto', max_leaf_nodes=20,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=50, n_jobs=1, oob_score=False, random_state=None,
            verbose=0, warm_start=False)
        Accuracy: 0.85493       Precision: 0.48407      Recall: 0.23550 F1: 0.31685     F2: 0.26245
        Total predictions: 14000        True positives:  471    False positives:  502   False negatives: 1529   True negatives: 11498

None

AdaBoost:
0.901098901099
Decision Tree Classifier: 7.695 s

AdaBoost:
AdaBoostClassifier(algorithm='SAMME', base_estimator=None, learning_rate=0.1,
          n_estimators=100, random_state=None)
        Accuracy: 0.86193       Precision: 0.56238      Recall: 0.15100 F1: 0.23808     F2: 0.17688
        Total predictions: 14000        True positives:  302    False positives:  235   False negatives: 1698   True negatives: 11765

None

```
