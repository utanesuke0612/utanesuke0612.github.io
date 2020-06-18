---
layout: post
title: 使用C#编写UiPath中的Activity
date: 2020-06-18 01:01:01
categories: RPA
tags: RPA
---
* content
{:toc}

关于如何在C#中编写Custom Acitivity，虽然在这里[Creating a Custom Activity
](https://docs.uipath.com/activities/docs/creating-a-custom-activity)有非常详尽的描述，但自己再将作成过程记录一次的话，印象更深。

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