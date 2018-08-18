---
layout: post
title: Uda-DataAnalysis-项目1-分析OpenStreetMap的OSM数据
date: 2017-10-8 20:00:00
categories: 数据分析
tags: MongoDB DataAnalysis 
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的项目1：分析OSM地图数据的总结。 
> 

# 1. 数据准备

- 利用[url](http://www.openstreetmap.org/export#map=14/35.5460/139.6937)选取区域(日本：左下角:横滨港北，右上角:大森北)

- 利用上面选取的区域经纬度，确定API Query:
`(node(35.5146,139.6262,35.5772,139.7611);<;);out meta;`

- [url](http://overpass-api.de/query_form.html)中输入上面的API Query下载数据。

- 最终数据大小:97M

# 2. 进一步理解数据格式

理解数据格式，作成数据格式概略结构，参考[here](https://1drv.ms/b/s!Ald1cKESY1BDgcZLoBn6nHlH1Slv1Q)。

# 3. 地图概要:

由node，way，relation三类数据构成，分别对应点，线，面。

```python
node, 410783
way, 77420
relation, 297
```

是一个如下的矩形，其面积相当于东京的5个新宿区，然而只有北京海淀区的1/5 :
```python
长:6.96KM  宽:12.20KM  面积：84.97平方KM
```

[代码](#91-地图构成:)

# 4. 待处理的数据问题:


- 邮政编码格式不统一，另外有错误数据。比如，一部分邮编格式为 `2100822`不带`-`分隔，另一部分有`-`分隔，如`210-0003`，还有两类错误数据，分别是不足8位，和带有特殊符号，如下:
```python
144052, 1
〒2100019, 1
```

- 一部分电话号码省略了区号，如`560-3207`等，严格说并不属于错误，而且这类数据无法程序修正。

- 数据分类不正确，比如，都是医院，但是数据中部分使用`hospital`分类，还有使用`doctors`分类，以及`clinic`通过抽取实际数据调查，实际都是同等规模的医院。

```python
    <tag k="amenity" v="doctors"/>
    <tag k="name" v="かめだこともクリニック"/>
    和
    <tag k="amenity" v="hospital"/>
    <tag k="name" v="ふたば歯科クリニック 蒲田院"/>
    和 
    <tag k="amenity" v="clinic"/>
    <tag k="description" v="8F"/>
    <tag k="name" v="アルファメディック クリニック"/>
    
```

     另外，有专门的牙医dentist分类，却使用了hospital分类。

```python
    <tag k="amenity" v="hospital"/>
    <tag k="name" v="久米歯科"/>
```


- 道路宽度`est_width`，后续用的"3.0m〜5.5m"形式表示，如果用于道路计算的话，最好是拆开为两个，分别是est_width_min和est_width_max，比如:

```python
    <tag k="est_width" v="3.0m〜5.5m"/>
```

     拆分后:

```python
    <tag k="est_width_min" v="3.0"/>
    <tag k="est_width_max" v="5.0"/>
```


- housenumber以及addr:block_number中存在全角数字。(其他地方还存在全角字符，只是显示是不存在问题，但如果是housenumber或blocknumber等用于检索的话，可能产生无法检索的问题)

```python
    <tag k="addr:housenumber" v="１１−１９"/>
    以及
    <tag k="addr:block_number" v="１"/>
    <tag k="addr:city" v="川崎市"/>
    <tag k="addr:housenumber" v="１"/>
```

[代码](#92-数据中的问题)

# 5. 清理数据

## 5.1 处理邮政编码

邮政编码处理原则:
1. 去除邮编中的分割线-，节省数据量。
2. 位数不对的邮编，修改为空。
3. 去除数字以外的字符。

[代码](#93-处理邮政编码)

## 5.2 处理医院的分类错误

医院的分类错误，无法全部处理，大部分需要靠人工去判断。只针对如下情况进行处理:
- 如果amenity是["hospital","doctors","clinic"]，但是name中包含了`歯科`，则将amenity修改为`dentist`。
下面是找出来的错误数据：

```python
{'amenity': 'hospital', 'name': '久米歯科'}
{'amenity': 'hospital', 'name': '島田歯科医院'}
{'amenity': 'hospital', 'name': 'ふたば歯科クリニック 蒲田院'}
{'amenity': 'hospital', 'name': '山田歯科'}
```


[代码](#94-处理医院分类错误)

## 5.3 处理道路宽度数据

所有的道路宽度est_width和yh:WIDTH类别，以及对应数量如下：

```python
3.0m〜5.5m,3219
5.5m〜13.0m,140
1.5m〜3.0m,44
2.0m〜5.5m,2
5.5-13.0,1
```

按如下步骤进行处理:
- 去除字母
- 将-替换为〜
- 用〜对字符串进行分割
- 分割后的第一个宽度，生成一个新的element:如`est_width_min`
- 分割后的第二个宽度，生成一个新的element:如`est_width_max`

处理前:
```
{'k': 'est_width', 'v': '3.0m〜5.5m'}
```
处理后:
```
{'k': 'est_width_min', 'v': 3.0}
{'k': 'est_width_max', 'v': 5.5}
```
[代码](#95-处理道路宽度)

## 5.4 处理housenumber以及block_number中混入的全角数字

Housenumber中还存在很多其他问题，比如有的是地址的全称，或是存储的区以下的地址。HouseNumber这个概念在日本很少人使用，通常用行政区划地址定位，没有像欧美地址的```**路**号```的名称。下面只对HouseNumber和block_number进行有限的处理:

- 将数字的全角转换成半角。(其他字符不予处理)
- HouseNumber中类似`12号`的，即前面是数字，后面是汉字`号`的情况下，只保留数字。

```python
1.处理前:１１−１９
1.处理后:11−19

2.处理前:1号
2.处理后:1
```

[代码](#96-处理HouseNumber的全半角)

# 6. 数据重组织-生成json-导入MongoDB

## 6.1 Json文件结构:

- pos 只有node类型的时候才存在
- nd 只有way类型时才存在
- member 只有relation类型时才存在

```python
dict1
    id:
    pos:(lat,log)
    version:
    timestamp
    changeset
    uid
    user
    
    type:(node|way|relation)
    
    tag:
        attrib[k]:attrib[v]
        attrib[k]:attrib[v]
        attrib[k]:attrib[v]
        ...
    
    nd:[ref1,ref2,ref3...]
    
    member:
          [type,ref,role]  
          [type,ref,role]  
          ...

dict2
...

dictN

```

## 6.2 运行`pj1-py3-all`，生成json文件
程序执行思路如下:

1. 读取XML文件(清理-处理各个tag构造dict的list数据结构)
2. 将上面构造的dict的list对象，写入json文件。

## 6.3 将json导入MongoDB

```python
C:\Users\utane\OneDrive\udacity\20-p-01-Project>mongoimport --db mydb --collection kawasaki --type json --file kawasaki.osm.json
2017-10-15T09:54:56.473+0900    imported 488500 documents
```

经验证，文档条数，与最初OSM文件中node/way/relation中的总数是一致的，转换或导入过程中没有文档丢失。

# 7. 利用MongoDB对数据进行分析

## 7.1 用户贡献度分析:

(1). 411位用户贡献了地图:
    
```python
> db.kawasaki.distinct("user").length
411
```

(2). user贡献的地图文档数量

```python
> db.kawasaki.find({"user":{"$ne":null}}).count()
488500
```

(3). 贡献度前8位的用户，一共贡献了381,312条文档，即不到2%的用户，贡献了接近80%的地图数据：

```python
def most_user():
    result = db.kawasaki.aggregate([
        {"$group":{"_id":"$user",
                  "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":8}
    ])
    return result
```

结果如下:

![image](https://user-images.githubusercontent.com/18595935/31580981-929bdb44-b199-11e7-85d9-fef98e47ca72.png)



## 7.2 地图新鲜度分析

将文档中的timestamp中的年份抽取出来，分析地图的最后更新年份，结果如下，2016年和2017年更新的数据占了一半以上：
![image](https://user-images.githubusercontent.com/18595935/31581368-e0a05828-b1a4-11e7-88fc-a0ba95e9f299.png)

## 7.3 地图更新月份分布

60%以上的更新，集中在1,2,3月份：
![image](https://user-images.githubusercontent.com/18595935/31581934-570a924c-b1b1-11e7-95df-18422f7a5cbb.png)

## 7.4 餐馆分类分布

首先过滤掉了餐馆中没有分类信息的数据，再按照cuisine进行分类，最终结果如下，前三位分别是 拉面 / 日本菜 / 中国菜:

![image](https://user-images.githubusercontent.com/18595935/31582335-7a26efdc-b1bb-11e7-84e3-59c73884ccda.png)

另外，中餐馆中按照餐馆名排列如下，第一位是一家连锁店:

```python
{'_id': 'バーミヤン', 'count': 3}
{'_id': 'GYOZA', 'count': 1}
{'_id': '如家飯店', 'count': 1}
{'_id': '珍味楼', 'count': 1}
{'_id': '粥菜坊', 'count': 1}
```

[代码](#97-餐厅的种类分布)

## 7.5 该区域内地物种类分布

如下是地物分类，以及对应的数目，其中比较日本特色的是:

- `drinking_water`饮水点，在大小公园里都会设有很多饮水点，日本的自来水是饮用水级别。
- `toilets`，公共厕所很多。
- `telephone`，即使手机都普及了，但还是有很多公用电话亭，一方面拆除成本高，另一方面还是有用户在使用，特别是如果发生地震，手机过于拥堵几乎打不出去，这种时候就只能靠公用电话。
- `library`，21个图书馆，平均4平方公里一个图书馆，自行车15分钟内能找到一个图书馆。

```python
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
{'_id': 'bench', 'count': 123}
{'_id': 'telephone', 'count': 114}
{'_id': 'pharmacy', 'count': 100}
...
{'_id': 'library', 'count': 21}
```

# 8. 结论与改进意见:

## 8.1 结论

总体上来说，作为一份共同编辑的地图数据，其准确度比较高，没有发现恶作剧式的错误数据。但也是因为是共同编辑的地图数据，存在如下的问题:

1. 没有统一的数据录入规则，同一类地物，可能由于不同人的理解不同，分类也不同，导致后续使用不便。
2. 数据不全，体现在数据中的属性不全，以及地物没有录入。
3. 数据较新，大部分的更新时间集中在2016年和2017年。

## 8.2 改进意见与实施分析

(1). 针对地物分类问题的问题，考虑有如下的改进意见：

在数据录入的时候，取消自定义分类的输入，只能在给定的分类中选取。将分类做得更加细化，另外将现在的单级分类修改为多级分类，比如大分类为餐厅，中分类为西餐，中餐，日本餐厅，小分类分为寿司，拉面等。

- **advantage**：理论上能提高分类精度。

- **disadvantage**：需要修改既有网站UI，增加成本，另外增加了分类的选取难度，可能会打消用户添加数据的积极性，或是找不到分类的话会任意选一个，使得数据质量反而恶化。

(2). 针对数据不全的问题，将一些热门车站周边的POI点数据，通过爬虫在其他网站上爬取下来后，显示在该车站的位置，提示地图的贡献者，希望他们把这些POI点放到正确的位置上。

- **advantage**：能进一步补全数据。

- **disadvantage**：爬虫的开发和既有网站UI的修改，都会增加成本。

(3). 邮政编码的错误，网站中添加输入判断，不正确的邮政编码不允许录入。

(4). 数字的全角半角问题，网站中添加处理，即使地图贡献者在输入全角后，网站的服务器端也能将全角处理成半角后再存储。

# 9. 参考代码

## 9.1 地图构成:

根据经纬度计算距离，需要安装geopy库 `pip install geopy `。

```python
from geopy.distance import great_circle
from xml.etree.ElementTree import parse
from collections import Counter

tag_counter = Counter()
lat_pt_set = set()
lon_pt_set = set()

doc = parse("kawasaki.osm")

# 循环第一层子节点
for item in doc.iterfind("./"):
    tag_counter[item.tag] += 1
    # 如果是node，将经纬度取出
    if item.tag == "node":
        lat_pt_set.add(float(item.attrib['lat']))
        lon_pt_set.add(float(item.attrib['lon']))
        
for tag,num in tag_counter.most_common():
    print("{},{}".format(tag,num))

# 计算矩形面积
p00 = (min(lat_pt_set),min(lon_pt_set))
p10 = (max(lat_pt_set),min(lon_pt_set))
p11 = (max(lat_pt_set),max(lon_pt_set))
row_distance = great_circle(p00, p10).kilometers
col_distance = great_circle(p10, p11).kilometers

myarea = row_distance * col_distance

print("长:{0:.2f}KM  宽:{1:.2f}KM  面积：{2:.2f}平方KM".format(row_distance,col_distance,myarea))

```

## 9.2 数据中的问题

- 邮政编码

```python
from xml.etree.ElementTree import parse
from collections import Counter

postcode_counter = Counter()

doc = parse("kawasaki.osm")

# 循环node下的子元素
for item in doc.iterfind("./node/"):
    if item.attrib["k"] == "addr:postcode":
        # 将邮编中的-去掉
        item.attrib["v"] = item.attrib["v"].replace("-","")
        # 查询邮编长度是否符号要求
        if len(item.attrib["v"]) != 7:
            postcode_counter[item.attrib["v"]] += 1

for tag,num in postcode_counter.most_common():
    print("{},{}".format(tag,num))
```

- 电话号码

```python
from xml.etree.ElementTree import parse
from collections import Counter

node_k_counter = Counter()

doc = parse("kawasaki.osm")

# 循环node下的子元素
for item in doc.iterfind("./node/"):
    if item.attrib["k"] == "phone":
        # 如果电话号码不足给定的位数
        if len(item.attrib["v"]) < 9:
            node_k_counter[item.attrib["v"]] += 1

for tag,num in node_k_counter.most_common():
    print("{},{}".format(tag,num))
```

## 9.3 处理邮政编码

```python
import re

def clean_zipcode(zipcode):
    # 去除数字以外的字符
    newzipcode = re.sub(u"\D",u"",zipcode)
    
    # 如果邮政编码长度不为7，则置空
    if not len(newzipcode) == 7:
        newzipcode = ""
    
    return newzipcode
```

## 9.4 处理医院分类错误

```python
import xml.etree.cElementTree as ET
import io

osm_file = open("kawasaki.osm","r",encoding="utf8")

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

for event,elem in ET.iterparse(osm_file,events=("start",)):
    if audit_dentist(elem):
        for tag in elem.iter("tag"):
                print("{},{}".format(tag.attrib['k'],tag.attrib['v']))
        print("\n")
```

## 9.5 处理道路宽度

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import io
import re
from collections import Counter
import copy
import pprint

est_width_counter = Counter()
osm_file = open("highway.osm","r",encoding="utf8")

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

# 处理后的验证
for event,elem in ET.iterparse(osm_file,events=("start",)):
    if elem.tag in ["node","way","relation"]:
        for item in elem.iter("tag"):
            if item.attrib['k'] in ["est_width","est_width_max","yh:WIDTH_min","yh:WIDTH_max"]:
                print(item.attrib)      
                
    audit_est_width(elem)
    if elem.tag in ["node","way","relation"]:
        for item in elem.iter("tag"):
            if item.attrib['k'] in ["est_width_min","est_width_max","yh:WIDTH_min","yh:WIDTH_max"]:
                print(item.attrib)  
```

## 9.6 处理HouseNumber的全半角

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import io
import re
from collections import Counter
import copy
import pprint

osm_file = open("kawasaki.osm","r",encoding="utf8")

# 全角转半角
def digit_full2half(fullnum):
    try:
        return {"０":"0","１":"1","２":"2","３":"3","４":"4","５":"5",
                "６":"6","７":"7","８":"8","９":"9","ー":"-"}[fullnum]
    except:
        return fullnum

def audit_number_full_half(elem):
    if elem.tag in ["node","way","relation"]:
        for item in elem.iter("tag"):
            if item.attrib["k"] in ["addr:housenumber","addr:block_number"]:
                number = item.attrib["v"]
                if re.match(u"[０-９]",number):
                    new_number = "".join((map(digit_full2half,number)))
                    print("1.处理前:{}".format(number))
                    print("1.处理后:{}".format(new_number))
                    print("\n")
                if re.match(u"^\d号$",number):
                    new_number = number.replace("号","")
                    print("2.处理前:{}".format(number))
                    print("2.处理后:{}".format(new_number))
                    print("\n")
                
# 
for event,elem in ET.iterparse(osm_file,events=("start",)):     
    audit_number_full_half(elem)
```

## 9.7 餐厅的种类分布

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

# 绘图用
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

## 9.8 程序中的注意事项:

- 之前课堂上都是处理英文，不需要关注文字编码，但是要处理汉字的话需要明确指定UTF-8编码，否则乱码。另外，在将dict写入json的时候，要显式将ascii关闭。示例如下:

```python
codecs.open(file_out, "w",encoding="utf-8")

fo.write(json.dumps(el,ensure_ascii=False)+"\n")
```
- Counter 这个数据结构在统计数量时很方便。

- 正则表达式在处理字符串时很强大，还要进一步熟悉。
