---
layout: post
title: Uda-DataAnalysis-项目1-分析OpenStreetMap的OSM数据(代码)
date: 2017-10-8 21:00:00
categories: Uda-数据分析进阶
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的项目1：分析OSM地图数据所使用的代码。 
> 


# 1. 清理数据


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import io
import re
from collections import Counter
import copy
import pprint
import codecs
import json

est_width_counter = Counter()
osm_file_name = "kawasaki1.osm"
osm_file = open(osm_file_name,"r",encoding="utf8")

# 处理邮政编码
def clean_zipcode(zipcode):
    # 去除数字以外的字符
    newzipcode = re.sub(u"\D",u"",zipcode)
    
    # 如果邮政编码长度不为7，则置空
    if not len(newzipcode) == 7:
        newzipcode = ""
    
    return newzipcode

# 处理邮政编码
def audit_zipcode(elem):
    if (elem.tag == "node") or (elem.tag == "way") or (elem.tag == "relation"):
        tag_dict = {}
        for tag in elem.iter("tag"):
            try:
                if (tag.attrib["k"] == "addr:postcode"):
                        zipcode = tag.attrib["v"]
                        newzipcode = clean_zipcode(zipcode)
                        tag.attrib["v"] = newzipcode 
                        #print("{},{}".format(zipcode,newzipcode))
            except:
                pass

# 处理医院相关错误
ori_amenity = ["hospital","doctors","clinic"]
excepted_amenity = 'dentist'
dentist_str = "歯科"

def audit_dentist(elem):
    if (elem.tag == "node") or (elem.tag == "way") or (elem.tag == "relation"):
        tag_dict = {}
        for tag in elem.iter("tag"):
            try:
                if (tag.attrib['k'] == "amenity") and (tag.attrib['v'] in ori_amenity):
                    tag_dict[tag.attrib['k']] = tag.attrib['v']
                if (tag.attrib['k'] == "name") and (dentist_str in tag.attrib['v']):
                    tag_dict[tag.attrib['k']] = tag.attrib['v']
            except:
                return None
        # 如果上面两个条件都满足，即名称含有牙科，但是分类不是牙科时，替换其amenity属性
        if len(tag_dict) == 2:
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "amenity":
                    tag.attrib['v'] = excepted_amenity
                    return True
            
    return False

# 处理宽度数据
def audit_est_width(elem):
    if elem.tag in ["node","way","relation"]:
        for item in elem.iter("tag"):
            if item.attrib["k"] in ["est_width","yh:WIDTH"]:
                width = item.attrib["v"]
                new_width = re.sub(u"[a-zA-Z]",u"",width)
                new_width = new_width.replace("-","〜")
                est_width_counter[new_width] += 1
                
                # 将原先的element改为min，新增一个max
                item_max = copy.deepcopy(item)
                
                item.attrib["k"] = item.attrib["k"] + "_min"
                item.attrib["v"] = float(new_width.split("〜")[0])
                
                # 修改新增的element
                item_max.attrib["k"] = item_max.attrib["k"] + "_max"
                item_max.attrib["v"] = float(new_width.split("〜")[1])
                
                elem.append(item_max)

# 全角转半角
def digit_full2half(fullnum):
    try:
        return {"０":"0","１":"1","２":"2","３":"3","４":"4","５":"5",
                "６":"6","７":"7","８":"8","９":"9","ー":"-"}[fullnum]
    except:
        return fullnum

# 处理housenumber的全半角问题 
def audit_number_full_half(elem):
    if elem.tag in ["node","way","relation"]:
        for item in elem.iter("tag"):
            if item.attrib["k"] in ["addr:housenumber","addr:block_number"]:
                number = item.attrib["v"]
                if re.match(u"[０-９]",number):
                    new_number = "".join((map(digit_full2half,number)))
                if re.match(u"^\d号$",number):
                    new_number = number.replace("号","")
                    
```

# 2. 读取数据，并写入Json文件


```python


