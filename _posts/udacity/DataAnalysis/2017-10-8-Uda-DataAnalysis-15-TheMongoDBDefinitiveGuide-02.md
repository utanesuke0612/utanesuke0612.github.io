---
layout: post
title: Uda-DataAnalysis-15-[扩展]-MongoDB权威指南(2)-查询
date: 2017-10-8 01:00:00
categories: 数据分析
tags: MongoDB DataAnalysis 
---
* content
{:toc}

> Udacity课程中涉及到MongoDB的知识，视频中讲得太概略，自己不做扩展的话，根据理解不了。
> 即使能模仿着完成练习，但是换个场景估计又不明白了。为了知其然更知其所以然，在进入后面的课程前，将这本书实践一遍。
> <<MongDB权威指南>> 书是2011年的，但是NoSQL的基本概念应该是不变的，看本书的目的是理解基本，后面高级的概念在工作中再去看官方文档扩展。
> 


# 1. find简介

- db.c.find()返回集合c中的所有内容

```python
> show dbs
admin     0.000GB
examples  0.001GB
local     0.000GB
mydb      0.044GB
test      0.000GB

> use mydb
switched to db mydb
> db.getCollectionNames()
[ "auto", "cities", "employees", "twitter", "unicorns" ]
> db.auto.find()
```

- 指定条件进行查询

```python
> db.auto.find({"name":"Porsche 924"}).limit(5).pretty()
```

- 指定返回的键
有时并不需要所有数据，如果指定返回键的话，既能节省传输的数据量，又能节省解码时间和内存消耗。

```python
# find前面的{}指不限定条件查询
> db.auto.find({},{"name":1,"width":1,"weight":1}).limit(2).pretty()

```

输出 

```python
{
        "_id" : ObjectId("59d64118a6f78538cda37c6a"),
        "weight" : 2721000000,
        "width" : 34.7472,
        "name" : "Crawler-transporter"
}
{
        "_id" : ObjectId("59d64118a6f78538cda37c6b"),
        "weight" : 908107,
        "width" : 1.778,
        "name" : "Ford GT40"
}
```

如果不需要输出id的话，需要显式指定，否则默认输出：

```python
> db.auto.find({},{"name":1,"width":1,"weight":1,"_id":0}).limit(2).pretty()
```


# 2. 查询条件

## 2.1 简单条件
`$lt,$lte,$gt,$gte` 就是全部的比较操作符，分别是`小于，小于等于，大于，大于等于 `。
比如下面查找宽度在1.5和2之间的车。

```python
> db.auto.find({"width":{"$lt":2,"$gt":1.5}},{"name":1,"productionStartYear":1,"width":1,"_id":0}).limit(5).pretty()

# 以下是输出:
{
        "productionStartYear" : "1964-01-01T00:00:00+02:00",
        "width" : 1.778,
        "name" : "Ford GT40"
}
{
        "productionStartYear" : "1977-01-01T00:00:00+02:00",
        "width" : 1.89,
        "name" : "Porsche 928"
}
{
        "productionStartYear" : "1976-01-01T00:00:00+02:00",
        "width" : 1.685,
        "name" : "Porsche 924"
}
{
        "productionStartYear" : "1982-01-01T00:00:00+02:00",
        "width" : 1.73482,
        "name" : "Porsche 944"
}
{
        "productionStartYear" : "1992-01-01T00:00:00+02:00",
        "width" : 1.73482,
        "name" : "Porsche 968"
}
```

如果要在上面的基础上查找1980年以后生成的汽车呢:

```python

> start = new Date("01/01/1980")
ISODate("1979-12-31T15:00:00Z")

> db.auto.find({"width":{"$lt":2,"$gt":1.5},"productionStartYear":{"$gte":start}},{"name":1,"productionStartYear":1,"width":1,"_id":0}).limit(5).pretty()

```


- `$ne`表示不相等

```python
> db.auto.find({"name":{"$ne":"Porsche 968"}},{"name":1,"productionStartYear":1,"width":1,"_id":0}).limit(5).pretty()
```

## 2.2 OR查询

- `$in $nin`分别表示存在于/不存在于某个list。

```python
> db.users.find({"age":{"$in":[2,4]}}).pretty()
{ "_id" : ObjectId("59d9e558c7399f16feebefe1"), "name" : "uta", "age" : 4 }
{
        "_id" : ObjectId("59d9e55ec7399f16feebefe2"),
        "name" : "utasuke",
        "age" : 2
}
> db.users.find({"age":{"$nin":[2,4]}}).pretty()
```

