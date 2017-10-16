---
layout: post
title: Uda-DataAnalysis-15-使用MongoDB
date: 2017-10-8 06:00:00
categories: Uda-数据分析进阶
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的15,16 关于MongDB使用的总结。 
> 


# 5.预先了解MongoDB

- 现在本地安装MongoDb

参考如下文档 https://github.com/ilivebox/the-little-mongodb-book/blob/master/zh-cn/mongodb.markdown
直接下载了免安装包，按照指示进行执行。


- 安装

C:\Users\utane>pip install pymongo

如果在anaconda中安装，要启动anaconda的prompt，输入 ` conda install -c anaconda pymongo`。


## 5.1 演示MongoDB的连接


```python
def add_city(db):
    db.cities.insert_one({"name" : "Chicago"})
    
def get_city(db):
    return db.cities.find_one()

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db

if __name__ == "__main__":
    db = get_db() 
    add_city(db)
    print get_city(db)
```

    输出：{u'_id': ObjectId('59d4eb91d467dc2a641541a4'), u'name': u'Chicago'}
    

## 5.2 演示文档的插入


```python
from pymongo import MongoClient

import pprint
client = MongoClient("mongodb://localhost:27017")

db = client.examples

def find():
    db.autos.insert_one({"manufacturer" : "porsche"})
    autos = db.autos.find({"manufacturer":"porsche"})
    for a in autos:
        pprint.pprint(a)
        
if __name__ == "__main__":
    find()
```

    输出：{u'_id': ObjectId('59e4bc8ad467dc1c3c464b4a'), u'manufacturer': u'porsche'}
    

# 10. 练习，查找保时捷

指定条件进行查询


```python
def porsche_query():
    query = {"manufacturer" : "porsche"}
    return query

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    return db.autos.find(query)


if __name__ == "__main__":
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print "Printing first 3 results\n"
    import pprint
    for car in results[:3]:
        pprint.pprint(car)
```

    输出：Printing first 3 results
    
    	{u'_id': ObjectId('59e4bc8ad467dc1c3c464b4a'), u'manufacturer': u'porsche'}
    

# 11,多字段查询，投影查询

- 多字段查询


```python
# 将查询条件修改如下，多字段查询
autos = db.autos.find({"manufacturer":"Toyota","class":"mid-size car"})
```

- 投影查询


```python
# 将查询条件修改如下，多字段查询
query = {"manufacturer":"Toyota","class":"mid-size car"}
# 不显示id字段，只显示name字段
projection = {"_id":0,"name":1}
autos = db.autos.find(query,projection)
```

# 13，将数据导入MongoDB


```python
num_autos = db.myautos.find().count()
print "before:",num_autos

for a in autos:
    db.myautos.insert(a)    
num_autos = db.myautos.find().count()
print "after:",num_autos    
```

    输出：before: 0
    	after: 0
    

# 15, 使用 mongoimport导入数据

参考如下命令：

```python
mongoimport -d examples -c myautos --file autos.json
mongoimport --db mydb --collection auto --type csv --headerline --file autos.csv 
```

1. 将MongoDB的bin目录加到环境变量中。
2. 打开cmd，将cmd当前目录切换到工作目录下。
参考如下命令：

C:\Users\utane\OneDrive\udacity\15-MongoDB>mongoimport --db mydb --collection auto --type csv --headerline --file autos.csv

输出如下：

2017-10-05T23:26:32.839+0900    connected to: localhost

2017-10-05T23:26:33.650+0900    imported 7799 documents

导入之后，在mongo的shell中就可以使用了：
- use mydb (命令：切换数据库)
  
  输出：switched to db mydb

- db.auto.find().count()   (命令)

  输出：7799

# 17 范围查询

```python
$gt : greater than
$lt : less than
$gte : greater equal than
$lte : less equal than
$ne : not equal
```

例如查询，人口大于某个值:
query =```{"population":{"$gt":25000}}``` 

大于某值，同时又小于某个值:
query =```{"population":{"$gt":25000,"$lte":50000}}``` 

下面是查询时间:
query =```{"foundingDate":{"$gt":datetime(1837,01,01),"$lte":datetime(1837,12,31)}}``` 


# 18. 练习 - 范围查询

```python
from datetime import datetime
    
def range_query():
    query = {"foundingDate":{"$ne":"NULL"}}
    return query

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.mydb
    return db

if __name__ == "__main__":
    # For local use
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    import pprint
    #pprint.pprint(cities[0])
```

    输出：Found cities: 221
    

- 将cities数据导入到MongoDB

C:\Users\utane\OneDrive\udacity\15-MongoDB>mongoimport --db mydb --collection cities --type csv --headerline --file cities2.csv

2017-10-06T21:52:53.789+0900    connected to: localhost

2017-10-06T21:52:54.183+0900    imported 1722 documents


