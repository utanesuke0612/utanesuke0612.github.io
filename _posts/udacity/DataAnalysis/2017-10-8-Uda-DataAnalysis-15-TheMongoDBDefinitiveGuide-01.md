---
layout: post
title: Uda-DataAnalysis-15-[扩展]-MongoDB权威指南(1)-创建更新删除
date: 2017-10-8 00:00:00
categories: Uda-数据分析进阶
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

> Udacity课程中涉及到MongoDB的知识，视频中讲得太概略，自己不做扩展的话，根据理解不了。
> 即使能模仿着完成练习，但是换个场景估计又不明白了。为了知其然更知其所以然，在进入后面的课程前，将这本书实践一遍。
> <<MongDB权威指南>> 书是2011年的，但是NoSQL的基本概念应该是不变的，看本书的目的是理解基本，后面高级的概念在工作中再去看官方文档扩展。
> 
>  


# 1. 入门
MongoDB基本概念:
1. 文档是MongoDB的数据基本单元，类似传统数据库的行，但是其结构比行复杂得多。
2. 类似，集合可以被看做是没有模式的表。
3. 一个MongoDB实例可以容纳多个独立的数据库，每个都有自己的集合和权限。
4. 每个文档，都有一个特殊的键"_id"，它在文档所处的集合中时唯一的，一般自动生成。


## 1.1 文档

多个key和关联的value有序的放置就是文档，没有固定的结构，类似于python中的字典，但是是有序的。

文档与传统数据库类似:
1. 区分数据类型
2. 区分字符串大小写
3. 不能有重复的key，与一个字典中的key概念一样，不能重复。

## 1.2 集合

集合就是一组文档，类似于传统数据库中的表。最大的特点就是无模式，即组成一个集合的文档与文档之间，可以有不同的数据类型，不同的key，例如下面的两个文档能够存在于一个集合中。

```python
{"greeting":"hello"}

{"foo":5}
```

## 1.3 数据库

类似上面，多个集合可以组成数据库，数据库的命名应该是全部小写，不要有特殊字符，如` . $ \0 空格` 等。

数据库名最终会变成文件系统中的文件。

如下是三个系统数据库:
1. admin，这个是root数据库，用于管理用户，以及运行一些特定的服务器端命令。
2. local，存储限于本地单台服务器的任意集合。
3. config，保存分片的相关信息。

把数据库名字放在集合前面，得到的是集合的完全限定名，成为命名空间，比如blog.post集合，如果存在于cms数据库中，集合的命名空间就是 cms.blog.post。

## 1.4 MongoDB shell

通过` c:\mongodb\bin\mongod --config c:\mongodb\bin\mongodb.config`命令启动MongoDB服务器端，` mongo.exe`是MongoDB的shell，用于交互式执行命令。

MongoDB shell是一个JavaScript解释器，可以运行JavaScript脚本，比如:

```python
> x = 200
200
> x / 5
40
> Math.sin(Math.PI / 2)
1
```

甚至能定义和调用JavaScript函数。

- MongoDB客户端

shell的真正威力在于它是一个独立的MongoDB客户端，开启的时候会自动连接到MongoDB的test数据库，并将数据库连接赋值给全局变量db。

```python
> show dbs
admin     0.000GB
local     0.000GB
mydb      0.044GB
test      0.000GB
> db
test
> use mydb 
> db
mydb
```

- shell基本操作-创建/读取

inset将文档插入对应的集合,追忆新增了一个` _id`字段:

```python
> post = {"title":"My blog post",}
{ "title" : "My blog post" }

# 插入文档
> db.blog.insert(post)
WriteResult({ "nInserted" : 1 })

# 查找
> db.blog.find()
{ "_id" : ObjectId("59d97dd312f96353a8fe2f32"), "title" : "My blog post" }
```


- shell基本操作-更新/删除


```python

# 给文档添加field，类似于字典的操作
> post.comment = {'rank':"excellent"}
{ "rank" : "excellent" }

# 更新文档
> db.blog.update({title:"My blog post"},post)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

# 文档被更新
> db.blog.find()
{ "_id" : ObjectId("59d97dd312f96353a8fe2f32"), "title" : "My blog post", "comment" : { "rank" : "excellent" } }

# 删除对应文档，不指定条件的话，删除blog集合中的所有文档
> db.blog.remove({title:"My blog post"})

```

- shell使用敲门

```python
> db.help()
> db.mydb.help()
> 
# 如果后面不加括号的话，查看函数源代码
> db.mydb.update

# db中本身有version属性
> db.version

# 如果要获取db中的version集合
> db.getCollection("version")

```


## 1.5 数据类型


