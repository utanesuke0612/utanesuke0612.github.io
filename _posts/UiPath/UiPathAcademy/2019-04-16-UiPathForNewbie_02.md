---
layout: post
title: 小白学UiPath-02-Level01-Foundation基礎-Part01
date: 2019-04-08 01:01:02
categories: RPA
tags: RPA
---
* content
{:toc}

# 0. 总结

这部分是Level 1 Foundation (基礎)トレーニング 的1-6章，主要介绍了：
1. UiPath的基本概念,构造,快捷键
2. 关于UiPath中使用的变量与数据类型
3. 控制flow/分支/循环 等程序设计中基本概念在UiPath的体现
4. 文字列的处理，数据的收集与处理
5. 各种recording的差异
6. UI高级操作，data scraping,OCR等
7. Selector的概念与操作

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

- **注释：**通过Ctrl + D 将选中的activity注释掉，通过Ctrl + E 将注释去掉

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

# 2.2 变量与数据类型

- **変数の管理**

通过下面两种方式添加变量：

![image](https://user-images.githubusercontent.com/18595935/56212514-1ded5f00-6095-11e9-8e62-ae550c6977b7.png)
> 通过这种方式添加的变量，其作用范围为最小的容器内。

![image](https://user-images.githubusercontent.com/18595935/56212527-25146d00-6095-11e9-8148-8b43112bfcd1.png)

- **workflow设计**

> 参考 [here](https://studio.uipath.com/lang-ja/docs/workflow-design)

各种activity：

1. 条件分支if
2. If...Else If 多条件分支
3. VB If函数
4. Switch Activity
5. Flow Switch

关于数据，从使用范围来区分，可以分为参数(引数)和变量(変数)：
- 参数：主要目的是将数据从一个workflow传递给别的workflow
- 变量：在一个单一的workflow内，捆绑在一个容器上

关于命名规则：
1. 变量：使用大写字母开头的驼峰命名法，如FirstName
2. 参数：添加表明参数类似的前缀，使用驼峰命名，例如in_FileName
3. activity名：比如「Click the Save Button」将操作的动作作为关键词包含在标题中
4. workflow名：所有的workflow名中，包含workflow要进行的操作，比如GetTransactionData。

- **変数パネル**

参考[here](https://studio.uipath.com/lang-ja/docs/the-variables-panel)

- **ジェネリック値(GenericValue)変数**

这是一种通用变量，根据执行的action，能自动变换成其他数据类型。

![image](https://user-images.githubusercontent.com/18595935/56263297-56d11680-611d-11e9-9819-5fa74bff032b.png)

- **テキスト変数**

![image](https://user-images.githubusercontent.com/18595935/56263523-39507c80-611e-11e9-8ec3-560ce39dda13.png)

- **True または False 変数**

参考[here](https://studio.uipath.com/lang-ja/docs/true-or-false-variables)

![image](https://user-images.githubusercontent.com/18595935/56264849-ba117780-6122-11e9-9a78-82b0774c47f0.png)

- **数字変数**
- **配列変数**
- **日付および時刻変数**
- **データテーブル変数**
- **引数の管理**
- **引数パネル**
- **引数の使用**
- **インポートした名前空間について**
- **新しい Namespaces のインポート**
> [here](https://academy.uipath.com/learn/course/457/play/4135/ressun2-xiang-xi-qing-bao;lp=21)
> 
> 

## 2.3 控制flow

- if / Then / Else
- Decision
- While / Do while / For Each
- FlowChart内部的重复构造
- workflow内部使用vb.net

## 2.4 条件分支

- Flow Decision，在FlowChart中使用

![image](https://user-images.githubusercontent.com/18595935/56266358-f2b35000-6126-11e9-9316-c01800d8e2d8.png)

- If，在Sequence中使用

![image](https://user-images.githubusercontent.com/18595935/56266384-03fc5c80-6127-11e9-9fa3-933536619efa.png)

1. 新建一个flowchart，命名masterflowchart
2. 在start后面，上面的masterflowchart内部，再新建一个flowchart，命名为具体要做的操作，如"闰年check"
3. 在闰年check flowchart中，添加变量year/int32
4. 在start后添加input dialog，将result设置为year变量接收
4. 添加flow decision，添加条件 year mod 4 = 0 ，即除以4是否为0
5. 添加两个messagebox，分布连接到flow decision的true和false
6. 在messagebox中，分布输入对应要显式的消息

![image](https://user-images.githubusercontent.com/18595935/56267377-9aca1880-6129-11e9-8c05-f5fc6cd5701d.png)

上面是flowchart,下面是sequence的情况：

![image](https://user-images.githubusercontent.com/18595935/56267712-918d7b80-612a-11e9-979f-8808feb8bc6d.png)

需要将上面的Flow Decision替换成If判断。

## 2.5 循环loop

- while():
- do{}while():

1. 添加Do While到Sequence中
2. 按住Ctrl，将input Dialog和If加入到Do while中
3. Do while中添加判断条件 **year mod 4 <> 0**

如下图：

![image](https://user-images.githubusercontent.com/18595935/56288322-7ede6b00-6159-11e9-8fd0-14ba48777f7f.png)

如上就实现了do while的判断，只要符合上面的条件，就不断循环。

- For...Each()循环

![image](https://user-images.githubusercontent.com/18595935/56291164-b819d980-615f-11e9-8232-ea3a672ba702.png)

下图是使用For Each循环：
1. 先弹出文件选择对话框
2. 选择文件夹后，将该文件夹内的文件列表打印出来

![image](https://user-images.githubusercontent.com/18595935/56291663-a422a780-6160-11e9-946e-9b9869073670.png)

## 2.6 实践篇(推测game)

1. 在MasterFlowChart中添加一个推測Game FlowChart
2. 添加Assign,添加RandomNumber = new Random().next(0,1000)
3. 添加InputDialog, 将其输出设置为GuessNumber变量
4. 添加FlowDecision, 条件是GuessNumber = RandomNumber
5. Ture的情况下，指向MessageBox
6. False的情况下，继续添加一个FlowDecision，条件是GuessNumber < RandomNumber
7. 上面FlowDecision的True和False，分别指向对应的Assign，在Assign中使用Hint = "请输入更大的数字"和Hint = "请输入更小的数字"
8. 将上述InputDiaglog中的Text修改为Hint
9. 另外，将上面的两个Hint的Assign指向Input Dialog

![image](https://user-images.githubusercontent.com/18595935/56293854-e3eb8e00-6164-11e9-9c55-4900dc4d5a1d.png)

下面是执行过后的图：

![image](https://user-images.githubusercontent.com/18595935/56293999-21e8b200-6165-11e9-9c3b-a0c6e6ec5a21.png)

其中800-785，是inputDialog的Title，800表示GuessNumber，785表示RandomNumber，需要设置InputDialog的Title为`GuessNumber.ToString + "-" + RandomNumber.ToString`。


## 2.7 小结

- sequence
- flowchart
- 控制Flow
- 代入Assign
- 延迟Delay
- Do While
- If
- Switch
- While
- For Each
- Break 循环中断

## 2.8 练习1

完成如下的任务：
1. 使用InputBox询问 "1+1=2?"
2. 如果是Yes，则将打开NotePad.exe，并写入“正解”，否则写入"不正解"

![image](https://user-images.githubusercontent.com/18595935/56297528-7000b400-616b-11e9-904f-44d9e0e1266f.png)

写入内容到NotePad.exe作为一个子sequence：

![image](https://user-images.githubusercontent.com/18595935/56297590-90307300-616b-11e9-8882-a07f49e44d85.png)

## 2.9 练习2

将sequence中添加4个GenericValue，分别为A/B/C/D，计算这4个变量的和：

![image](https://user-images.githubusercontent.com/18595935/56339557-b4329980-61e9-11e9-8e59-8153a0931d36.png)

# 3. 数据操作

本节包含：

- 处理文字列：分割/格式化
- 根据特定条件，取数据表中特定行

## 3.1 关于数据类型

- 单一型数据: Char / Boolean / Integer / Date
- 集合型数据: Array / Queue / List / String / Dictionary
- 表形式数据: DataTable

关于GenericValue型，可以保存各种数据类型，比如String/Boolean/Integer/Date。

GenericValue型能使用的method：

![image](https://user-images.githubusercontent.com/18595935/56291164-b819d980-615f-11e9-8232-ea3a672ba702.png)

**关于Array和List**：
- Array：其中的元素(可变);元素的个数(不可变)
- List ：其中的元素(可变);元素的个数(可变)

使用定义的Array和List进行循环，输出到log:

![image](https://user-images.githubusercontent.com/18595935/56341882-63bf3a00-61f1-11e9-94e3-32ebbe3bdf63.png)

**Dictionary<TKey,TValue>:**

![image](https://user-images.githubusercontent.com/18595935/56342342-b3eacc00-61f2-11e9-9c94-38a589478035.png)

## 3.2 文字列操作方式

![image](https://user-images.githubusercontent.com/18595935/56407847-79456a00-62ac-11e9-9b54-9c2b3544b93c.png)

另外，通过`strInput.Split("：]".ToCharArray)(1)`可以将字符串分割，遇到`:`或`]`即断开字符串，存储为字符串的数组。

## 3.3 数据收集与输出

如果要组合一段字符串，输出当前时间：

1. 添加strDate变量，默认值 **Today is **
2. 添加MessageBox：“Good morning,” + strDate + Now.ToString
3. 如果修改格式，则为“Good morning,” + strDate + Now.ToString("yyyy/MM/dd")
> 也可以使用format函数，比如`String.Format(Filepath1,"ファイル")`，使用方式可以具体参考帮助文件，参考VB的帮助。

下面是String的代表性方法：

![image](https://user-images.githubusercontent.com/18595935/56409034-1c4cb280-62b2-11e9-830a-4c4ab58a39b8.png)

**关于data table：**

常用data table有csv,excel,web数据，下面通过两种方式将CSV输出：

![image](https://user-images.githubusercontent.com/18595935/56409150-b6acf600-62b2-11e9-8e30-ec4e87d430c9.png)

或是：

![image](https://user-images.githubusercontent.com/18595935/56409201-ed830c00-62b2-11e9-93ed-f4f464fb6b6d.png)

## 3.4 演習1

1. 读取CSV文件，并将其保存到DataTable变量：Names
2. 根据是否会员，对数据进行过滤
3. 使用姓和名，根据简单的规则(姓的前面3个字母变成大写，名的前3个字母变成小写)，作成nickname
4. 将生成的Nickname输出

CSV文件如下：

![image](https://user-images.githubusercontent.com/18595935/56409306-6c784480-62b3-11e9-95f8-29971b5ebcd4.png)

作成workflow如下：

1. 将CSV读取，并保存到DataTable
2. 将DataTable代入到Member变量中，类型为DataRow[]
3. 使用For..each循环，取出每一行，设为row
3. 使用Assign取出姓和名
3. 使用String的函数，作成NickName

![image](https://user-images.githubusercontent.com/18595935/56411042-50c46c80-62ba-11e9-9d45-56238e3ce0f2.png)

# 4. recording概要

本篇学习：
1. 使用recorder添加UI的activity
2. customize方法

## 4.1 recording功能(basic,desktop基本)

- recording可能的：
1. 左键按下(button,checkbox,dropdown)
2. 文字输入

- recording不可的：
1. shortkey
2. 修饰key(ctrl+c,ctrl+a,など)
3. 右键key

下面分别使用basic和desktop的自动recording功能生成的workflow，用于在记事本中输入文字，并修改font：

- basic的自动记录

![image](https://user-images.githubusercontent.com/18595935/56425737-85ebb180-62f0-11e9-91d7-00fee671e977.png)

- desktop的自动记录

![image](https://user-images.githubusercontent.com/18595935/56425744-8edc8300-62f0-11e9-94de-74e4dd237748.png)


- 关于basic与desktop的差异：

![image](https://user-images.githubusercontent.com/18595935/56425895-16c28d00-62f1-11e9-98e4-b3820540de84.png)


## 4.2 recording功能(basic,desktop应用)

对上面的进行改造，可以根据inputdialog的内容，写入记事本：

![image](https://user-images.githubusercontent.com/18595935/56426248-88e7a180-62f2-11e9-8d0b-233f1a88f0b2.png)

## 4.3 recording功能(web)

访问天气预报网站，检索东京的天气，计算第二天的温度差，如果差高于10°则给予报警。

1. 选择web
2. web recording中，选择Record，然后选择东京都
3. 按下ESCkey，停止
4. 使用Text，copy下最高气温
5. 使用Text，copy下最低气温
6. 添加Assign，设置等式`TempDiff = 0+MaxTemp-MinTemp`,这里0表示将结果转变为数值
7. 使用If进行分支判断

![image](https://user-images.githubusercontent.com/18595935/56429667-b5a1b600-62fe-11e9-8f18-22c936c0c2de.png)

需要注意：OpenBrowser的Type设置为Chrome。

## 4.4 练习1

1. 弹出对话框，用于输入写入记事本的文字
2. 弹出对话框，用于输入记事本的文件名
3. 打开记事本
4. 将文字写入记事本
5. 改成粗体，size变为16
6. 以上面的文件名保存文件

具体的workflow作成步骤：

1. 作成两个inputdialog，分别用于保存记事本文字和文件名
2. 然后使用自动recording，录制剩余的部分，首先打开计时班
3. 选择recording -> desktop
4. 在desktop的recording中，选择start app，并点击记事本
5. 点击recording
6. 输入"text"到记事本
7. 点击修改格式，粗体和16，完毕后OK
8. 点击file->使用名称保存，输入"filename"并保存文件
9. esc退出recording，保存
10. 查看录制的workflow，使用inputDialog中的文字和文件名的变量，替换上面临时的文字和文件名。

## 4.5 练习2

1. 弹出对话框，输入要查询的城市
2. 进入google，输入该城市的天气，进行查询
3. 将查询的气温输出

具体的workflow作成步骤：
1. 添加InputDialog，并保存输入的城市
2. 在Chrome中打开google.com
3. 打开web，在web recording中打开web浏览器
4. 点击type,录入要检索的内容，内容随意，稍后会进行替换
5. 点击type->hotkey按下，使用enter key
6. 点击copy，将温度值copy下来
7. web recording中，选择关闭浏览器
8. 保存终止
9. 替换文本为变量

完毕后的workflow如下图：

![image](https://user-images.githubusercontent.com/18595935/56454277-3907e980-6389-11e9-8186-b815563b9ffc.png)

# 5. UI上的高级操作

1. 3种input 方式的设定，以及各自的差别
2. screen scraping wizard的使用方法
3. 3种output方式的设定以及区别
4. data scraping wizard的使用方法

## 5.1 输入输出方法

![image](https://user-images.githubusercontent.com/18595935/56466672-96666e00-644f-11e9-85ca-b4565362974f.png)

- 能recording的：
	+ button按下
	+ checkbox按下
	+ dropdown
	+ 文字shur

- 不能recording的
	+ shortkey
	+ 修饰key,ctrl+c等
	+ 右键按下
	+ mousebar

1. 选择basic
2. recording 开始按下
3. 选择记事本的空白区域，输入文字
4. 然后最小化
5. 再次点开记事本，继续输入
6. 保存

输入的方式有三种：
1. default
2. window message
3. simulator

## 5.2 画面scraping

关于数据的输出方式：

> 默认的方式是第一种，FullText

![image](https://user-images.githubusercontent.com/18595935/56466666-82227100-644f-11e9-8de2-2d84a8aee8b8.png)

看一下实际的例子：

1. 选择画像scraping
2. 准备打开记事本，IE，以及demo程序
3. 获取IE上的文字串，点击后在Scrape Result Review中选择Scraping Method可以切换不同的方式(OCR,Native,FullText)，同时更新，可以看到结果将发生变化
4. 最后用MessageBox输出

自动的输出方式，与其对应的手动追加方式：

|输出方法(自动)|activity(手动)|
|:--|--:|
|Basic Recording|GetText|
|Full Text|GetFullText|
|Native|GetVisibleText|
|OCR|GetOCRText|

然后，通过手动添加activity的方式添加了GetFullText：

![image](https://user-images.githubusercontent.com/18595935/56485662-e442ab00-650f-11e9-8ef2-4d14700f8582.png)

## 5.3 data scraping

与前面两类不同，data scraping能够对应的是**结构化数据**，比如google的结果，都是固定的格式(title-url-details)。

通过选择Data Scraping，选择结构化的数据后，根据wizard提示，抽出对应的数据的flow：

![image](https://user-images.githubusercontent.com/18595935/56486750-b95a5600-6513-11e9-89c1-3827804f2996.png)

## 5.4 练习1

1. 打开浏览器，输入“https://www.ebay.com/”
2. 检索 LapTop，将前100个项目的商品名和价格抽出
3. 输入到excle文件

workflow如下图：

1. 打开chrome，访问ebay.com
2. 使用web，自动录制
3. 输入laptop，点击Search
4. 保存退出
5. 打开data scraping
6. 按wizard提示操作
7. 最后将录制的activity的输出设置为ExtractDataTable
8. 添加system下写入excel的activity

![image](https://user-images.githubusercontent.com/18595935/56487640-ce84b400-6516-11e9-9a3b-c089d7796cee.png)

# 6. Selector

本章学习：
1. 什么是稳定的selector
2. 如何将wildcard插入selector
3. 如何将变量插入selector中
4. 如何作成相对selector

## 6.1 Selector概要

1. 打开basic
2. 按下recording，选择记事本"filename.txt"的输入区域
3. 输入文字

可以看到这个workflow如下：

![image](https://user-images.githubusercontent.com/18595935/56497948-a149fd00-653a-11e9-8ec2-9041d74b45ca.png)

下面就是notepad的selector，其中checkbox是一系列约束条件，如果不满足这些条件，robot会弹出下面的错误，显示selector无法找到。

![image](https://user-images.githubusercontent.com/18595935/56498071-246b5300-653b-11e9-9035-e7846c2f99fe.png)

如果将title的checkbox去掉，就会发现在其他文件名的记事本中，也能运行该robot。

## 6.2 Selector的结构/定制化/改善方法(1)

- 完全selector (recording-basic)
- 部分selector (recording-desktop)

### 1. 两者之间的差别

下面通过两种方式basic和desktop，录制计算器中按下7的操作，对比两种不同方式的workflow，以及selector：

![image](https://user-images.githubusercontent.com/18595935/56501179-c9405d00-6548-11e9-885e-44bb978e0dc0.png)

在basic中，针对按下7这个activity，其selector中包含了其app，以及按键等各个属性。
而在desktop中，最上层有一个attach window，下面存储的按下7这个activity，其selector只包含部分属性。

### 2. 使用通配符

`*` 和 `?` 分别表示多个文字，和 一个文字，比如如果某个workflow是针对文件`filename_0423.txt`的，要使得该workflow有通用性，可以将其selector
中的文件名进行修改，如下：

![image](https://user-images.githubusercontent.com/18595935/56551687-f8e07b00-65c3-11e9-9713-ccd9a6469e01.png)

## 6.3 Selector的结构/定制化/改善方法(2)

下面的workflow实现：
1. 弹出输入对话框，输入数字0-9
2. 使用highlight activity，并按下计算器中的数字

可以将输入框中的数字进行高亮显示：

![image](https://user-images.githubusercontent.com/18595935/56554210-ecf8b700-65cb-11e9-88ea-93ea09ba6c17.png)

## 6.4 Selector应用

假定在下面的网页(http://rpachallenge.com/?lang=ja)中输入名字，如果位置变化的话，可能会造成错误：

![image](https://user-images.githubusercontent.com/18595935/56557336-9001fe80-65d5-11e9-8884-da156b3df03b.png)


### 1. 使用 anchor base

1. 使用anchor base
2. 左边选择 find element,选中输入框旁边的label
3. 右边选择 type info，选中输入框，并输入文字

如下：

![image](https://user-images.githubusercontent.com/18595935/56557417-e5d6a680-65d5-11e9-9b30-0914e6798f7d.png)

### 2. 使用相对selector

1. 添加type info activity
2. 选中输入框后输入文字

会发现如果页面更新后，网页结构发生变化后，就无法正常工作了。

下面使用相对selector方式，修改上面的selector：
1. 使用Ui exploerer
2. 使用indicatetor选中输入框
3. 使用indicate anchor选中旁边的label

取出selector内容(因为id受页面结构影响，故将id的checkbox去掉)：

```html 
<html app='chrome.exe' title='RPAチャレンジ' />
<webctrl aaname='苗字' tag='LABEL' />
<nav up='1' />
<webctrl tag='INPUT' />
```

经过上面的修改后，发现即使发生页面变化，也能准备将文字输入到指定输入框。

## 6.5 练习

1. 使用 https://ja.fakenamegenerator.com 生成随机值，抽出姓名，电话号码，和公司名，并将姓名分割成LastName和FirstName
2. 然后将上面的信息，输入到 http://rpachallenge.com/?lang=ja 中。
3. 使用Ui Explorer作成selector

参考 [here](http://seikyoukan.jp/res/uipath/aca/%E3%83%AC%E3%83%83%E3%82%B9%E3%83%B36_%E6%BC%94%E7%BF%921.pdf)

1. `https://ja.fakenamegenerator.com `，选择成日本人的名字，其url为  `https://ja.fakenamegenerator.com/gen-random-jpja-us.php `
2. 打开 `http://rpachallenge.com/?lang=ja`

作成flow如下：

- 选取attach browser,选择上面的fakename的网站
- 查看selector，将其title修改为带有通配符的`<html app='chrome.exe' title='ランダムに名前を生成 - * - Fake Name Generator' />`
- 在Attach Browser中添加Get Text 的activity
- 使用indicate on screen选择生成的姓名
- 选择其selector，使用UI exploerer打开
- 追加其父要素，同时删除css-selector,处理前后：

处理前：

```python
<webctrl idx='1' tag='H3' />
```

处理后：

```python
<webctrl parentid='details' tag='DIV' idx='10' />
<webctrl tag='H3' />
```

- 将该activity的output设置为变量Name，因为这个Name变量在后续的Attach Browser会继续使用，需要修改其scope
- 下面处理公司名，公司名旁边有label，所以适合使用Anchor base,将其加入到Attach Browser中
- 左边使用Find element，点击网页上的label-社名
- 打开其selector，将 `<webctrl tag='DT' aaname='Company'/>` 复制过去。(通过UI Explorer查询到的)
- 右侧使用Get Text,将其output设置为变量CompanyName
- 另外将anchor的位置设置为left
- 同样的方式处理电话号码。(添加Anchor Base)
- FirstName和LastName使用两个Assign的activity处理，分别使用 `Name.Split(""c).GetValue(1).ToString`
- 下面处理文字输入，再加一个Attach Browser，将其指定为 `http://rpachallenge.com/?lang=ja `
- 这里可以使用两种方式，使用Anchor base，或相对Selector，这里使用相对Selector
- 使用UI Explorer，先使用IndicateElement选择姓名的输入框，再使用Indicate Anchor选择其label。
- 在selector editor中，check上其父要素，将Id的checkbox删除(它属于变动的)
- 添加Type Into到第二个AttachBrowser中，将上面得到的selector复制过去
- 用上面相同的方式，继续处理其他要输入的要素

> 上面的workflow没有执行成功，后续再修改，先赶进度。@2019年4月24日