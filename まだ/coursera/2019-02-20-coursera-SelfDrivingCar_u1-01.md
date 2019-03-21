---
layout: post
title: Coursera-Self-Driving Cars-U1-01-The Requirements for Autonomy
date: 2019-05 まだ-20 01:01:00
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 0. 小结

# 1. M0: 无人车专题

介绍一些主要概念和这个课程的结构，讨论近二十年内这个领域内的主要进步，重点介绍了几家大公司在安全和性能等方面的最新进展。

**主要目标：**
1. Review the layout of the courses in the Specialization
2. Review the main projects offered in this course
3. Examine the state of the self-driving industry

# 2. M0-1：无人车入门

**By the end of this course, you will：**

- Learn about the elements of driving: perception,prediction, decision making 感知 预测和决策
- Understand how to design the software and hardware stack to do autonomous driving 理解如何去设计自动驾驶软硬件
- Understand common safety practices for autonomous driving 理解自动驾驶的通用安全措施
- Learn the basics of vehicle modeling and control, and design controll
ers to do speed regulation(速度控制), path following(路径跟踪)
- Use these concepts to help navigate a self driving car in CARLA

# 3. M0-2：Meet the Self-Driving Car Experts

上面两个部分的video中，介绍无人车历史以及从业人员的访谈，里面的很多句子可以背下来，面试的时候可以用。两个老师的英语简直不能更清晰了，非常棒！

# 4. M1: The Requirements for Autonomy

