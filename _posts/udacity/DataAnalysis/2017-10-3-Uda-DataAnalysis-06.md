---
layout: post
title: Uda-DataAnalysis-06-数据质量
date: 2017-10-3 00:00:00
categories: 数据分析
tags: DataAnalysis
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的6,7 关于数据质量的总结。 
> 要完成本章，起始更重要的是python的应用。
> 


# 06-11 练习审查交叉字典的约束条件

数据中的某些字段存在关联关系，通过对这些关联关系的验证，将可疑数据取出。


```python
import csv
import math

def skip_lines(input_file,skip):
    for i in range(0,skip):
        next(input_file)


# 检查一个字符串是否数值
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

#  返回一个字符串的浮点数形式
def ensure_float(v):
    if is_number(v):
        return float(v)
    
# 根据面积，人口，以及人口密度计算并输出可疑记录
def audit_population_density(input_file):
    for row in input_file:
        population = ensure_float(row['populationTotal'])
        area = ensure_float(row['areaLand'])
        population_density = ensure_float(row['populationDensity'])
        if population and area and population_density:
            calculated_density = population / area
            if math.fabs(calculated_density - population_density) > 10:
                print "bad guy:",row['name'],":",calculated_density,":",population_density

if __name__ == '__main__':
    input_file = csv.DictReader(open('cities.csv'))
    skip_lines(input_file,3)
    audit_population_density(input_file)
```

# 06-12 修正有效性

检查 DBPedia 自动数据文件的“productionStartYear”并获取有效的值。应该完成以下任务：
-    检查字段“productionStartYear”是否包含年份
-    检查该年份是否在 1886 至 2014 范围内
-    将字段值转换为年份（而不是整个日期时间）
-    字段的其他部分和值应该保持不变
-    如果字段的值是如上所述范围内的有效年份，则将该行写入 output_good 文件中
-    如果字段的值不是如上所述的有效年份，则将该行写入 output_bad 文件中
-    你应该采用提供的数据读取和写入方式（DictReader 和 DictWriter），它们将会对标题进行处理。


```python
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'
```


```python
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def process_file(input_file, output_good, output_bad):
    # store data into lists for output
    data_good = []
    data_bad = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        # 取出文件头
        header = reader.fieldnames
        for row in reader:
            # validate URI value
            if row['URI'].find("dbpedia.org") < 0:
                continue

            ps_year = row['productionStartYear'][:4]
            try: # use try/except to filter valid items
                ps_year = int(ps_year)
                row['productionStartYear'] = ps_year
                if (ps_year >= 1886) and (ps_year <= 2014):
                    data_good.append(row)
                else:
                    data_bad.append(row)
            except ValueError: # non-numeric strings caught by exception
                if ps_year == 'NULL':
                    data_bad.append(row)

    # Write processed data to output files
    with open(output_good, "w") as good:
        # fieldnames设定文件头
        writer = csv.DictWriter(good, delimiter=",", fieldnames= header)
        # 写文件头
        writer.writeheader()
        for row in data_good:
            writer.writerow(row)

    with open(output_bad, "w") as bad:
        writer = csv.DictWriter(bad, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in data_bad:
            writer.writerow(row)       
        
def test():
    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)

if __name__ == "__main__":
    test()
```

处理上面文件时，会空一行出来，如果是python3中的话，用newline进行处理，参考 https://docs.python.jp/3/library/csv.html


# 练习1 审查数据质量

