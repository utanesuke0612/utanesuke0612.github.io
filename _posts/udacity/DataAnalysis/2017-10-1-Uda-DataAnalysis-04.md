---
layout: post
title: Uda-DataAnalysis-04-复杂格式数据提取
date: 2017-10-01 00:02:00
categories: 数据分析
tags: Python Udacity DataAnalysis
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的4,5 复杂格式数据提取的总结。 讲述如何用python提取xml和html等数据，不是很深入，但是能完成简单的任务，有特定任务时再详细研究。

# 1. `7 解析XML示例程序`

## 1.1 代码(1)- 获取节点下的标签tag

```python
import xml.etree.ElementTree as ET
import pprint

# 将xml文件解析为一个tree
tree = ET.parse('exampleResearchArticle.xml')
# 获取该tree的所有root节点
root = tree.getroot()

# 获取root节点下的标签
print '\nChildren of root:'
for child in root:
    print child.tag

```


## 1.2 代码2- find和findall函数查找元素

```python
# 获取特定路径下的标签
# 如果这里有两个title，修改上面的函数为findall，返回一个list。
# 否则通过find的话，返回最开始找到的那个。
title = root.find('./fm/bibl/title')
title_text = ""
# title元素中有<p></p>子元素，循环找出所有子元素
for p in title:
    title_text += p.text
print "\nTitle:\n",title_text

```

```python
# 因为aug下面有很多个au，故用findall函数取出所有的au元素
print "\nAuthor email addresses:"
for a in root.findall('./fm/bibl/aug/au'):
    # au元素下面只有一个email元素
    email = a.find('email')
    if email is not None:
        # email元素是最低级的元素，直接取出text
        print email.text

```

## 1.3 代码-练习

```python
# 取出au元素下面的作者信息，另外将作者信息组织成字典
# 将所有的作者信息作为list的一个元素添加进去

import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def get_authors(root):
    authors = []
    # 从当前起，指定一个特定的路径
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }

        # 取出author元素中fnm/snm/email标签的数据
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text

        authors.append(data)
    
    print authors

    return authors
```


## 1.4 代码-练习-处理属性

```python
def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }

        
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        
        # 生成器，将findall找到的所有xml元素取出，将每个元素的属性用attrib找到
        # 得到的结果是[{'iid': 'I3'}, {'iid': 'I4'}],即包含字典的list
        insr_list = [insr.attrib for insr in author.findall('insr')]
        print insr_list

        # 生成器，先将list中的字典取出，然后取出字典中key为iid的value值，赋值给data['insr']这个list
        data['insr'] = [insr['iid'] for insr in insr_list]
        
        #print data

        authors.append(data)

    return authors
```

## 1.5 示例代码-练习

```python
def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }
        # 确实这里一步到位就行了，不需要分开写
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        
        # 找到所有的insr，返回一个包含了很多xml元素list
        insr = author.findall('./insr')
        # 遍历list，i是一个xml的元素，取出其属性用attrib
        for i in insr:
            # 属性是个字典，将字典中的value用key为iid取出，添加到data['insr'] 这个list中
            data["insr"].append(i.attrib["iid"])
        authors.append(data)

    return authors
```

# 2. `使用beautiful soup提取html`

## 2.1 代码

```python
from bs4 import BeautifulSoup

def options(soup,id):
    option_values =[]
    
    # 找出所有特定id的元素list
    carrier_list = soup.find(id=id)
    # 在特定元素list中，找option标签的元素
    for option in carrier_list.find_all('option'):
        # 找到特定元素的value
        option_values.append(option['value'])
    return option_values

def print_list(label,codes):
    print "\n%s:" % label
    for c in codes:
        print c

def main():
    soup = BeautifulSoup(open('virgin_and_logan_airport.html'))
    
    codes = options(soup,"CarrierList")
    #print_list("Carriers",codes)
    
    codes = options(soup,"CarrierList")
    #print_list('Carriers',codes)
    
    codes = options(soup,"AirportList")
    #print_list('AirportList',codes)

main()

```

## 2.2 练习

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
         soup = BeautifulSoup(html,"lxml")
         # 获取所有tag name为input的标签，是一个set
         inputs = soup.find_all("input")
            
         # 循环处理 tag 标签集
         for input in inputs:
                # input.attrs 是取出一个tag的所有属性，返回的是一个字典，key和value的键值对
                # 因为有的input tag可能没有name属性，所以必须要要先判断
                if "name" in input.attrs.keys():
                    # 根据题目要求获取指定value值，input这个标签的操作完全类似于字典
                    if input["name"] == "__EVENTVALIDATION":
                        data['eventvalidation'] = input['value']
                    if input["name"] == "__VIEWSTATE":
                        data['viewstate'] = input['value']
    return data

# 这个函数是直接从网上获取数据
def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text

def test():
    data = extract_data(html_page)
    # data中包含了request所需要的参数数据，传递这个参数数据给request函数
    # request可以返回整个网页
    data2 = make_request(data)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")
  
