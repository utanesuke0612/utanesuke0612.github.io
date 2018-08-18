---
layout: post
title: Uda-DataAnalysis-48-[扩展]机器学习-D3 Tutorials
date: 2018-02-18 02:03:00
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}

# 00. 参考:
> [D3 Tutorials](http://alignedleft.com/tutorials/d3) 和 [D3 References](https://github.com/tianxuzhang/d3-api-demo)

> [line chart](http://www.utanesuke.shop/d3/D3Tutorials/linechart.html)

# 01. Fundamentals

## 01-1 HTML

```html
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>Page Title</h1>
        <p>This is a really interesting paragraph</p>
    </body>
</html>
```

## 01-2 DOM

The Document Object Model refers to the hierarchical structure of HTML. Each bracketed tag is an element, and we refer to elements’ relative relationships to each other in human terms: parent, child, sibling, ancestor, and descendant. In the HTML above, body is the parent element to both of its children, h1 and p (which are siblings to each other). All elements on the page are descendants of html.

Web browsers parse the DOM in order to make sense of a page’s content.

## 01-3 CSS

- CSS rules can be included directly within the head of a document

```html
<head>
    <style type="text/css">
        p {
            font-family: sans-serif;
            color: lime;
        }
    </style>
</head>

```

- saved in an external file with a .css suffix, and then referenced in the document’s head:

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>

```

## 01-4 JavaScript

- Scripts can be included directly in HTML, between two script tags

```html
<body>
    <script type="text/javascript">
        alert("Hello, world!");
    </script>
</body>
```

- stored in a separate file, and then referenced somewhere the HTML (commonly in the head):

```html
<head>
    <title>Page Title</title>
    <script type="text/javascript" src="myscript.js"></script>
</head>
```

## 01-5 SVG

 SVG is a text-based image format. Meaning, you can specify what an SVG image should look like by writing simple markup code, sort of like HTML tags.

```html
 <svg width="50" height="50">
    <circle cx="25" cy="25" r="22"
     fill="blue" stroke="gray" stroke-width="2"/>
</svg>
```

# 02. Setup

Download the d3 js file from [here](https://github.com/d3/d3/releases)

- place the file like this:

```html
project-folder/
    d3/
        d3.v3.js
        d3.v3.min.js (optional)
    index.html

```

- index.html

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>D3 Test</title>
        <script type="text/javascript" src="d3/d3.v3.js"></script>
    </head>
    <body>
        <script type="text/javascript">
            // Your beautiful D3 code will go here
        </script>
    </body>
</html>     
```

# 03. Adding elements

Using the last simple template index.html file, open the developer console, and input:

```html
d3.select("body").append("p").text("New paragraph!");
```
Once we enter the above command, a new text will be created.

Let’s walk through what just happened. In sequence, we:

- Invoked D3's select method, which selects a single element from the DOM using CSS selector syntax. (We selected the body.)
- Created a new p element and appended that to the end of our selection, meaning just before the closing `</body>` tag in this case.
- Set the text content of that new, empty paragraph to “New paragraph!”

# 04. Chaining methods

D3 smartly employs a technique called chain syntax, which you may recognize from jQuery. By “chaining” methods together with periods, you can perform several actions in a single line of code. It can be fast and easy, but it’s important to understand how it works, to save yourself hours of debugging headaches later.

Let’s revisit our first line of D3 code (demo page here):

```
d3.select("body").append("p").text("New paragraph!");
```
or:

```
d3.select("body")
    .append("p")
    .text("New paragraph!");
```

- `.select("body")` 

Give select() a CSS selector as input, and it will return a reference to the first element in the DOM that matches. (Use selectAll() when you need more than one element.) In this case, we just want the body, so a reference to body is handed off to the next method in our chain.

- `.append("p")` 

append() creates whatever new DOM element you specify and appends it to the end (but just inside) of whatever selection it’s acting on. In our case, we want to create a new p within the body. We specified "p" as the input argument, but this method also sees the reference to body that was passed down the chain from the select() method. Finally, append(), in turn, hands down a reference to the new element it just created.

- `.text("New paragraph!")`  

text() takes a string and inserts it between the opening and closing tags of the current selection. Since the previous method passed down a reference to our new p, this code just inserts the new text between <p> and </p>. (In cases where there is existing content, it will be overwritten.)

- `;` The all-important semicolon indicates the end of this line of code.

# 05. Binding data

We use D3’s `selection.data()` method to bind data to DOM elements. But there are two things we need in place first, before we can bind data:
- The data
- A selection of DOM elements
Let’s tackle these one at a time.

## 05-1. Data

D3 is smart about handling different kinds of data, so it will accept practically any array of numbers, strings, or objects (themselves containing other arrays or key/value pairs). It can handle JSON (and GeoJSON) gracefully, and even has a built-in method to help you load in CSV files.

But to keep things simple, for now we will start with a boring array of numbers. Here is our sample data set:

```html
var dataset = [ 5, 10, 15, 20, 25 ];
```

## 05-2. Please Make Your Selection

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Test</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
  </head>
  <body>
    <script type="text/javascript">
    
      var dataset = [ 5, 10, 15, 20, 25 ];
      
      d3.select("body").selectAll("p")
        .data(dataset)
        .enter()
        .append("p")
        .text("New paragraph!");
      
    </script>
  </body>
</html>
```

- `d3.select("body")` — Finds the body in the DOM and hands a reference off to the next step in the chain.
- `.selectAll("p")` — Selects all paragraphs in the DOM. Since none exist yet, this returns an empty selection. Think of this empty selection as representing the paragraphs that will soon exist.
- `.data(dataset)` — Counts and parses our data values. There are five values in our data set, so everything past this point is executed five times, once for each value.
- `.enter()` — To create new, data-bound elements, you must use enter(). This method looks at the DOM, and then at the data being handed to it. If there are more data values than corresponding DOM elements, then enter() creates a new placeholder element on which you may work your magic. It then hands off a reference to this new placeholder to the next step in the chain.
- `.append("p")` — Takes the placeholder selection created by enter() and inserts a p element into the DOM. Hooray! Then it hands off a reference to the element it just created to the next step in the chain.
- `.text("New paragraph!")` — Takes the reference to the newly created p and inserts a text value.

上述网页加载后，在console中输入如下，可知`p`element已经被创建了：

```html
> console.log(d3.selectAll("p"))
< [Array(5)]
```

# 06. Using your data

> 示例: [usingdata1.html](http://www.utanesuke.shop/d3/D3Tutorials/usingdata1.html)和[usingdata2.html](http://www.utanesuke.shop/d3/D3Tutorials/usingdata2.html)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Test</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>

  </head>
  <body>
    <script type="text/javascript">
    
      var dataset = [ 5, 10, 15, 20, 25 ];
      
      d3.select("body").selectAll("p")
        .data(dataset)
        .enter()
        .append("p")
        .text(function(d) {
          return "I can count up to " + d;
        });
      
    </script>
  </body>
</html>
```

- 显示为如下:

```
I can count up to 5

I can count up to 10

I can count up to 15

I can count up to 20

I can count up to 25
```

通过style还可以修改颜色，如：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Test</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>

  </head>
  <body>
    <script type="text/javascript">
    
      var dataset = [ 5, 10, 15, 20, 25 ];
      
      d3.select("body").selectAll("p")
        .data(dataset)
        .enter()
        .append("p")
        .text(function(d) {
                    return "I can count up to " + d;
                })
        .style("color",function(d) {
          if (d>15){
            return "blue";
          }
          else {
            return "green";
          }
        });
      
    </script>
  </body>
</html>
```

# 07. Drawing divs

> 示例[drawingdivs.html](http://www.utanesuke.shop/d3/D3Tutorials/drawingdivs.html)
> 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Test</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>

    <style type="text/css">
        div.bar {
          display: inline-block;
          width: 20px;
          height: 75px;   /* We'll override this later */
          background-color: teal;
          margin-right: 2px;
          }

        div.bar1 {
          display: inline-block;
          width: 20px;
          height: 75px;   /* We'll override this later */
          background-color: blue;
          margin-right: 2px;
          }

    </style>

  </head>
  <body>
    <script type="text/javascript">
    
      var dataset = [5, 10, 15, 20, 25,30];
      
      d3.select("body").selectAll("p")
        .data(dataset)
        .enter()
        .append("div")
        .attr("class", "bar")
        .style("height", function(d) {
                          var barHeight = d * 5;  //Scale up by factor of 5
                          return barHeight + "px";
          });
    </script>

    <div class="bar1"></div>

  </body>
</html>
```


# 08. The power of data()
> 示例[powerdata.html](http://www.utanesuke.shop/d3/D3Tutorials/powerdata.html)
> 

通过随机函数生成数据

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Test</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>

   <style type="text/css">
    div.bar {
      display: inline-block;
      width: 20px;
      height: 75px;   /* We'll override this later */
      background-color: teal;
      margin-right: 2px;
      }
        </style>
  </head>
  <body>
    <script type="text/javascript">
    
     var dataset = [];                        //Initialize empty array
      for (var i = 0; i < 250; i++) {           //Loop 25 times
          var newNumber = Math.random() * 30;  //New random number (0-30)
          dataset.push(newNumber);             //Add new number to array
      }
      
      d3.select("body").selectAll("p")
        .data(dataset)
        .enter()
        .append("div")
        .attr("class", "bar")
        .style("height", function(d) {
              var barHeight = d * 5;  //Scale up by factor of 5
              return barHeight + "px";
        });
    </script>
  </body>
</html>
```

# 09. An SVG primer

> 示例[svg.html](http://www.utanesuke.shop/d3/D3Tutorials/svg.html)

![image](https://user-images.githubusercontent.com/18595935/37554311-e463dbcc-2a19-11e8-86e3-9447519295fc.png)

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .pumpkin {
        fill: yellow;
        stroke: orange;
        stroke-width: 5;
     }
  </style>
</head>

<body>
<svg class="chart" width="150" height="125">
  <circle cx="25" cy="100" r="22" class="pumpkin"/>

  <rect x="0" y="0" width="30" height="30" fill="purple"/>
  <rect x="20" y="5" width="30" height="30" fill="blue"/>
  <rect x="40" y="10" width="30" height="30" fill="green"/>
  <rect x="60" y="15" width="30" height="30" fill="yellow"/>
  <rect x="80" y="20" width="30" height="30" fill="red"/>
</svg>

  <svg class="chart" width="150" height="125">
  <circle cx="25" cy="25" r="20" fill="rgba(128, 0, 128, 1.0)"/>
  <circle cx="50" cy="25" r="20" fill="rgba(0, 0, 255, 0.75)"/>
  <circle cx="75" cy="25" r="20" fill="rgba(0, 255, 0, 0.5)"/>
  <circle cx="100" cy="25" r="20" fill="rgba(255, 255, 0, 0.25)"/>
  <circle cx="125" cy="25" r="20" fill="rgba(255, 0, 0, 0.1)"/>

</svg>

</body>
</html>
```

# 10. Drawing SVGs

> 示例[svg-orange.html](http://www.utanesuke.shop/d3/D3Tutorials/svg-orange.html)

![image](https://user-images.githubusercontent.com/18595935/37554410-5f0fb82c-2a1b-11e8-8e5e-1451fa2a3afc.png)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: SVG with pretty colors</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      /* No style rules here yet */   
    </style>
  </head>
  <body>
    <script type="text/javascript">
      
      //Width and height
      var w = 500;
      var h = 100;
      
      //Data
      var dataset = [ 5, 10, 15, 20, 25 ];
      
      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      var circles = svg.selectAll("circle")
          .data(dataset)
          .enter()
          .append("circle");

      circles.attr("cx", function(d, i) {
            return (i * 50) + 25;
          })
           .attr("cy", h/2)
           .attr("r", function(d) {
            return d;
           })
           .attr("fill", "yellow")
           .attr("stroke", "orange")
           .attr("stroke-width", function(d) {
            return d/2;
           });
    </script>
  </body>
</html>
```

> 示例[svg-circle.html](http://www.utanesuke.shop/d3/D3Tutorials/svg-circle.html)

![image](https://user-images.githubusercontent.com/18595935/37554440-f0a11f56-2a1b-11e8-87c4-1a5c2b564e6d.png)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: SVG with pretty colors</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      /* No style rules here yet */   
    </style>
  </head>
  <body>
    <script type="text/javascript">
      
      //Width and height
      var w = 500;
      var h = 100;
      
  //Data
      var dataset = [ 5, 10, 15, 20, 25 ];
      
      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      var circles = svg.selectAll("circle")
          .data(dataset)
          .enter()
          .append("circle");

      circles.attr("cx", function(d, i) {
            return (i * 50) + 25;
          })
           .attr("cy", h/2)
           .attr("r", function(d) {
            return d;
           });
    </script>
  </body>
</html>
```

# 11. Types of data

- Variables

JavaScript不需要定义数据类型，另外在运行时还能改变数据类型。

```python
var value = 100;
value = 99.9999;
value = false;
value = "This can't possibly work.";
value = "Argh, it does work! No errorzzzz!";
```

- Arrays

```python
var percentages = [ 0.55, 0.32, 0.91 ];
var names = [ "Ernie", "Bert", "Oscar" ];

percentages[1]  //Returns 0.32
names[1]        //Returns "Bert"
```

- for 循环

```python
> var numbers = [ 5, 10, 15, 20, 25 ];
> for (var i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);  //Print value to console
};

< 5
< 10
< ...
```

- object

```python
> var fruit = {
    kind: "grape",
    color: "red",
    quantity: 12,
    tasty: true
  };

> fruit.kind      //Returns "grape"
> fruit.color     //Returns "red"
> fruit.quantity  //Returns 12
> fruit.tasty     //Returns true
```

- Objects + Arrays

```python
> var fruits = [
    {
        kind: "grape",
        color: "red",
        quantity: 12,
        tasty: true
    },
    {
        kind: "kiwi",
        color: "brown",
        quantity: 98,
        tasty: true
    },
    {
        kind: "banana",
        color: "yellow",
        quantity: 0,
        tasty: true
    }
  ];

> fruits[0].kind 
< "grape"
```

- JSON

JSON is basically a specific syntax for organizing data as JavaScript objects. The syntax is optimized for use with JavaScript (obviously) and AJAX requests, which is why you’ll see a lot of web-based APIs that spit out data as JSON. It’s faster and easier to parse with JavaScript than XML, and of course D3 works well with it.

```python
var jsonFruit = {
    "kind": "grape",
    "color": "red",
    "quantity": 12,
    "tasty": true
};
```

The only difference here is that our indices are now surrounded by double quotation marks "", making them string values.

- GeoJSON

GeoJSON can store points in geographical space (typically as longitude/latitude coordinates), but also shapes (like lines and polygons) and other spatial features. If you have a lot of geodata, it’s worth it to parse it into GeoJSON format for best use with D3.

```python
var geodata = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [ 150.1282427, -24.471803 ]
            },
            "properties": {
                "type": "town"
            }
        }
    ]
};
```


# 12. Making a bar chart

## 12-1. The New Chart

> [barchart1.html](www.utanesuke.shop/d3/D3Tutorials/barchart1.html)

![image](https://user-images.githubusercontent.com/18595935/37554669-763fceca-2a1f-11e8-8dca-de98c3c992b9.png)


```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: Making a bar chart with SVG</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      /* No style rules here yet */   
    </style>
  </head>
  <body>
    <script type="text/javascript">

      //Width and height
      var w = 500;
      var h = 100;
      var barPadding = 1;
      
      var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
              11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];
      
      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      svg.selectAll("rect")
         .data(dataset)
         .enter()
         .append("rect")
         .attr("x", function(d, i) {
            return i * (w / dataset.length);
         })
         .attr("y", function(d) {
            return h - (d * 4);
         })
         .attr("width", w / dataset.length - barPadding)
         .attr("height", function(d) {
            return d * 4;
         });
    </script>
  </body>
</html>
```

- color

![image](https://user-images.githubusercontent.com/18595935/37554706-e493ed98-2a1f-11e8-9ece-2dcbaffafa05.png)

添加如下代码：

```html
.attr("fill", function(d) {
    return "rgb(0, 0, " + (d * 10) + ")";
});
```


## 12-2 Label

> [barchart2.html](http://www.utanesuke.shop/d3/D3Tutorials/barchart2.html)

![image](https://user-images.githubusercontent.com/18595935/37554759-72dd6336-2a20-11e8-936c-091e2951cc02.png)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: Making a bar chart with value labels!</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      /* No style rules here yet */   
    </style>
  </head>
  <body>
    <script type="text/javascript">

      //Width and height
      var w = 500;
      var h = 100;
      var barPadding = 1;
      
      var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
              11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];
      
      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      svg.selectAll("rect")
         .data(dataset)
         .enter()
         .append("rect")
         .attr("x", function(d, i) {
            return i * (w / dataset.length);
         })
         .attr("y", function(d) {
            return h - (d * 4);
         })
         .attr("width", w / dataset.length - barPadding)
         .attr("height", function(d) {
            return d * 4;
         })
         .attr("fill", function(d) {
          return "rgb(0, 0, " + (d * 10) + ")";
         });

      svg.selectAll("text")
         .data(dataset)
         .enter()
         .append("text")
         .text(function(d) {
            return d;
         })
         .attr("x", function(d, i) {
            return i * (w / dataset.length) + 5;
         })
         .attr("y", function(d) {
            return h - (d * 4) + 15;
         })
         .attr("font-family", "sans-serif")
         .attr("font-size", "11px")
         .attr("fill", "white");
    </script>
  </body>
</html>
```

# 13. Making a scatterplot

> [scatterplot.html](http://www.utanesuke.shop/d3/D3Tutorials/scatterplot.html)

![image](https://user-images.githubusercontent.com/18595935/37554852-ee932a28-2a21-11e8-8ffc-4655e5ec0338.png)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: Making a scatterplot with SVG</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      /* No style rules here yet */   
    </style>
  </head>
  <body>
    <script type="text/javascript">

      //Width and height
      var w = 800;
      var h = 100;
      
      var dataset = [
              [5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
              [410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
              ];
  
      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      svg.selectAll("circle")
         .data(dataset)
         .enter()
         .append("circle")
         .attr("cx", function(d) {
            return d[0]+10;
         })
         .attr("cy", function(d) {
            return d[1];
         })
         .attr("r", function(d) {
            return Math.sqrt(h - d[1]);
         });

      svg.selectAll("text")
         .data(dataset)
         .enter()
         .append("text")
         .text(function(d) {
            return d[0] + "," + d[1];
         })
         .attr("x", function(d) {
            return d[0]+10;
         })
         .attr("y", function(d) {
            return d[1];
         })
         .attr("font-family", "sans-serif")
         .attr("font-size", "11px")
         .attr("fill", "red");
    </script>
  </body>
</html>
```

# 14. Scales

The values in any data set are unlikely to correspond exactly to pixel measurements for use in your visualization. Scales provide a convenient way to map those data values to new values useful for visualization purposes.

D3 scales are functions whose parameters you define. Once they are created, you call the scale function, pass it a data value, and it nicely returns a scaled output value. You can define and use as many scales as you like.

## 14.1 Domains and Ranges

- domain
 
A scale’s `input` domain is the range of possible input data values. Given the apples data above, appropriate input domains would be either 100 and 500 (the minimum and maximum values of the data set) or zero and 500.

- range

A scale’s `output` range is the range of possible output values, commonly used as display values in pixel units. The output range is completely up to you, as the information designer. If you decide the shortest apple-bar will be 10 pixels tall, and the tallest will be 350 pixels tall, then you could set an output range of 10 and 350.

如下图：

![image](https://user-images.githubusercontent.com/18595935/37561491-1a483e9e-2a93-11e8-8a95-efd7bcc13e6f.png)

## 14.2 Creating a Scale

- scale函数默认是直接返回input值

```html
> var scale = d3.scale.linear();
< undefined
> scale(4)
< 4

# 重新定义其domain和range
> scale.domain([100, 500]);
< ƒ u(n){return o(n)}
> scale.range([10, 350]);
< ƒ u(n){return o(n)}

> scale(400)
< 265
```

```html
> var scale = d3.scale.linear()
                    .domain([100, 500])
                    .range([10, 350]);
> scale(200)
< 95
```

## 14.3 example

> 示例 [scale1.html](http://www.utanesuke.shop/d3/D3Tutorials/scale1.html)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: Linear scales</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      /* No style rules here yet */   
    </style>
  </head>
  <body>
    <script type="text/javascript">

      //Width and height
      var w = 500;
      var h = 300;
      var padding = 20;
      
      var dataset = [
              [5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
              [410, 12], [475, 44], [25, 67], [85, 21], [220, 88],
              [600, 150]
              ];

      //Create scale functions
      var xScale = d3.scale.linear()
                 .domain([0, d3.max(dataset, function(d) { return d[0]; })])
                 .range([padding, w - padding * 2]);

      var yScale = d3.scale.linear()
                 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                 .range([h - padding, padding]);

      var rScale = d3.scale.linear()
                 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                 .range([2, 5]);
  
      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      svg.selectAll("circle")
         .data(dataset)
         .enter()
         .append("circle")
         .attr("cx", function(d) {
            return xScale(d[0]);
         })
         .attr("cy", function(d) {
            return yScale(d[1]);
         })
         .attr("r", function(d) {
            return rScale(d[1]);
         });

      svg.selectAll("text")
         .data(dataset)
         .enter()
         .append("text")
         .text(function(d) {
            return d[0] + "," + d[1];
         })
         .attr("x", function(d) {
            return xScale(d[0]);
         })
         .attr("y", function(d) {
            return yScale(d[1]);
         })
         .attr("font-family", "sans-serif")
         .attr("font-size", "11px")
         .attr("fill", "red");
      
    </script>
  </body>
</html>
```


# 15. Axes

Unlike scales, when an axis function is called, it doesn’t return a value, but generates the visual elements of the axis, including lines, labels, and ticks.

## 15.1 Setting up an Axis

接着上一部分的代码,在console中输入：

```html
> svg.append("g")
    .call(d3.svg.axis()
                .scale(xScale)
                .orient("bottom"));
```

会发现添加了X轴：

![image](https://user-images.githubusercontent.com/18595935/37561631-bfd1691e-2a96-11e8-9103-e6adef43eb01.png)

## 15.2 example

> 示例[axes.html](http://www.utanesuke.shop/d3/D3Tutorials/axes.html)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>D3 Demo: Axes</title>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <style type="text/css">
      
      .axis path,
      .axis line {
        fill: none;
        stroke: black;
        shape-rendering: crispEdges;
      }
      
      .axis text {
        font-family: sans-serif;
        font-size: 11px;
      }

    </style>
  </head>
  <body>
    <script type="text/javascript">

      //Width and height
      var w = 500;
      var h = 300;
      var padding = 30;
      
      /*
      //Static dataset
      var dataset = [
              [5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
              [410, 12], [475, 44], [25, 67], [85, 21], [220, 88],
              [600, 150]
              ];
      */
      
      //Dynamic, random dataset
      var dataset = [];         //Initialize empty array
      var numDataPoints = 50;       //Number of dummy data points to create
      var xRange = Math.random() * 1000;  //Max range of new x values
      var yRange = Math.random() * 1000;  //Max range of new y values
      for (var i = 0; i < numDataPoints; i++) {         //Loop numDataPoints times
        var newNumber1 = Math.round(Math.random() * xRange);  //New random integer
        var newNumber2 = Math.round(Math.random() * yRange);  //New random integer
        dataset.push([newNumber1, newNumber2]);         //Add new number to array
      }

      //Create scale functions
      var xScale = d3.scale.linear()
                 .domain([0, d3.max(dataset, function(d) { return d[0]; })])
                 .range([padding, w - padding * 2]);

      var yScale = d3.scale.linear()
                 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                 .range([h - padding, padding]);

      var rScale = d3.scale.linear()
                 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
                 .range([2, 5]);

      //Define X axis
      var xAxis = d3.svg.axis()
                .scale(xScale)
                .orient("bottom")
                .ticks(5);

      //Define Y axis
      var yAxis = d3.svg.axis()
                .scale(yScale)
                .orient("left")
                .ticks(5);

      //Create SVG element
      var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

      //Create circles
      svg.selectAll("circle")
         .data(dataset)
         .enter()
         .append("circle")
         .attr("cx", function(d) {
            return xScale(d[0]);
         })
         .attr("cy", function(d) {
            return yScale(d[1]);
         })
         .attr("r", function(d) {
            return rScale(d[1]);
         });

      //Create labels
      svg.selectAll("text")
         .data(dataset)
         .enter()
         .append("text")
         .text(function(d) {
            return d[0] + "," + d[1];
         })
         .attr("x", function(d) {
            return xScale(d[0]);
         })
         .attr("y", function(d) {
            return yScale(d[1]);
         })
         .attr("font-family", "sans-serif")
         .attr("font-size", "11px")
         .attr("fill", "red");
      
      //Create X axis
      svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(0," + (h - padding) + ")")
        .call(xAxis);
      
      //Create Y axis
      svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(" + padding + ",0)")
        .call(yAxis);

    </script>
  </body>
</html>

```

效果如下:

![image](https://user-images.githubusercontent.com/18595935/37561674-c76f1aee-2a97-11e8-83ba-d4b6388ab3d3.png)

如果将这部分注释，则红色的备注不显示：

```html
      //Create labels
      svg.selectAll("text")
         .data(dataset)
         .enter()
         .append("text")
         .text(function(d) {
            return d[0] + "," + d[1];
         })
         .attr("x", function(d) {
            return xScale(d[0]);
         })
         .attr("y", function(d) {
            return yScale(d[1]);
         })
         .attr("font-family", "sans-serif")
         .attr("font-size", "11px")
         .attr("fill", "red");
```