# 1.将node/way/relation中的id等值填到dict中
def set_common_info(dict_xml,elem):
    dict_xml["id"] = elem.attrib['id']
    dict_xml["version"] = elem.attrib['version']
    dict_xml["timestamp"] = elem.attrib['timestamp']
    dict_xml["changeset"] = elem.attrib['changeset']
    dict_xml["uid"] = elem.attrib['uid']
    dict_xml["user"] = elem.attrib['user']
    
    # 类型
    dict_xml["type"] = elem.tag
    
    # 如果类型是node，处理pos
    if dict_xml["type"] == "node":
        pos = (elem.attrib['lat'],elem.attrib['lon'])
        dict_xml["pos"] = pos

# 2. 将tag数据写入tag的字典
def set_tag_info(dict_xml,elem):
    dict_xml["tag"] = {}
    dict_tag = {}
    for item in elem.iter("tag"):
        dict_tag[item.attrib["k"]] = item.attrib["v"]
    
    dict_xml["tag"] = dict_tag

# 3. 处理nd数据
def set_nd_info(dict_xml,elem):
    dict_xml["nd"] = []
    for item in elem.iter("nd"):
        dict_xml["nd"].append(item.attrib["ref"])

# 4. 处理member数据
def set_member_info(dict_xml,elem):
    dict_xml["member"] = []
    for item in elem.iter("member"):
        mem_list = []
        mem_list.append(item.attrib["type"])
        mem_list.append(item.attrib["ref"])
        mem_list.append(item.attrib["role"])
        
        dict_xml["member"].append(mem_list)

        
        
# 将xml数据读取并处理为字典格式  
def read_and_process_XML(osm_file):
    dict_xml_list = []
    n = 0
    for event,elem in ET.iterparse(osm_file,events=("start",)):   

        audit_zipcode(elem)
        audit_dentist(elem)
        audit_est_width(elem)
        audit_number_full_half(elem)
        
        # 将一个elem组织成一个dict
        #if elem.tag in ["node","way","relation"]:
        if elem.tag in ["node","way","relation"]:
            #print(elem.tag)
            dict_xml = {}
            
            # 1.将node/way/relation中的id等值填到dict中
            set_common_info(dict_xml,elem)    
            
            # 2. 处理tag数据
            set_tag_info(dict_xml,elem)
            
            # 3. 如果是way类型，则处理nd数据
            if elem.tag == "way":
                set_nd_info(dict_xml,elem)
                
            # 4. 如果是relation类型，处理member数据
            if elem.tag == "relation":
                set_member_info(dict_xml,elem)
            
            # 将填充完毕的dict追加到list中
            dict_xml_list.append(dict_xml)

            # 调试用
            #n += 1
            #if n == 1000000:
            #    break        
    
    return dict_xml_list
        
# 将dict的list写入json文件
def write_dictlist_json(dict_xml_list,osm_file_name):
    file_out = "{0}.json".format(osm_file_name)
    print(file_out)
    with codecs.open(file_out, "w",encoding="utf-8") as fo:
        for el in dict_xml_list:
            #fo.write(json.dumps(el, indent=2,ensure_ascii=False)+"\n")
            # 下面这种方式比较节省空间，另外如果不加ensure_ascii 参数的话，会出现乱码
            fo.write(json.dumps(el,ensure_ascii=False)+"\n")
            pass
            
if __name__ == "__main__":
    dict_xml_list = []
    dict_xml_list = read_and_process_XML(osm_file)
    write_dictlist_json(dict_xml_list,osm_file_name)
    #pprint.pprint(dict_xml_list)
```

    kawasaki1.osm.json
    

# 3. 利用MongoDB进行数据分析

## 3.1  用户贡献度


```python
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.mydb
```


```python
dict_list = []

