---
layout: post
title: (未完)DjangoBasi-02-显示出第一个网页
date: 2017-08-12 11:45:59
categories: Django
tags: Django python
---
* content
{:toc}

>[DjangoGirls tutorial](https://tutorial.djangogirls.org/zh/django_urls/)的入门课程,这个课程非常浅显易懂，完全小白只要参考这个系列，也能做出自己的博客网站。

本系列参考上面的tutorial，进行了部分修改和增补，系列目录如下：
1.  运行环境部署
2.  显示出你的第一个网页
3.  模板扩展-blog详情页面
4.  Django表单
5.  添加草稿/发布/删除/编辑功能
6.  让网站更安全
7.  给网页添加评论
8.  总结-从URL请求到动态HTML内容返回的流程

---



# 1. 创建应用程序

如下是创建app到admin后台管理的过程：
![image](https://user-images.githubusercontent.com/18595935/29241621-6201626e-7fb8-11e7-819a-3ebdf2b588f9.png)

在第一节中，已经创建了一个django的project，但是这个project中没有任何应用程序，现在我们要在project内部创建应用程序。

在命令行中执行以下命令 (从 manage.py  文件所在的 djangogirls  目录)：
```
(myvenv) ~/djangogirls$ python manage.py startapp blog
```

创建完毕后，新增文件夹blog如下所示
```
└── blog
	├── migrations
	|       __init__.py
	├── __init__.py
	├── admin.py
	├── models.py
	├── tests.py
	└── views.py
```

接着在  mysite/settings.py 的INSTALLED_APPS 中，在它下面添加一行 'blog'，告诉Django要使用这个app。  



# 2. 创建文章模型和数据表

## 1. 创建一个博客文章模型
打开  blog/models.py ，从中删除一切并编写这样的代码：

```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```
上面好比是一个数据库中table的定义，author / .. / published_date 是数据库的字段，定义了字段类型和限制及默认值等。
另外还定义了Post类的两个方法。

## 2. 在数据库中为模型创建数据表

在这里将上面新创建的模型添加到数据中。分为如下两步:

1. 执行 `python manage.py makemigrations blog`，让django知道模型发生了变更，重新生成类似于SQL的建表文件
```
(myvenv) ~/djangogirls$ python manage.py
makemigrations blog Migrations for 'blog':
  0001_initial.py:
  - Create model Post
```

2. 执行上面完成的迁移文件，`python manage.py migrate blog`。
```
(myvenv) ~/djangogirls$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Rendering model states... DONE
  Applying blog.0001_initial... OK
```
这样Post模型现在已经在我们的数据库里面了!

# 3. admin 管理后台

## 1. 导入（包括）了前一章定义的Post模型
打开blog/admin.py文件，并替换其中的文件像这样：
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
让我们的模型在admin页面上可见，我们需要使用admin.site.register(Post)来注册模型.

## 2. 创建admin的用户
为了登录http://127.0.0.1:8000/admin/，还需要创建账号(username/password).
```
(myvenv) ~/djangogirls$ python manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```
返回到你的浏览器，用你刚才的超级用户来登录，然后你应该能看到Django admin的管理面板。


# 4. Django urls

## 1. URL在Django中是如何工作的

![image](https://user-images.githubusercontent.com/18595935/29241961-25a38318-7fbf-11e7-95d1-599232ae7824.png)

 - 客户请求会先经过mysite/urls.py处理。例如，访问 'http://127.0.0.1:8000/' 的请求转到 blog.urls，并看看那里面有没有进一步的指示。

```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
```
>写正则表达式时，记得把一个 r 放在字符串的前面。 这告诉 Python，这个字符串中的特殊字符是为正则表达式准备的，而不是为 Python 自身准备的。

- 创建一个新的 blog/urls.py 空文件,并加入如下代码:

```python
from django.conf.urls import url
from . import views #

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
```
在上面的的代码中，分配了一个叫post_list的view给`^$`的URL。^$在正则表达式中意思是开始和结尾，即URL为空的话，就会被分配给post_list的view去处理。
>只有 'http://127.0.0.1:8000/' 后面的部分会被解析。如果后面的部分为空，即是空字符串被解析。

最后的部分，name='post_list' 是 URL 的名字，用来唯一标识对应的 view。 它可以跟 view 的名字一样，也可以完全不一样。 在项目后面的开发中，我们将会使用命名的 URL ，所以在应用中为每一个 URL 命名是重要的。我们应该尽量让 URL 的名字保持唯一并容易记住。

浏览器里打开 http://127.0.0.1:8000/  是如下页面，原因是view还没有创建。
![image](https://user-images.githubusercontent.com/18595935/29242063-eb562e52-7fc0-11e7-9dd2-5624ccd5eae3.png)


# 5. Django视图
view是存放应用逻辑的地方。它将从你之前创建的 模型中获取数据，并将它传递给模板(html)。
视图都被置放在views.py文件中。我们将加入我们自己的views到blog/views.py文件。
代码如下:
```python
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
```
render 方法渲染模板 blog/post_list.html.
转到 http://127.0.0.1:8000/,依然出错，原因是我们还没有创建模板文件。

![image](https://user-images.githubusercontent.com/18595935/29242097-68c0372a-7fc1-11e7-96d5-893bf7fcadca.png)


# 6. HTML模板文件

# 7. 动态数据

# 8. 用CSS美化网页

# 参考:从url请求到返回动态html文件的流程
