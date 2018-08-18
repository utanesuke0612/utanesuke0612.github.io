---
layout: post
title: 深度学习入门-03-神经网络
date: 2018-07-28 00:00:03
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

# 1. 从感知机到神经网络

感知机理论上能表示复杂的函数，但是设定权重的工作，即确定合适的能符合预期的输入输出权重，认识要人工干预。
神经网络的出现能解决这一问题，因为神经网络的一个重要性质是它可以自动从数据中学习到合适的权重参数。

首先对比下神经网络和感知机:

![image](https://user-images.githubusercontent.com/18595935/43669526-9e7ea674-97be-11e8-9e65-124c1fb9bec4.png)


# 2. 激活函数

激活函数是连接感知机和神经网络的桥梁，上面出现的h(x)函数会将输入信号总和转换为输出信号，这种函数称为`激活函数`，激活函数的作用在于决定如何激活输入信号的总和。
如下，可以将输出信号的计算分解为两步:
- ` a = b + w1*x1 + w2*x2 `,首先计算加权输入信号和偏置的总和
- ` y = h(a)`，通过激活函数将a总和转变为输出y

![image](https://user-images.githubusercontent.com/18595935/43669607-3f11e60a-97bf-11e8-8dbe-f6f3cc48ddef.png)

感知机以阈值与界，一旦输入超过阈值，就切换输出，这样函数称为阶跃函数，另外如果以sigmoid函数为激活函数，则进入了神经网络的世界。

![image](https://user-images.githubusercontent.com/18595935/43669818-060b6546-97c1-11e8-989e-39d4486c5d16.png)

## 2.1 阶跃函数

如上图表示，阶跃函数当输入超过0，输出1；否则输出为0:

- 代码实现

```python
import numpy as np

def step_function(x):
    y = x > 0
    print(y)
    return y.astype(np.int)

x = np.array([-1,2,-2,3])
print(step_function(x))
```

输出如下:

```python
[False  True False  True]
[0 1 0 1]
```

- 图形化:

```python
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0,dtype=np.int)

x = np.arange(-5,5,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43670002-80f7318a-97c2-11e8-9718-b22050d72cfc.png)

## 2.2 sigmoid函数

sigmoid函数表达式参考上面，exp(-x)表示e(纳皮尔常熟,2.7182)的-x次方，神经网络中用sigmoid函数作为激活函数，进行信号转换，转换后的信号被传递给下一个神经元。

- 代码实现及图形表示

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5,5,0.1)
y = sigmoid(x)
print("x:",x[:5],"......")
print("y:",y[:5],"......")
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43670113-76b2c77e-97c3-11e8-888c-ee6124d9622c.png)

## 2.3 sigmoid函数和阶跃函数比较

首先从图形上，阶跃函数以0为界限，输出急剧变化，而sigmoid函数是一条平滑曲线，输出随着输入发生连续性变化。(单调递增函数)

```python
x = np.arange(-5,5,0.1)
y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x,y1)
plt.plot(x,y2)
plt.ylim(-0.1,1.1)
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/43670175-fdbcd0d4-97c3-11e8-977a-3f5e764187b5.png)

- 阶跃函数只能返回0和1，而sigmoid函数返回`0.00669285`等实数，也就是说感知机中的神经元只有0和1的二元信号，而神经网络中流动的是连续的实数值信号。
- 另外两个函数共同点时，不管输入信号多小或多大，输出信号都在0和1之间。

阶跃函数和sigmoid函数还有共同点，就都是`非线性函数`，sigmoid函数是一条曲线，阶跃函数是一条阶梯一样的折线。

- `线性函数`: 向这个转换器输入某个值后，输出值是输入值的常数倍，如`h(x)=cx，c为常数`
- `非线性函数`: 不像线性函数那样呈现一条直线的函数


**为什么神经网络的激活函数必须使用非线性函数呢?**

因为使用线性函数的话，加深神经网络的层数就没有意义了，线性函数的问题在于，不管如何加深层数，总是存在与之等效的`无隐藏层的神经网络`，比如有激活函数`h(x) = cx`,把`y(x)=h(h(h(x)))`的运算对应3层神经网络，但是可以同样的处理`y=c*c*c*x`来完成，这是一个没有隐藏层的神经网络。

## 2.4 ReLU函数(Rectified Linear Unit)函数

ReLU函数在输入大于0时，直接输出该值，输入小于0时，输出0

![image](https://user-images.githubusercontent.com/18595935/43670483-3b81ec62-97c7-11e8-84da-797e711876e1.png)


```python
def relu(x):
    return np.maximum(0,x)

x = np.arange(-5,5,0.1)
y1 = step_function(x)
y2 = sigmoid(x)
y3 = relu(x)

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.ylim(-0.1,5.1)
plt.show()
```

图形如下:

![image](https://user-images.githubusercontent.com/18595935/43670528-a25af960-97c7-11e8-8b2b-2fc4178afd23.png)

# 3. 多维数组的运算

![image](https://user-images.githubusercontent.com/18595935/43670561-10365e5c-97c8-11e8-8f0d-9119c9e14c64.png)

```python
B = np.array([[1,2],[3,4],[5,6]])
print(B)
print("形状:",B.shape)
print("行数:",B.shape[0])
print("列数:",B.shape[1])
```

```python
[[1 2]
 [3 4]
 [5 6]]
形状: (3, 2)
行数: 3
列数: 2
```

## 3.1 矩阵乘法

1. A 的 行数，B 的 列数，决定乘积矩阵的形状。
2. A 的 列数，要与B的行数保持相同。

![image](https://user-images.githubusercontent.com/18595935/43670892-6f2a39e8-97cc-11e8-8fa7-ba0d164e267e.png)

- 代码 `(2, 2) * (2, 2) = (2, 2)`

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.dot(A,B)
print(C,"\n")
print("A:",A.shape,"* B:",B.shape)
print("C:",C.shape)
```

输出

```python
[[19 22]
 [43 50]] 

A: (2, 2) * B: (2, 2)
C: (2, 2)
```

- 代码 `(3, 2) * (2, 4) = (3,4)`

```python
A = np.array([[1,2],[3,4],[1,2]])
B = np.array([[5,6,5,6],[7,8,7,8]])
C = np.dot(A,B)
print(C,"\n")
print("A:",A.shape,"* B:",B.shape)
print("C:",C.shape)
```

输出

```python
[[19 22 19 22]
 [43 50 43 50]
 [19 22 19 22]] 

A: (3, 2) * B: (2, 4)
C: (3, 4)
```

- 代码 `(3, 2) * (3, 4) = ERROR !`

```python
A = np.array([[1,2],[3,4],[1,2]])
B = np.array([[5,6,5,6],[7,8,7,8],[7,8,7,8]])
C = np.dot(A,B)
print(C,"\n")
print("A:",A.shape,"* B:",B.shape)
print("C:",C.shape)
```

输出

```python
ValueError: shapes (3,2) and (3,4) not aligned: 2 (dim 1) != 3 (dim 0)
```

## 3.2 神经网络内积

> 内积 [7. 内积(Inner Products/Dot Products)](http://road2ai.info/2018/03/22/LinearAlgebra-02/#7-%E5%86%85%E7%A7%AFinner-productsdot-products)

> 向量积 [13. 向量积(Cross products](http://road2ai.info/2018/03/22/LinearAlgebra-02/#13-%E5%90%91%E9%87%8F%E7%A7%AFcross-products)


![image](https://user-images.githubusercontent.com/18595935/43671022-34bc76e8-97ce-11e8-99fa-e0931df29ce3.png)

```python
A = np.array([[1,2]])
B = np.array([[1,3,5],[2,4,6]])
C = np.dot(A,B)
print(C,"\n")
print("A:",A.shape,"* B:",B.shape)
print("C:",C.shape)
```

输出

```python
[[ 5 11 17]] 

A: (1, 2) * B: (2, 3)
C: (1, 3)
```

# 4. 3层数据网络的实现

## 4.1 符号确认:

![image](https://user-images.githubusercontent.com/18595935/43671099-2ae0199e-97cf-11e8-8e50-3ecdb1d3955a.png)


## 4.2 第一层神经信号的计算

![image](https://user-images.githubusercontent.com/18595935/43671248-5cbd44e4-97d1-11e8-9647-f430f768549e.png)

- 代码实现:

```python
X = np.array([1,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

# 计算加权和
A1 = np.dot(X,W1) + B1

print("A1:",A1,"\n")
print("X:",X.shape,"* W1:",W1.shape, "+ B1:",B1.shape)
print("A1:",A1.shape,"\n")

# sigmoid函数计算
Z1 = sigmoid(A1)
print("Z1:",Z1)
print("Z1:",Z1.shape,"\n")
```

输出

```python
A1: [ 0.3  0.7  1.1] 

X: (2,) * W1: (2, 3) + B1: (3,)
A1: (3,) 

Z1: [ 0.57444252  0.66818777  0.75026011]
Z1: (3,) 
```

## 4.3 第二层神经信号的计算

![image](https://user-images.githubusercontent.com/18595935/43671323-98dd3366-97d2-11e8-8b31-2f3c7b4c386d.png)

- 计算第一层到第二层信号

```python
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]) 
B2 = np.array([0.1, 0.2]) 

# 根据上一层的信号，再次计算加权和
A2 = np.dot(Z1, W2) + B2 

# sigmoid函数计算
Z2 = sigmoid(A2) 
print("Z2:",Z2)
print("Z2:",Z2.shape,"\n")
```

输出 

```python
Z2: [ 0.62624937  0.7710107 ]
Z2: (2,) 
```

## 4.4 输出层信号计算

![image](https://user-images.githubusercontent.com/18595935/43671358-42e5f5e6-97d3-11e8-857d-6913e4afddb6.png)

```python
def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]]) 
B3 = np.array([0.1, 0.2]) 

A3 = np.dot(Z2, W3) + B3 

Y = identity_function(A3) # 或者Y = A3 

print("Y:",Y)
print("Y:",Y.shape,"\n")
```

输出如下:

```python
Y: [ 0.31682708  0.69627909]
Y: (2,) 
```

上面定义了一个函数`identity_function`，这是输出层的激活函数，输出层激活函数用`σ()`表示，不同于隐藏层的激活函数`h()`.

**输出层所用的激活函数，要根据特定问题性质决定**
- 一般回归问题(预测明天气温)用恒等函数
- 二元分类问题(预测婚否)用sigmoid函数
- 多元分类问题(预测猫狗鼠等)用softmax函数

## 4.5 代码小结

下面将上述的实现过程，整理到一起，按照神经网络的实现惯例，只把权重记为大写字母W，其他中间结果和偏置用小写字母:

```python
# 初始化权重和偏置，并保存到字典变量network中
def init_network():
    network = {}
    network["W1"] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    
    return network

# 从输入到输出方向的传递处理
def forward(network,x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    # 输入 → 第一层
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    
    # 第一层 → 第二层    
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    
    # 第二层 → 输出   
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    
    return y

network = init_network()
x = np.array([1.0,0.5])
y = forward(network,x)
print("Y:",Y)
```

输出为`Y: [ 0.31682708  0.69627909]`

# 5. 输出层的设计

神经网络可以用在回归问题和分类问题上，要根据情况改变输出层的激活函数，一般而已，回归问题用恒等函数，分类问题用softmax函数。

![image](https://user-images.githubusercontent.com/18595935/43671624-826b55a8-97d8-11e8-81a8-64f0d290e236.png)

可以看出，使用softmax的输出层的各个神经元，都受到上一层输入信号的影响。(因为分母是所有神经元的总和)
而恒等函数不会受到上一层输入信号的影响，输入信号被原封不动的输出。

## 5.1 softmax函数

上面提到分类问题使用softmax函数，softmax可以用下面的式子表示:

![image](https://user-images.githubusercontent.com/18595935/43671530-c7213610-97d6-11e8-96cc-fc5574b8ae87.png)

```python
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
a = np.array([0.1, 2.9, 4.0]) 
print("y:",softmax(a))
```

输出为`y: [ 0.01495951  0.24600391  0.73903658]`

上面的softmax函数，有一个缺陷就是溢出问题，softmax函数要进行指数函数的运算，但是指数函数的值很容易变到特别大，特大值进行除法时，结果会出现`不确定`的情况。

可以进行如下的改进:

![image](https://user-images.githubusercontent.com/18595935/43672309-52f60aee-97e6-11e8-9e49-886a6d8a614d.png)

分子分母都乘上C这个任意常数，这样避免特大值的出现，改进后程序如下:

```python
def softmax(a):
    c = -0#np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

a = np.array([1010, 1000, 990]) 
print("y:",softmax(a))
```

输出结果为`y: [  9.99954600e-01   4.53978686e-05   2.06106005e-09]`，如果用之前没有C的函数，输出为` [ nan  nan  nan] `


**softmax函数的特征**

- softmax函数的输出值总和是1，输出总和是1是softmax函数的一个重要性质，所以可以把softmax函数的输出解释为概率。
- 即便有了softmax函数，因为指数函数`y=exp(x)`是单调递增函数，所以`y与x`的大小关系没有变化。

## 5.2 输出层的神经元数量

输出层的神经元数量需要根据待解救的问题来决定，对于分类问题，输出层的神经元数据量一般设定为类别的数量，比如数字识别，则神经元的数量为10，即0-9.

![image](https://user-images.githubusercontent.com/18595935/43672398-05e3e2a6-97e8-11e8-8a3c-fbb6bba5636a.png)

上面的例子中神经元y2颜色最深，输出的值最大。

# 6. 手写数字识别

本书自带程序中有文件夹，`dataset`，导入该文件夹，使用mnist.py脚本下载MNIST数据集，并将数据转换成Numpy数组。

- ##读取数据并查看，代码##

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 输出各个数据的形状 
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, )
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000, )

img = x_train[0]
label = t_train[0]
print("\n",label)  # 5

print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 把图像的形状变为原来的尺寸
print(img.shape)  # (28, 28)

img_show(img)

```

- 先将数据集分成训练集，以及测试集，分别有60000和10000条记录，每条记录上有784个像素数据
- `5`表示该元素的标签，即正确的识别结果
- 将784个一维像素点，转换为二维数据，并显示为图像,图像显示使用PIL(Python Image Libray)模块

输出为:

```python
(60000, 784)
(60000,)
(10000, 784)
(10000,)

 5
(784,)
(28, 28)
```

图像显示为:

![image](https://user-images.githubusercontent.com/18595935/43672715-ed2c50b6-97ee-11e8-9c86-c544732ed1ff.png)

## 6.1 神经网络的推理处理

要实现的神经网络结构如下:

- 输入层有784个神经元，这个784个神经元来自图像大小28*28 = 784 像素。
- 输出层的10个神经元，这个数字来源于10类别分类。
- 这个神经网络有2个隐藏层，第一个隐藏层有50个神经元，第二个隐藏层有100个神经元。

![image](https://user-images.githubusercontent.com/18595935/43673118-d95ab358-97f7-11e8-8c30-f11cd0b34337.png)


```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import pickle
from dataset.mnist import load_mnist
#from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
        
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # 获取概率最高的元素的索引
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
```

- `get_data()`，获取训练数据和测试数据。
- `init_network()`,读取外部权重和偏置文件。
- `predict()`，根据权重和偏置，使用激活函数和softmax函数，得到输出结果y，y是10个神经元的概率。

最终计算索引号与标签匹配的个数，并得到识别精度。


## 6.2 批处理

上面的predict函数的一次只处理了一张图形，即一个输入神经元x，为此可以把x的形状改为100*784，将100张图形打包作为输入数据

![image](https://user-images.githubusercontent.com/18595935/43673343-29d3fce6-97fc-11e8-8c9f-b855859ca049.png)

输入和输出的神经元维度变成了100，批处理对计算机的运算大有好处，可以大幅度缩短每张图形的处理时间，因为大多数处理数值计算的库都进行了能够高效处理大型数组运算的最优化，并且在神经网络运算中，当数据传送成为瓶颈时，批处理可以减轻数据总线的负荷。

- 最后部分修改后代码如下:

```python
x, t = get_data()
network = init_network()

batch_size = 100 
accuracy_cnt = 0
for i in range(0,len(x),batch_size):
    x_batch = x[i:i+batch_size]
    print(x_batch.shape)
    y_batch = predict(network, x_batch)
    print(y_batch.shape)
    p = np.argmax(y_batch,axis=1) 
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
```

# 7. 小结

本章介绍了神经网络的前向传播，神经网络与感知器在信号的层传递上是相同的，但是向下一个神经元发送信号时改变信号的激活函数有很大差异。

- 神经网络中使用的是平滑变化的sigmoid函数
- 感知机中使用的是信号急剧变化的阶跃函数

**本章内容总结如下**:

- 神经网络中的激活函数使用平滑变化的sigmoid函数或ReLU函数
- 通过巧妙地使用Numpy多维数组，可以高效实现神经网络
- 机器学习大体分为回归问题(预测年龄)和分类问题(判断性别)
- 关于输出层的激活函数，回归问题中一般使用恒等函数，分类问题中一般用softmax函数
- 分类问题中，输出层的神经元数量设置为要分类的类别数
- 输入数据的集合称为批，通过以批为单位进行推理处理，能够实现高速运算