test()
```

## 2.3 示例代码

```python
def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml")
        # 直接通过id取得字典，如果有重复的怎么办呢
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

    return data

# 将得到的数据写入本地网页文件中

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    f = open('soup-output.html',"w")
    f.write(r.text)

data = extract_data(html_page)
make_request(data)
```

观察上面的输出文件，并没有得到想要的数据集。
解决方式： 视频中 21.抓取解法部分讲解了原因，没有弄明白

```python
def make_request():
    s = requests.Session()
    
    r = s.get("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
    soup = BeautifulSoup(r.text)
    
    eventvalidation_element = soup.find(id="__EVENTVALIDATION")
    eventvalidation = data["eventvalidation"]
    
    viewstate_element = soup.find(id="__VIEWSTATE")
    viewstate = viewstate_element['value']

    
    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    f = open('soup-output2.html',"w")
    f.write(r.text)

make_request()
```


# 3. 从html中提取特定数据

- 提取运营商

```python
from bs4 import BeautifulSoup
html_page = "options1.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        carrierList = soup.find(id="CarrierList")
        for child in carrierList.children:
            # 去除换行符，暂定方式
            if child == "\n":
                continue
                
            value = child['value']
            
            # 去除all之类的value，判断起始是否是all开头
            all_begin_value = value.startswith('All')
            
            # 如果不是all开头，则将value放入data中
            if all_begin_value == False:
                data.append(value)
            
            #print value
            #print all_begin_value

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__VIEWSTATEGENERATOR",viewstategenerator),
                       ("__EVENTVALIDATION", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

if __name__ == "__main__":
    test()


```

- 提取机场数据

```python

def extract_airports(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        carrierList = soup.find(id="AirportList")
        for child in carrierList.children:
            # 去除换行符，暂定方式
            if child == "\n":
                continue
                
            value = child['value']
            
            # 去除all之类的value，判断起始是否是all开头
            all_begin_value = value.startswith('All')
            
            # 如果不是all开头，则将value放入data中
            if all_begin_value == False:
                data.append(value)
            
            print value
            print all_begin_value

    return data


```

# 4. 处理所有的数据

在完成练习之前，需要将前两个练习结合起来，将所有的数据下载保存到本地。

## 4.1 获取所有request所需要的信息

```python

from bs4 import BeautifulSoup
import requests

html_page = "options1.html"

# 获取航空公司信息
def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        carrierList = soup.find(id="CarrierList")
        for child in carrierList.children:
            # 去除换行符，暂定方式
            if child == "\n":
                continue
                
            value = child['value']
            
            # 去除all之类的value，判断起始是否是all开头
            all_begin_value = value.startswith('All')
            
            # 如果不是all开头，则将value放入data中
            if all_begin_value == False:
                data.append(value)
            
    print "carrier:",data
    return data

# 获取机场信息
def extract_airports(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        carrierList = soup.find(id="AirportList")
        for child in carrierList.children:
            # 去除换行符，暂定方式
            if child == "\n":
                continue
                
            value = child['value']
            
            # 去除all之类的value，判断起始是否是all开头
            all_begin_value = value.startswith('All')
            
            # 如果不是all开头，则将value放入data中
            if all_begin_value == False:
                data.append(value)
    
    print "airports:",data
    return data

def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml")
        # 直接通过id取得字典
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

    print "extract_data:",data
    return data
```

## 4.2 进行网络请求，并将返回的数据写入本地文件

```python
def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = requests.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__EVENTVALIDATION", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))
    
    # 写到本地data文件夹，以airport和carrier命名
    f = open('data\{0}-{1}.html'.format(airport,carrier),"w")
    f.write(r.text)
    
    return r.text

def main():
    carriers_data = extract_carriers(html_page)
    airports_data = extract_airports(html_page)
    other_data = extract_data(html_page)
    
    data = {}
    data['eventvalidation'] = other_data['eventvalidation']
    data['viewstate'] = other_data['viewstate']
    
    # 循环调用
    for carrier in carriers_data:
        data["carrier"] = carrier
        for airport in airports_data:
            data['airport'] = airport
            make_request(data)

main()
```

# 5. 练习-分隔错误的xml文件

原始文件中，将几个xml文件合并在一起了，需要将其分开，并输出到单独的文件中。

```python

import xml.etree.ElementTree as ET
PATENTS = 'patent5.xml'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
   
    file_counter = 0
    with open(filename,'rb') as f:
        for line in f:
        	# 判断是否xml的文件头
            if line.startswith("<?xml"):
                if file_counter > 0:
                    f.close()
                # 如果是xml文件头，新打开一个文件
                f = open('{0}-{1}'.format(PATENTS,file_counter),"w")
                file_counter = file_counter + 1
            
            # 将数据写入文件
            f.write(line)  

# 如下是udacity的测试代码
def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()
```