```python
# null 空值或不存在的字段
> a = {"x":null}

> a = {"x":true}

> a = {"x":3}

# 对象ID
> a = {"x":ObjectId()}
{ "x" : ObjectId("59d98d745881a5de879a28f0") }

# 日期类型
> a = {"x":new Date()}
{ "x" : ISODate("2017-10-08T02:29:18.212Z") }

# 支持正则表达式
> a = {"x":/foobar/i}

# 定义函数
> a = {"x":function(){/*...*/}}
{ "x" : function (){/*...*/} }

# 未定义类型
> a = {"x":undefined}
{ "x" : undefined }

# 数组
> a = {"x":[1,2,3]}
{ "x" : [ 1, 2, 3 ] }

# 内嵌文档
> a = {"x":{'foo':"bar"}}
{ "x" : { "foo" : "bar" } }
```

## 1.6 _id和ObjectId

文档中必须有一个`_id`，默认为ObjectId对象，ObjectId并不像常规的做法生成主键ID，比如自增法，主要是MongoDB一开始就设计用来作为分布式数据库，处理多个节点是核心要求。即要保证一个集合分布到多个机器上后，同时生成文档的id不能有重复。


下面是ObjectId的构造，64位机器上是24位的id值。

```python
> a = {"x":ObjectId()}
{ "x" : ObjectId("59d991fd5881a5de879a28f1") }
> a = {"x":ObjectId()}
{ "x" : ObjectId("59d991fe5881a5de879a28f2") }
> a = {"x":ObjectId()}
{ "x" : ObjectId("59d992015881a5de879a28f3") }
```


- 0到5位: 时间戳，所以默认了按照时间顺序对文档排序
- 6到11位: 机器码，保证不同机器上能生成不同的id
- 12到17位: PID，同一个机器，如果多个进程并发的话，产生的ID也是唯一的
- 18到23位：计数器



# 2. 创建/更新/删除文档

## 2.1 插入并保存文档

尽量批量插入，批量插入的话能减少HTTP请求，减少消息头的数量，效率更高。
但是只能批量对一个文档插入，另外一次批量插入的文档大小是有限制的，主要是MongoDB希望避免不良的模式设计，保证稳定性能。

```python
db.foo.insert({"bar":"baz"})
```


## 2.2 删除文档

有两种方式可以删除文档，分别为` remove()`和` drop()`，前者只是删除集合中的文档，保留索引和集合本身，后面的drop会将直接清除集合，直接清除集合本身更快。

下面做个试验:

- 先插入10万条文档到集合中:

```python
from pymongo import MongoClient

import pprint
import time

client = MongoClient("mongodb://localhost:27017")
db = client.examples

start = time.time()

for i in range(100000):
    db.test.insert_one({"foo":"bar","bar":i,"z":10-i})

print "%f ms" %((time.time()-start)*1000)
```

输出时间为 `28109.999895 ms `，用了接近28秒。

