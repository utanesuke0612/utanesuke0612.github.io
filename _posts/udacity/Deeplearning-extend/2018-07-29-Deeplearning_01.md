---
layout: post
title: 深度学习入门-01-Python入门
date: 2018-07-28 00:00:01
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

# 1. 书籍简介

![image](https://user-images.githubusercontent.com/18595935/43462387-ec953504-9510-11e8-84f4-9fd29b99e0aa.png)


# 2. python解释器

可以参考:
> [廖雪峰python教程-笔记](http://road2ai.info/tag/#%E5%BB%96%E9%9B%AA%E5%B3%B0%E6%95%99%E7%A8%8B-ref)
> 

```python
#列表
print("1.列表")
a = [2,4,6,8]
print(a[0:2])
print(a[2:])
print(a[:-1])

#字典
print("\n2.字典")
me = {"age":18}
print(me["age"])
me["name"] = "lijun"
print(me)

#类
print("\n3.类")

class Man:
    def __init__(self,name):
        self.name = name
        print("created")
    
    def hello(self):
        print("hello," + self.name +" !")


m = Man("David")
m.hello()
```

输出如下:

```python
1.列表
[2, 4]
[6, 8]
[2, 4, 6]

2.字典
18
{'name': 'lijun', 'age': 18}

3.类
created
hello,David !
```

# 3. Numpy

```python

import numpy as np

x = np.array([1,2,3])
print(x)
print(type(x))

#算数运算
print("\n1.算数运算")
y = np.array([3,4,5])
print(x+y)

#N维数组
print("\n2.N维数组")
A = np.array([[1,2],[3,4]])
print(A.shape)
#查看矩阵元素的数据类型
print(A.dtype)

B = np.array([[3,1],[0,4]])
print("\nA*B(维度相同，对应位置直接相乘):")
print(A*B)

#广播
print("\n3.广播")
C = np.array([10,20])
print("\nB*C(维度不同，广播后相乘):")
print(B*C)

#获取元素
print("\n4.获取元素")
print(B[1][0])
for row in B:
    print(row)

print( B[B>0])
```

输出如下:

```python
[1 2 3]
<class 'numpy.ndarray'>

1.算数运算
[4 6 8]

2.N维数组
(2, 2)
int32

A*B(维度相同，对应位置直接相乘):
[[ 3  2]
 [ 0 16]]

3.广播

B*C(维度不同，广播后相乘):
[[30 20]
 [ 0 80]]

4.获取元素
0
[3 1]
[0 4]
[3 1 4]
```

- 广播:

![image](https://user-images.githubusercontent.com/18595935/43466403-6aa349fa-951a-11e8-988d-8be9f182eb45.png)



# 4. Matplotlib

- 基础作图

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0,6,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43468576-579b57b2-951f-11e8-9dec-9ba794bf96bd.png)

- 两图叠加


```python
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle = "--",label="cos")
plt.xlabel("x")
plt.ylabel("y")

plt.title("sin&cos")
plt.legend()
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43468591-61309a62-951f-11e8-8912-3f7af8b0702b.png)

- 显示图像

```python
from matplotlib.image import imread

img = imread("uta.jpg")
plt.imshow(img)

plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43468605-66265444-951f-11e8-8f00-596293163d49.png)
