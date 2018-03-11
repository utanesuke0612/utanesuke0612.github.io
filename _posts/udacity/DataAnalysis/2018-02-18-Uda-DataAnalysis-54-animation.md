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

> 下面的效果图如下: [02_globe_styled.html](http://www.utanesuke.shop/d3/globe/02_globe_styled.html)

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

# 14. 使用嵌套函数加载数据

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
                               .scale(140)
                               .translate([width / 2, height / 1.2]);
        
        var path = d3.geo.path().projection(projection);

        var map = svg.selectAll('path')
                     .data(geo_data.features)
                     .enter()
                     .append('path')
                     .attr('d', path)
                     .style('fill', 'lightBlue')
                     .style('stroke', 'black')
                     .style('stroke-width', 0.5);

        function plot_points(data) {
            //draw circles logic
        };

        var format = d3.time.format("%d-%m-%Y (%H:%M h)");

        d3.tsv("world_cup_geo.tsv", function(d) {
          d['attendance'] = +d['attendance'];
          d['date'] = format.parse(d['date']);
          return d;
        }, plot_points);
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

上面使用了嵌套函数来记载数据，顺序如下：
1. 调用`d3.json`函数，加载json数据，加载完毕后调用draw函数
2. 调用`draw`函数，在`d3.tsv`函数内，先加载tsv数据，加载完毕后，再调用`plot_points`函数

# 15. 嵌套函数

如需了解更多关于 D3 嵌套函数的信息，请查阅 [D3 嵌套文档](https://github.com/d3/d3/wiki#-nest)和 [D3 嵌套示例](http://bl.ocks.org/phoebebright/raw/3176159/)。


# 46. 世界杯代码和故事小结

> [22_globe_adding_events.html](http://www.utanesuke.shop/d3/worldcup/22_globe_adding_events.html)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="http://d3js.org/d3.v3.min.js"></script>
    <style>
      circle {
        fill: orange;
        stroke: black;
        stroke-width: 0.7;
        opacity: 0.7;
      }

      h2 {
        text-align: center;
        color: black;
      }

      div.years_buttons {
        position: fixed;
        top: 5px;
        left: 50px;
      }

      div.years_buttons div {
        background-color: rgb(251, 201, 127);
        padding: 3px;
        margin: 7px;
      }
    </style>
    <script type="text/javascript">  
      function draw(geo_data) {
        "use strict";
        var margin = 75,
            width = 1400 - margin,
            height = 600 - margin;

        d3.select("body")
          .append("h2")
          .text("World Cup ");

        var svg = d3.select("body")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin)
            .append('g')
            .attr('class', 'map');

        var years = [];

          for(var i = 1930; i < 2015; i += 4) {
            if(i !== 1942 && i !== 1946) {
              years.push(i);
            };
          }

        var projection = d3.geo.mercator()
                               .scale(140)
                               .translate([width / 2, height / 1.2]);

        var path = d3.geo.path().projection(projection);

        var map = svg.selectAll('path')
                     .data(geo_data.features)
                     .enter()
                     .append('path')
                     .attr('d', path)
                     .style('fill', 'lightBlue')
                     .style('stroke', 'black')
                     .style('stroke-width', 0.5);

        function plot_points(data) {
            
            function agg_year(leaves) {
                var total = d3.sum(leaves, function(d) {
                    return d['attendance'];
                });

                var coords = leaves.map(function(d) {
                    return projection([+d.long, +d.lat]);
                });

                var center_x = d3.mean(coords, function(d) {
                    return d[0];
                });

                var center_y = d3.mean(coords, function(d) {
                    return d[1];
                });

                var teams = d3.set();

                leaves.forEach(function(d) {
                    teams.add(d['team1']);
                    teams.add(d['team2']);
                });

                return {
                  'attendance' : total,
                  'x' : center_x,
                  'y' : center_y,
                  'teams' : teams.values()
                };
            }

            var nested = d3.nest()
                           .key(function(d) {
                              return d['date'].getUTCFullYear();
                           })
                           .rollup(agg_year)
                           .entries(data);

            var attendance_max = d3.max(nested, function(d) {
                return d.values['attendance'];
            });

            var radius = d3.scale.sqrt()
                           .domain([0, attendance_max])
                           .range([0, 15]);

            function key_func(d) {
                return d['key'];
            }

            svg.append('g')
               .attr("class", "bubble")
               .selectAll("circle")
               .data(nested.sort(function(a, b) { 
                  return b.values['attendance'] - a.values['attendance'];
               }), key_func)
               .enter()
               .append("circle")
               .attr('cx', function(d) { return d.values['x']; })
               .attr('cy', function(d) { return d.values['y']; })
               .attr('r', function(d) {
                    return radius(d.values['attendance']);
               })

          function update(year) {
              var filtered = nested.filter(function(d) {
                  return new Date(d['key']).getUTCFullYear() === year;
              });

              d3.select("h2")
                .text("World Cup " + year);

              var circles = svg.selectAll('circle')
                               .data(filtered, key_func);

              circles.exit().remove();

              circles.enter()
                     .append("circle")
                     .transition()
                     .duration(500)
                     .attr('cx', function(d) { return d.values['x']; })
                     .attr('cy', function(d) { return d.values['y']; })
                     .attr('r', function(d) {
                        return radius(d.values['attendance']);
                     });

              var countries = filtered[0].values['teams'];

              function update_countries(d) {
                  if(countries.indexOf(d.properties.name) !== -1) {
                      return "lightBlue";
                  } else {
                      return 'white';
                  }
              }

              svg.selectAll('path')
                 .transition()
                 .duration(500)
                 .style('fill', update_countries)
                 .style('stroke', update_countries);

          }

          var year_idx = 0;

          var year_interval = setInterval(function() {
            update(years[year_idx]);

            year_idx++;

            if(year_idx >= years.length) {
                clearInterval(year_interval);

                var buttons = d3.select("body")
                        .append("div")
                        .attr("class", "years_buttons")
                        .selectAll("div")
                        .data(years)
                        .enter()
                        .append("div")
                        .text(function(d) {
                            return d;
                        });

                buttons.on("click", function(d) {
                    d3.select(this)
                      .transition()
                      .duration(500)
                      .style("background", "lightBlue")
                      .style("color", "white");
                    update(d);
                });
            }
          }, 1000);
      }

      var format = d3.time.format("%d-%m-%Y (%H:%M h)");

      d3.tsv("world_cup_geo.tsv", function(d) {
        d['attendance'] = +d['attendance'];
        d['date'] = format.parse(d['date']);
        return d;
      }, plot_points);
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

# 44. 向按钮添加事件

Javascript 的 'this'
[清楚理解并掌握 JavasScript 的 'this']()

如果你需要可以快速查阅的信息，[此篇博文]()的部分内容向你提供了简洁明了的解释。

如需深入研究 JavaScript 的关键词 this，你可以就关键词 this 学习[面向对象的 JavaScript 课程]()！

Javascript 事件
[D3.js 鼠标事件](http://www.stator-afm.com/tutorial/d3-js-mouse-events/)（作者：Anthony Nosek）

[鼠标悬停、鼠标移出、鼠标按下教程](http://christopheviau.com/d3_tutorial/)（作者：Christophe Viau）

[向 D3.js 图形添加工具提示](http://www.d3noob.org/2013/01/adding-tooltips-to-d3js-graph.html)


# 48. Matt 关于制作地图的提示

示例:

[https://plot.ly/~etpinard/453/average-daily-surface-air-temperature-anomalies-c-in-july-2014-with-respect-to-1/](https://plot.ly/~etpinard/453/average-daily-surface-air-temperature-anomalies-c-in-july-2014-with-respect-to-1/
)

温度异常值是长期平均温度的差值。[来源](http://ete.cet.edu/gcc/?/globaltemp_anomalies/)

视频 1:16 处，Matt 说：“一个是在散点图顶部的等高线图。”当把鼠标悬停在地图上时，散点图的方位即为呈现出来的坐标值。

[https://plot.ly/~MattSundquist/878/the-1000-most-populous-canadian-cities/](https://plot.ly/~MattSundquist/878/the-1000-most-populous-canadian-cities/)

**D3 资源**

- [让我们制作地图](https://bost.ocks.org/mike/map/)（作者：Mike Bostock）
- [让我们制作气泡图](https://bost.ocks.org/mike/bubble-map/)（作者：Mike Bostock）
- [使用 D3 制作出的多个小型地图](https://blog.webkid.io/multiple-maps-d3/)
- [已被解释过的 D3.js 简单地图](http://www.d3noob.org/2013/03/a-simple-d3js-map-explained.html)
- [如何在 D3 中制作面量图](https://visual.ly/blog/how-to-make-choropleth-maps-in-d3/)（作者：EJ Fox）

**其他资源**
- [R 地图包文档](http://cran.r-project.org/web/packages/maps/maps.pdf)
- [Python 中的工作草图](https://pypi.python.org/pypi/basemap/1.0.7)

视频 2:13 处，Matt 提到用来制作地图的 GUI。图形用户界面 (Graphical User Interface) 或 GUI 是一款点击式软件，是命令行界面的替代方案。Tableau 和 Data Wrapper 是 Matt 提到的两款 GUI。

[Tableau](https://www.tableau.com/)
[Data Wrapper](https://www.datawrapper.de/)

# 50. 再见，继续学习吧 

- [Mike Bostock 的许多示例。](https://bost.ocks.org/mike/example/)
- [Observable is a better way to code](https://beta.observablehq.com/) (有关于地图的示例)