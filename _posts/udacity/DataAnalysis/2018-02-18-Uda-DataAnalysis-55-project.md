---
layout: post
title: Uda-DataAnalysis-55-机器学习-进阶项目4-创建有效的数据可视化
date: 2018-02-18 09:00:00
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 1. 概要

选取2015年-2017年波士顿马拉松选手的配速表，将不同级别选手在马拉松不同阶段上的配速，以可视化的方式呈现。

# 2. 设计

原始CSV数据是，2015-2017三年间每个选手的完赛时间以及每5公里所耗时间，通过对这些CSV数据进行如下的处理：

- 根据完赛时间，将选手分为sub2.5,sub3,sub3.5,sub4,sub4.5,sub5,over5等7个等级。(sub2.5指少于2.5小时,over5指5个小时以上)

- 根据上述7个等级，区分性别，计算不同性别以及不同等级下，所有选手每5公里的平均配速

- 将处理得到的数据保存到一个新的配速表CSV

利用D3读取并处理新的配速表CSV，生成如下的可视化图形:

- 将全程马拉松按照5公里分段，分为5k,10k,..40k,42k，并显示在X轴

- 每公里的配速显示在Y轴

- 图上的折线段，表示不同年份(2015,2016,2017)，不同性别(非区分,男性,女性)下，某个等级下所有选手配速变化

- 图例显示在折线图形的下方，默认显示的选手配速是不区分性别的，即男性配速及女性配速默认不显示

- 通过点击图例，可以控制折线段显示或非显示

- 图例标签的颜色，与其对应的折线段颜色一致

**通过最终生成的图形可以得到如下的信息**：

- sub2.5,sub3即全程马拉松在2.5小时内，以及2.5-3小时之间的高水平选手，全程的配速变化较小，而超过5小时的over5以及4.5-5小时的sub5选手，其配速的变化幅度较大。

- 所有选手，在30km-35km段配速都会变慢，俗称马拉松的撞墙期。35km后，速度会逐步变快。

- 同一个水平内(比如sub3)的选手，刚起步时男选手比女选手的配速要快，但越到马拉松后程，女选手的速度逐步提高，在最终段40-42km处，女选手的速度会超过男选手。

- 不同水平的选手，在最后40-42km处都会保持当前速度或是稍有加速，但是sub3.5及更低水平的选手，在2015年时其配速反而下降，尤其是over5水平较低选手，配速下降尤其明显。调查了2015-2017年的天气状况后发现，2015年下雨，2016年和2017年晴天，说明水平越低的选手越容易受到外界影响。

# 3. 反馈与修改

## 3.1 获取到的反馈

- 图形没有标题，最好添加标题说明该图形表达的主题

- Y轴上的数字意义不明

- 图形上的线条过多，显得有些杂乱无章

- 图例过多，显得繁杂

## 3.2 修改

- 添加了标题 `Boston 5K 平均成绩对比(2015-2017)`

- 添加了Y轴的说明`min/km`

- 将单独的男性配速和女性配速，默认为非显示

- 图例过多的问题没有修改，考虑过其他的方式设计图例，但如何保持图例与图形的配色，没有想到好的解决方案，故没有修改

# 4. 资源

