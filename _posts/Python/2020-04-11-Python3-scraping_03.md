---
layout: post
title: Python网络爬虫-03-实战-正则表达式
date: 2020-05-06 03:00:04
categories: Python
tags: Python
---
* content
{:toc}

1. 参考网络课程：[Python网络爬虫与信息提取](https://www.icourse163.org/course/BIT-1001870001)
2. [youtube-Python 6小时网络爬虫入门课程完整版(2020年）](https://www.youtube.com/watch?v=ZMjhBB17KVY)
3. 关于正则表达式，在这里也有涉及：[正则表达式](http://road2ai.info/2017/10/08/Uda-DataAnalysis-RegExr/)
4. 正则表达式online check工具 [https://regexr.com/](https://regexr.com/)
5. [莫烦python-正则表达式]（https://morvanzhou.github.io/tutorials/python-basic/basic/13-10-regular-expression/）

# 0. 快速参考

- 参考1：

![image](https://user-images.githubusercontent.com/18595935/79087406-1d57d900-7d7a-11ea-923a-8a7f2d98a3c5.png)

- 参考2：

![image](https://user-images.githubusercontent.com/18595935/79098238-7b95b380-7d9c-11ea-99e3-b4b46b4439ea.png)


# 1. Re(正则表达式)库入门

正则表达式是用来简洁表达一组字符串的表达式，比如有如下的一系列字符：

```html
'PN'
'PYN'
'PYTN'
'PYTHN'
'PYTHON'
```

使用正则表达式`P(Y|YTH|YTHO)?N`，切换到Python代码：

```python
regex='P(Y|YTH|YTHO)?N'
p=re.compile(regex)
```

## 1.1 正则表达式的常用操作符

![image](https://user-images.githubusercontent.com/18595935/79087725-33b26480-7d7b-11ea-8e0d-102ab505a363.png)
![image](https://user-images.githubusercontent.com/18595935/79087744-42008080-7d7b-11ea-87d4-ccc6b74bbe9e.png)

- 基本语法示例

![image](https://user-images.githubusercontent.com/18595935/79087894-c81cc700-7d7b-11ea-92ff-0e5c1dd6088c.png)

- 经典的正则表达式示例

![image](https://user-images.githubusercontent.com/18595935/79087905-ceab3e80-7d7b-11ea-9374-b908630a518d.png)


# 2. Re库的基本使用

Re库采用raw String原生字符串，书写为`r'text'`，通过这种方式会忽略掉转义符号。比如 `r'[1-9]\d{5}' `

![image](https://user-images.githubusercontent.com/18595935/79090241-f1415580-7d83-11ea-84dd-c775d23c4057.png)

## 2.1 search的使用

```python
re.search(pattern,string,flags=0)
```

在一个字符串中搜索匹配的正则表达式的第一个位置返回match对象。

1. pattern: 正则表达式的字符串或原生字符串
2. string：待匹配字符串
3. flags：正则表达式使用时的控制标记
   1. re.I,re.IGNORECASE: 忽略正则表达式的大小写，`[A-Z]`能够匹配小写字符
   2. re.M,re.MULTILINE: 正则表达式中的`^`能够将给定字符串的每行当做匹配开始
   3. re.S,re.DOTALL：正则表达式中的`.`能匹配所有字符，默认匹配换行外的所有字符

```python
import re
match = re.search(r'\d{5}','BIT 10081')
if match:
    print(match.group(0))
```

输出：

```html
10081
```

## 2.2 match的使用

```python
re.match(pattern,string,flags=0)
```

在一个字符串的**开始位置**，匹配的正则表达式的第一个位置返回match对象。

1. pattern: 正则表达式的字符串或原生字符串
2. string：待匹配字符串
3. flags：正则表达式使用时的控制标记
   1. re.I,re.IGNORECASE: 忽略正则表达式的大小写，`[A-Z]`能够匹配小写字符
   2. re.M,re.MULTILINE: 正则表达式中的`^`能够将给定字符串的每行当做匹配开始
   3. re.S,re.DOTALL：正则表达式中的`.`能匹配所有字符，默认匹配换行外的所有字符

```python
import re
match = re.match(r'\d{5}','10081 BIT ')
if match:
    print(match.group(0))
```

输出：

```html
10081
```

## 2.3 findall的使用

```python
re.findall(pattern,string,flags=0)
```

搜索字符串，以列表类型返回全部能匹配的子串。

1. pattern: 正则表达式的字符串或原生字符串
2. string：待匹配字符串
3. flags：正则表达式使用时的控制标记
   1. re.I,re.IGNORECASE: 忽略正则表达式的大小写，`[A-Z]`能够匹配小写字符
   2. re.M,re.MULTILINE: 正则表达式中的`^`能够将给定字符串的每行当做匹配开始
   3. re.S,re.DOTALL：正则表达式中的`.`能匹配所有字符，默认匹配换行外的所有字符

```python
import re
match = re.findall(r'\d{5}','10081 BIT TSU10084')
print("1:",match)
```

输出：

```html
1: ['10081', '10084']
```

## 2.4 split的使用

```python
re.split(pattern,string,maxsplit=0,flags=0)
```

将一个字符串按照正则表达式匹配结果，进行分割，返回列表类型

1. pattern: 正则表达式的字符串或原生字符串
2. string：待匹配字符串
3. maxsplit: 最大分个数，剩余部分作为最后一个元素输出
4. flags：正则表达式使用时的控制标记
   1. re.I,re.IGNORECASE: 忽略正则表达式的大小写，`[A-Z]`能够匹配小写字符
   2. re.M,re.MULTILINE: 正则表达式中的`^`能够将给定字符串的每行当做匹配开始
   3. re.S,re.DOTALL：正则表达式中的`.`能匹配所有字符，默认匹配换行外的所有字符


```python
import re
match1 = re.split(r'\d{5}','10081BIT 10084 TSU ')
match2 = re.findall(r'\d{5}','10081 BIT TSU10084')
print("1:",match1)
print("2:",match2)
```

输出：

```html
1: ['', 'BIT ', ' TSU ']
2: ['10081', '10084']
```

## 2.5 finditer的使用

```python
re.finditer(pattern,string,flags=0)
```

搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象。

1. pattern: 正则表达式的字符串或原生字符串
2. string：待匹配字符串
3. flags：正则表达式使用时的控制标记
   1. re.I,re.IGNORECASE: 忽略正则表达式的大小写，`[A-Z]`能够匹配小写字符
   2. re.M,re.MULTILINE: 正则表达式中的`^`能够将给定字符串的每行当做匹配开始
   3. re.S,re.DOTALL：正则表达式中的`.`能匹配所有字符，默认匹配换行外的所有字符

```python
import re
for m in re.finditer(r'\d{5}','BIT10081 TSU10099'):
    if m:
        print(m.group(0))
```

输出：

```html
10081
10099
```

## 2.6 sub的使用

```python
re.sub(pattern,repl,string,count=0,flags=0)
```

搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象。

1. pattern: 正则表达式的字符串或原生字符串
2. repl:替换匹配字符串的字符串
3. string：待匹配字符串
4. count：匹配最大替换次数
5. flags：正则表达式使用时的控制标记
   1. re.I,re.IGNORECASE: 忽略正则表达式的大小写，`[A-Z]`能够匹配小写字符
   2. re.M,re.MULTILINE: 正则表达式中的`^`能够将给定字符串的每行当做匹配开始
   3. re.S,re.DOTALL：正则表达式中的`.`能匹配所有字符，默认匹配换行外的所有字符

```python
import re
match = re.sub(r'\d{5}',':zipcode','BIT10081 TSU10099')
print(match)
```

输出：

```html
BIT:zipcode TSU:zipcode
```

## 2.7 Re库的另一种等价用法

```python
regex = re.compile(pattern,flags=0)
```

将正则表达式的字符串形式编译成正则表达式对象。

1. pattern: 正则表达式的字符串或原生字符串
2. repl:替换匹配字符串的字符串

- 函数式用法：

```python
rst = re.search(r'\d{5}','BIT10081 TSU10099')
```

- 面向对象用法，编译后的多次操作

```python
pat = re.compile(r'\d{5}')
rst = pat.search('BIT10081 TSU10099')
```

![image](https://user-images.githubusercontent.com/18595935/79105348-72601300-7dab-11ea-85c8-f74b4eecc52c.png)

# 3. Re库的Match对象

- Match对象的属性
- Match对象的方法

![image](https://user-images.githubusercontent.com/18595935/79107062-a6890300-7dae-11ea-8bd0-ed0884bf5541.png)
![image](https://user-images.githubusercontent.com/18595935/79107077-adb01100-7dae-11ea-9d54-bfbd033da6c3.png)

```python
import re
m = re.search(r'\d{5}','ABCDE10081 F10099')
print("1.string   :  ",m.string)
print("2.pos      :  ",m.pos)
print("3.endpos   :  ",m.endpos)
print("4.group    :  ",m.group(0))
print("5.start    :  ",m.start())
print("6.end      :  ",m.end())
print("7.span     :  ",m.span())
```

输出：

```html
1.string   :   ABCDE10081 F10099
2.pos      :   0
3.endpos   :   17
4.group    :   10081
5.start    :   5
6.end      :   10
7.span     :   (5, 10)
```

# 4. Re库的贪婪匹配和最小匹配

Re库默认采用贪婪匹配，即输出匹配最长的子串。

![image](https://user-images.githubusercontent.com/18595935/79108003-6591ee00-7db0-11ea-9863-3c4c25111828.png)

```python
match1 = re.search(r'PY.*N','PYANBNCNDN')
print("贪婪匹配:",match1.group(0))

match2 = re.search(r'PY.*?N','PYANBNCNDN')
print("最小匹配:",match2.group(0))
```

输出结果如下：

```html
贪婪匹配: PYANBNCNDN
最小匹配: PYAN
```



# 4. 示例2，淘宝定向比价爬虫

# 5. 示例3，股票数据定向爬虫

