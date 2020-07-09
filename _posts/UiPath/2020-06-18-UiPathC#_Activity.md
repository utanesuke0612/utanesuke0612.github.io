---
layout: post
title: 使用C#编写UiPath中的Activity
date: 2020-06-18 01:01:01
categories: RPA
tags: RPA
---
* content
{:toc}

1. 关于如何在C#中编写Custom Acitivity，虽然在这里[Creating a Custom Activity
](https://docs.uipath.com/activities/docs/creating-a-custom-activity)有非常详尽的描述，但自己再将作成过程记录一次的话，印象更深。
2. [UiPath Studioで使用するカスタムアクティビティの作成方法](https://qiita.com/masatomix/items/1f63513e80313a99faeb)

# 1. 使用的工具

- [Microsoft Visual Studio](https://visualstudio.microsoft.com/ja/) 
- [NuGet Package Explorer](https://github.com/NuGetPackageExplorer/NuGetPackageExplorer/releases)

# 2. 在C#中编写dll

- 创建dll用的工程:

![image](https://user-images.githubusercontent.com/18595935/84987203-b4764e00-b17a-11ea-86ac-d693ee933a61.png)

- 添加依赖关系:

![image](https://user-images.githubusercontent.com/18595935/84987277-d1128600-b17a-11ea-91d4-4a3cbc815945.png)

- 追加对应代码:

注意添加了新的using：`using System.Activities;`和`using System.ComponentModel;`

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Activities;
using System.ComponentModel;

    namespace ClassMathCustomActivity
{
    public class SimpleFormula : CodeActivity
    {
        [Category("Input")]
        [RequiredArgument]
        public InArgument<double> FirstNumber { get; set; }

        [Category("Input")]
        public InArgument<double> SecondNumber { get; set; }

        [Category("Output")]
        public OutArgument<double> ResultNumber { get; set; }

        protected override void Execute(CodeActivityContext context)
        {
            var firstNumber = FirstNumber.Get(context);
            var secondNumber = SecondNumber.Get(context);
            var result = System.Math.Pow(firstNumber + secondNumber, 2);
            ResultNumber.Set(context, result);
        }
    }
}
```

- 编译成dll文件：

![image](https://user-images.githubusercontent.com/18595935/84987551-54cc7280-b17b-11ea-912c-510c96353ad9.png)

可以在对应目录中找到dll文件。

# 3. 创建NuGet Package

- 启动NuGet Package Explorer，创建新的包

![image](https://user-images.githubusercontent.com/18595935/84987677-92c99680-b17b-11ea-8cff-426e8048ad50.png)

- 将dll添加到Nuget Package中：

![image](https://user-images.githubusercontent.com/18595935/84988034-3c108c80-b17c-11ea-9cdf-3b14865a9b80.png)


- 最后`File -> Save as...`，既可以保存为`nupkg`文件了。

# 4. 在UiPath中使用该Activity

![image](https://user-images.githubusercontent.com/18595935/84990097-9bbc6700-b17f-11ea-8ca8-b0980f5c45f4.png)

# 5. 使用Activity Creator

使用 [Activity Creator](https://connect.uipath.com/ja/marketplace/components/activity-set-creator)能更快的创建自定义Activity。
参考使用方法：[DEMO: Build custom activities in minutes with the UiPath Activity Creator](https://www.youtube.com/watch?time_continue=43&v=p8GrdJHwHPw&feature=emb_logo)

- **在Visual Studio 2019中安装：**

注意：在2019之前的版本中不能使用。

![image](https://user-images.githubusercontent.com/18595935/87009889-c50d6780-c200-11ea-9e2c-299307fce577.png)

- **安装完毕后，启动Visual Studio，创建一个Uipath Activity Project:**

![image](https://user-images.githubusercontent.com/18595935/87010193-2f260c80-c201-11ea-968d-f80c06b4129e.png)

- **创建一个Project后，通过Extension的UiPath可以追加Activities：**

![image](https://user-images.githubusercontent.com/18595935/87010707-eae73c00-c201-11ea-874e-8c79f8465f54.png)

- **创建Activity完毕后，publish：**

![image](https://user-images.githubusercontent.com/18595935/87013215-423adb80-c205-11ea-8984-9cb41ff8f36e.png)

- **导入后，在UiPath中结果如下：**

![image](https://user-images.githubusercontent.com/18595935/87013690-02282880-c206-11ea-8d78-c4483e869875.png)

这个Extension做得很强大，更多功能等着去挖掘！

