---
layout: post
title: Uda-DataAnalysis-01-数据提取基础
date: 2017-09-30 00:00:00
categories: Uda-数据分析进阶
tags: Python Udacity DataAnalysis
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的2,3 数据提取基础的总结。 讲述如何用python提取csv/xls/json等数据。


# 1. `7.解析CSV文件 `，纯python自己解析 

使用纯python解析csv文本文件，要求如下：
1. 逐行读入数据，取前10行
2. 按` ，`拆分每行，然后为每行创建一个字典
3. 第一行是key，后续行是value
4. 使用strip()删除多余的空白

## 1.1 自己写的代码

```python

import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    i = 0
    line_index_list = []
    with open(datafile, "r") as f:
        for line in f:
            # 设定读取最大行数，因为第一行是key，故多一行
            if i == 11:
                break
            
            # 取出数据并去除空格，以及通过逗号分隔为list
            line_after = line.strip()
            line_value_list = line_after.split(",")
            
            line_dict = {}
            
            # 判断，如果是第一行的话，将其作为index行
            if i == 0:
                line_index_list = line_value_list
            # 如果是后续行，则按照value进行处理
            else:
                # 取出index和value的list，赋予到dict的key和value中
                for n in range(len(line_index_list)):
                    line_dict[line_index_list[n]] = line_value_list[n]
                
                # data是list，将字典结构作为list中的元素，追加到list中
                data.append(line_dict)
                
            i = i + 1
    return data

```

## 1.2 示例代码

```python
def uda_parse_file(datafile):
    data = []
    with open(datafile,'rb') as f:
        # 读取第一行文件头作为header ★ 
        header = f.readline().split(",")
        
        # 计数器
        counter = 0
        for line in f:
            if counter == 10:
                break
        
            fields = line.split(',')
            entry = {}
        
            # ★ 使用enumerate函数，将list变成Dict
            for i,value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1
        
    return data
d = uda_parse_file(DATAFILE)

```

## 1.3 示例程序可借鉴点等


1. 将第一行读取单独抽取，读取后作为key。这样程序结构更清晰些。
2. 另外，counter判断的时候也更方便。不会我的程序中需要判断为11，需要加1.
3. 一个字符串，通过split函数分隔为字符串的list
4. 示例程序的命名更加易懂，header / counter / fields / entry等
5. 使用enumerate函数，将list变成Dict，可以获取index作为key。这样的话，就不需要用range的方式循环了。


# 2. `9.使用 CSV 模块 `对上述数据进行解析

## 2.1 示例代码

```python
import csv
import os
import pprint

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile,'rb') as sd:
        # 注意使用的是DicReader，自动将第一行的数据作为key，后续每行的数据作为value
        r = csv.DictReader(sd)
        # r是一个reader，在下面for循环的每一次中去取得一行的数据
        for line in r:
            data.append(line)
    return data

if __name__ == '__main__':
    # os的path.join函数，自动组合为一个全文件路径
    datafile = os.path.join(DATADIR,DATAFILE)
    d = parse_csv(datafile)
    pprint.pprint(d) # pprint 包含一个“美观打印机”,用于生成数据结构的一个美观视图。

```

## 2.2 什么是`if __name__ == ‘__main__’:`

上面的函数中，使用了if __name__ == ‘__main__’:，这个到底是什么意思呢？
简单说，就是用来判断，如果这段代码是被直接执行的话，if后面的就被执行；如果这段代码，是被import到其它代码中，直接执行的是其他代码的话，这段代码就不执行。

- test.py 直接被执行时，if后面的语句也被执行。

```python

print "I'm the first."
print 'test:',__name__
if __name__=="__main__":
    print "I'm the second."

```

输出：

```python

I'm the first.
test: __main__
I'm the second.

```

- 将上面的test.py import到下面的代码中时，上面test.py的if后面的就不被执行。

```python

import test
print "importTest:",__name__

```

输出:

