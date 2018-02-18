---
layout: post
title: Uda-DataAnalysis-47-机器学习[ing]-可视化基础
date: 2018-02-18 01:00:00
categories: 数据分析
tags: R Udacity DataAnalysis 
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

1.定类数据（Nominal）：名义级数据，数据的最低级，表示个体在属性上的特征或类别上的不同变量，仅仅是一种标志，没有序次关系。例如， ”性别“，”男“编码为1，”女“编码为2。
2.定序数据（Ordinal）:数据的中间级，用数字表示个体在某个有序状态中所处的位置，不能做四则运算。例如，“受教育程度”，文盲半文盲=1，小学=2，初中=3，高中=4，大学=5，硕士研究生=6，博士及其以上=7。
3.定距(定量)数据（Interval,quantitative）:具有间距特征的变量，有单位，没有绝对零点，可以做加减运算，不能做乘除运算。例如，温度。
4.定比变量（Ratio）:数据的最高级，既有测量单位，也有绝对零点，例如职工人数，身高。

# 18. 


