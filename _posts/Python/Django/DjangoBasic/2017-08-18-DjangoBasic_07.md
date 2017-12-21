---
layout: post
title: DjangoBasic-07-重要-给网页添加评论
date: 2017-08-18 23:50:59
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
# <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>**注意`本节非常重要`：**
Django的标签导致Jekyll无法编译，都修改为了`[%`和`[{`，使用时需要替换将`[`替换为`{`！

>第六节中，我们增加了用户验证过程，并改进了UI，添加了login用的forms，真正的login和logout的view处理-即逻辑处理，都是Django自身完成的。

本节中，将实现给每个post添加comment的功能，需要添加comment的模型，并将comment模型与post关联，将涉及到模型之前的关联，以及如何取这些数据。

# 1. 创建comment模型
首先如果要对Post添加Comment的话，Comment就要作为数据存储在数据库中，需要有数据表，那么就需要有模型，如下是模型的定义。

```python
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
```

- Comment中包含了post外key，不同于数据库表中定义的外键，这里外key没有定义数据类型，最终在数据库中，会自动变成post_id，与post中主key相同。
- approved_comment字段，是个bool型的数据类型，在admin后台中，这个字段在界面上表现为checkbox，默认为非check状态。这个字段的作用类似于post中的published_date,即首次写了comment之后，还需要后续的approve才能在页面上显示。
- `related_name='comments'`字段，允许在post中访问其关联的comments，比如`post.comments.all`，这在模型的relationship中是1:N的关系，即一个post有多个comments。
- 在views中添加如下输出表结构的调试用语句:

```python
from django.db import connection

def my_album_sql():
    cursor = connection.cursor()
    cursor.execute('select * from sqlite_master where type="table"')
    results = cursor.fetchall()
    for createsql in results:
        print(createsql[4])

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    print(posts)
    my_album_sql()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

输出的表结构
```sql
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "text" text NOT NULL, "created_date" datetime NOT NULL, "published_date" datetime NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id"))
CREATE TABLE "blog_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" text NOT NULL, "created_date" datetime NOT NULL, "approved_comment" bool NOT NULL, "post_id" integer NOT NULL REFERENCES "blog_post" ("id"), "author" varchar(200) NOT NULL)
```
- 表名，是app名_模型名的结构
- 外key post，在表定义语句中字段名为post_id，参照了post表的主key id
- 两个表中，都被自动添加了主key id，自增型数值型。


# 2. 给新模型创建db表
- 告诉django，模型发生了变化，需要重新生成建表sql语句

```python
(myvenv) ~/djangogirls$ python manage.py makemigrations blog
Migrations for 'blog':
  0002_comment.py:
    - Create model Comment
```
- 执行上述生成的sql，创建数据表

```python
(myvenv) ~/djangogirls$ python manage.py migrate blog
   Operations to perform:
     Apply all migrations: blog
   Running migrations:
     Rendering model states... DONE
     Applying blog.0002_comment... OK
```

# 3. 在admin中注册新模型
在`blog/admin.py`中，添加如下代码，这样在admin后台中就能管理新模型的table了。

```python
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
```

# 4. 显示comments
- 在`blog/templates/blog/post_detail.html`页面底部，显示comment，将下面的代码加在`[% endblock %}`前。

```python
<hr>
[% for comment in post.comments.all %}
    <div class="comment">
        <div class="date">[{ comment.created_date }}</div>
        <strong>[{ comment.author }}</strong>
        <p>[{ comment.text|linebreaks }}</p>
    </div>
