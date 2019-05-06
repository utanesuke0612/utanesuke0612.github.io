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

# 2. 日文版-Orchestrator

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

- Process的导入与触发trigger方法
- Robot的provisioning(预测)方法
- バージョニングVersioning(版本)控制
- job的scheduling
- job queue的结构，保留的job处理，job的取消和终止
- 通过log监视所有登录到Orchestrator中的robot
- 什么是Asset
- 什么是Orchestrator queue

> `%userprofile%\.nuget\packages`通过这个可以删除已经发布的robot
> 意见：应该先搞清楚，robots/environments/process/job/schedules/assets的关系，然后再详细摄入，更好理解


# 3. 英文版-Orchestrator2018.3

因为日文版视频以及练习中，使用的Orchestrator版本，与现状最新版本有差别，故使用英文版Orchestrator课程。

## 3.1 前期准备

在 [https://platform.uipath.com/](https://platform.uipath.com/)  上注册一个tenant.
> 作成  `lijun_uipath_demo1`，`lijun.kawasaki@gmail.com` 1107的密码。 

## 3.2 概要-Part 1

![image](https://user-images.githubusercontent.com/18595935/57074459-e29e9180-6d1e-11e9-8220-b141e34c4ed8.png)

第一步需要将Robot的instance连接到Orchestrator，在下一节中讲解。

进入 Orchestrator页面：
1. 打开左边的Robot，进入Environment，创建一个Environment，并将已有的robots加入该新建的Environment中。非
2. 为了在所有可用的robots上运行Package，需要在上面的Demo Environment中，将package连接到Environment中，这个连接可以通过创建一个Process完成。
3. 在Processes中，点击Deploy Process，选择已经上传的package。
4. 通过这个Process的创建，使得可以同时在已有的三个robot上执行该package。为了实现这个，需要创建一个新的job。
5. 点击JOB页面的Play，可以创建job并执行。

## 3.3 Orchestrator连接-Part 2

将Robot的instance连接到Orchestrator，有三步：
1. Provisioning the Machine in Orchestrator
2. Provisioning the robot
3. Setting up the local robot with the necessary information from Orchestrator

### 1. Provisioning the robot in Orchestrator

有两种，分别为Standard Robot和a floating one.

**创建一个floating的robot：**

- Machine 页面中，选择Machine Template
- Robot中添加一个新的floating robot，命名localFloatingRobot
	+ 下面的字段`Domain\UserName`，通过cmd中输入命令`whoami`，得到`laptop-4kogtoiu\utane`，密码设为1107的密码，Type设为Attended
> 问题1：这里无法设置为Attended，显示如下的error，只能设置为Development
![image](https://user-images.githubusercontent.com/18595935/57064426-3c905e80-6d01-11e9-85d5-831a51342a0f.png)

- 打开UiPath Robot的setting，将刚才生成的Machine Template的Machine Key copy过来，另外，设置Orchestrator Url为`https://platform.uipath.com`，即当前Orchestrator web app的URL。
> 问题2：视频中说该setting的Status会变成Connected LICENSEed，但是我这里显示的是Robot unavailable
![image](https://user-images.githubusercontent.com/18595935/57064494-706b8400-6d01-11e9-8e55-d5db77abd627.png)

通过上面的步骤，就将一台机器与Robot连接了。

**创建一个Standard的robot：**

先将上述的floating robot与Machine template删除。

- 复制robot setting中的Machine name，粘贴到Orchestrator的Machine -> standard machine.
- Robots页面-> Standard Robots
	+  下面的字段`Domain\UserName`，通过cmd中输入命令`whoami`，得到`laptop-4kogtoiu\utane`，密码设为1107的密码，Type设为development 
- 将上面的Machine key和URL，设置到Robot设定项目中，然后connected。显示status为：Connected,licensed.

然后再经过下面的步骤，就可以在远程运行robot了：
- 将robot添加到environment中。
- 手动添加Package到Orchestrator中，使用Porcesses页面的Package Tab, upload一个Package文件`*.nupkg`。
- 再Deploy一个Process
- 最后，在JOBS中Start一个Process，按下Start后，就可以看到这个Package被执行了。

同时，也可以在本地执行，通过Robot运行刚才的Process后，同时在Orchestrator的job中也有对应的执行记录。

**在UiPath Studio中，将Package Publish到Orchestrator中：**

在Publish中选择Orchestrator，publish后，在Orchestrator下显示如下：

![image](https://user-images.githubusercontent.com/18595935/57072617-4756ed80-6d19-11e9-8423-7f4861083ace.png)

在Process中出现多个对应版本，同样在Robot中也显示有新的版本可以更新。

### 2. Orchestrator中管理和运行Process的5步骤

1. 在Orchestrator中注册Robots
2. 在UiPath Studio中publish一个Package到Orchestrator中
3. 创建一个包含了待使用Robots的Environment
4. 新建一个Process，关联到刚才的Package，和Environment
5. 创建一个job来运行刚才的Package

### 3. 输入输出参数

- 创建一个Workflow如下图，有两个参数，输入和输出，输入带有默认值，输出通过Assign计算得到。

![image](https://user-images.githubusercontent.com/18595935/57074139-fb5a7780-6d1d-11e9-9d2d-9e646b1a914d.png)

- Publis后，在Orchestrator中，将Process切换到最新版的Package

- 新建一个Job，在job中修改输入参数的值，如下图，运行后得到的结果就变了：

![image](https://user-images.githubusercontent.com/18595935/57074210-33fa5100-6d1e-11e9-9ce1-2a5605437edf.png)

- JOB运行后的结果如下图，输出参数out的值如下图：

![image](https://user-images.githubusercontent.com/18595935/57074266-59875a80-6d1e-11e9-9681-11cb115e7862.png)

## 3.4 Process/Schedules/kill/stop-Part 3

### 1. 重复执行Process

创建job的时候，在Allocate dynamically 中指定执行次数即可，比如指定2次，那么在job中可以看到如下图：

![image](https://user-images.githubusercontent.com/18595935/57083550-b2adb900-6d33-11e9-965c-ebe29f73e09f.png)

可以看到一个job还没有执行完的话，另一个是处理pending挂起状态。

### 2. Schedules

选定Process，触发的周期等，可以设置Schedules，另外在User Setting中，有Non-Working Days的设定，可以用于在Schedules设定中。

### 3. kill和Stop的区别

作成如下的Workflow，并publish到Orchestrator上：

![image](https://user-images.githubusercontent.com/18595935/57087327-c3156200-6d3a-11e9-875b-ae428468517d.png)

1. 如果是stop的话，会使得上面的Workflow走True的flow，能做最终的处理
2. 如果是kill的话，会直接杀死flow

## 3.5 Log表示-Part 4

本节讲述，如果在Orchestrator中显示LOG，在UiPath Studio中，添加了log message后，可以在JOB的View logs中确认。

## 3.6 Assets/Queque-Part 5

### 1. Assets and Credentials

Assets是Orchestrator中，Robot能访问的信息，通过Assets页面中的Add按钮可以添加，有四种Assets，Text/Bool/Integer/Credential，比如在Credentials中可以创建username和password。

1. 在Orchestrator中，添加type为Text的asset，命名为**Message**。
2. Value中设定初始值。
3. 在Studio中，添加Get Asset的activity，在AssetName中填上面创建的asset，**Message**。
4. 在Value字段中添加一个新的变量，并在MessageBox中设置该变量。

同样的步骤可以设置Credentials，但它有两个字段，username和password，因为这里是密码，所以不能直接把解析的变量显示出来，需要用到TypeSecureText的activity。

- 注意1：在Orchestrator中设置Assets和Credentials时，不需要给字符串加双引号。
- 注意2：在UIStudio中，使用Assets和Credentials时，要设置AssetsName，这时要用引号将AssetsName包含起来。

如下图：

![image](https://user-images.githubusercontent.com/18595935/57120742-53d95580-6dae-11e9-923e-80ab20f7c1e3.png)

另外，在Assets设置时，可以根据不同的Robot给该Assets设定不同的值。

### 2. Queues-Practice

Queues是Orchestrator中一个强大的工具，能简单的将一个工作分配到多个Robots上，Queues中的transaction item按照顺序被处理。

在Queues中的各个Item，能够被多个Robots并行处理。

下面演示如何使用Queues，模拟一个简单的业务处理：计算多个transaction的和。输入数据包含在一个Excel文件中，有两列incomes和Payments，entries的确切数目未知。

在Ui Studio中创建两个Project，一个用于填充队列，另一个处理队列中的Items。

#### 1. 第一个Project：队列填充

**Orchestrator中创建一个Queue：**
- 在Queues页面中，点击Add
- 命名为	queue1，并在Max of retries section中为3

然后创建两个Projects，一个用于添加Items到Queue，另一个处理这些Items，处理的可以运行在多个Robots上，加快处理速度。

**Ui Studio中创建Rroject**

1. 创建一个Project，添加Excel Application Scope 的activity
2. 上面activity的路径设置为上面要读取的excel文件
3. 在上面的activity的do中添加Read Range，输出Result为"dt_practice8"的data table。
4. 添加For each row的activity，并将Add Queue Item的activity添加进去。
5. 在Add Queue Item activity的QueueName字段，能将Orchestrator中的queque与这个activity关联起来。在这里填入上面生成的"queue1"，注意有双引号。
6. ItemInformation字段，是Transaction中的Value被添加到的地方，这个Process类似于将arguments传递给一个Invoked Workflow，点击后面的省略号。
7. 继续点击Create Argument，给第一个argument命名 Income, Type为String，将其value设置为之前data table中的第一列`row(0).ToString`
8. 重复上面的步骤，添加第二个field "Payment"。

完成后的Workflow如下图：

![image](https://user-images.githubusercontent.com/18595935/57221852-96639200-703b-11e9-9c5a-457b1d76cd92.png)


执行上面的Workflow后，能发现在Orchestrator中，在对应的queue1中view Transactions，能发现从excel读取的数据：

![image](https://user-images.githubusercontent.com/18595935/57221987-fce8b000-703b-11e9-9e14-2915aaccad74.png)

#### 2. 第二个Project：处理队列中的Item

第二个Project中，有两个相关的activity，**Get transaction item**和**Set transaction status**，前者从queue中获取Item，后者通知Orchestrator这个特定的Transaction Item是否成功处理了。

1. Studio中，新建一个sequence，命名为ProcessTransactions
2. 将Get Transaction Item activity添加进去，将之前的queue名填入QueueName字段
3. 在TransactionItem字段中，按下Ctrl + K创建一个Transaction Item，命名为TransactionItem

运行上面的Workflow后，可以看到orchestrator中，queue1中有transaction的Status从New变成了In Progress。

上面的步骤只是取出了队列中的Item，还没有处理。

1. 添加两个Assign activity，分别用来接收上面TransactionItem中的两个值。
2. Assign中赋值：`Income = cint(TransactionItem.SpecificContent(“Income”))`，这里Income和Payment作为两个新增的变量，Type为Int32
3. 再添加一个activity：Set Transaction Status，其字段TransactionItem，设置为之前新增的变量`TransactionItem`。
4. 运行上面的Workflow，在Orchestrator中该Item变成了successful。

![image](https://user-images.githubusercontent.com/18595935/57224759-5ef9e300-7045-11e9-8b2e-62b1bd0e8bb4.png)

另外，上面将Status设置为了successfull，也可以设置为Failed，ErrorType设置为Business，Reason设置为`“The field cannot be identified.”`。

重新运行后，Orchestrator中也能出现Failed的项目。

同样，也可以设ErrorType为Application，重新运行后，在Queues的APP EXCEPTIONS中会发现次数增加了。查看其details，可以比较其retry次数，发现business没有retry，而application形式的有retry：

![image](https://user-images.githubusercontent.com/18595935/57226104-23611800-7049-11e9-9b73-1b10db3a5671.png)

最后，如果一个以Application Exception失败了多次(Queue定义时的Max of retries)后，上面的 “In Review”, “Retry Items”, “Mark as verified” , “Assign Reviewer” 这些Button就变成激活状态，reviewers就能手动处理：
1. 选择 Retry Items的话，能将该Item放回队列稍后再处理。
2. 选择 In Review，是告诉别的用户你正在review这个item
3. reviewer可以通过已有的Orchestrator Users指定。

### 3. Input and Output Arguments Practice

1. 创建一个新的Project，命名`CheckFileSize`，定义两个Argument，一个in和一个out，分别为`in_File`和`out_Size`
2. 在Try...Catch中添加两个Assign
3. 使用第一个Assign获取文件size，新建一个变量，类型为System.Double,`SizeInBytes = new System.IO.FileInfo(in_File).Length`,其中`in_File`是上面的in argument
4. 第二个Assign Activity用于存储output，将前面的size转换为kb形式，`out_Size = (SizeInBytes / 1024).ToString + "KB"`
5. 在Catch中捕获`System.IO.IOException`，以防输入文件不存在，对out argument赋值，提示说文件不存在。

最后将该Project发布到Orchestrator上，生成一个Process，启动一个job(使用一个Project folder中存在的文件)，结束后，check其输出的size。

其Workflow如下：

![image](https://user-images.githubusercontent.com/18595935/57228817-ac7b4d80-704f-11e9-8500-159befd35882.png)

运行后如下，如果文件名不存在，会触发异常；如果文件名存在，会输出文件size：

![image](https://user-images.githubusercontent.com/18595935/57229026-1c89d380-7050-11e9-84ea-2fe4cd1327ae.png)


# 4. 修了证明

![image](https://user-images.githubusercontent.com/18595935/57172085-3cee3e00-6e56-11e9-85f6-dbf6e2140093.png)


