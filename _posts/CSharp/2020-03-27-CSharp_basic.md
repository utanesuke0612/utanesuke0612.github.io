---
layout: post
title: C#入门
date: 2020-05-27 01:01:01
categories: CSharp
tags: CSharp
---
* content
{:toc}

> 工作关系有很多地方需要用到C#，需要系统学习下，所幸自己有C++和java基础，粗看了一遍教材，很多概念都是相通的，比如虚拟函数，匿名函数，Lambda函数等。
> 不过现在这些程序语言中加入了很多新的概念，比如LINQ。
> 这本书完毕后，开始学习那本C#的AI教程。

参考[西安交大-C#程序设计](https://www.icourse163.org/course/XJTU-1002843011)

这个网课的笔记参考如下：[C#程序设(中国MooC-西安交大)](https://docs.google.com/document/d/e/2PACX-1vRBgyKBjiv9IfBHRce-F2ukduRhgch2iPFf4lwGd5ACqw2sM3cS-KKshywygyeSLlyanr30rLj1QhVx/pub)

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

```csharp
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

```csharp
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

本章快速跳过，语法与既有语言都是一样的，抽出记录一些自己印象不深的部分。

1. 注释方法，`/* */ `多段注释，`//`单行注释，`///`单行注释用于创建文档。
2. 区分大小写
3. `#region .... #endregion`关键字用来定义可以展开和折叠的代码区域。
4. 以`#`开头的任意关键字实际上是一个预处理指令，严格说并不是C#关键字。
5. 常见整数类型：`sbyte -> byte -> short -> ushort -> int -> uint -> long -> ulong`
6. 常见浮点类型：`float -> double -> decimal`
7. 文本和布尔类型：`char -> bool -> string`, char是Unicode字符，存储0到65535之间整数，bool是true和false，string一组字符，数量没有上限，可变大小的内存。
8. 通过转义字符，可以在文本中输出特殊字符，如果使用`@`，比如`Console.WriteLine(@"C:\Temp\Hello");`与`Console.WriteLine("C:\\Temp\\Hello");`一样。
9. 字符串是引用类型，字符串也可以被赋予null值，表示字符串变量不引用字符串。
10. 以using关键字开头的，声明C#代码中使用System等名称空间，他们可以在该文件的所有名称控件中访问。
11. 另外，C#6中新增了using static关键字，这个关键字允许静态成员直接包含到C#，比如`using static System.Console`添加到名称空间列表中时，访问WriteLine()方法时就不需要再前面加静态类名`Console`了。

- 示例代码1：

> 注意下面的转义字符

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int myInteger;
            string myString;

            myInteger = 18;
            myString = "\"myInteger\" is  ";
            Console.WriteLine($"{myString}{myInteger}");

            Console.ReadKey();
        }
    }
}
```

输出：

```
"myInteger" is  18
```

- 转义序列：

![image](https://user-images.githubusercontent.com/18595935/77811609-d5c92000-70de-11ea-9d62-2e7dd7c5b4c4.png)

- 简单的数学运算符

![image](https://user-images.githubusercontent.com/18595935/77811830-7ff57780-70e0-11ea-85c9-c077f85768c9.png)

- 简单的表达式

![image](https://user-images.githubusercontent.com/18595935/77811884-de225a80-70e0-11ea-9d8d-2597a3449ebe.png)

- 用户输入与类型转换：

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string userName;
            Console.WriteLine("Please enter your name:");
            userName = Console.ReadLine();
            Console.WriteLine($"Welecome {userName}!!");

            double firstNumber;
            Console.WriteLine("Now give me another Number:");
            firstNumber = Convert.ToDouble(Console.ReadLine());
            Console.ReadKey();
        }
    }
}

```

- 赋值运算符