```python
db.cities.find().count()
```

    输出：1722


在 MongoDB命令行中，通过pretty()可以将结果整形，如下:

db.cities.find().limit(2).pretty()

# 20. MongoDB中使用正则表达式:

查询城市宣言中，包含 friendship的数据

db.cities.find({"motto":{"$regex":"friendship"}}).pretty()

如果要忽略大小写:

```python
db.cities.find({"motto":{"$regex":"[Tt]he"}}).count()
   115
db.cities.find({"motto":{"$regex":"[T]he"}}).count()
   59
```




关于更多正则表达式:参考专门的文档。如下是一些常用的正则表达式。
https://www.regexpal.com/ 可以在线试验正则表达式。

```
Character classes
.	any character except newline
\w \d \s	word, digit, whitespace
\W \D \S	not word, digit, whitespace
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g
Anchors
^abc$	start / end of the string
\b	word boundary
Escaped characters
\. \* \\	escaped special characters
\t \n \r	tab, linefeed, carriage return
\u00A9	unicode escaped ©
Groups & Lookaround
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead
(?!abc)	negative lookahead
Quantifiers & Alternation
a* a+ a?	0 or more, 1 or more, 0 or 1
a{5} a{2,}	exactly five, two or more
a{1,3}	between one & three
a+? a{2,}?	match as few as possible
ab|cd	match ab or cd
```

# 22. in运算符


```python
db.auto.find({"modelYears":{"$in":[1987,1999,2002]}}).count()
```


    输出：0



# 23. 练习使用$in

Your task is to write a query that will return all cars manufactured by
"Ford Motor Company" that are assembled in Germany, United Kingdom, or Japan.


```python
query = {"manufacturer":"Ford Motor Company","assembly":{"$in":["Germany","Japan","United Kingdom"]}}
```


# 24. all运算符

与上面的```$in```类似，```$in```是取后面list的任意一个，但是```$all```是要包含后面所有的list。

# 25. 练习:点表示法

