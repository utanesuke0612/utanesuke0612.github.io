---
layout: post
title: Uda-DataAnalysis-19-案例研究-通过OpenStreetMap了解数据审查清洗
date: 2017-10-8 08:00:00
categories: Uda-数据分析进阶
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的的19通过一个案例，了解如何审查清洗和准备OpenStreetMap数据。
> 


相关格式文档，参考：

1. http://wiki.openstreetmap.org/wiki/Main_Page

2. http://wiki.openstreetmap.org/wiki/OSM_XML

# 3. 练习 迭代解析

要求解析出各个标签的标签名，以及各个标签的数目。

下面的代码虽然解析出来了，但是代码写得没有扩展性，在判断某个节点有没有子节点的时候，这里是知道文件结构，所以判断了两层。

另外，下面的效率也不行，要是读个2G的文件，内存早爆胎了。


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    tags = {}
    # 根节点的tag取出来
    tags[root.tag] = 1
    
    # 循环第一层子节点
    for child in root.findall("./"):
        label = child.tag
        
        # 判断是否在tags的key中了，在的话，数量加1
        if label in tags.keys():
            tags[label] = tags[label] + 1
        # 不在的话，新建一个
        else:
            tags[label] = 1
     
        # 再循环一层，做相同的判断
        if child.findall("./"):
            for child_01 in child:
                label_child = child_01.tag
                if label_child in tags.keys():
                    tags[label_child] = tags[label_child] + 1
                else:
                    tags[label_child] = 1
    
    return tags


def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

if __name__ == "__main__":
    test()
```

    输出:{'bounds': 1,
	     'member': 3,
	     'nd': 4,
	     'node': 20,
	     'osm': 1,
	     'relation': 1,
	     'tag': 7,
	     'way': 1}
    

下面是上面方法的改进版，直接一次性取出所有的标签tag，但是还是很占用内存啊，没有像视频中说的省内存。


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    tags = {}
    
    for event,elem in ET.iterparse(filename,events=("start",)):
        if elem.tag in tags.keys():
            tags[elem.tag] = tags[elem.tag] + 1
        else:
            tags[elem.tag] = 1
    return tags


def test():

    tags = count_tags('example.osm')
    #tags = count_tags('E:\udacity-data\chicago_illinois.osm')
    pprint.pprint(tags)

if __name__ == "__main__":
    test()
```

    {'bounds': 1,
     'member': 3,
     'nd': 4,
     'node': 20,
     'osm': 1,
     'relation': 1,
     'tag': 7,
     'way': 1}
    

# 6. 循环访问道路标签

street_types = defaultdict(set)  十分方便的创建字典的方法，这样就不用检查key是否重复了。


```python
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osm_file = open("E:\udacity-data\example.osm","r")

street_type_re = re.compile(r'\b\S+\.?$',re.IGNORECASE)
street_types = defaultdict(set)

expected = ["Street","Avenue","Boulevard","Drive","Court","Place"]

def audit_street_type(street_types,street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys,key=lambda s:s.lower())
    for k in keys:
        v = d[k]
        print "%s:%d" % (k,v)

# 判断道路数据中的属性，是不是 addr:street
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

# 
def audit():
    for event,elem in ET.iterparse(osm_file,events=("start",)):
        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types,tag.attrib['v'])
                    pass
    pprint.pprint(dict(street_types))


if __name__ == "__main__":
    audit()
    
```

    输出： {'service': set(['service'])}
    

# 7. 练习:标签类型


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    flag = 0
    if element.tag == "tag":
        for tag in element.iter("tag"):
            #if tag.attrib['k'] == "addr:street":
                if re.search(lower, element.attrib["k"]):
                    keys["lower"] += 1
                    print element.attrib["k"]
                    return keys
                if re.search(lower_colon, element.attrib["k"]):
                    keys["lower_colon"] += 1
                    print element.attrib["k"]
                    return keys
                if re.search(problemchars, element.attrib["k"]):
                    keys["problemchars"] += 1
                    print element.attrib["k"]
                    return keys
                
                print element.attrib["k"]
                keys["other"] += 1
                
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()
```

    {'lower': 0, 'lower_colon': 0, 'other': 0, 'problemchars': 0}
    

# 8. 探索用户

element.attrib 返回一个element的所有属性和值，是一个dict


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        # 
        #pprint.pprint(element.attrib)
        #pprint.pprint(element.tag)
        if "uid" in element.attrib.keys():
            #print element.attrib["uid"]
            users.add(element.attrib["uid"])

    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    #assert len(users) == 6



if __name__ == "__main__":
    test()
```

    输出: set(['1219059', '147510', '26299', '451048', '567034', '939355'])
    

