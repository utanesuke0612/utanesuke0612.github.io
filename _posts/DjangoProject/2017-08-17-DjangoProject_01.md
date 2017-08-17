---
layout: post
title: DjangoProject-01-Models模型入门(1)( Introduction to models)
date: 2017-08-16 22:45:59
categories: Python
tags: DjangoProject
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

# <i class="fa fa-cubes" style="font-size:1em;"></i> 1. 快速示例

## 1. 在当前的Project中创建一个新app。
 `python manage.py startapp dpjTest`

## 2.在setting中注册上述app
mysite/settings.py 的INSTALLED_APPS 中，在它下面添加一行 `‘dpjTest’`

## 3. 创建模型
在`dpjTest\models`中添加如下代码，完成一个模型的创建：

```python
  from django.db import models

  class Person(models.Model):
      first_name = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)
```

最终Django提交给数据库时的SQL语句类似如下：
```sql
 CREATE TABLE dpjTest_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```
- 表名，`app名_模型名`的组成结构。
- id，这个字段作为主key被Django自动追加的，可以自己重写。

# <i class="fa fa-cubes" style="font-size:1em;"></i> 2. 使用模型model

## 1. 重新生成类似于SQL的建表文件
在上一步中，已经将新建的app天骄到了settings.py中的INSTALLED_APPS中，那接着我们要为它生成数据库表，使用`python manage.py makemigrations dpjTest`,代码以及响应结果如下：

```
(myvenv) C:\Users\61041150\djangoproject\mysite>python manage.py makemigrations dpjTest
Migrations for 'dpjTest':
  dpjTest\migrations\0001_initial.py
    - Create model Person
```

## 2. 执行建表文件
`python manage.py migrate`。

## 3. 验证
在django的shell环境中验证上述表单是否创建成功，如下
 ```
(myvenv) C:\Users\61041150\djangoproject\mysite>python manage.py shell
Python 3.6.0 (default, Jan 23 2017, 17:35:20) [MSC v.1900 32 bit (Intel)] on win
32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from dpjTest.models import Person
>>> Person.objects.all()
<QuerySet []>
```

# <i class="fa fa-cubes" style="font-size:1em;"></i> 3.【重要】Fields 字段
模型Model中最重要的部分，也是唯一必须的部分，就是要为数据库定义字段field。字段field在这里对应class的属性。在models.py中继续追加两个model:

```python
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
```

## ①. 在admin.py中注册上面的三个模型
  ```python
  from django.contrib import admin
  from .models import Musician,Person,Album

  admin.site.register(Person)
  admin.site.register(Album)
  admin.site.register(Musician)
  ```

## ②. 重新生成SQL文件并执行：
 ```
 (myvenv) C:\Users\61041150\djangoproject\mysite>python manage.py makemigrations
 dpjTest
 Migrations for 'dpjTest':
   dpjTest\migrations\0002_auto_20170816_1245.py
     - Create model Album
     - Create model Musician
     - Add field artist to album

 (myvenv) C:\Users\61041150\djangoproject\mysite>python manage.py migrate
 Operations to perform:
   Apply all migrations: admin, auth, contenttypes, dpjTest, sessions, zoneManage

 Running migrations:
   Applying dpjTest.0002_auto_20170816_1245... OK
 ```

