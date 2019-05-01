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

## 2.1 Process的导入与触发trigger方法

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



## 2.2 Robot的provisioning(预测)方法

## 2.3 バージョニングVersioning(版本)控制

## 2.4 job的scheduling

## 2.5 job queue的结构，保留的job处理，job的取消和终止

## 2.6 通过log监视所有登录到Orchestrator中的robot

## 2.7 什么是Asset

## 2.8 什么是Orchestrator queue


- `%userprofile%\.nuget\packages`通过这个可以删除已经发布的robot
- 意见：应该先搞清楚，robots/environments/process/job/schedules/assets的关系，然后再详细摄入，更好理解