---
layout: post
title: 小白学UiPath-02-Level01-Foundation基礎-Part02
date: 2019-04-08 01:01:03
categories: RPA
tags: RPA
---
* content
{:toc}

# 0. 总结

这部分是Level 1 Foundation (基礎)トレーニング 的7-13章，主要介绍了：


# 1. Lesson7 - 图像与文本的自动化
 
Citrix的自动化，一般都发生在虚拟环境中，虚拟环境中都是以图像的形式存在，所以不能通过OS直接访问其app，本章介绍Citrix自动化中使用的几种方式(图像,文本,keystroke击键的自动化)。
1. Citrix Recorder的使用
2. Click Image activity的图像自动化方式
3. Click Text activity的文本自动化方式
4. 使用Scrape Relative抽出图像关联的数据

参考 [画像とテキストの自動化について](https://studio.uipath.com/lang-ja/docs/about-image-and-text-automation)，可以了解更多图像与文本自动化的知识。

## 1.1 图像base自动化-Citrix recording基础

使用click image和click text

## 1.2 图像base自动化-keyboard自动化

使用click image和click text都容易受到环境的影响而不稳定，使用它keyboard比如Tab键进行跳转更稳定。

## 1.3 图像base自动化-情报取得

使用Screen Scraping和Scrape Relative。

## 1.4 练习

使用如下的软件，利用图像/Text和hotkey，实现经费追加：

![image](https://user-images.githubusercontent.com/18595935/56631543-b20c8700-6690-11e9-9bef-66617cac3fe3.png)

操作如下：

1. 打开上面的ExpenseIt软件
2. 使用Recorder的Image
3. 使用click Text，点击Email:周围
4. 弹出ScrapingWizard后，在Search Text中输入Email，并点击Set mouse position，选择Email旁边的输入框
5. 另外，将OCR设置为MicrosoftOCR
6. 继续使用Recorder中的Type，并选择ExpenseIT这个exe的全体window，输入【training@uipath.com】。
7. 下面将Employee Number作为图像识别，选择Recorder中的Click Image
8. 选择Employee Number旁边的TextBox，点击Indicate a point
9. 点击Employee Number内某处
10. 使用Type，输入45321

下面继续处理其他字段：

1. 将CostCenter后面的下拉框打开
2. 使用Click Text，选择window全体
3. 在Search Text中使用Marketing
4. Employees中，再次使用Click Text，选择window全体，在TexttoBefound中输入 CSG
4. 最后使用Click Image，在Create Expense Report按钮的周围选择

## 1.5 补足：

本章比较难，参考[画像とテキストの自動化について](https://studio.uipath.com/lang-ja/docs/about-image-and-text-automation)继续学习。

