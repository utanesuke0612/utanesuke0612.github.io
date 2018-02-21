---
layout: post
title: Uda-DataAnalysis-48-机器学习[ing]-D3基础构件
date: 2018-02-18 02:00:00
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 2. 成为技术传播者

附加资料：

- Scott Murray 在他的网站 [alignedleft.com](http://alignedleft.com/tutorials/d3/fundamentals) 上对这些基本原理进行了非常精彩的概述。（时间估计：10 分钟）

- 要了解 HTML、CSS 和 Javascript 的基础知识，我们鼓励你在 [https://dash.generalassemb.ly/](https://dash.generalassemb.ly/) 上完成第 1 个和第 2 个项目。（时间估计：10 至 20 个小时）

- Scott Murray 还针对[使用 D3.js 创建可视化](http://alignedleft.com/tutorials/d3)提供了非常有用的教程，可让你预览后面课程中的内容。（时间估计：10 至 15 个小时）

- 如果你有更多时间，或想在继续本课程前更多地熟悉 HTML 和 CSS，你可以考虑学习我们的 [HTML 和 CSS 入门课程](https://cn.udacity.com/course/intro-to-html-and-css--ud304)。（时间估计：18+ 个小时）

# 4. 加载D3

在chrome中打开任意一个网页，`Ctrl+shift+J`可以打开JavaScript的命令行工具，输入如下代码可载入D3：

```python
var script = document.createElement("script")
script.type = "text/javascript"
script.src = "https://d3js.org/d3.v4.min.js"
document.head.appendChild(script)
```

载入后，输入`d3.`就会出现对应的函数提示了。

一个已经载入了d3的网页，如`https://d3js.org/`的Elements中，其head中包含了`<script src="d3.v4.min.js" charset="utf-8"></script>`。

# 7. 在 JavaScript 控制台操作

通过`Ctrl+Shift+J`打开JavaScript控制台后，可以定义函数并执行操作。

- 使用`Shift+enter`用于在一个命令内换行，在定义函数时使用
- 使用`clear()`可以清理屏幕
- `↑ ↓`可以选择历史命令

```python
> function add_me(a,b){
 return a + b;
}
< undefined
> add_me(2,3)
< 5
```

# 8. 文档选择器和查询

示例：

```python
# 返回id为footer的元素
> document.getElementById("footer")
< null

# 返回标签为footer的元素
> document.getElementsByTagName("footer")
< HTMLCollection [footer]

# 返回类名称为main的元素
> document.querySelector(".main")
< null

```