def most_user():
    result = db.kawasaki.aggregate([
        {"$group":{"_id":"$user",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":8}
    ])
    return result

if __name__ == "__main__":
    sum = 0
    result = most_user()
    for row in result:
        dict_user = {}
        dict_user["_id"] = row['_id']
        dict_user["count"] = row['count']
        sum += row['count']
        
        dict_list.append(dict_user)
    
    # 补全最后的其他用户
    others = {}
    others["_id"] = "others"
    # 488500 是所有文档数目，减去前8位用户贡献的文档，就是其他人贡献的
    others["count"] = 488500 - sum
    dict_list.append(others)
    
    pprint.pprint(dict_list)
```

    [{'_id': 'futurumspes', 'count': 265385},
     {'_id': 'kawah64', 'count': 37233},
     {'_id': 'Ryo-a', 'count': 20083},
     {'_id': 'Nuko', 'count': 14077},
     {'_id': 'hayashi', 'count': 13189},
     {'_id': 'ribbon', 'count': 12811},
     {'_id': 'kurauchi', 'count': 10178},
     {'_id': 'indyKK', 'count': 8356},
     {'_id': 'others', 'count': 107188}]
    


```python
def get_labels_values_from_dictlist(dict_list):
    labels = []
    sizes = []
    
    for row in dict_list:
        labels.append(row["_id"])
        sizes.append(row["count"])
    
    return labels,sizes
```


```python
import matplotlib.pyplot as plt
import numpy as np

labels,sizes = get_labels_values_from_dictlist(dict_list)
print(labels)
print(sizes)

# starttangle指第一个饼起始旋转的角度，逆时针旋转
plt.pie(sizes,labels=labels,autopct='%1.1f%%',
        shadow=True,startangle=90)

plt.show()
```

    ['futurumspes', 'kawah64', 'Ryo-a', 'Nuko', 'hayashi', 'ribbon', 'kurauchi', 'indyKK', 'others']
    [265385, 37233, 20083, 14077, 13189, 12811, 10178, 8356, 107188]
    


![image](https://user-images.githubusercontent.com/18595935/31617909-736b9bdc-b2cb-11e7-835f-26500c23af77.png)




```python
# 不同类型的地图，贡献度也不同，区分条件中加入type
def most_user():
    result = db.kawasaki.aggregate([
        {"$group":{"_id":{"user":"$user","type":"$type"},
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":10}
    ])
    return result

if __name__ == "__main__":
    result = most_user()
    for row in result:
        #pass
        pprint.pprint(row)
```

    {'_id': {'type': 'node', 'user': 'futurumspes'}, 'count': 222374}
    {'_id': {'type': 'way', 'user': 'futurumspes'}, 'count': 43011}
    {'_id': {'type': 'node', 'user': 'kawah64'}, 'count': 31345}
    {'_id': {'type': 'node', 'user': 'Ryo-a'}, 'count': 16568}
    {'_id': {'type': 'node', 'user': 'Nuko'}, 'count': 12198}
    {'_id': {'type': 'node', 'user': 'ribbon'}, 'count': 11116}
    {'_id': {'type': 'node', 'user': 'hayashi'}, 'count': 11070}
    {'_id': {'type': 'node', 'user': 'kurauchi'}, 'count': 8353}
    {'_id': {'type': 'node', 'user': 'indyKK'}, 'count': 7120}
    {'_id': {'type': 'node', 'user': 'nyampire'}, 'count': 6656}
    

## 3.2 更新时间分布


```python
from collections import Counter

time_counter = Counter()

def process_time(timestamp,key="year"):
    if key == "year":
        return timestamp[:4]
    if key == "month":
        return timestamp[5:7]
    if key == "hour":
        return timestamp[11:13]
    if key == "weekday":
        pass
    pass
    

def most_time():
    result = db.kawasaki.aggregate([
        {"$group":{"_id":"$timestamp",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}}
    ])
    return result

if __name__ == "__main__":
    result = most_time()
    judge_key = "month"
    sum = 0
    for row in result:
        row["_id"] = process_time(row["_id"],judge_key)
        time_counter[row["_id"]] += row["count"]
        sum += row["count"]
    
    time_counter = time_counter.most_common()
    print(time_counter)
    print(sum)
```

    [('02', 108736), ('03', 107897), ('01', 77523), ('12', 30395), ('05', 30153), ('06', 28304), ('07', 22837), ('04', 19932), ('08', 18515), ('09', 17435), ('11', 13534), ('10', 13239)]
    488500
    


```python
def get_label_values_from_list(time_counter):
    labels = []
    sizes = []
    for item in time_counter:
        labels.append(item[0])
        sizes.append(item[1])
        
    return labels,sizes

labels,sizes = get_label_values_from_list(time_counter)

# starttangle指第一个饼起始旋转的角度，逆时针旋转
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)

plt.show()
```


![image](https://user-images.githubusercontent.com/18595935/31617940-9101f222-b2cb-11e7-9acf-c1bf054c88b4.png)


## 3.3 餐馆种类


```python
def most_food():
    result = db.kawasaki.aggregate([
        {"$match":{"tag.amenity":{"$exists":1},
                 "tag.amenity":{"$in":["fast_food","restaurant"]},
                  "tag.cuisine":{"$exists":True}
                  }},
        {"$group":{"_id":"$tag.cuisine",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":10}
    ])
    return result

food_counter = Counter()
dict_label={"ramen":"noodle","noodle;ramen":"noodle","chicken":"broiled meat","barbecue":"broiled meat"}

if __name__ == "__main__":
    sum = 0
    result = most_food()
    for row in result:
        try:
            food_label = dict_label[row["_id"]]
            food_counter[food_label] += row["count"]
        except:
            food_label = row["_id"]
            food_counter[food_label] += row["count"]
    
    food_counter = food_counter.most_common()
    print(food_counter)
```

    [('noodle', 61), ('japanese', 50), ('chinese', 40), ('sushi', 27), ('burger', 26), ('broiled meat', 16), ('italian', 11)]
    


```python
def get_label_values_from_list(food_counter):
    labels = []
    sizes = []
    for item in food_counter:
        labels.append(item[0])
        sizes.append(item[1])
        
    return labels,sizes
labels,sizes = get_label_values_from_list(food_counter)
print(labels)
print(sizes)

# starttangle指第一个饼起始旋转的角度，逆时针旋转
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)

plt.show()
```

    ['noodle', 'japanese', 'chinese', 'sushi', 'burger', 'broiled meat', 'italian']
    [61, 50, 40, 27, 26, 16, 11]
    


![image](https://user-images.githubusercontent.com/18595935/31617961-9e504528-b2cb-11e7-8a26-8178ecc738c2.png)


## 3.4 地物种类分布


```python
def most_cat():
    result = db.kawasaki.aggregate([
        {"$match":{"tag.amenity":{"$exists":1}}},
        {"$group":{"_id":"$tag.amenity",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":10}
    ])
    return result

food_counter = Counter()

if __name__ == "__main__":
    sum = 0
    result = most_cat()
    for row in result:
        print(row)
```

    {'_id': 'parking', 'count': 3635}
    {'_id': 'restaurant', 'count': 376}
    {'_id': 'drinking_water', 'count': 321}
    {'_id': 'school', 'count': 290}
    {'_id': 'toilets', 'count': 261}
    {'_id': 'kindergarten', 'count': 230}
    {'_id': 'place_of_worship', 'count': 207}
    {'_id': 'social_facility', 'count': 186}
    {'_id': 'fast_food', 'count': 183}
    {'_id': 'pub', 'count': 126}
    

## 3.5 中国餐馆


```python
def most_cat():
    result = db.kawasaki.aggregate([
        {"$match":{"tag.cuisine":"chinese"}},
        {"$group":{"_id":"$tag.name",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":100}
    ])
    return result

food_counter = Counter()

if __name__ == "__main__":
    sum = 0
    result = most_cat()
    for row in result:
        print(row)
```

    {'_id': 'バーミヤン', 'count': 3}
    {'_id': 'GYOZA', 'count': 1}
    {'_id': '如家飯店', 'count': 1}
    {'_id': '珍味楼', 'count': 1}
    {'_id': '粥菜坊', 'count': 1}
    {'_id': '珍々亭 (Chin Chin Tei)', 'count': 1}
    {'_id': '満園', 'count': 1}
    {'_id': 'バーミヤン 北加瀬店', 'count': 1}
    ...
    
