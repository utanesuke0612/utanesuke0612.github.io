---
layout: post
title: Coursera-Self-Driving Cars-U1-04-Vehicle Dynamic Modeling(车辆动态建模)
date: 2019-02-20 01:04:10
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 0. 小结

# 1. Module 4: Vehicle Dynamic Modeling

本章讲述运动学建模(位置和速度)，以及动力学建模(力和力矩)，以及它们是如何关联的。然后再下一章中，我们将广泛使用这些车辆模型进行控制器设计。

1. Basics of kinematic and coordinates 运动学与坐标基础
2. Kinematic model development of a bicycle 自行车运动学模型开发
3. Basics of dynamic modeling 动力学建模基础
4. Vehicle longitudinal dynamics and modeling车辆纵向动力学建模
5. Vehicle lateral dynamics and modeling车辆横向动力学建模
6. Vehicle actuation system汽车驱动系统
7. Tire slips and modeling轮胎滑移及模型


**学习目标：**
1. Develop a kinematic bicycle model of a car with velocity and steering angle inputs - 建立带有速度和转向角输入的运动学自行车模型
2. Develop a dynamic bicycle models of a car with velocity and steering angle inputs - 建立带有速度和转向角输入的动力学自行车模型
3. Differentiate between models of tire forces - 轮胎动力模型的区分
4. Develop a model for actuation in a car, from pedal and steering wheel to tire forces - 开发一个从踏板和方向盘到轮胎力的汽车驱动模型，

# 2. Lesson1：Kinematic Modling in 2D二维运动学模型

本章讲述：
- 2D运动学基础
- 坐标系和变换
- 二轮机器人的连续与离散运动学模型。

一般来说，车辆的运动可以通过两种方式建模：
1. 通过定义其运动的几何约束 - 运动学模型，在加速度不多的低速情况下，运动学模型能很好的捕捉车辆的运动。
2. 通过车辆的力和力矩 - 动力学模型，比运动学模型更复杂

在进入车辆运动建模之前，先复习下坐标系变换(2D变换和3D变换)。

**坐标系(coordinate frames)：**

- inertial coordinate frame 惯性坐标系，有时也称其为 East North Up(ENU)，固定的相对于地球的坐标系
- body frame 体坐标系，依附于车辆自身，原点位于车辆重心，或是旋转中心，比如车的重心点，或是车后轮的中心点(后轮驱动)
- sensor frame 传感器坐标系 这是一种依附于各个传感器的坐标系，根据传感器的输出定义其坐标系原点与位置

下面是三种坐标系示意图：

