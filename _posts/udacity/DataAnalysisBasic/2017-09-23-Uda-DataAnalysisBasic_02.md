---
layout: post
title: Uda-DataAnalysisBasic-01-数据分析过程(2)
date: 2017-09-23 00:00:00
categories: 数据分析
tags: Python Udacity DataAnalysis
---
* content
{:toc}

> Udacity上的数据分析入门课程，共分四个部分
- 数据分析过程
- 用Numpy和Pandas分析一维数据
- 用Numpy和Pandas分析二维数据
- 最终项目:探索数据集

---
# 1. 探索学员的参与度

通过前一节的实验，有了一组参与超过7天学生数据，但是是无序的。
-现在我们来将这些学生分成多个group,用dictionary的list组织。
  - key:account_key
  - values: list of engagement records
- 再将各组学生的学习时长进行汇总。


- 建立了一个以account_key为索引，以engagement中记录为values的字典
```python
from collections import defaultdict

# 使用默认dict，如果通过一个key在defaultdict中找不到的话，返回一个空的list
engagement_by_account = defaultdict(list)

for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)
```

记住字典与list等的区别，字典是不可迭代的对象，{'0':list1,'1':list2,'999':list999},只能通过dict[index]的方式获取。
这里list内部是engagement_record，也是一个字典类型。即一个学生一周内学习记录，最多有7条。

```python
In[117]: engagement_by_account['2']

# 输出如下:
[{'account_key': u'2',
  u'lessons_completed': u'0.0',
  u'num_courses_visited': u'0.0',
  u'projects_completed': u'0.0',
  u'total_minutes_visited': u'0.0',
  u'utc_date': u'2015-06-08'},
 ...#省略另外5条数据
 {'account_key': u'2',
  u'lessons_completed': u'0.0',
  u'num_courses_visited': u'0.0',
  u'projects_completed': u'0.0',
  u'total_minutes_visited': u'0.0',
  u'utc_date': u'2015-06-14'}]
```

- 将每个学生的时间记录起来
```python
# 将可能是空字符串或字符串类型的数据转为 整型 或 None。
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# 建立一个记录时间的字典，以account_key为索引，一周内的总时间为value
total_minutes_by_account = {}

for account_key,engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += parse_maybe_int(float(engagement_record['total_minutes_visited']))
    total_minutes_by_account[account_key] = total_minutes

```

- 统计

```python
total_minutes = total_minutes_by_account.values()

import numpy as np

print 'mean:',np.mean(total_minutes)
print 'Standard deviation:',np.std(total_minutes)
print 'Minimum',np.min(total_minutes)
print 'Maximum',np.max(total_minutes)

```
输出如下：

```python
mean: 642.870611836
Standard deviation: 1123.12784614
Minimum 0
Maximum 10535

```

# 2. 找问题
上面有个学生的时间长度为10535分钟，即180小时左右，显然不正常，需要调查。
- 首先要找出异常数据的account_key，都是输出`(u'183', 10535)`，即account_key和总时间长度

```python
# 方法1，使用lambda表达式取最大值
max(total_minutes_by_account.items(), key=lambda pair: pair[1])

# 方法2，排序后输出
import operator
sorted_x = sorted(total_minutes_by_account.items(), key=operator.itemgetter(1))
sorted_x[-1]
```

通过该account_key，可以找到对应的engagement_record，发现结果远不止7条，分析其中的时间记录，发现范围超过了一周。
出错的代码为:

```python
# 修改前:
def within_one_week(join_date, engagement_date):
    time_delta =parse_date(engagement_date) - parse_date(join_date)
    return time_delta.days>0 and time_delta.days < 7

# 修改后：
def within_one_week(join_date, engagement_date):
    time_delta =parse_date(engagement_date) - parse_date(join_date)
    return time_delta.days < 7

```
