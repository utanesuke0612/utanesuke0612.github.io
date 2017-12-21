---
layout: post
title: DjangoBasic-02-显示出第一个网页
date: 2017-08-12 12:45:59
categories: Python
tags: Django
---
* content
{:toc}

>[DjangoGirls tutorial](https://tutorial.djangogirls.org/zh/django_urls/)的入门课程,这个课程非常浅显易懂，完全小白只要参考这个系列，也能做出自己的博客网站。

本系列参考上面的tutorial，进行了部分修改和增补，系列目录如下,代码参考 [here](https://github.com/utanesuke0612/pythonBlog)：
1.  [运行环境部署](https://utanesuke0612.github.io/2017/08/11/DjangoBasic_01/)
2.  [显示出你的第一个网页](https://utanesuke0612.github.io/2017/08/12/DjangoBasic_02/)
3.  [模板扩展-blog详情页面](https://utanesuke0612.github.io/2017/08/12/DjangoBasic_03/)
4.  [Django表单](https://utanesuke0612.github.io/2017/08/15/DjangoBasic_04/)
5.  [添加草稿/发布/删除/编辑功能](https://utanesuke0612.github.io/2017/08/18/DjangoBasic_05/)
6.  [让网站更安全](https://utanesuke0612.github.io/2017/08/18/DjangoBasic_06/)
7.  [给网页添加评论](https://utanesuke0612.github.io/2017/08/18/DjangoBasic_07/)

---
# <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>**注意：**
Django的标签导致Jekyll无法编译，都修改为了`[%`和`[{`，使用时需要替换将`[`替换为`{`！

# 1. 创建应用程序

如下是创建app到admin后台管理的过程：
![image](https://user-images.githubusercontent.com/18595935/29241621-6201626e-7fb8-11e7-819a-3ebdf2b588f9.png)

在第一节中，已经创建了一个django的project，但是这个project中没有任何应用程序，现在我们要在project内部创建应用程序。

>在django中有两个概念需要弄清楚。一个是工程（project）的概念，一个是应用（application）的概念。 它们的关系是：一个工程中包含多个应用。每个应用都是独立的，应用通过setting.py注册到工程中来就可以使用了。 这样可以解耦合，并且好的应用也可以复用。很好的模块化设计！

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

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)
```


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

---

> django中实现一个功能,只需要三个步骤即可，这里叫它三部曲，即如下的4-6步.
> 1. 定义urls映射
> 2. 定义views视图
> 3. 定义HTML模板文件

# 4. 定义Django urls映射

## 1. URL在Django中是如何工作的

![image](https://user-images.githubusercontent.com/18595935/29241961-25a38318-7fbf-11e7-95d1-599232ae7824.png)

1. 客户端的请求，先经过mysite的url处理，这个是网站的入口，所有的请求最开始都通过它处理。
2. 然后处理进一步分流，交给blog的urls处理，blog是project下面的一个app模块，blog下的urls.py对URL进行匹配，分配给对应的view(post_list)去处理。
3. 在view中进行逻辑处理，获取对应的model数据，组织成html文件，返回给客户端。下面的例子中，直接render即渲染了一个静态的html文件。

## 2. 添加URL的处理代码
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


# 5. 定义view视图
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

# 6. 定义HTML模板文件
在blog/templates/blog 目录下，创建post_list.html模板文件，并在文件中写入:
```html
<html>
	<p>Hi there!</p>
	<p>It works!</p>
</html>
```
这样，在上面第5步中就可以找到对应的html文件了。

# 7. 【重要】动态数据
本节讲述Django如何连接到数据库，并将数据存储在里面。

## 1. Django ORM 和 QuerySets（查询集）
QuerySet 是给定模型的对象列表（list），类似于数据库中的一个Table。允许从数据库中读取数据，对其进行筛选以及排序。
运行 `(myvenv) ~/djangogirls$ python manage.py shell `可以开启Django shell，输入Django shell命令可以直接操作QuerySets。

```python
# 导入Post的model，查询所有对象以及创建对象
>>> from blog.models import Post
>>> Post.objects.all()
>>> Post.objects.create(author=me, title='Sample title', text='Test')
# 上面会出错，因为我们给author传递了变量me，但是没有给me这个user赋值。

# 查询数据库中的用户并获取一个用户实例
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> me = User.objects.get(username='ola')

# 接着运行上述Post的create就OK了，类似于SQL的insert
>>> Post.objects.create(author=me, title='Sample title', text='Test')
```

## 2. 筛选对象
```python
# 筛选出所有ola为user的Post
>>> Post.objects.filter(author=me)

# 包含在  title  字段标题的所有帖子，返回了上面创建的Post
>>> Post.objects.filter(title__contains='title')
<QuerySet [<Post: Sample title>]>

# 如果想尝试获取所有publish的Post
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())[]
# 但是我们上面只是create了Post还没有Publish，故获得的是空集

# 先获取指定对象，在用publish将其发布，就可以获取pulished的Post了
>>> post = Post.objects.get(title="Sample title")
>>> post.publish()
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: Sample title>]>

```

> 注在 title  与  contains  之间有两个下划线字符 ( _ )。 Django 的 ORM 使用此语法来分隔字段名称 （"title"） 和操 作或筛选器 （"contains"）。


## 3. 对象排序
```python
>>> Post.objects.order_by('created_date')

# 反向排序
>>> Post.objects.order_by('-created_date')

# 链式组合，先获取再排序
>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
```

## 4. 使用模板标签展示动态数据

我们最终的目的是，获取一些内容 （保存在数据库中的模型） 然后在我们 的模板中很漂亮的展示。这就是view应该做的，连接模型models和模板html文件。

 - view中获取需要的模型model数据，`blog/views.py` 中添加代码如下。

```python
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

 - html模板文件中解析post模型，并显示。

```python
<div>
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>

  [% for post in posts %}
        <div>
            <p>published: [{ post.published_date }}</p>
            <h1><a href="">[{ post.title }}</a></h1>
            <p>[{ post.text|linebreaksbr }}</p>
        </div>
  [% endfor %}
```


 1. 用模板标签在HTML中显示变量，` [{ posts }}`。
 2. `% for %} 和 % endfor %} `之间的内容将会被Django对象列表中的每个对象所代替。
 3. `|linebreaksbr`通过一个过滤器，使得行间隔编程段落。

至此，我们就将model中的数据，呈现到浏览器中了，效果如下：

![image](https://user-images.githubusercontent.com/18595935/29245595-782dddfe-8019-11e7-9611-3ee515a3f4fe.png)



# 8. 用CSS美化网页
在blog应用的目录下创建一个名为static的文件夹及子文件夹和css文件，创建后目录结构如下：

```
    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    │ 		└─── css
    │             └─── blog.css
    └── mysite
```
在css中添加sample代码
```css
h1 a {
        color: #FCA205;
    }
```

在使用静态css文件之前，需要在django中配置静态文件，在[DjangoBasi-01-环境部署](https://utanesuke0612.github.io/2017/08/11/DjangoBasic_01/)中，
服务器部署Django生成project后，已经设定了static文件Root配置。


修改对应html文件,body部分。没有修改
```html
 [% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="[% static 'css/blog.css' %}">
        </head>
......
    </html>
```
1. 告诉HTML 模板，添加了一些 CSS`[% load staticfiles %}`
2. head中引入刚才的css文件`<link rel="stylesheet" href="[% static 'css/blog.css' %}">`

最终，继续修改css，添加其他样式，html文件中的body部分修改为如下：

```html
<div class="content container">
        <div class="row">
            <div class="col-md-8">
                [% for post in posts %}
                    <div class="post">
                        <div class="date">
                            [{ post.published_date }}
                        </div>
                        <h1><a href="">[{ post.title }}</a></h1>
                        <p>[{ post.text|linebreaksbr }}</p>
                    </div>
                [% endfor %}
            </div>
        </div>
    </div>

```
最终呈现如下的效果
![image](https://user-images.githubusercontent.com/18595935/29245645-b19f8fe0-801b-11e7-8f67-ba94d8ad1d87.png)

# 参考:从url请求到返回动态html文件的流程(MTV结构)
![image](https://user-images.githubusercontent.com/18595935/29245508-3fddc7ae-8017-11e7-9e0f-6b33bb52c606.png)

## django的MTV模式

django的结构，一般我们称之为MTV模式：

 - M 代表模型（Model），即数据存取层。该层处理与数据相关的所有事务：如何存取、如何确认有效性、包含哪些行为以及数据之间的关系等。
 - T 代表模板(Template)，即表现层。该层处理与表现相关的决定：如何在页面或其他类型文档中进行显示。
 - V 代表视图（View），即业务逻辑层。该层包含存取模型及调取恰当模板的相关逻辑。你可以把它看作模型与模板之间的桥梁。
那么通常意义的控制器Controller去哪里了呢，那就是我们上面所讲的urls.py配置文件。
一句话总结：**URLconf+MTV构成了django的总体架构**。

结合上图和实际代码，详细的处理流程如下:

## ① 用户访问浏览器，输入URL

## ② 寻找对应HTTPServer

网络连接，DNS解析等，最终请求request到达指定IP的HTTPServer

## ③ HTTPServer分配请求

HTTPServer监听到端口的请求，将请求提供给指定的APP

## ④ Middleware(作用不明)


## ⑤ 分配request给指定View

到达指定程序的mysite/urls.py入口，解析URL，分配请求给指定View

- 初始解析

```python
url(r'^admin/', include(admin.site.urls)),
url(r'', include('blog.urls')),
```

- 指定app的url解析

```python
from django.conf.urls import url
from . import views  #表示从当前目录当如views
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]
```

## ⑥ 向Model请求数据


指定的View收到请求后，向Model请求数据（实际上是获取存储在DB的数据）

```python
def post_list(request):
	posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

```

## ⑦ 模板文件生成静态html文件

View将获取到的数据传递给Template模板文件，模板通过标签对Model中的数据进行重组，生成静态HTML文件

- 将Model传递给Template
```python
 render(request, 'blog/post_list.html', {'posts':posts,'text':"lj"})
```

- Template中解析数据
```html
	 [% for post in posts %}
	            <div>
	                <p>published:[{post.published_date}}</p>
	                <h2><a href="">[{post.title}}</a></h2>
	                <p>[{post.text|linebreaksbr}}</p>
	                <p>[{text}}</p>
	            </div>
	 [% endfor %}
```

## ⑧ 返回最终的静态html

View接受到生成的静态HTML文件(用model数据替换了模板中的标签后的html)，并返回给WebServer。
