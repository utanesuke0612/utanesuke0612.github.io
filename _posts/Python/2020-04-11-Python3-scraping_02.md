---
layout: post
title: Python网络爬虫-02-提取-Beautiful Soup库
date: 2020-05-06 03:00:02
categories: Python
tags: Python
---
* content
{:toc}

1. 参考网络课程：[Python网络爬虫与信息提取](https://www.icourse163.org/course/BIT-1001870001)
2. 关于beautiful soup库，更详细说明资料参考[Beautiful Soup 4.4.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
3. [如何在uipath中使用python](https://qiita.com/RPAbot/items/05b3943f7362494ef496)
4. [井上さん：RPAにおけるインテグレーションのためのライブラリ開発](https://thinkit.co.jp/article/17318)

Beautiful soup库与Requests库的功能分担如下图：

![image](https://user-images.githubusercontent.com/18595935/79046557-a40e9800-7c4c-11ea-9bb9-0b90ec7d1e22.png)

> 下一步的工作中，需要大量解析网页中的内容，这个库用的比较多，要掌握。

# 1. Beautiful Soup库入门

## 1.1 安装：

```python
(base) C:\Users\jun.li>pip install beautifulsoup4
```

下面打印出一个示例页面的html源代码：

```python
import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    
    # Beautiful Soup 利用
    soup = BeautifulSoup(demo,"html.parser")
    print(soup.prettify())
except:
    print("NG")
```

打印出来结果如下：

```html
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
```

## 1.2 Beautiful Soup库的基本元素

|基本元素|说明|
|:--|:--|
|Tag|标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾|
|Name|标签的名字，`<p>..</p>`的名字是p，格式`<tag>.name`|
|Attributes|标签的属性，字典形式组织，格式`<tag>.attrs`|
|NavigableString|标签内非属性字符串，`<p>...</p>`中的省略号，格式`<tag>.string`|
|Comment|标签内字符串的注释部分，一种特殊的Comment类型|

示例：

```html
<p class="title">...</p>
```
1. 整个表示标签
2. p是标签的名称name
3. class与title是属性attrs，因为会有多个，所以是字典类型
4. ...表示非属性字符串，注释

示例：

- 将html内容做成soup，并从中提取p标签，赋值给tag

```python
import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    
    # Beautiful Soup 利用
    soup = BeautifulSoup(demo,"html.parser")
    tag = soup.p  #返回p标签
except:
    print("NG")
```

- **从p的tag中获取各种信息**:

```python
print("1:",tag)
print("2:",tag.name)
print("3:",tag.attrs)
print("4:",tag.string)
print("5:",tag.parent.name)
```

打印结果如下：

```html
1: <p class="title"><b>The demo python introduces several python courses.</b></p>
2: p
3: {'class': ['title']}
4: The demo python introduces several python courses.
5: body
```

- **string与Comment**：

```python
newsoup = BeautifulSoup("<b><!--This is a b tag comment --></b><p>This is not a comment</p>","html.parser")

print("1:",newsoup.b.string)
print("2:",type(newsoup.b.string))

print("3:",newsoup.p.string)
print("4:",type(newsoup.p.string))

```

输出结果如下：

```python
1: This is a b tag comment 
2: <class 'bs4.element.Comment'>
3: This is not a comment
4: <class 'bs4.element.NavigableString'>
```

## 1.3 基于bs4库的HTML内容遍历方法

回顾下demo.html的格式：

```html
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
```

基于标签树的上行遍历，下行遍历，平行遍历：

![image](https://user-images.githubusercontent.com/18595935/79062643-10ce7480-7cd7-11ea-8c36-fcfd56eebcb8.png)


![image](https://user-images.githubusercontent.com/18595935/79062692-6014a500-7cd7-11ea-81f3-934d5f66343f.png)

示例如下，先煲汤：

```python
import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
kv = {'user-agent':'Mozilla/5.0'}

r = requests.get(url,headers = kv)
r.raise_for_status()
r.encoding = r.apparent_encoding
demo = r.text
    
# Beautiful Soup 利用
soup = BeautifulSoup(demo,"html.parser")
```



## 1.4 下行遍历

```python
print("1:",soup.head)
print("2:",soup.head.contents)
print("3:",soup.body.contents)
print("4:",soup.body.contents[1])
```

输出如下：

```html
1: <head><title>This is a python demo page</title></head>
2: [<title>This is a python demo page</title>]
3: ['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
4: <p class="title"><b>The demo python introduces several python courses.</b></p>
```

- **遍历儿子节点**
 
```python
for child in soup.body.children:
    print(child)
    print("---")
```

输出如下：

```html
<p class="title"><b>The demo python introduces several python courses.</b></p>


<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>

```

- **遍历子孙节点**

迭代输出，比如第一个`<p><b>×××</b></p>`，1.整体输出一次，2.b tag输出一次，3.×××输出一次。

```python
for child in soup.body.descendants:
    print(child)
    print("---")
```

输出如下：

```html
---
<p class="title"><b>The demo python introduces several python courses.</b></p>
---
<b>The demo python introduces several python courses.</b>
---
The demo python introduces several python courses.
---


---
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
---
Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

---
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
---
Basic Python
---
 and 
---
<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
---
Advanced Python
---
.
---


---
```

## 1.5 上行遍历

```python
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
```

输出如下：

```html
p
body
html
[document]
```

## 1.6 平行遍历

```python
print("1:",soup.a.next_sibling)
print("2:",soup.a.next_sibling.next_sibling)
print("3:",soup.a.previous_sibling)
print("4:",soup.a.previous_sibling.previous_sibling)
print("5:",soup.a.parent)
```

输出如下：

1. and，是下一个的平行节点
2. Python is a wonder...，是其上一个的平行节点

```html
1:  and 
2: <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
3: Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

4: None
5: <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
```

- **遍历后续节点和遍历前序节点**： 

```python
for sibling in soup.a.next_sibling:
    print(sibling)
```

```python
for sibling in soup.a.previous_sibling:
    print(sibling)
```

## 1.7 bs4的格式化输出

```python
print("1:",soup.prettify())
print("2:",soup.a.prettify())
```

# 2. 信息组织与提取方法

## 2.1 信息标记的三种方式

XML,JSON,YAML，各有优缺点。

## 2.2 [重要]基于bs4库的HTML内容查找方法

```python
<>.find_all(name,attrs,recursive,string,**kwargs)
```

1. 返回一个列表类型，存储查找的结果。
2. `name`：对标签名称的检索字符串。
3. `attrs`：对标签属性值得检索字符串，可标注属性检索
4. `recursive`：是否对子孙全部检索，默认True
5. `string`：<>...</>中字符串区域的检索字符串

```python
print("1:",soup.find_all('a'))
print("2:",soup.find_all(['a','b']))
```

结果：

```html
1: [<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
2: [<b>The demo python introduces several python courses.</b>, <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
```

可以通过`soup.find_all(True)`检索所有标签。


- **使用正则表达式：**

```python
import re

for tag in soup.find_all(re.compile("b")):
    print(tag.name)
```

检索所有以b开头的tag 名：

```html
body
b
```

- **P标签中，属性中带有course字符的标签**

```python
soup.find_all("p","course")
```

```html
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
 <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]
```

- **使用id进行查找：**

```python
import re
print("1:",soup.find_all(id='link1'))
print("2:",soup.find_all(id='link2'))
print("\n")
print("3:",soup.find_all(id=re.compile("link")))
```

输出如下：

```html
1: [<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]
2: [<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]


3: [<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
```

- **string中带有特定字符串**

```python
print("1:",soup.find_all(string = re.compile("python")))
```

输出：

```html
1: ['This is a python demo page', 'The demo python introduces several python courses.']
```
## 2.3 扩展方法

注意有两种简写方法：

1. `<tag>(..),`等价于`<tag>.find_all(..)`
2. `soup(..)`,等价于`soup.find_all(..)`


![image](https://user-images.githubusercontent.com/18595935/79067025-6286f700-7cf7-11ea-9e2d-12a51330d197.png)

# 3. 示例，中国大学排名爬取

```python
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("NG")
    
    return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    pass


def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
    
    print("Suc" + str(num))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) # 20 univs
main()

```

输出：

```html
    排名    	  学校  	    总分    
    1     	 清华大学 	    北京    
    2     	 北京大学 	    北京    
    3     	 浙江大学 	    浙江    
    4     	上海交通大学	    上海    
    5     	 复旦大学 	    上海    
    6     	中国科学技术大学	    安徽    
    7     	华中科技大学	    湖北    
    7     	 南京大学 	    江苏    
    9     	 中山大学 	    广东    
    10    	哈尔滨工业大学	   黑龙江    
    11    	北京航空航天大学	    北京    
    12    	 武汉大学 	    湖北    
    13    	 同济大学 	    上海    
    14    	西安交通大学	    陕西    
    15    	 四川大学 	    四川    
    16    	北京理工大学	    北京    
    17    	 东南大学 	    江苏    
    18    	 南开大学 	    天津    
    19    	 天津大学 	    天津    
    20    	华南理工大学	    广东    
Suc20
```

# 4. 从指定网站抽取QA

```python
import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("NG")
    
    return ""

def fillQAList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    
    print("-----------------------------------------質問-------------------------------------------")
    print("\n\n")
    
    for question in soup.find_all(class_="m-hdgLv3__hdg"):
        if(question.text.startswith("問")):
            print(question.text)
    
    print("\n\n")
    print("------------------------------------------質問と回答--------------------------------------")
    
    for question in soup.find_all(class_="m-grid__col1"):
        if(question.text.find("ページの先頭へ戻る")):
            for answer in question.text.split("ページの先頭へ戻る")[:-1]:
                print(answer.rstrip('\n'))
        pass

def main():
    uinfo = []
    url1 = {"name" : "よくあるお問い合わせをまとめました（FAQ）（２月21日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/newpage_00017.html"}
    url2 = {"name" : "一般の方向けQ&A（４月８日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/dengue_fever_qa_00001.html"}
    url3 = {"name" : "医療機関・検査機関向けQ&A（４月７日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/dengue_fever_qa_00004.html"}
    url4 = {"name" : "企業（労務）の方向けQ&A（４月６日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/dengue_fever_qa_00007.html"}
    url5 = {"name" : "労働者の方向けQ&A（３月25日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/dengue_fever_qa_00018.html"}
    url6 = {"name" : "関連業種の方向けQ&A（４月２日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/covid19_qa_kanrenkigyou.html"}
    url7 = {"name" : "水際対策の抜本的強化に関するQ&A（４月２日版）","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/covid19_qa_kanrenkigyou_00001.html"}
    url8 = {"name" : "学校再開に関するQ&A（子供たち、保護者、一般の方へ）","url" : "https://www.mext.go.jp/a_menu/coronavirus/mext_00003.html"}
    url9 = {"name" : "布マスクの全戸配布に関するQ&A","url" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/cloth_mask_qa_.html"}

    urllist = [url1,url2,url3,url4,url5,url6,url7,url8,url9]
    
    for url in urllist:
        print("\n\n\n")
        print(url["name"])
        html = getHTMLText(url["url"])
        fillQAList(uinfo,html)
    
main()
```

# 5. 补充-爬虫与网页结构

> 参考 [莫烦-python](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic/)

# 6. 补充-BeautifulSoup解析网页

# 7. 补充-更多请求/下载方式

# 8. 补充-加速你的爬虫

# 9. 补充-高级爬虫