- 先用remove的方式删除(remove已经不推荐使用了:(  ):

```python
def remove_collections():
    start = time.time()
    
    db.test.remove()
    db.test.find()
    
    print "%f ms" %((time.time()-start)*1000)
    
if __name__ == "__main__":
    remove_collections()
```

输出时间为 ` 658.999920 ms`

发现集合还是存在的:

```python
> db.getCollectionNames()
[ "arachnid", "autos", "cities", "test" ]

```

- 再次运行上面的代码，将这10万条插入集合，再用drop方式清除集合

```python
def drop_collections():
    start = time.time()
    
    db.test.drop()
    db.test.find()
    
    print "%f ms" %((time.time()-start)*1000)
    
if __name__ == "__main__":
    drop_collections()
```

输出时间为 `2.000093 ms `，时间缩短了很多。

发现集合已经消失了：

```python
> db.getCollectionNames()
[ "arachnid", "autos", "cities" ]
```

但是用drop的代价就是，不能有任何的限制条件，直接将集合删除。


## 2.3 更新文档

###2.3.1  文档替换式更新

```python
> post = {"title":"My blog post",}
{ "title" : "My blog post" }

> db.blog.insert(post)
WriteResult({ "nInserted" : 1 })

> post.comment = {'rank':"excellent"}
{ "rank" : "excellent" }

> db.blog.update({title:"My blog post"},post)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.blog.find()
{ "_id" : ObjectId("59d99aef5881a5de879a28f4"), "title" : "My blog post", "comment" : { "rank" : "excellent" } }

```

### 2.3.2 修改器 - `$set`

`$set` 用来指定一个键的值，如果这个键不存在，则创建它。

- 通过`$set`能增减键和值，更新指定键的值，值还可以改变类型，比如修改为list，最后也能清空。

```python
> db.users.insert({"name":"ljun","age":18,"sex":"male","loc":"tokyo"})

# 原来不存在，所以追加了键
> db.users.update({"name":"ljun"},{"$set":{"favorite book":"war and peace"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "favorite book" : "war and peace" }

# 更新
> db.users.update({"name":"ljun"},{"$set":{"favorite book":"python2"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "favorite book" : "python2" }

# 更新为list
> db.users.update({"name":"ljun"},{"$set":{"favorite book":["python2","war and peace"]}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "favorite book" : [ "python2", "war and peace" ] }

# 清空了指定key的值
> db.users.update({"name":"ljun"},{"$unset":{"favorite book":1}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo" }

```


- 也能对内嵌文档进行更新，比如

```python
> mama = {"name":"wl","age":18,"children":{"name":"uta","age":4}}
> db.users.insert(mama)

> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo" }
{ "_id" : ObjectId("59d9a1505881a5de879a28f8"), "name" : "wl", "age" : 18, "children" : { "name" : "uta", "age" : 4 } }

# 通过.号引入关联文档
> db.users.update({"name":"wl"},{"$set":{"children.name":"utane"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo" }
{ "_id" : ObjectId("59d9a1505881a5de879a28f8"), "name" : "wl", "age" : 18, "children" : { "name" : "utane", "age" : 4 } }
>
```

- 注意修改的时候，一定要用修改器，如果不用的话，注意如下代码:


```python
# 如果不用修改器，会将文档整体进行更新
> db.users.update({"name":"wl"},{"children":"utane"})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo" }
{ "_id" : ObjectId("59d9a1505881a5de879a28f8"), "children" : "utane" }

```


### 2.3.3 修改器 - `$inc`

`$inc` 修改器用来增加已有的键的值，或者在键不存在的时候创建一个键，对于分析数据十分方便。
注意只能针对数字类型进行操作。

```python
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo" }

# 新增了一个键
> db.users.update({"name":"ljun"},{"$inc":{"point":100}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 100 }

# 增减了键point的值
> db.users.update({"name":"ljun"},{"$inc":{"point":100}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200 }
```

### 2.3.4 数组修改器 - `$push` 和 `$addToSet`

- `$push`会向已有的数组末尾加入一个元素，没有就会创建新的数组。

```python

# 第一次的话，新增了一个键，对应的value是个list
> db.users.update({"name":"ljun"},{"$push":{"children":"uta"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "children" : [ "uta" ] }

# 第二次，往已有的list中追加
> db.users.update({"name":"ljun"},{"$push":{"children":"utasuke"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "children" : [ "uta", "utasuke" ] }

# 只能一次追加一个，如果将list添加进入的话，会成为一个嵌套的list
> db.users.update({"name":"ljun"},{"$push":{"children":["x","y"]}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "children" : [ "uta", "utasuke", [ "x", "y" ] ] }
```


- `$addToSet` ，类似上面的功能，但是如果已经有那个值的话，就不会重复添加。

```python

# 新加了一个新的键
> db.users.update({"name":"ljun"},{"$addToSet":{"newname":"ljun1"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1" ] }

# 指定键中追加了一个值
> db.users.update({"name":"ljun"},{"$addToSet":{"newname":"ljun2"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1", "ljun2" ] }

# 再次追加相同的值，无法追加进去
> db.users.update({"name":"ljun"},{"$addToSet":{"newname":"ljun1"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1", "ljun2" ] }

```

- `$addToSet` 结合`$each`实现一次添加多个不同的值。

```python
> db.users.update({"name":"ljun"},{"$addToSet":{"newname":{"$each":["ljun1","ljun3","ljun4"]}}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1", "ljun2", "ljun3", "ljun4" ] }

> db.users.update({"name":"ljun"},{"$addToSet":{"newname":["ljun1","ljun3","ljun4"]}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1", "ljun2", "ljun3", "ljun4", [ "ljun1", "ljun3", "ljun4" ] ] }
>

```

### 2.3.5 `$pop` 和`$pull`删除数组中元素


```python

# 通过pop，从头部或末尾删除，{$pop:{key:1}}末尾删除，-1则从头部删除
> db.users.update({"name":"ljun"},{"$pop":{"newname":1}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1", "ljun2", "ljun3", "ljun4" ] }

# pull可以指定条件进行删除
> db.users.update({"name":"ljun"},{"$pull":{"newname":"ljun3"}})
> db.users.find()
{ "_id" : ObjectId("59d99fb95881a5de879a28f7"), "name" : "ljun", "age" : 18, "sex" : "male", "loc" : "tokyo", "point" : 200, "newname" : [ "ljun1", "ljun2", "ljun4" ] }
>
```

### 2.3.6 数组的定位修改器:

先准备点数据:

```python

# 
> comments = [{"comment":"good people","author":"wl","votes":1},{"comment":"bad guy","author":"uta","votes":2}]

# 将上面的comments数据添加到指定文档中
> db.users.update({"name":"ljun"},{"$set":{"comments":comments}})

# 
> db.users.find().pretty()
{
        "_id" : ObjectId("59d99fb95881a5de879a28f7"),
        "name" : "ljun",
        "age" : 18,
        "sex" : "male",
        "loc" : "tokyo",
        "point" : 200,
        "newname" : [
                "ljun1",
                "ljun2",
                "ljun4"
        ],
        "comments" : [
                {
                        "comment" : "good people",
                        "author" : "wl",
                        "votes" : 1
                },
                {
                        "comment" : "bad guy",
                        "author" : "uta",
                        "votes" : 2
                }
        ]
}
```


定位符`$`,即下面的第二种方式，只更新第一个匹配的元素。
如果该集合中，有多个uta的author，那也只会更新第一个找到的文档。

```python

# 通过下标去更新指定的文档的field
> db.users.update({"name":"ljun"},{"$inc":{"comments.1.votes":1}})
> db.users.find().pretty()
{
......
                {
                        "comment" : "bad guy",
                        "author" : "uta",
                        "votes" : 3
                }
        ]
}

# 但是很多情况是不知道下标的，这时可以通过下面的方式更新指定的键

> db.users.update({"comments.author":"uta"},{"$set":{"comments.$.comment":"bad bad guy"}})
> db.users.find().pretty()
{
......
                {
                        "comment" : "bad bad guy",
                        "author" : "uta",
                        "votes" : 3
                }
        ]
}
>
```

### 2.3.7 关于修改器的速度

有些修改器的运行速度较快，比如`$inc`，因为它不需要改变文档的大小，只需要修改键的值。
`$set`能在文档大小不变化时立即修改，否则性能也会有所下降。但是比如`$push`因为会改变文档大小，速度就会慢一些。

如果`$push`成为了速度的瓶颈，可以考虑将内嵌数组独立出来，放到一个单独的集合中。

下面做个试验，测试下set和push的速度

- push

```python

def push_collections():
    start = time.time()
    for i in range(1000):
        db.test.update_one({},{"$push":{"x":i}})
    
    print "%f ms" %((time.time()-start)*1000)
    
if __name__ == "__main__":
    push_collections()

```

输出的时间是 ` 2479.000092 ms`

- set

```python
def inc_collections():
    start = time.time()
    for i in range(1000):
        db.test.update_one({},{"$set":{"x":1}})
    
    print "%f ms" %((time.time()-start)*1000)
    
if __name__ == "__main__":
    inc_collections()
```

输出的时间是 ` 322.999954 ms`


## 2.4 upsert

upsert是一种特殊的更新，要是没有文档符合更新条件，就会以这个条件和更新文档为基础，创建一个新的文档。

- 使用save进行更新

save是一个shell函数，可以在文档不存在时插入，存在的时候更新，它只有一个参数，文档。
要是这个文档有`_id`键，save会调用upsert，否则会调用插入。

```python
> var x = db.analytics.findOne()
> x.pageviews = 100
100

> db.analytics.save(x)
> db.analytics.find()
{ "_id" : ObjectId("59d99cd55881a5de879a28f6"), "url" : "yahhoo.co.jp", "pageviews" : 100 }

> x.pageviews = 101
101

# 如果不用save，则用update，比较繁琐
> db.analytics.update({"_id":x._id},x)
> db.analytics.find()
{ "_id" : ObjectId("59d99cd55881a5de879a28f6"), "url" : "yahhoo.co.jp", "pageviews" : 101 }
```

## 2.5 更新多个文档`{multi:true}`

```python

# 修改之前的文档
> db.users.find().pretty()
{
        "_id" : ObjectId("59d99fb95881a5de879a28f7"),
        "age" : 18,
}
{ "_id" : ObjectId("59d9b6155881a5de879a28f9"), "name" : "wal", "age" : 19 }

# 不添加任何option的话，会只更新第一条数据
> db.users.update({},{"$set":{"age":15}})
> db.users.find().pretty()
{
        "_id" : ObjectId("59d99fb95881a5de879a28f7"),
        "age" : 15,
}
{ "_id" : ObjectId("59d9b6155881a5de879a28f9"), "name" : "wal", "age" : 19 }

# 添加`{multi:true}`，所有的数据都进行了更新
> db.users.update({},{"$set":{"age":16}},{multi:true})
> db.users.find().pretty()
{
        "_id" : ObjectId("59d99fb95881a5de879a28f7"),
        "age" : 16,
}
{ "_id" : ObjectId("59d9b6155881a5de879a28f9"), "name" : "wal", "age" : 16 }
>
```


## 2.6 瞬间完成

本章讨论的各个操作，插入/删除/更新，都是瞬间完成的，这是因为他们不需要等待数据库的响应。
客户端将文档发送给服务器后就立刻干别的了，客户端永远不会收到服务器端的响应。

这个特点是速度快，这些操作都会非常快的被执行，只会受发送速度和网络速度的制约。
(MongoDB开发者选择了不安全版本作为默认版本)


