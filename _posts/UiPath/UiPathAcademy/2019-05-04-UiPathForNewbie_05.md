---
layout: post
title: 小白学UiPath-05-Level03-UiPath进阶
date: 2019-04-08 01:01:05
categories: RPA
tags: RPA
---
* content
{:toc}

# 0. 总结

# 1. 理解Rebotic Enterprise Framework

这个课程通过demo的application和web App，开发业务流程，主要目的是为了理解ReFramework。

**背景：**

假定你是ACME System Inc这个公司的职员，责任是将backoffice的业务自动化。主要使用的是「ACME System Inc」这个web程序，TODOList在「Work Items」session内的结构化list中显示。

为了避免手工处理，开发机器人，对「Work Items」内的List项目进行处理。

**准备工作：**

1. 在[http://www.acme-test.com/](http://www.acme-test.com/)中注册，注册用email与Academy地址一致。
2. login后，点击User Options -> Reset Test Data。
3. reset后，会为该account自动作成测试用数据。
4. 如果想将已有数据删除，作成新的数据时，用上面的Reset Test Data，处理完毕后，Work Items的status，会从Open变成Completed。
5. 如果要修改密码，通过Forgot Password处理

## 1.1 ReFramework入門

Building productive robots requires:

1. Proper exceptions handling
2. Recovery abilities
3. Effective logging
4. Reporting functionalities
5. High maintainability
6. Extensibility
7. Reusability
8. Ease of development

> 下载 ReFramework，在[here](https://github.com/UiPath/ReFrameWork)

如下是Main的Workflow图，使用了StateMachine，四种status：
1. Init，读取配置文件，初始化程序。成功执行的话，会迁移到下一个state；出错则进入End Process。
2. Get Transaction Data
3. Process Transaction
4. End Process

![image](https://user-images.githubusercontent.com/18595935/57180788-29c78680-6ec7-11e9-8590-4488b9edee2d.png)



# 2. 业务流程-顾客secure hashで计算

# 3. 业务流程-年报的生成
