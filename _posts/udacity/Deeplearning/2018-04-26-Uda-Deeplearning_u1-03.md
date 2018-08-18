---
layout: post
title: Uda-DeepLearning-U1-03-矩阵数学和NumPy复习
date: 2018-04-26 00:00:00
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

# 2. 数据维度

深度学习涉及很多矩阵数学，在开始构建你自己的神经网络之前，了解这方面的基础知识非常重要。这些课程简单复习了你需要知道的知识，并提供了如何将 NumPy 库与 Python 中的矩阵高效搭配的指导建议。

![image](https://user-images.githubusercontent.com/18595935/39310165-af25a03a-49a4-11e8-91c7-6d89a55e792f.png)

按照数据维度区分，Scalar-0维-标量，Vector-1维-向量，Matrix-2维-矩阵，Tensor-多维-张量。

# 3. NumPy 中的数据

> 本节是复习Numpy的基本操作，更多关于Numpy可以参考[Numpy库入门](http://road2ai.info/2017/08/19/DataAnalysis_02/)
> 

Numpy是一个C语言编写的大型库，很方便的进行数学运算。

## 3.1 导入Numpy

```python
import numpy as np
```

## 3.2 数据类型和形状

```python
s = np.array(5)
v = np.array([1,2,3])
m = np.array([[1,2], [4,6], [8,9]])

print("{},{},{}".format(s.shape,v.shape,m.shape))
```

上面s,v,m分别表示标量，向量和矩阵，输出结果为`(),(3,),(3, 2)`。

```python
print("{},{}".format(v[1],v[1:]))
```

上面输出为`2,[2 3]`,也能使用python中的切片操作。

## 3.3 更改形状

```python
v = np.array([1,2,3,4])
v1 = v.reshape(2,2)
print("{},{}".format(v.shape,v1.shape))
```

输出为`(4,),(2, 2)`，即将一个1维变成了二维。

```python
print("{},{}".format(v,v1))
```

输出为 `[1 2 3 4],[[1 2] [3 4]]`。

# 4. 元素级矩阵运算

![image](https://user-images.githubusercontent.com/18595935/39552312-a3374cf2-4ea3-11e8-98eb-7c9c5aee6d5b.png)

两个不同维度的矩阵不能进行运算：

![image](https://user-images.githubusercontent.com/18595935/39552375-ef26babc-4ea3-11e8-9e06-06b777121454.png)


# 5. Numpy中的元素级运算

数组的数学运算，先看如果通过纯粹的python如何实现:

```python
values = [1,2,3,4,5]
for i in range(len(values)):
    values[i] += 5
print(values)
```

通过numpy中的ndarray则简单得多:

```python
values = np.array([1,2,3,4,5])
print(values + 5)

values *= 2
print(values)
```
分别输出 `[ 6  7  8  9 10]`和`[ 2  4  6  8 10]`。

下面看看矩阵的形状:

```python
a = np.array([[1,3],[5,7]])
b = np.array([[2,4],[6,8]])
print(a+b)
```

输出为：

```python
array([[ 3,  7],
       [11, 15]])
```

但是如果是`c = np.array([[2,3,6],[4,5,9],[1,8,7]])`，`print(a + c)`,结果为错误:

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-16-ca57d551b7f3> in <module>()
----> 1 a + c

ValueError: operands could not be broadcast together with shapes (2,2) (3,3) 
```

这两种形状是不同的，因此我们无法执行元素级运算。

# 6. 矩阵乘法:第1部分

矩阵积运算:

![image](https://user-images.githubusercontent.com/18595935/39660141-9dfa91e6-5073-11e8-99dd-f983e2f4a2fd.png)

如下图是两个矩阵的积运算，矩阵1 (2*4)的列数，要与矩阵2 (4*3)的行数一致，这里都是4，在下一个部分有更详细的解释。

![image](https://user-images.githubusercontent.com/18595935/39660211-c4fa59f6-5074-11e8-99f0-6dbf0702e3e0.png)

# 7. 矩阵乘法:第2部分

关于矩阵乘法的重要提醒:

- 左侧矩阵的列数必须等于右侧矩阵的行数。
- 答案矩阵始终与左侧矩阵有相同的行数，与右侧矩阵有相同的列数。
- 顺序很重要：乘法 A•B 不等于乘法 B•A 。
- 左侧矩阵中的数据应排列为行，而右侧矩阵中的数据应排列为列。
记住这四点，在构建神经网络时，就能搞清楚如何正确排列矩阵乘法了。

# 8. NumPy 矩阵乘法

## 8.1 元素级乘法

```python
m = np.array([[1,2,3],[4,5,6]])
print(m)

n = m * 0.25
print(n)
```

分别输出为:

```python
[[1 2 3]
 [4 5 6]]

[[ 0.25  0.5   0.75]
 [ 1.    1.25  1.5 ]]
```

元素级乘法，下面两种方式都OK：

```python
print(m*n)
print(np.multiply(m,n))
```

最终结果为:

```python
[[ 0.25  1.    2.25]
 [ 4.    6.25  9.  ]]
```

## 8.2 矩阵积运算

要获得矩阵乘积，可以使用 NumPy 的 matmul 函数，如下示例:

```python
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.shape)
```

输出如下，a是一个2行4列的矩阵:

```python
[[1 2 3 4]
 [5 6 7 8]]
(2, 4)
```

```python
b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(b)
print(b.shape)
```

输出如下,b是一个4行3列的矩阵:

```python
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
(4, 3)
```

执行矩阵乘法后:

```python
c = np.matmul(a, b)
print(c)
print(c.shape)
```

输出如下，最终结果是一个2行3列的矩阵:

```python
[[ 70  80  90]
 [158 184 210]]
(2, 3)
```

如果说将a和b顺序反过来，那将出错，不符合矩阵乘法的规格:

```python
np.matmul(b, a)
```

结果如下:

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-26-e4bc68249b85> in <module>()
----> 1 np.matmul(b, a)

ValueError: shapes (4,3) and (2,4) not aligned: 3 (dim 1) != 2 (dim 0)
```

# 9. 矩阵转置(Matrix Transpose)

如下是一个矩阵转置，通过矩阵转置后，可以实现两个矩阵相乘。

![image](https://user-images.githubusercontent.com/18595935/39660461-64cd74ae-507a-11e8-871f-0c226e3a5a05.png)

# 10. NumPy 中的转置

在 NumPy 中获得矩阵的转置非常容易。只需访问其 T 属性即可。

```python
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("before:\n {}".format(m))
print("After:\n {}".format(m.T))
```

输出如下:

```python
before:
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
After:
 [[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
```

尝试对翻转后矩阵进行修改：

```python
m_t = m.T
m_t[3][1] = 200
print("before:\n {}".format(m))
print("After:\n {}".format(m.T))
```

输出结果如下:

```python
before:
 [[  1   2   3   4]
 [  5   6   7 200]
 [  9  10  11  12]]
After:
 [[  1   5   9]
 [  2   6  10]
 [  3   7  11]
 [  4 200  12]]
```

NumPy 在进行转置时不会实际移动内存中的任何数据 - 只是改变对原始矩阵的索引方式 - 所以是非常高效的。

但是，这也意味着你要特别注意修改对象的方式，因为它们共享相同的数据。
请注意上面同时修改了转置和原始矩阵，这是因为它们共享相同的数据副本。
所以记住，**将转置视为矩阵的不同视图，而不是完全不同的矩阵。**

## 10.1 实际的用例

假设有以下两个矩阵，称为 inputs 和 weights，

```python
inputs = np.array([[-0.27,  0.45,  0.64, 0.31]])
weights = np.array([[0.02, 0.001, -0.03, 0.036], \
    [0.04, -0.003, 0.025, 0.009], [0.012, -0.045, 0.28, -0.067]])

print("inputs,shape:{}:\n{}".format(inputs.shape,inputs))
print("weights,shape:{}:\n{}".format(weights.shape,weights))
```

输出如下:

```python
inputs,shape:(1, 4):
[[-0.27  0.45  0.64  0.31]]
weights,shape:(3, 4):
[[ 0.02   0.001 -0.03   0.036]
 [ 0.04  -0.003  0.025  0.009]
 [ 0.012 -0.045  0.28  -0.067]]
```

左边矩阵的列数，与右边矩阵的行数不一致，直接矩阵乘法的话，会出错:

```python
x = np.matmul(inputs, weights.T) # (1,4) *(4,3)
y = np.matmul(weights,inputs.T) # (3,4) *(4,1)

print("x.shape:{}\n{}".format(x.shape,x)) 
print("y.shape:{}\n{}".format(y.shape,y))
```

输出结果如下:

```python
x.shape:(1, 3)
[[-0.01299  0.00664  0.13494]]
y.shape:(3, 1)
[[-0.01299]
 [ 0.00664]
 [ 0.13494]]
```

# 11. NumPy 练习


```python
# Use the numpy library
import numpy as np

def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    input_array = np.array([inputs])
    
    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    # We can use NumPy's min function and element-wise division
    inputs_minus_min = input_array - np.min(input_array)

    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    # We can use NumPy's max function and element-wise division
    inputs_div_max = inputs_minus_min / np.max(inputs_minus_min)

    return input_array, inputs_minus_min, inputs_div_max
    

def multiply_inputs(m1, m2):
    # Check the shapes of the matrices m1 and m2. 
    # m1 and m2 will be ndarray objects.
    #
    # Return False if the shapes cannot be used for matrix
    # multiplication. You may not use a transpose
    if m1.shape[0] != m2.shape[1] and m1.shape[1] != m2.shape[0]:     
        return False

    # Have not returned False, so calculate the matrix product
    # of m1 and m2 and return it. Do not use a transpose,
    #       but you swap their order if necessary
    if m1.shape[1] == m2.shape[0]:
        return np.matmul(m1, m2)        
    else:
        return np.matmul(m2, m1)        


def find_mean(values):
    # Return the average of the values in the given Python list
    # NumPy has a lot of helpful methods like this.
    return np.mean(values)



input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print("--------------------")

print("Multiply 1:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))))
print("Multiply 2:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))))
print("Multiply 3:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))))

print("Mean == {}".format(find_mean([1,3,4])))
```


输出如下:

```python
Input as Array: [[-1  2  7]]
Input minus min: [[0 3 8]]
Input  Array: [[0.    0.375 1.   ]]
--------------------
Multiply 1:
False
Multiply 2:
[[14]
 [32]]
Multiply 3:
[[ 9 12 15]]
Mean == 2.6666666666666665
```