在第一道练习中，请审核数据集中某些特定字段中的数据类型。
值类型可以是：
-    NoneType，如果值是字符串“NULL”或空字符串“”
-    列表，如果值以“{”开头
-    整型，如果值可以转型为整型
-    浮点型，如果值可以转型为浮点型，但是无法转型为整型。

例如，“3.23e+07”应该被当做浮点型，因为可以转型为浮点型，但是int('3.23e+07') 将抛出 ValueError

-    “str”，表示其他所有值


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

# 添加一个专门判断类型的函数
def judge_type(field):
    # 判断是否为空
    if (field == "") or (field == "NULL"):
        return type(None)
    # 是否为列表
    if field.startswith("{"):
        return type([])
    try:
        # 判断是否int类型
        field_int = int(field)
        return type(1)
    except ValueError:
        try:
            # 是否float类型
            field_float = float(field)
            return type(1.1)
        except ValueError:
            # 都不是则返回str类型
            return type(str())


def audit_file(filename, fields):
    fieldtypes = {}
    # 初始化fieldtypes
    for field_key in FIELDS:
        fieldtypes[field_key] = set()

    # YOUR CODE HERE
    with open(CITIES, "r") as f:
        reader = csv.DictReader(f)
        # 取出文件头
        header = reader.fieldnames
        for row in reader:
            # validate URI value
            if row['URI'].find("dbpedia.org") < 0:
                continue
            for field_key in FIELDS:
                field = row[field_key]
                field_type = judge_type(field)
                fieldtypes[field_key].add(field_type)

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    #assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    #assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    print judge_type("stre4233")
    test()
```

    <type 'str'>
    {'areaCode': set([<type 'int'>,
                      <type 'list'>,
                      <type 'NoneType'>,
                      <type 'str'>]),
     'areaLand': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'areaMetro': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'areaUrban': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'elevation': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'governmentType_label': set([<type 'list'>, <type 'NoneType'>, <type 'str'>]),
     'homepage': set([<type 'list'>, <type 'NoneType'>, <type 'str'>]),
     'isPartOf_label': set([<type 'list'>, <type 'NoneType'>, <type 'str'>]),
     'maximumElevation': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'minimumElevation': set([<type 'float'>, <type 'NoneType'>]),
     'name': set([<type 'list'>, <type 'NoneType'>, <type 'str'>]),
     'populationDensity': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'populationTotal': set([<type 'int'>, <type 'list'>, <type 'NoneType'>]),
     'timeZone_label': set([<type 'list'>, <type 'NoneType'>, <type 'str'>]),
     'utcOffset': set([<type 'float'>,
                       <type 'int'>,
                       <type 'list'>,
                       <type 'NoneType'>,
                       <type 'str'>]),
     'wgs84_pos#lat': set([<type 'float'>, <type 'list'>, <type 'NoneType'>]),
     'wgs84_pos#long': set([<type 'float'>, <type 'list'>, <type 'NoneType'>])}
    

# 练习3 修复区域
计算面积，上面的areaLand字段，有几种不同的类型，如果是无法计算正确的值，返回None。


```python
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

# 添加一个专门判断类型的函数
def judge_type(field):
    # 判断是否为空
    if (field == "") or (field == "NULL"):
        return type(None)
    # 是否为列表
    if field.startswith("{"):
        return type([])
    try:
        # 判断是否int类型
        field_int = int(field)
        return type(1)
    except ValueError:
        try:
            # 是否float类型
            field_float = float(field)
            return type(1.1)
        except ValueError:
            # 都不是则返回str类型
            return type(str())

# 处理list类型的area，返回一个精度高的浮点数
def fix_list_area(area):
    # 去除{}字符
    area = area.replace("{","")
    area = area.replace("}","")
    
    # 根据分隔符分隔list
    area_list = area.split("|")

    # 取出各个字符长度
    area_list_len = [len(area) for area in area_list]
    # 取出list中最大值的下表
    area_index = area_list_len.index(max(area_list_len))
    
    # 取出大的那个值，比如 ` 5.499999e+07`
    area_real = area_list[area_index]
    
    try:
        return float(area_real)
    except ValueError:
        return None
    
def fix_area(area):
    if (judge_type(area) == type(None)) or (judge_type(area) == type(str())):
        area = None
    elif judge_type(area) == type(1) :
        area = int(area)
    elif judge_type(area) == type(1.1):
        area = float(area)
    # 如果是列表的话，还需要进行特殊处理
    elif judge_type(area) == type([]):
        area = fix_list_area(area)
    else:
        area = None
        
    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #直接跳过三行数据
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(0,10):
        pprint.pprint(data[n]["areaLand"])

#    assert data[3]["areaLand"] == None        
#    assert data[8]["areaLand"] == 55166700.0
#    assert data[20]["areaLand"] == 14581600.0
#    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()
```

    Printing three example results:
    1213
    54907700.0
    None
    None
    None
    54999999.6
    None
    None
    1213
    None
    

# 练习5：修复姓名

处理姓名数据，将其变成列表，如果姓名为NULL，则列表为空。


```python
import codecs
import csv
import pprint

CITIES = 'cities.csv'


def fix_name(name):
    if name == "NULL":
        return []
    
    name = name.replace("{","")
    name = name.replace("}","")
    
    name_list = name.split("|")
    return name_list


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #头三行数据是多余的，跳过
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)
    return data


def test():
    data = process_file(CITIES)

    print "Printing 20 results:"
    for n in range(20):
        pprint.pprint(data[n]["name"])

    #assert data[14]["name"] == ['Negtemiut', 'Nightmute']
    #assert data[9]["name"] == ['Pell City Alabama']
    #assert data[3]["name"] == ['Kumhari']

if __name__ == "__main__":
    test()
```

    Printing 20 results:
    ['Kud']
    ['Kuju']
    ['Kumbhraj']
    ['Kumhari']
    ['Kundagola', 'Kundgol ???????????']
    ['Kunigal']
    ['Kunzer']
    ['Kurduvadi', '???????????????']
    ['Kurgunta']
    ['Kurinjipadi']
    ['Kurud']
    ['Kushtagi']
    ['Ladnun', '?????????']
    ['Lahar', '??????']
    ['Laharpur']
    ['Lakheri']
    ['Lakhipur']
    ['Laksar', '????????']
    ['Lalkuan']
    ['Lalsot']
    

# 练习6：交叉字段审查

 "point"字段，似乎是"wgs84_pos#lat" 和 "wgs84_pos#long"字段的组合，但是不太确定，这里需要进行判断，我们将point字段拆开，然后分别进行判断。


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pprint

CITIES = 'cities.csv'


def check_loc(point, lat, longi):
    try:
        point_lat = point.split(" ")[0]
        point_longi = point.split(" ")[1]
        
        if ( float(point_lat) == float(lat)) and (float(point_longi) == float(longi)):
            return True
        else:
            return False
    except:
        return False


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra matadata
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to check the location
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print "{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            data.append(line)

    return data


def test():
    print check_loc("33.083 75.28", "33.08", "75.28")
    #assert check_loc("33.08 75.28", "33.08", "75.28") == True
    #assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") == False

if __name__ == "__main__":
    test()
```

    False
    