![image](https://user-images.githubusercontent.com/18595935/53323451-8899de00-3921-11e9-9e71-afc5015958fc.png)

一般来说，车上会有多个坐标系统，但最终都要转换都一个上去，比如将体坐标系转换为惯性坐标系。

![image](https://user-images.githubusercontent.com/18595935/53323617-f8a86400-3921-11e9-991a-180d78cb9606.png)

**举个例子**,速度矩阵的坐标系变换，一般来说运动学变量比如速度，以包含大小和方向的矩阵形式表示。

![image](https://user-images.githubusercontent.com/18595935/53323836-9f8d0000-3922-11e9-9837-b83d009e669a.png)

上图中绿色的表示速度和方向，它有两个坐标系：
1. {b1,b2},体坐标系
2. {e1,e2},惯性坐标系

假设上面两个坐标系有相同的固定原点，但是b的体坐标系基于e惯性坐标系，有一个角度的选择。然后我们可以定义两个旋转矩阵:

![image](https://user-images.githubusercontent.com/18595935/53324025-13c7a380-3923-11e9-8f61-71ab5a5d3fe3.png)

下面是两个坐标的变化，假设其当前位置为P，将两个坐标系互相转换的话，需要这几个变量:
- O(EB)/O(BE)
- C(EB)/C(BE)

![image](https://user-images.githubusercontent.com/18595935/53324274-bb44d600-3923-11e9-8297-d2bb85ee9837.png)

**homogeneous coordinate form 齐次坐标表示：**
> 齐次坐标就是将一个原本是n维的向量用一个n+1维向量来表示，是指一个用于投影几何里的坐标系统，如同用于欧氏几何里的笛卡儿坐标一般。

![image](https://user-images.githubusercontent.com/18595935/53325035-abc68c80-3925-11e9-9286-03cf6bf904f3.png)

## 2.1 2D kinematic Modeling

先看一个概念，非完整性约束(nonholonomic constraint),“非完整”(nonholonomic) 起源于近代分析力学，许多实际控制系统常常要考虑与外部环境的接触因素，这类系统带有一定的约束条件，被称为受限系统。

运动学约束就是非完整的：
1. 速度在一定范围内变化
2. 速度方向切向与当前的移动路径

![image](https://user-images.githubusercontent.com/18595935/53325339-740c1480-3926-11e9-8db4-3894ae64c762.png)

![image](https://user-images.githubusercontent.com/18595935/53386874-7c685c00-39c7-11e9-963d-d33c99e36e01.png)

# 3. Lesson2：The Kinematic Bicycle Model运动学自行车模型

假设:

1. 前轮方向决定车的方向
2. 车在2D方向移动

![image](https://user-images.githubusercontent.com/18595935/53389729-c2c3b800-39d3-11e9-9b04-bd341b0df9f0.png)

![image](https://user-images.githubusercontent.com/18595935/53390467-952c3e00-39d6-11e9-8e21-04d396e272e2.png)

![image](https://user-images.githubusercontent.com/18595935/53390494-aecd8580-39d6-11e9-95bf-384105352073.png)

# 4. Lesson3：Dynamic Modeling in 2D二维动力学建模

上一课中，将了通过自行车模型，以及输入的转向速率和速度，获取车的运动状态。
本节开始考虑车的力和力矩，进入二维动力学建模的范畴，这种模型能更精准的预internal combustion engine测，当然这种更精确是建立在更多复杂计算基础之上，所以不论是自行车模型还是动力学模型，都在自动驾驶中使用。

> Free-body diagrams:自由体受力图,将固体质点及刚体系统受外力及外加力矩作用所产生之运动行为，建构自由体图（ free-body diagrams ），具体描述其物理现象，并应用运动学及动力学求解固体之运动。

**为什么动力学建模很重要：**
1. 前面的自行车建模基于一个前提条件，前轮方向决定车的方向，但是实际行车过程中，特别是高速行车时，会出现打滑的现象，这样将使得前提条件不满足
2. 其他的一些力(摩擦力)的作用
> 没太明白，总之感觉意思就是自行车模型限制条件多，而实际行驶中不可能完美，所以需要一个更复杂的模型-动力学模型
> 

> 力矩：力矩在物理学里是指作用力使物体绕着转动轴或支点转动的趋向。力矩的单位是牛顿-米。力矩 (moment of force) 力对物体产生转动作用的物理量。可以分为力对轴的矩和力对点的矩。即：M=L*F。其中L是从转动轴到着力点的距离矢量, F是矢量力；力矩也是矢量。

**建立典型动力学模型的步骤：**

1. 创建该模型所使用的坐标系，比如体坐标系或惯性坐标系
2. 将这个动力学系统分解成集总动力学元素，这些元素一起构成该系统的各个方面，比如下图中的弹簧减震器等。
3. 为上面动力学元素中的刚体，创建自由体图
4. 最后使用牛顿第二法则，使用数学方程式来定义力学模型

![image](https://user-images.githubusercontent.com/18595935/53397114-99158b80-39e9-11e9-8bbc-d7669620cd1d.png)

**示例(一维平移系统)：**

比如用下面一个简单的示例(一个一维的平移系统)说明上面的步骤：
1. 首先定义该一维平移系统的坐标系，即X
2. 找出这个系统的刚体，这里是M
3. 画出该刚体上，所有的力，这里是f1,f2,f3
4. 最后使用牛顿第二法则，创建方程式

![image](https://user-images.githubusercontent.com/18595935/53397117-9c107c00-39e9-11e9-8bb3-1bcfbc436c0e.png)


**示例(减震器)：**

类似的，可以为减震器(shock absorber)创建动力学模型：
1. 创建坐标系，这里是垂直向下的y方向
2. 识别该系统中的刚体，这里有三个原始，一个mass质量M，一个弹簧K和液压缸
3. 画出上面刚体的受力和力矩
4. 最后使用牛顿第二法则，创建方程式

![image](https://user-images.githubusercontent.com/18595935/53397123-a0d53000-39e9-11e9-8d2e-d7b8720165df.png)

**旋转系统：**

下图是一个旋转系统的组成元素：

![image](https://user-images.githubusercontent.com/18595935/53397130-a894d480-39e9-11e9-91da-eb027d1a5c9d.png)

**轮胎的旋转动力学：**

![image](https://user-images.githubusercontent.com/18595935/53397162-be09fe80-39e9-11e9-929d-fc6613f22994.png)

**纵向的动力学模型：**

![image](https://user-images.githubusercontent.com/18595935/53397173-c5c9a300-39e9-11e9-82a4-affc28f92c23.png)

**横向的动力学模型：**

![image](https://user-images.githubusercontent.com/18595935/53397185-cd894780-39e9-11e9-8be3-9817c8075479.png)

# 5. Lesson4：Longitudinal Vehicle Modeling纵向车辆建模

本节介绍车辆的纵向动力，以及对轮胎产生力矩的动力系统。通过本节了解到：
1. 定义车辆的动态力平衡
2. 描述动力系统组件
3. 将动力系统组件组合，生成完全的纵向运动模型

**纵向车辆模型：**

如下图，红色箭头表示阻力，蓝色箭头表示驱动力，这两种力之间的平衡，决定这车辆的加速度：

![image](https://user-images.githubusercontent.com/18595935/53399674-c8c79200-39ef-11e9-8d8d-ab048106554f.png)

![image](https://user-images.githubusercontent.com/18595935/53399711-d8df7180-39ef-11e9-84ab-13f2db5488a0.png)


**模型中的阻力：**

![image](https://user-images.githubusercontent.com/18595935/53399732-e09f1600-39ef-11e9-955f-554ce8079254.png)

**动力系统模型：**

通过引擎产生力，来扭动轮胎

![image](https://user-images.githubusercontent.com/18595935/53399745-e39a0680-39ef-11e9-846a-e342211b6a41.png)

**动力系统中的动力流：**

![image](https://user-images.githubusercontent.com/18595935/53399781-f01e5f00-39ef-11e9-8815-7af8eec59090.png)

**引擎动力：**

![image](https://user-images.githubusercontent.com/18595935/53399791-f3b1e600-39ef-11e9-880a-ead1a6783707.png)

# 6. Lesson5：Lateral Dynamics of Bicycle Model　自行车模型的横向动力学

有如下假设：
1. 纵向速度不变，这用于分离横向和纵向动力模型，能大大简化建模工作，但是当通过弯道产生加速减速时，会降低精度
2. 左右车轮被合并到一个轮子上，如自行车模型
3. 其他如阻力，道路坡度等因素不予考虑

**横向动力:**
1. 将车的重心点作为参考点

![image](https://user-images.githubusercontent.com/18595935/53401499-4214b400-39f3-11e9-8fc3-2212b87236a2.png)

**轮胎滑移角：**

![image](https://user-images.githubusercontent.com/18595935/53401511-493bc200-39f3-11e9-85e9-5370dfef4e88.png)

**前后轮驱动力：**

![image](https://user-images.githubusercontent.com/18595935/53401524-50fb6680-39f3-11e9-9b6a-bee970511211.png)

**横向动力和偏航动力：**

![image](https://user-images.githubusercontent.com/18595935/53401548-5c4e9200-39f3-11e9-8461-6cbc25326b8c.png)
![image](https://user-images.githubusercontent.com/18595935/53401554-607aaf80-39f3-11e9-9096-622f9cfe509b.png)


# 7. Lesson6：Vehicle Actuation 车辆驱动

# 8. Lesson7：Tire slip and modeling 轮胎滑移建模

# 9. Experts:Challenges for the industry

# 10. Assignment: