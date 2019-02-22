---
layout: post
title: Coursera-Self-Driving Cars-U1-02-Self-Driving Hardware and Software Architectures(无人车软硬件架构)
date: 2019-02-20 01:02:00
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 0. 小结

![image](https://user-images.githubusercontent.com/18595935/53143891-544eb680-35dd-11e9-8ce8-14ecdab3031c.png)

# 1. M2: 无人车软硬件架构

无人驾驶的系统结构非常的多样化，至今没有出现一个标准的解决方案。本章介绍了通常使用的软硬件结构，以及在成本/可靠性/性能/复杂性之间的一些折衷，这些因素都会影响到无人车的设计。

**学习目标：**
1. Design an omni-directional(全方位) multi-sensor system for an autonomous vehicle
2. Describe the basic architecture of a typical self-driving software system
3. Break down the mapping requirements for self-driving cars based on their intended uses(预期用途).

# 2. M2-1: 无人车软硬件与环境表现

**本章包括：**
1. 感知相关的传感器
2. 无人车的计算相关硬件
3. 无人车的传感器配置
4. 系统结构
5. 环境表现(Environment representation for self-driving)

## 2.1 L1 感知需要的传感器和计算单元

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

## 2.2 L2 硬件配置设计

Let’s learn how to place these sensors to aggregate a complete view of the environment.
1. 在不同场景下的传感器覆盖范围的要求，比如高速场景和市区场景
2. 整体的覆盖范围

|类型|用途|
|:--|:--|
|Camera|Appearance input|
|Stereo Camera|Depth information|
|RADAR|Object detection|
|LIDAR|3D input|
|ULTRASONIC|short-range 3D input|
|GNSS/IMU|ego state estimation|
|WHEEL ODOMETRY|ego state estimation|

在继续讨论之前，先定义一些参数：
1. Aggressive deceleration = `5m/(s**2)`，比较激进的减速度
2. Comfortable deceleration = `2m/(s**2)`,比较温和的减速度
3. Stopping distance = `d = (v**2)/(2*a)`，刹车所需要的距离，a是加速度

另外还有比如系统反应时间，道路的摩擦系数等先暂且不考虑。

### 1. Where to place sensors?

在指定的环境下(ODD)，传感器能够满足所有的场景，比如在下面两种典型的case(高速和市区)：

||高速|市区/居民区|
|:--|:--|:--|
|Traffic Speed|High|Low - Medium|
|Traffic Volume|High|Medium - High|
|lanes|More|2-4 typically|
|Other Features|Fewer, gradual curves; merges |Many turns and intersections|

### 2. Highway Analysis：

概括的说，高速有3种场景：
- 合流
- 车速保持
- 换道

**紧急停止：**

- 驾驶前方有交通堵塞，当前车速为120kmph，制动距离是至少110米，才能以一个激进的减速度停下来。
- 另外，为了避免碰撞，也可以换道的方式，需要旁边至少有一个车道

![image](https://user-images.githubusercontent.com/18595935/53135439-8e5c9000-35be-11e9-90fc-d491b1ef3fce.png)

**车速保持：**

- 按照车速120kmph计算，前方至少保持100米的距离

![image](https://user-images.githubusercontent.com/18595935/53135526-de3b5700-35be-11e9-83bc-cd1c94cd9ca3.png)

**合流：**

- 旁边的lane过来合流，首先要能探测到旁边的lane，需要是160-180°的视角，而且还需要40-60米左右发现车辆。

![image](https://user-images.githubusercontent.com/18595935/53135446-99afbb80-35be-11e9-858b-27a927a71ef7.png)

**换道：**

- 首先从纵向来看，是否与前面的车辆保持了足够的距离，后方的车辆做做什么。
- 观察旁边的车道，是否也有车准备换道。

换道对传感器的要求，与车速维持的类似，都需要知道前后车的状态，以及周边车的状态。

![image](https://user-images.githubusercontent.com/18595935/53135451-9caaac00-35be-11e9-89dd-fb83a6c57d75.png)
![image](https://user-images.githubusercontent.com/18595935/53135492-b8ae4d80-35be-11e9-9165-80e43044436b.png)


### 2. Urban Analysis：

市区的状况，车速慢，车道少，但是要考虑的case更多，主要有如下场景：
1. 紧急停车
2. 车速维持
3. 车道变换
4. 超车
5. 通过交叉口
6. 通过环状路口

前三种与高速类似

**超车：**

- 如果要超一辆停在路边的车，需要能够检测到旁边车线的车辆(探测距离可能较长，要至到换道完毕)

![image](https://user-images.githubusercontent.com/18595935/53135607-3a9e7680-35bf-11e9-9bb8-13ace81b9178.png)

**交叉路口：**

- 在交叉路口，需要一种全方位的传感器，能够检测到各个方向的移动，车辆，行人等。

![image](https://user-images.githubusercontent.com/18595935/53135611-3d996700-35bf-11e9-9bba-15ad5f4fe5f6.png)

**环状交叉路口：**

- 需要一个广角，短距离的传感器。

![image](https://user-images.githubusercontent.com/18595935/53135613-3f632a80-35bf-11e9-87a0-165a536fe101.png)

将上面的高速和市区场景总结如下：

![image](https://user-images.githubusercontent.com/18595935/53139499-2c575700-35cd-11e9-8b85-c7161d8219b8.png)

## 2.3 L3 软件架构

本章描述无人车软件的基本结构，包含5个部分，如下图，环境感知/环境地图构建/运动规划/汽车控制/系统监视。

**整体结构：**

![image](https://user-images.githubusercontent.com/18595935/53140212-5c9ff500-35cf-11e9-8282-d48046c2022e.png)

### 1. 环境感知：

1. 定位自车位置(GPS/IMU/Wheel Odometry)
2. 探测自车周边的重要物体，比如其他的汽车,自行车,行人,静态的信号灯等。
 - 动态物体检测：LIDAR / RADAR / Camera
 - 静态物体检测：HD Road Map

![image](https://user-images.githubusercontent.com/18595935/53140241-6f1a2e80-35cf-11e9-98a1-a3d2f7dec624.png)

### 2. 环境地图：

针对当前汽车所处环境，创建不同类型的各种地图，主要有三种：
1. Occupancy Grid Map
2. Localization Map
3. Detailed Road Map

**Occupancy Grid Map:**当前环境中静止物体地图

![image](https://user-images.githubusercontent.com/18595935/53140344-baccd800-35cf-11e9-984f-cdc3804d853c.png)

**Localization Map：**提供给定位模块，改善自车状态评估
> Sensor data is compared to this map while driving to determine the motion of the car relative to the localization map.

![image](https://user-images.githubusercontent.com/18595935/53140422-f23b8480-35cf-11e9-888f-c0a399a76fa3.png)

**Detailed Road Map：**结合多种信息(高精度地图,检测到的静止物体等)生成的地图。

![image](https://user-images.githubusercontent.com/18595935/53140404-e3ed6880-35cf-11e9-983b-c9beed5fc2e9.png)


**感知和环境地图模块，两者交互频繁，相互改善**，比如感知模块检测静止的物体，提供给环境地图模块生成详细的道路图，然后这个详细道路图，又反过来提供给感知模块，进行更精确的动态物体预测。

### 3. 运动规划：

基于感知的信息，做出该如何驾驶的决策，这个模块的输出是安全有效而且舒适的路径。

这是个非常有挑战性的部分，很难用一个单独的过程来解决，一般把其抽象成下面几个层次去完成：

1. Mission Planner: 处理long-term planning
2. Behavior Planner:  处理short-term planning
3. Local Planner: 处理immediate or reactive planning

最终输出的信息是规划好的路径，包括：
1. desired path
2. velocity profile 

**Mission Planner：**

在起点和终点之间，寻找一条最优路径，然后传递给下一个layer：

![image](https://user-images.githubusercontent.com/18595935/53141966-83612a00-35d5-11e9-9505-5d591070a08a.png)

**Behavior Planner：**

在上面传递过来的路径上，创建一系列安全的动作和策略，比如是否需要合流到旁边车道，或是给出合适的速度：

![image](https://user-images.githubusercontent.com/18595935/53141973-8825de00-35d5-11e9-9361-d5dec23a03ed.png)

上面的放大图如下：
![image](https://user-images.githubusercontent.com/18595935/53142201-5feaaf00-35d6-11e9-81bf-000d92060e92.png)


**Local Planner：**

负责定义具体的路径和速度，必须做到平滑，安全和有效。要达到这个目的，需要综合考虑，车辆的限制信息，其他动态物体，以及上面两层过来的路径信息等。

![image](https://user-images.githubusercontent.com/18595935/53141976-89efa180-35d5-11e9-845e-5c92aa4e3daa.png)


### 4. 汽车控制：

接收上面输出路径，决定该路径上最好的角速度，刹车位置等控制信息。包括：
1. 纵向控制(longitudinal control):Velocity Controller
2. 横向控制(litral control):Steering Controller

![image](https://user-images.githubusercontent.com/18595935/53140530-578f7580-35d0-11e9-8648-15ce11c5d632.png)

### 5. 系统管理：

这个模块常驻监视软件的各个模块，以及硬件的输出，保证系统正常工作，以及如果子系统发生了问题，负责向外报告。

包括两个部分：
1. Hardware Supervisor:监视硬件，比如刹车sensor等，监视硬件的输出数据，数据是否满足当前场景，比如当前相机被包给挡住了，或是下雪阻碍了激光雷达。
2. Software Supervisor:监视软件部分是否正常运行，是否以正确的频率，有否完整的输出。

![image](https://user-images.githubusercontent.com/18595935/53140533-59f1cf80-35d0-11e9-9008-fbfed15eb0d5.png)

## 2.4 L4 环境表现(Environment Representation)

上面的环境地图模块中提到，会创建如下的三种地图：

1. Occupancy Grid Map 占用网格地图:Collision avoidance with static objects.
2. Localization Map 定位地图：Localization of vehicle in the environmen
3. Detailed Road Map 详细道路图:Path planning.

### 1. Localization Map

通过车移动过程中的，一系列连续的激光点云，以及相机的特征点数据而创建，通过与GPS/IMU/Wheel Odometry结合使用，精确估计自车的位置。 

### 2. Occupancy Grid Map 

也是通过连续的激光点云数据，构建静止的物体地图，用于规划安全的路径，告诉系统哪里能走哪里不行。

![image](https://user-images.githubusercontent.com/18595935/53143413-34b68e80-35db-11e9-9c20-817292f15f2e.png)

### 3. Detailed Road Map

包含了所有能行走道路的详细信息，用于道路规划。通过下面三种方式创建：
1. Fully online - 高度依赖感知模块，这种方式很少使用，实时创建地图难度太大
2. Fully offline - 事先制作好地图，也就是高精度地图
3. Created Offline and Updated Online

# 3. M2-2: Learn from Industry Experts

# 4. M2-3: Weekly Assignment