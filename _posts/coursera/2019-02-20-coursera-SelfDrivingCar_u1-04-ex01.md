---
layout: post
title: Coursera-Self-Driving Cars-U1-04-练习1-运动学自行车模型
date: 2019-02-20 01:04:11
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 1. 任务

在此notebook中要实现自行车运动模型，模型接收速度和转向角作为输入，逐步实现自行车运动模型的各个公式。
最终通过这个模型，我们能提供一系列的输入，驱动自行车走8字状的路径。

输入是自行车速度v和转向角w，模型如下图：

![image](https://user-images.githubusercontent.com/18595935/53461404-cb73c700-3a83-11e9-8f12-94753b1ea170.png)

# 2. 代码

1. 最大转速为: 1.22rad/s
2. 前后轮中心点之间距离：2m
3. 后轮中心到重心距离：1.2m
4. 各个值初始化为0

```python
from notebook_grader import BicycleSolution, grade_bicycle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        
        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        
        self.sample_time = 0.01
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
```
