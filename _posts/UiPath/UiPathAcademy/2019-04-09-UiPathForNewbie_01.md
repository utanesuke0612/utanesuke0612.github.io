---
layout: post
title: 小白学UiPath-01-RPA基础
date: 2019-04-08 01:01:01
categories: RPA
tags: RPA
---
* content
{:toc}

> 机缘巧合进入了UiPath工作，这个RPA领域的领头羊，冥冥之中注定的吧，自己这两年来一直为进一家自动驾驶工作而努力，结果一个星期的时间，就从第一次听说RPA，到签约这家公司，这就是缘分。自己的第一个小目标，就是一年内升为**RPA高级顾问**，成为RPA领域的专家。

![image](https://user-images.githubusercontent.com/18595935/55791438-7357c800-5af9-11e9-86c4-41ae0653c1a1.png)
> <<小白学UiPath>>系列主要根据上面的书本整理而成。

本篇文章中，主要介绍：
1. 什么是RPA？RPA有什么作用？
2. RPA能给公司带来什么？
3. 使用UiPath开始RPA

# 1. 什么是RPA？

如果不是在相关领域工作的人，听到RPA估计也是一脸的懵逼，RPA是*Robotic Process Automation*的缩写，即机器人业务自动化，使用RPA的主要目的，是将人类中PC重复作业中解放出来，进行一些更有创造性的事情。

RPA将基于规则的常规操作自动化，例如读取邮件和系统，计算，生成文件和报告，检查文件等，因此，RPA的应用范围非常广泛。在未来，那些你不想做的枯燥的工作，也许真的可以不做了，重复化、标准化的工作都可以让机器人帮你完成。

这里有一个视频解释了RPA是什么，能够完成什么工作 [什麼是RPA, 它又如何幫助企業提升效率？](https://www.youtube.com/watch?v=LTZLZFAlNs8)

上面的定义比较概括，关于RPA主要要理解下面两点:
1. RPA虽然号称机器人，但是它没有实体，是运行在PC上的软件机器人
2. RPA应用场景为：大量重复，规则明确

如果使用过excel的宏应该知道， 在Excel 中, 若要自动执行重复任务, 可以使用宏录制器快速记录宏中的步骤, 然后单击一次即可重新执行该任务。

RPA也比较类似，不过它不局限于Excel，适用于任何windows上的软件，比如浏览器/Office/SAP等，实现请求书发行，顾客管理，在库管理等一系列重复工作的自动化。另外，通过与其他设备的组合，有更加大的威力。

![image](https://user-images.githubusercontent.com/18595935/55794325-e8c69700-5aff-11e9-80db-a951c11fb680.png)

# 2. RPA能给公司带来什么？

RPA给公司带来的主要好处在于能够降低成本、提高质量和缩短响应时间。通过自动化手动和容易出错的工作来降低风险，通过大规模简化和自动化流程来提高效率，将员工的时间释放出来，让员工把时间和关注点放在更有价值的事情上——包括重新规划工作内容，更专注地解决产品组合、利润创造以及产品定价等机器人无法替代的工作上。

![image](https://user-images.githubusercontent.com/18595935/55966082-bdd07480-5cb2-11e9-85c5-15c927077ed2.png)


# 3. 使用UiPath开始RPA

**UiPath主要具备如下特征：**

1. 操作简单

UiPath通过可视化的拖拽以及录像功能，使得其操作非常简单。

2. 精度高

能精确定位每次操作的控件，比如button/Edit box等。

3. 应用范围

UiPath既能进行简单的作业，也能应用到大规模的复杂作业上，有桌面版和服务器版两种版本，满足中小企业以及大型企业的需求。

另外，还能与其他AI，如IBM的Watson以及Google Cloud，OCR等连接使用，截止2019年1月，在日本就有800家公司导入了UiPath，世界范围内共2700家公司。

**UiPath的构成：**

由三个部分的软件构成：

1. UiPath Studio: 作成Robot
2. UiPath Robot: 执行Robot
3. UiPath Orchestrator: 管理Robot

![image](https://user-images.githubusercontent.com/18595935/55966985-70ed9d80-5cb4-11e9-8926-89431013ec5a.png)

## 3.1 UiPath的基本操作

有如下一系列操作：
1. 从浏览器中选取一段内容
2. copy这段内容
3. 将这段内容，粘贴到word中

上面的这个作业整体，叫做一个**project**, 单个操作叫做一个**activity**，从1到3这一系列的操作叫做**workflow**。

可以通过下面三种方式完成一个workflow，可以相互结合使用：
1. 自动recording
2. 手动recording
3. programing


## 3.2 UiPath Studio主要构成

主要有编辑和执行两部分构成：

- 编辑：

![image](https://user-images.githubusercontent.com/18595935/56077026-487bb580-5e12-11e9-990e-451fd4ac3818.png)

- 执行：

![image](https://user-images.githubusercontent.com/18595935/56077030-61846680-5e12-11e9-852a-6993a7044700.png)

# 4. Recording

![image](https://user-images.githubusercontent.com/18595935/56077216-7c57da80-5e14-11e9-8d8e-fddca73d4000.png)

如上图是进行一个recording时常用的四个button，**新建**,**保存**,**执行**,**recording**。

另外recording有5类:
1. basic，标准记录方式，记录桌面软件的操作以及鼠标的移动。几乎所有场景，都是使用basic和desktop方式。每个activity中保存了`什么window`,`什么button`是操作对象。
2. desktop，与basic一样都是标准记录方式，同样记录桌面软件的操作与鼠标的移动，与上面basic不同的是，每个activity中保存的是相对位置信息，这使得需要customize时非常方便。
3. web，专门用于记录浏览器或是web程序的记录方式，与desktop一样，每个activity中保存的是相对位置信息。
4. 画像，basic和desktop通过menu和window的text信息进行特定，但是如果没有text时就无法特定了，比如FLASH和虚拟化环境中的操作，这时需要通过画像的方式去recording。
5. native Citrix，与desktop类型，但是是在Citrix环境中特有的记录方式。

**recording的controller：**

![image](https://user-images.githubusercontent.com/18595935/56077409-e40f2500-5e16-11e9-986e-267f4043517d.png)

- 自动recording：只使用①和②两个按钮，只能记录鼠标左键按下，以及text输入。
- 手动recording：使用所有按钮，能记录各种复杂的操作，如程序开始结束，左键按下，双击，右键...。

## 4.1 自动Recording与执行

1. UiPath Studio的编辑主界面中，点击 recording → basic。
2. Basic Controller中，点击 recording 开始进行录制。
3. 选取要录制的记事本，并在弹出框中输入要录入的文字，最后enter结束。
4. 按下ESC键，结束录制。
5. 保存并终止basic controller，返回UiPath主界面，点击保存，这样就得到了一个自动录制的Project。

![image](https://user-images.githubusercontent.com/18595935/56077620-55e86e00-5e19-11e9-8c12-be62e57c62d9.png)

在主界面中按下`実行`后，能自动执行刚才的workflow，能在记事本中自动录入文字，录入后如下图：

![image](https://user-images.githubusercontent.com/18595935/56077651-b11a6080-5e19-11e9-9ee0-67e5fb6f34c0.png)

## 4.2 手动Recording与执行









