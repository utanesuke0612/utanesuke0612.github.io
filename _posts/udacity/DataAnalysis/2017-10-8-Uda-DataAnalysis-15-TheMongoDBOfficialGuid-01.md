---
layout: post
title: Uda-DataAnalysis-15-[扩展]-MongoDB官方文档-聚合
date: 2017-10-8 03:00:00
categories: Uda-数据分析进阶
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

> 参考[官方文档-aggregation](https://docs.mongodb.com/manual/aggregation/)
> 和 [http://www.runoob.com ](http://www.runoob.com/mongodb/mongodb-aggregate.html)
> 

# 1. aggregate() 方法

MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等),并返回计算后的数据结果。有点类似sql语句中的 count(*)。


- 示例数据：

```python
> db.mycol.find().pretty()
{
        "_id" : ObjectId("59da23e8c7399f16feebefec"),
        "title" : "MongoDB Overview",
        "description" : "MongoDB is no sql database",
        "by_user" : "runoob.com",
        "url" : "http://www.runoob.com",
        "tags" : [
                "mongodb",
                "database",
                "NoSQL"
        ],
        "likes" : 100
}
{
        "_id" : ObjectId("59da23eac7399f16feebefed"),
        "title" : "NoSQL Overview",
        "description" : "No sql database is very fast",
        "by_user" : "runoob.com",
        "url" : "http://www.runoob.com",
        "tags" : [
                "mongodb",
                "database",
                "NoSQL"
        ],
        "likes" : 10
}
{
        "_id" : ObjectId("59da23ecc7399f16feebefee"),
        "title" : "Neo4j Overview",
        "description" : "Neo4j is no sql database",
        "by_user" : "Neo4j",
        "url" : "http://www.neo4j.com",
        "tags" : [
                "neo4j",
                "database",
                "NoSQL"
        ],
        "likes" : 750
}

```

- 代码示例
 
```python

# 计算每个作者所写的文章数
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}])
{ "_id" : "Neo4j", "num_tutorial" : 1 }
{ "_id" : "runoob.com", "num_tutorial" : 2 }

# 计算每个作者得到的like数目
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])
{ "_id" : "Neo4j", "num_tutorial" : 750 }
{ "_id" : "runoob.com", "num_tutorial" : 110 }

# 计算作者，一篇文章平均得到的like数
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}])
{ "_id" : "Neo4j", "num_tutorial" : 750 }
{ "_id" : "runoob.com", "num_tutorial" : 55 }

# 计算作者，一篇文章中最少的like数
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}])
{ "_id" : "Neo4j", "num_tutorial" : 750 }
{ "_id" : "runoob.com", "num_tutorial" : 10 }
>

# 计算作者，一篇文章中最多的like数
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}])
{ "_id" : "Neo4j", "num_tutorial" : 750 }
{ "_id" : "runoob.com", "num_tutorial" : 100 }
>

# 以user分组，将该user中对应的url放入数组
> db.mycol.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}])
{ "_id" : "Neo4j", "url" : [ "http://www.neo4j.com" ] }
{ "_id" : "runoob.com", "url" : [ "http://www.runoob.com", "http://www.runoob.com" ] }


# 类似上面，但是是放入set，即不重复放
> db.mycol.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}])
{ "_id" : "Neo4j", "url" : [ "http://www.neo4j.com" ] }
{ "_id" : "runoob.com", "url" : [ "http://www.runoob.com" ] }

# 按user分组，每个分组中的第一个文档的对应field
> db.mycol.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}])
{ "_id" : "Neo4j", "first_url" : "http://www.neo4j.com" }
{ "_id" : "runoob.com", "first_url" : "http://www.runoob.com" }
>

# 按user分组，每个分组中的最后一个文档的对应field
> db.mycol.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}])
{ "_id" : "Neo4j", "last_url" : "http://www.neo4j.com" }
{ "_id" : "runoob.com", "last_url" : "http://www.runoob.com" }

```

# 2. 管道的概念

MongoDB的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的。

- $project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
- $match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
- $limit：用来限制MongoDB聚合管道返回的文档数。
- $skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
- $unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
- $group：将集合中的文档分组，可用于统计结果。
- $sort：将输入文档排序后输出。
- $geoNear：输出接近某一地理位置的有序文档。


通过project选取输出field，默认会输出id，_id:0 指定后不输出

```python
> db.mycol.aggregate(
...     { $project : {
...         title : 1 
...     }}
...  );
# 输出
{ "_id" : ObjectId("59da23e8c7399f16feebefec"), "title" : "MongoDB Overview" }
{ "_id" : ObjectId("59da23eac7399f16feebefed"), "title" : "NoSQL Overview" }
{ "_id" : ObjectId("59da23ecc7399f16feebefee"), "title" : "Neo4j Overview" }

```


通过match过滤数据，并输出到下一个管道group中。

```python
> db.mycol.aggregate( [
...                         { $match : { likes : { $gt : 5, $lte : 200 } } },
...                         { $group: { _id: null, count: { $sum: 1 } } }
...                        ] );

# 输出
{ "_id" : null, "count" : 2 }
```


通过skip过过滤前面两个文档：

```python
> db.mycol.aggregate(     { $skip : 2 });
```

如下图中，原始文档是第一个管道，经过$match处理进入下一个管道，再次经过$group处理后，作为结果输出：

![image](https://user-images.githubusercontent.com/18595935/31317423-df2be79c-ac7b-11e7-9946-44a60449b5a3.png)


# 3. 示例:处理ZipCode数据

- 导入zips.json文件

```python
C:\Users\utane\OneDrive\udacity\99-the other\01-MongoDB>mongoimport -d examples -c zips --file zips.json
2017-10-08T23:05:20.522+0900    connected to: localhost
2017-10-08T23:05:20.894+0900    imported 29353 documents

```

- 然后切换到新的db中

```python
> use examples
switched to db examples
> db.getCollectionNames()
[
        "zips"
]

> db.zips.find().limit(1).pretty()
{
        "_id" : "01012",
        "city" : "CHESTERFIELD",
        "loc" : [
                -72.833309,
                42.38167
        ],
        "pop" : 177,
        "state" : "MA"
}
>
```

## 3.1 `$group` -> `$match`

通过state分组，并输出每个state的人口总数，最后输出人口总数大于1千万的state。

```python
db.zips.aggregate([
	{$group:{_id:"$state",totalPop:{$sum:"$pop"}}},
	{$match:{totalPop:{$gte:10*1000*1000}}}
	])

# 输出如下:
{ "_id" : "IL", "totalPop" : 11427576 }
{ "_id" : "OH", "totalPop" : 10846517 }
{ "_id" : "FL", "totalPop" : 12686644 }
{ "_id" : "NY", "totalPop" : 17990402 }
{ "_id" : "PA", "totalPop" : 11881643 }
{ "_id" : "TX", "totalPop" : 16984601 }
{ "_id" : "CA", "totalPop" : 29754890 }
```

上面的语句有两个阶段:
1. group处理后，两个field，分别为state的值，以及计算的各个state的人口总数和totalPop
2. match，接收上一个阶段的数据，过滤totalPop在1千万的州。

如果用SQL语句处理的话：

```python
SELECT state, SUM(pop) AS totalPop
FROM zipcodes
GROUP BY state
HAVING totalPop >= (10*1000*1000)
```


## 3.2 `$group` -> `$group`


```python
db.zips.aggregate( [
   { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },
   { $group: { _id: "$_id.state", avgCityPop: { $avg: "$pop" } } }
] )
```

输出如下:

```python
{ "_id" : "NH", "avgCityPop" : 5232.320754716981 }
{ "_id" : "MA", "avgCityPop" : 14855.37037037037 }
{ "_id" : "ME", "avgCityPop" : 3006.4901960784314 }
{ "_id" : "NY", "avgCityPop" : 13131.680291970803 }
{ "_id" : "VT", "avgCityPop" : 2315.8765432098767 }
{ "_id" : "PA", "avgCityPop" : 8679.067202337472 }
{ "_id" : "DE", "avgCityPop" : 14481.91304347826 }
{ "_id" : "DC", "avgCityPop" : 303450 }
{ "_id" : "VA", "avgCityPop" : 8526.177931034483 }
{ "_id" : "SC", "avgCityPop" : 11139.626198083068 }
{ "_id" : "FL", "avgCityPop" : 27400.958963282937 }
{ "_id" : "AL", "avgCityPop" : 7907.2152641878665 }
{ "_id" : "NJ", "avgCityPop" : 15775.89387755102 }
...
```

上面也分成两个阶段:
- 第一个group，先按state和city分组，计算每个组即每个city的人口总数。

如果没有第二个group的话，输出如下：

```python

> db.zips.aggregate( [
...    { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } }
... ] )
{ "_id" : { "state" : "AK", "city" : "HYDER" }, "pop" : 116 }
{ "_id" : { "state" : "AK", "city" : "THORNE BAY" }, "pop" : 744 }
{ "_id" : { "state" : "AK", "city" : "SKAGWAY" }, "pop" : 692 }
{ "_id" : { "state" : "AK", "city" : "SITKA" }, "pop" : 8638 }
{ "_id" : { "state" : "AK", "city" : "HOONAH" }, "pop" : 1670 }
...

```


- 第二个group，接收上一个stage的输出，即state,city和pop，再按照state分组，计算每个state内的人口平均数。

如果将avg修改为sum，则与上面3.1的结果一样，当然也没有必要分两个stage计算。

```python
> db.zips.aggregate( [    { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },    { $group: { _id: "$_id.state", sumCityPop: { $sum: "$pop" } } } ] )
> 
{ "_id" : "IL", "sumCityPop" : 11427576 }
{ "_id" : "MO", "sumCityPop" : 5110648 }
{ "_id" : "KS", "sumCityPop" : 2475285 }

```


## 3.3 `【重要】`返回每个州内人口最多和最少的city:


```python

> db.zips.aggregate( [
...    { $group:
...       {
...         _id: { state: "$state", city: "$city" },
...         pop: { $sum: "$pop" }
...       }
...    },
...    { $sort: { pop: 1 } },
...    { $group:
...       {
...         _id : "$_id.state",
...         biggestCity:  { $last: "$_id.city" },
...         biggestPop:   { $last: "$pop" },
...         smallestCity: { $first: "$_id.city" },
...         smallestPop:  { $first: "$pop" }
...       }
...    },
...   { $project:
...     { _id: 0,
...       state: "$_id",
...       biggestCity:  { name: "$biggestCity",  pop: "$biggestPop" },
...       smallestCity: { name: "$smallestCity", pop: "$smallestPop" }
...     }
...   }
... ] )

```

输出为:

```python
{ "biggestCity" : { "name" : "NEWARK", "pop" : 111674 }, "smallestCity" : { "name" : "BETHEL", "pop" : 108 }, "state" : "DE" }
{ "biggestCity" : { "name" : "SAINT LOUIS", "pop" : 397802 }, "smallestCity" : { "name" : "BENDAVIS", "pop" : 44 }, "state" : "MO" }
```


上面分成四个阶段:

- 第一个group，按state和city分组，计算每个组的人口总数，并输出三个field，类似如下:

```python
{ "_id" : { "state" : "AK", "city" : "HYDER" }, "pop" : 116 }
```

- 第二个阶段sort，按照city的人口数目升序排列

- 第三个阶段，基于上面排序后的文档，按照state分组，输出每个state的最大最小人口数的city和人口数。

- 第四个阶段，是基于第三个阶段的数据，对输出结果进行一个整形，即重新排列。
如果没有最后一个project的整形阶段，输出为如下，可以与上面进行对比：

```python
{ "_id" : "DE", "biggestCity" : "NEWARK", "biggestPop" : 111674, "smallestCity" : "BETHEL", "smallestPop" : 108 }
{ "_id" : "MO", "biggestCity" : "SAINT LOUIS", "biggestPop" : 397802, "smallestCity" : "BENDAVIS", "smallestPop" : 44 }
```


# 4. 示例2：处理用户喜好数据集

- 准备数据

```python
> db.club.insert(x1)
WriteResult({ "nInserted" : 1 })
> db.club.insert(x2)
WriteResult({ "nInserted" : 1 })
> db.club.insert(x3)
WriteResult({ "nInserted" : 1 })
> db.club.insert(x4)
WriteResult({ "nInserted" : 1 })
> db.club.insert(x5)
WriteResult({ "nInserted" : 1 })
> db.club.insert(x6)
WriteResult({ "nInserted" : 1 })
> db.club.find().pretty()
{
        "_id" : "jane",
        "joined" : ISODate("2011-03-02T00:00:00Z"),
        "likes" : [
                "golf",
                "tennis"
        ]
}
{
        "_id" : "lijun",
        "joined" : ISODate("2012-07-02T00:00:00Z"),
        "likes" : [
                "tennis",
                "golf",
                "swimming"
        ]
}
{
        "_id" : "jane2",
        "joined" : ISODate("2011-01-02T00:00:00Z"),
        "likes" : [
                "golf",
                "runing"
        ]
}
{
        "_id" : "joe3",
        "joined" : ISODate("2012-01-02T00:00:00Z"),
        "likes" : [
                "tennis",
                "golf",
                "swimming"
        ]
}
{
        "_id" : "jane4",
        "joined" : ISODate("2011-03-02T00:00:00Z"),
        "likes" : [
                "golf",
                "pingpong"
        ]
}
{
        "_id" : "joe5",
        "joined" : ISODate("2012-01-02T00:00:00Z"),
        "likes" : [
                "tennis",
                "golf",
                "swimming"
        ]
}
>
```

## 4.1 数据规范化/排序

将name先全部大写，然后升序排列。

```python
db.club.aggregate(
  [
    { $project : { name:{$toUpper:"$_id"} , _id:0 } },
    { $sort : { name : 1 } }
  ]
)

# 输出

{ "name" : "JANE" }
{ "name" : "JANE2" }
{ "name" : "JANE4" }
{ "name" : "JOE3" }
{ "name" : "JOE5" }
{ "name" : "LIJUN" }

```

## 4.2 根据用户加入的月份排序

```python
db.club.aggregate(
  [
    { $project :
       {
         month_joined : { $month : "$joined" },
         name : "$_id",
         _id : 0
       }
    },
    { $sort : { month_joined : 1 } }
  ]
)
```

输出如下：

```python
{ "month_joined" : 1, "name" : "jane2" }
{ "month_joined" : 1, "name" : "joe3" }
{ "month_joined" : 1, "name" : "joe5" }
{ "month_joined" : 3, "name" : "jane" }
{ "month_joined" : 3, "name" : "jane4" }
{ "month_joined" : 7, "name" : "lijun" }
```

## 4.3 返回每个月的总加入人数:


```python
db.club.aggregate(
  [
    { $project : { month_joined : { $month : "$joined" } } } ,
    { $group : { _id : {month_joined:"$month_joined"} , number : { $sum : 1 } } },
    { $sort : { "_id.month_joined" : 1 } }
  ]
)
```

输出如下:

```python
{ "_id" : { "month_joined" : 1 }, "number" : 3 }
{ "_id" : { "month_joined" : 3 }, "number" : 2 }
{ "_id" : { "month_joined" : 7 }, "number" : 1 }
```

## 4.4 返回最喜欢的3种运动

```python
db.club.aggregate(
  [
    { $unwind : "$likes" },
    { $group : { _id : "$likes" , number : { $sum : 1 } } },
    { $sort : { number : -1 } },
    { $limit : 3 }
  ]
)
```

输出如下

```python
{ "_id" : "golf", "number" : 6 }
{ "_id" : "tennis", "number" : 4 }
{ "_id" : "swimming", "number" : 3 }
```

上面分成四个阶段:

1. unwind第一阶段,将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值，以及除了该数组以外的所有值。

这个阶段的输出如下结构:

```python
> db.club.aggregate(
...   [
...     { $unwind : "$likes" }
...   ]
... )
{ "_id" : "jane", "joined" : ISODate("2011-03-02T00:00:00Z"), "likes" : "golf" }
{ "_id" : "jane", "joined" : ISODate("2011-03-02T00:00:00Z"), "likes" : "tennis" }
{ "_id" : "lijun", "joined" : ISODate("2012-07-02T00:00:00Z"), "likes" : "tennis" }
{ "_id" : "lijun", "joined" : ISODate("2012-07-02T00:00:00Z"), "likes" : "golf" }
{ "_id" : "lijun", "joined" : ISODate("2012-07-02T00:00:00Z"), "likes" : "swimming" }
{ "_id" : "jane2", "joined" : ISODate("2011-01-02T00:00:00Z"), "likes" : "golf" }
...
```


2. group,针对上面被打散后的文档进行分组，按照likes进行分组，分组后统计文档的条数。

3. sort，接收上一个阶段的number，按降序排列。

4. limit，限定输出前三名。




