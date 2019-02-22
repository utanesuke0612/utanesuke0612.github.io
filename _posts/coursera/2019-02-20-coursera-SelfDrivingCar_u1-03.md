---
layout: post
title: Coursera-Self-Driving Cars-U1-03-Safety Assurance for Autonomous Vehicles(无人车安全保证)
date: 2019-02-20 01:03:00
categories: self-driving(自動運転)
tags: self-driving Coursera
---
* content
{:toc}

# 0. 小结

本章主要介绍无人车的安全课题，主要是一些理论知识，在udacity上有更详细的讲解，参考如下：

- [Nano01(自動運転)-Extend-Additional Content-L07-Introduction to Functional Safety](http://road2ai.info/2019/02/14/Nano_Extend_01_07/)
- [Nano01(自動運転)-Extend-Additional Content-L08-Functional Safety:safety plan](http://road2ai.info/2019/02/14/Nano_Extend_01_08/)
- [Nano01(自動運転)-Extend-Additional Content-L09-Functional Safety:Hazard Analysis and Risk Assessment](http://road2ai.info/2019/02/14/Nano_Extend_01_09/)
- [Nano01(自動運転)-Extend-Additional Content-L10-Functional Safety:Functional Safety Concept](http://road2ai.info/2019/02/14/Nano_Extend_01_10/)
- [Nano01(自動運転)-Extend-Additional Content-L11-Functional Safety:Technical Safety Concept](http://road2ai.info/2019/02/14/Nano_Extend_01_11/)
- [Nano01(自動運転)-Extend-Additional Content-L12-Functional Safety at the software and Hardware Levels](http://road2ai.info/2019/02/14/Nano_Extend_01_12/)

![image](https://user-images.githubusercontent.com/18595935/53161335-297c5680-360d-11e9-9a53-4d08359ad592.png)

# 1. M3: 无人车安全保证

随着自动驾驶技术的不断成熟，公道上的驾驶安全性显得更加重要。在不可控的公共道路环境下，保证无人车的安全驾驶，这是一个需要解决的巨大挑战。
> 翻译得比较糊弄，原句： You will evaluate the challenges and approaches employed to date to tackle the immense challenge of assuring the safe operation of autonomous vehicles in an uncontrolled public road driving environment.

**学习目标：**
1. Assess the primary contributions to the overall safety system for self-driving cars
2. Investigate the main causes of prominent(卓越的) autonomous driving failures recorded to date
3. Employ safety assessment methods for analysis of specific scenarios and hazards(危害) for self-driving
4. Describe analytical(解析的) and empirical(经验主义的) approaches to safety assessment.


# 2. M3-1: 无人车安全

本章中：
1. Autonomous vehicle crash reports
2. Safety concepts
3. Hazard sources(风险来源)
4. Industry perspectives on safety
5. Safety frameworks for self driving

## 2.1 L1:无人车安全保证

本节讲述:
1. Autonomous driving crashes
2. Formal definitions
3. Major hazard sources
4. Safety requirements

### 1. 无人车碰撞事故

最有名的就是去年uber无人驾驶车致死事件，后来经调查有多重原因：
1. 当时安全员没有监视系统，在看hulu视频
2. 识别系统出错，最初识别为车，然后识别为自行车，最后识别结论是无视
3. 在1.3秒前车本身的识别系统识别了，但是这个无人车禁用了该功能

![image](https://user-images.githubusercontent.com/18595935/53150913-1a89aa00-35f5-11e9-8e03-ea7852bb4761.png)

每一个环节出错都有可能出现致命的错误。

### 2. 安全相关术语

![image](https://user-images.githubusercontent.com/18595935/53149362-dd231d80-35f0-11e9-987f-d3d28af73693.png)

Safety is the process of avoiding **UNREASONABLE RISK** of harm to a living thing. For example, driving into an intersection when the traffic signal is red would be unsafe, as it leads to unreasonable risk of harm to the occupants of the vehicle and the other vehicles moving through the intersection.

### 3. 主要危险来源

![image](https://user-images.githubusercontent.com/18595935/53149453-0fcd1600-35f1-11e9-89ff-da5520a0cf74.png)

1. 机械上的问题，比如刹车系统没有正确的组装，可能导致不成熟的错误。
2. 电气相关，比如内部线路问题导致没有点灯。
3. 硬件相关，如计算用CPU芯片等。 
4. 软件错误
5. 传感器
6. 驾驶员
7. 黑客 cybersecurity

### 4. NHTSA: Safety Framework

分成下面三个大的方面：

![image](https://user-images.githubusercontent.com/18595935/53151332-48bbb980-35f6-11e9-9166-1526fa58fb56.png)

**Autonomy Design：**

![image](https://user-images.githubusercontent.com/18595935/53151401-7bfe4880-35f6-11e9-9b88-e28d5782ae50.png)

1. ODD,一个定义好的ODD，可以让设计者了解系统的边界，在测试或部署的时候可以知道哪些case是安全的。
2. HMI：清晰明了，能较好传递信息的用户界面
3. Fallback：将错误减少到最小。

**Testing & Crash Mitigation(缓和):**
1. Testing，包括3部分：simulation,close track testing, public road driving
2. Crashworthiness，防撞性能
3. Post crash, 发生事故后，不能将故障扩大，比如关于...避免火灾
4. Data recording,黑匣子
5. Consumer ED，用户培训，让用户了解系统功能以及限制

![image](https://user-images.githubusercontent.com/18595935/53151420-8587b080-35f6-11e9-95a9-7e60813cff96.png)

> **这一节有很好的附加材料，需要学习**

## 2.2 L2:无人车安全与驾驶(工业解决方案)

### 1. Waymo

**Waymo: Safety Levels:**
1. Behavioral Safety,准守交通规则，满足ODD下的各种场景
2. Functional Safety,系统冗余与备份，即使发生错误，也能切换到另一种方案，尽量减少严重程度，使车回归安全状态
3. Crash Safety，即使发生事故，也要使乘客的危害减少
4. Operational Safety，用户界面要是易用方便，直觉的
5. Non collision safety，从系统设计上，减少可能与系统有交互人员的伤害，比如第一目击者,机械工,硬件工程师等。

![image](https://user-images.githubusercontent.com/18595935/53153673-38a6d880-35fc-11e9-9c8b-9a83a46d4057.png)

**Waymo: Safety Processes:**
1. 识别危险情况/潜在的缓解措施
2. 使用危险评估方式去定义安全需求
3. 投入大量的测试确保达到安全要求

![image](https://user-images.githubusercontent.com/18595935/53153691-43fa0400-35fc-11e9-9890-e07d1402f419.png)

**Waymo: Levels of testing to ensure safety:**

- 生成大量随机的测试case，在模拟器上测试

![image](https://user-images.githubusercontent.com/18595935/53153714-52e0b680-35fc-11e9-9ec1-81f57949250b.png)

- 在封闭道路上测试

![image](https://user-images.githubusercontent.com/18595935/53153730-5ecc7880-35fc-11e9-8ace-3de4ce76dfb8.png)

- 实际的道路测试

![image](https://user-images.githubusercontent.com/18595935/53153738-6724b380-35fc-11e9-9d46-0845edcad925.png)


### 2. GM safety Perspective

采用迭代式的设计：
1. Analyze
2. Build
3. Simulate
4. Drive

![image](https://user-images.githubusercontent.com/18595935/53155030-81ac5c00-35ff-11e9-83c2-94883772c332.png)

**GM: Safety Processes**
- Deductive Analysis 演绎分析
	+ fault tree analysis 故障树型分析
- Inductive Analysis 归纳分析
	+ Design&Process FMEA
- Exploratory Analysis 探索性分析
	+ HAZOP:Hazard & Operability Study

**GM: Safety Thresholds**

All GM vehicles are equipped with two key safety thresholds:
- **Fail safes** - There is redundant functionality (second controllers, backup systems etc) such that even if primary systems fail, the vehicle can stop normally
- **SOTIF** - All critical functionalities are evaluated for
unpredictable scenarios

**GM: Testing**

- **Performance testing 性能测试** at different levels
- **Requirements validation 需求验证** of components, levels
- **Fault injection testing 故障注入测试** of safety critical functionality
- **Intrusive testing 侵入性测试** such as electromagnetic interference,
etc.
- **Durability testing 耐久性测试** and simulation based testing

### 3. Analytical vs Data Driven: Definitions

- **Analytical Safety**
Ensuring the system works in theory and meets safety requirements found by hazard assessment(灾害评估)
从理论上保证系统运行，而且通过灾害评估满足了安全要求

- **Data driven safety**
Safety guarantee due to the fact that the system has performed autonomously without fail on the roads for a very large number of kms. 通过大量的实际路测保证系统安全


## 2.3 L3:无人驾驶的安全框架

本节讨论：
1. 通用安全框架(Fault Trees,FMEA,HAZOP)
2. 功能性安全框架(FuSa HARA,SOTIF)

![image](https://user-images.githubusercontent.com/18595935/53159783-e4a2f080-3609-11e9-85cf-e2576d0efad9.png)

### 1. Generic Safety Frameworks 

**Fault Tree Analysis 故障树分析：**

这个方法广泛应用在核项目和航空项目中，难点在于建立叶子和叶子上的概率。

- 自顶向下的演绎错误分析法
- bool逻辑判断

比如下面的这个例子，发生了车的碰撞，用下面的分解树进行分析

![image](https://user-images.githubusercontent.com/18595935/53157672-59bff700-3605-11e9-81bb-570b530c3741.png)

给每一个可能错误的叶子上赋予概率，通过逻辑门演示错误树：

![image](https://user-images.githubusercontent.com/18595935/53157676-5b89ba80-3605-11e9-8f5b-94d43d2e5d1f.png)

**FMEA：**，Failure Mode and Effects Analyses
自底向上的识别，系统中错误可能导致的所有影响，与上面的故障树分析法正好相反，两者经常结合使用。

FMEA的目标是，通过优先级给错误模式分类，所以在分析的时候，进行下面的提问：
1. 这个影响有多严重？
2. 多大的频率会发生？
3. 方便检测否？

FMEA步骤如下：

![image](https://user-images.githubusercontent.com/18595935/53158070-2467d900-3606-11e9-840e-29114f23a200.png)


**HAZOP：**，a variation on FMEA，一种简化版的FMEA头脑风暴方法。
- Hazard and operability study (HAZOP)
- Qualitative brainstorming process, needs “imagination”
- Uses guide words to trigger brainstorming (not, more, less etc.)
- Applied to complex 'processes'
 - Sufficient design information is available, and not likely to change significantly

![image](https://user-images.githubusercontent.com/18595935/53159001-4b270f00-3608-11e9-983a-da3c826abf09.png)


### 2. Functional Safety Process

- ISO 26262 - Functional Safety Process
- ISO/PAR 21448.1 -  Safety of the Intended Functionality

![image](https://user-images.githubusercontent.com/18595935/53158228-7ad51780-3606-11e9-9707-1eb711e8b4ec.png)

### 3. Safety of the Intended Functionality (SOTIF)

- Failures due to performance limitations and misuse
 - Sensor limitations
 - Algorithm failures / insufficiencies
 - User misuse –overload, confusion 
- Designed for level 0-2 autonomy
- Extension of FuSa 
 - V-shaped process
 - Employs HARA

# 3. M3-2: Learn from Industry Experts

# 4. Weekly Assignment



