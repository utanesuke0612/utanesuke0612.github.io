---
layout: post
title: Uda-DataAnalysis-48-机器学习-D3基础构件
date: 2018-02-18 02:00:00
categories: 数据分析
tags: R DataAnalysis 
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

```html
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

```html
> function add_me(a,b){
 return a + b;
}
< undefined
> add_me(2,3)
< 5
```

# 8. 文档选择器和查询

示例：

```html
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

# 11. D3链语法和更改导航栏

通过上面的函数，如`document.getElementsByTagName`和`document.querySelector`返回的是`dom`对象，该dom对象不能使用d3的方法。要使用d3的方法，就要用到d3 selections。

```html
> var elem = d3.select(".navbar")
< undefined

# elem就是一个返回的d3对象
> elem
< [Array(1)]

# 返回颜色
> elem.style("background-color")
"rgb(28, 38, 47)"

# 修改颜色
< elem.style("background-color","#765432")
[Array(1)]
```

最终颜色发生了变化：

![image](https://user-images.githubusercontent.com/18595935/36544599-32bf6090-182a-11e8-9b92-d8eb79902d95.png)

另外，通过`selectAll`能选出所有符号条件的元素：

```html
> d3.selectAll("img")
< [Array(4)]
```

# 14. 更改标题

```html
# 通过类名class名
d3.select(".main-title").html("Gapminder World: China")

# 下面也可以实现相同的目的，通过标签名
d3.select("h1").html("Gapminder World: China")
```

# 15. 嵌套选择器

加入要选择img部分：

```html
<a class="navbar-brand logo" id="header-logo" href="https://classroom.udacity.com">
    <img src="./assets/udacity.svg" alt="logo">
</a>
```

使用如下的代码：

```html
> var parent_el = d3.select("#header-logo")
< undefined

> parent_el.select("img")
< [Array(1)]

> parent_el.select("img").attr("src")
< "./assets/udacity.svg"

> parent_el.select("img").attr("alt","udacity")
< [Array(1)]

# 下面的语句等同上面的：
> d3.select("#header-logo img").attr("alt","udacity")
< [Array(1)]
```

# 16. 练习：嵌套选择器

- 直接用一行语句实现logo替换：

```html
> d3.select("#header-logo").select("img").attr("src","./assets/udacity_white.png")
< [Array(1)]

# 更加简明的方式
> d3.select("#header-logo img").attr("src","./assets/udacity_white.png")

# 或是
> d3.select(".navbar-brand img").attr("src","./assets/udacity_white.png")
> d3.select(".logo img").attr("src","./assets/udacity_white.png")
```

# 17. 运用 D3 删除元素

```html
# 可以有多种方式，下列方式都可行：

> d3.selectAll(".main").html(null)
> d3.selectAll(".main").html("")
> d3.selectAll(".main").remove()
```



# 20. 刻度的原理

![image](https://user-images.githubusercontent.com/18595935/36727489-c9525e16-1c00-11e8-8c3a-e69c0282fa1c.png)

SVG的坐标系与通常的坐标系不同，我们在使用的时候，需要构建：

- domain([15,90]): 带有实际意义的范围，人均寿命
- range([250,0]): 映射到屏幕的范围
- d3.scale.linear()

# 21. 添加SVG元素

```html
> d3.select(".main").html("")
< [Array(1)]

# 添加svg对象
> var svg = d3.select(".main").append("svg")
< undefined

# 修改svg的属性
> svg.attr("width",600).attr("height",300)
< [Array(1)]
```

# 22. D3 刻度语法

```html
> var y=d3.scale.linear().domain([15,90]).range([250,0])
> y(15)
< 250
> y(90)
< 0

> var x=d3.scale.log().domain([250,100000]).range([0,600])
> x(250)
< 0
> x(100000)
< 600

# 如下定义的x和y是函数
> x
< ƒ u(t){return n(e(t))}

> y
< ƒ u(n){return a(n)}

```

# 25. 创建半径刻度

Create a scale for the circles on the Gapminder plot and save it to a variable called "r".

The population of the countries ranges from 52070 in Marshall Islands to 1.38 billion in China. Map the values to a range of 10 pixels to 50 pixels.

```html
> var r=d3.scale.sqrt().domain([52070,1380000000]).range([10,50]);
```

# 26.添加和格式化中国的红圈

如下是一个完整的代码：

```html
# 移除main部分
> d3.select(".main").html("")
< [Array(1)]

# 添加svg
> var svg = d3.select(".main").append("svg")
< undefined

# 重新设置大小
> svg.attr("width",600).attr("height",300)
< [Array(1)]

# 设置y轴函数
> var y=d3.scale.linear().domain([15,90]).range([250,0])
< undefined

# 设置x轴函数
> var x=d3.scale.log().domain([250,100000]).range([0,600])
< undefined

# 设置r半径函数
> var r=d3.scale.sqrt().domain([52070,1380000000]).range([10,50]);
< undefined

# 添加圆圈
> svg.append("circle").attr("fill","red").attr("r",r(1380000000)).attr("cx",x(13330)).attr("cy",y(77))
< [Array(1)]

# 上面添加的圆圈有一部分显示不完全，需要重新设置r半径
> var r=d3.scale.sqrt().domain([52070,1380000000]).range([10,40]);
< undefined

> svg.append("circle").attr("fill","red").attr("r",r(1380000000)).attr("cx",x(13330)).attr("cy",y(77))
< [Array(1)]

```

# 28. 服务器请求和 D3

参考下图：

- client-server mode(1)

![image](https://user-images.githubusercontent.com/18595935/36941704-d57e899c-1fa4-11e8-8b07-6b55d7dadafc.png)

- client-server mode(2)

![image](https://user-images.githubusercontent.com/18595935/36941711-1c6e8140-1fa5-11e8-9be1-fe84a011098d.png)

# 29. 一起来制作柱状图

- `index.html`

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="http://d3js.org/d3.v3.min.js"></script>
<style>
.chart rect {
  fill: steelblue;
}

.chart text {
  fill: white;
  font: 10px sans-serif;
  text-anchor: end;
}
</style>
<script>
function draw(data) {
  var width = 420,
  barHeight = 20;

  var x = d3.scale.linear()
    .range([0, width]);

  var chart = d3.select(".chart")
      .attr("width", width);

  x.domain([0, d3.max(data, function(d) { return d.value; })]);

  chart.attr("height", barHeight * data.length);

  var bar = chart.selectAll("g")
      .data(data)
    .enter().append("g")
      .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

  bar.append("rect")
      .attr("width", function(d) { return x(d.value); })
      .attr("height", barHeight - 1);

  bar.append("text")
      .attr("x", function(d) { return x(d.value) - 3; })
      .attr("y", barHeight / 2)
      .attr("dy", ".35em")
      .text(function(d) { return d.value; });
}
</script>
</head>
<body>
  <svg class="chart"></svg>
  <script type="text/javascript">

  function type(d) {
    d.value = +d.value; // coerce to number
    return d;
  }

  d3.tsv("data.tsv", type, draw);

  </script>
</body>
</html>

```


- `data.tsv`

```
name	value
Locke	4
Reyes	8
Ford	15
Jarrah	16
Shephard	23
Kwon	42

```

- 最终图形：

![image](https://user-images.githubusercontent.com/18595935/36849372-3eca929c-1da7-11e8-8356-499b888336c1.png)

# 30. 代码结构和 JavaScript

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="http://d3js.org/d3.v3.min.js"></script>
<style>
.chart rect {
  fill: steelblue;
}

.chart text {
  fill: white;
  font: 10px sans-serif;
  text-anchor: end;
}
</style>
<script>
function draw(data) {
  var width = 420,
  barHeight = 20;

  var x = d3.scale.linear()
    .range([0, width]);

  var chart = d3.select(".chart")
      .attr("width", width);

  x.domain([0, d3.max(data, function(d) { return d.value; })]);

  chart.attr("height", barHeight * data.length);

  var bar = chart.selectAll("g")
      .data(data)
    .enter().append("g")
      .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

  bar.append("rect")
      .attr("width", function(d) { return x(d.value); })
      .attr("height", barHeight - 1);

  bar.append("text")
      .attr("x", function(d) { return x(d.value) - 3; })
      .attr("y", barHeight / 2)
      .attr("dy", ".35em")
      .text(function(d) { return d.value; });
}
</script>
</head>
<body>
  <svg class="chart"></svg>
  <script type="text/javascript">

  function type(d) {
    d.value = +d.value; // coerce to number
    return d;
  }

  d3.tsv("data.tsv", type, draw);

  </script>
</body>
</html>
```

- 布局和刻度
- 绑定数据
- 添加柱和文本

![image](https://user-images.githubusercontent.com/18595935/36941387-4fdc431c-1f9d-11e8-9532-e463a21a54df.png)