# 11. 练习，完善街道名


```python
# 用mapping中的对应表，替换道路名中的简写为全称

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "example.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Rd.": "Road",
            "Ave": "Avenue",
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            #print street_type
            #print street_name
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

# 完善街道名
def update_name(name, mapping):
    # 先用正则表达式找出name中的最后部分
    m = street_type_re.search(name)
    before_str = m.group()
    
    # 这里的最后部分是简写，需要获取简写对应的全称
    after_str = mapping[before_str]
    
    # 用全称替换简写
    name = name.replace(before_str,after_str)

    return name


def test():
    st_types = audit(OSMFILE)
    #assert len(st_types) == 3
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            #print name, "=>", better_name
            #if name == "West Lexington St.":
            #    assert better_name == "West Lexington Street"
           # if name == "Baldwin Rd.":
           #     assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()
```

# 12. 练习: 准备数据库:MongoDB

最终输出的data，应该是类似如下dict的一个list，字典的生成规则，具体参考课程17的要求。

```python
{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}
```


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        # 
        if "id" in element.attrib.keys():
            node["id"] = element.attrib['id']
        node["type"] = element.tag
        if "visible" in element.attrib.keys():
            node["visible"] = element.attrib['visible']
        
        # 处理created
        created_dict = {}
        created_dict['version'] = element.attrib['version']
        created_dict['changeset'] = element.attrib['changeset']
        created_dict['timestamp'] = element.attrib['timestamp']
        created_dict['user'] = element.attrib['user']
        created_dict['uid'] = element.attrib['uid']
        
        node["created"] = created_dict
        
        # 如果是node类型
        if element.tag == "node":
            pos = []
            pos.append(float(element.attrib['lat']))
            pos.append(float(element.attrib['lon']))
            node['pos'] = pos
            
        # 如果是way类型
        if element.tag == "way":
            # 先处理nd 标签
            node_list = []
            for nd in element.iter("nd"):
                node_list.append(nd.attrib['ref'])
            
            node["node_refs"] = node_list
            
            # 再处理 tag标签
            address = {}
            for tg in element.iter("tag"):
                k_str = tg.attrib['k']
                #print k_str
                
                # 如果k标签中的有问题字符，则跳过本条数据
                if re.search(problemchars, k_str):
                    continue
                
                # 如果是以addr:开头的
                if k_str.startswith("addr:"):
                    k_str_item = k_str.split(":")
                    if len(k_str_item) == 2:
                        address[k_str_item[1]] = tg.attrib['v']

            if address != {}:
                node["address"] = address
            
            pass
            
        
        return node
    else:
        return None

# 将处理后的字典，写入json文件
def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def test():
    data = process_map('example.osm', True)
    pprint.pprint(data)
    
    correct_first_elem = {
        "id": "261114295", 
        "visible": "true", 
        "type": "node", 
        "pos": [41.9730791, -87.6866303], 
        "created": {
            "changeset": "11129782", 
            "user": "bbmiller", 
            "version": "7", 
            "uid": "451048", 
            "timestamp": "2012-03-28T18:31:23Z"
        }
    }

if __name__ == "__main__":
    test()
```

    输出: [{'created': {'changeset': '11129782',
                  'timestamp': '2012-03-28T18:31:23Z',
                  'uid': '451048',
                  'user': 'bbmiller',
                  'version': '7'},
      'id': '261114295',
      'pos': [41.9730791, -87.6866303],
      'type': 'node',
      'visible': 'true'},
     {'created': {'changeset': '8448766',
                  'timestamp': '2011-06-15T17:04:54Z',
                  'uid': '451048',
                  'user': 'bbmiller',
                  'version': '6'},
      'id': '261114296',
      'pos': [41.9730416, -87.6878512],
      'type': 'node',
      'visible': 'true'},
     ...
     {'created': {'changeset': '20187382',
                  'timestamp': '2014-01-25T02:01:54Z',
                  'uid': '1219059',
                  'user': 'linuxUser16',
                  'version': '1'},
      'id': '258219703',
      'node_refs': ['2636086179', '2636086178', '2636086177', '2636086176'],
      'type': 'way',
      'visible': 'true'}]
    
 
