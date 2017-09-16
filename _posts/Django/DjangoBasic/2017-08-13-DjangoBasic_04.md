---
layout: post
title: DjangoBasic-04-重要-Django表单
date: 2017-08-15 22:45:59
categories: Django
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
1. Django的标签导致Jekyll无法编译，都修改为了`[%`和`[{`，使用时需要替换将`[`替换为`{`！
2. **`本节非常重要！`**

>截至到第三节，我们已经将model中的动态数据显示到网页上，并通过点击title实现了查看post详情。在实现方式上，应用了模板和CSS等。通过本节，继续扩展我们的功能，添加post的表单form，实现post的新增和编辑。

# 1. 创建表单
通过Django自带的Admin也能实现对model的操作，但是很难去自定义，因为结构已经固定。通过forms，我们可以完全自定义我们的页面。

首先，在blog目录下创建forms.py表单定义文件。

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
```
 - 首先导入表单，然后导入Post模型。
 - `forms.ModelForm`告诉Django这个表单时一个ModelForm
 - class Meta，在这里我们告诉Django哪个模型会被用来创建这个表单（model=Post）。
 - fields，说明有哪些字段能被显示出来。

> forms类似于Models，这个只在程序启动时，或是变化时被调用。在这里添加了一个print()函数，只在上述情况下才被调用，即使点击New Post也不会被调用。

---
>创建了forms后，接下来的工作，与之前创建Detail页面是类似的，
>  - 创建入口的URL
>  - URL匹配部分添加记录
>  - URL匹配到后，会跳到视图，故添加视图
>  - 视图会将数据返回给模板文件，故添加对应的模板文件
> 这里我们暂时把forms先理解为model。(Q:可以么？？)

# 2. 创建指向该表单的链接
添加新Post的链接入口，是在header的右上角，故我们在这里添加一个一行 ` <a href="[% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>`
即这里被点击后，会利用`post_new`去urls.py去进行匹配。

添加后完整的base.html文件为:

```python
[% load staticfiles %}
   <html>
       <head>
           <title>Django Girls blog</title>
           <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
           <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
           <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
           <link rel="stylesheet" href="[% static 'css/blog.css' %}">
       </head>
       <body>
           <div class="page-header">
               <a href="[% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
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
       </body>
   </html>
```

# 3. URL中添加对应记录
在`blog/urls.py`中，添加一条新的记录：
` url(r'^post/new/$', views.post_new, name='post_new'),`
1. 即上面通过post_new匹配之后，会生成一个post/new的url，当然我们也可以不生成链接，直接在浏览器中输入.../post/new，也可以到达这里
2. 匹配到了之后，继续将request转发给post_new 这个view。

# 4. 添加post_new视图
在`blog/views.py`中，加入如下代码：
```python
from .forms import PostForm

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```
这里先导入了上面创建的新的PostForm，然后将这个form作为参数传递给模板文件。
这时form是一个完全新创建的空form，注意这里为类PostForm创建对应的方式，非常简洁。

# 5. 【重要】添加post_edit模板文件
在`blog/templates/blog`目录下创建一个文件post_edit.html。html文件代码如下

```python
[% extends 'blog/base.html' %}

    [% block content %}
        <h1>New post</h1>
        <form method="POST" class="post-form">[% csrf_token %}
            [{ form.as_p }}
            <button type="submit" class="save btn btn-default">Save</button>
        </form>
    [% endblock %}

```
1. 要展示表单，甚至需要一行 `[{ form.as_p }}`
2. forms要被 `<form method="POST">...</form>`标签所包含。
3. 完毕后，通过submit的button提交。
4. 最后在`<form ...>`标签后，我们需要加上`[% csrf_token %}`。 这个非常重要，因为他会让你的表单变得更安全！

# 6. 【重要】保存表单
当前`blog/views.py`,`post_new`中的视图内容是:

```python
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```
当我们提交表单的时候，都回到相同的视图，即下面两种情况，都会到post_new这个视图这里来处理。
1. 点击右上角的new post，经由url等最后到post_new视图这里。
2. 通过post_new视图到post_edit.html后，按下submit的button，又会回到post_new视图这里进行处理。

