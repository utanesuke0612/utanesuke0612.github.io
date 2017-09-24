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
# 1. 数据分析过程
数据分析的主要流程包括：提出问题、数据收集与清洗、数据探索、得出结论或做出预测以及结果交流。

- 提出问题：兴趣是学习最好的老师。在课程中，我们会经常鼓励你提出自己感兴趣的问题并尝试回答。感兴趣的问题会激发你的好奇心，引导你不断地探索和分析数据。
- 数据收集与清洗：数据是分析的基础，数据的质量很大程度上决定分析的准确性。因此，在正式分析之前，优秀的数据分析师都会去了解数据的来源并基于使用的目的来清洗数据。事实上，这一步将占用分析师大量的时间，因此掌握高效的清洗技能非常重要。
- 数据探索：我们周围充斥着大量的数据。基于想要回答的问题，你可能需要分析几百MB上G甚至更多的数据。面对这样大规模的数据，你需要掌握一些探索性数据分析的方法帮助你快速找到分析的方向并确定主要变量的关系。这对你分析的效率非常有帮助。
- 得出结论或做出预测：回顾整个数据探索的过程并从中选出最佳的发现用来回答你的问题。有时你也会建立机器学习模型来对未来的数据做出预测。
- 结果交流：这部分恰恰是很多数据分析师所忽略的地方。分析师的价值不止在于发现数据的奥秘，更在于可以把自己的发现分享给自己的老板、同事或任何对问题感兴趣的人，酒香也怕巷子深。而在交流的过程中，合适的可视化图表将会让你事半功倍。


# 2. 使用Anaconda
本课程中使用的是python 2.7，在浏览器中打开 https://www.continuum.io/downloads 后，下载对应的python2.7版本的程序。

## 2.1 IPython笔记本
IPython 笔记本是为数据分析师准备的强大工具，允许你将代码、图形、输入和描述合并到一个简单易读的文档中。
打开 `jupyter notebook`程序后，笔记本在浏览器中运行，从浏览器中可以打开ipynb文件。

`table_descriptions.txt`，其中描述了每个文件（或数据表）中呈现的数据和列。
- enrollments.csv:数据分析纳米学位学员中，完成了第一个项目的学员的一个随机子集的数据，以及没有完成第一个项目的学员的一个随机子集的数据。
- daily_engagement.csv:报名注册表中每一位学生，在数据分析纳米学位的日常参与学习数据。
- project_submissions.csv:关于在报名注册表中的每个学生提交数据分析纳米学位项目的数据。
- daily_engagement_full.csv:与 daily_engagement.csv 类似，但是进一步细分课程和更多可以用的字段。

## 2.2 Ipython的使用
Ipython中可以插入代码，也可以插入markdown文本(先以cell的方式插入，再在cell - cell type中修改)。
如下是几段示例代码:

```python
import matplotlib.pyplot as plt

xs = range(-30, 31)
ys = [x ** 2 for x in xs]

plt.scatter(xs, ys)

```

