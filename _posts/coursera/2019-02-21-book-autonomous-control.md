---
layout: post
title: 【书】-无人驾驶汽车运动控制
date: 2019-02-20 01:04:00
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

Coursera上的课程，在进行到车辆动态建模的时候，开始懵逼了，参考下面两本书总结本篇之后再开始学习。

- [无人驾驶汽车系统入门(申泽邦-已出书 无人驾驶原理与实践)](https://blog.csdn.net/AdamShan/column/info/28410)
- [第一本无人驾驶技术书(刘少山等著)](https://item.jd.com/12184804.html)
- [无人驾驶汽车概论(陈慧岩)](https://item.jd.com/11526889.html)

# 0. 小结

# 1. 规划与控制简介

无人车作为一个复杂的软硬件结合系统，需要依靠车载硬件，传感器，感知/预测/控制等多个模块的协同工作，其中感知预测与控制规划的紧密配合尤为重要。
控制规划广义上分为：
1. 路由寻径
2. 行为决策
3. 动作规划
4. 反馈控制

下面是无人车系统控制规划示意图：

![image](https://user-images.githubusercontent.com/18595935/53224644-d52eb080-36b8-11e9-9b88-45e8d40ecfc4.png)

## 1.1 规划1-路由寻径

> 参考[运动规划](http://road2ai.info/2019/02/20/coursera-SelfDrivingCar_u1-02/#3-%E8%BF%90%E5%8A%A8%E8%A7%84%E5%88%92)-Mission Planner

宏观上控制无人车软件系统的控制规划模块按照什么样的道路行驶，从而实现起点到目的地的路径规划，类似于传统导航，但其细节上紧密依赖高精度地图。

传统导航或google/baidu地图等的道路层面的路由寻径，其结果是表示给人看的，传统导航能够具体到某一条路的某一个车道，但这些道路和车道都是符合自然的道路划分和标识。

而无人车路径规划的路由寻径问题，虽然也是解决相同的问题，但是输出结果并不是给驾驶员看的，而是给下游的决策模块作为输入，要更加深入到代表高精度地图级别的道路划分和方向，如下图：

![image](https://user-images.githubusercontent.com/18595935/53225628-08267380-36bc-11e9-8d5f-d2c810e3aff5.png)

常见的最短路径问题算法，与传统导航的类似，Dijkstra算法和A*算法，但是算法实现时考虑的因素更多，不仅局限于路径的长短和拥堵情况，还要考虑到无人车执行驾驶的难以程度，比如尽量避免切换车道等。

详细的路由寻径，后续章节再介绍。


## 1.2 规划2-行为决策

> 参考[运动规划](http://road2ai.info/2019/02/20/coursera-SelfDrivingCar_u1-02/#3-%E8%BF%90%E5%8A%A8%E8%A7%84%E5%88%92)-Behavior Planner

路径规划的下面是行为决策，行为决策模块可以理解成无人车的副驾驶，接收上层的路径结果，同时接收感知预测和地图信息，综合这些信息，宏观上决定无人车该如何行驶。

**输入信息：**
1. 上层的路由寻径结果
2. 无人车的当前自身状态：车位置/速度/朝向/所处车道等
3. 无人车的历史信息：上一个决策是什么？跟车/停车/换道...
4. 周边障碍信息,交通标识信息
5. 当地交通规则

根据上面信息，综合计算后，输出下面的信息：

**输出信息：**
1. 行驶(车速)
2. 跟车(跟车对象,跟车距离,目的车速)
3. 转弯(当前车道,目的车道,转弯属性,转弯速度)
4. 换道(当前车道,目的车道,加速/减速)
5. 停车(停车位置)

## 1.3 规划3-动作规划

> 参考[运动规划](http://road2ai.info/2019/02/20/coursera-SelfDrivingCar_u1-02/#3-%E8%BF%90%E5%8A%A8%E8%A7%84%E5%88%92)-Local Planner

上层抽象的行为决策，在动作规划时要计算出具体车道，所需要的车速和朝向等信息。这两个模块尤其要紧密配合，设计时基本准则是，**行为决策模块的输出逻辑需要和下游的动作规划模块配合一致。**

动作规划需要具体把一个短暂时间t内从A到B的路径点做出规划，包括：
1. 途径的具体路径点
2. 到达各个路径点时无人车要到达的速度、朝向、加速度、车轮转向

不仅如此，动作规划为了达到舒适性/安全性/高效性，还要保证：
1. 后续时间内，生成从A到B的路径要保持一定的一致性
2. A到B之间路径点的速度/朝向等，反馈给下游车辆控制时，是属于车辆和道路物理属性范围内，是可以实际操作的


## 1.4 反馈控制

反馈控制模块位于最下层，是一个直接与无人车底层控制接口CAN-BUS对接的模块，其核心任务是消化上层动作规划模块的输出轨迹点，通过一系列结合车身属性和外界物理因素的动力学计算，转换成：
1. 车辆Drive-By-Wire控制的油门
2. 刹车
3. 方向盘信号
从而尽可能控制车去实际执行这些轨迹点，反馈控制模块主要涉及对车辆自身控制，以及和外界物理环境交互的建模。

单独从车辆的姿态控制角度看，无人车反馈控制部分和普通车辆反馈控制并无本质不同，都是基于一定的预设轨迹，考虑当前车辆姿态和此预设轨迹的误差并进行不断的跟踪反馈控制。

**因为本章主题是控制，下面会详细进行介绍，另外三个规划的课题，在其他的文章中讲述。**

# 2. 基于PID的反馈控制系统

## 2.1 为什么需要控制理论

想象一下自己开车的时候，有下面一个弯道，是不是一点点打方向盘，确认位置，打多了后就反向回一下，逐步调整方向盘角度和油门踏板的力度，这种基于环境反馈的控制，我们成为**反馈控制**。

![image](https://user-images.githubusercontent.com/18595935/53228886-fb0e8200-36c5-11e9-9ad3-76b2bd46a896.png)

**反馈控制的定义：**

反馈控制是指在某一行动和任务完成之后，将实际结果进行比较，从而对下一步行动的进行产生影响，起到控制的作用。
其特点是：对计划决策在实施过程中的每一步骤所引起的客观效果，能够及时做出反应，并据此调整、修改下一步的实施方案，使计划决策的实施与原计划本身在动态中达到协调。

我们希望控制对象-无人车能够按照规划好的路径行驶：
1. 将环境当前给我们的反馈(当前位置)和参考线进行比较，得到偏离参考线的距离(误差)
2. 基于这个误差，设计一定算法产生输出信号，使得这个误差不断变小

这个过程就是**反馈控制**的一般过程。

![image](https://user-images.githubusercontent.com/18595935/53229860-b33d2a00-36c8-11e9-9ef2-bc10f95fb2d2.png)

误差为0意味着车一直在你规划的路径上行驶，如何减少误差就是需要解决的课题。

## 2.2  比例/积分/导数

PID就是指 **比例（proportion）**、**积分（integral）**、**导数（derivative）**，这三项表示我们如何使用我们的误差来产生控制指令，整个流程如下：

![image](https://user-images.githubusercontent.com/18595935/53229971-eed7f400-36c8-11e9-94d1-bf6ee7b1e73b.png)

1. 首先根据反馈和参考值求出**误差值**，这里的误差值根据具体的情况可以是各种度量，比如说控制车辆按照指定路径行驶，那么就是**车辆当前位置和参考线的距离**，控制车辆速度在设定的值，就是**当前速度和设定速度的差值**。
2. 求出误差以后，再根据误差求比例，积分和微分三项，其中K表示搁置的系数，决定这三项对最后输出影响的比重。
3. 最后，将P/I/D三项求和作为最后的输出信号。

## 2.3 P(比例)控制

P：比例单元—对方向盘应用与误差成比例的校正。如果我们离目标太远，我们会转向另一个方向。

P即使用比例控制，如下图所示，当偏差大的时候，我们偏转更多的角度，偏差小的时候，偏转小一点。

![image](https://user-images.githubusercontent.com/18595935/53231636-bafecd80-36cc-11e9-8a6c-9b9f41ddc760.png)

最后的实际路径如下图：

![image](https://user-images.githubusercontent.com/18595935/53231232-c7365b00-36cb-11e9-85b1-b469ad318d57.png)

上面就是P control(比例控制)，这里我们使用CTE(Cross Track Error)作为偏差度量，CTE就是我们到参考线的距离，那么这时转角就变成了：

```
steering angel = Kp * e(t)
```

其中e(t)就是t时刻的CTE，在P控制中系数Kp会直接影响到实际的控制效果，在合理的数值范围内Kp越大效果越好，因为能快速的回到参考线附近，但是当本身位置和参考线相距较远，且Kp系数很大的时候，就会出现车辆失去控制的情况(计算出的转向角过大)。

**下面就是失去控制的图示：**

![image](https://user-images.githubusercontent.com/18595935/53232101-b71f7b00-36cd-11e9-9de9-94239eb3b8e4.png)

所以说，如果Kp参数设计合理的话，P控制要比固定控制要好，但是还是不能很好的控制，因为P控制的车辆容易0值的影响，如图所示：

![image](https://user-images.githubusercontent.com/18595935/53232189-ed5cfa80-36cd-11e9-8e04-7c6ee2279ca2.png)

此时车辆虽然在参考线上，但是并不是我们希望的状态(下一刻就会偏离)，但是对于P控制而言，这是理想状态，此时控制转角为0，因此，P控制会一次又一次的超过参考线(overshot)，为了矫正这种overshot，我们需要考虑一个额外的误差项-**CTE变化率**。


## 2.4 PD控制

CTE的变化率描述了我们无人车向着参考线方向移动的有多快，如果我们的无人车一直都完美的贴合参考路径，那么CTE的变化率就是0，那么这一项(误差变化率)就可以用导数来表示，那么现在控制输出就变成了**比例项**和**导数项**求和的形式：

```
steering angel = Kp * e(t) + Kd * (de(t)/ dt)
```
Kd是导数项的系数，作用于Kp一样，控制该项目对于反馈控制的影响。

1. 增大Kp系数，将会增大无人车向着参考线的倾向
2. 增大Kd系数，将会增大无人车快速向参考线运动的**抵抗力**，从而使得向参考线方向的运动变得平滑

合适的选择Kp和Kd系数，可以使无人车快速回到参考路径，同时很好维持在路径上行驶。

1. 使用过大的Kp系数，过小Kd系数，我们称之为`欠阻尼(underdamped)`,这种情况的无人车将沿着参考线震荡前进
2. 反之，Kp过小，Kd过大，称之为`过阻尼(overdamped)`,这将使得无人车要较长时间才能纠正错误差。

PD控制似乎能良好胜任反馈控制了，但还是不够，PD控制器可以保证正常控制的需求，但是当环境存在扰动时：

![image](https://user-images.githubusercontent.com/18595935/53235493-4714f300-36d5-11e9-83fc-0a98ab450b17.png)

车在受力发生微小偏移后，由于PD控制下P倾向于向参考线运动，而D则尝试低效这种倾向，造成无人车始终无法沿着参考线运动。

这个问题叫做**steady state error**为了解决这个问题，我们再引入一项—— **积分项**。

## 2.5 PID控制

与上面类似，将积分项也加入控制输出函数，这时，无人车的转角就可以表示为：

![image](https://user-images.githubusercontent.com/18595935/53235634-aa9f2080-36d5-11e9-99b7-40bbac06f965.png)

- Ki是系数，与上面一样
- 积分项，本质就是车实际路线到参考线图形的面积，加入积分项之后，控制函数会尽可能使车辆路线积分变小(即参考路径与行驶路径之间的面积)，那么也就避免了steady state这种情况。

同样，这里的Ki积分项系数大小也会影响整个控制系统的稳定性：
- 过大的Ki会使控制系统`震荡`运行
- 过小的 Ki 又会使控制的车辆在遇到扰动以后（处于steady state）要很久才能回到参考线上，这在某些情况下势必会使车辆处于一个危险的境况。

PID控制就是由这三项共同决定的，还有其他应用于无人驾驶汽车的高级控制算法，但是他们都和PID控制的原理相似。

## 2.6 如何寻找PID的系数

我们发现其实PID实现确实不难，但是三个系数的选择却很难，那么如何选择PID系数呢？我们可以在我们的控制循环中通过一定的算法不断尝试，下面是一种寻找参数的算法：

![image](https://user-images.githubusercontent.com/18595935/53236710-4af64480-36d8-11e9-928a-9de4dac36cc8.png)

代码实现如下：

**pid.cpp：**

```c
#include <limits>
#include <iostream>
#include "PID.h"

//using namespace std;

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp, double Ki, double Kd) {
    parameter.push_back(Kp);
    parameter.push_back(Ki);
    parameter.push_back(Kd);

    this->p_error = 99999999.;
    this->d_error = 0.0;
    this->i_error = 0.0;

    //twiddle parameters
    need_twiddle = false;

    step = 1;
    // let the car run at first 100 steps, then in the next 3000 steps add the cte^2 to the total_error
    val_step = 100;
    test_step = 2000;

    for (int i = 0; i < 3; ++i) {
        // init the change rate with the value of 0.1*parameter
        changes.push_back(0.1 * parameter[i]);
    }
    index_param = 0;

    best_error = std::numeric_limits<double>::max();
    total_error = 0;
    // fail to make the total_error better times
    fail_counter = 0;
}

void PID::UpdateError(double cte) {
    if(step == 1){
        p_error = cte;

    }
    d_error = cte - p_error;
    p_error = cte;
    i_error += cte;

    if(need_twiddle){
        if(step % (val_step + test_step) > val_step){
            total_error += (cte * cte);
        }

        if(step % (val_step + test_step) == 0){
            std::cout<<"==============  step "<<step<<" =============="<<std::endl;
            std::cout << "P: "<< parameter[0]<<" I: "<<parameter[1]<<" D: "<<parameter[2]<<std::endl;
            if (step == (val_step + test_step)){
                if(total_error < best_error){
                    best_error = total_error;

                }
                parameter[index_param] += changes[index_param];
            } else{
                if(total_error < best_error){
                    best_error = total_error;
                    changes[index_param] *= 1.1;
                    IndexMove();
                    parameter[index_param] += changes[index_param];
                    fail_counter = 0;
                } else if(fail_counter == 0){
                    parameter[index_param] -= (2*changes[index_param]);
                    fail_counter++;
                } else{
                    parameter[index_param] += changes[index_param];
                    changes[index_param] *= 0.9;
                    IndexMove();
                    parameter[index_param] += changes[index_param];
                    fail_counter = 0;
                }
            }

            std::cout << "best_error: "<< best_error<<" total_error: "<<total_error<<std::endl;
            std::cout << "change_index: "<<index_param<<" new_parameter: "<<parameter[index_param]<<std::endl;
            std::cout <<  std::endl;
            total_error = 0;
        }
    }
    step++;
}

double PID::TotalError() {
    return -parameter[0] * p_error - parameter[1] * i_error - parameter[2] * d_error;
}

void PID::IndexMove() {
    index_param++;
    if(index_param >=3){
        index_param = 0;
    }
}
```

**pid.h：**

```c
#ifndef PID_H
#define PID_H

#include <cmath>
#include <vector>

class PID {
private:
    int step;
    std::vector<double> changes;
    double best_error;
    double total_error;
    int index_param;

    int val_step;
    int test_step;

    int fail_counter;

    void IndexMove();

    bool need_twiddle;

public:
    /*
    * Errors
    */
    double p_error;
    double i_error;
    double d_error;

    /*
    * Coefficients, the order is P, I, D
    */
    std::vector<double> parameter;

    /*
    * Constructor
    */
    PID();

    /*
    * Destructor.
    */
    virtual ~PID();

    /*
    * Initialize PID.
    */
    void Init(double Kp, double Ki, double Kd);

    /*
    * Update the PID error variables given cross track error.
    */
    void UpdateError(double cte);

    /*
    * Calculate the total PID error.
    */
    double TotalError();
};

#endif /* PID_H */
```

**用法：**，在实际控制循环中，调用：

```c
PID pid;
pid.Init(0.3345, 0.0011011, 2.662); //your init parameters

for (in your control loop) {
  pid.UpdateError(cte);
  steer_value = pid.TotalError();
}
```

# 3. 车辆模型

了解了上面的PID控制后，我们需要接触一些现代的控制算法，在了解高级的车辆控制算法之前，掌握车辆运动模型是非常有必要的。

**车辆运动模型**就是一类能够描述我们车辆的运动规律的模型，下面先了解下两个广泛使用的车辆模型：

1. 运动学自行车模型（Kinematic Bicycle Model）
2. 动力学自行车模型（Dynamic Bicycle Model）

无人驾驶系统分为三个大的模块，**感知**，**决策**，**控制**，其中无人车的路径规划和底层控制是在不同层工作的：

1. 路径规划，往往会基于更加高层(感知,定位)的信息，和底层(控制层)的实时信息，计算出行驶路径，最终输出车辆的**参考路径**给控制层
2. 控制系统需要做的就是严格按照这个**参考路径(速度/转向角控制量)**去驾驶车辆

一般来说，我们会用多项式的行驶来描述这个曲线：

![image](https://user-images.githubusercontent.com/18595935/53237976-70d11880-36db-11e9-8324-352b2a57d704.png)

无人车的控制依赖于一项称为**模型预测控制(Model Predictive Control)**的技术。这种控制的方法是产生一系列可行(车辆能执行)的控制输入，基于一定的算法(带约束的非线性优化算法)来调整这一系列的控制输入，使得**损失函数(cost function)**最小化，这个损失函数的求解就要依赖于车辆运动学或者动力学模型的输出和参考路径的差值求得。

# 3. 运动学自行车模型-Kinematic Bicycle Model

## 3.1 自行车模型

首先我们要简化汽车运动，其中自行车模型就是简单有效的简化方式，自行车模型基于下面几个驾驶：
1. 车辆在垂直方向运动被忽略，驾驶车辆是在一个二维平面运动
2. 驾驶车辆结构与自行车一样，也就是说假设车辆的前面两个轮胎有一样的角度和转速，后面也一样，前后的两个轮胎，可以用一个轮胎描述
3. 假设车辆运动与自行车一样，前面轮胎控制车辆转动

如下图，θ是其在Y方向的偏转角度，v是θ方向的速度，L是车辆的轴距(前后轮胎距离)：

![image](https://user-images.githubusercontent.com/18595935/53294667-56f41a80-382e-11e9-8f2b-91829cd706ed.png)

## 3.2 运动学自行车模型




# 4. 动力学自行车模型-Dynamic Bicycle Model