---
layout: post
title: Uda-DataAnalysis-15-[扩展]-MongoDB权威指南(3)-聚合
date: 2017-10-8 02:00:00
categories: 数据分析
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

> Udacity课程中涉及到MongoDB的知识，视频中讲得太概略，自己不做扩展的话，根据理解不了。
> 即使能模仿着完成练习，但是换个场景估计又不明白了。为了知其然更知其所以然，在进入后面的课程前，将这本书实践一遍。
> <<MongDB权威指南>> 书是2011年的，但是NoSQL的基本概念应该是不变的，看本书的目的是理解基本，后面高级的概念在工作中再去看官方文档扩展。

> 聚合这一部分，讲得并不多，还是学习官方文档靠谱。

# 1. count

最简单的聚合工具，返回文档数量，也可以在find内指定条件

```python
> db.users.find().count()
5
> db.users.count()
5
```


# 2. distinct 

```python
> db.runCommand({"distinct":"users","key":"age"})
{ "values" : [ 16, 4, 2, null, 18 ], "ok" : 1 }
>
```

# 3. group

## 3.1  准备实验数据

```python
> var time1 = new Date(01/01/2010)
> var time2 = new Date(01/02/2010)
> var time3 = new Date(01/03/2010)
> var time4 = new Date(01/04/2010)
> var time5 = new Date(01/03/2010)
> var time6 = new Date(01/02/2010)

> x1 = {"day":"2010/01/01","time":time1,"price":4.05}
> x2 = {"day":"2010/01/02","time":time2,"price":4.05}
> x3 = {"day":"2010/01/03","time":time3,"price":4.18}
> x4 = {"day":"2010/01/04","time":time4,"price":4.228}
> x5 = {"day":"2010/01/03","time":time5,"price":4.228}
> x6 = {"day":"2010/01/02","time":time6,"price":4.98}

> db.stocks.insert(x1)
> db.stocks.insert(x2)
> db.stocks.insert(x1)
> db.stocks.insert(x3)
> db.stocks.insert(x4)
> db.stocks.insert(x5)
> db.stocks.insert(x6)
> 

> db.stocks.find()
{ "_id" : ObjectId("59da0d7ac7399f16feebefe5"), "day" : "2010/01/01", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.05 }
{ "_id" : ObjectId("59da0d7cc7399f16feebefe6"), "day" : "2010/01/02", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.05 }
{ "_id" : ObjectId("59da0d7fc7399f16feebefe7"), "day" : "2010/01/01", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.05 }
{ "_id" : ObjectId("59da0d83c7399f16feebefe8"), "day" : "2010/01/03", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.18 }
{ "_id" : ObjectId("59da0d85c7399f16feebefe9"), "day" : "2010/01/04", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.228 }
{ "_id" : ObjectId("59da0d88c7399f16feebefea"), "day" : "2010/01/03", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.228 }
{ "_id" : ObjectId("59da0d8ac7399f16feebefeb"), "day" : "2010/01/02", "time" : ISODate("1970-01-01T00:00:00Z"), "price" : 4.98 }
>
```

## 3.2  group 按天进行分组，然后再每一组里取包含最新时间搓的文档


```python
> db.runCommand({"group":{
> 	"ns":"stocks",
> 	"key":"day",
> 	"initial":{"time":0},
> 	"$reduce":function(doc,prev) { 
> 		if (doc.time > prev.time){ 
> 			prev.price = doc.price;
> 			prev.time = doc.time
> 			}
> 		}
> 	}
> })
```

1. `ns`表示要分组的集合
2. `key`指文档分组要依据的键
3. `initial` 每一组reduce函数调用的初始时间，会作为初始文档传递给后续过程。


另外，如果是只处理2010年以后的，可以添加条件：

```python
```python
> db.runCommand({"group":{
> 	"ns":"stocks",
> 	"key":"day",
> 	"initial":{"time":0},
> 	"$reduce":function(doc,prev) { 
> 		if (doc.time > prev.time){ 
> 			prev.price = doc.price;
> 			prev.time = doc.time
> 			}
> 		},
> 	"condition":{"day":{"$gt":"2010/01/01"}}}
> })
```


