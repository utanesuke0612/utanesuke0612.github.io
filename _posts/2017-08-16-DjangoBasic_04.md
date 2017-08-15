---
layout: post
title: DjangoBasi-04-[重要]Django表单
date: 2017-08-16 22:45:59
categories: Python
tags: Web Django
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

---
# <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>**注意：**
1. Django的 标签导致Jekyll无法编译，都修改为了[%，使用时需要替换！
2. **`本节非常重要！`**

>截至到第三节，我们已经将model中的动态数据显示到网页上，并通过点击title实现了查看post详情。在实现方式上，应用了模板和CSS等。通过本节，继续扩展我们的功能，添加post的表单form，实现post的新增和编辑。

# 1. 创建表单
通过Django自带的Admin也能实现对model的操作，但是很难去自定义，因为结构已经固定。通过forms，我们可以完全自定义我们的页面。

1. 在blog目录下创建forms.py表单定义文件。

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
```



# 2. 创建指向该表单的链接

# 3. URL中添加对应记录

# 4. 添加post_new视图

# 5. 添加post_edit模板文件

# 6. 保存表单

# 7. 验证表单

# 8. 编辑表单

# 9.  表单安全性
