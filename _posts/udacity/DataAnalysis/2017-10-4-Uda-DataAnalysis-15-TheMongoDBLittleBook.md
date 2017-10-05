---
layout: post
title: Uda-DataAnalysis-15-the-little-mongodb-book
date: 2017-10-4 00:00:00
categories: Uda-数据分析进阶
tags: Python Udacity DataAnalysis 
---
* content
{:toc}

> Udacity课程中涉及到MongoDb的知识，在学习如何在python中应用MongoDB之前，将这本小册子读一读,理解MongoDB的基本概念很重要。
> [the-little-mongodb-book](https://github.com/ilivebox/the-little-mongodb-book/blob/master/zh-cn/mongodb.markdown)
> 


# 1. 下载与安装

1. 在官方网站上找社区版本的二进制文件 [win32/mongodb-win32-x86_64-2008plus-ssl-v3.4-latest.zip)](https://www.mongodb.org/dl/win32/x86_64-2008plus-ssl?_ga=2.243229121.256873343.1507121726-639191289.1507121726),下载到本地。
2. 按照[the-little-mongodb-book](https://github.com/ilivebox/the-little-mongodb-book/blob/master/zh-cn/mongodb.markdown)中` 开始`部分的指示进行操作。
3. 为了方便，建了一个bat文件，` c:\mongodb\bin\mongod --config c:\mongodb\bin\mongodb.config`，运行直接启动MongoDB。
4. mongo.exe是一个shell，用于输入mongo命令。


# 2. 基础知识

## 2.1 MongoDB与传统数据库的对比

|MongoDB|传统数据库|备注|
|:--|--:|:--:|
|database|数据库|两者概念一样，一个MongoDB实例中可以有多个数据库|
|collection集合|table表|集合与传统意义的table概念类似|	
|documents文档|row行|集合是由多个documents文档构成|	
|field字段|column列|文档由多个field字段组成|	
|index索引|index索引|两者概念类似|	
|Cursors游标|Cursors游标|两者概念类似，游标是，当你问 MongoDB 拿数据的时候，它会给你返回一个结果集的指针而不是真正的数据，这个指针我们叫它游标，我们可以拿游标做我们想做的任何事情，比如说计数或者跨行之类的，而无需把真正的数据拖下来，在真正的数据上操作。|

用一个实际例子说明上述概念:

![image](https://user-images.githubusercontent.com/18595935/31227506-0c099ec6-aa15-11e7-8c51-23a288ad95a4.png)


## 2.2 基础命令

- ` db.unicorns.insert({name: 'Aurora',gender: 'f', weight: 450})` 向集合unicorns中插入一个文档，即一行数据。
- ` db.getCollectionNames()`，查询当前数据中的集合。
- ` db.unicorns.find()`，返回集合unicorns对应的文档列表。
- ` db.unicorns.remove({})`,删除unicorns集合中的数据。
-  `db.unicorns.count()`，返回条数。


## 2.3 掌握选择器(Selector)

- 先追加一些实验用数据：

```python
db.unicorns.insert({name: 'Dunx',
	dob: new Date(1976, 6, 18, 18, 18),
	loves: ['grape', 'watermelon'],
	weight: 704,
	gender: 'm',
	vampires: 165});
...
...

```

- `{field: value}` 用来查找那些 field 的值等于 value 的文档。 `{field1: value1, field2: value2}` 相当于 and 查询。
还有 `$lt, $lte, $gt, $gte 和 $ne` 被用来处理 小于，小于等于，大于，大于等于，和不等于操作。

例如，` db.unicorns.find({gender: 'm',weight: {$gt: 700}})` 或 `db.unicorns.find({gender: {$ne: 'f'},weight: {$gte: 701}}) `，表示查询大于700的male。
注意后面的否定式查询。

$exists 用来匹配字段是否存在，比如:` db.unicorns.find({vampires: {$exists: false}})`，返回一个不存在vmpires字段的文档。

'$in' 被用来匹配查询文档在我们传入的数组参数中是否存在匹配值，` db.unicorns.find({loves: {$in:['apple','orange']}})` ，喜欢apple和orange的。

- 返回那些喜欢 apples 或者 weigh 小于500磅的母独角兽。

```python
db.unicorns.find({gender: 'f',
	$or: [{loves: 'apple'},
		  {weight: {$lt: 500}}]})
```

MongoDB真是与python类似，易用功能强大。


# 3. 更新update

## 3.1 `$set `实现指定字段更新

通过 `db.unicorns.update({name: 'Roooooodles'},{weight: 590}) `更新一条记录后，然后查询`db.unicorns.find({name: 'Roooooodles'}) `，发现找不到任何文档，但是新增了下面的一条记录：

```python
{ "_id" : ObjectId("59d62dec6a18c7e711a19e6e"), "weight" : 590 }
```

变更前:

```python
{ "_id" : ObjectId("59d62dec6a18c7e711a19e6e"), "weight" : 590, "name" : "Roooooodles", "dob" : ISODate("1979-08-18T09:44:00Z"), "loves" : [ "apple" ], "gender" : "m", "vampires" : 99 }

```

这里的update与SQL中的update是完全不同的，这里通过name找到对应的文档，然后用后面的参数，替换了后面的整个文档。

如果要实现类似SQL中的update，即只更新指定的字段，比如，我们要将上面的新增的记录，更新成变更前的话，

```python
db.unicorns.update({weight: 590}, {$set: {
	name: 'Roooooodles',
	dob: new Date(1979, 7, 18, 18, 44),
	loves: ['apple'],
	gender: 'm',
	vampires: 99}})
```

所以，最开始我们的更新命令应该是:

```python
db.unicorns.update({name: 'Roooooodles'},
	{$set: {weight: 590}})
```

## 3.2 ` $inc`增加正/负值，`$push `追加值

- 变更前

```python

> db.unicorns.find({name: 'Pilot'})
{ "_id" : ObjectId("59d62dec6a18c7e711a19e74"), "name" : "Pilot", "dob" : ISODate("1997-02-28T20:03:00Z"), "loves" : [ "apple", "watermelon" ], "weight" : 650, "gender" : "m", "vampires" : 54 }


> db.unicorns.find({name: 'Aurora'})
{ "_id" : ObjectId("59d62dec6a18c7e711a19e6c"), "name" : "Aurora", "dob" : ISODate("1991-01-24T04:00:00Z"), "loves" : [ "carrot", "grape" ], "weight" : 450, "gender" : "f", "vampires" : 43 }


```

- 执行命令后

```python

# 减少2
db.unicorns.update({name: 'Pilot'},{$inc: {vampires: -2}})

> db.unicorns.find({name: 'Pilot'})
{ "_id" : ObjectId("59d62dec6a18c7e711a19e74"), "name" : "Pilot", "dob" : ISODate("1997-02-28T20:03:00Z"), "loves" : [ "apple", "watermelon" ], "weight" : 650, "gender" : "m", "vampires" : 52 }

# 新增一个sugar
db.unicorns.update({name: 'Aurora'},{$push: {loves: 'sugar'}})

> db.unicorns.find({name: 'Aurora'})
{ "_id" : ObjectId("59d62dec6a18c7e711a19e6c"), "name" : "Aurora", "dob" : ISODate("1991-01-24T04:00:00Z"), "loves" : [ "carrot", "grape", "sugar" ], "weight" : 450, "gender" : "f", "vampires" : 43 }

```

## 3.3 ` upserts`更新/新增

所谓 upsert 更新，即在文档中找到匹配值时更新它，无匹配时向文档插入新值，你可以这样理解。要使用 upsert 我们需要向 update 写入第三个参数 {upsert:true}


```python

# 普通的更新，因为本身没有文档，故find无法找到任何东西
> db.hits.update({page: 'unicorns'},{$inc: {hits: 1}});
> db.hits.find();

# 换了一种更新方式，添加了upsert，如果没有记录，则新增
> db.hits.update({page: 'unicorns'},{$inc: {hits: 1}}, {upsert:true});
> db.hits.find();
{ "_id" : ObjectId("59d63215a6f78538cda37766"), "page" : "unicorns", "hits" : 1 }

# 第二个更新的时候，基于现有的记录更新
> db.hits.update({page: 'unicorns'},{$inc: {hits: 1}}, {upsert:true});
> db.hits.find();
{ "_id" : ObjectId("59d63215a6f78538cda37766"), "page" : "unicorns", "hits" : 2 }

```

## 3.4 批量更新 `{multi:true} `

默认情况下update只更新一个文档，比如执行

```python
> db.unicorns.update({},{$set: {vaccinated: true }});
> db.unicorns.find({vaccinated: true});
```

只有第一条被更新了，如果要对所有文档都更新的话，需要将multi选项设置为true:

```python
> db.unicorns.update({},{$set: {vaccinated: true }},{multi:true});
> db.unicorns.find({vaccinated: true});

```

# 4. 掌握查询

find 返回的结果是一个 cursor。

## 4.1 字段选择

```python
# 查询结果只保留name字段
db.unicorns.find({}, {name: 1});

# id字段是默认返回的，如果不需要，要显式指定
db.unicorns.find({}, {name:1, _id: 0});
```

## 4.2 排序

-1 表示降序，1表示升序排序。

```python
//heaviest unicorns first
db.unicorns.find().sort({weight: -1})

//by unicorn name then vampire kills:
db.unicorns.find().sort({name: 1,
	vampires: -1})
```

## 4.3 分页

对结果分页可以通过 limit 和 skip 游标方法来实现。比如要获取第二和第三重的独角兽，我们可以这样:

```python
db.unicorns.find()
	.sort({weight: -1})
	.limit(2)
	.skip(1)
```

## 4.4 计数

```python

db.unicorns.count({vampires: {$gt: 50}})

db.unicorns.find({vampires: {$gt: 50}}).count()

```


# 5. 数据建模
未完待续...