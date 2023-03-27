---
layout: post
title: Udacity-基础线性代数LinearAlgebra
date: 2018-03-22 00:02:00
categories: 数学
tags: 数学
---
* content
{:toc}

# 1. 向量

## 1.1 点和向量

点表示一个绝对位置，向量表示位置上的位移(大小和方向)

![image](https://user-images.githubusercontent.com/18595935/37912983-bec8d9e4-314e-11e8-86f2-fca736097d6b.png)

## 1.2 Vector 模块

1. `__init__`初始化程序，根据坐标轴列表输入创建向量，同时设定维度
2. `__str__`打印输出，定制该class的`print`函数
3. `__eq__`比较，定制该class的`==`号运算符

```python
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

# 调用了__init__构造函数
my_vector = Vector([1,2,3])
# 调用了__str__，用于打印输出
print(my_vector)

my_vector1 = Vector([1,2,3])
my_vector2 = Vector([1,2,-3])

# 调用了__eq__ 用于比较
print(my_vector1 == my_vector)
print(my_vector1 == my_vector2)
```

输出如下:

```python
Vector: (1, 2, 3)
True
False
```

## 1.3 向量运算

![image](https://user-images.githubusercontent.com/18595935/37971972-38d6158a-3212-11e8-9af2-22d0973b4d28.png)

## 1.4 练习:加减和标量乘法

- 在上面的示例中追加了三个成员函数，用于进行向量的加减和惩罚

```python
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    # 与myplus相同的功能
    def myplus2(self,v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def myplus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def myminus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)


    def mytimes(self,c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

my_vector1 = Vector([8.218,-9.341])
my_vector2 = Vector([-1.129,2.111])

print(my_vector1.myplus2(my_vector2))

my_vector3 = Vector([7.119,8.215])
my_vector4 = Vector([-8.223,0.878])

print(my_vector1.myminus(my_vector2))

my_vector5 = Vector([1.671,-1.012,-0.318])

print(my_vector5.mytimes(7.41))

```

- 输出结果

```
Vector: (7.089, -7.229999999999999)
Vector: (9.347, -11.452)
Vector: (12.38211, -7.49892, -2.35638)
```

- 关于zip函数

```python
>>> x = [1,2,3]
>>> y = [4,5,6]
>>> z = zip(x,y)
>>> z
[(1, 4), (2, 5), (3, 6)]

# 如果两个向量维度不同，结果是维度小的那个
>>> y1 = [4,5]
>>> z1 = zip(x,y1)
>>> z1
[(1, 4), (2, 5)]
```


## 1.5 大小(magnitude)和方向(direction)

![image](https://user-images.githubusercontent.com/18595935/37975113-8cad74c6-3219-11e8-983e-e45ace5229fa.png)

- `||V||`绿色部分表示向量的大小
- `u`表示是V的单位向量，即正规化后的向量，大小为1

1. A unit vector is a vector whose magnitude is 1. 单位向量其大小为1.
2. A vector's direction can be represented by a unit vector.
3. Normalization: process of finding a unit vector in the same direction as a given vector.

## 1.6 练习: 编写大小和方向函数

![image](https://user-images.githubusercontent.com/18595935/37976705-0d0a3624-321d-11e8-9bb8-e394435726bf.png)

左边是求解向量的大小，右边是计算其单位向量。

- 只举例了新增的函数(自己写的函数)

```python
from math import sqrt
... 

    def magnitude(self):
        magnitude = 0
        for i in range(len(self.coordinates)):
            magnitude += self.coordinates[i] * self.coordinates[i]

        return sqrt(magnitude)

    def norm(self):
        magnitude1 = self.magnitude()
        new_coordinates = [x/magnitude1 for x in self.coordinates]
        return Vector(new_coordinates)
```

- udacity的示例函数

```python
from math import sqrt
... 

    def magnitude2(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def norm2(self):
        try:
            magnitude = self.magnitude2()
            return self.mytimes(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector!")
```

- 使用上述函数:

```python
my_vector1 = Vector([-0.221,7.437])
print(my_vector1.magnitude())

my_vector2 = Vector([8.813,-1.331,-6.247])
print(my_vector2.magnitude())

my_vector3 = Vector([5.581,-2.136])
print(my_vector3.norm())

my_vector4 = Vector([1.996,3.108,-4.554])
print(my_vector4.norm())

print("------------------------")

my_vector1 = Vector([-0.221,7.437])
print(my_vector1.magnitude2())

my_vector2 = Vector([8.813,-1.331,-6.247])
print(my_vector2.magnitude2())

my_vector3 = Vector([5.581,-2.136])
print(my_vector3.norm2())

my_vector4 = Vector([1.996,3.108,-4.554])
print(my_vector4.norm2())
```

- 输出结果：

```python
7.44028292473
10.8841875673
Vector: (0.9339352140866403, -0.35744232526233)
Vector: (0.3404012959433014, 0.5300437012984873, -0.7766470449528028)
------------------------
7.44028292473
10.8841875673
Vector: (0.9339352140866403, -0.35744232526233)
Vector: (0.3404012959433014, 0.5300437012984873, -0.7766470449528029)
```

## 1.7 内积(Inner Products/Dot Products)

![image](https://user-images.githubusercontent.com/18595935/43036134-311713a6-8d36-11e8-8079-b0cd3fcb9782.png)

1. 默认小角度
2. 两个向量的内积，结果是一个标量
3. V和W的向量内积 = 向量V的大小 * 向量W的大小 * Cos角度

### 1.7.1 柯西-徐瓦尔兹等式

![image](https://user-images.githubusercontent.com/18595935/43036146-7301920a-8d36-11e8-8251-6cb68f59c0bf.png)

![image](https://user-images.githubusercontent.com/18595935/43036161-c193a9e4-8d36-11e8-81a2-e9e3d2281cc7.png)

### 1.7.2 练习：编写点积和夹角函数

![image](https://user-images.githubusercontent.com/18595935/43036364-6f39c8a4-8d3b-11e8-89be-72b4b0befe48.png)

-代码如下，本次新增函数为`myinner`:

```python
from math import sqrt,acos,degrees
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates 

    def myplus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    
    # 与myplus相同的功能
    def myplus2(self,v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def myminus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)


    def mytimes(self,c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)
    
    def myinner(self,v):
        new_coordinates = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(new_coordinates)

    def magnitude(self):
        magnitude = 0
        for i in range(len(self.coordinates)):
            magnitude += self.coordinates[i] * self.coordinates[i]

        return sqrt(magnitude)
    
    def magnitude2(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def norm(self):
        magnitude1 = self.magnitude()
        new_coordinates = [x/magnitude1 for x in self.coordinates]
        return Vector(new_coordinates)
    
    def norm2(self):
        try:
            magnitude = self.magnitude2()
            return self.mytimes(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector!")
```

```python
v1_vector = Vector([7.887,4.138])
w1_vector = Vector([-8.802,6.776])

v2_vector = Vector([-5.955,-4.904,-1.874])
w2_vector = Vector([-4.496,-8.755,7.103])

v3_vector = Vector([3.183,-7.627])
w3_vector = Vector([-2.668,5.319])

v4_vector = Vector([7.35,0.221,5.188])
w4_vector = Vector([2.751,8.259,3.985])

print(v1_vector.myinner(w1_vector))
print(v2_vector.myinner(w2_vector))

angel3_arccos = acos(v3_vector.myinner(w3_vector) / (v3_vector.magnitude2() * w3_vector.magnitude2()))
print(angel3_arccos)

angel4_arccos = acos(v4_vector.myinner(w4_vector) / (v4_vector.magnitude2() * w4_vector.magnitude2()))
deg4 = degrees(angel4_arccos)
print(deg4)

```

结果输出如下:

```python
-41.382286
56.397178000000004
3.0720263098372476
60.27581120523091
```

## 1.8 平行和正交向量

![image](https://user-images.githubusercontent.com/18595935/43036433-e257d438-8d3c-11e8-9e95-8feb4744fe8d.png)

### 1.8.1 练习: 检查是否平行或正交

![image](https://user-images.githubusercontent.com/18595935/43036534-c63c9700-8d3e-11e8-9b7c-6070de839f25.png)

```python
from math import sqrt,acos,degrees,pi
class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR = "Cannot normalize the zero vector"
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates 

    def myplus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    
    # 与myplus相同的功能
    def myplus2(self,v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def myminus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)


    def mytimes(self,c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)
    
    def myinner(self,v):
        new_coordinates = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(new_coordinates)

    def magnitude(self):
        magnitude = 0
        for i in range(len(self.coordinates)):
            magnitude += self.coordinates[i] * self.coordinates[i]

        return sqrt(magnitude)
    
    def magnitude2(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def norm(self):
        magnitude1 = self.magnitude()
        new_coordinates = [x/magnitude1 for x in self.coordinates]
        return Vector(new_coordinates)
    
    def norm2(self):
        try:
            magnitude = self.magnitude2()
            return self.mytimes(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector!")
      
    # 新增的函数       
    def checkParallel(self,v):
        return (self.is_zero() or
               v.is_zero() or
               self.angle_with(v) == 0 or
               self.angle_with(v) == pi)
    
    def checkOrthogonal(self,v,tolerance=1e-10):
        return abs(self.myinner(v)) < tolerance
    
    def is_zero(self,tolerance=1e-10):
        return self.magnitude2() < tolerance
    
    def angle_with(self,v,in_degrees=False):
        try:
            angle_in_radians = acos(self.myinner(v) / (self.magnitude2() * v.magnitude2()))
            
            if in_degrees:
                degrees_per_radian = 180 / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception("Cannot compute an angle with a zero vector")
            else:
                raise e
```

```python
v1_vector = Vector([-7.579,-7.88])
w1_vector = Vector([22.737,23.64])

v2_vector = Vector([-2.029,9.97,4.172])
w2_vector = Vector([-9.231,-6.639,-7.235])

v3_vector = Vector([-2.328,-7.284,-1.214])
w3_vector = Vector([-1.821,1.072,-2.94])

v4_vector = Vector([2.118,4.827])
w4_vector = Vector([0,0])

print(v1_vector.checkParallel(w1_vector))
print(v2_vector.checkParallel(w2_vector))
print(v3_vector.checkParallel(w3_vector))
print(v4_vector.checkParallel(w4_vector))

print("------")

print(v1_vector.checkOrthogonal(w1_vector))
print(v2_vector.checkOrthogonal(w2_vector))
print(v3_vector.checkOrthogonal(w3_vector))
print(v4_vector.checkOrthogonal(w4_vector))
```

输出结果为:

```python
True
False
False
True
------
False
False
True
True
```

## 1.9 向量投影

![image](https://user-images.githubusercontent.com/18595935/43083654-005f9b50-8ed2-11e8-8039-474c346dcde9.png)

![image](https://user-images.githubusercontent.com/18595935/43083675-0ca50ce2-8ed2-11e8-97b7-ceace0d377c3.png)



## 1.10 练习:编写向量投影函数

![image](https://user-images.githubusercontent.com/18595935/43354416-37f23e66-9287-11e8-8e5c-7d75ec018316.png)

代码如下:

```python
    def conponent_parallel_to(self,basis):
        try:
            u = basis.norm2()
            weight = self.myinner(u)
            return u.mytimes(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception("No unique parallel component!")
            else:
                raise e
                
    def component_orthogonal_to(self,basis):
        try:
            projection = self.conponent_parallel_to(basis)
            return self.myminus(projection)
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception("No unique parallel component!")
            else:
                raise e
```

![image](https://user-images.githubusercontent.com/18595935/43354520-bdf60d52-9288-11e8-8470-ef21d1403916.png)

使用上述代码，得到结果:

```python
v1_vector = Vector([3.03,1.879])
w1_vector = Vector([0.825,2.036])
print(v1_vector.conponent_parallel_to(w1_vector))

v2_vector = Vector([-9.88,-3.264,-8.159])
w2_vector = Vector([-2.155,-9.353,-9.473])
print(v2_vector.component_orthogonal_to(w2_vector))

```

```python
Vector: (1.0813376451873125, 2.668610237092568)
Vector: (-8.350081043195763, 3.376061254287722, -1.4337460427811841)
```


## 1.11 向量积(Cross products)

向量积，数学中又称外积、叉积，物理中称矢积、叉乘，是一种在向量空间中向量的二元运算。与点积不同，它的运算结果是一个向量而不是一个标量。并且两个向量的叉积与这两个向量和垂直。其应用也十分广泛，通常应用于物理学光学和计算机图形学中。

![image](https://user-images.githubusercontent.com/18595935/43354632-ef41b8e6-928a-11e8-9fa6-62f39e5380f5.png)

![image](https://user-images.githubusercontent.com/18595935/43354637-069ac686-928b-11e8-8f41-7d49ed6295bc.png)

![image](https://user-images.githubusercontent.com/18595935/43354760-e3e01a18-928c-11e8-9069-5770ddd6eff5.png)

- 两个向量的面积计算:

![image](https://user-images.githubusercontent.com/18595935/43355371-f41326ec-9295-11e8-9b3c-b0ef177ab2ca.png)

## 1.12 练习: 编写向量积函数

![image](https://user-images.githubusercontent.com/18595935/43355492-e50a1366-9297-11e8-9460-d7f006fe1ab8.png)

- 内积函数如下，省略了异常处理部分:

```python
    def cross(self,v):
        try:
            x_1,y_1,z_1 = self.coordinates
            x_2,y_2,z_2 = v.coordinates
            new_coordinates = [y_1*z_2 - y_2*z_1,
                              -(x_1*z_2 - x_2*z_1),
                              x_1*y_2 - x_2*y_1]
            
            return Vector(new_coordinates)
        
        except ValueError as e:
            pass
```

使用如下(只计算了最下面的一个问题，平行四边形面积是三角形面积的两倍):

```python
v3_vector = Vector([1.5,9.547,3.691])
w3_vector = Vector([-6.007,0.124,5.772])
cross3_vector = v3_vector.cross(w3_vector)
print(cross3_vector)
print(cross3_vector.magnitude2())
print(cross3_vector.magnitude2()/2)
```

结果如下:

```python
Vector: (54.647600000000004, -30.829836999999998, 57.534829)
85.12987479883788
42.56493739941894
```

## 1.13 总结:

本节目标:能更熟悉向量算法，并了解向量代数的几何原理。在下面的几节课中，我们将开始学习如何利用这些基本运算解决不同类型的问题。

### 1.13.1 本节代码

```python
from math import sqrt,acos,degrees,pi
class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR = "Cannot normalize the zero vector"
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates 

    def myplus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    
    # 与myplus相同的功能
    def myplus2(self,v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def myminus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)


    def mytimes(self,c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)
    
    def myinner(self,v):
        new_coordinates = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(new_coordinates)

    def magnitude(self):
        magnitude = 0
        for i in range(len(self.coordinates)):
            magnitude += self.coordinates[i] * self.coordinates[i]

        return sqrt(magnitude)
    
    def magnitude2(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def norm(self):
        magnitude1 = self.magnitude()
        new_coordinates = [x/magnitude1 for x in self.coordinates]
        return Vector(new_coordinates)
    
    def norm2(self):
        try:
            magnitude = self.magnitude2()
            return self.mytimes(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector!")
            
    def checkParallel(self,v):
        return (self.is_zero() or
               v.is_zero() or
               self.angle_with(v) == 0 or
               self.angle_with(v) == pi)
    
    def checkOrthogonal(self,v,tolerance=1e-10):
        return abs(self.myinner(v)) < tolerance
    
    def is_zero(self,tolerance=1e-10):
        return self.magnitude2() < tolerance
    
    def angle_with(self,v,in_degrees=False):
        try:
            angle_in_radians = acos(self.myinner(v) / (self.magnitude2() * v.magnitude2()))
            
            if in_degrees:
                degrees_per_radian = 180 / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception("Cannot compute an angle with a zero vector")
            else:
                raise e
                
    def conponent_parallel_to(self,basis):
        try:
            u = basis.norm2()
            weight = self.myinner(u)
            return u.mytimes(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception("No unique parallel component!")
            else:
                raise e
                
    def component_orthogonal_to(self,basis):
        try:
            projection = self.conponent_parallel_to(basis)
            return self.myminus(projection)
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception("No unique parallel component!")
            else:
                raise e
                
    def cross(self,v):
        try:
            x_1,y_1,z_1 = self.coordinates
            x_2,y_2,z_2 = v.coordinates
            new_coordinates = [y_1*z_2 - y_2*z_1,
                              -(x_1*z_2 - x_2*z_1),
                              x_1*y_2 - x_2*y_1]
            
            return Vector(new_coordinates)
        
        except ValueError as e:
            pass
```

### 1.13.2 各个符号的含义：

![image](https://user-images.githubusercontent.com/18595935/43355647-d5d80760-929a-11e8-9f44-6fd3f6c0cf1a.png)