- `$or`用来表示对查询条件做or操作，下面的意思是name为wal，或是年龄小于5岁

```python
> db.users.find({"$or":[{"name":"wal"},{"age":{"$lt":5}}]}).pretty()
{ "_id" : ObjectId("59d9b6155881a5de879a28f9"), "name" : "wal", "age" : 16 }
{ "_id" : ObjectId("59d9e558c7399f16feebefe1"), "name" : "uta", "age" : 4 }
{
        "_id" : ObjectId("59d9e55ec7399f16feebefe2"),
        "name" : "utasuke",
        "age" : 2
}
```

与之相反的是，`$and`是完全满足条件。

```python
> db.users.find({"$and":[{"name":"uta"},{"age":{"$lt":5}}]}).pretty()
{ "_id" : ObjectId("59d9e558c7399f16feebefe1"), "name" : "uta", "age" : 4 }
```


## 2.3 `$not` 是元条件句，可以用在任何其他条件上。


```python
> db.users.find({"age":{"$gt":4}},{"name":1,"age":1,"_id":0}).pretty()
{ "name" : "ljun", "age" : 16 }
{ "name" : "wal", "age" : 16 }

# 对上面的条件取反
> db.users.find({"age":{"$not":{"$gt":4}}},{"name":1,"age":1,"_id":0}).pretty()
{ "name" : "uta", "age" : 4 }
{ "name" : "utasuke", "age" : 2 }
```


# 3. 特定于类型的查询

## 3.1 null查询
- 通过null查询出特定键为null，或是不存在该键的文档。如下:

```python
> db.users.find({"comments":null}).pretty()
{ "_id" : ObjectId("59d9b6155881a5de879a28f9"), "name" : "wal", "age" : 16 }
{ "_id" : ObjectId("59d9e558c7399f16feebefe1"), "name" : "uta", "age" : 4 }
{
        "_id" : ObjectId("59d9e55ec7399f16feebefe2"),
        "name" : "utasuke",
        "age" : 2
}
{
        "_id" : ObjectId("59d9e9c0c7399f16feebefe3"),
        "name" : "x1",
        "age" : null,
        "comments" : null
}
```

- 如果要找出有comments键，但是为null的话，通过如下方式:

```python
> db.users.find({"comments":{"$in":[null],"$exists":true}}).pretty()
{
        "_id" : ObjectId("59d9e9c0c7399f16feebefe3"),
        "name" : "x1",
        "age" : null,
        "comments" : null
}
>
```

## 3.2 正则表达式

关于正则表达式的详细操作，参考官方文档。

```python
> db.users.find({"name":/uta*/i})
{ "_id" : ObjectId("59d9e558c7399f16feebefe1"), "name" : "uta", "age" : 4 }
{ "_id" : ObjectId("59d9e55ec7399f16feebefe2"), "name" : "utasuke", "age" : 2 }
```


## 3.3 查询数组

- 先准备数组数据:

```python
> db.users.update({"name":"uta"},{"$push":{"love":"sugar"}})
> db.users.update({"name":"uta"},{"$push":{"love":"cake"}})
> db.users.update({"name":"uta"},{"$push":{"love":"ice"}})
> db.users.update({"name":"uta"},{"$push":{"love":"apple"}})
> db.users.update({"name":"uta"},{"$push":{"love":"java"}})

> db.users.find({"name":"uta"}).pretty()
{
        "_id" : ObjectId("59d9e558c7399f16feebefe1"),
        "name" : "uta",
        "age" : 4,
        "love" : [
                "sugar",
                "cake",
                "ice",
                "apple",
                "java"
        ]
}
```

###3.3.1 `$all` 查询既喜欢`ice`又有`java`的文档。

```python
> db.users.find({"love":{"$all":["ice","java"]}}).pretty()
{
        "_id" : ObjectId("59d9e558c7399f16feebefe1"),
        "name" : "uta",
        "age" : 4,
        "love" : [
                "sugar",
                "cake",
                "ice",
                "apple",
                "java"
        ]
}
```

###3.3.2  `$size` 用来查询数组长度，查询love中包含两个的文档

```python
> db.users.find({"love":{"$size":2}}).pretty()
{
        "_id" : ObjectId("59d9ed11c7399f16feebefe4"),
        "name" : "lj",
        "age" : 18,
        "love" : [
                "python",
                "java"
        ]
}

```

