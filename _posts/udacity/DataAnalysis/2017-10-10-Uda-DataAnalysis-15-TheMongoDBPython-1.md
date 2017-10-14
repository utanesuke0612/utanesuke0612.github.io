---
layout: post
title: Uda-DataAnalysis-15-[扩展]-python中使用MongoDB简介
date: 2017-10-8 04:00:00
categories: Uda-数据分析进阶
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}


> 参考 http://api.mongodb.com/python/current/tutorial.html
讲述在Python中操作MongoDB的基础知识。


# 1. 创建一个MongoDB的客户端连接

```python
from pymongo import MongoClient
client = MongoClient()

#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')
```

# 2. 取得数据库

```python
# db = client['test-database']
db = client.test_database
```

# 3. 取得集合

集合是文档的group。

```python
#collection = db['test-collection']
collection = db.test_collection
```

要注意的是，上面的连接(集合和数据库)都是懒连接，上面的命令，并不会立即在MongoDB的服务器端执行，只有在实际开始使用，比如插入一条文档，或是查询一条文档的时候，才去实际的连接

# 4. 文档

在MongoDB中，文档是以jason格式呈现，在pymongo即python中，以字典dict的方式建立，然后存储到MongoDB中时转换为BSON形式。


```python
import datetime
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
```

# 5. 插入文档

插入一条文档，没有指定id的话，会自动创建一个，这个id在集合内是唯一的。

insert_one() 函数在插入一个文档的同时，返回对应的InsertOneResult对象。

```python
# 没有对应的collection会建立一个
posts = db.posts

# 取出返回的InsertOneResult的id
post_id = posts.insert_one(post).inserted_id
post_id
```


    输出: ObjectId('59dc634de2861d140079142a')



下面验证是是否生成了对应的集合：


```python
db.collection_names(include_system_collections=False)
```

    输出: ['posts', 'profiles']



# 6. 取得一个文档

通过  find_one()  可以取得一个文档或是多个文档的第一条,返回一个dict数据类型。


```python
import pprint
pprint.pprint(posts.find_one())
```

    {'_id': ObjectId('59dc634de2861d140079142a'),
     'author': 'Mike',
     'date': datetime.datetime(2017, 10, 10, 6, 6, 2, 947000),
     'tags': ['mongodb', 'python', 'pymongo'],
     'text': 'My first blog post!'}
    

当然也可以指定条件进行查询:


```python
pprint.pprint(posts.find_one({"author":"Mike"}))
```

    输出: {'_id': ObjectId('59dc634de2861d140079142a'),
     'author': 'Mike',
     'date': datetime.datetime(2017, 10, 10, 6, 6, 2, 947000),
     'tags': ['mongodb', 'python', 'pymongo'],
     'text': 'My first blog post!'}
    

# 7. 通过ObjectID查找

也可以通过ID查找，post_id是之前插入数据时返回对象中的字段。


```python
pprint.pprint(posts.find_one({"_id":post_id}))
```

    输出: {'_id': ObjectId('59dc634de2861d140079142a'),
     'author': 'Mike',
     'date': datetime.datetime(2017, 10, 10, 6, 6, 2, 947000),
     'tags': ['mongodb', 'python', 'pymongo'],
     'text': 'My first blog post!'}
    

需要注意的是:post_id是一种objectID的数据类型，不能用String替代去查找，id不是一个str，而是一个ObjectId对象。


```python
print(type(post_id))
```

    输出: <class 'bson.objectid.ObjectId'>
    


```python
print(type(str(post_id)))
print(str(post_id))
```

    输出: <class 'str'>
    59dc634de2861d140079142a
    

通过String类型去查找，找到不对应的对象。


```python
pprint.pprint(posts.find_one({"_id":str(post_id)}))
```

    输出: None
    

# 8. 一次性插入多条记录

注意下面的两个文档，结构是不同的。


```python
new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
```

通过函数 insert_many可以一次性插入多条记录，与上面的insert不同的是，返回的也是一个文档集合。


```python
result = posts.insert_many(new_posts)
```


```python
result.inserted_ids
```


    输出: [ObjectId('59dc6365e2861d140079142b'), ObjectId('59dc6365e2861d140079142c')]



# 9. 一次性查询多条记录


```python
posts_finder = posts.find()
```


```python
print(posts_finder)
print(type(posts_finder))
```

    输出: <pymongo.cursor.Cursor object at 0x0455EE50>
    	  <class 'pymongo.cursor.Cursor'>
  

注意上面通过find()返回的是个cursor，即游标，要通过下面的迭代才能取得文档数据。


```python
for post in posts_finder:
    pprint.pprint(post)
```

	输出:{'_id': ObjectId('59dc634de2861d140079142a'),
	     'author': 'Mike',
	     'date': datetime.datetime(2017, 10, 10, 6, 6, 2, 947000),
	     'tags': ['mongodb', 'python', 'pymongo'],
	     'text': 'My first blog post!'}
	    {'_id': ObjectId('59dc6365e2861d140079142b'),
	     'author': 'Mike',
	     'date': datetime.datetime(2009, 11, 12, 11, 14),
	     'tags': ['bulk', 'insert'],
	     'text': 'Another post!'}
	    {'_id': ObjectId('59dc6365e2861d140079142c'),
	     'author': 'Eliot',
	     'date': datetime.datetime(2009, 11, 10, 10, 45),
	     'text': 'and pretty easy too!',
	     'title': 'MongoDB is fun'}

与find_one()一样，也可以追加查找条件。

# 10. 集合的count


```python
posts.count()
```

    输出: 3


```python
posts.find({"author": "Mike"}).count()
```

    输出: 2



# 11. 范围查询

`{"date":{"$lt":d}这种过滤器的语法，与MongoDBshell中一样，另外，sort支持多个条件共同排序，支持升序降序等方式，具体查看文档。


```python
d = datetime.datetime(2009, 11, 12, 12)

for post in posts.find({"date":{"$lt":d}}).sort("author"):
    pprint.pprint(post)
```

	 输出:{'_id': ObjectId('59dc6365e2861d140079142c'),
	     'author': 'Eliot',
	     'date': datetime.datetime(2009, 11, 10, 10, 45),
	     'text': 'and pretty easy too!',
	     'title': 'MongoDB is fun'}
	    {'_id': ObjectId('59dc6365e2861d140079142b'),
	     'author': 'Mike',
	     'date': datetime.datetime(2009, 11, 12, 11, 14),
	     'tags': ['bulk', 'insert'],
	     'text': 'Another post!'}
    

# 12. index

添加index能加快特定的查询的查询速度。

创建指定键的index，create_index中还可以指定联合index，以及优先顺序，具体去查文档。


```python
result = db.profiles.create_index('user_id',unique=True)
```

可以看到index被正确加入了:


```python
sorted(list(db.profiles.index_information()))
```


    输出: ['_id_', 'user_id_1']



在增加几条新的记录:


```python
user_profiles = [
     {'user_id': 211, 'name': 'Luke'},
     {'user_id': 212, 'name': 'Ziltoid'}]
```


```python
result = db.profiles.insert_many(user_profiles)
```

这条记录因为有不同的user_id，可以正确的插入:


```python
new_profile = {'user_id': 213, 'name': 'Drew'}
```


```python
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
```


```python
result = db.profiles.insert_one(new_profile) 
```

result = db.profiles.insert_one(duplicate_profile)

但是执行上面的insert时会出如下错误，因为index重复了。

```
DuplicateKeyError: E11000 duplicate key error index: test_database.profiles.$user_id_1 dup key: { : 212 }
```