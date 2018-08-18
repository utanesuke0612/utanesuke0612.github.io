---
layout: post
title: Uda-DataAnalysis-17-使用MongoDB分析数据
date: 2017-10-8 07:00:00
categories: 数据分析
tags: MongoDB DataAnalysis 
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的17,18 关于如何使用MongoDB分析数据。 
> 


# 3. 聚合框架示例

下面的示例中，按照user的screen_name进行分类，然后各个name下的count计算，再降序排列。

1. 下面的语句使用了管道，管道就是把一个stage的数据传递给下一个stage。
2. 在这里stage1就是group处理后的数据，stage1处理后的数据包含 id 和对应的cout。
3. stage2接收stage1的数据，并排序处理。

注意在经过stage的时候，可能会对数据的形式作出很大的变化。

下面的代码与视频演示中的示例代码有所不同:

1. 在本地的db名和collections名不同。
2. 最新的mongodb在返回的结果集时，返回的是游标，而不是数据，游标类似python的生成器，需要再次for循环取出数据。


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

def most_tweets():
    result = db.twitter.aggregate([
        {"$group":{"_id":"$user.screen_name",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}}])
    return result

if __name__ == "__main__":
    result = most_tweets()
    for row in result:
        pass
        # pprint.pprint(row)
```

输出结果如下:
```python
{ "_id" : "behcolin", "count" : 8 }
{ "_id" : "JBTeenageDream", "count" : 7 }
{ "_id" : "mysterytrick", "count" : 7 }
{ "_id" : "fatcouncillor", "count" : 6 }
{ "_id" : "officialjamesj", "count" : 6 }
{ "_id" : "mollyripsher", "count" : 6 }
Type "it" for more
```

# 5. 练习 使用组

与上面示例代码完全一样


```python
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
        {"$group":{"_id":"$source",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}}]
    return pipeline

def tweet_sources(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]

if __name__ == '__main__':
    db = get_db('mydb')
    pipeline = make_pipeline()
    result = tweet_sources(db, pipeline)
    import pprint
    #pprint.pprint(result[0])
    #assert result[0] == {u'count': 868, u'_id': u'web'}
```

# 8. Match运算符


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

def highest_ratio():
    result = db.twitter.aggregate([
        {"$match":{"user.friends_count":{"$gt":0},
                  "user.followers_count":{"$gt":0}}},
        {"$project":{"ratio":{"$divide":["$user.followers_count",
                                         "$user.friends_count"]},
                    "screen_name1":"$user.screen_name"}},
        {"$sort":{"count":-1}},
        {"$limit":3}])
    return result

if __name__ == "__main__":
    result = highest_ratio()
    for row in result:
        pprint.pprint(row)
        pass
```

输出如下:

```python
{u'_id': ObjectId('59d787bfa6f78538cda3b1ab'),
 u'ratio': 0.11764705882352941,
 u'screen_name': u'seabass18'}
{u'_id': ObjectId('59d787bfa6f78538cda3b1ac'),
 u'ratio': 1.1523809523809523,
 u'screen_name': u'wildcard_7'}
{u'_id': ObjectId('59d787bfa6f78538cda3b1ad'),
 u'ratio': 1.551111111111111,
 u'screen_name': u'Liahyunjoong'}
```


# 9. Project运算符

1. 使用原始文档中的field
2. 插入新计算得到的field
3. 重命名field
4. 生成一个包含子文档的field

```python
result = db.tweets.aggregate([
    {"$match":{"user.friends_count":{"$gt":0},
                "user.followers_count":{"$gt":0}}},
    {"$project":{"ratio":{"$divide":["$user.followers_count",
                                    "$user.friends_count"]},
                 "screen_name":"$user.screen_name"}},
    {"$sort":{"ratio":-1}},
    {"$limit":1}
    ])

```

例如上面的ratio，就是通过计算得到的，计算用的运算符是`$divide`

# 10. 练习 match和 project

写一个回答以下问题的聚合查询：
对于巴西利亚时区的用户，哪些用户发推次数不低于 100 次，哪些用户的关注者数量最多？

