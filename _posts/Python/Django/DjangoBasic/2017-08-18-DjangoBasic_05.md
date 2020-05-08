---
layout: post
title: DjangoBasic-05-添加草稿/发布/删除/编辑功能
date: 2020-05-02 00:01:05
categories: Python
tags: Django
---
* content
{:toc}


>[DjangoGirls tutorial](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/)的入门课程(扩展篇),这个课程非常浅显易懂，完全小白只要参考这个系列，也能做出自己的博客网站。

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

>在第四节中，创建表单，并关联到新建和编辑post的page上，能验证表单正确性，最终保存到数据中。

# 1. 将新的post保存为drafts
将 post_new和post_edit 方法中的`post.published_date = timezone.now()`去掉，这样每次修改或追加后都没有published_date属性。

# 2. 追加浏览drafts page的功能
按照追加一个功能的流程:

- 入口追加，在base.html中添加显示按钮

```
<a href="[% url 'post_draft_list' %}" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>
```

- urls.py中添加url解析

```python
url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
```

- 添加对应的view

```python
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
```

- 添加模型文件 `blog/templates/blog/post_draft_list.html`

```python
[% extends 'blog/base.html' %}

[% block content %}
    [% for post in posts %}
        <div class="post">
            <p class="date">created: [{ post.created_date|date:'d-m-Y' }}</p>
            <h1><a href="[% url 'post_detail' pk=post.pk %}">[{ post.title }}</a></h1>
            <p>[{ post.text|truncatechars:200 }}</p>
        </div>
    [% endfor %}
[% endblock %}

```

上述的过程就完成了从页面右上角点击，显示drafts页面的功能。

# 3. 添加发布button
既然在发布post的流程上增加了一步，那么对应程序也需要对应。这里在post_detail页面上要追加publish的button。
> 回忆一下，post_new和post_edit最后点击submit后，都跳转到了post_detail页面。

将post_detail页面修改为如下，判断是否发布了，如果是没有published_date的post，则显示按钮Publish:
```python
[% if post.published_date %}
    <div class="date">
        [{ post.published_date }}
    </div>
[% else %}
    <a class="btn btn-default" href="[% url 'post_publish' pk=post.pk %}">Publish</a>
[% endif %}

```
同样，因为追加了该button，那也需要添加该button的处理过程。

- 添加url解析

```python
url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
```

- 添加post_publish的view

```python
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

```
注意上面调用了post模型的publish()函数

- 添加publish函数的处理

```python
def publish(self):
    self.published_date = timezone.now()
    self.save()
```

通过上述流程，在post_detail页面中，判断后添加了publish按钮，点击后添加published_date，保存到数据库中。

# 4. 删除post
整个处理流程，与上面publish的处理类似。

- 添加入口，在post_detail页面中添加delete的按钮

```python
<a class="btn btn-default" href="[% url 'post_remove' pk=post.pk %}"><span class="glyphicon glyphicon-remove"></span></a>
```
- URL解析

```python
url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
```

- 添加view的处理

```python
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

```

与publish处理类似，view处理完毕后并不需要跳转到模型文件，故不需要添加，这里重定向到post_list视图。

通过上述的过程，就完成了:
- 添加了drafts按钮和对应功能
- 添加了publish按钮和对应功能
- 添加了delete按钮和对应功能
