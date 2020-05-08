---
layout: post
title: DjangoSample-01-Models数据在html的显示
date: 2020-05-02 02:01:01
categories: Python
tags: Django总结
---
* content
{:toc}

> [DjangoSample-XX...]系列,记录平常做的一些Django范例程序。
> 作为自己以后工作时的参考信息。

# <i class="fa fa-cubes" style="font-size:1em;"></i> 实现功能
1. 添加了两个model，其中一个需要另外一个表的字段作为外键。
2. 可以在后台添加这两个表的数据。
3. 添加后，可以在前台进行显示。分为两种方式，DjangoAPI获取数据以及原生SQL获取数据。

# <i class="fa fa-cubes" style="font-size:1em;"></i> 实现过程

## 1. 生成app
`python manage.py startapp dpjTest`

## 2. 将app加到setting
在`mysite/settings.py` 的INSTALLED_APPS 中，在它下面添加一行 `‘dpjTest’`

## 3. 定义model
在`models.py`中添加如下代码，创建模型，Album模型中的artist属性，外key依赖Musician表：
```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
```
> 上面的__str__，生成的字段，在admin的后台显示，另外在一个表的外键中也显示。如下图:

 - 显示的是Musician中first_name和last_name的组合：

   ![image](https://user-images.githubusercontent.com/18595935/29394743-528eaf7a-8347-11e7-9dd0-ca130a47f6a3.png)
 - 在Album表的外key中显示为__str__字段：

   ![image](https://user-images.githubusercontent.com/18595935/29394865-2d5a5b4a-8348-11e7-949e-70ec48719ebf.png)

## 4. 生成SQL
执行`python manage.py makemigrations dpjTest`。

## 5. 执行SQL，生成数据表
执行`python manage.py migrate`。

## 6. 添加url
1. 在mysite的urls.py中添加 `url(r'^test/', include('dpjTest.urls')),`。
2. 在dpjTest的app中，添加urls.py文件，并添加`url(r'^$', views.index, name='index'),`，使得test/ 的url被匹配到index的view上去。

## 7. 在admin中注册models
```python
from django.contrib import admin
from .models import Musician,Album

admin.site.register(Musician)
admin.site.register(Album)
```

## 8.添加view
```python
from django.shortcuts import render
from .models import Musician,Album

def index(request):
    musician = Musician.objects.all()
    album = Album.objects.all()

    return render(request, 'dpjTest/index.html', {"musician":musician,
                                                     "album":album,})
```

## 9.添加模板文件
添加`/dpjTest/templates/dpjTest/index.html`
```html
<h2>DjangoAPI查询后显示</h2>
<a>1. Musician 表 </a>
<table class="table5" border=1>
    <tr><th>first_name</th><th>last_name</th><th>instrument</th></tr>
    [% for record in Musician %}
    <tr>
         <td> [{record.first_name}}</td>

          <td>[{record.last_name}}</td>

         <td>[{record.instrument}}</td>
    </tr>
    [% endfor %}
</table>

<a>2. Album 表 </a>
<table class="table5" border=1>
    <tr><th>artist</th><th>name</th><th>release_date</th><th>num_stars</th></tr>
    [% for record in Album %}
    <tr>
         <td> [{record.artist}}</td>

          <td>[{record.name}}</td>

         <td>[{record.release_date}}</td>

        <td>[{record.num_stars}}</td>
    </tr>
    [% endfor %}
</table>
```

## 10. 通过上面的步骤，能在html中显示如下

![image](https://user-images.githubusercontent.com/18595935/29395215-441e49ac-834a-11e7-93ac-e372428e06a5.png)

## 11. 尝试用原生SQL获取数据并显示
### 1. view中添加SQL获取数据的代码，最终view代码如下：
```python
from django.shortcuts import render
from .models import Musician,Album
from django.db import connection

def index(request):
    musician = Musician.objects.all()
    album = Album.objects.all()

    musiciansql = my_musician_sql()
    albumsql= my_album_sql()

    return render(request, 'dpjTest/index.html', {"Musician":musician,
                                                     "Album":album,
                                                  "AlbumSQL": albumsql,
                                                  "MusicianSQL":musiciansql,})

def my_album_sql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dpjTest_Album")
    results = cursor.fetchall()
    return results

def my_musician_sql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dpjTest_Musician")
    results = cursor.fetchall()
    return results
```

### 2. 修改模板文件
```html
<h2>原生SQL查询后显示</h2>
<a>1. Musician 表 </a>
<table class="table5" border=1>
    <tr><th>id</th><th>first_name</th><th>last_name</th><th>instrument</th></tr>
    [% for record in MusicianSQL %}
     <tr>
        [% for field in record%}
            <td>[{field}}</td>
            [% endfor %}
     </tr>
    [% endfor %}
</table>

<a>2. Album 表 </a>
<table class="table5" border=1>
    <tr><th>id</th><th>name</th><th>release_date</th><th>num_stars</th><th>artist</th></tr>
    [% for record in AlbumSQL %}
     <tr>
        [% for field in record%}
            <td>[{field}}</td>
            [% endfor %}
     </tr>
    [% endfor %}
</table>
```
可以看出与上面通过DjangoAPI解析数据的差别：
 - DjangoAPI中获取的数据，是键值对的list，有key和value。
 - 原生API中获取的数据，是List的List，没有key和value，只能按上面方式输出。

### 3. 对比原生SQL的输出结果

![image](https://user-images.githubusercontent.com/18595935/29396995-5f00f1a0-8356-11e7-952f-ae8fc113a30d.png)

### 4. 观察实际sqlite3中数据库表的结构，
用如下的语句输出表结构
```python
cursor.execute('select * from sqlite_master where type="table"')
results = cursor.fetchall()
for createsql in results:
    print(createsql[4])
```
>createsql[4]只取出第5个字段，即创建表的SQL语句。

输出如下(这里把其他表也输出供参考)：
```sql

CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL)

CREATE TABLE sqlite_sequence(name,seq)

CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE)

CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"))

CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"))

CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"))

CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "action_time" datetime NOT NULL)

CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL)

CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL)

CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "username" varchar(150) NOT NULL UNIQUE)

CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL)

CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "text" text NOT NULL, "created_date" datetime NOT NULL, "published_date" datetime NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id"))

CREATE TABLE "dpjTest_musician" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(50) NOT NULL, "last_name" varchar(50) NOT NULL, "instrument" varchar(100) NOT NULL)

CREATE TABLE "dpjTest_album" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "release_date" date NOT NULL, "num_stars" integer NOT NULL, "artist_id" integer NOT NULL REFERENCES "dpjTest_musician" ("id"))
```

注意，上面Musician和Album的结构如下：
```sql
CREATE TABLE "dpjTest_musician" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(50) NOT NULL, "last_name" varchar(50) NOT NULL, "instrument" varchar(100) NOT NULL)

CREATE TABLE "dpjTest_album" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "release_date" date NOT NULL, "num_stars" integer NOT NULL, "artist_id" integer NOT NULL REFERENCES "dpjTest_musician" ("id"))

```
- 自动添加了id字段，主key自增类型
- 注意外key字段，自动链接到其他表的主key字段
- 注意生成的表名，是app名和model名的组合


# <i class="fa fa-bell" aria-hidden="true"></i> 下一步
- 搞清楚djiango的model，熟练使用其接口函数。
- 了解djiango对数据库表的生成，查询，以及更新的方式，是怎么最终生成SQL的。
