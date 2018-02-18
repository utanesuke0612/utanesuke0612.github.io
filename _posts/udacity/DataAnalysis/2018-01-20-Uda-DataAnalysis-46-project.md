---
layout: post
title: Uda-DataAnalysis-46-机器学习-【ing】-进阶项目3：从安然公司邮件中发现欺诈证据
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

本数据集中，包含了146条记录，每条记录中包含了雇员的财务和邮件相关信息，另外数据中包含21个特征。进一步分析数据中的每条记录的`poi`特征，发现共有18条记录可能是嫌疑人。

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

|算法|耗时(s)|
|:--|--:|
|GaussianNB|0.021|
|Decision Tree|1.492|
|SVM|0.056|
|RandomForest|54.018|
|AdaBoost|7.314|

## 4.1 最终选定的算法

>3.你最终使用了什么算法？

通过对上面评分结果(Accuracy,Recall,F1,ie.)的分析，判断`GaussianNB classifier`给出了最好的预测结果。

## 4.2 调试算法

>4.调整算法的参数是什么意思，如果你不这样做会发生什么？你是如何调整特定算法的参数的？

在代码中，使用了`GridSearchCV()`来调试各个算法的参数，另外通过`test_classifier()`测试了算法并给出了判断结果，经过调试最好的结果来自`GaussianNB classifier`。

对参数的调试是机器学习中很重要的一环，因为不同的算法函数和初始设定会对最终结果产生很多影响。在某些情况下，为算法选择了错误的参数，会造成过拟合。

# 5. 验证与评价

>5.什么是验证，未正确执行情况下的典型错误是什么？你是如何验证你的分析的？

验证是将训练出得模型，用测试数据进行评价的过程，验证中的典型错误是没有将数据分成训练和测试两部分，从而导致过拟合。
在这里使用交叉验证`train_test_split()`函数，将数据的30%作为测试数据，得到最终得评价结果如下：

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

最终选取的算法是朴素贝叶斯`GaussianNB`，主要基于准确率`Accuracy`,召回率`Recall`和综合评价指标`F1`等进行的判断。

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

- 关于准确率`Accuracy`:
准确率(accuracy)计算公式为： `ACC = (TP+TN) / (TP+TN+FP+FN)`，准确率是我们最常见的评价指标，而且很容易理解，就是被分对的样本数除以所有的样本数，通常来说，正确率越高，分类器越好。 但是在在正负样本不平衡的情况下，准确率这个评价指标有很大的缺陷。本数据集中的数据是不均衡的，所以不能单纯只依靠准确率来评价。

- 关于召回率`Recall`：
召回率是覆盖面的度量，度量有多个正例被分为正例，`recall=TP/(TP+FN)=TP/P=sensitive`，可以看到召回率与灵敏度是一样的。s

- 关于综合评价指标`F1`：
Precision与Recall有时候会出现矛盾，如上表所示，这时就需要综合考虑他们，最常见的方法是F-Measure,F-Measure的计算公式如下：

```python
F = (a**2 + 1)*P*R / a**2(P+R)
```

F是Precision与Recall的甲醛调和评价，当a=1时，就是最常见的F1，公式为 `F1 = 2*P*R / (P+R)`，可见F1综合了P和R的结果，当F1较高时则能说明该模型效果不错，上表中也显示`GaussianNB`的F1为其中的最高值，为`0.36177`。


# 9. 参考
1. [wiki-安然公司](https://zh.wikipedia.org/wiki/%E5%AE%89%E7%84%B6%E5%85%AC%E5%8F%B8)
2. [Identify Fraud From Enron Data](https://arjan-hada.github.io/enron-fraud.html)
3. [sample code](https://jefflirion.github.io/udacity/Intro_to_Machine_Learning/Lesson5.html)
4. [Investigating the Enron Fraud with Machine Learning](http://luizschiller.com/enron/)
5. [机器学习安然数据集分析报告](http://blog.csdn.net/Einstellung/article/details/78387849)
6. [机器学习：准确率(Precision)、召回率(Recall)、F值(F-Measure)、ROC曲线、PR曲线](http://blog.csdn.net/quiet_girl/article/details/70830796)