以下提示将帮助你解决这一问题：
- 你可以在每个推特的用户对象的“time_zone”字段中找到时区。
- 你可以在“statuses_count”字段中找到每个用户的发推数量。

注意，你需要创建“followers”、“screen_name”和“tweets”字段，这三个字段分别表示 关注者数量，网络名，以及发推文的数量。


```python
#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
        {"$match":{"user.statuses_count":{"$gt":100},
                  "user.time_zone":"Brasilia"}},
        {"$project":{"screen_name":"$user.screen_name",
                    "followers":"$user.followers_count",
                    "tweets":"$user.statuses_count"}},
        {"$sort":{"followers":-1}},
        {"$limit":1}]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('mydb')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    #assert len(result) == 1
    #assert result[0]["followers"] == 17209
```

    输出: [{u'_id': ObjectId('59d787bfa6f78538cda3def0'),
          u'followers': 259760,
          u'screen_name': u'otaviomesquita',
          u'tweets': 10997}]
    

# 11. unwind运算符

unwind能将数据分开，比如一个father文档中，有children字段，children字段有多个孩子的信息，是个list。

unwind能把每个孩子作为一个field，与father的其他field一起，组成一个新的文档。

先看一个数据的结构，存储的用户在推文中，提到的其他用户名:

```python
"entities" : {
                "user_mentions" : [
                        {
                                "indices" : [
                                        0,
                                        12
                                ],
                                "screen_name" : "AdmireBiebs",
                                "name" : "with ari ♥",
                                "id" : 64392486
                        }
                ],
                "urls" : [ ],
                "hashtags" : [ ]
        },
```



```python
# 如下是找出提到了其他用户三个的推文
result = db.twitter.find({"entities.user_mentions":{"$size":3}})
pprint.pprint(result[0])
```

    输出：{u'_id': ObjectId('59d787bfa6f78538cda3b1e6'),
         u'contributors': None,
         u'coordinates': None,
         u'created_at': u'Thu Sep 02 18:11:30 +0000 2010',
         u'entities': {u'hashtags': [],
                       u'urls': [],
                       u'user_mentions': [{u'id': 115877519,
                                           u'indices': [48, 57],
                                           u'name': u'Lathifah Maulida',
                                           u'screen_name': u'fremolio'},
                                          {u'id': 86039346,
                                           u'indices': [65, 73],
                                           u'name': u"Nya' Zata Amani",
                                           u'screen_name': u'nyazaaa'},
                                          {u'id': 59490923,
                                           u'indices': [101, 113],
                                           u'name': u'Aidina Ashura',
                                           u'screen_name': u'aidinashura'}]},
         u'favorited': False,
         u'geo': None,
         ...
         u'source': u'<a href="http://www.snaptu.com" rel="nofollow">Snaptu.com</a>',
         u'text': u'Yang ini pun ga memberikan penjelasan --&gt; RT @fremolio: --"RT @nyazaaa: Aku ikutan bingung -,- RT @aidinashura: Alasanya? -.-"',
         u'truncated': False,
         u'user': {u'contributors_enabled': False,
                   u'created_at': u'Thu Jul 23 15:11:48 +0000 2009',
                   u'description': u'I am a person, a kid, a daughter, a grandchild, a little sister, a cousin, a student, a friend, a ...
                   u'verified': False}}
    


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

