---
layout: post
title: Coursera-Self-Driving Cars-U1-00-第一部分 无人车入门
date: 2019-02-20 01:00:00
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 0. 课程概要

本套自动驾驶学习课程，共有4个单元:

1. [**Introduction to Self-Driving Cars**](https://www.coursera.org/learn/intro-self-driving-cars/home/welcome)
2. [State Estimation and Localization for Self-Driving Cars](https://www.coursera.org/learn/state-estimation-localization-self-driving-cars/home/welcome)
3. [Visual Perception for Self-Driving Cars](https://www.coursera.org/learn/visual-perception-self-driving-cars)
4. [Motion Planning for Self-Driving Cars](https://www.coursera.org/learn/motion-planning-self-driving-cars)

通过上面的系列课程，达到如下目的：

1. Introduction to Self-Driving Cars **无人车入门**
	- Design a basic hardware system
	- Identify main components of the autonomous driving software
	- Create a safety assessment strategy for a self-driving car program
2. State Estimation and Localization for Self-Driving Cars **无人车的状态估计和定位**
	- Understand the key methods for parameter and state estimation
	- Develop and use models for typical vehicle localization sensors
	- Apply kalman filters to a vehicle state estimation problem
	- Register point clouds from LIDAR to 3D Maps
3. Visual Perception for Self-Driving Cars **无人车的视觉感知**
	- Project 3D points onto the camera image plane
	- Calibrate the pinhole camera model 校正小孔相机模型
	- Apply feature detection algorithms for localization and mapping 在定位和匹配中应用特征检测
	- Develop an train neural networks for object detection and semantic segmentation 为物体检测和语义分割设计神经网络
4. Motion Planning for Self-Driving Cars **无人车的运动规划**
	- Devise trajectory rollout motion planning
	- Calculate the time to collision 计算冲突事件
	- Define high-level vehicle behaviours
	- Develop kinematically feasible paths through environments
	- Compute velocity profiles
	- Plan behaviours and execute maneuvers to navigate through the world
	- Gain valuable experience in debugging and testing in the Carla simulator

本章，也就是上面第一个部分**Introduction to Self-Driving Cars**，分为如下章节(每周一个章节)：
- Module 0: Welcome to the Self-Driving Cars Specialization!
- Module 1: The Requirements for Autonomy 
- Module 2: Self-Driving Hardware and Software Architectures 无人车的硬件软件架构 
- Module 3: Safety Assurance for Autonomous Vehicles 无人车的安全保障
- Module 4: Vehicle Dynamic Modeling 车辆动态建模
- Module 5: Vehicle Longitudinal Control 车辆纵向控制
- Module 6: Vehicle Lateral Control 车辆横向控制
- Module 7: Putting it all together

# 1. 专业术语

- **ACC: Adaptive Cruise Control(自适应巡航控制)**

A cruise control system for vehicles which controls longitudinal speed(经线速度,纵向速度). ACC can maintain a desired reference speed or adjust its speed accordingly to maintain safe driving distances to other vehicles.

- **Ego**

A term to express the notion of self, which is used to refer to the vehicle being controlled autonomously, as opposed to other vehicles or objects in the scene. It is most often used in the form ego-vehicle, meaning the self-vehicle.

- **FMEA: Failure Mode and Effects Analysis(故障模式与影响分析)**

A bottom up approach of failure analysis which examines individual causes and determines their effects on the higher level system.

- **GNSS: Global Navigation Satellite System(全球导航卫星系统)**

A generic term for all satellite systems which provide position estimation. The Global Positioning System (GPS) made by the United States is a type of GNSS. Another example is the Russian made GLONASS (Globalnaya Navigazionnaya Sputnikovaya Sistema).

- **HAZOP: Hazard and Operability Study(危害和可操作性研究)**

A variation of FMEA (Failure Mode and Effects Analysis) which uses guide words to brainstorm over sets of possible failures that can arise.

- **IMU: Inertial Measurement Unit(惯性测量装置)**

A sensor device consisting of an accelerometer(加速计) and a gyroscope(陀螺仪). The IMU is used to measure vehicle acceleration and angular velocity(测量加速度和角速度), and its data can be fused with other sensors for state estimation.
> 如扩展卡尔曼滤波中，将IMU与GPS的数据融合进行状态估计。

- **LIDAR: Light Detection and Ranging(激光雷达)**

A type of sensor which detects range by transmitting light and measuring return time and shifts of the reflected signal.
> 激光雷达，是以发射激光束探测目标的位置、速度等特征量的雷达系统。其工作原理是向目标发射探测信号(激光束),然后将接收到的从目标反射回来的信号(目标回波)与发射信号进行比较,作适当处理后,就可获得目标的有关信息,如目标距离、方位、高度、速度、姿态、甚至形状等参数,从而对飞机、导弹等目标进行探测、跟踪和识别。

- **LTI: Linear Time Invariant(线性时不变系统)**

A linear system whose dynamics( 动力学，力学) do not change with time. For example, a car using the unicycle model is a LTI system. If the model includes the tires degrading over time (and changing the vehicle dynamics), then the system would no longer be LTI.
> 线性时不变系统是根据系统输入和输出是否具有线性关系来定义的。满足叠加原理的系统具有线性特性。

- **LQR: Linear Quadratic Regulation(线性二次型调节器)**

A method of control utilizing full state feedback. The method seeks to optimize a quadratic cost function dependent on the state and control input.

- **MPC: Model Predictive Control(模型预测控制)**

A method of control whose control input optimizes a user defined cost function over a finite time horizon. A common form of MPC is finite horizon LQR (linear quadratic regulation).

- **NHTSA: National Highway Traffic Safety Administration(国家公路交通安全管理局)**

An agency of the Executive Branch of the U.S. government who has developed a 12-part framework to structure safety assessment for autonomous driving. The framework can be found here. https://www.nhtsa.gov/sites/nhtsa.dot.gov/files/documents/13069a-ads2.0_090617_v9a_tag.pdf

- **ODD: Operational Design Domain(操作设计领域)**

The set of conditions under which a given system is designed to function. For example, a self driving car can have a control system designed for driving in urban environments, and another for driving on the highway.

- **OEDR: Object and Event Detection and Response(对象和事件检测和响应)**

The ability to detect objects and events that immediately affect the driving task, and to react to them appropriately.

- **PID: Proportional Integral Derivative Control(比例积分微分控制)**

A common method of control defined by 3 gains.
 - 1) A proportional(比例的) gain which scales the control output based on the amount of the error
 - 2) An integral(积分的；完整的) gain which scales the control output based on the amount of accumulated(累积的) error
 - 3) A derivative(派生的) gain which scales the control output based on the error rate of change


- **RADAR: Radio Detection And Ranging(雷达,无线电探测)**

A type of sensor which detects range and movement by transmitting radio waves and measuring return time and shifts of the reflected signal.

- **SONAR: Sound Navigation And Ranging(声波定位)**

A type of sensor which detects range and movement by transmitting sound waves and measuring return time and shifts of the reflected signal.

