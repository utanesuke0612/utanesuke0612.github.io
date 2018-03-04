---
layout: post
title: Uda-DataAnalysis-51-机器学习[ing]-Dimple.js
date: 2018-02-18 05:00:00
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 3. 世界杯草图

[world cup data](https://www.statista.com/statistics/264441/number-of-spectators-at-football-world-cups-since-1930/)

```python
setwd("C:/Users/utane/OneDrive/udacity/48-D3")
getwd()
library(ggplot2)

pf <- read.csv("worldcup.csv",sep=',')

ggplot(data=pf, aes(x=year, y=number)) + geom_bar(stat="identity")
```

```python
"year","number"
2014,3429873
2010,3167984
2006,3367000
......
```

![image](https://user-images.githubusercontent.com/18595935/36946193-629dbb2a-1ffc-11e8-9eb3-56a6abdd2a57.png)

# 4. Dimple.js 代码文件

- 使用 Python 开始一个本地服务器。在终端中导航到包含所有代码文件的文件夹地址，然后输入`python -m SimpleHTTPServer`(python3使用python3 -m http.server)。

```
C:\Users\utane\OneDrive\udacity\51-dimple>python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

- 在浏览器地址栏中前往 `localhost:8000`，你会在网页中看到图形。

- 为什么要使用web服务器？

“在某些情况下，你可以在你的 web 浏览器中直接查看本地 HTML 文件，但是有些浏览器出于安全原因设有一定的限制，阻止通过 JavaScript 加载本地文件。也就是说，如果你的 D3 代码尝试拉入任何外部数据文件（如 CSV 或 JSON），它将会失败，而且不会明确说明理由。这并不是 D3 的故障，而是一个浏览器功能，用于防止加载来自第三方不受信任网站的脚本和其他外部文件。”

# 6. Dimple 柱状图代码概述

> 参考[basic_charts.html](http://www.utanesuke.shop/d3/dimple/basic_charts.html)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="http://d3js.org/d3.v3.min.js"></script>
  <script src="http://dimplejs.org/dist/dimple.v2.0.0.min.js"></script>
    <script type="text/javascript">
      function draw(data) {
      
      /*
        D3.js setup code
      */

          "use strict";
          var margin = 75,
              width = 1400 - margin,
              height = 600 - margin;

          var svg = d3.select("body")
            .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin)
            .append('g')
                .attr('class','chart');

      /*
        Dimple.js Chart construction code
      */

          var myChart = new dimple.chart(svg, data);
          var x = myChart.addTimeAxis("x", "year"); 
          myChart.addMeasureAxis("y", "attendance");
          myChart.addSeries(null, dimple.plot.bar);
          myChart.draw();
        };
      </script>
  </head>
<body>
  <script type="text/javascript">
  /*
    Use D3 (not dimple.js) to load the TSV file
    and pass the contents of it to the draw function
    */
  d3.tsv("world_cup.tsv", draw);
  </script>
</body>
</html>

```

![image](https://user-images.githubusercontent.com/18595935/36946371-3b7a8b2e-1fff-11e8-94d0-d983d9bda831.png)

# 7. Javascript 调试器

阅读更多关于[回调函数](http://javascriptissexy.com/understand-javascript-callback-functions-and-use-them/)的信息！
[Chrome 中的 Javascript 调试](https://developers.google.com/web/tools/chrome-devtools/?utm_source=dcc&utm_medium=redirect&utm_campaign=2016q3)
AJAX 代表“异步 JavaScript 和 XML”，指 web 页面在页面加载后进行 HTTP 请求的过程。你可以[在此](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started)阅读更多相关信息。



