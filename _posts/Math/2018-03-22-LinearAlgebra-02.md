---
layout: post
title: Udacity-基础线性代数LinearAlgebra-02-[ing]向量
date: 2018-03-22 00:02:00
categories: 数学
tags: 统计学
---
* content
{:toc}

# 2. 点和向量

点表示一个绝对位置，向量表示位置上的位移(大小和方向)

![image](https://user-images.githubusercontent.com/18595935/37912983-bec8d9e4-314e-11e8-86f2-fca736097d6b.png)


# 3. Vector 模块

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

# 3. 向量运算

![image](https://user-images.githubusercontent.com/18595935/37971972-38d6158a-3212-11e8-9af2-22d0973b4d28.png)

# 4. 加减和标量乘法

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


# 5. 大小和方向

![image](https://user-images.githubusercontent.com/18595935/37975113-8cad74c6-3219-11e8-983e-e45ace5229fa.png)

- `||V||`绿色部分表示向量的大小
- `u`表示是V的单位向量，即正规化后的向量，大小为1

# 6. 编写大小和方向函数

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