既然有两个入口都可以到达这个视图，而两个入口达到后视图给予的处理应该是不同的，第一次应该提供一个空白的forms表单，第二次填入数据后submit button被按下，应该进入post_deta页面。
代码如下
```python
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```
1. 首先判断这个request是不是post，是的的话说明从forms的submit button迁移过来的。
2. 然后将request中提交的数据取出。`request.POST`
3. `form.is_valid()`验证数据有效性，有效的话，先保存表单。
4. 使用form.save保存表单，我们添加一个作者（因为 PostForm 中没有author字段，然而这个字段是必须的！）
5. commit=False意味着我们还不想保存Post模型—我们想首先添加作者。(大多数情况下，当你使用form.save()时，不会使用commit=False)
6. post.save()会保留更改（添加作者），并创建新的博客文章！
7. 最后，通过`redirect('post_detail', pk=post.pk)`，将重定向到post_detail视图。

# 7. 验证表单
Model中自带方法对field的合法性，比如字段类型是否吻合，是否非空等进行了简单的验证，如果需要更详细的验证，需要在model中添加自定义方法。
详细的介绍参考Model部分。

# 8. 编辑表单
上面我们通过new post的button按下，进入空白的form page，新建了新的post，那如何对已有的post进行编辑呢，这个与新建post类似。
1. 首先在`post_detail.html`中加入一行，以添加一个button
```html
<a class="btn btn-default" href="[% url 'post_edit' pk=post.pk %}">
   <span class="glyphicon glyphicon-pencil"></span>
</a>
```
2. 后面的步骤类似,首先添加对url的匹配处理，在`blog/urls.py`中添加：
```python
url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
```
3. 在新建post的处理中，我们追加了post_edit的模板文件，这里编辑采用相同的模板。在views.py中添加如下的视图:
```python
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
```
上面的代码类似于之前的post_new视图，但不完全是，下面再贴出post_new视图的代码进行对比：
```python
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```

**异同点：**
   1. 【同】都判断了当前的request类型，针对post(通过forms的submit按钮发出的request)和get(post_new的+号新规按钮，post_edit的笔型icon；以及url直接输入)，做出了不同的处理。
   2. 【同】针对post和get的处理，最后的跳转都是一样，post后跳转到对应的详情post_detail页面；而get后的处理就是跳转到对应的post_edit页面，进入forms表单页面。
   3. 【同】针对修改后或是新加后的form，都会进行验证处理。验证处理完毕后，都会再补齐不足的信息。
   4. 【异】post_edit中，无论是post还是get，都会从url中取出pk字段，获取相应的post实例，并用该post实例去生成form。
   5. 【异】post_new中，如果是get类型的request，则生成空白的forms，如果是post类型的话，直接用request中的POST实例去生成form。
   6. 【异】注意post_edit中的`form = PostForm(request.POST, instance=post)`，与post_new稍有不同，如果跟post_new一样，去掉后面的`instance=post`的话，就会造成编辑一个的同时，新生成一个Post，比如我想把A编辑成A1，但是这里会在保留A的同时，新生成一个A1。

通过上面的处理，实现了Post的编辑。

# 9.  表单安全性
现在的代码中，没有对身份进行任何验证，也就会导致所有的人，都能看到右上角的新加 + 按钮，从而new post。下面的代码简单的进行了身份验证：
```python
[% if user.is_authenticated %}
        <a href="[% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    [% endif %}
```

但这仅仅让没有登录的人看不到new post的按钮而已，其实仍然可以从url直接进入，更多关于安全的操作，详细见后续章节。



# 参考：
1. `[% csrf_token %}`的意义和作用。
2.  java中的form表单提交实例代码如下：
```java
[form method="post" action="./Send">
  <input type="text" name="text1">
  <input type="text" name="text2">
  <input type="submit" value="POSTで送信">
[/form>
```
这里就有表单提交的目的地，即Send这个Servlet，交给它去处理forms过来的数据。
对比一下Django中的处理方式，还是Django比较简洁，但是是不是失去了一些灵活性呢。
3. 从new_post或是edit
_post的button被按下，到填写forms表单，然后按下submit，最后写入数据库的过程图如下：
![image](https://user-images.githubusercontent.com/18595935/29367043-9db0bab4-82d6-11e7-984d-2845d5956de1.png)