![image](https://user-images.githubusercontent.com/18595935/77811903-0b6f0880-70e1-11ea-83a1-3158ec21a908.png)

- 运算符优先级

![image](https://user-images.githubusercontent.com/18595935/77811924-26417d00-70e1-11ea-8c3e-baced44e1a70.png)


# 4. 流程控制

本章也快速跳过！

1. 条件布尔运算，`&&`都是true则true，`||`一个是true则true
2. 三元运算符 `string resultString = (5 < 10) ? "utasuke" : "utane";`
3. if, switch 选择
4. 循环，`do {} while()`以及`while () {}`, for循环，`for(int i=1;i<=10;i++) {}`
5. 循环中断，`break`立即终止,`continue`终止当前进行下一次循环，`return`跳出循环以及包含该循环的函数。
6. 无限循环 `while (true) {}`

# 5. 变量的更多内容

主要包含：
- 类型的显式和隐式转换
- 创建使用，枚举类型，结构类型，数组
- 如何处理字符串值

1. 显式转换，要求编译器把数值从一种数据类型转换为另一种数据类型。
2. 使用Convert命令进行显式转换，比如`Convert.ToString(doubleVal)`。
3. 枚举，运行一个类型，取值范围是给定的集合，枚举中的数据类型都是基本类型，也只能一个。
4. 结构，struct，这样更加类似于class了，由几个数据组成的数据结构，能有不同的类型。
5. 数组定义： `int[] myIntArray = {1,2,3,4,5}`或是`int[] myIntArray = new int[5]`
6. foreach循环，这个就跟uipath中的foreach繰り返し一样
7. string类似一个类，有很多成员函数，比如`ToLower()`,`Trim()`等

- 参考：隐式数值变换：
> 即可以像正常赋值一样的操作

![image](https://user-images.githubusercontent.com/18595935/77812943-4cb6e680-70e8-11ea-9a66-b09b8935472c.png)

- 枚举示例代码与类型转换
> 枚举类似于一个新定义的数据类型，类似类名

```csharp
namespace ConsoleApp1
{
    enum orientation : byte {
        north = 1,
        south = 2,
        east = 3,
        west =4
    }
    class Program
    {
        static void Main(string[] args)
        {
            orientation myDirection = orientation.north;
            Console.WriteLine($"myDirection =  {myDirection}  !!");
            Console.WriteLine($"myDirection =  {(byte)myDirection}  !!");
            Console.ReadKey();
        }
    }
}

```

输出如下：

```
myDirection =  north  !!
myDirection =  1  !!
```

- foreach循环

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] familyMembers = { "wangling", "junlee", "utane", "utasuke" };
            foreach (string name in familyMembers) {

                Console.WriteLine($"name:{name}");
            }
            Console.ReadKey();

        }
    }
}
```

# 6. 函数

本章主要内容：
1. 如何定义及使用，既不接收数据也不返回值的简单函数
2. 如何在函数传入传出数据
3. 使用变量作用域
4. 如何结合使用Main函数和命令行函数
5. 如何把函数提供为结构类型成员
6. 如何使用函数重载
7. 使用使用委托

除了第7以外的概念，都是理解的。

## 6.1 定义和使用函数

- 参数数组

C#运行指定给一个特殊参数，这个参数必须是函数定义的最后一个参数，称为参数数组，允许使用个数不定的参数调用数组，使用`params`关键字定义它们。
> Python中也有类似用法

```csharp
namespace ConsoleApp1
{
    class Program
    {

        static int Sumvals(params int[] vals)
        {
            int sum = 0;
            foreach (int val in vals)
            {
                sum += val;
            }
            return sum;
        }

        static void Main(string[] args)
        {
            int sum = Sumvals(1, 3, 4, 4);

            WriteLine($"Summed Values = {sum}");
            ReadKey();

        }
    }
}
```

上面代码中直接使用了WriteLine和Readkey，因为添加了`using static System.Console;`。

- 引用参数和值参数

使用参数时，通过引用传递参数，即函数处理的变量与函数调用中使用的变量相同，对这个变量进行的修改，会影响原来的参数，需要使用`ref`关键字来指定参数。

但是使用ref，必须有两个限制：
- 只能针对非常量，如果针对const变量，那是非法的。
- 必须使用初始化过的变量。

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static void ShowDouble(ref int val) {
            val *= 2;
            WriteLine($"val doubled = {val}");
        }
        static void Main(string[] args)
        {
            int sum = 5;
            WriteLine($"original = {sum}");
            ShowDouble(ref sum);
            ReadKey();
        }
    }
}
```

输出：
original = 5
val doubled = 10

- 输出参数

除了按引用传递值外，还可以使用out关键字，指定所给的参数时一个输出参数。但是与引用ref有下面的区别：
- 可以把未赋值的变量用作out参数
- 函数在会使用out参数时，必须把他看成未赋值。

即使把已赋值的变量用作out参数，但存储在该变量的值会在函数执行时丢失。
因为out的值，是用于输出的，所以原始值有与没有都无所谓。


示例代码：