![image](https://user-images.githubusercontent.com/18595935/31280586-c4689daa-aae7-11e7-9b4b-7d7738481fa2.png)

- 将twitter.json文件导入MongoDB

mongoimport --db mydb --collection twitter --type json --file twitter.json

C:\Users\utane\OneDrive\udacity\15-MongoDB>mongoimport --db mydb --collection twitter --type json --file twitter.json

```
2017-10-06T22:40:14.977+0900    connected to: localhost
2017-10-06T22:40:17.970+0900    [######################..] mydb.twitter 84.0MB/88.0MB (95.4%)
2017-10-06T22:40:18.121+0900    [########################] mydb.twitter 88.0MB/88.0MB (100.0%)
2017-10-06T22:40:18.121+0900    imported 51428 documents
```

## 25.1 练习-范围查询 


```python
#!/usr/bin/env python
# 查询宽度大于2.5的汽车

def dot_query():
    query = {"dimensions.width":{"$gt":2.5}}
    return query

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.mydb
    return db

if __name__ == "__main__":
    db = get_db()
    query = dot_query()
    cars = db.cars.find(query)

    print "Printing first 3 results\n"
    import pprint
    for car in cars[:3]:
        pprint.pprint(car)
```

    输出：Printing first 3 results
    

# 26. 更新

```
# 查找一条满足条件的文档，有多个文档情况返回第一个文档
city = db.cities.find_one({"name":"Munchen","country":"Germany"})
city["isoCountryCode"] = "DEU"
db.cities.save(city)
```

# 27. 设置与复位（更新或是删除指定field）

下面的语句完成相同的功能，更新第一条找到的记录:

```python
city = db.cities.update({"name":"Munchen","country":"Germany"},
                        {"$set":{
                           "isoCountryCode": "DEU"
                        }})
```

注意：语句后面必须有`$set`。

不能是如下,下面的条件将匹配前面{}的文档，更新成后面的一条数据的文档:

```python
city = db.cities.update({"name":"Munchen","country":"Germany"},{"isoCountryCode": "DEU"})
```


- 下面的语句，将"isoCountryCode"删除，如果该文档不存在该field，则忽略执行。

```python

city = db.cities.update({"name":"Munchen","country":"Germany"},
                        {"$unset":{
                           "isoCountryCode": ""
                        }})
```

# 28. 多项更新（multi=True）

上面的示例中，只是更新了一个文档，如果要更新多个文档，要追加option: multi=True

```python
city = db.cities.update({"name":"Munchen","country":"Germany"},
                        {"$set":{
                           "isoCountryCode": "DEU"
                        }},multi=True)
```

# 29.删除文档

```python
# 删除所有文档
db.cities.remove()

# 删除所有文档，包括index
db.cities.drop()

# 删除指定城市
db.cities.remove({"name":"tokyo"})

# 删除所有没有名称的城市
db.cities.remove({"name":{"$exists":0}})

```


# 练习-1. :准备数据

- 根据 FIELDS 字典中的映射更改字典的键,即将CSV中的key，修改为FIELD字典中的value，只处理FIELDS中出现过的key。

- 删掉“rdf-schema#label”中的小括号里的多余说明，例如“(spider)”

- 如果“name”为“NULL”，或包含非字母数字字符，将其设为和“label”相同的值。

- 如果字段的值为“NULL”，将其转换为“None”。

- 如果“synonym”中存在值，应将其转换为数组（列表），方法是删掉“{}”字符，并根据`|` 拆分字符串。剩下的清理方式将由你自行决定，例如删除前缀“*”等。如果存在单数同义词，值应该依然是列表格式。

- 删掉所有字段前后的空格（如果有的话）

- 输出结构应该如下所示：

```python
[ { 'label': 'Argiope',
    'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
    'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
    'name': 'Argiope',
    'synonym': ["One", "Two"],
    'classification': {
                      'family': 'Orb-weaver spider',
                      'class': 'Arachnid',
                      'phylum': 'Arthropod',
                      'order': 'Spider',
                      'kingdom': 'Animal',
                      'genus': None
                      }
  },
  { 'label': ... , }, ...
]
```


```python
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        
        # 跳过第2-4行，第一行默认作为key读入
        for i in range(3):
            l = reader.next()
        
        # 处理value数据
        for line in reader:
            data_row = {}
            data_row["classification"] = {}
            for key,k_value in FIELDS.items():
                # 处理 'rdf-schema#label' 中的小括号
                line = check_label(key,line)
                
                # 处理 name 字段,不符合要求就转换为label的值
                line = check_name(key,line)
                
                # 处理字段为NULL的值
                if line[key] == "NULL":
                    line[key] = None
                    
                # 如果是字符串就进行处理
                if type(line[key]) == type(""):
                    line[key] = line[key].strip()
                
                # 处理 synonym
                if key == "synonym" and line["synonym"] != None:
                    #print line["synonym"] 
                    line["synonym"] = parse_array(line["synonym"])
                
                # 处理lable，组成一个字典，这种字段特殊处理
                if key.endswith("_label"):
                    data_row["classification"][k_value] = line[key]
                    continue
                    
                # 除了上述字典外，其他字段的特殊处理
                data_row[k_value] = line[key]
            
            # 
            data.append(data_row) 
            
    pprint.pprint(len(data))
    return data

# 处理 name 字段
def check_name(key,line):
    if key == "name":
        if line[key] == "NULL":
            line[key] = line['rdf-schema#label']
    
        # 如果包含非字母和数字时处理
        if not re.match('^[a-zA-Z0-9]+$',line[key]): 
            line[key] = line['rdf-schema#label']
            
    return line    


# 处理 'rdf-schema#label' 中的小括号
def check_label(key,line):
    if key == "rdf-schema#label":
        # 正则表达式删除括号内内容
        line[key] = re.sub(r'\([^)]*\)', '', line[key])
        line[key] = line[key].strip()
    return line

# 将一个带大括号的字符串处理分隔成list
def parse_array(v):
    # 借鉴这个处理方式
    if (v[0] == "{") and (v[-1] == "}"):
        # 分别从左右开始删除大括号，确保删除的是第一个大括号对
        v = v.lstrip("{")
        v = v.rstrip("}")
        # 分隔成list
        v_array = v.split("|")
        
        # 去除*
        v_array = [i.replace("*","") for i in v_array]
        
        # 去除空格
        v_array = [i.strip() for i in v_array]
        return v_array
    
    # 即使只有一个值，也转换为list
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print "Your first entry:"
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None, 
        "name": "Argiope", 
        "classification": {
            "kingdom": "Animal", 
            "family": "Orb-weaver spider", 
            "order": "Spider", 
            "phylum": "Arthropod", 
            "genus": None, 
            "class": "Arachnid"
        }, 
        "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
        "label": "Argiope", 
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == "__main__":
    test()
```

	输出: 76
	    Your first entry:
	    {'classification': {'class': 'Arachnid',
	                        'family': 'Orb-weaver spider',
	                        'genus': None,
	                        'kingdom': 'Animal',
	                        'order': 'Spider',
	                        'phylum': 'Arthropod'},
	     'description': 'The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced.',
	     'label': 'Argiope',
	     'name': 'Argiope',
	     'synonym': None,
	     'uri': 'http://dbpedia.org/resource/Argiope_(spider)'}
    

# 练习-2. 将数据插入MongoDB

完成 insert_data 函数，将数据插入 MongoDB。需要复习以前Json文件的知识。


```python
import json

def insert_data(data, db):
    for row in data:
        db.arachnid.insert_one(row) 


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        #print db.arachnid.find_one()
```
