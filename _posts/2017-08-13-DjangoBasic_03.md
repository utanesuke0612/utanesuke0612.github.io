---
layout: post
title: DjangoBasi-03-模板扩展-blog详情页面
date: 2017-08-12 22:45:59
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
# <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>**注意：**
Django的 标签导致Jekyll无法编译，都修改为了[%，使用时需要替换！

> 本节中，扩展Base模板，实现点击主页面Postlist的标题后进入PostDetail页面。

# 1. 创建一个基础模板
一个网站往往有统一的风格，即相同的header / leftnavi / footer 等部分，共同组成网页比较统一的布局。
一个基础模板是最重要的模板，你扩展到你网站的每一页。

1. 创建一个base.html文件到blog/templates/blog/:
```
    blog
    └───templates
        └───blog
                base.html
                post_list.html
```
先将post_list.html中代码复制过来，再将变化的post_list部分删除，用标签替换，body部分最终代码如下：
```html
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                [% block content %}
                [% endblock %}
                </div>
            </div>
        </div>
```
用上面的 block - endblock 的内容，替换了 for - endfor 之间的代码。

2. 修改对应的post_list.html文件
```python
[% extends 'blog/base.html' %}
   [% block content %}
       [% for post in posts %}
           <div class="post">
               <div class="date">
                   [{ post.published_date }}
               </div>
               <h1><a href="">[{ post.title }}</a></h1>
               <p>[{ post.text|linebreaksbr }}</p>
           </div>
       [% endfor %}
   [% endblock content %}
```
最开始的extends声明了扩展自 base.html文件，另外定义了名为content的block。
在base中可以引用多个content，在post_list中，也可以定义多个block。

---

>下面的2-5 步，描述了从创建新的url，到匹配url到对应view，新建对应的view并匹配到对应的模板html，创建对应的模板html。


# 2. 创建模板链接
修改上面的post.title部分为` <h1><a href="[% url 'post_detail' pk=post.pk %}">[{ post.title }}</a></h1>`
即当点击post_title的时候，跳转到这里指定的href，这里href由 url标签来生成真正的url链接。
这时如果访问http://127.0.0.1:8000/ ，会得到如下的错误:
![image](https://user-images.githubusercontent.com/18595935/29250583-b3283f88-807f-11e7-8ced-bee0bfd91dbf.png)
这是预料之中的，因为我们没有名为post_detail 的 URL 或 视图,在下一部分中会创建名为post_detail的url。

# 3. 创建文章详细页面的URL
在blog/urls.py中添加一行记录，添加后如下:
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
```
- `(?P<pk>[0-9]+)`表示将 post/ 后面的数字部分，传递给变量pk，然后这个变量pk接着传递给对应的view。
- 后面是`name='post_detail'`，应该与上面的模板链接匹配。
- 接收到符合这中情况的url，就将请求交给 post_detail这个view处理。
- 通常有两种情况可以访问到post_detail页面
  - 通过点击title，产生name为post_detail的url，将request传递给对应的view
  - 直接通过访问`http://localhost:8000/post/9/`，也能将request传递给对应的view

上面将request传递给了view，那么接着在blog的views.py中添加post_detail view。


# 4. 增加文章详细页面的视图
打开 blog/views.py ，添加如下:
```python
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

上面的视图中，将request继续提供给post_detail.html模板文件。



# 5. 为文章详细页面增加模板
在blog/templates/blog 中创建一个文件，叫做 post_detail.html .
```python
[% extends 'blog/base.html' %}

   [% block content %}
       <div class="post">
           [% if post.published_date %}
               <div class="date">
                   [{ post.published_date }}
               </div>
           [% endif %}
           <h1>[{ post.title }}</h1>
           <p>[{ post.text|linebreaksbr }}</p>
       </div>
   [% endblock %}
```

通过上述步骤，最终实现了输入`http://localhost:8000/post/9/`，或是从list的title点击，都可以访问到post_detail页面。如下图
![image](https://user-images.githubusercontent.com/18595935/29250847-c53b0c14-8084-11e7-8390-a4788a850b4c.png)