```csharp
    class Program
    {
        static int MaxValue(int[] intArray, out int maxIndex) {
            int maxVal = intArray[0];
            maxIndex = 0;
            for (int i = 1; i < intArray.Length; i++) {
                if (intArray[i] > maxVal) {
                    maxVal = intArray[i];
                    maxIndex = i;
                }
            }
            return maxVal;
        }
        static void Main(string[] args)
        {
            int[] myArray = { 1, 2, 3, 4, 5, 3, 3, 3, 7, 1, 1 };
            int maxIndex;
            WriteLine($"Max is : {MaxValue(myArray,out maxIndex)}");
            WriteLine($"index is in : {maxIndex+1}");
            ReadKey();
        }
    }
}
```

输出如下：

```
Max is : 7
index is in : 9
```

注意：
- out的参数，必须在该函数中再次赋值，否则编译出错
- out参数可以放多个，用法一样。

## 6.2 变量作用域

- 局部变量：作用域覆盖一个函数的变量
- 全局变量：作用域覆盖多个函数的变量，必须使用static或const关键字来定义这种形式的全局变量，static可修改，const禁止修改变量的值。

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static string myString;

        static void Write() {
            string myString = "defined in write()";
            WriteLine("Now in Write()");
            WriteLine($"Local myString = {myString}");
            WriteLine($"Global myString = {Program.myString}");
            
        }

        static void Main(string[] args)
        {
            string myString = "define in Main()";
            Program.myString = "Global String";
            Write();

            WriteLine($"\n Now in Main()");
            Program.myString = "Global String2";
            WriteLine($"Local myString = {myString}");
            WriteLine($"Global myString = {Program.myString}");

            ReadKey();
        }
    }
}
```

输出：

```
Now in Write()
Local myString = defined in write()
Global myString = Global String

 Now in Main()
Local myString = define in Main()
Global myString = Global String2
```
- 如果将上面的static，修改为const，则会发生编译错误。
- 另外，可以看到`Program.myString`，通过类名来引用这个变量的，就是说这个变量是所有类共通的。


示例：

```csharp
    class Program
    {
        static void ShowDouble(ref int val) {

            val *= 2;
            WriteLine($"val doubled = {val}");
        }

        static void Main(string[] args)
        {
            int val = 5;
            WriteLine($"val = {val}");

            ShowDouble(ref val);

            WriteLine($"val = {val}");
            
            ReadKey();
        }
    }
```

输出：

```
val = 5
val doubled = 10
val = 10
```

通过下面的代码也可以得到同样的结果，一个是通过传入引用参数，一个是使用类的全局变量。

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static int val;
        static void ShowDouble()
        {
            val *= 2;
            WriteLine($"val doubled = {val}");
        }

        static void Main(string[] args)
        {
            val = 5;
            WriteLine($"val = {val}");

            ShowDouble();

            WriteLine($"val = {val}");

            ReadKey();
        }
    }
}
```

## 6.3 Main()函数

Main()是C#应用程序的入口点，可以返回void,int,有一个可选参数`string[] args`:

```
static void Main()
static void Main(string[] args)
static int Main()
static int Main(string[] args)
```

1. 一般情况下，返回0表示正常终止。
2. 可选参数args是从应用程序的外部接收信息的方法。

有两种方式可以设定外部接收信息：

- 在IDE工具studio中设定，项目属性页面，即Properties页面中，选择debug页面，在Command line arguments中设置命令行参数。

![image](https://user-images.githubusercontent.com/18595935/78467887-b2404e00-774c-11ea-9b3c-f8dc902ecc1a.png)

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine($"{args.Length}");
            foreach (string arg in args)
                WriteLine(arg);
            ReadKey();
        }
    }
}
```

输出如下：

```
4
hello
li utane
li utansuke
124
```

- 在项目输出所在的目录`\bin\debug`中打开命令提示窗口，输入如下代码，也可以得到同样的结果：

```
ConsoleApp1 hello "li utane" "li utansuke" 124
```

注意如果参数有空格，需要双引号将参数括起来。

## 6.4 结构函数

除了数据，结构中还可以包含函数，如下代码，定义了结构函数`Name()`:

```csharp
namespace ConsoleApp1
{
    struct CustomerName {
        public string firstname, lastname;
        public string Name() => firstname + " " + lastname;
    }
    class Program
    {
        static void Main(string[] args)
        {
            CustomerName myCustomer;
            myCustomer.firstname = "li";
            myCustomer.lastname = "utane";
            WriteLine(myCustomer.Name());

            ReadKey();
        }
    }
}
```

## 6.5 函数的重载

函数的重载与其他语言中概念一样，同一个函数名，但是包含的参数类型或个数不同，这样重载，比如如下的代码：

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static int MaxValue(int[] intArray)
        {
            int maxVal = intArray[0];
            for (int i = 1; i < intArray.Length; i++)
            {
                if (intArray[i] > maxVal)
                    maxVal = intArray[i];
            }
            return maxVal;
        }

        static double MaxValue(double[] doubleArray)
        {
            double maxVal = doubleArray[0];
            for (int i = 1; i < doubleArray.Length; i++)
            {
                if (doubleArray[i] > maxVal)
                    maxVal = doubleArray[i];
            }
            return maxVal;
        }
        static void Main(string[] args)
        {
            int[] myArray = { 1, 2, 3, 5, 3, 3, 33, 99 };
            int maxVal = MaxValue(myArray);
            WriteLine($"Max: is {maxVal}");
            
            double[] mydoubleArray = { 1.1, 2.1, 3.2, 5.2, 3.2, 3.2, 3.3, 19.24 };
            double maxdoubleVal = MaxValue(mydoubleArray);
            WriteLine($"Max: is {maxdoubleVal}");


            ReadKey();
        }
    }
}
```

