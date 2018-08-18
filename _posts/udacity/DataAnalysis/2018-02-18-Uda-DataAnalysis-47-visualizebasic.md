---
layout: post
title: Uda-DataAnalysis-47-机器学习-可视化基础
date: 2018-02-18 01:00:00
categories: 数据分析
tags: R DataAnalysis 
---
* content
{:toc}

# 4. 功能化艺术 - 肥胖与教育

参考:
- [Alberto Cairo: Three steps to become a visualization/infographics designer (a Tableau version)](http://www.vizwiz.com/2013/01/alberto-cairo-three-steps-to-become.html)
- [A new data visualization tool: Flourish](http://www.thefunctionalart.com/2018/02/a-new-data-visualization-tool-flourish.html)

这是一幅很好的可视化作品，[肥胖与教育](https://public.tableau.com/shared/N2ZFK6MW8?:display_count=yes),线的左端表示学历，右端表示肥胖率，棕色的线表示低学历，高肥胖率，蓝色的线表示高学历，低肥胖率。

![image](https://user-images.githubusercontent.com/18595935/36357405-fe2f6398-1540-11e8-9dec-14dbc23dbc18.png)

# 9. 数据科学过程

下图来自BenFry博士论文：

![image](https://user-images.githubusercontent.com/18595935/36357548-06116e38-1543-11e8-9e31-3cd322c3ea27.png)

1. 包含数据获取与解析，比如从网络数据中抓取,日志采集,数据库存取等，涉及到计算机科学
2. 数据过滤与挖掘，这部分与数据科学练习最密切，涉及到统计与数据挖掘
3. 呈现，涉及到可视化涉及
4. 与观众有关，涉及到信息可视化和人机交互领域的技巧

上述的过程并不是瀑布式而是不断迭代的过程。

# 14. Anscombe 四重奏

下面的四个数据，有相同的均值，方差等统计要素，直接通过统计量无法看出差别，而可视化的图形上对其差异可以一目了然。

![image](https://user-images.githubusercontent.com/18595935/36357680-c6248a6a-1544-11e8-97fd-37bb67c23a3d.png)

# 16. 数据类型

- [不同数据类型 1 — 数值数据](https://classroom.udacity.com/courses/ud359/lessons/692548568/concepts/6785689350923)
- [不同数据类型 2 — 类别数据](https://www.udacity.com/course/viewer#!/c-ud359/l-692548568/m-678568936)
- [不同数据类型 3 — 时间序列数据](https://classroom.udacity.com/courses/ud359/lessons/692548568/concepts/6785689370923)

在统计学中，统计数据主要可分为四种类型，分别是定类数据，定序数据，定距数据，定比变量。
1. 定类数据（Nominal）：名义级数据，数据的最低级，表示个体在属性上的特征或类别上的不同变量，仅仅是一种标志，没有序次关系。例如， ”性别“，”男“编码为1，”女“编码为2。
2. 定序数据（Ordinal）:数据的中间级，用数字表示个体在某个有序状态中所处的位置，不能做四则运算。例如，“受教育程度”，文盲半文盲=1，小学=2，初中=3，高中=4，大学=5，硕士研究生=6，博士及其以上=7。
3. 定距(定量)数据（Interval,quantitative）:具有间距特征的变量，有单位，没有绝对零点，可以做加减运算，不能做乘除运算。例如，温度。
4. 定比变量（Ratio）:数据的最高级，既有测量单位，也有绝对零点，例如职工人数，身高。

# 17. 识别数据类型

![image](https://user-images.githubusercontent.com/18595935/36378531-8759b196-15be-11e8-91cd-55e637ff6ed7.png)

- Doctor visits Per Year:Ordered
- Life Expectancy:Quantitative
- Spending Per Person:Quantitative
- Has Universal Healthcare:Nominal 

# 18. 视觉编码

![image](https://user-images.githubusercontent.com/18595935/36379194-0316e1f8-15c1-11e8-9dd3-7838ec7af967.png)

如下的变量称为视网膜变量，用图标的大小，颜色的等级来表示有序数据，比如国家的人口；用不同的颜色或不同性质的图标或不同文理，表示种类数据，比如国家。

![image](https://user-images.githubusercontent.com/18595935/36379282-55d27880-15c1-11e8-95da-590b5f93683c.png)

# 19. 世界杯射手榜可视化的编码

![image](https://user-images.githubusercontent.com/18595935/36379408-cfc17308-15c1-11e8-8cb5-4713195fb447.png)

可视化的编码方式：

|Variable|VisualEncoding|
|:--|--:|
|Country|position x|
|Goals Scored|size|
|Player|position x|
|Time|position y|
|TopScorer|color hue|

# 20. 胜、负或平的可视化编码

一个柱子表示一场球赛，柱子朝上表示win，朝下表示lose，☆表示该届世界杯冠军。

![image](https://user-images.githubusercontent.com/18595935/36379820-5b44c942-15c3-11e8-83e6-f49c34e3ac13.png)

可视化的编码方式：

|Variable|VisualEncoding|
|:--|--:|
|Country|color hue|
|Game Win/Loss| postion y / orientation |
|Scoring Margin|position y / length |
|WorldCupWinner|shape |
|Time| position x |

# 21. 视觉编码的排序

![image](https://user-images.githubusercontent.com/18595935/36380566-1a15e91c-15c6-11e8-8452-8febad46a8c8.png)

左图表示传递信息的准确度，所以最重要的变量都用x和y轴表示。


# 22. 分解可视化图形

非常好的一篇文章[Visual Encoding](https://www.targetprocess.com/articles/visual-encoding/)

# 23. Facebook 募股

参考图形：[The Facebook Offering: How It Compares](http://www.nytimes.com/interactive/2012/05/17/business/dealbook/how-the-facebook-offering-compares.html)

# 26. 在可视化光谱中穿梭

D3使用了CSS/HTML/Javascript/SVG等开放网络技术。

![image](https://user-images.githubusercontent.com/18595935/36450763-4c7acd0c-16d2-11e8-9bd2-0b4d57e8958d.png)

关于上面涉及到的技术，更详细的参考：

- [HTML5 Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
- [WebGL](https://en.wikipedia.org/wiki/WebGL)
- [SVG（可缩放向量图形）](https://developer.mozilla.org/en-US/docs/Web/SVG)
- [D3.js](https://d3js.org/)
- [NVD3](http://nvd3.org/)
- [Dimple.js](http://dimplejs.org/)
- [Rickshaw](http://code.shutterstock.com/rickshaw/)
- [Chartio](https://chartio.com/)
- [RAW](https://densitydesign.org/2013/10/raw-the-missing-link-between-spreadsheets-and-vector-graphics/)

# 27. D3网页技术

D3是Data Driven Documents的简称，即通过数据驱动文档，数据Data指如xml或json文件，文档Documents指html/svg元素，通过D3将数据与文档联系在一起。

1. When does the DOM get created? `During Page load`，在浏览器接收到html源的时候，就开始一点点的构建DOM对象。
2. How can the DOM be accessed? `JavaScript API`,本unit通过浏览器和JavaScript来解析DOM。
3. The DOM is a specification and hierarchical object.

# 29. 为什么选用D3？

关于网页技术上的服务器端与客户端的执行，参考[网页脚本：客户端与服务器端](https://study.com/academy/lesson/web-scripting-client-side-and-server-side.html#lesson)

使用D3的好处有:
1. Leverages existing technologies(DOM,CSS,SVG,etc)
2. Seperation of concerns
3. Benefits from advances in browser related technologies(javascript,HTML5,etc)







