---
layout: post
title: Coursera-Self-Driving Cars-U1-02-Self-Driving Hardware and Software Architectures
date: 2019-02-20 01:02:00
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 0. 小结

# 1. Module 2: Self-Driving Hardware and Software Architectures

无人驾驶的系统结构非常的多样化，至今没有出现一个标准的解决方案。本章介绍了通常使用的软硬件结构，以及在成本/可靠性/性能/复杂性之间的一些折衷，这些因素都会影响到无人车的设计。

**学习目标：**
1. Design an omni-directional(全方位) multi-sensor system for an autonomous vehicle
2. Describe the basic architecture of a typical self-driving software system
3. Break down the mapping requirements for self-driving cars based on their intended uses(预期用途).

# 2. Module 2-1: Autonomous Vehicle Hardware, Software and Environment Representation

**本章包括：**
1. 感知相关的传感器
2. 无人车的计算相关硬件
3. 无人车的传感器配置
4. 系统结构
5. 环境表现(Environment representation for self-driving)

## 2.1 Lesson1 感知需要的传感器和计算单元

**本节包括：**
1. 传感器型号和特性
2. 无人车计算单元

**传感器：**用于测量和检测周边环境，根据传感器记录的属性，可以分为：
1. exteroceptive: extero = surroundings 外部传感器
2. proprioceptive: proprio = internal 内部传感器，记录自身信息

### 1. 感知所需的传感器：

![image](https://user-images.githubusercontent.com/18595935/53095722-e2d12280-3560-11e9-90eb-101d77baa9fe.png)

![image](https://user-images.githubusercontent.com/18595935/53095888-39d6f780-3561-11e9-99ba-49814b457ef5.png)

 **1. 相机**，主要的参考参数有：
  1. Resolution 解像度
  2. Field of view 视角
  3. Dynamic range 动态范围(the difference between the darkest and the lightest tones in an image)
  > The field of view is defined by the horizontal and vertical angular extent that is visible to the camera.相机所能捕捉到的水平和垂直角的范围，通过lens和zoom能改变其视角。
  > High dynamic range is critical for self-driving car due to the highly variable lighting conditions encountered while driving especially at night.

  另外，将两台相机一起组合起来，形成立体照相机(stereo camera)，两张图片叠加起来，可以估算像素的深度信息。

 **2. LADAR 激光雷达**，是一种光学遥感技术，它通过向目标照射一束光，通常是一束脉冲激光来测量目标的距离等参数。其所测得的数据为数字表面模型(Digital Surface Model, DSM)的离散点表示，数据中含有空间三维信息和激光强度信息。
 
 因为它自身向外发射激光，LIDAR不会被外界光线所影响，白天黑夜都OK。

 主要的参考参数有：
  1. Number of beams 光线束，8线，16线，32线，64线等
  2. Points per second 越高，收集到的3D点云数据越详细
  3. Rotation rate 转速越高，3D点云数据更新的越快
  4. Field of view - the angular extent visible to the LIDAR sensor
  
 现在也出现了一种新的激光雷达，低成本而且也可靠：**High-resolution,solid-state LIDAR**, 与典型的激光雷达相比，没有那个可以转动的部件。

 **3. RADAR 雷达**，which stands for radio detection and ranging, 其探测范围比LIDAR要远，能稳定的探测大的物体，尤其在不好的天气情况下发挥作用，它不受降水之类的影响。
 主要的参考参数有：
  1. range
  2. position and speed accuracy
  3. Field of view
 
 有两种配置的：
  1. WFOV，short range：wide angular field of view 广角，但是距离短
  2. NFOV，long range：narrow angular field of view 窄角，但是长距离

 **4. Ultrasonics 超声波**，短距离声波，价格便宜，适用于停车等近距离使用。与LIDAR和RADAR相同，不受光线和降水的影响主要的参考参数有：
  1. range
  2. Cost
  3. Field of view

 **5. GNSS/IMU 全球定位系统和陀螺仪**，是一种内部传感器
  1. GNSS(GPS..):测量自身位置信息和速度，其精度受其使用的方式影响(RTK/PPP/DGPS)等。
  2. IMU(陀螺仪): 测量角速度和加速度
  3. 结合GPS和IMU，可以计算其朝向(heading)

 **6. Wheel Odometry 轮测程法**，也是一种内部传感器，根据轮胎转速估算车的速度，以及转向角速度，里程计就是用这种传感器车辆的

### 2. 计算单元

被称作无人车的大脑，接收所有的传感器数据，执行计算操作，现在通用的有：
1. NVIDIA的Drive PX/AGX
2. Mobileye的EyeQ

无人车的计算中枢，需要有线性和并行计算单元，特别是用于`image processing`,`object detection`,`Mapping`。
1. GPUs - Graphic Processing Unit 图形处理器
2. FPGAs - Field Programmable Gate Array 现场可编程门阵列
3. ASICs - Application Specfic Integrated Chip 应用专用集成芯片

最后是硬件的同步性，因为我们在做决策的时候要保证所有信息都是同一时间的，在系统中保持各个模块的同时性就非常必要，使用共同的时钟。

GPS上有着非常精确的时钟，其他模块可以将其作为参照。

## 2.2 Lesson2 Hardware Configuration Design 硬件配置设计

Let’s learn how to place these sensors to aggregate a complete view of the environment.
1. 在不同场景下的传感器覆盖范围的要求，比如高速场景和市区场景
2. 整体的覆盖范围

|类型|用途|
|:--|:--|:--|
|Camera|Appearance input|
|Stereo Camera|Depth information|
|RADAR|Object detection|
|LIDAR|3D input|
|ULTRASONIC|short-range 3D input|
|GNSS/IMU|ego state estimation|
|WHEEL ODOMETRY|ego state estimation|

在继续讨论之前，先定义一些参数：
1. Aggressive deceleration = `5m/s**2`，比较激进的减速度
2. Comfortable deceleration = `2m/s**2`,比较温和的减速度
3. Stopping distance = `d = v**2/2*a`，刹车所需要的距离

另外还有比如系统反应时间，道路的摩擦系数等先暂且不考虑。





## 2.3 Lesson3

## 2.4 Lesson4

# 3. Module 2-2: Learn from Industry Experts

# 4. Module 2-3: Weekly Assignment