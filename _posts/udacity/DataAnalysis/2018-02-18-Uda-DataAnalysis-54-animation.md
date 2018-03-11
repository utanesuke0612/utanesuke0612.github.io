---
layout: post
title: Uda-DataAnalysis-54-机器学习[ing]-动画与互动
date: 2018-02-18 08:00:00
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 5. 让我们制作地图

[Let’s Make a Map](https://bost.ocks.org/mike/map/),但是这个文章有些古老，这些新作[Command-Line Cartography](https://medium.com/@mbostock/command-line-cartography-part-1-897aa8f8ca2c)

地形（topography，地面的高度或形状）与拓扑结构（topology，在这种情况下与地点之间的邻接关系和连接有关）这两个词拼法很像，但它们是不同的。TopoJSON 对拓扑结构编码，不对地形进行编码。

[地图学习](https://mapschool.io/)

Check all of the following which are benefits of GeoJSON over Shapefiles.
- can be parsed by most programming languages
- human readable

# 7. 什么是投影？

![image](https://user-images.githubusercontent.com/18595935/37248702-405eb1fc-251c-11e8-876f-8dbe0e9ddfa7.png)


![image](https://user-images.githubusercontent.com/18595935/37248718-6b7f5e72-251c-11e8-8fc8-e8d4b8fa9efd.png)

Longitude values actually come first in GeoJSON. Draw a picture of latitude and longitude lines. As you move across lines of longitude the horizontal position changes. It's similar to how the x-coordinate is listed before y-coordinates for points (x, y).

The mercator projection actually stretches areas near the poles. This is why Greenland and Antarctica appear so large in mercator projections.

mercator投影选择扭曲人最少的两极，即通过赤道将地球切开展平。

- longitude:経度 Y
- latitude:緯度 X
- equator:赤道
- Antarctica:南極大陸

![image](https://user-images.githubusercontent.com/18595935/37248802-acfa351a-251d-11e8-87bc-530b2ce7a4cd.png)

- 练习

![image](https://user-images.githubusercontent.com/18595935/37248819-3794c47e-251e-11e8-9722-368e4653e925.png)

# 8. 地图变形

![image](https://user-images.githubusercontent.com/18595935/37248947-b0b569d8-2520-11e8-818d-20bf4aff5fe2.png)

- 练习

1. mercator投影产生非对称的扭曲，另外在经线上逐渐递增。
2. mercator投影在纬度方向上，扭曲度是一样的。

![image](https://user-images.githubusercontent.com/18595935/37248905-22e56130-2520-11e8-8f59-9f0ba12c0b0c.png)


# 9. D3中的地图

[Ogre](http://ogre.adc4gis.com/)：将空间文件转换为 GeoJSON

[如何将形状文件转换为可在 Github 上使用的 GeoJSON](https://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/)（作者：Ben Balter）

如果你想了解 GeoJSON 值如何转化为视觉表征，[geojson.io](http://geojson.io/#map=2/20.0/0.0) 是一款交互式的 GeoJSON 编辑器。

> 下面的效果图如下: [02_globe_styled.html]()

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="http://d3js.org/d3.v3.min.js"></script>
    <style>
    </style>
    <script type="text/javascript">  
      function draw(geo_data) {
        "use strict";
        var margin = 75,
            width = 1400 - margin,
            height = 600 - margin;

        var svg = d3.select("body")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin)
            .append('g')
            .attr('class', 'map');

        var projection = d3.geo.mercator()
                               .scale(150)
                               .translate( [width / 2, height / 1.5]);

        var path = d3.geo.path().projection(projection);

        var map = svg.selectAll('path')
                     .data(geo_data.features)
                     .enter()
                     .append('path')
                     .attr('d', path)
                     .style('fill', 'lightBlue')
                     .style('stroke', 'black')
                     .style('stroke-width', 0.5);
      };
      </script>
  </head>
<body>
  <script type="text/javascript">
  /*
    Use D3 to load the GeoJSON file
    */
    
d3.json("world_countries.json", draw);
  </script>
</body>
</html>
```