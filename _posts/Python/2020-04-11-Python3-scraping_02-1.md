---
layout: post
title: Python网络爬虫-【扩展】Beautiful Soup 4.4.0 文档
date: 2020-05-06 03:00:03
categories: Python
tags: Python
---
* content
{:toc}

关于beautiful soup库，更详细说明资料参考[Beautiful Soup 4.4.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)和[文档日文版](http://kondou.com/BS4/)

参考：
1. [](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic/)
2. [](https://geek-docs.com/python/python-tutorial/python-beautifulsoup.html#BeautifulSoup-4)

> **在接下来的工作中，估计会大量涉及HTML中内容的解析，所以对这个库务必做到非常熟悉！！**

> 考虑自己做一个Django的网站，用于抽取指定网站上的QA列表，并支持编辑和CSV下载，类似于DX suite这样的。


# 0. 准备工作

```python
import requests
from bs4 import BeautifulSoup
url = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/cloth_mask_qa_.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"html.parser")
```

# 1. 快速开始

- 定义一个html对象：

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"lxml")

print(soup.prettify())
```

打印出来效果如下：

```html
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
```

## 1.1 常见操作

```python
print("1:",soup.title)
print("1:",type(soup.title)) # 

print("\n2:",soup.title.next) # 单独的文本，是title的子节点
print("2:",type(soup.title.next))

print("\n3:",soup.title.parent)
print("3:",soup.title.parent.name)
```

打印如下：

```html
1: <title>The Dormouse's story</title>
1: <class 'bs4.element.Tag'>

2: The Dormouse's story
2: <class 'bs4.element.NavigableString'>

3: <head><title>The Dormouse's story</title></head>
3: head
```

- 定位查找

```python
print("1:",soup.p)
print("1:",soup.p['class'])

print("\n2:",soup.p.next)
print("2:",soup.p.next.next)

print("\n3:",soup.find_all('a'))

print("\n4:",soup.find(id="link3")['href'])
```

输出

```html
1: <p class="title"><b>The Dormouse's story</b></p>
1: ['title']

2: <b>The Dormouse's story</b>
2: The Dormouse's story

3: [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

4: http://example.com/tillie
```

**注意这里取href的方式：**，link是数组中的一个元素，这个元素获取href，可以用get函数。

```python
for link in soup.find_all('a'):
    print(link.get('href'))
```

```html
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
```

获取其中所有的文本：

```python
print(soup.get_text()[0:200])
```

```html
The Dormouse's story

The Dormouse's story
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
```

# 2. 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: `Tag` , `NavigableString`, `BeautifulSoup`, `Comment`.

## 2.1 Tag

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>','lxml')
tag = soup.b
print("1:",type(tag))
print("2:",tag)
```

输出：

```html
1: <class 'bs4.element.Tag'>
2: <b class="boldest">Extremely bold</b>
```

Tag最重要的两个属性，分别是`name`和`attributes`。

### name

```python
print("1:",tag.name)
print("1:",tag)
tag.name = "blockquote"
print("2:",tag.name)
print("2:",tag)
tag.name = "b"
```

这里能给一个tag重新赋值：

```html
1: b
1: <b class="boldest">Extremely bold</b>
2: blockquote
2: <blockquote class="boldest">Extremely bold</blockquote>
```

### attributes

```python
print("1:",tag.attrs)
print("2:",tag['class'])
```

```html
1: {'class': ['boldest']}
2: ['boldest']
```

tag作为一个字典来进行处理，可以像字典一样访问，并对tag的属性进行追加，删除和修改。

```python
tag['class'] = 'verybold'
tag['id'] = 1
print("1:",tag)
print("2:",tag.attrs)
```

```html
1: <b class="verybold" id="1">Extremely bold</b>
2: {'class': 'verybold', 'id': 1}
```

删除：

```python
del tag['id']
print("1:",tag)
```

```html
1: <b class="verybold">Extremely bold</b>
```

### 有多个值的时候

```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>', "lxml")
print('1:',css_soup.p['class'])

css_soup = BeautifulSoup('<p class="body"></p>', "lxml")
print('2:',css_soup.p['class'])

```

输出：

```html
1: ['body', 'strikeout']
2: ['body']
```

如果某个属性看起来好像有多个值,但在任何版本的HTML定义中`都没有被定义为多值属性 `,那么Beautiful Soup会将这个属性作为字符串返回

```python
id_soup = BeautifulSoup('<p id="my id"></p>', "lxml")
id_soup.p['id']
```
输出：`'my id'`

### 可以遍历的字符串

Beautiful Soup用 NavigableString 类来包装tag中的字符串:

```python
print("1:",tag.string)
print("2:",type(tag.string))
```

```python
1: Extremely bold
2: <class 'bs4.element.NavigableString'>
```

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用`replace_with()`方法:

```python
tag.string.replace_with("No longer bold")
print("1:",tag)
```
输出：

```python
1: <b class="boldest">No longer bold</b>
```

### 注释及特殊字符串

```python
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,'lxml')
comment = soup.b.string
print('1:',type(comment))
```

```html
1: <class 'bs4.element.Comment'>
```

# 3. 遍历文档树

拿下面的HTML举例子：

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

## 3.1 子节点

一个Tag可能包含多个字符串或其他的Tag。

tag的名字：

```python
print("1:",soup.head)
print("2:",soup.title)
```

```html
1: <head><title>The Dormouse's story</title></head>
2: <title>The Dormouse's story</title>
```

```python
# 下面的代码可以获取<body>标签中的第一个<b>标签:
print("1:",soup.body.b)
# 获得当前名字的第一个tag:
print("2:",soup.a)
# 得到所有的<a>标签,
print("3:",soup.find_all('a'))
```

```html
1: <b>The Dormouse's story</b>
2: <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
3: [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

### [重要].contents 和 .children

tag的 .contents 属性可以将tag的子节点以列表的方式输出:

```python
head_tag = soup.head
print("1:",head_tag)

# 注意contents的返回值是个list
title_tag = head_tag.contents
print("2:",title_tag)

print("3:",title_tag[0].contents)
```

```html
1: <head><title>The Dormouse's story</title></head>
2: [<title>The Dormouse's story</title>]
3: ["The Dormouse's story"]
```

通过tag的 .children 生成器,可以对tag的子节点进行循环:

```python
for child in title_tag[0].children:
    print(child)
```

```html
The Dormouse's story
```

### .descendants

### .string

### .strings 和 stripped_strings

## 3.2 父节点

### .parent

### .parents

## 3.3 兄弟节点

### .next_sibling 和 .previous_sibling

### .next_siblings 和 .previous_siblings

## 3.4 回退和前进

### .next_element 和 .previous_element

### .next_elements 和 .previous_elements

# 4. 搜索文档树

## 4.1 过滤器

### 正则表达式

### 列表

### True

### 方法

## 4.2 find_all()

### name 参数

### keyword 参数

### 按CSS搜索

### string 参数

### limit 参数

### recursive 参数

## 4.3 其他find函数

### 像调用 find_all() 一样调用tag

### find()

### find_parents() 和 find_parent()

### find_next_siblings() 和 find_next_sibling()

### find_previous_siblings() 和 find_previous_sibling()

### find_all_next() 和 find_next()

### find_all_previous() 和 find_previous()

## 4.4 CSS选择器

# 5. 修改文档树

### 修改tag的名称和属性

### 修改 .string

### append()

### NavigableString() 和 .new_tag()

### insert()

### insert_before() 和 insert_after()

### clear()

### extract()

### decompose()

### replace_with()

### wrap()

### unwrap()

# 6. 输出

## 6.1 格式化输出

## 6.2 压缩输出

## 6.3 输出格式

## 6.4 get_text()

# 7. 指定文档解析器

解析器之间的区别

# 8. 编码

## 8.1 输出编码

## 8.2 Unicode, Dammit! (乱码, 靠!)

### 智能引号

### 矛盾的编码

# 9. 其他

比较对象是否相同
复制Beautiful Soup对象
解析部分文档
SoupStrainer


# 10 .常见问题

代码诊断
文档解析错误
版本错误
解析成XML
解析器的错误
杂项错误
如何提高效率

# 11. Beautiful Soup 3
迁移到BS4
需要的解析器
方法名的变化
生成器
XML
实体
迁移杂项