但是$size不能与比较运算符并用，比如下面会显示错误 ` db.users.find({"love":{"$size":{"$gt":2}}}).pretty()`



###3.3.3  常见的替代方法是:


```python
> db.users.update({"name":"utasuke"},{"$push":{"love":"sugar"},"$inc":{"size":1}})
> db.users.update({"name":"utasuke"},{"$push":{"love":"pie"},"$inc":{"size":1}})
> db.users.update({"name":"utasuke"},{"$push":{"love":"banana"},"$inc":{"size":1}})

> db.users.find({"size":{"$gt":2}}).pretty()

# 输出
{
        "_id" : ObjectId("59d9e55ec7399f16feebefe2"),
        "name" : "utasuke",
        "age" : 2,
        "love" : [
                "sugar",
                "pie",
                "banana"
        ],
        "size" : 3
}
>
```

###3.3.4 `$slice` 切片

```python
{
        "_id" : ObjectId("59d9e558c7399f16feebefe1"),
        "name" : "uta",
        "age" : 4,
        "love" : [
                "sugar",
                "cake",
                "ice",
                "apple",
                "java"
        ]
}

# 查询最后两个
> db.users.find({"name":"uta"},{"love":{"$slice":-2}}).pretty()
{
        "_id" : ObjectId("59d9e558c7399f16feebefe1"),
        "name" : "uta",
        "age" : 4,
        "love" : [
                "apple",
                "java"
        ]
}

# 第二个和第三个
> db.users.find({"name":"uta"},{"love":{"$slice":[1,2]}}).pretty()
{
        "_id" : ObjectId("59d9e558c7399f16feebefe1"),
        "name" : "uta",
        "age" : 4,
        "love" : [
                "cake",
                "ice"
        ]
}

# 查询最后一个
> db.users.find({"name":"uta"},{"love":{"$slice":-1}}).pretty()
{
        "_id" : ObjectId("59d9e558c7399f16feebefe1"),
        "name" : "uta",
        "age" : 4,
        "love" : [
                "java"
        ]
}
```

## 3.4 查询内嵌文档

通过类似 `name.first`的形式指定内嵌文档的键。


# 4. 游标

数据库使用游标来返回find的执行结果

```python
> var cursor = db.users.find()

> d = cursor.next()
{ "_id" : ObjectId("59d9b6155881a5de879a28f9"), "name" : "wal", "age" : 16 }
```

通常在python中通过for循环可以取出迭代对象的元素。


```python
    autos = db.autos.find({"manufacturer":"Toyota"})
    for a in autos:
        pprint.pprint(a)
```

## 4.1 `limit`,`skip`，`sort`

```python

# 只取前两个
> db.users.find().limit(2)

# 跳过前两个，取后面的
> db.users.find().skip(2)

# age降序，name升序排列
> db.users.find().sort({"age":-1,"name":1})

```

下面是个实际例子，比如，有个在线商店，搜索mp3，每页50个结果，按价格从大到小排列


```python
> db.stock.find({"desc":"mp3"}).limit(50).sort({"price":-1})

# 点击下一页，只需要略过前50个即可
> db.stock.find({"desc":"mp3"}).limit(50).skip(50)sort({"price":-1})

```

但是skip会影响性能，尽量少用。

## 4.2 避免使用skip略过大量结果

- 使用skip进行分页:

```python
var page1 = db.foo.find().limit(100)
var page2 = db.foo.find().skip(100).limit(100)
var page3 = db.foo.find().skip(200).limit(100)

```

- 替代方式:
按照date排序，第二页取大于date的值继续查询

```python

page1 = db.foo.find().sort({"date":-1}).limit(100)

var latest = null

# first page
while (page1.hasNext()){
	latest = page1.next()
	display(latest)
}

var page2 = db.foo.find({"$date":{"$gt":latest.date}})

page2.sort({"date":-1}).limit(100)

```

## 4.3 随机选取文档

最笨的方法就是获取文档总数，然后再这总数之间生成随机数，但这么做事非常低效的。

```python
var total = db.foo.count()
var random = Math.floor(Math.random()*total)
db.foo.find().skip(random).limit(1)
```

替代方式是，再每次添加文档的时候，添加一个随机数键

```python
db.people.insert({"name":"ljun","random":Math.random})
db.people.insert({"name":"wangling","random":Math.random})

var random = Math.random()
result = db.foo.findOne({"random":{"$gt":random}})

if (result == null):
	result = db.foo.findOne({"random":{"$lt":random}})
```


