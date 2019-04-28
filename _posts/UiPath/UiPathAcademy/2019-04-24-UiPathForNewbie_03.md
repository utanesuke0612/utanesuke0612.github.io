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

### 1.Select/Copy

Select/Copy最简单，但是只适用于这种TextBox，可以看如下的例子：

- 使用Image中的Select/Copy，分别选择下图的两个TextBox，图一
- 保存后，在两个Select/Copy中，添加TypeIn，选择Tab键，这样能从一个TextBox跳转到下一个，如图二

图一：

![image](https://user-images.githubusercontent.com/18595935/56844424-e9767000-68ea-11e9-8508-a7571aadb8f4.png)

图二：

![image](https://user-images.githubusercontent.com/18595935/56844441-1dea2c00-68eb-11e9-8065-8fafc479f019.png)

### 2. ScrapeRelative

与之前的ScreenScraping类似，但是这个不是针对整个window，而是相对某个固定的anchor，如下的例子：

- 选择Image的ScreenRelative，选择左边的label作为anchor，弹出的indicate后，选择右边的textbox
- 在弹出的wizard中，选择OCR识别Textbox的文字，根据效果切换OCR种类，以及scale等其他选项
- 重复上述操作两次

图一：

![image](https://user-images.githubusercontent.com/18595935/56844595-b84b6f00-68ed-11e9-843b-71e9947f0e6f.png)


打开上面ScrapeRelative的workflow，可以看到总共有四步：
1. Find Image，根据anchor查找相同的图像
2. Translate clipping region，Uipath根据anchor图像，计算指定区域的位置
3. Get OCR Text
4. Reset clipping region

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

# 2. Lesson8 - 高度な Citrix の自動化の概要

虚拟环境中的自动化开发是很困难的，通常由很多不同方式可以实现，本章讲解Find Image这个activity，学习内容：
1. 自动化action，和其application上stage的同期方法
2. highlight activity的使用方法
3. 使用icon的双击，快捷键，以及命令行，打开Citrix环境内的application

## 2.1 高度な Citrix の自動化 - より良い操作

1. 打开一个[SAP网站](https://www.sap.com/japan/index.html)
2. 添加一个sequence，在sequence中添加FindImage，选择SAP网页标签的icon，出现这个icon说明网页加载完毕
3. 为了确认找到的是否正确，添加Highlight
4. 将上面的FindImage的Result设为elemnt，同时将变量elemnt设置到到Highlight中
5. 添加clickimage，选择login用的button
6. 在弹出的输入框后，添加Type Into，这是焦点已经在第一个输入框中了
7. 如果要同时输入多个内容，可以使用Tab键跳转

> 上面第5步之后，要判断弹出的输入password和email的页面是否加载成功，可以使用FindImage，加载Ok后，再使用TypeIn

## 2.2 高度な Citrix の自動化 - アプリケーション開始

虚拟环境中，可以通过如下三种方式打开app
1. 使用click image的activity，选中app的icon，并将该activity的click type修改为double click，但是这种方式比较脆弱，如果icon有变化就无法对应了
2. 或是，将该app的shortkey设置，设置后，使用send hot key 的activity

上面两种workflow的截图如下：

![image](https://user-images.githubusercontent.com/18595935/56846187-f0ab7700-6906-11e9-9eaf-413d096c5dcf.png)


另外，还有一种方式，通过命令打开，如下图：

![image](https://user-images.githubusercontent.com/18595935/56846190-0caf1880-6907-11e9-951a-920fb36f7b77.png)

workflow如下图：

![image](https://user-images.githubusercontent.com/18595935/56846194-3ec07a80-6907-11e9-94dc-1290fe700668.png)

# 3. Lesson9 - Excel与数据表的操作

通过本章：
1. 使用Read Range activity读取Excel中的数据
2. data table的操作
3. Excel中定义表的过滤方式
4. Append Range的使用方式

## 3.1 基础-Excel与数据表的操作

1. 打开一个Excel Application Scope 的activity，作为一个容器存储对该excel的所有操作
2. 添加Read Range的activity，前面是sheet名，后面空的表示整个sheet读入
3. 添加Output Data Table，将上面的data table的result转换为String
4. 添加MessageBox确认
5. 因为要将上面的内容写入一个新的excle中，所以需要添加一个新的Excel Application Scope 
6. 添加Write Range将上面读取的data table写入新的excel中

具体的workflow如下图：

![image](https://user-images.githubusercontent.com/18595935/56846912-e641ab00-690f-11e9-851b-b44016734060.png)

## 3.2 应用-Excel与数据表的操作

上面讲述了Excel的基本操作，下面操作如何给表中添加数据，如何排序，如何ReadCell和WriteCell:

1. 在上面的两个Scope中间，添加Build Data Table
2. 将三个字段"入社年","名字","名前"和对应的字段，添加到表中，最后结构如下图1，将result命名为dt_NewEmployeeData.
3. 然后再第二个Scope最后添加Append Range的activity，将上面的变量设置到这里

通过上面的操作，就可以将新追加的数据，添加到第二个Excel中了。

1. 添加Sort Data Table 的 activity，属性设置参考图2
2. 同样，通过Output Data Table，将上面输出的datatable，转换为String


另外，通过ReadCell和WriteCell，也可以将某处cell的内容，写到指定位置。通过SelectRange可以选定范围，进行后续操作，比如删除Copy等。

图1：

![image](https://user-images.githubusercontent.com/18595935/56847205-27878a00-6913-11e9-9e21-bad698246bbd.png)

图2：

![image](https://user-images.githubusercontent.com/18595935/56847242-9533b600-6913-11e9-8bc7-99b20196690f.png)


最后所有的workflow参考如下(第二个scope)：

![image](https://user-images.githubusercontent.com/18595935/56847316-3f134280-6914-11e9-83da-bbbe30421b9f.png)

![image](https://user-images.githubusercontent.com/18595935/56847332-594d2080-6914-11e9-8891-79751e1ea8eb.png)

## 3.3 实践-Excel与数据表的操作

实践篇综合上面的两节：
1. 将excel中的数据，通过条件过滤，最终输出
2. 将excel中通过条件过滤的数据，最终写到另一个新建的excel中

针对第一个任务：

1. 添加Excel Application Scope，指定该excel文件
2. 添加Read Range，指定sheet名
3. 添加Filter Wizard，指定条件，住所为东京，部署为总务部
4. 添加Output Table，将上面Filter过后的data table转换成String
5. 通过MessageBox输出上面的String类型

![image](https://user-images.githubusercontent.com/18595935/56858984-11370800-69bf-11e9-9d18-bf9c2d3dabce.png)

针对第二个任务，
1. 复制上面的workflow，将第四步以后的activity删除
2. 添加BuildDataTable，添加四个字段，分别与之前的excel的header对应，名字/名前/部署/住所，其output设置为dt_NewClientInfo
3. 添加For Each Row，设为row in dt_ClientInfo
4. 添加四个Get Row Item，分别将上面字段取出来，ColumnName为“名字”，Output的Value设置为“LastName”，另外三个字段类似
5. 添加Add Data Row的activity，DataTable设置为**dt_NewClientInfo**，ArrayRow设为**{LastName,FirstName,Department,Address}**，即上面通过For Each取出的字段
6. 因为要处理新的excle，故再添加一个Excel的Scope
7. 添加Write Range的activity，将`dt_NewClientInfo`设置为要写入的对象data table。

![image](https://user-images.githubusercontent.com/18595935/56859038-0e88e280-69c0-11e9-89bc-83b139a7cb7a.png)

## 3.4 练习1

将下面A和B列中的值求和，写入C列中：

![image](https://user-images.githubusercontent.com/18595935/56859083-c8804e80-69c0-11e9-8a2e-d6bc014576f0.png)

通过三种方式实现：

1. 打开Excel，将每一行的结果直接写入C列
2. 关闭Excel，在DataTable中新建一个列，将该DataTable写入到Excel文件最后
3. 使用Excel文件的公式进行计算

### **方法1：**

1. 添加Excel App Scope，并将visible选上
2. 添加Read Range，去除Add Header选项，output输出为InputsTable
3. 添加For Each Row，添加RowIndex的Int32参数
4. 将Assign activity，添加到For Each的body内部，设置`RowIndex = InputsTable.Rows.IndexOf(row) +1`.
5. 再下面添加两个Get Row Item，index分别为0和1，出力设置为ValueA和ValueB
6. 添加Assign，设置为ValueC=ValueA+ValueB
7. 添加Write Cell的activity，使用ValueC作为入力值，另外范围为`“C” + RowIndex.ToString`

![image](https://user-images.githubusercontent.com/18595935/56859496-d1741e80-69c6-11e9-9dfa-1ad07e41d1c2.png)


### **方法2：**

1. 添加WorkBook下的ReadRange，去除Add Header选项，output输出为InputsTable
2. 入力处，选择该excle的全路径
3. 添加AddDataColumn，列名设为`“C”`，output为InputsTable，类型设为Int32
4. 添加For Each Row，collection设为InputsTable
5. 添加Assign，设为ValueA=row(0).ToString
6. 添加另一个Assign，设为ValueB=row(1).ToString
7. 添加Assign，左边row(2)，右边`Integer.Parse(ValueA) + Integer.Parse(ValueB) `
8. 最后使用workBook下的WriteRange，写入原始的excel文件中。

![image](https://user-images.githubusercontent.com/18595935/56859649-cd490080-69c8-11e9-9f4a-2d7674b457ff.png)

### **方法3：**

> 省略了部分说明，具体参考下面的workflow图，以及上面的表述

下面直接将计算用的公式写入excel中：

1. 使用Excel Scope
2. 添加Read Range并设置Output
3. 添加Assign，设置RowsCount = InputsTable.Rows.Count
4. 添加Write Cell，范围为`“C1:C” + rowsCount`，值为`=SUM(A1,B1)`

![image](https://user-images.githubusercontent.com/18595935/56859643-c3bf9880-69c8-11e9-853f-55f2e76ad113.png)

## 3.5 总结

1. Excel文件操作时，有两种方式：通过ExcelApplicationScope作为容器，在容器内操作；或是使用workbook中的activity。如果能使用后者的话推荐使用，不需要安装excel，在后台运行
2. 通过Visible属性，可以决定操作在内部运行，还是使用Excel运行
3. ReadRange activity，读取excel的一部分，将其存储为data table
4. workbook是存储了多种不同类型数据的excel文件；data table是有行和列的table
5. write range在之前的entry上覆盖写入，而AppendRange是在最后追加写入
6. ReadRange和WriteRange中，通过Add Headers属性，决定是否读取或写入列的名字。
7. 通过Build Data Table activity作成data table时，列的数据类型参考VB.net中的。
8. 通过Sort Table或Filter Table activity，需要DataTable(内存中的表)作为输入
9. 通过SelectRange Activity可以方便的操作Excel文件
10. 操作data table时，使用For Each Row能简单的循环处理
11. 如果有Header时，在使用GetRowItem的activity时，不要用index，可以使用列名作为索引条件。

# 4. Lesson 10 - PDF自動化概要

通过本章学习如何从PDF文档中抽出数据：
1. Read PDF activity的使用方法
2. Read PDF with OCR activity的使用方法
3. 使用anchor，从PDF内的field中获取数据

使用前需要如下的准备工作：
1. 打开Acrobat，使用Ctrl+B，打开环境设定，在左边的読み上げ中，顺序设置为**印刷ストリーミングの読み上げ順序を使用**。这样就能确认每个PDF的要素了
2. 然后左边的アクセシビリティ中，[その他のアクセシビリティオプション] セクション中前面两个checkbox去掉

截图如下(中文)：

![image](https://user-images.githubusercontent.com/18595935/56860133-f3bd6a80-69cd-11e9-8ef4-b85ef74034cf.png)

## 4.1 PDF自动化-文档全体抽出方式

三种方式可以抽出文档全体的文本：
1. Read PDF Text
2. Read PDF With OCR
3. Screen Scraping

三种的workflow如下图：

![image](https://user-images.githubusercontent.com/18595935/56861127-1608b580-69d9-11e9-97c8-7673390e8e8c.png)

![image](https://user-images.githubusercontent.com/18595935/56861129-1dc85a00-69d9-11e9-9bed-2777b2c557eb.png)

![image](https://user-images.githubusercontent.com/18595935/56861136-26209500-69d9-11e9-9527-0f932551e441.png)

## 4.2 PDF自动化-特定要素抽出方式

通过Get Text，获取PDF中的文本，通过Get Text中的selector，修改其属性，使得其更通用。

> 但是在本机上测试无法通过，无法取得PDF的Text

## 4.3 PDF自动化-Anchor Base

通过Anchor Base，能更灵活的定位，旁边的Find element 也可以用Find Image代替：

![image](https://user-images.githubusercontent.com/18595935/56861501-5289e080-69dc-11e9-83ef-8b1a7be3c88e.png)

> 但是在本机上测试无法通过，无法取得PDF的Text

## 4.4 练习

> 注意开始前要检查PDF的设置状况。

1. 添加一个Attach window，将PDF file reader 关联起来
2. 在Do中添加Anchor Base
3. 使用Find element 添加到左边，选取作为anchor的对象，这里是请求日的label
4. 右侧使用Get Text，选择对应的日期Text，输出设为InvoiceDate变量
5. 另外，左边anchor的selector中，只保留Type属性，将id属性删除
6. anchor base中的position从Auto修改为left
7. 用上面相同的方式，再添加一个Anchor Base
8. 将得到的变量，用MessageBox输出

![image](https://user-images.githubusercontent.com/18595935/56861802-84e90d00-69df-11e9-9a91-3e3aabea65b3.png)

## 4.5 总结

1. PDF activity，分成两类，一类处理大的文本block及文档全体，另一类处理特定的文本要素。
2. 从PDF中抽取数据时，根据使用的文件，从2个activity中选择一个，Read PDF Text和Read PDF with OCR
3. 上面的两个activity都是在后台运行
4. 通过Screen Scraping activity可以获取Text的block
5. 从PDF文件中获取特定值时，可以使用Anchor Base
6. 使用OCR容易出错，尽量考虑用Read PDF Text代替Read PDF With OCR
7. 使用AnchorBase，即使文件内部的构造发生大的变化也能对应，所以能提高可靠性




# 5. Lesson11-Mail自动化概要

# 6. Lesson12-Debug与例外处理

# 7. Lesson13-Project构成概要



