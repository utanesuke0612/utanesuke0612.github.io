---
layout: post
title: 小白学UiPath-05-Level03-UiPath进阶(1)
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

如下是该Project的构造图：

![image](https://user-images.githubusercontent.com/18595935/57195013-8474e700-6f88-11e9-9450-e0e9bc4367ab.png)

如下是Main的Workflow图，使用了StateMachine，四种status：
1. Init，读取配置文件，初始化程序。成功执行的话，会迁移到下一个state；出错则进入End Process。
2. Get Transaction Data
3. Process Transaction
4. End Process

![image](https://user-images.githubusercontent.com/18595935/57180788-29c78680-6ec7-11e9-8590-4488b9edee2d.png)

### 1.2 ReFramework詳細

### 1.3 UiDemo自動化-概要

下面使用UiDemo这个应用，完成transaction的自动化。输入用的数据(Transaction处理)保存在Excel文件中。

包含：添加Read Range的activity以及循环处理，从输出的data table的各列中取出数据，将处理登录到UiDemo程序中。

另外，为了成功的自动化，有如下课题需要解决：

1. Transaction数很大，为了一次能处理需要多个robot
2. 本次通过solution architector和business analyst的分析，为了处理这个Process需要5个robot。
3. business analyst的分析，有两个business的exception要处理：「无效的输入数据」和「CashIn值的超过」(要处理超过1000美元的CashIn的值)
4. solution architector分析，失败的transaction需要retry两次。
5. 如果UiDemo在使用时发生了异常，robot需要将其恢复正常，然后继续处理。
6. 另外，Transaction的retry，需要有warn作为log记录。
7. Hint：要使用Orchestrator的queue和Reframewok
8. UiDemo的登录名为admin，密码为password

### 1.4 UiDemo自動化-详细

> UiDemo.exe这个用admin/password登录。

#### **准备工作：**
- 将上面下载的ReFramework文件夹作为template，修改其对应的文件夹名。
- 修改project.json文件，修改为如下：

```python
...
  "name": "UiPath_REFrameWork_UiDemo",
  "description": "Demonstrating the REFramework with UiDemo",
...
```

#### **Dispatcher作成：**

> 2019年5月9日 流れに疑問が残っているので、後程整理