```python

I'm the first.
test: test
importTest: __main__

```

- 如何实现的呢？

` __name__`是每个python模块中都内置的变量，如果是被import的话，name为模块名，比如上面import执行时的` test: test`；如果是直接被执行的话，name为`__main__`，比如上面test.py被执行时的的`test: __main__ `。


# 3. `11.练习:读取Excel文件 `

## 3.1 讲解中的示例程序

```python
import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data#10.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    # 生成器，很简洁的生成一个二维数组
    data = [[sheet.cell_value(r,col)
            for col in range(sheet.ncols)]
               for r in range(sheet.nrows)]
    
    print "\n■■■List Comprehesion"
    print "■data[3][2]:",
    print data[3][2]
    
    # sheet中的属性有nrows和ncols,获取行数和列数
    print "\n■■■Cells in a nested loop:"
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row,col),

    # 直接取出一列的数据，下面是取第一行到第三行的第三列数据
    print "■Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3,start_rowx=1,end_rowx=4)

    # 返回该cell的数据类型，excel与csv不同，可以返回实际的数据类型
    # 1: 文字列 2: 数値  3: 日付
    print sheet.cell_type(1,0)
    exceltime = sheet.cell_value(1,0)

    # 将xlrd的单个浮点的时间值，转换为年/月/日/时/分/秒的元组 (2013, 1, 1, 1, 0, 0)
    print xlrd.xldate_as_tuple(exceltime,0)

    return data

data = parse_file(datafile)


```

## 3.2 练习

```python
import xlrd
import math
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile("{0}.zip".format(datafile),"r") as myzip:
        myzip.extractall()


def parse_file(datafile):
    worokbook = xlrd.open_workbook(datafile)
    sheet = worokbook.sheet_by_index(0)
    
    # 取整个sheet中的数据
    sheet_data = [[sheet.cell_value(r,col)
                  for col in range(sheet.ncols)]
                     for r in range(sheet.nrows)]
    
    # 取第二列的所有数据
    coast_list = sheet.col_values(1,start_rowx=1,end_rowx=sheet.nrows)
    
    maxcoast = max(coast_list)
    mincoast = min(coast_list)
    
    # 计算平均值
    avgcoast = sum(coast_list) / max(len(coast_list),1)
    
    
    # 取第一列的所有数据，除掉第一行，因为第一行是key label
    time_list = sheet.col_values(0,start_rowx=1,end_rowx=sheet.nrows)
    
    # 判断最大值和最小值，找出最大值和最小值对应的时间点
    for n in range(len(time_list)):
        if sheet.cell_value(n, 1) == maxcoast:
            maxtime_ori = sheet.cell_value(n, 0)
            maxtime = xlrd.xldate_as_tuple(maxtime_ori,0)
        if sheet.cell_value(n, 1) == mincoast:
            mintime_ori = sheet.cell_value(n, 0)
            mintime = xlrd.xldate_as_tuple(mintime_ori,0)
    
    print maxtime,mintime

    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    
    data['maxtime'] = maxtime
    data['maxvalue'] = maxcoast
    data['mintime'] = mintime
    data['minvalue'] = mincoast
    data['avgcoast'] = avgcoast
    
    return data

```

## 3.3 练习的示例代码