- [Multi-Series Line Chart](https://bl.ocks.org/mbostock/3884955)
- [D3.js 基本4 – Scaleでデータを画面に収める](http://deep-blend.com/jp/2014/05/d3-js-basic4-scale/)
- [d3 categorical colors & Google colors](http://bl.ocks.org/aaizemberg/78bd3dade9593896a59d)
- [Simple d3.js tooltips](http://bl.ocks.org/d3noob/a22c42db65eb00d4e369)


# 5. 相关代码
> 参考 [http://www.utanesuke.shop/d3/pj06/](http://www.utanesuke.shop/d3/pj06/)

显示效果如下:

![image](https://user-images.githubusercontent.com/18595935/37702872-4239eb68-2d37-11e8-93df-f696819bcdfc.png)


## 5.1 index.html

```html
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title></title>
        <link rel="stylesheet" type="text/css" href="mystyle.css">
	<script src="https://d3js.org/d3.v3.min.js"  charset="utf-8"></script>
    </head>

    <body>
        <h2 class="headertekst">Boston马拉松-选手配速迁移图(2015-2017)</h2>
        
        <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspx轴表示全程马拉松的不同阶段，以5KM为一个刻度，比如5KM处表示该选手的0-5km段；y轴是选手配速，比如4表示4min/km，一公里耗时4分钟。</p>
        
        <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp关于图例:&nbsp2015_Both_sub2.5表示2015年的波士顿马拉松，完善成绩在2.5小时内的选手。Female及Male是女性或男性选手，默认为不显示。</p>

        <script src="myscripts.js"></script>
    </body>
</html>

```

## 5.2 mystyle.css

```html
body { font: 12px Arial;}

path { 
    stroke: steelblue;
    stroke-width: 2;
    fill: none;
}

.axis path,
.axis line {
    fill: none;
    stroke: grey;
    stroke-width: 1;
    shape-rendering: crispEdges;
}

.legend {
    font-size: 16px;
    font-weight: bold;
    text-anchor: middle;
}

h2.headertekst {
  text-align: center;
}

p {text-align: center;}

</style>

```

## 5.3 myscripts.js

```html
// define the x label
var x_labellist = ["5km","10km","15km","20km","25km","30km","35km","40km","42km"]

// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 20, left: 50},
    width = 1600 - margin.left - margin.right,
    height = 480 - margin.top - margin.bottom;

// Set the ranges
var x = d3.scale.ordinal().rangePoints([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var paceline = d3.svg.line()   
    .x(function(d) { return x(d.PaceType); })
    .y(function(d) { return y(d.Pace); });
    
// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("x", 0)
    .attr("y", 0)
    .text("min/km");

var svg1 = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height*0.5 + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");
// Get the data
d3.csv("data/pace_result.csv", function(error, data) {
    data.forEach(function(d) {
        d.PaceType = d.PaceType;
        d.Pace = +d.Pace;
    });

    // Scale the range of the data
    x.domain(x_labellist);
    y.domain([d3.min(data, function(d) { return d.Pace; }), d3.max(data, function(d) { return d.Pace; })]);

    // Nest the entries by Type 
    var dataNest = d3.nest()
        .key(function(d) {return d.Type;})
        .entries(data);

    var color = d3.scale.category10();   // set the colour scale

    legendSpace = 7*width/dataNest.length; // spacing for the legend

    // Loop through each type / key
    dataNest.forEach(function(d,i) { 

        year = d.values[0]["Year"];
        gender = d.values[0]["Gender"];
        rank = d.values[0]["Rank"];
        
        console.log(i);
        console.log(year);
        console.log(gender);
        console.log(rank);

        svg.append("path")
            .attr("class", "line")
            .style("stroke", function() { // Add the colours dynamically
                return d.color = color(d.key); })
            .attr("id", 'tag'+d.key.replace(/[.]/g, '_')) // assign ID
            .attr("d", paceline(d.values))
            .style("opacity", function(){
                if (gender == "Both"){
                    d.active = true;
                    return 1;
                }else{
                    d.active = false;
                    return 0;
                }
            });


    	// Add the Legend
    	
    	// calculate the x/y position

    	x_pos =  (legendSpace/2)+(i%7)*legendSpace*1.3;
    	y_pos =  parseInt(i/7)*25;

        svg1.append("text")
            .attr("x",x_pos)  // space legend
            .attr("y",y_pos)
            .attr("class", "legend")    // style the legend
            .style("fill", function() { // Add the colours dynamically
                return d.color = color(d.key); })
            .attr("id", 'label_'+d.key.replace(/[.]/g, '_')) // assign ID
            .style("opacity",function(){
                // Determine if current line is visible 
                var active   = d.active ? false : true,
                newDisplay = active ? 0.4 : 1;
                // change label's state
        
                // Update whether or not the elements are active
                return newDisplay;
            })
            .style("text-decoration",function(){
                // Determine if current line is visible 
                var active   = d.active ? false : true,
                newDisplay1 = active ? "line-through" : "";
                // change label's state
        
                // Update whether or not the elements are active
                d.active = active;
                return newDisplay1;
            })
            .on("click", function(){
                // Determine if current line is visible 
                var active   = d.active ? false : true,
                newOpacity = active ? 0 : 1;
        		newDisplay = active ? 0.4 : 1;
        		newDisplay1 = active ? "line-through" : "";
                // Hide or show the elements based on the ID
                d3.select("#tag"+d.key.replace(/[.]/g, '_'))
                    .transition().duration(100) 
                    .style("opacity", newOpacity); 
                // change label's state
                d3.select("#label_"+d.key.replace(/[.]/g, '_'))
                    .style("opacity", newDisplay) 
                    .style("text-decoration",newDisplay1); 
		
                // Update whether or not the elements are active
                d.active = active;
                })  
            .text(d.key);
    });

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

});
```

# 6. 数据前期处理

> 参考[https://www.kaggle.com/rojour/boston-results/kernels](https://www.kaggle.com/rojour/boston-results/kernels)

## 6.1 第一步处理:将选手成绩分段取平均配速

原始数据为，2015-2017年三年波士顿马拉松选手的成绩csv文件。每位选手的国籍性别等个人信息，以及每5km的配速信息，一个选手一条记录。

数据处理的第一步，将三个csv文件，处理成9个csv文件，处理后的csv文件为，每年分为3个csv文件，分别是不分男女，男和女的不同水平选手的平均配速，结构如下：

![image](https://user-images.githubusercontent.com/18595935/37703876-75b2aa54-2d3a-11e8-9a8a-f6422ba26c6d.png)

处理代码如下:

- import相关库

```python
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
%matplotlib inline

from datetime import datetime
import time
```

- 读取指定数据，以及设定本次处理的数据类别(例:男性选手)，以及输出的文件名(例:2016年男性选手)

```python
df = pd.read_csv('data/marathon_results_2016.csv', index_col='Bib')
df = df.query('MF == "M"')
outputfilepath = "data/result_summary_2016M.csv"
```

- 浏览当前数据dataframe结构(字段及类型等)

```python
df.info()
```

- 将指定的第9到21列数据转换为时间类型

```python
df.iloc[:, 9:21] = df.iloc[:, 9:21].apply(pd.to_timedelta)
```

- 转换数据格式，输出为`2.21`以小时为单位的格式

```python
officialtime_hour = df['Official Time'].apply(lambda x: x.total_seconds()/3600)
```

- 将上面生成的新格式数据，添加成df的新的一列

```python
df['officialtime_hour'] = officialtime_hour
```

- 将每5km的配速转换为min/km格式

```python
pace_5k = df['5K'].apply(lambda x: x.total_seconds())/(5*60)
pace_10k = (df['10K'].apply(lambda x: x.total_seconds()) - df['5K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_15k = (df['15K'].apply(lambda x: x.total_seconds()) - df['10K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_20k = (df['20K'].apply(lambda x: x.total_seconds()) - df['15K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_25k = (df['25K'].apply(lambda x: x.total_seconds()) - df['20K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_30k = (df['30K'].apply(lambda x: x.total_seconds()) - df['25K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_35k = (df['35K'].apply(lambda x: x.total_seconds()) - df['30K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_40k = (df['40K'].apply(lambda x: x.total_seconds()) - df['35K'].apply(lambda x: x.total_seconds()))/(5*60)
pace_42k = (df['Official Time'].apply(lambda x: x.total_seconds()) - df['40K'].apply(lambda x: x.total_seconds()))/(2.195*60)
```

- 添加新的列

```python
df['pace_5k'] = pace_5k
df['pace_10k'] = pace_10k
df['pace_15k'] = pace_15k
df['pace_20k'] = pace_20k
df['pace_25k'] = pace_25k
df['pace_30k'] = pace_30k
df['pace_35k'] = pace_35k
df['pace_40k'] = pace_40k
df['pace_42k'] = pace_42k
```

- 根据全程的配速，将每个选手划分到指定的rank，并新增为df的新的一列

```python
# use the official time to calculate the rank
def calculate_rank(officialtime_hour):
    if officialtime_hour < 2.5:
        return "sub2.5"
    elif (officialtime_hour < 3.0) and (officialtime_hour >= 2.5):
        return "sub3"
    elif (officialtime_hour < 3.5) and (officialtime_hour >= 3):
        return "sub3.5"
    elif (officialtime_hour < 4) and (officialtime_hour >= 3.5):
        return "sub4"
    elif (officialtime_hour < 4.5) and (officialtime_hour >= 4):
        return "sub4.5"
    elif (officialtime_hour < 5) and (officialtime_hour >= 4.5):
        return "sub5"
    elif officialtime_hour >= 5:
        return "above5"
    else:
        return "unknown rank"

rank = [calculate_rank(officialtime_hour) for officialtime_hour in df['officialtime_hour']]

df['rank'] = rank
```

- 创建一个函数，用于获取不同rank上的平均配速

```python
def get_mean_per_rank(df,pace_list):
    
    mean_pace_df = pd.DataFrame()
    for pace in pace_list:
        pace_mean = []
        pace_mean.append(df.query('rank == "sub2.5"')[pace].mean())
        pace_mean.append(df.query('rank == "sub3"')[pace].mean())
        pace_mean.append(df.query('rank == "sub3.5"')[pace].mean())
        pace_mean.append(df.query('rank == "sub4"')[pace].mean())
        pace_mean.append(df.query('rank == "sub4.5"')[pace].mean())
        pace_mean.append(df.query('rank == "sub5"')[pace].mean())
        pace_mean.append(df.query('rank == "above5"')[pace].mean())
        
        mean_pace_df[pace] = pace_mean
    
    return mean_pace_df

```

- 创建一个新的df，并使用上面的函数取生成新结构的df

```python
mean_pace_df = pd.DataFrame()
pace_list = ["pace_5k","pace_10k","pace_15k","pace_20k","pace_25k","pace_30k","pace_35k","pace_40k","pace_42k"]
mean_pace_df = get_mean_per_rank(df.dropna(subset=["pace_5k","pace_10k","pace_15k","pace_20k","pace_25k","pace_30k","pace_35k","pace_40k","pace_42k"]),pace_list)
```

- 新生成dataframe的结构

```python
mean_pace_df
```

![image](https://user-images.githubusercontent.com/18595935/37703876-75b2aa54-2d3a-11e8-9a8a-f6422ba26c6d.png)

- 将上面的df，写入csv文件中

```python
mean_pace_df.to_csv(outputfilepath)
```

## 6.2 合并上述CSV，并改变CSV结构以适应D3的数据读取

- 将上述的9个文件合并到一个CSV中

```python
df = pd.read_csv('result_summary_all.csv', index_col='idx')
```

- 改变CSV结构

```python
for i in range(len(df)):
    for ii in range(9):
        pace = df.iloc[i, ii+3]
        new_row = [df.iloc[i, 0],df.iloc[i, 1],df.iloc[i, 2],pace,df.iloc[:, ii+3].name]
        print(new_row)
```

修改后的CSV结构如下:

```python
[2015, 'Both', 'sub2.5', 3.2663492060000001, 'pace_5k']
[2015, 'Both', 'sub2.5', 3.3029761899999999, 'pace_10k']
[2015, 'Both', 'sub2.5', 3.3484920630000001, 'pace_15k']
[2015, 'Both', 'sub2.5', 3.3687301589999996, 'pace_20k']
[2015, 'Both', 'sub2.5', 3.369722222, 'pace_25k']
...
```




