---
layout: post
title: DjangoBasic-03-模板扩展-blog详情页面
date: 2020-05-02 00:01:03
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

---

# 参考:url扩展处理(胶水:连接外部程序)

![image](https://user-images.githubusercontent.com/18595935/29279230-2cb18a1c-8152-11e7-92f0-319e3ab7a6d9.png)

>这是一个demo程序，实现当点击page页面上的button的时候，执行不同的poweshell脚本，最终输出脚本结果到Result.html页面。
处理流程如下：
 1. 对page上的button创建onclick响应　→　url处理
 2. urls.py中添加url的处理　→　view处理
 3. view中添加逻辑处理 → 逻辑处理
 4. vsetup.py中添加逻辑处理代码
 5. view中接受逻辑处理函数的return，并传递给模板html文件

## 1. 添加button的onclick响应
```html
<fieldset>
       <legend><h2>タスクのカテゴリ名2</h2></legend>
       [% for tool in toolsList %}
           [% if tool.Execute == "True"%}
               <h3>[{ tool.ID}}.[{ tool.Comment }}</h3>
               <button type="button"
                       onclick="location.href='[% url 'vSetup' Name=tool.Name %}'"
                       STYLE="color:red; background-color:white">
                   実行</button>
               <hr style="border:0;border-top:1px solid blue;">
           [% endif %}
       [% endfor %}
   </fieldset>
```
 - 点击后，使用url标签去生成实际的url，这里接住了urls.py去生成。
 - 为了使urls.py能识别这是它拿过去的请求，添加了`'vSetup'`，与urls中的`name='vSetup'`对应。
 - 另外，点击时需要识别点击的是哪个button，需要通过 `Name=tool.Name`传递参数。

## 2. urls.py中添加url处理
```python
urlpatterns = [
   url(r'^$', views.index,name='index'),
   url(r'^(?P<Name>[a-zA-Z0-9]+)/$', views.vSetup,name='vSetup'),
]
```
- 通过`name='vSetup',点击button后找到这里的url记录，通过`name`变量生成url，并把`name`变量传递给下一个view即vSetup中去。


## 3. view中添加逻辑处理
代码如下，通过从urls中传递过来的参数Name，判断该Name并调用对应的处理。
>如下的三个逻辑处理函数，存在于另一个py文件中，需要预先import。

```python
def vSetup(request,Name):
    message = ""
    if Name == "disconnect":
        message = disconnectHost()
    elif Name == "updateIP":
        message = updateHostIP()
    elif Name == "connect":
        message = connectHost()
    else:
        message = "エラー"

    return render(request, 'tools/result.html', {"message":message})

```

## 4. vSetup.py中添加逻辑处理代码
集中进行逻辑处理，注意updateHostIP函数，发挥了python的胶水特性，直接调用了PowerShell脚本。
```python
from django.shortcuts import render
from django.http import HttpResponse
import subprocess, sys

def disconnectHost():
    return "タスク1"

def updateHostIP():
    p = subprocess.Popen(["PowerShell.exe", "MyScripts\\ipcheck.ps1"], stdout=sys.stdout)
    p.communicate()
    return "タスク2"

def connectHost():
    return "タスク3"
```

## 5. view中接受逻辑处理函数的return，并传递给模板html文件
参考上述view代码，将逻辑处理的返回值传递给了html模板，模板通过下面的代码进行处理，将标签部分用传递过来的数据进行替换,生成静态html文件。
```html
<body>
  <h1>[{message}}が実行完了</h1>
</body>
```

## 补足:
有两种方式可以跳转到第三步，即转入对应的view进行处理。
1. 从button点击进入，这时url通过标签去生成，生成的url内容由传递过去的参数name决定。
2. url由手动输入，例如直接访问`http://localhost:8000/tools/disconnect/`，仍然可以访问到对应的view。将代码修改为如下`html文件`(删除了onclick的动作)
```html
<button type="button"
         onclick=""
       STYLE="color:red; background-color:white">
    実行(押す前に、設定ファイルを再確認してください！)</button>
```
将 `urls.py`修改为如下(删除name='vSetup'，因为不需要被button的onclick匹配了)
```python
 url(r'^(?P<Name>[a-zA-Z0-9]+)/$', views.vSetup),
```
修改为上述后，这里直接通过url匹配到vSetup这个view，并传递Name变量过去。注意这个Name变量与view中的接收参数名要一致。


## Todo
 - 如果有不希望访问的link，可以通过url直接这样访问进去，需要考虑根本性的方式禁止，而不是只在page上不显示而已。
