---
layout: post
title: PythonSample-01-控制结构/eval函数
date: 2017-08-16 22:45:59
categories: Python
tags: 北理 Python
---
* content
{:toc}

> [PythonSample-XX...]系列,记录平常做的一些python范例程序。
> 作为自己以后工作时的参考信息。参考[**Python语言程序设计 嵩天@北京理工**](http://www.icourse163.org/learn/BIT-268001?tid=1002001005)

# 1. eval函数
eval()函数十分强大，官方demo解释为：将字符串str当成有效的表达式来求值并返回计算结果。
例如

```python
>>> a,b,c = eval(input("please input(a,b,c):"))
please input(a,b,c):1,2,3
>>> print("{},{},{}".format(a,b,c))
1,2,3
```
上面的代码等价于 `a,b,c = 1,2,3`，因为eval将用户输入的字符串当做了表达式。
如果上面不使用eval会是如何：

```python
>>> a,b,c = input("please input(a,b,c):")
please input(a,b,c):1,2,3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b,c = input("please input(a,b,c):")
ValueError: too many values to unpack (expected 3)
```
上面的代码等价于 `a,b,c = "1,2,3"`,显然会出错。

再看另一个例子：

```python
>>> a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
>>> b = eval(a)
>>> print("{}".format(a))
[[1,2], [3,4], [5,6], [7,8], [9,0]]
>>> print("{}".format(b))
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
>>> print("{},{}".format(type(a),type(b)))
<class 'str'>,<class 'list'>
```
`b=eval(a)`时，将a中引号内的部分作为表达式，赋值给b，那么b最终是list即列表，而a是字符串。

1. **eval函数非常方便，能够将用户输入作为代码接收进来并执行，还可以将代码写入文本，读入后动态执行。**
2. **方便的反面就是安全性，如果用户输入恶意代码并执行的话，会造成安全性问题。**

## 1.1 与此类似的exec()函数
eval只能计算单个表达式的值，而exec可以动态执行代码段，另外exec没有返回值**，如下

```python
def func():
    y = 20
    a = exec('2*y')
    print('a: ', a)

    a1 = eval('1.5*y')
    print('a1: ', a1)    

    exec("A=1;B=A+2;print(\"{},{}\".format(A,B))")

func()
```
输出结果为:

```
a:  None
a1:  30
1,3
```
上面程序说明：
1. exec 函数没有返回值，而eval有返回值
2. exec可以执行多段表达式

# 2. 异常处理
与其他程序类似，实例如下：

```python
import math
def main():
    try:
        number1,number2=eval(input("Enter the two number,separated by a comma  :"))
        result = number1 / number2

    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("A comma may be missing!")
    except:
        print("Something wrong!")
    else:
        print("No exception,the reslut is ",result)
    finally:
        print("Over!")

main()
```

输出结果如下：

```python
Enter the two number,separated by a comma  :1 3
A comma may be missing!
Over!

========= RESTART: C:\Users\legendcos\Desktop\python-study\052701.py =========
>>>
Enter the two number,separated by a comma  :1,0
Division by zero!
Over!

========= RESTART: C:\Users\legendcos\Desktop\python-study\052701.py =========
Enter the two number,separated by a comma  :1,2
No exception,the reslut is  0.5
Over!

```

# 3. 交互式循环

```python
def main():
    sum = 0.0
    count = 0
    xStr = input("Enter a number(<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number(<Enter> to quit) >> ")

    print("\n The average of the numbers is: ",sum / count)

main()
```
一直接受用户输入，直到直接输入enter

# 4. 文件循环

```python
def main():
    fileName = input("what file are the numbers in：\n")
    infile = open(fileName,'r')
    sum = 0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\n The average of the numbers is: ",sum / count)
main()
```

执行结果如下：

```pycon
what file are the numbers in：
h:\data.txt

 The average of the numbers is:  4.111111111111111
>>>
```

也可以使用 readline()函数，如下：

```python
def main():
    fileName = input("what file are the numbers in：\n")
    infile = open(fileName,'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print("\n The average of the numbers is: ",sum / count)
main()

```

上面的输入文件中，每行只有一个数字，如果每行有多个数字，而且以「，」分割，则需要嵌套循环，改进后代码如下：

```python
def main():
    fileName = input("what file are the numbers in：\n")
    infile = open(fileName,'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\n The average of the numbers is: ",sum / count)
main()

```

# 5. 死循环
在python中我们可以利用死循环完成特定功能

```python
while True:
    try:
        x = int(input("please enter a number:"))
        break
    except ValueError:
        print("oh,that wa no valid number,Try again..")
```
程序直到输入数字才退出break


# 参照:
1. 关于format的使用方法，参照 [here](http://qiita.com/utanesuke/items/8f31753a353195da1a0f)
