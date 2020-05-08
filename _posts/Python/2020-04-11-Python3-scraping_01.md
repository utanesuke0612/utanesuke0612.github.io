---
layout: post
title: Python网络爬虫-01-规则-requests库
date: 2020-05-06 03:00:01
categories: Python
tags: Python
---
* content
{:toc}

参考网络课程：[Python网络爬虫与信息提取](https://www.icourse163.org/course/BIT-1001870001)

# 1. Requests库入门

## 1.1 Requests 库

- 安装(在控制台)

```python
pip install requests
```

Requests库的7个主要方法：

![image](https://user-images.githubusercontent.com/18595935/79045519-86d6cb00-7c46-11ea-86b9-80dc891c440b.png)

## 1.2 requests的Get方法

```python
requests.get(url,params=None,**kwargs)
```

观察返回的Response对象：

![image](https://user-images.githubusercontent.com/18595935/79045593-e7fe9e80-7c46-11ea-877c-a7e9c0410e1f.png)

- Response的对象属性：

![image](https://user-images.githubusercontent.com/18595935/79045621-0e243e80-7c47-11ea-9382-ac63653a5e38.png)

```python
import requests
r = requests.get("http://www.baidu.com")
r.status_code
print(r.encoding)
print(r.apparent_encoding)
```

输出结果：

```
ISO-8859-1
utf-8
```

## 1.3 爬取网页的通用代码框架

下面的函数`raise_for_status()`，如果状态不是200，引发HTTPError异常。

```python
import requests
url = "https://www.mhlw.go.jp/stf/seisakunitsuite/newpage_00017.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[800:1000])
except:
    print("NG")
```

## 1.4 HTTP协议以及Requests库方法

HTTP协议对资源的操作：

![image](https://user-images.githubusercontent.com/18595935/79045885-8b9c7e80-7c48-11ea-8a13-76b0bd8d1192.png)

1. 用户 ->  网页：GET，HEAD
2. 网页 ->  用户：PUT，POST，PATCH，DELETE

## 1.5 Requests库主要方法解析

`requests.request(method,url,**kwargs)`,

1. method表示请求方式
2. `**kwargs`控制访问的参数，可选
3. params：字典或是字典序列，作为参数增加到url中

有如下的调用方式：

```python
r = requests.request('GET',url,**kwargs)
r = requests.request('HEAD',url,**kwargs)
r = requests.request('POST',url,**kwargs)
r = requests.request('PUT',url,**kwargs)
r = requests.request('PATCH',url,**kwargs)
r = requests.request('delete',url,**kwargs)
r = requests.request('OPTIONS',url,**kwargs)

```

比如，如下的代码表示修改agent去访问：

```python
import requests
url = "http://www.baidu.com/s"
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("NG")
```

# 2. 网络爬虫的规则

1. 网络爬虫的尺寸：
   1. 小规模，速度不敏感：Requests库，占需求的9成以上
   2. 中规模：Scrapy库
   3. 大规模：定制开发
2. 关于Robots协议，`https://www.jd.com/robots.txt`.

# 3. Requests库的网络实战

## 3.1 网络图片的爬取和链接 

> (获取pdf 、 动画等也应该是一样的)

```python
import requests
import os
# url = "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1091978681,1253128401&fm=26&gp=0.jpg"
url = "https://www.mhlw.go.jp/content/10900000/000610189.pdf"
root = "C://Users//jun.li//Desktop//TEMP//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("file saved")
    else:
        print("file existed")
except:
    print("NG")
```

## 3.2 百度搜索引擎关键词提交

```python
import requests
url = "http://www.baidu.com/s"
kv = {'wd':'Python'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("NG")
```