```
Max: is 99
Max: is 19.24
```


## 6.6 委托

委托是一个比较新的概念，以前没有学习过，关于委托，更多介绍在第13章。

1. 委托delegate是一种存储函数引用的类型。
2. 委托最重要的用途在本书后面的事件和事件处理时使用。
3. 委托的声明非常类似于函数，但不带函数体，要使用`delegate`关键字，委托的声明指定了一个返回类型和一个参数列表。

```csharp
namespace ConsoleApp1
{
    class Program
    {
        delegate double ProcessDelegate(double param1, double param2);
        static double Multiply(double param1, double param2) => param1 * param2;
        static double Divide(double param1, double param2) => param1 / param2;

        static void Main(string[] args)
        {
            ProcessDelegate process;
            WriteLine("Enter 2 number separated with a comma:");
            string input = ReadLine();
            int commaPos = input.IndexOf(",");
            double param1 = Convert.ToDouble(input.Substring(0, commaPos));
            double param2 = Convert.ToDouble(input.Substring(commaPos + 1,
                input.Length - commaPos - 1));

            WriteLine("Enter M to multipy or D to divide:");
            input = ReadLine();

            if (input == "M")
                process = new ProcessDelegate(Multiply);
            else
                process = new ProcessDelegate(Divide);

            WriteLine($"Result : {process(param1, param2)}");

            ReadKey();

        }
    }
}
```

```csharp
Enter 2 number separated with a comma:
1,2.3
Enter M to multipy or D to divide:
D
Result : 0.434782608695652
```

```csharp

```

## 6.7 练习

- 使用两个命令行参数，分别把值放在字符串和整形变量中，然后显示这些值：

```csharp
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string myfirst = args[0];
            int myint = Convert.ToInt32(args[1]);
            WriteLine($"{myfirst} and {myint}");
            ReadKey();

        }
    }
}
```

- 创建一个委托，在请求用户输入时，使用它模拟Console.ReadLine()函数

```csharp
namespace ConsoleApp1
{
    class Program
    {
        delegate string ReadLineDelegate(); 

        static void Main(string[] args)
        {
            ReadLineDelegate readLine = new ReadLineDelegate(ReadLine);
            WriteLine("Type a string");

            string userInput = readLine();
            WriteLine($"You typed : {userInput}");

            ReadKey();

        }
    }
}
```

输出：

```
Type a string
没有
You typed : 没有
```

## 6.8 要点：

1. 函数的名称和参数统称为函数签名，名称相同但签名不同的多个函数，这称为函数重载。
2. 个数不定的特定类型参数，可以用参数数组指定，`params int[] args`，放在参数列表最后面。
3. 参数可以指定ref或out，以便给调用者返回值，调用函数时也必须包括对应的ref和out关键字。
4. 委托：除了直接调用函数外，还可以通过委托调用他们，具体见上面。

# 7. 总结(1-6)

各个章节要点总结如下：

![image](https://user-images.githubusercontent.com/18595935/77814756-73c8e480-70f7-11ea-8898-700f1c9c66a7.png)

![image](https://user-images.githubusercontent.com/18595935/77814746-5a279d00-70f7-11ea-8ba7-19f4b59277f9.png)

![image](https://user-images.githubusercontent.com/18595935/77814662-93134200-70f6-11ea-9769-3753340f0686.png)

![image](https://user-images.githubusercontent.com/18595935/77814555-66aaf600-70f5-11ea-832e-983edf3ed2c8.png)

![image](https://user-images.githubusercontent.com/18595935/77814539-3f542900-70f5-11ea-93cc-9f8e140a62dd.png)

