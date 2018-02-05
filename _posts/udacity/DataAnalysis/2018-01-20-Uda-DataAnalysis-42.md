---
layout: post
title: Uda-DataAnalysis-42-机器学习-特征选择
date: 2018-01-16 12:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 1. 一个新的安然特征练习

新的特征选取过程如下，自觉-》编码-》可视化-》重复:
- use my human intuition
- code up the new feature
- visualize
- repeat

下面是一个练习的编码，确定某个人的邮件接收的邮件中，是否是来自嫌疑人，`if from_emails:`部分是添加的代码：

```python
#!/usr/bin/python

###
### in poiFlagEmail() below, write code that returns a boolean
### indicating if a given email is from a POI
###

import sys
import reader
import poi_emails

def getToFromStrings(f):
    '''
    The imported reader.py file contains functions that we've created to help
    parse e-mails from the corpus. .getAddresses() reads in the opening lines
    of an e-mail to find the To: From: and CC: strings, while the
    .parseAddresses() line takes each string and extracts the e-mail addresses
    as a list.
    '''
    f.seek(0)
    to_string, from_string, cc_string   = reader.getAddresses(f)
    to_emails   = reader.parseAddresses( to_string )
    from_emails = reader.parseAddresses( from_string )
    cc_emails   = reader.parseAddresses( cc_string )

    return to_emails, from_emails, cc_emails


### POI flag an email

def poiFlagEmail(f):
    """ given an email file f,
        return a trio of booleans for whether that email is
        to, from, or cc'ing a poi """

    to_emails, from_emails, cc_emails = getToFromStrings(f)

    ### poi_emails.poiEmails() returns a list of all POIs' email addresses.
    poi_email_list = poi_emails.poiEmails()

    to_poi = False
    from_poi = False
    cc_poi   = False

    ### to_poi and cc_poi are boolean variables which flag whether the email
    ### under inspection is addressed to a POI, or if a POI is in cc,
    ### respectively. You don't have to change this code at all.

    ### There can be many "to" emails, but only one "from", so the
    ### "to" processing needs to be a little more complicated
    if to_emails:
        ctr = 0
        while not to_poi and ctr < len(to_emails):
            if to_emails[ctr] in poi_email_list:
                to_poi = True
            ctr += 1
    if cc_emails:
        ctr = 0
        while not cc_poi and ctr < len(cc_emails):
            if cc_emails[ctr] in poi_email_list:
                cc_poi = True
            ctr += 1

    #################################
    ######## your code below ########
    ### set from_poi to True if #####
    ### the email is from a POI #####
    #################################
    if from_emails:
        ctr = 0
        while not from_poi and ctr < len(from_emails):
            if from_emails[ctr] in poi_email_list:
                from_poi = True
            ctr += 1
    
    #################################
    return to_poi, from_poi, cc_poi
```


- 其中部分的结果如下：

```python
'Billy': {'from_poi_to_this_person': 0}, 'mike.mcconnell@enron.com': {'from_poi_to_this_person': 1}, 'Coal&EmissionsQBRMcClellan': {'from_poi_to_this_person': 0}, 'kent.densley@enron.com': {'from_poi_to_this_person': 0}, 'brad.alford@enron.com': {'from_poi_to_this_person': 0}, 'amy.spoede@enron.com': {'from_poi_to_this_person': 1},
```

- 添加新特征后的散点图，x轴是接收到嫌疑人的邮件数量，y轴是发送给嫌疑人的邮件数量，红色表示此人是嫌疑人：

