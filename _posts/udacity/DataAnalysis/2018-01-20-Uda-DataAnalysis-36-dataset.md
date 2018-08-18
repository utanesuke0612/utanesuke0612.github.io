---
layout: post
title: Uda-DataAnalysis-36-机器学习-数据集与问题
date: 2018-01-16 06:00:01
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}

# 13. 数据集大小 / 特征数 / 问题POI数

修改 `E:\udacity\32-ML\ud120-projects-master\datasets_questions\explore_enron_data.py` 的代码如下，求解标题的三个问题：

```python
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

print "######### 特征数"
for features in enron_data.values():
    print len(features)
    print features
    break

print "######### 有问题的poi数"
i = 0
for key,value in enron_data.items():
	if (value["poi"] == 1):
		i = i + 1
print i
```

输出结果为：

```python
146
#########
21
{'salary': 365788, 'to_messages': 807, 'deferral_payments': 'NaN', 'total_payments': 1061827, 'exercised_stock_options': 'NaN', 'bonus': 600000, 'restricted_stock': 585062, 'shared_receipt_with_poi': 702, 'restricted_stock_deferred': 'NaN', 'total_stock_value': 585062, 'expenses': 94299, 'loan_advances': 'NaN', 'from_messages': 29, 'other': 1740, 'from_this_person_to_poi': 1, 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN', 'email_address': 'mark.metts@enron.com', 'from_poi_to_this_person': 38}
#########
18
```

# 18. 特定人员的股票数目

和任何字典的字典一样，个人/特征可以这样被访问：
`enron_data["LASTNAME FIRSTNAME"]["feature_name"]`
或者 
`enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]`
James Prentice 名下的股票总值是多少？

```python
for key,value in enron_data.items():
	if (key == "PRENTICE JAMES"):
		print key
		print value["total_stock_value"]

# this method is more simple
print enron_data["PRENTICE JAMES"]["total_stock_value"]
```

输出结果为:`1095040`

# 28. 字典到数组的转换


不能将 python 字典直接读入到 sklearn 分类或回归算法中；它其实需要一个 numpy 数组，或者一个由列表组成的列表（此列表本身是一个列表，它的每个元素都是数据点，而较小列表的元素是该点的特征）。

我们编写了一些辅助函数（tools/feature_format.py 中的 featureFormat() 和 targetFeatureSplit()），它们可以获取特征名的列表和数据字典，然后返回 numpy 数组。

如果特征没有某个特定人员的值，此函数还会用 0（零）替换特征值。

```python 	
import numpy as np

def featureFormat( dictionary, features, remove_NaN=True, remove_all_zeroes=True, remove_any_zeroes=False, sort_keys = False):
    """ convert dictionary to numpy array of features
        remove_NaN = True will convert "NaN" string to 0.0
        remove_all_zeroes = True will omit any data points for which
            all the features you seek are 0.0
        remove_any_zeroes = True will omit any data points for which
            any of the features you seek are 0.0
        sort_keys = True sorts keys by alphabetical order. Setting the value as
            a string opens the corresponding pickle file with a preset key
            order (this is used for Python 3 compatibility, and sort_keys
            should be left as False for the course mini-projects).
        NOTE: first feature is assumed to be 'poi' and is not checked for
            removal for zero or missing values.
    """


    return_list = []

    # Key order - first branch is for Python 3 compatibility on mini-projects,
    # second branch is for compatibility on final project.
    if isinstance(sort_keys, str):
        import pickle
        keys = pickle.load(open(sort_keys, "rb"))
    elif sort_keys:
        keys = sorted(dictionary.keys())
    else:
        keys = dictionary.keys()

    for key in keys:
        tmp_list = []
        for feature in features:
            try:
                dictionary[key][feature]
            except KeyError:
                print "error: key ", feature, " not present"
                return
            value = dictionary[key][feature]
            if value=="NaN" and remove_NaN:
                value = 0
            tmp_list.append( float(value) )

        # Logic for deciding whether or not to add the data point.
        append = True
        # exclude 'poi' class as criteria.
        if features[0] == 'poi':
            test_list = tmp_list[1:]
        else:
            test_list = tmp_list
        ### if all features are zero and you want to remove
        ### data points that are all zero, do that here
        if remove_all_zeroes:
            append = False
            for item in test_list:
                if item != 0 and item != "NaN":
                    append = True
                    break
        ### if any features for a given data point are zero
        ### and you want to remove data points with any zeroes,
        ### handle that here
        if remove_any_zeroes:
            if 0 in test_list or "NaN" in test_list:
                append = False
        ### Append the data point if flagged for addition.
        if append:
            return_list.append( np.array(tmp_list) )

    return np.array(return_list)


def targetFeatureSplit( data ):
    """ 
        given a numpy array like the one returned from
        featureFormat, separate out the first feature
        and put it into its own list (this should be the 
        quantity you want to predict)

        return targets and features as separate lists

        (sklearn can generally handle both lists and numpy arrays as 
        input formats when training/predicting)
    """

    target = []
    features = []
    for item in data:
        target.append( item[0] )
        features.append( item[1:] )

    return target, features
```

