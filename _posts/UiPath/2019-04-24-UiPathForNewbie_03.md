---
layout: post
title: UiPath-03-Level01-Foundation基礎-Part02
date: 2019-04-08 01:01:03
categories: RPA
tags: RPA-Dev
---
* content
{:toc}

# 0. 总结

这部分是Level 1 Foundation (基礎)トレーニング 的7-13章，主要介绍了：
1. 图像与文本的自动化
2. Citrix の自動化(图像)
3. Excel与数据表的操作
4. PDF自動化概要
5. Mail自动化概要
6. Debug与例外处理
7. Project构成概要

# 1. Lesson7 - 图像与文本的自动化
 
Citrix的自动化，一般都发生在虚拟环境中，虚拟环境中都是以图像的形式存在，所以不能通过OS直接访问其app，本章介绍Citrix自动化中使用的几种方式(图像,文本,keystroke击键的自动化)。
1. Citrix Recorder的使用
2. Click Image activity的图像自动化方式
3. Click Text activity的文本自动化方式
4. 使用Scrape Relative抽出图像关联的数据

参考 [画像とテキストの自動化について](https://studio.uipath.com/lang-ja/docs/about-image-and-text-automation)，可以了解更多图像与文本自动化的知识。

## 1.0 总结

- 提高OCR精度的方法：
	+ 识别只有数字的情况时，使用Numbers Only，利用Google OCR
	+ 抽取变动值的时候，先找到固定要素，再使用ScrapeRelative
	+ 如果文本标签的font size变动时，使用Click OCR Text
	+ Citrix环境下抽取文本最好的方式是，选取所有文本进行copy

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

## 2.0 小结

1. 通过Select Item能将dropdown list中项目选取出来
2. 通过Find Image能找到指定的画像，并返回UI要素的Object
3. 通过Set Clipping Region能reset clip region的内存区域
4. 通过break能中断loop
5. Pick Branch不能单独使用

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

## 3.0 小结

![image](https://user-images.githubusercontent.com/18595935/56939553-f4780d00-6b43-11e9-9994-fee9c11268bf.png)


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

# 5. Lesson11-Mail自动化概要(练习未完成)

通过本章学习：
1. mail专用的activity的使用
2. message的发送与接收
3. 过滤mail，并从mail从下载附件
4. 使用maill的template

## 5.1 邮件自动化-收信

- 示例1：通过Get Outlook Mail Message，获取指定folder中的邮件，并输出标题：

![image](https://user-images.githubusercontent.com/18595935/56865323-c55c8100-6a07-11e9-9339-8798a2bc77f4.png)

> 如果Outlook中有多个账号，可以设置Get Outlook Mail Message 中Account为指定账号

- 示例2：与上面类似，不过这里将指定title的邮件，其附件抽出并保存：

![image](https://user-images.githubusercontent.com/18595935/56865352-03f23b80-6a08-11e9-9bb5-1faf8a38509f.png)

## 5.2 邮件自动化-收信2

完成的任务与上面类似，Get Outlook Mail Message中有个属性Filter，可以设置更加具体的Filter，详细可以参考Outlook中的Filter说明

![image](https://user-images.githubusercontent.com/18595935/56865925-82ea7280-6a0e-11e9-8402-25dac450eb2e.png)

## 5.3 邮件自动化-发信

- 通过下面的workflow，发送邮件：

![image](https://user-images.githubusercontent.com/18595935/56866133-d9f14700-6a10-11e9-9397-22bd3c254762.png)

- robot运行出错后，自动截图，并作为附件发送邮件：

比如如下，是一个click button的workflow，但是click button的程序并没有启动，出现了如下的错误：

![image](https://user-images.githubusercontent.com/18595935/56866165-35233980-6a11-11e9-84fd-bcde030b5b59.png)

通过下面的workflow，通过Try...Catch进行例外处理，这里分成两步完成：

- 先做成截图，保存，并发送邮件的workflow：
	+ 添加 Take Screenshot 的activity，其Output设置为Image变量
	+ 添加 Save Image的activity，保存图片
	+ 添加 Send Outlook Mail Message 的activity，发送邮件，其Attach Files中，最后一个value参数，设定为上面保存图片时的文件名

单独运行上面的workflow的话，会在运行时截取屏幕，并发送邮件

- 然后将需要监视的robot(业务robot)，与上面的截图workflow进行关联：
	+ 添加Try...Catch的activity，将业务处理的sequence，移动到Try Part中
	+ 使用左边的Project栏，将截图workflow的xaml文件，拖入到Catch部分

这样，当业务robot发生异常时，触发截图workflow，上面的两个workflow如下图：

![image](https://user-images.githubusercontent.com/18595935/56866406-ac59cd00-6a13-11e9-88f9-b4fec28d79dc.png)

![image](https://user-images.githubusercontent.com/18595935/56866417-cbf0f580-6a13-11e9-8cc1-0d02ca062d73.png)

## 5.4 练习1

## 5.5 练习2

## 5.6 总结

- 根据使用的不同的邮件协议，有多种关联的activity，有SMTP,POP3,IMAP,Exchange,Outlook等多种。
- 邮件取得关联的activity中，主要有如下共同的activity：
	+ 从特定的mail folder中获取email
	+ 只获取未读的mail，将其标记为已读
	+ 限定mail的收信数
- MailMessage的Object中无法直接获取timestamp信息，需要从Headers dictionary的Date值中取得。
- Outlook的activity中，为了根据Subject和ReceivedTime而接受邮件，有对应的Filter功能。
- 从文件读取内容，作为邮件模板的时候，使用一定的格式`{0}`，可以动态改变邮件内容。
- Outlook activity和Exchange activity，不需要设定连接参数，较易使用。

# 6. Lesson12-Debug与例外处理(练习未完成)

使用Debug，能特定出不需要的动作和Error，将其从workflow中删除，本章学习：
1. debug功能的使用方法
2. 使用Find Element 或 Element Exists，与application同步的方法
3. Try Catch activity的结构和使用方法

## 6.1 debug与例外处理-debug功能

在错误信息框中，弹出activity的名字，所以命名非常重要，能准确定位问题所在。

在Execute页面中，使用Debug启动调试，调试过程中，可以通过Locals确认运行时变量的值

## 6.2 debug与例外处理-意外操作的对应方法

如果因为窗口重叠，导致元素无法检出的error时，可以通过修改该Activity的属性的来对应，使得隐藏状态也可以操作：
- window message 送信
- click simulate 

输入activity的dubug顺序：
1. application 表示确认
2. 输入方法变更 动作确认
3. 合适的selector 设定确认

处理timing问题时，有如下三个activity：
- Find Element
- Element Exists - 对workflow的运行没有影响
- Wait Element Vanish

同样，处理图像也是上面的三个activity，不过对应的是Find Image，Image Exists，Wait Image Vanish。

参考下面的例子：

![image](https://user-images.githubusercontent.com/18595935/56904820-07ee8e00-6ada-11e9-97c7-39730ca83d53.png)

## 6.3 debug与例外处理-TryCatch

- Try：业务flow，即可能出现异常的workflow
- Catch：异常出现时执行的workflow，其Exception有很多种
- Finally：不管结果如何，肯定会执行的workflow

下面的例子中，捕捉上面workflow中timeout的错误，并在catch中进行补救的workflow，如下图：

![image](https://user-images.githubusercontent.com/18595935/56906311-eb078a00-6adc-11e9-972c-b67aa81f6fa7.png)

- Try中是上面一节的workflow，因为将timeout设为了0，所以会引发一场
- Catches中，添加了异常的处理，首先通过Log Message将异常信息输出了
- Rethrow能再次抛出异常，如果没有这一步的话，异常信息的messagebox不会被显示出来
- 第③不的sequence是补救措施，这个sequence与上面的Try Part类似，但是去掉了timeou为0秒，让你正常执行

## 6.4 练习1

## 6.5 练习2

## 6.6 总结

- 通过Execute页面的Start Debug按钮，开始Debug。
- debug时会出现下面三种现象：
	+ 现在执行中的action，会出现黄色的高亮，根据option的设定，该action影响到的要素，也会被红色高亮。
	+ Local Panel中，能确认所有当前的变量值
	+ 能取得所有workflow执行时action的详细log
- 需要将执行速度延缓时，通过Slow Step按钮，或者是使用Toggle Breakpoint将其完全暂定，然后使用Step Over跳过该action，再继续执行后续步骤。
- 等待application读取时，activity的默认timeout时间是30秒。Element Exists,Find Element,Wait Element Vanish等activity也可用于待机操作。
- Element Exists不对workflow产生影响，单纯的返回一个blue值。
- Try...Catch：将有可能发生异常的操作放在Try中，发生异常后的处理放在Catch中，最后无论如何都会执行的操作，放在Finally中。
- 为了对应多种异常，可以用多个Catch
- 即使检出了异常，想停止workflow的case也有，这时可以使用Rethrow。
- 在一个workflow中使用其他的workflow，可以使用Invoke Workflow.
- action/flowchart的命名要规范
- 希望使用的window上，有别的window存在时，可能会导致问题，为了回避这种问题，建议不要使用默认的输入method。
- selector有问题时，通过使用Indicate On Screen Option和Attach to live element Option，能刷新selector。

# 7. Lesson13-Project构成概要

本章介绍：
1. Invoke Workflow activity的使用方法
2. 有效率的Project的构成方法

## 7.1 workflow/process的构成方式-基础1

- 信赖性
	+ Workflow/Process稳定，异常处理
- 效率性
	+ 缩短时间
	+ 容易导入
- 可维护性
	+ 其他的担当者容易理解
	+ 易维护
- 扩展性
	+ 容易追加新的process

1. sequence：顺序执行的Workflow
2. flowchart：带有条件判断的业务Workflow
3. state machine：复杂规模的Workflow

## 7.2 workflow/process的构成方式-基础2

通过Invoke Workflow File，调用外部的Workflow文件，设定变量使其工作。

![image](https://user-images.githubusercontent.com/18595935/56937679-0902d800-6b39-11e9-910a-0be57c5a354c.png)

## 7.3 workflow/process的构成方式-实践

一个复杂的业务Workflow作成时，通过如下的步骤：
1. 画出大致的流程图
2. 在UiPath中将各个sequence/flowchart进行layout，并命名
3. 各个模块详细化

**图1:**

![image](https://user-images.githubusercontent.com/18595935/56937774-89c1d400-6b39-11e9-9d7b-d0e2bf6110a3.png)

**图2:**

![image](https://user-images.githubusercontent.com/18595935/56937887-05bc1c00-6b3a-11e9-8896-eb7f7a54a7a3.png)

如下是该Project的构成，Main是主Workflow，通过Invoke workflow调用其他的workflow：

![image](https://user-images.githubusercontent.com/18595935/56937965-73684800-6b3a-11e9-8522-e6f286497ed0.png)


## 7.4 总结

作为RPA Project，要考虑其信赖性，效率性，可维护性，扩展性、学习了Invoke Workflow使用方法，以及Process的构成方式：

- 能选择任意一个sequence或flowchart，右键选择Extract as workflow，然后替换为Invoke Workflow，实现相同的效果，这里将该sequence或flowchart作为了程序参数，在主workflow中使用。
- 花时间琢磨每个Workflow中最合适的layout
	+ Main：flowchart
	+ business logic：flowchart
	+ UI Interface：sequence
- 将Process分割成小的Workflow，这样方便单独开发和测试，以及Workflow的重复利用
- 考虑异常处理，将可能发生异常的Workflow放入TryCatch中，同时考虑补救处理的Workflow
- Workflow命名注意规则，同时使用comment，随时收集log，将跟随环境变化的设定，写入config文件，建议用excel配置
- 将不需要使用application关闭，长期保持clean的状态


# 8. 修了证明

![image](https://user-images.githubusercontent.com/18595935/56941168-ab2cbb00-6b4d-11e9-9d8d-5e649a278ef4.png)

# 9. 参考

- [UiPath アカデミー Level 1基礎 問題&解答集　～Les.1-5～](https://mara-ashida.hatenablog.com/entry/2018/12/23/020616)
- [UiPath アカデミー Level 1基礎 問題&解答集　～Les.6-9～](https://mara-ashida.hatenablog.com/entry/2018/12/23/075018)
- [UiPath アカデミー Level 1基礎 問題&解答集　～Les.10-13～](https://mara-ashida.hatenablog.com/entry/2018/12/23/075735)
- [【UiPath】Academyのテストを突破する(Lesson1)](http://zawaoo.com/uipath-academy-lesson1/)
- 上記のその他Lesson01-Lesson10