![image](https://user-images.githubusercontent.com/18595935/30770702-05cd59b4-a072-11e7-977a-fba93dbfefaf.png)

## 2.3 Ipython中的快捷键
- Enter：进入编辑模式
- Enter + Shift：进入下一个单元格
- a 在当前单元格前面插入cell，b 在当前单元格后面插入cell
- 一行连续按两次 D 可以删除单元格
- 在一个单元格中，按照 control + enter可以运行代码
- tab进行代码补全(opera中不灵)
- 更多shortcut参考help菜单。


# 3. 数据采集和清洗

## 3.1 熟悉CSV的处理
csv是一组以`,`分隔的一维数组，纯文本文件。

- [此页面](https://www.codementor.io/sheena/python-generators-and-iterators-du1082iua)解释了 Python 中迭代器（iterators）和列表（lists）之间的区别，以及如何使用迭代器。
如下的reader并不是个列表，是一种迭代器。对每个迭代器只能进行一次循环，比如再追加`for row in reader: print 'yes'`，无法进行print。

```python
import unicodecsv

enrollments=[]
f = open('enrollments.csv','rb')
reader = unicodecsv.DictReader(f)

for row in reader:
    enrollments.append(row)

f.close()

enrollments[0]
```

输出如下：
```
    {u'account_key': u'448',
     u'cancel_date': u'2015-01-14',
     u'days_to_cancel': u'65',
     u'is_canceled': u'True',
     u'is_udacity': u'True',
     u'join_date': u'2014-11-10',
     u'status': u'canceled'}
```


- 改进后的代码，通过with语句，使得文件在使用完毕后能自动关闭；另外，通过list(reader)能将迭代器转换为list。

```python
import unicodecsv

enrollments=[]
with open('enrollments.csv','rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

enrollments[0]
```

输出如下：
```python
    {u'account_key': u'448',
     u'cancel_date': u'2015-01-14',
     u'days_to_cancel': u'65',
     u'is_canceled': u'True',
     u'is_udacity': u'True',
     u'join_date': u'2014-11-10',
     u'status': u'canceled'}
```

如下是练习中的答案：
1. 将读取csv的过程函数化了。
2. 注意with和迭代器转list的用法。

```python
import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily-engagement.csv')
project_submissions = read_csv('project-submissions.csv')
```

## 3.2 清理数据
可以看到上面所有输出数据的格式都是String，但是如果要进行处理，有一部分要变成int，一部分需要变成date类型，或True/False的bool。
注意`int(float(engagement_record['lessons_completed']))`，因为在csv中数据为`0.0`，这种字符串直接转变为int会报错，需要先转为float。

```python
from datetime import datetime as dt

# 将字符串格式的时间转为 Python datetime 类型的时间。
# 如果没有时间字符串传入，返回 None

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# 将可能是空字符串或字符串类型的数据转为 整型 或 None。

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# 清理 enrollments 表格中的数据类型

for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

enrollments[0]

# 清理 engagement 的数据类型
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

daily_engagement[0]

# 清理 submissions 的数据类型
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

project_submissions[0]


```

现在输出的数据为，变成了我们理想的数据格式，便于后续的处理:

```python
{u'account_key': u'448',
 u'cancel_date': datetime.datetime(2015, 1, 14, 0, 0),
 u'days_to_cancel': 65,
 u'is_canceled': True,
 u'is_udacity': True,
 u'join_date': datetime.datetime(2014, 11, 10, 0, 0),
 u'status': u'canceled'}
```


## 3.3 获取学生数目

- 找出每个csv中记录的数目和学生的数目
- 一个学生可能选重复的课程，所以将将学生的key去重复

```python
## 计算每张表中的总行数，和独立学生（拥有独立的 account keys）的数量

def get_unique_account_set(attri_list,key):
    account_set = set()
    # 添加到集合set中会自动去除重复
    for attri in attri_list:
        account_set.add(attri[key])

    return account_set

enrollment_num_rows = len(enrollments)           
enrollment_num_unique_students = len(get_unique_account_set(enrollments,'account_key'))

engagement_num_rows = len(daily_engagement)           
engagement_num_unique_students = len(get_unique_account_set(daily_engagement,'acct'))  

submission_num_rows = len(project_submissions)      
submission_num_unique_students = len(get_unique_account_set(project_submissions,'account_key'))

```

最终的输出如下:

```python
1640 # 注册条数
1302 # 注册的学生数
136240 # 参与了的课程数
1237 # 参与了课程的学生数
3642 # 提交的项目数
743 # 提交了项目的学生数
```


## 3.4 数据中的问题
1. 为什么注册的学生数，比参与课程的学生数要多？
2. 同一个属性的字段，在各个表中的index名不同，两个表中为`account_key`，一个表中为`acct`。

- 下面的代码中先添加一个列`account_key`，用已有的`acct`赋值给它，再将原始的列删除。

```python
## 将 daily_engagement 表中的 "acct" 重命名为 ”account_key"
for daily_engagement_record in daily_engagement:
    daily_engagement_record['account_key'] = daily_engagement_record['acct']
    del(daily_engagement_record['acct'])
```

- 分析为什么学生数目不一致
分析思路:
1. 找出异常的数据点Identify surprising data points
  - 在注册表中存在，但是在参与表中没有的记录。
2. 输出异常的数据点 Print out one or a few surprising data points
3. 解决问题 Fix any problems you find

```python
## 找到任意一个 enrollments 中的学生，但不在 daily engagement 表中。
## 打印出这条 enrollments 记录。

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in get_unique_account_set(daily_engagement,'account_key'):
        print enrollment
        break
```

输出结果：

```python
{u'status': u'canceled', u'is_udacity': u'True', u'is_canceled': u'True', u'join_date': u'2015-01-10', u'account_key': u'1304', u'cancel_date': u'2015-03-10', u'days_to_cancel': u'59'}
{u'status': u'canceled', u'is_udacity': u'True', u'is_canceled': u'True', u'join_date': u'2015-03-10', u'account_key': u'1304', u'cancel_date': u'2015-06-17', u'days_to_cancel': u'99'}
{u'status': u'canceled', u'is_udacity': u'False', u'is_canceled': u'True', u'join_date': u'2014-11-12', u'account_key': u'841', u'cancel_date': u'2014-11-12', u'days_to_cancel': u'0'}

```

从上面结果发现，几乎都是当前注册当天就取消了。但是也有例外，例外的条数为3，即3条数据不是当天取消的:

```python
## 计算无众不同的数据点条数（在 enrollments 中存在，但在 engagement 表中缺失）

num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in get_unique_account_set(daily_engagement,'account_key') and
            enrollment['join_date'] != enrollment['cancel_date']):
        print enrollment
        num_problem_students += 1

num_problem_students
```

输出结果为:

```python
{u'status': u'canceled', u'is_udacity': u'True', u'is_canceled': u'True', u'join_date': u'2015-01-10', u'account_key': u'1304', u'cancel_date': u'2015-03-10', u'days_to_cancel': u'59'}
{u'status': u'canceled', u'is_udacity': u'True', u'is_canceled': u'True', u'join_date': u'2015-03-10', u'account_key': u'1304', u'cancel_date': u'2015-06-17', u'days_to_cancel': u'99'}
{u'status': u'current', u'is_udacity': u'True', u'is_canceled': u'False', u'join_date': u'2015-02-25', u'account_key': u'1101', u'cancel_date': u'', u'days_to_cancel': u''}
3
```

为什么会出现这种情况，因为其`u'is_udacity': u'True'`，说明这个是测试用账号。

## 3.5 解决数据中的问题
- 先将测试帐号抽取出来，输出为`6`：

```python
# 为所有 Udacity 测试帐号建立一组 set
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)
```

- 再将三个表中的测试帐号相关的记录删除:

```python
# 重新生成了一个非测试账号的数据集
# 通过 account_key 删除所有 Udacity 的测试帐号
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print len(non_udacity_enrollments) # 输出 1622
print len(non_udacity_engagement) # 输出 135656
print len(non_udacity_submissions) # 输出 3634

```

## 3.6 : 分析更多数据-提炼问题

抽取具有如下条件的学生:
- 没有cancel的
- 超过7天(试用期外)cancel
- keys:account_key values:enrollement_date



```python
## 创建一个叫 paid_students 的字典，并在字典中存储所有还没有取消或者注册时间超过7天的学生。
## 字典的键为帐号（account key），值为学生注册的时间。

paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
len(paid_students)

```

>説明①： 这个是安全处理，因为一个学生有可能多次注册，所以要添加判断:
> - 如果该学生不在paid_students中，则直接`追加`进去(因为该account_key还不存在)
> - 如果该学生在paid_students中，并且注册日期是大于之前的，则更新为最新的数据(因为account_key已经存在，则为更新)

上面的or判断是个短路的判断，不能颠倒顺序，即如果前一个条件满足，则不会判断第二个了。
但是使用`|`的话，就是两个都要判断。

```python
In [10]: 1 or 1/0
Out[10]: 1

In [11]: 0 or 1/0
---------------------------------------------------------------------------
ZeroDivisionError: integer division or modulo by zero

In [12]: 1 | 1/0
---------------------------------------------------------------------------
ZeroDivisionError: integer division or modulo by zero

```

## 3.7 获取一周的数据

```python
# 基于学生的加入日期和特定一天的互动记录，若该互动记录发生在学生加入1周内，则反回 True

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

## 创建一个 engagement 记录的列表，该列表只包括付费学生以及加入的前7天的学生的记录
def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print len(paid_enrollments)
print len(paid_engagement)
print len(paid_submissions)

## 输入符合要求的行数
paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

len(paid_engagement_in_first_week)

```