# 
def user_mentions():
    result = db.twitter.aggregate([
        {"$match":{"entities.user_mentions":{"$size":3}}},
        {"$unwind":"$entities.user_mentions"},
        {"$group":{"_id":"$user.screen_name",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":1}
    ])
    return result

if __name__ == "__main__":
    result = user_mentions()
    for row in result:
        pprint.pprint(row)
        pass
```

    输出: {u'_id': u'vanilla3450', u'count': 18}
    

# 12. 练习 使用unwind运算符

印度的哪个地区包括的城市最多？“isPartOf”字段包含一个地区数组，可以在其中查找城市。

```python
def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
        {"$match":{"country":"India"}},
        {"$unwind":"$isPartOf"},
        {"$group":{"_id":"$isPartOf",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        ]
        
    return pipeline
```


输出的结果为:(Uttar Pradesh为印度人口最多的城市，也是最大的城市，包含了623个city)

```python
{u'_id': u'Uttar Pradesh', u'count': 623}
```

数据的格式为:

```python
{
    "_id" : ObjectId("52fe1d364b5ab856eea75ebc"),
    "elevation" : 1855,
    "name" : "Kud",
    "country" : "India",
    "lon" : 75.28,
    "lat" : 33.08,
    "isPartOf" : [
        "Jammu and Kashmir",
        "Udhampur district"
    ],
    "timeZone" : [
        "Indian Standard Time"
    ],
    "population" : 1140
}
```

- $unwind：将数组元素拆分为独立字段

例如:article文档中有一个名字为tags数组字段：

```
db.article.find() 

{ "_id" : ObjectId("528751b0e7f3eea3d1412ce2"),
"author" : "Jone", 
"title" : "Abook",
"tags" : [  "good",  "fun",  "good" ] }
```
使用$unwind操作符后：

```
db.article.aggregate({$project:{author:1,title:1,tags:1}},{$unwind:"$tags"}) 

{ 
        "result" : [ 
                { 
                        "_id" : ObjectId("528751b0e7f3eea3d1412ce2"), 
                        "author" : "Jone", 
                        "title" : "A book", 
                        "tags" : "good" 
                }, 
                { 
                        "_id" : ObjectId("528751b0e7f3eea3d1412ce2"), 
                        "author" : "Jone", 
                        "title" : "A book", 
                        "tags" : "fun" 
                }, 
                { 
                        "_id" : ObjectId("528751b0e7f3eea3d1412ce2"), 
                        "author" : "Jone", 
                        "title" : "A book", 
                        "tags" : "good" 
                } 
                    ], 
        "ok" : 1 
}
```

# 13. 组累加运算符  ``` $addToSet,$push```

上面两者的差别在于，前者不重复追加。

另外，在group运算符中，可以使用如下运算符，```$sum,$first,$last,$max,$min,$avg ```

下面的语句取出每个标签下，tweet被转发的平均次数。


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

# 
def user_mentions():
    result = db.twitter.aggregate([
        {"$unwind":"$entities.hashtags"},
        {"$group":{"_id":"$entities.hashtags.text",
                  "retweet_avg":{"$avg":"$retweet_count"}}},
        {"$sort":{"retweet_avg":-1}},
        {"$limit":1}
    ])
    return result

if __name__ == "__main__":
    result = user_mentions()
    for row in result:
        pprint.pprint(row)
        pass
```

    输出: {u'_id': u'ChatterFact', u'retweet_avg': None}
    

- 每个用户使用过的不同标签


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

# 
def uniqu_hashtag_by_user():
    result = db.twitter.aggregate([
        {"$unwind":"$entities.hashtags"},
        {"$group":{"_id":"$user.screen_name",
                  "unique_hashtags":{"$addToSet":"$entities.hashtags.text"}}},
        {"$limit":1}
    ])
    return result

if __name__ == "__main__":
    result = uniqu_hashtag_by_user()
    for row in result:
        pprint.pprint(row)
        pass
```

    输出: {u'_id': u'cwofford', u'unique_hashtags': [u'kpisback']}
    

# 14. 练习，使用推送

在下面的聚合中，使用了五个阶段:
1. unwind，使用tag将文档打散，即每个taglist中的tag单独出来，与文档的其他field组成给一个新的文档，比如list中有3个tag，则一个文档会变成3个文档。
2. group，利用上面unwind重新生成的文档，用用户的screen_name进行分组，并计算每组用户名下文档的条数(因为之前是按tag打散了文档，所以计算结果是每个用户下tag的数量)，并输出对应用户的推文(将推文加到一个)。(视频中使用的是push，但是重复的推文太多，影响阅读)
3. sort，每个用户tag的数量降序排列。
4. skip，前两条数据没有代表性，全是重复的，skip掉。
5. limit，限定输出一条，即除了skip掉的最多的。


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

# 
def uniqu_hashtag_by_user():
    result = db.twitter.aggregate([
       {"$unwind":"$entities.hashtags"},
        {"$group":{"_id":"$user.screen_name",
                  "tweet_texts":{"$addToSet":"$text"},
                  "count":{"$sum":1}
                  }
        },
        {"$sort":{"count":-1}},
        {"$skip":2},
        {"$limit":1}
    ])
    return result

if __name__ == "__main__":
    result = uniqu_hashtag_by_user()
    for row in result:
        pprint.pprint(row)
        pass
```

    输出: {u'_id': u'oliviapearson',
         u'count': 16,
         u'tweet_texts': [u'How To Lose Weight - free videos here: http://bit.ly/c7blWO #video #videos #free #how #howto #loseweight #freeweightloss #diet #obesity',
                          u'Santana video selection - click here: http://bit.ly/aZXeeH #music #nowplaying #guitar #musicmonday #video #tickets #santana']}
    

以上面的数据`u'_id': u'oliviapearson',`做个示例的讲解:


1.原始数据结构如下，只是节选了一部分数据，screen_name为`oliviapearson`，共有两条推文，一共有16个标签，第一条推文7个tag，第二个推文9个tag:

```python
> db.twitter.find({"user.screen_name":"oliviapearson"}).pretty()
{
        "_id" : ObjectId("59d787c0a6f78538cda3fcc7"),
        "text" : "Santana video selection - click here: http://bit.ly/aZXeeH #music #nowplaying #guitar #musicmonday #video #tickets #santana",
        "entities" : {
                "hashtags" : [
                        {
                                "text" : "music",
                                "indices" : [
                                        59,
                                        65
                                ]
                        },
                        {
                                "text" : "nowplaying",
                                "indices" : [
                                        66,
                                        77
                                ]
                        },
                ]
        },
        "user" : {
                "screen_name" : "oliviapearson",
        },
}

{
        "_id" : ObjectId("59d787c0a6f78538cda418c0"),
        "text" : "How To Lose Weight - free videos here: http://bit.ly/c7blWO #video #videos #free #how #howto #loseweight #freeweightloss #diet #obesity",
        "entities" : {
                "hashtags" : [
                        {
                                "text" : "video",
                                "indices" : [
                                        60,
                                        66
                                ]
                         }
                         ...
                ]
        },
        "user" : {
                "screen_name" : "oliviapearson",
        },
}
```

2.按照tag将文档分成多个:


```python
# 通过如下函数查看示例效果:
def uniqu_hashtag_by_user():
    result = db.twitter.aggregate([
       {"$match":{"user.screen_name":"oliviapearson"}},
       {"$unwind":"$entities.hashtags"},
    ])
    return result

if __name__ == "__main__":
    result = uniqu_hashtag_by_user()
    for row in result:
        #pprint.pprint(row)
        pass
```

上面的结果输出后如下:

- 第1条推文(7个tag)的第1个分散后文档

{u'_id': ObjectId('59d787c0a6f78538cda3fcc7'),
 u'entities': {u'hashtags': {u'indices': [59, 65], u'text': u'music'}},
 u'text': u'Santana video selection - click here: http://bit.ly/aZXeeH #music #nowplaying #guitar #musicmonday #video #tickets #santana',
 u'user': {
           u'screen_name': u'oliviapearson',
          }

- 第1条推文(7个tag)的第2个分散后文档

{u'_id': ObjectId('59d787c0a6f78538cda3fcc7'),
 u'entities': {u'hashtags': {u'indices': [66, 77], u'text': u'nowplaying'}},
 u'text': u'Santana video selection - click here: http://bit.ly/aZXeeH #music #nowplaying #guitar #musicmonday #video #tickets #santana',
 u'user': {
           u'screen_name': u'oliviapearson',
           }

- 第2条推文(9个tag)的第1个分散后文档

{u'_id': ObjectId('59d787c0a6f78538cda418c0'),
 u'entities': {u'hashtags': {u'indices': [60, 66], u'text': u'video'}},
 u'text': u'How To Lose Weight - free videos here: http://bit.ly/c7blWO #video #videos #free #how #howto #loseweight #freeweightloss #diet #obesity',
 u'user': {
           u'screen_name': u'oliviapearson',
           }

- 第2条推文(9个tag)的第2个分散后文档

{u'_id': ObjectId('59d787c0a6f78538cda418c0'),
 u'entities': {u'hashtags': {u'indices': [67, 74], u'text': u'videos'}},
 u'user': {
           u'screen_name': u'oliviapearson',
           }

-对上面的数据按用户名分组，该用户名下共有16条数据，另外将这两条推文加到一个新的list中去。

通过如下函数查看示例效果:

```python
def uniqu_hashtag_by_user():
    result = db.twitter.aggregate([
       {"$match":{"user.screen_name":"oliviapearson"}},
       {"$unwind":"$entities.hashtags"},
       {"$group":{"_id":"$user.screen_name",
                  "tweet_texts":{"$addToSet":"$text"},
                  "count":{"$sum":1}
            }
        },
        {"$sort":{"count":-1}},
    ])
    return result

if __name__ == "__main__":
    result = uniqu_hashtag_by_user()
    for row in result:
        pprint.pprint(row)
        pass
```

    输出 {u'_id': u'oliviapearson',
         u'count': 16,
         u'tweet_texts': [u'How To Lose Weight - free videos here: http://bit.ly/c7blWO #video #videos #free #how #howto #loseweight #freeweightloss #diet #obesity',
                          u'Santana video selection - click here: http://bit.ly/aZXeeH #music #nowplaying #guitar #musicmonday #video #tickets #santana']}



# 15. 使用给定运算符的多个阶段

下面的聚合分成6个stage，用来计算哪个用户提到其他用户最多。
1. unwind，每个推文文档，利用推文中提到的用户list打散成多个文档。
2. group，使用上面被打散的文档，利用screen_name分组，并将被提到的用户放入一个set中。
3. unwind，上面的输出有两个，第一个是用户名，第二个是该用户提到过的用户set，再次用后面的被提到的用户set将文档打散。
4. group，经过了上面的打散，成了 A(发推文的用户) -> 1(被提到的用户)，A -> 2，A -> 3，B -> 1， B->99，这样的数据结构，然后再次用发推特的用户进行分组，每组的文档数目，就是该用户提到的用户的总数目。
5. sort，按照上面的count排序。
6. limit，只取前5条文档。


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb

def unique_user_mentions():
    result = db.twitter.aggregate([
       {"$unwind":"$entities.user_mentions"},
        {"$group":{"_id":"$user.screen_name",
                   "mset":{
                       "$addToSet":"$entities.user_mentions.screen_name"
                   }}},
        {"$unwind":"$mset"},
        {"$group":{"_id":"$_id","count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":5}
    ])
    return result

if __name__ == "__main__":
    result = unique_user_mentions()
    for row in result:
        pprint.pprint(row)
        pass
```

     输出: {u'_id': u'Democracy_Work', u'count': 17}
        {u'_id': u'ThizBoySwagLoud', u'count': 16}
        {u'_id': u'itsajstuerd', u'count': 15}
        {u'_id': u'FollowersNeeded', u'count': 15}
        {u'_id': u'Egreeedy', u'count': 12}
    

# 16. Same运算符

这个题目问题的有些暧昧，真实的意图是这样，

1.湖北省内，10个城市，一共5万人，每个城市的平均人口数量是5,000人。

2.湖南省内，5个城市，一共10万人，每个城市的平均人口数量是2万人。

本题需要的是:

- 所有省内，各个城市的平均人口数量 的 平均数 : 2万+5000 / 2 = 12,500人

下面分成四个阶段:
1. unwind，将数据用所属的地区打散，使得文档结构为: 每个city/每个州/该city的人口数量。
2. group,利用上面打散后的文档，按照州分组，得到每个州的城市平均人口数量。(对应上面例子的1/2，省内的城市平均人口数)
3. group，第二个group，利用上面group的输出，即每个州/该州内城市的平均人口数量，继续分组，不过本次只有一个组，该组对应的值是所有州的城市平均人口数的平均数。


```python
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [            
            {'$match' : {'country' : 'India'} },
            {'$unwind' : '$isPartOf'},
            {'$group' : {'_id' : '$isPartOf',
                         'region_avg': {'$avg' : '$population'} } },
            {'$group' : {'_id' : 'India Regional City Population Average',
                         'avg': {'$avg' : '$region_avg'} } },
            ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    #assert len(result) == 1
    # Your result should be close to the value after the minus sign.
    #assert abs(result[0]["avg"] - 201128.0241546919) < 10 ** -8
    import pprint
    pprint.pprint(result)

```



# 18-1. 练习: 最常见的城市名

存在没有城市名name的文档，第一步就是要过滤掉这种数据，使用`$exists`过滤。


```python
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ 
         {"$match":{"name":{"$exists":True}}},
         {"$group":{"_id":"$name",
                    "count":{"$sum":1}}},
         {"$sort":{"count":-1}},
         {"$limit":1}
    ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('mydb')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
   # assert len(result) == 1
   # assert result[0] == {'_id': 'Shahpur', 'count': 6}
```

    输出:[{u'_id': u'?????,NULL"', u'count': 7},
         {u'_id': u'??????', u'count': 3},
         {u'_id': u'Patan', u'count': 3},
         {u'_id': u'Malkapur', u'count': 2},
         {u'_id': u'Waterloo', u'count': 2},
         {u'_id': u'{City of Duluth|Duluth}', u'count': 2},
         {u'_id': u'City of Rochester', u'count': 2},
         {u'_id': u'The City of ANAPRA  New Mexico', u'count': 1},
         {u'_id': u'Lexington North Carolina', u'count': 1},
         {u'_id': u'Sunset Hills Missouri', u'count': 1},
         {u'_id': u'Bourbon Missouri', u'count': 1},
         {u'_id': u'Alamogordo New Mexico', u'count': 1},
         {u'_id': u'City of Kinston North Carolina', u'count': 1},
         {u'_id': u'Westhope North Dakota', u'count': 1},
         {u'_id': u'Bottineau North Dakota', u'count': 1},
         {u'_id': u'Alsen North Dakota', u'count': 1},
         {u'_id': u'Rogers North Dakota', u'count': 1},
         {u'_id': u'Washington North Carolina', u'count': 1},
         {u'_id': u'White Plains New York', u'count': 1},
         {u'_id': u'Leal North Dakota', u'count': 1}]
        

# 18.2. 练习

求特定经纬度之间的哪个含最多城市的region

本地运行不过的，因为本地的数据是没有清洗过的。所以只节选了关键函数。

首先 使用经度过滤，然后利用region的list去将文档分成多个，再按照region分组，得到的每个region的文档数目，也就是city数目
```python
def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ 
        {"$match":{"lon":{"$lte":80,"$gte":75},"country":"India"}},
        {"$unwind":"$isPartOf"},
        {"$group":{"_id":"$isPartOf",
                    "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":1}
        ]
    return pipeline
```


# 18.3. 练习，平均人口

为所有国家，找到每个region的city平均人口数。

1.首先为一个国家的每个region计算city的平均人口数，

2.再计算每个国家的所有region的city平均人口数的平均人口数。
类似于#17的第16个练习。

```python
def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ 
           {'$unwind' : '$isPartOf'},
           {'$group' : {'_id' : {"state":'$isPartOf',"country":"$country"},
                         'region_avg': {'$avg' : '$population'} } },
            {"$group":{"_id":"$_id.country",
                       "avgRegionalPopulation":{"$avg":"$region_avg"}}},
            {"$sort":{"avgRegionalPopulation":1}},
        ]
    return pipeline
```