![image](https://user-images.githubusercontent.com/18595935/35830184-b8157056-0b08-11e8-96f1-e18e0f8c035f.png)

从上图中蓝色点与红色点混合在一起，看不出明显的趋势，所以还需要进一步编码。


# 5. 可视化新特征

上面增加的新特征没有明显的趋势，进一步分析，或许并不是需要某个人发送接收嫌疑人邮件的绝对数量，而是在自己总邮件中的比例，代码如下：

- `studentCode.py`

```python
import pickle
from get_data import getData

def computeFraction( poi_messages, all_messages ):
    """ given a number messages to/from POI (numerator) 
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """
    ### you fill in this code, so that it returns either
    ###     the fraction of all messages to this person that come from POIs
    ###     or
    ###     the fraction of all messages from this person that are sent to POIs
    ### the same code can be used to compute either quantity

    ### beware of "NaN" when there is no known email address (and so
    ### no filled email features), and integer division!
    ### in case of poi_messages or all_messages having "NaN" value, return 0.
    fraction = 0.
    
    if poi_messages == "NaN" or all_messages == "NaN":
        return 0

    fraction = float(poi_messages)/all_messages
    
    return fraction


data_dict = getData() 

submit_dict = {}
for name in data_dict:

    data_point = data_dict[name]

    print
    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    fraction_from_poi = computeFraction( from_poi_to_this_person, to_messages )
    print fraction_from_poi
    data_point["fraction_from_poi"] = fraction_from_poi


    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    fraction_to_poi = computeFraction( from_this_person_to_poi, from_messages )
    print fraction_to_poi
    submit_dict[name]={"from_poi_to_this_person":fraction_from_poi,
                       "from_this_person_to_poi":fraction_to_poi}
    data_point["fraction_to_poi"] = fraction_to_poi
    
    
#####################

def submitDict():
    return submit_dict

```

- `get_data.py`

```python
def getData():
    data = {}
    data["METTS MARK"]={'salary': 365788, 'to_messages': 807, 'deferral_payments': 'NaN', 'total_payments': 1061827, 'loan_advances': 'NaN', 'bonus': 600000, 'email_address': 'mark.metts@enron.com', 'restricted_stock_deferred': 'NaN', 'deferred_income': 'NaN', 'total_stock_value': 585062, 'expenses': 94299, 'from_poi_to_this_person': 38, 'exercised_stock_options': 'NaN', 'from_messages': 29, 'other': 1740, 'from_this_person_to_poi': 1, 'poi': False, 'long_term_incentive': 'NaN', 'shared_receipt_with_poi': 702, 'restricted_stock': 585062, 'director_fees': 'NaN'}
    data["BAXTER JOHN C"]={'salary': 267102, 'to_messages': 'NaN', 'deferral_payments': 1295738, 'total_payments': 5634343, 'loan_advances': 'NaN', 'bonus': 1200000, 'email_address': 'NaN', 'restricted_stock_deferred': 'NaN', 'deferred_income': -1386055, 'total_stock_value': 10623258, 'expenses': 11200, 'from_poi_to_this_person': 'NaN', 'exercised_stock_options': 6680544, 'from_messages': 'NaN', 'other': 2660303, 'from_this_person_to_poi': 'NaN', 'poi': False, 'long_term_incentive': 1586055, 'shared_receipt_with_poi': 'NaN', 'restricted_stock': 3942714, 'director_fees': 'NaN'}
    #...省略上面大部分数据
    return data
```

- 输出结果如下： 
`{'METTS MARK': {'from_poi_to_this_person': 0.04708798017348203, 'from_this_person_to_poi': 0.034482758620689655}, 'BAXTER JOHN C': {'from_poi_to_this_person': 0, 'from_this_person_to_poi': 0},...`

- 可视化：

可以看到红色点集中在黄色部分的上方，则可以推断，如果发送给嫌疑人的邮件比率不到20%，则很可能不是嫌疑人：

![image](https://user-images.githubusercontent.com/18595935/35830877-1219fc46-0b0b-11e8-8664-df9d806b9986.png)

# 7. 去除特征

有时为了处理方便和准确，还需要去除一些特征，理由如下：

- It's noisy
- It causes overfitting
- It is strongly related(highly correlated) with a feature that's already present
- Additional features slow down trainging/testing process

Features 不是 information，如果某个特征不能带来信息，基于上面的原因，这个特征就应该被删除。

# 9. 单变量特征选择

在 sklearn 中自动选择特征有多种辅助方法。多数方法都属于单变量特征选择的范畴，即独立对待每个特征并询问其在分类或回归中的能力。

sklearn 中有两大单变量特征选择工具：`SelectPercentile` 和 `SelectKBest`。 两者之间的区别从名字就可以看出：`SelectPercentile` 选择最强大的 X% 特征（X 是参数），而 `SelectKBest` 选择 K 个最强大的特征（K 是参数）。

由于数据维度太高，特征约简显然要用到文本学习。 实际上，在最初的几个迷你项目中， Sara/Chris 邮件分类的问题上进行了特征选择；可以在 `tools/email_preprocess.py` 的代码中看到它。

# 10. TfIdf 向量器中的特征选择