```python
def parse_file(datafile):
    worokbook = xlrd.open_workbook(datafile)
    sheet = worokbook.sheet_by_index(0)
    
    # 取整个sheet中的数据，★生成器的写法
    sheet_data = [[sheet.cell_value(r,col)
                  for col in range(sheet.ncols)]
                     for r in range(sheet.nrows)]
    
    # 从第一行开始取值，注意后面None的写法
    cv = sheet.col_values(1,start_rowx=1,end_rowx=None) 
    maxval = max(cv) 
    minval = min(cv)
    
    # 通过值获取对应的indx
    maxpos = cv.index(maxval) + 1 # 因为之前取值时  start_rowx=1 第一行是lable，这里也要加1
    minpos = cv.index(minval) + 1 # 通过value取index的方式要记住，numpy和pandas也有类似的操作

    maxtime = sheet.cell_value(maxpos,0)
    mintime = sheet.cell_value(minpos,0)
    
    # https://github.com/python-excel/xlrd/blob/master/xlrd/xldate.py 源代码
    # datemode: 0: 1900-based, 1: 1904-based.
    realmaxtime = xlrd.xldate_as_tuple(maxtime,0) # 处理时间 ★这里后面的0表示date_mode
    realmintime = xlrd.xldate_as_tuple(mintime,0)
    
    data = {
            'maxtime': realmaxtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': sum(cv) / float(len(cv)) # 注意要严谨，前后计算的数值类型一致
    }
    
    return data

parse_file(datafile)

```

## 3.4 代码总结：

1. `sheet.col_values(1,start_rowx=1,end_rowx=None)  `，取第一行到最后一行的数据，用` None`表示后续所有，写法很优雅。

2. ` cv.index(maxval)`，传入值 `maxval `，取得list cv中对应的index。

3. `open_zip(datafile) ` 函数实现解压缩文件。



# 4. `16. 探索Json`


## 4.1 示例代码

```python

"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# 一组用于传递给requests.get的参数
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}

# ★★★★★★★★★★注意是如何获取json的
# 输入url，以及get所需要的参数，返回从网络上get到的json对象
# 后面两个是默认参数，不传值也可以
def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)

# 打印函数
def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():

    # 取出json对象，results是dict字典类型
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    print "★★",type(results)
    pretty_print(results)

    # 获取key为artists数据(list类型)，取出该list的第4个值
    print "\nARTIST:"
    pretty_print(results["artists"][3])

    # 上面的第四个值，是一个字典，通过key`id `取得对应的value
    artist_id = results["artists"][3]["id"]
    
    # 通过上面的id，以及另一个获取json对象的函数获取json对象
    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print "★★",type(releases[0])

    # 通过上面得到的release是一个list
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)

    # 但是list releases 中的每个元素是字典类型
    # 注意下面的这种写法，很简洁，一步到位获取了release列表各个元素字典中的特定value
    release_titles = [r["title"] for r in releases]
    print "\nALL TITLES:"
    for t in release_titles:
        print t

if __name__ == '__main__':
    main()

```

## 4.2 总结

1. ` query_site`和` query_by_name`讲述如何从网络获取json对象。
2. ` main`，讲述如何将json对象中的值取出来。
3. ` release_titles = [r["title"] for r in releases]`，releases是包含了一系列字典的list，这样直接将所有字典中的title抽取出来，重新组成list。




# 5. `课程3，练习1 使用csv模块 `

```python
def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        r = csv.reader(f)
        
        # 迭代器调用next，获取一行数据，第一行的数据是气象站信息
        station_info = next(r)
        name = station_info[1]
        
        # 迭代器获取第二行key 信息
        label_info = next(r)
        
        # enumerate使得list有了key和value的属性
        for row_id,row_value in enumerate(list(r)):
            row_data = []
            # 将一行数据的list，各个cell的值取出，加到row_data这个list中
            for col_id,col_value in enumerate(row_value):
                row_data.append(col_value)
            data.append(row_data)    
        
    # Do not change the line below
    return (name, data)

```


1. 注意reader的next函数用法，如` next(r)`
2. ` for row_id,row_value in enumerate(list(r)):`的用法很简洁


# 6. `课程3，练习2  Excel 至 CSV`


## 6.1 示例代码

