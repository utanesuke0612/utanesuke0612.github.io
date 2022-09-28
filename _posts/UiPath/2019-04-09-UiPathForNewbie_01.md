---
layout: post
title: UiPath-01-RPA入门
date: 2019-04-08 01:01:01
categories: RPA
tags: RPA
---
* content
{:toc}

![image](https://user-images.githubusercontent.com/18595935/55791438-7357c800-5af9-11e9-86c4-41ae0653c1a1.png)
> <<小白学UiPath>>系列根据上书以及UiPath官网课程整理而成。

本篇文章中，主要介绍：
1. 什么是RPA？RPA有什么作用？
2. RPA能给公司带来什么？
3. 使用UiPath开始RPA

# 0. 总结

本篇根据上面的书整理而成，介绍RPA的组成，UiPath的基本操作，Project的作成方式(自动,手动,Programming)等，以及录制方法：
1. 时间差Recording
2. 使用Hotkey
3. 获取文件名
4. Website检索
5. InputDialog及MessageBox，接收用户输入
6. 使用变量
7. 使用ActivityPackage自动化Excel/Word

# 1. 什么是RPA？

如果不是在相关领域工作的人，听到RPA估计也是一脸的懵逼，RPA是*Robotic Process Automation*的缩写，即机器人业务自动化，使用RPA的主要目的，是将人类中PC重复作业中解放出来，进行一些更有创造性的事情。

RPA将基于规则的常规操作自动化，例如读取邮件和系统，计算，生成文件和报告，检查文件等，因此，RPA的应用范围非常广泛。在未来，那些你不想做的枯燥的工作，也许真的可以不做了，重复化、标准化的工作都可以让机器人帮你完成。

这里有一个视频解释了RPA是什么，能够完成什么工作 [什麼是RPA, 它又如何幫助企業提升效率？](https://www.youtube.com/watch?v=LTZLZFAlNs8)

上面的定义比较概括，关于RPA主要要理解下面两点:
1. RPA虽然号称机器人，但是它没有实体，是运行在PC上的软件机器人
2. RPA应用场景为：大量重复，规则明确

如果使用过excel的宏应该知道， 在Excel 中, 若要自动执行重复任务, 可以使用宏录制器快速记录宏中的步骤, 然后单击一次即可重新执行该任务。

RPA也比较类似，不过它不局限于Excel，适用于任何windows上的软件，比如浏览器/Office/SAP等，实现请求书发行，顾客管理，在库管理等一系列重复工作的自动化。另外，通过与其他设备的组合，有更加大的威力。

![image](https://user-images.githubusercontent.com/18595935/55794325-e8c69700-5aff-11e9-80db-a951c11fb680.png)

# 2. RPA能给公司带来什么？

RPA给公司带来的主要好处在于能够降低成本、提高质量和缩短响应时间。通过自动化手动和容易出错的工作来降低风险，通过大规模简化和自动化流程来提高效率，将员工的时间释放出来，让员工把时间和关注点放在更有价值的事情上——包括重新规划工作内容，更专注地解决产品组合、利润创造以及产品定价等机器人无法替代的工作上。

![image](https://user-images.githubusercontent.com/18595935/55966082-bdd07480-5cb2-11e9-85c5-15c927077ed2.png)


# 3. 使用UiPath开始RPA

**UiPath主要具备如下特征：**

- 操作简单

UiPath通过可视化的拖拽以及录像功能，使得其操作非常简单。

- 精度高

能精确定位每次操作的控件，比如button/Edit box等。

- 应用范围广泛

UiPath既能进行简单的作业，也能应用到大规模的复杂作业上，有桌面版和服务器版两种版本，满足中小企业以及大型企业的需求。

另外，还能与其他AI，如IBM的Watson以及Google Cloud，OCR等连接使用，截止2019年1月，在日本就有800家公司导入了UiPath，世界范围内共2700家公司。

**UiPath的构成：**

由三个部分的软件构成：

1. UiPath Studio: 作成Robot
2. UiPath Robot: 执行Robot
3. UiPath Orchestrator: 管理Robot

![image](https://user-images.githubusercontent.com/18595935/55966985-70ed9d80-5cb4-11e9-8926-89431013ec5a.png)

## 3.1 UiPath的基本操作

有如下一系列操作：
1. 从浏览器中选取一段内容
2. copy这段内容
3. 将这段内容，粘贴到word中

上面的这个作业整体，叫做一个**project**, 单个操作叫做一个**activity**，从1到3这一系列的操作叫做**workflow**。

可以通过下面三种方式完成一个workflow，可以相互结合使用：
1. 自动recording
2. 手动recording
3. programing


## 3.2 UiPath Studio主要构成

主要有编辑和执行两部分构成：

- 编辑：

![image](https://user-images.githubusercontent.com/18595935/56077026-487bb580-5e12-11e9-990e-451fd4ac3818.png)

- 执行：

![image](https://user-images.githubusercontent.com/18595935/56077030-61846680-5e12-11e9-852a-6993a7044700.png)

# 4. Recording

![image](https://user-images.githubusercontent.com/18595935/56077216-7c57da80-5e14-11e9-8d8e-fddca73d4000.png)

如上图是进行一个recording时常用的四个button，**新建**,**保存**,**执行**,**recording**。

另外recording有5类:
1. basic，标准记录方式，记录桌面软件的操作以及鼠标的移动。几乎所有场景，都是使用basic和desktop方式。每个activity中保存了`什么window`,`什么button`是操作对象。
2. desktop，与basic一样都是标准记录方式，同样记录桌面软件的操作与鼠标的移动，与上面basic不同的是，每个activity中保存的是相对位置信息，这使得需要customize时非常方便。
3. web，专门用于记录浏览器或是web程序的记录方式，与desktop一样，每个activity中保存的是相对位置信息。
4. 画像，basic和desktop通过menu和window的text信息进行特定，但是如果没有text时就无法特定了，比如FLASH和虚拟化环境中的操作，这时需要通过画像的方式去recording。
5. native Citrix，与desktop类型，但是是在Citrix环境中特有的记录方式。

**recording的controller：**

![image](https://user-images.githubusercontent.com/18595935/56077409-e40f2500-5e16-11e9-986e-267f4043517d.png)

- 自动recording：只使用①和②两个按钮，只能记录鼠标左键按下，以及text输入。
- 手动recording：使用所有按钮，能记录各种复杂的操作，如程序开始结束，左键按下，双击，右键...。

## 4.1 自动Recording与执行

1. UiPath Studio的编辑主界面中，点击 recording → basic。
2. Basic Controller中，点击 recording 开始进行录制。
3. 选取要录制的记事本，并在弹出框中输入要录入的文字，最后enter结束。
4. 按下ESC键，结束录制。
5. 保存并终止basic controller，返回UiPath主界面，点击保存，这样就得到了一个自动录制的Project。

![image](https://user-images.githubusercontent.com/18595935/56077620-55e86e00-5e19-11e9-8c12-be62e57c62d9.png)
> 上图就是一个录制的workflow，可以点击其中的activity进行修改。


在主界面中按下`実行`后，能自动执行刚才的workflow，能在记事本中自动录入文字，录入后如下图：

![image](https://user-images.githubusercontent.com/18595935/56077651-b11a6080-5e19-11e9-9ee0-67e5fb6f34c0.png)

> 执行button按下后，即使当时没有符合条件的软件，该robot貌似在后台监控，如果出现了上面workflow中的记事本文件，就会触发执行。

## 4.2 手动Recording与执行

因为自动Recording只能记录简单的操作，对于软件的启动和终止，右键按下等操作只能通过手动Recording完成。

例如上面的自动Recording的workflow，其记事本的启动，必须要手动完成。通过下面的方式完成自动Recording：

- UiPath Studio的编辑主界面中，点击 recording → basic。
- 打开记事本
- Basic Recording中，点击 Start app 开始进行录制。
  ![image](https://user-images.githubusercontent.com/18595935/56081143-eb4d2780-5e44-11e9-8a1f-0633fe3b326a.png)
- 选取要录制的记事本，会记录下当前记事本的信息，如下图：
  ![image](https://user-images.githubusercontent.com/18595935/56081112-82fe4600-5e44-11e9-88c3-74cd93b7b652.png)
- Basic Recording中，点击 Type，然后输入要录入的文字
- 保存并终止basic Recording，返回UiPath主界面，点击保存，这样就得到了一个手动录制的Project。

运行上面录制的project后，能自动启动一个记事本文件，然后输入录入完毕的文字。

## 4.3 编辑录制后的project

可以将录制后的project进行修改，比如复制一个已有的activity，修改activity中的输入值等。

![image](https://user-images.githubusercontent.com/18595935/56081263-46334e80-5e46-11e9-85bb-e3e7fb9620a3.png)


# 5. 更多Recording选项

## 5.1 时间差Recording

下面我们要进行的操作是将记事本中的文本，粘贴到word中，因为这里有下拉菜单，所以需要使用时间差recording。
在Basic Recording中，选择要进行的操作，比如click，然后按下F2键，将启动倒计时3秒，在屏幕右下角会显示，这三秒内的操作不会被记录。

下面是完成复制记事本文本，并粘贴到word的workflow，事先将记事本和word打开：
- 启动Basic Recording，选择 click
- 按下记事本中的「編集」菜单
- 再次按下Basic Recording中的 click
- 按下F2进行延时
- 在延时的3秒内，按下「編集」的下拉菜单，倒计时完毕即为0秒时，按下全部选择菜单「すべて選択」
- 再次按下Basic Recording中的 click
- 按下记事本中的「編集」菜单
- 再次按下Basic Recording中的 click
- 按下F2进行延时
- 在延时的3秒内，按下「編集」的下拉菜单，倒计时完毕即为0秒时，按下复制菜单「コピー」
- 再次按下Basic Recording中的 click
- 然后点击word中的粘贴按钮，最后Basic Recording中保存该workflow

保存后运行该Workflow，能自动完成从记事本中复制文本，并粘贴到word中。

## 5.2 使用hotkey

上面使用menu进行选取复制粘贴，下面使用快捷键完成相同的工作：

操作步骤如下：

- 启动Basic Recording，选择 Type→Send hotkey
- 选取记事本中的文本区域，添加key，ctrl + a 
- 继续选择Send hotkey，选择文本区域，添加key，ctrl + c
- 打开word，选择Send hotkey，添加key,ctrl + v
- 保存

## 5.3 获取文件名

下面的workflow实现将某个文件夹中的文件的路径及文件名全部取出，并复制到word中后，将路径删除，只保留文件名。

- 启动Basic Recording，打开任意文件夹。
- 按下 Start App，选择文件夹，并在参数栏中输入文件夹路径。
- 点击 Type→Send hotkey，选择该文件夹后，添加key，ctrl + a。
- 点击 Click，选择文件夹的「パスのコーピ」。如下图：

  ![image](https://user-images.githubusercontent.com/18595935/56108556-77676800-5f87-11e9-881d-7035b6a7529b.png)
- 启动word，按下 Start App，选择word，并在参数栏中输入`/w`。
- 点击 Type→Send hotkey，选择word后，添加key，ctrl + v。
- 点击 Type→Send hotkey，选择word后，添加key，ctrl + h。(用于替换操作)
- 上面的操作，会弹出文本替换对话框。
- 点击 Type→Type，选择文本替换对话框的输入框，输入要替换的文件串，enter结束。
- 按下 Click，选择全部替换按钮。
- 按下 Click，在弹出的完毕对UiPath话框中，选择OK按钮。

## 5.4 website检索

自动打开一个网站，并输入关键字进行检索，另外，需要预先在浏览器上安装插件。

1. 点击 Recording→Web
2. 打开浏览器 Edge，点击Web Recording的OpenBrowser
3. 在弹出框中输入URL参数
4. 按下Type，点击浏览器中的检索输入框，弹出框中输入检索用关键字，Enter结束
5. 按下Click，点击浏览器中的检索按钮
6. 结束保存workflow

# 6. Programing

前面介绍了手动和自动的recording，虽然很方便，但是自由度不高，所以需要与Programing结合使用，这里说是Programing，实际不涉及编码，只是将预置的activity进行排列组合。

## 6.1 workflow的种类

- Sequence

自上而下执行activity的workflow。

- Flowchart

流程图，可以有更多复杂的操作，比如重复和判断，能与上面的Sequence组合使用。

- StateMachine

状态机，用于表现复杂并且的特殊的workflow。

- Global Handler

当发生错误时，用于进行错误处理的workflow，一个Project中只能有一个Global Handler。

## 6.2 显示消息框

运行后弹出如下的消息框：

![image](https://user-images.githubusercontent.com/18595935/56111302-6ff98c00-5f92-11e9-8bb2-e68f6f97ac9e.png)

1. activity中选择 system - dialog - messagebox
2. 在该messagebox的properties中，修改其text和caption，注意有双引号，否则就是变量名了。

![image](https://user-images.githubusercontent.com/18595935/56111284-5d7f5280-5f92-11e9-84a9-a1bb8802c833.png)

## 6.3 使用变量

上面的消息框，只能输出预先设置好的内容，通过变量的设定，可以根据用户输入决定输出：

![image](https://user-images.githubusercontent.com/18595935/56112740-ec8e6980-5f96-11e9-8f63-a327449d8a48.png)

1. 将input dialog和message box加入到sequence中
2. 在input dialog中设置label和title，在result框中，按下ctrl+k，设置输出为变量 name01
3. 在Message box中，将Text设置为`"hello, " +name01`，这样显示出来的是上面的变量内容

![image](https://user-images.githubusercontent.com/18595935/56112649-a9cc9180-5f96-11e9-9d2e-787664e03b57.png)

# 7. 将工作自动化

## 7.1 添加activity的Package

UiPath针对一些软件，比如Excel/Mail等准备了activity的Package，进行其特有的操作。

通过下面的方式可以进行Package的添加：

![image](https://user-images.githubusercontent.com/18595935/56135415-a8698c00-5fcb-11e9-825f-868bc512f9cb.png)

添加后的ActivityPackage如下显示：

![image](https://user-images.githubusercontent.com/18595935/56135497-db138480-5fcb-11e9-888a-7d786ee6f81d.png)

## 7.2 使用Excel的Activity

下面的步骤，实现自动将文本输入到Excel中指定单元格。如下图，将A1和A2单元格中能写入指定的内容：

![image](https://user-images.githubusercontent.com/18595935/56136667-3777a380-5fce-11e9-8b33-0170ee83ddaf.png)

> 关于Excel与Word，都需要将其操作对象的文件作为scope进行对象指定。

## 7.3 作业记录Project的执行

下面的sequence实现:
1. 弹出输入用对话框，输入工作内容
2. 然后将当前时间，与工作内容，记入到excel表格

下图是其activity：

![image](https://user-images.githubusercontent.com/18595935/56138357-b6baa680-5fd1-11e9-8708-935c19257542.png)

执行后的excel
如下图：

![image](https://user-images.githubusercontent.com/18595935/56138507-06996d80-5fd2-11e9-9192-23a5de6f61b7.png)

# 8. 发布

上面在UiPath Studio中制作和执行了Project，下面将Studio中制作的Project进行发布，并在UiPath Robot中执行，过程非常简单：
1. UiPath Studio中Design页面的menu bar中点击 Publish/Deploy
2. 启动UiPath Robot，会出现在桌面的右下角，点击左键后，弹出可以下载的Packages，下载即可
3. 下载完毕后，就变成了start按钮，运行即可

如下图：

![image](https://user-images.githubusercontent.com/18595935/56179290-0b950600-6040-11e9-9e44-ddc9d3ea18fb.png)