![image](https://user-images.githubusercontent.com/18595935/53082475-426b0600-3540-11e9-8d19-60948eb6d517.png)

**学習目標**
- Identify perception, prediction and planning requirements for driving
- Define the environmental elements that influence driving
- Breakdown the task of driving into elemental decisions and actions
- Assess the effects of driving conditions on the driving task

# 5. M1-1: 驾驶分类,感知与决策

## L1: 驾驶分类

介绍无人车的主要构成，以及技术要求，无人车分级。

**Terms and Definitions:**
- Driving task:
	+ Perceiving the environment 环境感知，感知车周边的环境，比如交通标识，其他的车辆，行人，特别是还要能预测其他车辆和行人的下一步动作，以便做决策
	+ Planning how to reach from point A to B 路径规划
	+ Controlling the vehicle 车辆控制，操作车的转向角，加速减速等控制车的位置和速度
这3个构成了无人驾驶的主要任务，在驾驶过程中一直被执行。

- ODD: Operational Design Domain(操作设计领域)
这个标识无人车被投入的领域，比如有的是在城市内运行，有的是在高速。

Clearly defining the operating conditions for which a self-driving car is designed, is crucial to ensuring the safety of the system. So the ODD needs to be planned out carefully in advance.

**How to classify driving system automation?**
1. Driver attention requirements 需要司机多大的参与，他可以同时看电影么，是否需要关注汽车转向
2. Driver action requirements，转向加速减速，是否需要人的参与
3. What exactly makes up a driving task?

**What makes up a driving task?**
1. Lateral control - steering，横向控制，左转右转等
2. Longitudinal control - braking,accelerating 纵向控制，比如加速减速等
3. Object and Event Detection and Response:detection,reaction 检测和反应，OEDR包含了无人驾驶的很大一部分工作
4. Planning(long term/short term)
5. Miscellaneous(多种多样的)，比如处理前车尾灯，其他司机的手势等。

**Autonomous Capabilities**
1. Automated lateral control? 能横向控制么，如转向，车道变换
2. Automated longitudinal control? 能否加速减速等纵向控制
3. OEDR，能否完成物体和事件检测和反应，以及能到什么程度
 - Automatic emergency response 能否自发的处理紧急事件
 - Driver supervision 或是需要人为介入
4. Complete vs Restricted ODD ，系统能在所有环境下运行么？或是在特定条件下？

**关于无人驾驶分级(SAE Standard J3 016)：**
- level0:常规驾驶,无自动化
- level1:驾驶辅助，比如常见的自动巡航和车道保持。只能横向控制或是只能纵向控制。
- level2:部分驾驶自动化，比如GM的super cruise和Nissan的Propilot Assist，虽然能同时实现纵向和横向控制，但需要驾驶员时刻监视着系统。
- leve3:特定环境下自动驾驶，与level2的区别是，在特定环境下不需要时刻监视着系统，它能提前预警，比如Audi A8的Sedan系统。
> level 3 systems cannot handle emergencies automatically and as a result require full user alertness.

- leve4:高度自动驾驶，汽车能够处理紧急情况，虽然有时可能会需要向驾驶员确认。
- level5:无条件自动驾驶，无需人工干预

## L2: 感知

分析一个驾驶任务是如何被完成的，介绍什么是感知，感知的目标是什么，以及感知现在的挑战是什么。

所有的驾驶任务都可以分解为两个部分：
1. 分析周边环境，自己所在的位置 
2. 做出驾驶的决策，比如是否要转向，加速减速等

![image](https://user-images.githubusercontent.com/18595935/53076039-03ce4f00-3532-11e9-80b2-599bea359b9e.png)

**什么是感知 perception：**
弄清楚自己和周边的环境，主要包含
1. **识别物体**，是汽车，bus，或是自行车
2. **理解行为**，识别的物体是否在移动

**感知的目标：**
- 静止的物体：
	+ 道路和车线标识(on-road)
	+ Curb 道路边线 (off-road)
	+ 信号灯 (off-road)
	+ 道路标识，比如限速牌等 (off-road)
	+ 工事中的标识啊，道路故障灯 (on-road)
- 动态的物体(on-road):
	+ 汽车，摩托车，自行车灯
	+ 行人
- Ego localization 自我定位，通过GPS,IMU和其他传感器一起完成
	+ 位置 postion
	+ 速度，加速度等
	+ 方向，方向角

**感知中的挑战：**
- 虽然现在可以通过机器学习/深度学习等来检测物体，但是要达到人类的相同认知水平，还是十分困难
- 深度学习需要大量的数据，通过大量的数据可以达到较好的识别精度，但是这个数据收集以及数据标记本身，需要耗费大量的时间和金钱。
- 传感器的不确定性，GPS/雷达/激光雷达等都可能有噪声，处理的时候要考虑这些不确定性
- Occlusion(吸收),reflection(反射)：相机和激光雷达会受到影响
- illumination(光照强度),lens flare(透镜光晕)
- Weather,precipitation(冰雹)，比如雷达很受天气影响。

**Quiz：**
1. Radar are primarily used for dynamic object detection.雷达主要用于动态物体的检测
2. ACC Adaptive Cruise Control  自适应巡航控制：adaptive cruise control detects vehicles ahead to control speed and to maintain safe driving distances.

## L3: 驾驶决策

上一课讲了感知，这部分是感知后的决策，以及决策后的执行。

**Making decisions:**
1. long-term planning decision,比如如何从北京到上海
2. short-term,能否换道，或是在交叉口能否左转
3. Immediate,时刻需要做的，比如如何在弯道上行驶,加速减速需要多少

**例子：车在交叉口左转**

![image](https://user-images.githubusercontent.com/18595935/53080315-b820a300-353b-11e9-8f12-62c5685e75c3.png)

如上图，即使是一个交叉口左转，都包含了很多的处理：
1. 识别并理解交通灯信号
2. 判断是否需要换道
3. 接近交叉口时要缓慢的停止
4. 如果有行人该如何处理
5. 如果前方有行车该如何处理
6. ...

即使像上面一个简单的case，都到了leve3/level4的程度，做决策时要考虑到安全，效率，法规等各项条件，是个非常难的问题。

**规划的方式1：reactive planning 基于规则的规划**

设定一些基于当前车，以及环境中其他物体的规则，然后做出决策。比如：
1. 有行人就停止
2. 道路限速有变化，就改变速度

**规划的方式2：Predictive Planning 预测性规划**
预测其他的车辆下一步的行动，然后用这些预测做出自己的决策。比如：
1. 前面的车停了10秒了，可能会继续停止下去。
2. 行人正在横穿马路(jaywalking)，下个时间点可能会到达正在行驶的车道。

We predict where other objects on the road will be in the future before we make our decisions.

这种方式依赖于预测的准确性，所以也就增加了感知perception的复杂性。

# 6. M1-2: Learn from Industry Experts

# 7. M1-3: Weekly Assignment

