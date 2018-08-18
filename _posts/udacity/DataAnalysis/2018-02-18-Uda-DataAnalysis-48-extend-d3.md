---
layout: post
title: Uda-DataAnalysis-48-[扩展]机器学习-Make a Bar Chart
date: 2018-02-18 02:05:00
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}

This post is the summary of the blog-[Let’s Make a Bar Chart](https://bost.ocks.org/mike/bar/).

Before we dive into the d3,we will see two templates for html(css/javascript) and d3.

# 1. The html template 

## 1.1 Inline css/javascript in html

> [bones.html](http://www.utanesuke.shop/d3/barchart/bones.html)

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Html和CSS的关系</title>
        <style type="text/css">
        h1{
            font-size:12px;
            color:#930;
            text-align:left;
        }
        h2{
            font-size:18px;
            color:#930;
            text-align:left;
        }
        </style>

        <script type="text/javascript">
            var mystr="我是";
            var mychar="JavaScript";
            document.write(mystr + "<br>")
            document.write(mystr + mychar + "的忠实粉丝")
        </script>

    </head>

    <body>
        <h1>Hello World!</h1>
        <h2>Hello World!</h2>
    </body>
</html>
```

## 1.2 External css/javascript file

> [bones-external.html](http://www.utanesuke.shop/d3/barchart/bones-external.html)

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Html和CSS的关系</title>
        <link rel="stylesheet" type="text/css" href="mystyle.css">
        <script src="myscripts.js"></script>
    </head>

    <body>
        <h1>Hello World!</h1>
        <h2>Hello World!</h2>
    </body>
</html>
```

- External css/javascript file 

> [mystyle.css](http://www.utanesuke.shop/d3/barchart/mystyle.css)

```html
h1{
 font-size:12px;
 color:#930;
 text-align:left;
}

h2{
 font-size:18px;
 color:#930;
 text-align:left;
}
```


- External css/javascript file

> [myscripts.js](http://www.utanesuke.shop/d3/barchart/myscripts.js)

```html
var mystr="我是";
var mychar="JavaScript";
document.write(mystr + "<br>")
document.write(mystr + mychar + "的忠实粉丝")
```

# 2. The D3 template 

>  [barchart-bones.html](http://www.utanesuke.shop/d3/barchart/barchart-bones.html)

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>barchart</title>
        <div class="chart"></div>
        <script src="https://d3js.org/d3.v3.min.js"  charset="utf-8"></script>
        <style type="text/css">
        .chart div {
          font: 10px sans-serif;
          background-color: steelblue;
          text-align: right;
          padding: 3px;
          margin: 1px;
          color: white;
        }
        </style>

        <script type="text/javascript">
        var data = [4, 8, 15, 16, 23, 42];

        var x = d3.scale.linear()
            .domain([0, d3.max(data)])
            .range([0, 420]);

        d3.select(".chart")
          .selectAll("div")
            .data(data)
          .enter().append("div")
            .style("width", function(d) { return x(d) + "px"; })
            .text(function(d) { return d; });
        </script>
    </head>

    <body>
        <h1>Hello World!</h1>
    </body>
</html>
```

# 3. Selecting an Element

## 3.1 With vanilla JavaScript

In vanilla JavaScript, we typically deal with elements one at a time. 

> input the below commands in console(chrome:`ctrl+shift+J`)

```html
# create a div element
var div = document.createElement("div");

# set its contents
div.innerHTML = "Hello, world!";

# append it to the body
document.body.appendChild(div);
```

> vanilla: If you describe a person or thing as vanilla, you mean that they are ordinary, with no special or extra features.

## 3.2 With D3

With D3, It's different from the vanilla JavaScript,we handle groups of related elements called selections.
> We can manipulate a single element or many of them without substantially restructuring your code. 

**for example:**

- `d3.select("body")`,Only the first body element will be return.

```html
var body = d3.select("body");
var div = body.append("div");
div.html("Hello, world!");
```
- `d3.selectAll("section")`,All of the section elements will be return.

```html
var section = d3.selectAll("section");
var div = section.append("div");
div.html("Hello, world!");
```

# 4. Chaining Methods

## 4.1 Without method chaining

```html
var body = d3.select("body");
body.style("color", "black");
body.style("background-color", "white");
```

## 4.2 With method chaining

```html
d3.select("body")
    .style("color", "black")
    .style("background-color", "white");
```
While most operations return `the same selection`(like the above example), some methods return a new one! 

For example, selection.append returns a new selection containing the new elements. 

```html
d3.selectAll("section")
    .attr("class", "special")
  .append("div")
    .html("Hello, world!");
```

Since method chaining can only be used to descend into the document hierarchy, use `var` to keep references to selections and go back up.

```html
var section = d3.selectAll("section");

section.append("div")
    .html("First!");

section.append("div")
    .html("Second.");
```

# 5. Coding a Chart, Manually

Create a bar chart without JavaScript:

> [ChartManually.html](http://www.utanesuke.shop/d3/barchart/ChartManually.html)

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>CodingAChartManually</title>
        <style>
        .chart div {
          font: 10px sans-serif;
          background-color: steelblue;
          text-align: right;
          padding: 3px;
          margin: 1px;
          color: white;
        }
        </style>
    </head>

    <body>
        <div class="chart">
          <div style="width: 40px;">4</div>
          <div style="width: 80px;">8</div>
          <div style="width: 150px;">15</div>
          <div style="width: 160px;">16</div>
          <div style="width: 230px;">23</div>
          <div style="width: 420px;">42</div>
        </div>
    </body>
</html>
```

This chart has one div for a container, and one child div for each bar. The child divs have a blue background color and a white foreground color, giving the appearance of bars with right-aligned value labels.

# 6. Coding a Chart, Automatically

You can refer to the `2. The D3 template` for the complete code.

>  [barchart-bones.html](http://www.utanesuke.shop/d3/barchart/barchart-bones.html)

```html
 <script type="text/javascript">
 var data = [4, 8, 15, 16, 23, 42];

 var x = d3.scale.linear()
  .domain([0, d3.max(data)])
  .range([0, 420]);

 d3.select(".chart")
  .selectAll("div")
   .data(data)
  .enter().append("div")
   .style("width", function(d) { return x(d) + "px"; })
   .text(function(d) { return d; });
 </script>
```

> Let’s break it down, rewriting the above concise code in long form, to see how it works.

```

# First, we select the chart container using a class selector.
> var chart = d3.select(".chart");
< undefined

# Next we initiate the data join by defining the selection to which we will join data.
> var bar = chart.selectAll("div");
< undefined

# the selection is empty
> bar
< [Array(0)]

# Next we join the data (defined previously) to the selection using selection.data.
> var barUpdate = bar.data(data);
< undefined

# We instantiate these missing elements by appending to the enter selection.
> var barEnter = barUpdate.enter().append("div");
< undefined

> barEnter
< [Array(6)]
  0
  :
  (6) [div, div, div, div, div, div, parentNode: div.chart]

# after excuting the blow, the length of the bar will be changed
> barEnter.style("width", function(d) { return d * 10 + "px"; });
< [Array(6)]

# add a text for each of the bar
> barEnter.text(function(d) { return d; });
< [Array(6)]
```

- 最后图形如下:

![image](https://user-images.githubusercontent.com/18595935/36940779-f520f86e-1f8d-11e8-8713-f14144371f72.png)

# 7. Scaling to Fit

At the last example, we used a very simple way to map the data valueto the pixel width.

We can make these dependencies explicit and eliminate the magic number by using a linear scale. D3’s scales specify a mapping from data space (domain) to display space (range):

```html
# the domain() is the data range
# the range() is the pixel range
var x = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([0, 420]);
```

Although x here looks like an object, it is also a function that returns the scaled display value in the range for a given data value in the domain. 

To use the new scale, simply replace the hard-coded multiplication by calling the scale function:

```html
d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) { return x(d) + "px"; })
    .text(function(d) { return d; });
```

# 8. SVG template

> [svg-bones.html](http://www.utanesuke.shop/d3/barchart/svg-bones.html)

```html
<!DOCTYPE html>
<html>
<body>

<svg width="400" height="180">
  <rect x="50" y="20" width="150" height="150" style="fill:blue;stroke:pink;stroke-width:5;fill-opacity:0.1;stroke-opacity:0.9" />
  Sorry, your browser does not support inline SVG.  
</svg>
 
</body>
</html>
```

## 8.1 SVG template(external)

- `svg-bones - external.html`

```html
<!DOCTYPE html>
<html>
	<body>
	<object data="template.svg" type="image/svg+xml"></object>
	</body>
</html>
```

- `template.svg`

```html
<svg width="400" height="180">
  <rect x="50" y="20" width="150" height="150" style="fill:blue;stroke:pink;stroke-width:5;fill-opacity:0.1;stroke-opacity:0.9" />
  Sorry, your browser does not support inline SVG.  
</svg>
```

# 9. Coding a Chart, Manually

> [svg-manual.html](http://www.utanesuke.shop/d3/barchart/svg-manual.html)

```html
<!DOCTYPE html>
<html>
<body>

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

<svg class="chart" width="420" height="120">
  <g transform="translate(0,0)">
    <rect width="40" height="19"></rect>
    <text x="37" y="9.5" dy=".35em">4</text>
  </g>
  <g transform="translate(0,20)">
    <rect width="80" height="19"></rect>
    <text x="77" y="9.5" dy=".35em">8</text>
  </g>
  <g transform="translate(0,40)">
    <rect width="150" height="19"></rect>
    <text x="147" y="9.5" dy=".35em">15</text>
  </g>
  <g transform="translate(0,60)">
    <rect width="160" height="19"></rect>
    <text x="157" y="9.5" dy=".35em">16</text>
  </g>
  <g transform="translate(0,80)">
    <rect width="230" height="19"></rect>
    <text x="227" y="9.5" dy=".35em">23</text>
  </g>
  <g transform="translate(0,100)">
    <rect width="420" height="19"></rect>
    <text x="417" y="9.5" dy=".35em">42</text>
  </g>
</svg>

</body>
</html>
```

# 10. Coding a Chart, Automatically

> [svg-manual.html](http://www.utanesuke.shop/d3/barchart/svg-manual.html)

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>barchart</title>
        <div class="chart"></div>
        <script src="https://d3js.org/d3.v3.min.js"  charset="utf-8"></script>
        <style type="text/css">
            .chart rect {
              fill: steelblue;
            }

            .chart text {
              fill: white;
              font: 10px sans-serif;
              text-anchor: end;
            }
        </style>

        <script type="text/javascript">
        var data = [4, 8, 15, 16, 23, 42];

        var width = 420,
            barHeight = 20;

        var x = d3.scale.linear()
            .domain([0, d3.max(data)])
            .range([0, width]);

        var chart = d3.select(".chart")
            .attr("width", width)
            .attr("height", barHeight * data.length);

        var bar = chart.selectAll("g")
            .data(data)
          .enter().append("g")
            .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

        bar.append("rect")
            .attr("width", x)
            .attr("height", barHeight - 1);

        bar.append("text")
            .attr("x", function(d) { return x(d) - 3; })
            .attr("y", barHeight / 2)
            .attr("dy", ".35em")
            .text(function(d) { return d; });
        </script>

    </head>

    <body>
        <h1>Hello World!</h1>
    </body>
</html>
```

1. We set the svg element's size in js so that we can compute the height based on the size of the dataset.

```html
var chart = d3.select(".chart")
  .attr("width", width)
  .attr("height", barHeight * data.length);
```

2. Each bar consists of a g element which in turn contains a rect and a text.

```html
var bar = chart.selectAll("g")
  .data(data)
  .enter().append("g")
  .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
```



# 11. Loading Data

An external data file separates the chart implementation from its data, making it easier to reuse the implementation on multiple datasets or even live data that changes over time.

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

- `d3.tsv("data.tsv", type, draw);`

To use this data in a web browser, we need to download the file from a web server and then parse it, which converts the text of the file into usable JavaScript objects.

- Loading data introduces a new complexity: downloads are asynchronous. 

When you call d3.tsv, it returns immediately while the file downloads in the background. At some point in the future when the download finishes, your callback function is invoked with the new data, or an error if the download failed. In effect your code is evaluated out of order:

```html
// 1. Code here runs first, before the download starts.

d3.tsv("data.tsv", function(error, data) {
  // 3. Code here runs last, after the download finishes.
});

// 2. Code here runs second, while the file is downloading.
```

- Here’s one more gotcha with external data: types!

 d3.tsv isn’t smart enough to detect and convert types automatically. Instead, we specify a type function that is passed as the second argument to d3.tsv. This type conversion function can modify the data object representing each row, modifying or converting it to a more suitable representation:

```html
function type(d) {
  d.value = +d.value; // coerce to number
  return d;
}
```

Type conversion isn’t strictly required, but it’s an awfully good idea. By default, all columns in TSV and CSV files are strings. If you forget to convert strings to numbers, then JavaScript may not do what you expect, say returning "12" for "1" + "2" rather than 3. 


# 12. Part 3

> [Part 3](https://bost.ocks.org/mike/bar/3/)
