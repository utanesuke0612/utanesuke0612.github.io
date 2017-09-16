---
layout: post
title: DjangoProject-01-Models模型入门(2)(Introduction to models)
date: 2017-08-16 22:46:59
categories: Django
tags: Django官方文档
---
* content
{:toc}

> [DjangoProject-XX...]系列根据[官网文档](https://docs.djangoproject.com/en/1.11/)整理，添加了自己的理解以及实验部分。
> 作为自己以后工作时的参考信息。


Model 模型是关于数据的单一并决定性的数据源。(这句话的原始翻译，简单点说，就在Django中通过Model来表现数据，数据存储在Model中)。除了数据的值，Model还能存储数据的方法，比如存储 Person，数据值有first-name和last-name，方法有 eat()等。一般来说，一个Model模型映射到一个单独的数据库table中。
1. 每一个model都是继承于 `django.db.models.Model.`的python class。
2. model的每一个属性attribute，对应到数据库表中是一个field，即字段。
3. Django提供了访问数据库的api接口，具体参考 [Making queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/)。

> 参考 [djangoproject 官方文档-model 篇](https://docs.djangoproject.com/en/1.11/topics/db/models/#)

>本篇上集是[Models模型入门(1)](https://utanesuke0612.github.io/2017/08/16/DjangoProject_01/)
>本篇专门讲解 **Model inheritance**

Django中的模型model继承，几乎与python中普通class的继承一样，所有子类都继承于django.db.models.Model.

在Django中，可能用到三种类型的继承:
1. 类似于抽象类，即该类不能单独的生成对象，它抽取所有子类的共有属性，组成基类。比如PC,TV,SmartPhone，它们都有属性电压，显示器，故可以将这部分属性抽取出来，组成一个包含了电源和显示属性的抽象类，但这个抽象类不能生成具体对象。(回顾一下java中抽象类与接口的差别)
2. 如果想继承一个已有的model(可能是外部导入的)，另外也想每个model都有它独自的db 表，可以使用多表继承。
3. 最后，如果只想修改一个model的默认行为，而不需要修改model的任何field，可以使用代理模型Proxy models。

# 1. 抽象基类 Abstract base classes

在类的`class Meta`中添加`abstract=True`，用于声明一个class是抽象类，这个类不会用来创建数据表，类似无法生成对象。当在其他类中使用该基类的时候，这些基类的field将被添加到各个子类中，子类中不能与基类的field重名。

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

```
重写生成上述sql文件，如下:

```
(myvenv) C:\Users\61041150\djangoproject\mysite>python manage.py makemigrations
dpjTest
Migrations for 'dpjTest':
  dpjTest\migrations\0006_student.py
    - Create model Student

```
上面只生成Student的表，然后注册到admin.py中时，也只能对Student注册，否则出错如下:
`    'The model %s is abstract, so it cannot be registered with admin.' % model._
_name__`

在admin后台，给Student表添加一条记录的话，会显示出name / age / home_group 三个字段。



## 1. Meta class的继承

如果一个子类不声明其自身的Meta Class的话，就会继承父类的Meta，如果子类想要扩展父类的Meta Class，可以继承它
如下代码:

```python
from django.db import models

class CommonInfo(models.Model):
    # ...
    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'

```
1. 默认`abstract=False.`，即默认非基类。
2. 有些属性，默认不继承，比如上面的` db_table = 'student_info'`。

如下是Student的表结构
```sql
CREATE TABLE "dpjTest_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 "name" varchar(100) NOT NULL, "age" integer unsigned NOT NULL, "home_group" var
char(5) NOT NULL)
```

## 2. 注意related_name 和 related_query_name
本节先跳过


# 2. 多表继承 Multi-table inheritance

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

如下是上面的表结构
```sql
CREATE TABLE "dpjTest_place" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "
name" varchar(50) NOT NULL, "address" varchar(80) NOT NULL)

CREATE TABLE "dpjTest_restaurant" ("place_ptr_id" integer NOT NULL PRIMARY KEY R
EFERENCES "dpjTest_place" ("id"), "serves_hot_dogs" bool NOT NULL, "serves_pizza
" bool NOT NULL)
```

上面的定义中，restaurant表中，其主key的定义为`"place_ptr_id" integer NOT NULL PRIMARY KEY R
EFERENCES "dpjTest_place" ("id")`。

注意外键定义时的表结构的差别，外key会改变model中的field名，如:
```python
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    ...

# 该外key的定义如下
"artist_id" integer NOT NULL REFERENCES "dpjTest_musician" ("id")
```
参考 [Musician与Album](https://utanesuke0612.github.io/2017/08/16/DjangoSample_01/#4-观察实际sqlite3中数据库表的结构)

## 1. admin中restaurant的定义界面:

![](assets/DjangoProject-Models-1-79f55.png)

自动引入了place中的字段，这里输入的place信息，会同时插入到place表中，不会根据name或address排除重复。
1. 比如在 Restaurant表中插入一条记录`lijun / hori5-7 / true / true`
2. 单独在Place表中插入一条记录`wangling / hori5-7`
3. 在django shell 中测试如下，说明Restaurant中插入的place信息，也同时被加入Place表中了：

```
>>> Place.objects.filter(name="lijun")
<QuerySet [<Place: lijun>]>
>>> Restaurant.objects.filter(name="lijun")
<QuerySet [<Restaurant: lijun>]>
>>> Place.objects.filter(name="wangling")
<QuerySet [<Place: wangling>]>
>>> Restaurant.objects.filter(name="wangling")
<QuerySet []>
```


## 2. 未完待续ing
