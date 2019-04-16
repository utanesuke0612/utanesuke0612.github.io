---
layout: post
title: 小白学UiPath-02-Level01-Foundation基礎
date: 2019-04-08 01:01:02
categories: RPA
tags: RPA
---
* content
{:toc}

# 0. 总结

# 0. 关于UiPath Academy Certifications

详细参考[here](https://www.uipath.com/rpa/academy/certifications),FREE Advanced RPA Developer certification 在6月30日前免费。

**目标：在5月7日前取得该资格！**

- **Prerequisites：**

If UiPath is new to you, we strongly recommend completing **the RPA Developer Advanced Learning Plan** (Foundation, Orchestrator and Advanced trainings and REFramework knowledge) before applying for the certification. 

- **How does the process work?**

1. Phase I - Theoretical exam (Quiz) - 90 minutes
2. Phase II - Practical exam - 3h30m

# 1. Lesson01-UiPath概要

## 1.1 简介

一个业务流程称为Project，流程中的每个步骤称为Activity，Activity由button的按下，文件的读取等小的操作构成。

流程分为如下几种：

1. Sequence：直线型的流程
2. FlowChart：复杂流程，分有分支和循环等
3. State Machines：大规模的工作流程
4. Global Exception Handler：发生Error时触发的工作流

## 1.2 快捷键

- **文件管理：**

1. Ctrl + Shift + N - 新建新的Process
2. Ctrl + O - 打开以前作成的workflow
3. Ctrl + L - 打开log文件所在的文件夹
4. Ctrl + S - 保存当前的workflow
5. Ctrl + Shift + S - 保存当前所有的workflow
6. Ctrl + Tab - 当前所有打开的workflow之间移动
   ![iamge](https://files.readme.io/9f12fbc-crtlTab.png)

- **注释：**

通过Ctrl + D 将选中的activity注释掉，通过Ctrl + E 将注释去掉

- **调试：**

1. F7 - 针对打开的workflow进行调试
2. F8 - 检查当前的workflow是否有错误
3. F9 - 给选中的workflow设置调试断点
4. Shift + F9 - 删除当前workflow中的所有断点
5. F11 - 调试的时候，进入一个activity内部执行
6. Shift + F11 - 调试的时候，跳过某个activity

- **录制：**

1. Alt + Ctrl + W - 打开Web Recording工具栏
2. Alt + Ctrl + B - 打开Basic Recording工具栏
3. Alt + Ctrl + C - 打开Citrix Recording工具栏
4. Alt + Ctrl + D - 打开Desktop Recording工具栏
5. F2 - 迟延处理
6. F3 - 指定独立的录制区域
7. F4 - 記録する UI フレームワークを 既定値、AA、および UIA から選択できます

- **workflow的执行：**

1. F5 - 开始执行当前的workflow
2. Pause - 暂时中止
3. F12 - 停止执行当前workflow

- **選択したアクティビティ：**

1. Ctrl + T - アクティビティを [トライキャッチ (Try Catch)] アクティビティの [Try] セクション内に配置します。
2. Ctrl + N - 新しいシーケンスダイアグラムを現在のプロジェクトに作成します。
3. Ctrl + C - 复制一个activity
4. Ctrl + V - 粘贴一个activity

- **其他：**

1. F1 - 帮助
2. Alt + Ctrl + F - 检索
3. Ctrl + P - 启动Package管理

## 1.3 automation project

制作了一个简单的根据输入判断，然后显示messagebox的flowchart，如下：

![image](https://user-images.githubusercontent.com/18595935/56189060-021c9580-6062-11e9-8ccf-11f6f0dd855e.png)

- inputdialog中的Output Result设置为变量name (使用ctrl+k按下)
- 另外添加了一个Flow Decision，其condition设置为`name = "lijun"`
- 如果条件为True，则能跳转到MessageBox，MessageBox的Test设置为`"Hello," + name`

> 注意字符串有双引号，变量没有

## 1.4 activity package的管理

通过Manage Packages可以管理activity package，根据来源分为Local/Official/Community/Orchestrator，比如之前转为Excel操作而install的excel activity package。

## 1.5 automation lib的重复使用

通过将常用操作整理成lib，可以实现重复使用，下面是lib的显示栏：

![image](https://user-images.githubusercontent.com/18595935/56208861-145ff900-608d-11e9-835e-7f20de18e185.png)

## 1.6 Chrome与Firefox插件

[Chrome](https://studio.uipath.com/lang-ja/docs/installing-the-chrome-extension) 和 [Firefox](https://studio.uipath.com/lang-ja/docs/installing-the-firefox-extension)中安装UiPath插件后，可以实现自动化。

## 1.7 连接source管理系统

UiPath中通过team选项，可以连接各种[source管理系统](https://studio.uipath.com/lang-ja/docs/connecting-your-project-to-a-source-control)。

# 2. 入门知识

# 2.1 变量与数据类型


- **変数の管理**

通过下面两种方式添加变量：

![image](https://user-images.githubusercontent.com/18595935/56212514-1ded5f00-6095-11e9-8e62-ae550c6977b7.png)
> 通过这种方式添加的变量，其作用范围为最小的容器内。

![image](https://user-images.githubusercontent.com/18595935/56212527-25146d00-6095-11e9-8148-8b43112bfcd1.png)


- **workflow设计**



- **変数パネル**

- **ジェネリック値変数**

- **テキスト変数**

- **True または False 変数**

- **数字変数**

- **配列変数**

- **日付および時刻変数**

- **データテーブル変数**

- **引数の管理**

- **引数パネル**

- **引数の使用**

- **インポートした名前空間について**

- **新しい Namespaces のインポート**