## ③. 验证，新增了下面的model：
![image](https://user-images.githubusercontent.com/18595935/29403845-84d4fdd6-8374-11e7-8832-cb527e7be94d.png)

- 上面的Album有个外key，指向Musician，我们先到Musician中插入一条数据如下：
![image](https://user-images.githubusercontent.com/18595935/29403886-9a8f0a9a-8374-11e7-93c6-7dc34fc8dc78.png)

- 在接下来插入Album数据时，该外key字段，自动关联到Musician的`def __str__(self)`，匹配到对应的数据：
![image](https://user-images.githubusercontent.com/18595935/29403934-aba4c7f2-8374-11e7-8c4f-5a5d3c8696d1.png)
> 上面的`def __str__(self)`返回的是first_name和last_name的组合。

---

## 3.1 字段Field类型
模型中的每一个Field，都是Field 类的一个实例即instance。Django需要他们实现:
1. 确定数据库中的表字段类型
2. 确定Html中该如何渲染数据
3. 进行最低限度的数据验证
Django提供了大量的内置数据类型，
可参考[model的Field类型](https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types)
，当然用户也可以自定义数据类型，参考[自定义Field类型](https://docs.djangoproject.com/en/1.11/howto/custom-model-fields/)。

## 3.2 Field Option 字段的可选项
每个field字段，都可以指定一些参数，比如`models.CharField(max_length=64)`中max_length.
有如下常见的可选项：
  - `null`:默认为False，指定为True的话，Django存储空值NULL到数据库。
  - `blank`：该字段是否允许为空，默认为False，即不允许。该字段影响到form验证。
  - `choices`添加选择项，将上面的Person模型修改为如下:
```python
 class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,default="L")
```

这样，在admin后台添加时，会给shirt_size提供选择项。在shell中演示如下
 ```python
 >>> p = Person(name="Fred","Flintstone",shirt_size="L")
 >>> p.save()
 >>> p.shirt_size
 'L'
 >>> p.get_shirt_size_display()
 'Large'
```

- 还有很多可选项，如 `default`,`help_text`,`primary_key`,`unique`等，使用时需要查询。

## 3.3 Automatic primary key fields
如果不显式指定一个primary key的话，django会自动增加一个如下的字段，生成一个自增型的id主key。
```python
id = models.AutoField(primary_key=True)
```
每个模型model都需要一个primary key，不管是显式指定还是自动生成的。

## 3.4 长字段名 Verbose field names
1. ForeignKey, ManyToManyField and OneToOneField 以外的field, 直接在第一个参数处，写入长字段名，就是该字段的别名。比如 `first_name = models.CharField("person's first name",max_length=30)`，如果是 `first_name = models.CharField(max_length=30)`的话，显示为first_name。
2. ForeignKey, ManyToManyField and OneToOneField将第一个参数处，征用成了model名，所以需要显式使用verbose_name关键字，例如：
 ```python
 poll = models.ForeignKey(
     Poll,
     on_delete=models.CASCADE,
     verbose_name="the related poll",
 )
 sites = models.ManyToManyField(Site, verbose_name="list of sites")
 place = models.OneToOneField(
     Place,
     on_delete=models.CASCADE,
     verbose_name="related place",
 )
 ```

## 3.5 关系 Relationships
Django中提供了三种常见的关系，N:1,N:M和1：1。
### ① N:1 关系
使用` django.db.models.ForeignKey`去进行定义，我们将它从另一个model中include进来，当作另一个field类型。例如上面的Album和Musician的关系，多个Album可能出自一个Musician。

```python
artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
```
ForeignKey有很多选择项参数，例如上面的on_delete，默认在主表记录被删除情况下，这个记录也被删除。
这个字段非常重要，详细的参考 [ForeignKey中的详细定义](https://docs.djangoproject.com/en/1.11/ref/models/fields/#arguments)。

### ② N:M 关系
使用 `ManyToManyField`去定义，例如下面代码，一个person可能多个Group，一个Group也可能多个Person。

```python
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
```


 ### ③ 1：1 关系
使用`OneToOneField`去进行定义，将它看作一个field处理。例如下面代码，一个Restaurant有一个Place，一个Place也只有一个Restaurantself。
> 只是不太明白为什么这样使用？ 纯粹只是想将model变小么？将原本一个model中按类型，分成几个不同类型的model？

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name


```


## 3.6 Models across files
除了将现有的field 用foreign key 关联到当前的model外，还可以import外部的model，并使用。
例如:

```python
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

```

## 3.7 Field Name命名限制
1. 不能使用python保留字(废话^_^)
2. 不能使用多余一个的下划线 _ ,因为  __ 会被django视为语法错误。

# <i class="fa fa-cubes" style="font-size:1em;"></i> 4. Meta options
通过`class Meta`，可以给model定义meta data。

```python
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
```

Model的matadata定义了field外的任何属性，例如排序选项`ordering`，数据表名`db_table`等。
更多详细参考[meta option all](https://docs.djangoproject.com/en/1.11/ref/models/options/)


# <i class="fa fa-cubes" style="font-size:1em;"></i> 5. 模型属性Model Attirbutes
一个model最重要的attribute就是Manager，它是一个接口用来提取存储在数据库中的实例instance。
如果没有定义Manager，则其默认名为objects,Mangers 只能通过model类去访问，不能通过model的实例访问。

1. 利用默认objects提取数据
```python
pData = Person.objects.all()
```

2. 也可以自己定义Manager，如下:
```python
class Person(models.Model):
    #...
    people = models.Manager()
```
如果继续用`Person.objects`提取数据的话，会产生 `AttributeError`的异常，需要使用`Person.people.all() `获取Person的objects list。

3. Manager是model class类的属性，只能通过model class访问，不能使用instance访问.(类似java中class的static变量，这个变量只有一个，在class类被创建时就存在)，看如下实例代码：
```
>>> p = Person(first_name="wang",last_name="ling",shirt_size="S")
>>> p.shirt_size
'S'
>>> p.get_shirt_size_display()
'Small'
>>> p.objects
Traceback (most recent call last):
 File "<console>", line 1, in <module>
 File "C:\Users\61041150\djangoproject\myvenv\lib\site-packages\django\db\model
s\manager.py", line 186, in __get__
   raise AttributeError("Manager isn't accessible via %s instances" % cls.__nam
e__)
AttributeError: Manager isn't accessible via Person instances
>>>
```
在Django shell中，创建了一个Person的实例，通过实例p，可以直接获取其属性`shirt_size`,也可以访问其方法`get_shirt_size_display()`。
但是如果直接访问objects属性 `p.objects`，就会出现上面的错误`Manager isn't accessible via Person instances`。


# <i class="fa fa-cubes" style="font-size:1em;"></i> 6. 模型方法Model methods
在model中添加一个自定义的方法，就是给objects(参考上面的定义，一个table中的所有记录)添加一个"row-level"即`行级别`的处理函数。
Manager中的方法是处理`表级别`的处理函数(类似于java中类的静态方法，只能被class调用)，而model的方法作用于特定的model实例，即表中的一行数据，类似于类的一个具体对象(类似于java中类的实例方法，被对象所调用)。
>※This is a valuable technique for keeping business logic in one place – the model.

修改后Person模型如下：

```python

class Person(models.Model):
    first_name = models.CharField("person's first name",max_length=30)
    last_name = models.CharField("person's last name",max_length=30)

    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,default="M")

    birth_date = models.DateField(null=True)

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

```
- 上面有两个自定义函数，都是针对一个特定的model实例进行操作的，其self就是一个实例。
- 注意第二个自定义函数`full_name(self)`，前面有 `@property`标记符，这个允许我们将 full_name作为一个属性使用。参考如下代码：
```
>>> from dpjTest.models import Musician,Person,Album
>>> p = Person(first_name="wang",last_name="haha",shirt_size="S")
>>> p.first_name
'wang'
>>> p.full_name
'wang haha'
```
在这里参照所有的model预定义函数[model的预定义方法](https://docs.djangoproject.com/en/1.11/ref/models/instances/#model-instance-methods)
，大部分预定义函数都可以重写定义，下面两个是几乎都需要重新定义的。

- `__str__()` (Python 3)
这个是python中的魔法方法，能将一个object作为一个unicode的字符串表示出来。(java中也有类似的方式，具体忘了...),但这个方法需要自己去重新定义，默认的方式基本没什么用处。

- get_absolute_url()
告诉Django怎么去计算一个Object的URL。例如:
```python
def get_absolute_url(self):
    return '/%s/' % self.name
```

## 6.1 重载预定义的Model方法
另外，还有一些model 方法封装了数据库的行为，可能需要重新定义，比如save()，delete()。
```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
        do_something_else()
```
上面自定义了save函数，注意一定要`调用其父类的save函数`。


## 6.2 执行SQL语句
除了django封装后的api可以访问数据库外，还能使用原生SQL,更详细参考[原生SQL查询](https://docs.djangoproject.com/en/1.11/topics/db/sql/).

- 示例1

```python
>>> lname = 'Doe'
>>> Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
```

- 示例2

```python
from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row
```

# <i class="fa fa-bell" aria-hidden="true"></i> 下一步
1. 创建一个专题，专门讲述 model的relationship。
2. 关于[Model inheritance](https://docs.djangoproject.com/en/1.11/topics/db/models/#model-inheritance),限于篇幅，在下一篇讲解。
