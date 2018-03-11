---
layout: post
title: Uda-DataAnalysis-53-机器学习[未完]-叙事结构
date: 2018-02-18 07:00:00
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 6. 获取数据

Scott 解释说，创建数据可视化 90% 的时间实际上都花在“寻找、验证、解析、筛选和探索数据”上。在数据科学及尝试回答数据问题的背景下，的确如此。幸运的是，有很多资源可以任你使用，来解决这些重要的任务。

标题文本“获取数据”中的链接包含很多探寻数据的绝妙技巧，我们建议你查阅以下两个章节：[五分钟实战指南](http://datajournalismhandbook.org/1.0/en/getting_data_0.html)和[从 Web 获取数据](http://datajournalismhandbook.org/1.0/en/getting_data_3.html)。你还可以给“获取数据”资源加上标签，在以后使用。

# 7. 如何用柱状图撒谎

柱状图应该遵守从0开始的原则，但是下图是从34%开始的：

![image](https://user-images.githubusercontent.com/18595935/37241199-88a12ea6-2498-11e8-991b-6d47785ad2d8.png)

> 参考[Fox News 继续保持卓越绘图](http://flowingdata.com/2012/08/06/fox-news-continues-charting-excellence/)

# 8. 如何用饼图撒谎

[把馅饼留作甜点吧（Save the Pies for Dessert）](http://www.perceptualedge.com/articles/visual_business_intelligence/save_the_pies_for_dessert.pdf)

# 9. 如何用线形图撒谎

[Misleading With Statistics](https://medium.com/i-data/misleading-with-statistics-c63780efa928)

# 10. 偏差类型

- **偏差类型**
之前 Cole 和 Matt 分享的数据可视化包含偏差。在构造图形时有三种偏差需要注意：作者偏差、数据偏差和读者偏差。

- **作者偏差**
Cole 和 Matt 的数据可视化包含作者偏差。也就是说，可视化的设计者和呈现者（无意或有意地）通过可视化编码或其他设计选择（如图表类型）篡改了数据。如果你将来想使用三维饼图，请记住 Andy Kriebel 的一句话“真的朋友不会让自己的朋友使用饼图”。

作为数据可视化的设计者或呈现者，你的设计选择应该在读者和图形之间建立信任。你的设计选择应该促进信息的交流。否则就像 Cole 指出的那样，你的信息会在读者中面临整体可信度风险。

- **数据偏差**
在了解数据偏差之前，我们想让你先看一个视频，在这个视频中 Scott 回答了 Cole 和 Matt 的同样问题。但 Scott 用另一种方式解释了他认为什么是“主观”数据可视化。

- **读者偏差**
我们将在几个视频之后讲解这种偏差。

# 12. 数据偏差

数据偏差产生于数据收集过程中。系统测量误差或有缺陷的设备会使原始数据值产生偏差，而选择偏差会导致不能代表特定问题兴趣群体的子组。数据偏差和抽样方法不在此课程的范围之内，但是我们鼓励你多多了解这些话题。你可以阅读一些关于数据收集、抽样方法或其他偏差话题的文章。Scott Murray 将在下一个视频中提及测量误差的一个示例。

# 18. 作者驱动/读者驱动/马提尼酒杯

![image](https://user-images.githubusercontent.com/18595935/37248138-ad705dd2-250c-11e8-8ccb-7baf3b701449.png)

# 21. 无人机空袭和枪击死亡

[无人机空袭](http://drones.pitchinteractive.com/)和[枪击死亡](https://guns.periscopic.com/?year=2013)

# 25. 解密 D3

Demystifying D3 - Declarative API

Q: How do I draw a circle for every row of my data?

```
d3.select("svg")
 .selectAll("circle")
 .data(data)
 .enter()
 .append("circle")
```

[用连接来思考Thinking with Joins](https://bost.ocks.org/mike/join/)

# 28. D3 中的联接

![image](https://user-images.githubusercontent.com/18595935/37248278-1c4cab4e-2511-11e8-909c-27a877fa3113.png)

要更详细地了解联接和选择，请参考以下文章。
- [三个小圆圈](https://bost.ocks.org/mike/circles/)（作者：Mike Bostock）
- [运用联接来思考](https://bost.ocks.org/mike/join/)（作者：Mike Bostock）
- [数据绑定](http://alignedleft.com/tutorials/d3/binding-data)（作者：Scott Murray）

# 30. 使用维恩图思考

![image](https://user-images.githubusercontent.com/18595935/37248299-e901b5c6-2511-11e8-82d9-7ca255e72715.png)

**.exit()** 和 **.enter()** 这两个函数可以视为相反的函数。
- **.enter()**会返回不在 index.html（页面上）的 data.tsv 的每行数据选择的所有元素。
- **.exit()**会返回 index.html（页面上）选择的未绑定到数据的所有元素。


# 31. 未完待续

> 未完待续