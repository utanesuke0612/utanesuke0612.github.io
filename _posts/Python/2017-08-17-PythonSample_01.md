---
layout: post
title: C#入门经典第1章至第5章
date: 2020-03-27 01:01:01
categories: CSharp
tags: CSharp
---
* content
{:toc}

> 工作关系有很多地方需要用到C#，需要系统学习下，所幸自己有C++和java基础，粗看了一遍教材，很多概念都是相通的，比如虚拟函数，匿名函数，Lambda函数等。
> 不过现在这些程序语言中加入了很多新的概念，比如LINQ。
> 这本书完毕后，开始学习那本C#的AI教程。

![image](https://user-images.githubusercontent.com/18595935/77747631-572e9d00-7062-11ea-828e-3f8b24514b32.png)

关于本书：
1. 本书介绍C#基础OOP语言，桌面编程，云编程，数据源的使用，以及新的高级技术。
2. OOP语言(01-13章)
   1. C#与.NET关系
   2. C#语法
   3. 变量，流程控制，数组等高级变量类型，函数
   4. 使用C#语言调试应用程序
   5. 面向对象编程
   6. 实践
   7. 类的成员
   8. 第11章开始，介绍常见OOP场景，包括处理对象集合，比较和转换对象
   9. 泛型，利用它可以创建非常灵活的类
   10. 其他技术，比如事件
3. Windows桌面编程(14-15章)
   1. 关注如何使用WPF以图形方式构建桌面应用程序。
   2. 在应用程序中如何使用.NET Framework提供的丰富控件。
4. 云编程(16-17章)
   1. 什么是云编程，再讨论云优化堆栈。
   2. 学习如何创建ASP.NET Web API，并部署到云中。
5. 数据访问
   1. 介绍应用程序如何将数据保存到磁盘，检索数据，压缩数据，监视和处理文件系统变化。
   2. 学习数据交换的事实标准XML，以及JSON格式。
   3. 介绍LINQ，以及使用LINQ访问数据库和其他数据。
6. 其他技术
   1. 简要介绍Windows Communication Foundation
   2. 创建通用的windows应用程序

> 光是列举完毕上面的章节名，就很兴奋，看来自己还是喜欢做这些具体的技术性工作。

在学习本书时：
1. 将C#中的概念与C++/Python/Java的进行对比，这样更容易理解，了解设计者思路。
2. 所有书上的示例代码，都要自己手动输入，加深印象。

# 1. C#简介

- 什么是.NET Framework
- .NET 应用程序的工作原理
- C#概念与.NET Framework的关系
- 用C#创建.NET 应用程序的工具

下面这幅图很好的总结了C#与.NET Framework的关系：

![image](https://user-images.githubusercontent.com/18595935/77757332-6585b480-7074-11ea-9ef3-002fcc2218bc.png)

下面是Java与JVM的关系图，作为对比：

![image](https://user-images.githubusercontent.com/18595935/77757596-d3ca7700-7074-11ea-945c-ddbf7c858eae.png)

下面是直接的对比图，比较直观：

![image](https://user-images.githubusercontent.com/18595935/77757820-3e7bb280-7075-11ea-891b-41d02d07ce53.png)

## 1.1 .NET Framework的含义

上图中.NET Framework的Microsoft版本运行在WindowsOS上，但也有运行在其他OS，比如Mono，是.NET Framwork的开源版本，可以在Linux版本和MacOS上运行。

为了执行C#代码，必须把他们转换成OS能理解的语言，即Native Code，这种转换由编译器执行，称为编译代码，.NET中分为两个阶段。

- **CIL和JIT**

1. 通过开发工具，将代码编译为通用中间语言，CIL代码
2. 再通过Just In Time(JIT)编译器，把CIL编译为专用于OS的Native Code。这个编译在应用程序运行过程中动态发生。

- **托管代码**

在将C#转换为Native Code后，还需要CLR进行执行，类似于Java的JVM，即虚拟机。

- **垃圾回收**

托管代码中最重要的一个功能是垃圾回收，.NET垃圾回收会定期检查计算机内存，从中删除不需要的内容。

整理一下上面的过程：

![image](https://user-images.githubusercontent.com/18595935/77762888-8c94b400-707d-11ea-8937-9d57799065ee.png)

## 1.2 C#的含义

用C#可以编写什么样的应用程序：

- 桌面应用程序，使用WPF模块构建WindowsUI
- Windows Store应用程序，主要针对触摸设备，全屏运行，界面简洁
- WebAPI，建立REST风格的HTTP服务框架
- WCF服务，创建各种分布式应用程序的方式

# 2. 编写C#程序

- 控制台程序

File -> New -> Project -> Console App 创建：

```C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            // The code provided will print ‘Hello World’ to the console.
            // Press Ctrl+F5 (or go to Debug > Start Without Debugging) to run your app.
            Console.WriteLine("Hello World!");
            Console.ReadKey();

            // Go to http://aka.ms/dotnet-get-started-console to continue learning how to build a console app! 
        }
    }
}
```

- 桌面程序

File -> New -> Project -> WFP App 创建，然后在界面添加一个button，双击button，填写MessageBox的代码后，

```C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp2
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Hello, World!!");
        }
    }
}
```

# 3. 变量和表达式

# 4. 流程控制

# 5. 变量的更多内容

# 6. 总结