[% empty %}
    <p>No comments here yet :(</p>
[% endfor %}
```

- 改进css，在`static/css/blog.css`中添加comment用的样式：

```css
.comment {
    margin: 20px 0px 20px 20px;
}
```

- 在post_list.html中添加如下代码，使得在list页面post底部显示comments的条数：

```python
<a href="[% url 'post_detail' pk=post.pk %}">Comments: [{ post.comments.count }}</a>
```
> 1. comments中表有post外key，用来说明该comment是属于哪个post的，外key的关联名是`comments`，那这里就直接用`post.comments`获取post中关联comments了。
> 2. 这个技巧很有用，到时候在实际工作中，一个host表中有hw属性表作为外key，上过上面用户，可以取出某个hw属性记录的所有host。
> 3. 反过来，如果我想知道当前comment是在哪个post上，可以使用`comment.post.pk`，比如在如下代码中，

```python
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)
```
- 将该comment对应的post的pk传递给了post_detail视图，Django中的数据库操作还真是非常方便(前提是熟练使用)。


# 5. 写comments
通过上面的处理，能将comment显示在detail和list的页面中的，但我们还需要在detail中添加追加comment的处理。

- 在 `blog/forms.py`中，添加如下的forms：

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
```
同时在import中添加 `from .models import Post, Comment`

- 在post_detail.html页面中添加`<a class="btn btn-default" href="[% url 'add_comment_to_post' pk=post.pk %}">Add comment</a>`,即为每篇post后面添加用于评论的button。

- 类似于之前的处理，接着进行url的解析处理，在blog/urls.py中添加：

```python
url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
```

- 在view中添加对应的view:

```python
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
```
> 1. 这里进行表单的处理，同之前的new和edit一样，如果是点击add comment处理，则处理else中内容,生成form，并传递给模型文件。
> 2. 如果是form中按下submit，由于request类型是POST，则进行comment的处理，并重定向到post_detail视图。
> 3. 详细可以参考之前的表单章节。

- 添加上面需要的模型文件：

```python
[% extends 'blog/base.html' %}

[% block content %}
    <h1>New comment</h1>
    <form method="POST" class="post-form">[% csrf_token %}
        [{ form.as_p }}
        <button type="submit" class="save btn btn-default">Send</button>
    </form>
[% endblock %}
```

# 6. 添加comment的承认和删除功能
修改post_detail.html，添加两个按钮:

```python
[% for comment in post.comments.all %}
    [% if user.is_authenticated or comment.approved_comment %}
    <div class="comment">
        <div class="date">
            [{ comment.created_date }}
            [% if not comment.approved_comment %}
                <a class="btn btn-default" href="[% url 'comment_remove' pk=comment.pk %}"><span class="glyphicon glyphicon-remove"></span></a>
                <a class="btn btn-default" href="[% url 'comment_approve' pk=comment.pk %}"><span class="glyphicon glyphicon-ok"></span></a>
            [% endif %}
        </div>
        <strong>[{ comment.author }}</strong>
        <p>[{ comment.text|linebreaks }}</p>
    </div>
    [% endif %}
[% empty %}
    <p>No comments here yet :(</p>
[% endfor %}
```
- 如果该comment没有approve的话，则显示删除和approve的按钮。
- 类似的处理，添加url的处理，blog/urls.py中添加：

```python
url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
```
- 追加对应的view，添加如下：

```python
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
```

- 修改list页面下显示comment条数的处理：
当前显示了所有的comments，包含未承认的

```python
<a href="[% url 'post_detail' pk=post.pk %}">Comments: [{ post.comments.count }}</a>
```
修改后，只统计被承认后的comments，如下：

 ```python
<a href="[% url 'post_detail' pk=post.pk %}">Comments: [{ post.approved_comments.count }}</a>
 ```

 - 对应的，需要在model中添加对应的method，过滤出被approved的：

 ```python
 def approved_comments(self):
     return self.comments.filter(approved_comment=True)
 ```

---

# <i class="fa fa-comment" aria-hidden="true"></i> 后记
通过这7个系列的学习，完成了基本的纯文字博客，实现了用户的登录，新建blog，编辑删除blog，同时也有评论功能。掌握了如下的知识点:
1. Django框架的结构，以及各个部分的作用。
2. 掌握了从用户输入url提交request，到最终返回生成后的html给用户的全过程，以及django是如何处理这一过程的。
3. Django中如何使用model实现数据库表的操作的。
4. Django的MVT，model / view / templates 结构，以及这三部分的数据传递。
5. 通过Post和Comment，演示了两个关联model之间的数据组织关系，以及Django是如何处理模型并生成对应的SQL语句的。
