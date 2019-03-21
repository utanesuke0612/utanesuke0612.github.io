---
layout: post
title: Coursera-Self-Driving Cars-U1-04-练习1-运动学自行车模型
date: 2019-05-20 01:04:11
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

> 这个练习忒TM难了，画不出来8字，暂时先pass

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

通过下面的函数，将除8以外的都画出来了，8怎么也画不出来...

```python
class Bicycle(Bicycle):
    def step(self, v, w):
        # ==================================
        #  Implement kinematic model here
        # ==================================
        
        # 0. update the delta
        self.delta = self.delta + w*self.sample_time
        if(self.delta > self.w_max):   #limits the steer angle to the fisical limit
            self.delta = self.w_max
        if(self.delta < -self.w_max):
            self.delta = -self.w_max

        # 1. update the beta
        tan_delta = np.tan(self.delta)
        self.beta = np.arctan((tan_delta*(self.lr))/(self.L))
        
        # 2. update the theta
        self.theta = ((v*(np.cos(self.beta))*(np.tan(self.delta))) / self.L)*self.sample_time + self.theta
        
        # 3. update the x and y
        theta_plus_beta = self.beta + self.theta
        self.xc = (v*(np.cos(theta_plus_beta)))*self.sample_time + self.xc
        self.yc = (v*(np.sin(theta_plus_beta)))*self.sample_time + self.yc
```