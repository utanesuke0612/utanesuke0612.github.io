---
layout: post
title: Uda-DataAnalysis-04-[扩展]-BeautifulSoup
date: 2017-10-01 00:03:00
categories: 数据分析
tags: Python Udacity DataAnalysis
---
* content
{:toc}

> 本篇是 Udacity 中` 数据分析进阶` 的4 复杂数据格式中的扩展，如何使用Beautiful Soup的[官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#) 。


# Beautiful Soup 4.2.0 文档

# 1. 快速开始


```python
from bs4 import BeautifulSoup
```


```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>1.The Dormouse's story</b></p>
<p class="title"><b>2.The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```


```python
soup = BeautifulSoup(html_doc, "lxml")

# 将上述html整体打印
# print(soup.prettify())
```

几个简单的浏览结构化数据的方法:


```python
print "1:",soup.title,"--",type(soup.title),"\n"

# 取出上面title object的属性
print "2:", soup.title.name
print "3:",soup.title.string
print "4:",soup.title.parent.name,"\n"

# 有多个时仅取第一个P
print "5:",soup.p,"--",type(soup.p)
print "6:",soup.p['class'],"--",type(soup.p['class']),"\n"

# 类似于上面的p
print "7:",soup.a,"--",type(soup.a)
# 获取所有的a，注意打印出来的类型差异
print "8:",soup.find_all('a'),"--",type(soup.find_all('a')),"\n"

# 根据id取出对应的数据
print "9:",soup.find(id="link3"),"--",type(soup.find(id="link3")),"\n"
```

    1: <title>The Dormouse's story</title> -- <class 'bs4.element.Tag'> 
    
    2: title
    3: The Dormouse's story
    4: head 
    
    5: <p class="title"><b>1.The Dormouse's story</b></p> -- <class 'bs4.element.Tag'>
    6: ['title'] -- <type 'list'> 
    
    7: <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> -- <class 'bs4.element.Tag'>
    8: [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>] -- <class 'bs4.element.ResultSet'> 
    
    9: <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a> -- <class 'bs4.element.Tag'> 
    
    

从文档中找到所有```<a>```标签的链接:


```python
# 分别打印所有元素的数据类型，和其中给一个元素的数据类型
print type(soup.find_all('a'))
print type(soup.find_all('a')[0]),"\n"

# 该元素中，有href可以取出
for link in soup.find_all('a'):
    print(link.get('href'))
```

    <class 'bs4.element.ResultSet'>
    <class 'bs4.element.Tag'> 
    
    http://example.com/elsie
    http://example.com/lacie
    http://example.com/tillie
    

从文档中获取所有文字内容,即所有从位于tag之间的文字


```python
print(soup.get_text())
```

    The Dormouse's story
    
    1.The Dormouse's story
    2.The Dormouse's story
    Once upon a time there were three little sisters; and their names were
    Elsie,
    Lacie and
    Tillie;
    and they lived at the bottom of a well.
    ...
    
    

# 2. 如何使用

将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象, 可以传入` 一段字符串`或`一个文件句柄`.


```python
soup1 = BeautifulSoup(open("index.html"))
soup2 = BeautifulSoup("<html>２．data</html>")
print soup1,"\n"
print soup2
```

    <html><body><p>data</p></body></html> 
    
    <html><body><p>２．data</p></body></html>
    

首先,文档被转换成Unicode,并且HTML的实例都被转换成Unicode编码


```python
print BeautifulSoup("Sacr&eacute; bleu!")
```

    <html><body><p>Sacré bleu!</p></body></html>
    

然后,Beautiful Soup选择最合适的解析器来解析这段文档,如果手动指定解析器那么Beautiful Soup会选择指定的解析器来解析文档.(参考 解析成XML ).


```python
print BeautifulSoup("Sacr&eacute; bleu!","lxml")
```

    <html><body><p>Sacré bleu!</p></body></html>
    

# 3. 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所以对象可以归纳为四种，: Tag , NavigableString , BeautifulSoup , Comment。

## 3.1 Tag

与HTML文档中的tag概念相同


```python
soup = BeautifulSoup('<b class="boldest" id="123">Extremely bold</b>')
tag = soup.b
print tag,"\n"
print type(tag)
```

    <b class="boldest" id="123">Extremely bold</b> 
    
    <class 'bs4.element.Tag'>
    

## 3.2 Name


```python
print tag.name
tag.name = "B"
tag
```

    b
    <B class="boldest" id="123">Extremely bold</B>



每个tag都有自己的名字,通过 .name 来获取,如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档。

## 3.3 Attributes

tag的属性操作方法与字典一样，可以被添加，删除或是修改。


```python
# 当前tag的class属性
tag['class']
```

    ['boldest']




```python
# 修改tag的属性
tag['class'] = "very bold"
```


```python
# 删除tag的属性
del tag['id']
```


```python
# 添加tag的属性
tag['id1'] = '999'
```

获取该tag的所有属性:


```python
print tag.attrs
```

    {'class': 'very bold', 'id1': '999'}
    

## 3.4 多值属性

HTML 4定义了一系列可以包含多个值的属性.在HTML5中移除了一些,却增加更多.最常见的多值的属性是 class (一个tag可以有多个CSS的class). 还有一些属性 rel , rev , accept-charset , headers , accesskey . 在Beautiful Soup中多值属性的返回类型是list:


```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print css_soup.p['class'],"--",type(css_soup.p['class'])

css_soup = BeautifulSoup('<p class="body"></p>')
print css_soup.p['class'],"--",type(css_soup.p['class'])
```

    ['body', 'strikeout'] -- <type 'list'>
    ['body'] -- <type 'list'>
    

如果转换的文档是XML格式,那么tag中不包含多值属性


```python
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print xml_soup.p['class'],"\n",type(xml_soup.p['class'])
```

    body strikeout 
    <type 'unicode'>
    

<未完待续>

# 4. 遍历文档树

# 5. 搜索文档树

# 6. 修改文档树

# 7. 输出

# 8. 指定文档解析器

# 9. 编码

# 10. 解析部分文档


