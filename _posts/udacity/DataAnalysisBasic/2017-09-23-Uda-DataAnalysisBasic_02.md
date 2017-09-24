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
# 创建基于 student 对 engagement 进行分组的字典，字典的键为帐号（account key），值为包含互动记录的列表

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
# 创建一个包含学生在第1周在教室所花总时间和字典。键为帐号（account key），值为数字（所花总时间）
total_minutes_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
          total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes
```

- 统计

```python
import numpy as np

# 汇总和描述关于教室所花时间的数据
total_minutes = total_minutes_by_account.values()
print 'Mean:', np.mean(total_minutes)
print 'Standard deviation:', np.std(total_minutes)
print 'Minimum:', np.min(total_minutes)
print 'Maximum:', np.max(total_minutes)

```
输出如下：

```python
Mean: 647.590173826
Standard deviation: 1129.27121042
Minimum: 0.0
Maximum: 10568.1008673

```

# 2. 找问题
上面有个学生的时间长度为10568分钟，即180小时左右，显然不正常，需要调查。
- 首先要找出异常数据的account_key，都是输出(u'108', 10568.100867332541)，即account_key和总时间长度

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
因为注册之后再注销，反复多次，就造成了join_date可能晚于engagement_date。

## 2.1  找出 `第一周内完成的课程`

在之前的代码中，完成了第一周内时间数的统计，这一类是非常常见的操作，最好将其封装为函数，将要统计的属性作为参数名传递过去。
重构之前的代码，重构后：

```python
from collections import defaultdict

def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

engagement_by_account = group_data(paid_engagement_in_first_week,
                                   'account_key')

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

total_minutes_by_account = sum_grouped_items(engagement_by_account,
                                             'total_minutes_visited')

import numpy as np

def describe_data(data):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)

describe_data(total_minutes_by_account.values())

```

- 调用上面的函数，来分析第一周完成的课程，如下所示：
```python
lessons_completed_by_account = sum_grouped_items(engagement_by_account,
                                                 'lessons_completed')
describe_data(lessons_completed_by_account.values())
```

> 未完待续
