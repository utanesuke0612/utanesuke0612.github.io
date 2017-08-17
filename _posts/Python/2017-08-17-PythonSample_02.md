---
layout: post
title: PythonSample-02-数据类型及操作
date: 2017-08-16 22:45:59
categories: Python
tags: PythonSample 北理
---
* content
{:toc}

> [PythonSample-XX...]系列,记录平常做的一些python范例程序。
> 作为自己以后工作时的参考信息。参考[**Python语言程序设计 嵩天@北京理工**](http://www.icourse163.org/learn/BIT-268001?tid=1002001005)

# 1. 练习程序

## 1.1 例1 接受用户输入
```python
n = input("输入N：")
sum = 0
for i in range(int(n)):
    sum += i + 1
print("1到N 求和结果:",sum)
```
## 1.2 例2  格式化输出 乘法口诀表
```python
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end=' ')
    print(' ')
```

## 1.3 例3 图形化程序
```python
import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
```
输出如下:

<img src="https://qiita-image-store.s3.amazonaws.com/0/177240/ec747cb1-75a8-fb29-113a-012f38975e0c.png" width=30%>


# 2. 例:温度转换程序
```python
val = input("please input the temprature(eg:32C):")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("after the conversion: %.2fF"%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("after the conversion: %.2fC"%c)
else:
    print("input error!!")
```

```python
>>> t="abcdefg"
>>> t[3]
'd'
>>> t[-3]
'e'
>>> t[1:3]
'bc'
>>> t[1:-3]
'bcd'
>>> "python" + ":" + t[0:3]
'python:abc'

```

上面的程序解析：
1. 若字符长度为7，则第一位索引为0或-7，最后一位索引为6或-1
2. 通过方括号取区间时，右边是非包含的。如t[1:3]，表示一个从[0,3)的区间
3. 通过 + 可以实现字符串连接
4. 上面的val[0:-1]，表示取除了最后一位以外的字符

# 3. 利用turtle库画蟒蛇，分段着色
```python
#分段分颜色画
import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        if(i%2 == 0):
            turtle.pencolor("blue")
        else:
            turtle.pencolor("red")
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rd)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()
```

![image](https://qiita-image-store.s3.amazonaws.com/0/177240/fb6e01e0-a849-9926-33da-b06b407921aa.png)

1. setup启动图形窗口，左上角为0,0原点
2. pensize设置运动轨迹宽度
3. seth 设定运动时的轨迹方向
4. `import turtle` 方式，但是使用时需要turtle.XX()
5. `from turtle import *`，可以直接使用该库的函数 XX()
6. 拓展，用turtle库画一个三角形，代码如下(seth(0) 水平向右，是0度。fd指画线)：

```python
#画三角形
import turtle
def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 2
    turtle.pensize(pythonsize)

    turtle.seth(0)
    turtle.fd(90)

    turtle.seth(120)
    turtle.fd(90)

    turtle.seth(240)
    turtle.fd(90)

main()

```
![image](https://qiita-image-store.s3.amazonaws.com/0/177240/82b20c17-4b79-94b7-5c21-4c81f83b0dc7.png)


# 4. 数据类型
本课程主要讲解如下6种Python语言类型：

- 数字 与 字符串类型
- 元组 与 列表类型
- 文件 与 字典类型

## 4.1 数字类型
1. 整数类型（0x9a / 0X9a ，0x开头16进制，0b开头2进制，0o开头8进制）
2. 浮点数类型（如0.0, -2.17, 96e4, 9.6E5）,浮点数精度与系统相关，使用`import sys`和`sys.float_info`，确定当前精度：
3. 复数类型（z = a + bj,a是实数，b是虚数部分，a和b都是浮点类型，虚数部分用j标识。如 -5.6+7j 。z.real获取实数部分，z.imag获取虚数部分）
4. 上面三种可以互相转换（int() / float() / complex()）, 如 complex(4) = 4 + 0j
5. 整数 -》浮点数 -》复数，不同类型进行计算时，取右边的类型
6. type(z)可以获取数据的类型。
7. 常用运算符和运算函数如下:

 ![image](https://qiita-image-store.s3.amazonaws.com/0/177240/66b2986f-9a2a-6274-9c0e-e9cd20386031.png)


## 4.2 字符串类型
1. 用双引号或单引号
2. 转义符为 \ ，如comment中代码 ,如 `print("\"hello\"")` 输出:"hello" 。
3. 用索引可以访问字符串中特定的位置，关于索引操作，可以参考Page3中的讲解
4. 除了 ＋号可以进行字符串连接外，还可以用 ＊进行字符串的复制
5. len函数返回字符串长度
6. 大多数数据类型，都可以通过 str()转换为字符串
7. 常用字符串操作函数有

 ![image](https://qiita-image-store.s3.amazonaws.com/0/177240/f30d409d-ae3d-c9dd-b237-0442f9c4716e.png)

8. 示例代码：

```python
#将字符串拆开逐行输出
str="hell,world"
for i in str:
    print(i + "\n")
print("end")

---
>>> print("Hello\nWorld\n")
Hello
World
```

## 4.3 元组类型(tuple)
>元组因为不可变，所以更安全

**元组的概念：**
1. 元组是包含多个元素的类型，用逗号分隔。如 t1 = 1,2,3,"hello"
2. 元组可以为空，t2=()
3. 元组外侧可以用（）也可以不用
4. 一个元组也可以作为另一个元组的元素。

**元组的特点：**
1. 元组元素存在先后关系，通过索引可以访问，如t1[0]。
2. 元组定义后不能更改，也不能删除。如t1[0] = “hel”，会出错：
   TypeError: 'tuple' object does not support item assignment
3. 与字符串一样，元组之间也可以＋和＊号进行运算。

## 4.4 列表类型[list]
**列表的概念：**
1. 列表与元组一样，元素类型可以不一样，
2. 顺序集合可以索引。
3. 但是与元组不同，列表大小无限制，可以随时修改列表有些基本操作，与字符串操作类似。

![](https://qiita-image-store.s3.amazonaws.com/0/177240/b5fcc158-961b-ce45-c081-14601e79a876.png)
![](https://qiita-image-store.s3.amazonaws.com/0/177240/ac1037a6-880d-a8e4-fb6c-9e409eabb423.png)

# 5. math库与random库

## 5.1 math库
![](https://qiita-image-store.s3.amazonaws.com/0/177240/c148a4d3-050f-a0c8-12b6-0523e3ec2619.png)

![](https://qiita-image-store.s3.amazonaws.com/0/177240/045f2c11-9d23-ef7a-36e5-dc377248e75e.png)

## 5.2 random库

![](https://qiita-image-store.s3.amazonaws.com/0/177240/9f3c1b06-2254-d213-1d79-81c6bcd7b9f7.png)

```python
>>> from random import *
>>> seed(2)
>>> uniform(1,10)
9.604308447003245
>>> uniform(1,10)
9.530447383534144
>>> uniform(1,10)
1.5089623095412783
>>> seed(2)
>>> uniform(1,10)
9.604308447003245
>>> uniform(1,10)
9.530447383534144
>>> uniform(1,10)
1.5089623095412783
```
上面设定了随机种子后，每次生成的随机数序列都是一样的。
因为计算机是一个确定设备，不能生成真正的随机数，每次都是由一个种子开始的伪随机序列。
如果不设定的话，seed()函数随机种子是系统时钟。

# 6.PI的计算（蒙特卡洛Monte Carlo方法）
圆周率PI是个无理数，没有公式可以精确计算，PI的计算只能近似算法。
随机向单位正方形和圆结构抛洒大量点，对于每个点， 可能在圆内或者圆外，当随机抛点数量达到一定程度， 圆内点将构成圆的面积，全部抛点将构成矩形面积。圆 内点数除以圆外点数就是面积之比，即π/4。随机点数 量越大，得到的π值越精确。

```python
from random import random
from math import sqrt
from time import clock
DARTS = 1200000
hits = 0
clock()
for i in range(1,DARTS):
    x,y = random(),random()
    dist = sqrt(x**2 + y**2)
    if dist <=1.0:
        hits = hits + 1
pi = 4 *(hits/DARTS)
print("pi的值是 %s"%pi)
print("程序运行时间 %-5.5ss"%clock())

```
输出结果为:
>pi的值是 3.14148
>程序运行时间 2.655s

**注意：**

1. `x,y = random(),random()`,可以给两个赋值。
2. 同步赋值：例如交换 x 和 y的值，一般方法要使用临时变量t，在python 中直接如下方式交换：`x,y = y,x`,解析实例图：

 ![image](https://qiita-image-store.s3.amazonaws.com/0/177240/3ada275c-31b6-2085-da17-60247cac4fb7.png)
