---
layout: post
title: DjangoBasic-06-让网站更安全(login处理)
date: 2020-05-02 00:01:06
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

>第五节中，我们完成了: ①添加了drafts按钮和对应功能 / ②添加了publish按钮和对应功能 / ③添加了delete按钮和对应功能

目前为止，我们只是在按钮的显示上面，如publish/new/delete按钮上，添加了用户验证，如下代码

```python
[% if user.is_authenticated %}
...
[% endif %}
```

但是如果用户从url直接进入编辑或是新建post呢，一样可以进入对应的页面。(但是无法保存，因为保存的时候需要添加user，而此时没有user，则会引发异常)
```
Exception Value:
Cannot assign "<SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x03B351F0>>": "Post.author" must be a "User" instance.
```

# 1.授权post的编辑和追加
在这里我们需要使用Django的装饰器`@login_required`。
- 在`blog/views.py`中，引入需要的包

```python
from django.contrib.auth.decorators import login_required
```
- 在需要添加保护的view上添加上面的装饰器，需要保护的view有`post_new`, `post_edit`, `post_draft_list`, `post_remove` and `post_publish`。

```python
@login_required
def post_new(request):
    [...]
```
添加上述装饰器后，在未login的情况下，无法访问 `localhost:8000/post/new/`，访问后出现下面的错误页面。
```python
Page not found (404)
Request Method:	GET
Request URL:	http://localhost:8000/accounts/login/?next=/post/new/
```

# 2. 添加login画面
- 在`mysite/urls.py`中，添加如下两行，进行url解析

```python
from django.contrib.auth import views

url(r'^accounts/login/$', views.login, name='login'),

```
上面将这个解析到的url，交给 django.contrib.auth的login view 去处理。

- 添加对应的模型文件，新建文件`blog/templates/registration/login.html`,添加代码如下

```python
[% extends "blog/base.html" %}

[% block content %}
    [% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    [% endif %}

    <form method="post" action="[% url 'login' %}">
    [% csrf_token %}
        <table>
        <tr>
            <td>[{ form.username.label_tag }}</td>
            <td>[{ form.username }}</td>
        </tr>
        <tr>
            <td>[{ form.password.label_tag }}</td>
            <td>[{ form.password }}</td>
        </tr>
        </table>

        <input type="submit" value="login" />
        <input type="hidden" name="next" value="[{ next }}" />
    </form>
[% endblock %}
```
这里提交后，全部交给Django的模块去进行处理，不需要自己去users模型中去验证用户名和密码。

- 最后，在`mysite/settings.py` 中加入 `LOGIN_REDIRECT_URL = '/'`，这样在logout的状态下访问`http://localhost:8000/post/new/`，会自动跳转到`http://localhost:8000/accounts/login/?next=/post/new/`。
- 上面的实现原理不明白★。


# 3. 改进layout
修改base.html中右上角的按钮处理代码，修改为如下：
```python
[% if user.is_authenticated %}
          <a href="[% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
          <a href="[% url 'post_draft_list' %}" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>
      [% else %}
          <a href="[% url 'login' %}" class="top-menu"><span class="glyphicon glyphicon-lock"></span></a>
      [% endif %}
```
当没有login的时候显示lock按钮。


# 4. 继续改进user登录部分
在上面 判断了如果是授权用户的分支中，加入欢迎语句和logout功能:
```python
<p class="top-menu">Hello [{ user.username }} <small>(<a href="[% url 'logout' %}">Log out</a>)</small></p>
   [% else %}
```

- 处理logout - url匹配处理
在mysite/urls.py中，加入`url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),`

后续logout处理，全部交给Django，特别方便。

---

本节增加了用户验证过程，并改进了UI，添加了login用的forms，真正的login和logout的view处理-即逻辑处理，都是Django自身完成的。
