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

使用click image和click text：
- Click text使用的是OCR技术，将图片中的文字进行识别，然后查找对应的文字
- Click image使用单纯的图像，容易受到外界环境的影响，但其优点是速度快而且信赖度高。

人类如何进行选择和输入？会先确定旁边的label，再点击或输入内容，这里有两个button处理，Click Image和Click Text。
1. 比如下图中，先用Click Image选中 Cash In 的label，然后用弹出的Indicate选中后面的Input输入框
2. 然后使用Type in 在输入框中输入
3. 下面针对②，使用Click Text处理，点击Click Text选择Not On Us Check 的 label
4. 弹出Screen Scraper Wizard，在Text to be found 中输入"Not On Us Check"，然后点击Set Mouse Postion，**选中刚才的label**
5. 然后用弹出的Indicate选中后面的InPut 输入框
6. 然后使用Type in 在输入框中输入
7. 继续点击Click Text，选择整个windows，弹出的Wizard中，将Select输入到Text to be found中，然后点击Set Mouse Postion，定位到Select 按钮上，OK

![image](https://user-images.githubusercontent.com/18595935/56777595-659a8600-680d-11e9-808e-3571ae93741e.png)

## 1.2 图像base自动化-keyboard自动化

使用click image和click text都容易受到环境的影响而不稳定，使用它keyboard比如Tab键进行跳转更稳定。比如如下连续为两个input box输入，可以使用tab key跳转：

![image](https://user-images.githubusercontent.com/18595935/56784143-1f075480-682a-11e9-9868-0e87279e9557.png)

## 1.3 图像base自动化-情报取得

如果要从虚拟机(图像)中获取信息，有两种方式：Select/Copy和ScrapeRelative：
1. Select/Copy最简单，但是是适用于这种TextBox

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

