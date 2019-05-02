---
layout: post
title: 小白学UiPath-04-Level02-Orchestrator
date: 2019-04-08 01:01:04
categories: RPA
tags: RPA
---
* content
{:toc}

# 0. 总结

# 1. Orchestrator简介

## 1.1 课程介绍

UiPath Orchestrator是一个web程序，实现robot的自动化，监视和管理。
后面的课程video，主要介绍如下内容：
- Process的导入与触发trigger方法
	+ UiPath Workflow的公开
	+ Environment作成
- Robot的provisioning(预测)方法
- バージョニングVersioning(版本)控制
- job的scheduling
- job queue的结构，保留的job处理，job的取消和终止
	+ job的cancel与终止的差异
- 通过log监视所有登录到Orchestrator中的robot
	+ error message level的传递方法
- 什么是Asset
	+ Orchestrator中变量的存储
	+ 指定使用哪个robot中存储的asset
	+ credential存储
- 什么是Orchestrator queue
	+ 使用queque，操作多个robot处理的item的list
	+ queue中item的status
	+ item中添加queue的方法，以及transaction item的获取方法


## 1.2 前期准备

1. [demo site](https://demo.uipath.com/account/login?returnUrl=%2F)中，Become a tenant
2. 填入姓名等，注册成功后，进入如下的页面。

![image](https://user-images.githubusercontent.com/18595935/56942150-02358e80-6b54-11e9-82d0-4ed4789bd211.png)

# 2. Orchestrator详细

**Robot与Orchestrator之间的连接：**
- Provision Robot设定
 + 将robot设置中的machine name复制到Provision Robot中，并设定Username和Password
 + 同时复制Provision Robot中的Key
2. 将Orchestrator中的信息，设定到Robot中
 + 将上面的Key 设定到Robot的设置中
 + 将Orchestrator Url设定，比如`https://demo.uipath.com/`

现在最新的版本，与上面的手顺有差异，实际操作如下：
- Robots -> 添加+ -> Standard Robots，将Robot设置中的Machine Key复制过来，创建一个robot。
- Machine -> 选择一台，将其Machine key复制到Robot设置中，并设置URL。

![image](https://user-images.githubusercontent.com/18595935/57003482-146e0600-6c02-11e9-87c2-b01bb99b7ad1.png)

![image](https://user-images.githubusercontent.com/18595935/57003516-497a5880-6c02-11e9-87c2-616225d65c87.png)

1. 将robot注册到Orchestrator中
2. 通过UiPath Studio的publish
3. 为要使用的robot构筑环境environment
4. 使用publish的package，以及environment，创建Process
5. 最后启动job

- Process的导入与触发trigger方法
- Robot的provisioning(预测)方法
- バージョニングVersioning(版本)控制
- job的scheduling
- job queue的结构，保留的job处理，job的取消和终止
- 通过log监视所有登录到Orchestrator中的robot
- 什么是Asset
- 什么是Orchestrator queue

> `%userprofile%\.nuget\packages`通过这个可以删除已经发布的robot
> 意见：应该先搞清楚，robots/environments/process/job/schedules/assets的关系，然后再详细摄入，更好理解
> 

# 3. 练习

## 3.1 练习1

1. 创建一个新的Project，命名HelloWorld
2. 添加MessageBox，输出为「Hello UiPath Orchestrator!」
3. 使用Publish公开，公开成功后，会弹出Success的message，显示已经公开到了本地`C:\ProgramData\UiPath\Packages`

> 注意Publish到本地时，Robot的设定中，要与远程的disconnect

# 4. 英文版-Orchestrator2018.3

因为日文版视频以及练习中，使用的Orchestrator版本，与现状最新版本有差别，故使用英文版Orchestrator课程。

## 4.1 前期准备

在 [https://platform.uipath.com/](https://platform.uipath.com/)  上注册一个tenant.
> 作成  `lijun_uipath_demo1`，`lijun.kawasaki@gmail.com` 1107的密码。 

## 4.2 Orchestrator - Video Part 1

![image](https://user-images.githubusercontent.com/18595935/57074459-e29e9180-6d1e-11e9-8220-b141e34c4ed8.png)

第一步需要将Robot的instance连接到Orchestrator，在下一节中讲解。

进入 Orchestrator页面：
1. 打开左边的Robot，进入Environment，创建一个Environment，并将已有的robots加入该新建的Environment中。非
2. 为了在所有可用的robots上运行Package，需要在上面的Demo Environment中，将package连接到Environment中，这个连接可以通过创建一个Process完成。
3. 在Processes中，点击Deploy Process，选择已经上传的package。
4. 通过这个Process的创建，使得可以同时在已有的三个robot上执行该package。为了实现这个，需要创建一个新的job。
5. 点击JOB页面的Play，可以创建job并执行。

## 4.3 Orchestrator - Video Part 2

将Robot的instance连接到Orchestrator，有三步：
1. Provisioning the Machine in Orchestrator
2. Provisioning the robot
3. Setting up the local robot with the necessary information from Orchestrator

### 1. Provisioning the robot in Orchestrator

有两种，分别为Standard Robot和a floating one.

- Machine 页面中，选择Machine Template
- Robot中添加一个新的floating robot，命名localFloatingRobot
	+ 下面的字段`Domain\UserName`，通过cmd中输入命令`whoami`，得到`laptop-4kogtoiu\utane`，密码设为1107的密码，Type设为Attended
> 问题1：这里无法设置为Attended，显示如下的error，只能设置为Development
![image](https://user-images.githubusercontent.com/18595935/57064426-3c905e80-6d01-11e9-85d5-831a51342a0f.png)

- 打开UiPath Robot的setting，将刚才生成的Machine Template的Machine Key copy过来，另外，设置Orchestrator Url为`https://platform.uipath.com`，即当前Orchestrator web app的URL。
> 问题2：视频中说该setting的Status会变成Connected LICENSEed，但是我这里显示的是Robot unavailable
![image](https://user-images.githubusercontent.com/18595935/57064494-706b8400-6d01-11e9-8e55-d5db77abd627.png)

通过上面的步骤，就将一台机器与Robot连接了。

下面创建一个Standard的robot，先将上述的floating robot与Machine template删除。

- 复制robot setting中的Machine name，粘贴到Orchestrator的Machine -> standard machine.
- Robots页面-> Standard Robots
	+  下面的字段`Domain\UserName`，通过cmd中输入命令`whoami`，得到`laptop-4kogtoiu\utane`，密码设为1107的密码，Type设为development 
- 将上面的Machine key和URL，设置到Robot设定项目中，然后connected。显示status为：Connected,licensed.

然后再经过下面的步骤，就可以在远程运行robot了：
- 将robot添加到environment中。
- 手动添加Package到Orchestrator中，使用Porcesses页面的Package Tab, upload一个Package文件`*.nupkg`。
- 再Deploy一个Process
- 最后，在JOBS中Start一个Process，按下Start后，就可以看到这个Package被执行了。

同时，也可以在本地执行，通过Robot运行刚才的Process后，同时在Orchestrator的job中也有对应的执行记录。


**在UiPath Studio中，将Package Publish到Orchestrator中：**

在Publish中选择Orchestrator，publish后，在Orchestrator下显示如下：

![image](https://user-images.githubusercontent.com/18595935/57072617-4756ed80-6d19-11e9-8423-7f4861083ace.png)

在Process中出现多个对应版本，同样在Robot中也显示有新的版本可以更新。

### 2. Orchestrator中管理和运行Process的5步骤

1. 在Orchestrator中注册Robots
2. 在UiPath Studio中publish一个Package到Orchestrator中
3. 创建一个包含了待使用Robots的Environment
4. 新建一个Process，关联到刚才的Package，和Environment
5. 创建一个job来运行刚才的Package

### 3. 输入输出参数

- 创建一个Workflow如下图，有两个参数，输入和输出，输入带有默认值，输出通过Assign计算得到。

![image](https://user-images.githubusercontent.com/18595935/57074139-fb5a7780-6d1d-11e9-9d2d-9e646b1a914d.png)

- Publis后，在Orchestrator中，将Process切换到最新版的Package

- 新建一个Job，在job中修改输入参数的值，如下图，运行后得到的结果就变了：

![image](https://user-images.githubusercontent.com/18595935/57074210-33fa5100-6d1e-11e9-9ce1-2a5605437edf.png)

- JOB运行后的结果如下图，输出参数out的值如下图：

![image](https://user-images.githubusercontent.com/18595935/57074266-59875a80-6d1e-11e9-9681-11cb115e7862.png)

## 4.4 Orchestrator - Video Part 3

### 1. 重复执行Process

创建job的时候，在Allocate dynamically 中指定执行次数即可，比如指定2次，那么在job中可以看到如下图：

![image](https://user-images.githubusercontent.com/18595935/57083550-b2adb900-6d33-11e9-965c-ebe29f73e09f.png)

可以看到一个job还没有执行完的话，另一个是处理pending挂起状态。

### 2. Schedules

选定Process，触发的周期等，可以设置Schedules，另外在User Setting中，有Non-Working Days的设定，可以用于在Schedules设定中。

### 3. kill和Stop的区别

作成如下的Workflow，并publish到Orchestrator上：

![image](https://user-images.githubusercontent.com/18595935/57087327-c3156200-6d3a-11e9-875b-ae428468517d.png)

1. 如果是stop的话，会使得上面的Workflow走True的flow，能做最终的处理
2. 如果是kill的话，会直接杀死flow

## 4.5 Orchestrator - Video Part 4