```python
import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"

# 解压缩用函数
def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

# 
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    # 数据的定义是，staion / 最大值 / 最小值
    # 用字典比较合适，station作为key，最大值和最小值作为value，该value又是个字典
    data = {}
    # process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        cv = sheet.col_values(n, start_rowx=1, end_rowx=None)

        maxval = max(cv)
        # 注意通过value获取list的index
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        data[station] = {"maxval": maxval,
                         "maxtime": realtime}

    return data


# 将读取的上述字典数据，写入到CSV文件中
def save_file(data, filename):
    with open(filename, "w") as f:
        w = csv.writer(f, delimiter='|')
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for s in data:
        	# 这种写法很好，直接将不需要的值省略
            year, month, day, hour, _ , _= data[s]["maxtime"]

            # 写入一行数据
            w.writerow([s, year, month, day, hour, data[s]["maxval"]])


if __name__ == "__main__":
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

```

## 6.2 总结

1. 选取合适的数据结构，比如这里用嵌套字典就比较合适。
2. ` year, month, day, hour, _ , _= data[s]["maxtime"]`，这种写法很好，直接将不需要的值省略


# 7. `课程3，练习3  整理Json `

## 7.1 代码

```python


import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "",
            "article": ""}


# 直接从Json文件中读取，返回json对象
def get_from_file(kind, period):
    filename = "popular-{0}-{1}.json".format(kind, period)
    print filename
    with open(filename, "r") as f:
    	# 注意是如何从文件中获取json对象的
        return json.loads(f.read())

'''
- labels: list of dictionaries, where the keys are the "section" values and
  values are the "title" values for each of the retrieved articles.
- urls: list of URLs for all 'media' entries with "format": "Standard Thumbnail".
'''

# 根据上面的要求去获取数据
def article_overview(kind, period):
    data = get_from_file(kind, period)
    
    titles = []
    urls =[]
    # YOUR CODE HERE

    # data是list，row是一个字典
    for row in data:
        title = {}
        # title是一个字典，key为row字典中section对应的value，value为row中的title值
        title[row['section']] = row['title']
        titles.append(title)
        
        # 这一部分要对照实际json文件才明白
        media_list = row['media']
        
        for media in media_list:
            media_metadata_list = media['media-metadata'] # 不能用- 命名
            
            for media_metadata in media_metadata_list:
                if media_metadata['format'] == 'Standard Thumbnail':
                    urls.append(media_metadata['url'])
                    
    return (titles, urls)

# 从网络上获取json文件，注意这里需要APIkey
def query_site(url, target, offset):
    if API_KEY["popular"] == "" or API_KEY["article"] == "":
        print "You need to register for NYTimes Developer account to run this program."
        print "See Intructor notes for information"
        return False
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

# 根据对应网站提供的API的参数，调用上面的从网络获取json对象的函数
def get_popular(url, kind, days, section="all-sections", offset=0):
    if days not in [1,7,30]:
        print "Time period can be 1,7, 30 days only"
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print "kind can be only one of viewed/shared/emailed"
        return False

    url += "most{0}/{1}/{2}.json".format(kind, section, days)
    data = query_site(url, "popular", offset)

    return data

# 将上面函数返回的data 即json对象，存储到文件中
# ★★
def save_file(kind, period):
    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]
    full_data = []
    with codecs.open("popular-{0}-{1}.json".format(kind, period), encoding='utf-8', mode='w') as v:
        for offset in range(0, num_results, 20):        
            data = get_popular(URL_POPULAR, kind, period, offset=offset)
            full_data += data["results"]
        
        v.write(json.dumps(full_data, indent=2))


def test():
    titles, urls = article_overview("viewed", 1)
    assert len(titles) == 20
    assert len(urls) == 30
    assert titles[2] == {'Opinion': 'Professors, We Need You!'}
    assert urls[20] == 'http://graphics8.nytimes.com/images/2014/02/17/sports/ICEDANCE/ICEDANCE-thumbStandard.jpg'


if __name__ == "__main__":
    test()
    titles, urls = article_overview("viewed", 1)

```

 ## 7.2 总结

 上面虽然是通过网络去获取json对象，但是没有使用，直接用了提供的json文件。
 1. `query_site `，将json数据从网络上获取到。
 2. `save_file `,将json 数据写到文件中，注意编码和偏移等。

