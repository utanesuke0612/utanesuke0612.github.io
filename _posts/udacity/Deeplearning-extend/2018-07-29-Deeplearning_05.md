---
layout: post
title: 【书】深度学习入门-05-误差反向传播法
date: 2018-07-28 00:00:05
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

上一章介绍了神经网络的学习，并通过数值微分计算了神经网络的权重参数的梯度(损失函数关于权重参数的梯度)，数值微分虽然简单容易实现，但是比较费时间。本站介绍能高效计算权重参数的梯度的方法-误差反向传播法。

# 1. 计算图

计算题通过节点和箭头表示计算过程，节点用O表示,O中是计算的内容，计算中间结果在箭头上方。

![image](https://user-images.githubusercontent.com/18595935/43989774-50de30a6-9d8b-11e8-97dc-6891df5aae6f.png)

使用计算图最大的原因是 **可以通过反向传播高效计算导数**。

在介绍计算图的反向传播时，思考一个如下的例子，计算购买2个苹果时加上消费税最终需要支付的金额。

![image](https://user-images.githubusercontent.com/18595935/43989882-8e822ece-9d8d-11e8-8c37-23cf72a4e03c.png)

假设我们这里想知道苹果价格上涨会多大程度上影响支付金额，即支付金额关于苹果的价格导数，上图可知是2.2，其他因素，比如个数和消费税对支付金额的影响，也可以通过类似的方式求得。

# 2. 链式法则

局部导数的反向传递，是基于**链式法则(chain rule)**.

![image](https://user-images.githubusercontent.com/18595935/43989945-cdbf0930-9d8e-11e8-8c98-8a440dc2c4f0.png)

如上图所示，反向传播的计算顺序，将信号E乘以节点的局部导数(y关于x的导数)，假设y=f(x)=x**2，则局部导数为2x.

## 2.1 链式法则

链式法则是关于符合函数的导数的性质: *如果某个函数由复合函数表示，则该复合函数的导数可以用构成复合函数的各个函数的导数乘积表示。*

![image](https://user-images.githubusercontent.com/18595935/43990269-c2592214-9d94-11e8-89f2-dece6035f46d.png)

将链式法则的计算，用计算图表示出来，如下:

![image](https://user-images.githubusercontent.com/18595935/44035401-63db9462-9f4a-11e8-8c17-4147f5be4a4f.png)


# 3. 反向传播

- 加法节点的反向传播，将上游的值原封不动的输出到下游，因为加法节点的导数为1.
- 乘法的反向传播会乘以输入信号的翻转值.

加法的反向传播只是将上游的值传给下游，并不需要正向传播的输入信号，但是，乘法的反向传播需要正向传播时的输入信号值。
因此，**实现乘法节点的反向传播时，要保存正向传播的输入信号**。

![image](https://user-images.githubusercontent.com/18595935/44035940-98266408-9f4b-11e8-9dea-8dd06361a58f.png)

购买苹果的反向传播例子,乘法节点的反向传播会将输入信号翻转后传给下游，加法节点会直接传给下游:

![image](https://user-images.githubusercontent.com/18595935/44036419-b3f77cd4-9f4c-11e8-8746-d3d2ff9a0d3e.png)

# 4. 简单层的实现

## 4.1 乘法层的实现

层的实现中有两个共通的方法forward()和backward()，前者负责正向传播，后面负责反向传播。

![image](https://user-images.githubusercontent.com/18595935/44037396-2eff8500-9f4f-11e8-8463-08ad6626893f.png)

通过下面的代码，实现上面乘法层的前向和反向传播:

```python
# 一个乘法节点，作为一个类的对象
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    # 进行一次前向传播后，对象的x和y被赋值，即输入信号，输出为结果，只有一个值
    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x * y
    
        return out
    
    # 反向的话，对应两个输出
    def backward(self,dout):
        dx = dout * self.y
        dy = dout * self.x
        
        return dx,dy
```

- 前向传播,前一层前向传播的结果，作为下一层前向传播的输入信号

```python
apple = 100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
apple_price = mul_apple_layer.forward(apple,apple_num)
price = mul_tax_layer.forward(apple_price,tax)

print("forward price:",price)
```

输出为: `forward price: 220.00000000000003`

- 反向传播, tax和apple的乘法节点中，经过前向传播，节点对象中有x和y，分别为该节点的输入信号。

```python
# backward
dprice = 1
dapple_price,dtax = mul_tax_layer.backward(dprice)
dapple,dapple_num = mul_apple_layer.backward(dapple_price)

print("dapple:",dapple,",dapple_num:",dapple_num,",dtax:",dtax)
```

输出为: `dapple: 2.2 ,dapple_num: 110.00000000000001 ,dtax: 200`

## 4.2 加法层的实现

![image](https://user-images.githubusercontent.com/18595935/44036419-b3f77cd4-9f4c-11e8-8746-d3d2ff9a0d3e.png)

如果我要实现上面的乘法层和加法层混合的计算图：

```python
class AddLayer:
    # 因为加法的导数，不需要输入信号，即与其他的输入信号无关，故不用保存
    def __init__(self):
        pass
    
    # 直接相加
    def forward(self,x,y):
        out = x + y
        return out
    
    def backward(self,dout):
        dx = dout * 1
        dy = dout * 1
        return dx,dy
```

```python
apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

# forward
apple_price = mul_apple_layer.forward(apple,apple_num)
orange_price = mul_orange_layer.forward(orange,orange_num)
all_price = add_apple_orange_layer.forward(apple_price,orange_price)
price = mul_tax_layer.forward(all_price,tax)

# backward
dprice = 1
dall_price,dtax = mul_tax_layer.backward(dprice)
dapple_price,dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price) 
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

# 前向传播结果
print(price)

# 反向传播结果，对应5个输入信号的导数
print(dapple_num, dapple, dorange, dorange_num, dtax) # 110 2.2 3.3 165 650
```


输出结果如下:

```python
715.0000000000001
110.00000000000001 2.2 3.3000000000000003 165.0 650
```

综上，计算图中层的实现(这里是加法层和乘法层)非常简单，使用这些层可以进行复杂的导数计算。

# 5. 激活函数层的实现

## 5.1 ReLU(Rectified Linear Unit)

激活函数，y=f(x)：
- x>0时，y=x，对应y关于x的导数为1
- x<=0时，y=0，对应y关于x的导数为0

根据上面的激活函数定义，以及其对应导数:
- 如果正向传播时输入x大于0，则反向传播会将上游的值原封不动传给下游
- 如果正向传播时x小于等于0，则反向传播中传给下游的信号停在此处

可以用如下的计算图表示:

![image](https://user-images.githubusercontent.com/18595935/44215691-1eec8a80-a1ae-11e8-88b4-34d36d98122a.png)

代码实现如下:

```python
class Relu:
    def __init__(self):
        self.mask = None
    
    def forward(self,x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        
        return out
    
    def backward(self,dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx

```

上面的`out[self.mask] = 0` 用法很巧妙，看下面的实际用法:

```python
import numpy as np
x = np.array([[1.0,-0.5],[-2,3]])
print("before-x:",x)

mask = (x <= 0) 
print("mask:",mask)

x[mask] = 0 
print("after-x:",x)
```

输出如下:

```python
before-x: [[ 1.  -0.5]
 [-2.   3. ]]
mask: [[False  True]
 [ True False]]
after-x: [[ 1.  0.]
 [ 0.  3.]]
```

ReLU层的作用就像电路中的开关，正向传播时，有电流通过就将开关设为ON，没有电流就设为OFF。
反向传播时，开关为ON的话，电流直接通过，开关为OFF的话，不会有电流通过。

## 5.2 Sigmoid层

Sigmoid函数表达式为 y=f(x)= 1/(1+exp(-x))，用计算图表达式，则如下图:

![image](https://user-images.githubusercontent.com/18595935/44216676-6e33ba80-a1b0-11e8-8556-6be757c06214.png)

上面反向传播的`/`和`exp`的推导，参考教材P142页，涉及到微积分。

简化后的计算图如下:

![image](https://user-images.githubusercontent.com/18595935/44216862-fc0fa580-a1b0-11e8-908b-c09f785b86fb.png)

代码实现如下:

```python
class Sigmoid:
    def __init__(self):
        self.out = None
    
    def forward(self,x):
        out = 1 / (1+np.exp(-x))
        self.out = out
        
        return out
    
    def backward(self,dout):
        dx = dout * (1-self.out) * self.out
        return dx
```

正向传播时将输出保存在了实例变量out中，然后反向传播时，使用该变量out进行计算。

# 6. Affine-Softmax层的实现

## 6.1 Affine层

神经网络的正向传播中进行的矩阵的乘积运算在几何学领域被称为“仿射变换”  。
因此，这里将进行仿射变换的处理实现为“Affine层” 。 

内积的计算参考下图，左边列数要与右边的行数相同，乘积:

![image](https://user-images.githubusercontent.com/18595935/43670892-6f2a39e8-97cc-11e8-8fa7-ba0d164e267e.png)

![image](https://user-images.githubusercontent.com/18595935/43671022-34bc76e8-97ce-11e8-99fa-e0931df29ce3.png)

参考代码如下:

```python
X = np.random.rand(2)
W = np.random.rand(2,3)
B = np.random.rand(3)

Y = np.dot(X,W) + B

print("■ X.shape",X.shape)
print("X:",X)

print("■ W.shape",W.shape)
print("W:",W)

print("■ B.shape",B.shape)
print("B:",B)

print("■ Y.shape",Y.shape)
print("Y:",Y)
```

```python
■ X.shape (2,)
X: [ 0.86921374  0.91685817]
■ W.shape (2, 3)
W: [[ 0.0615422   0.62958261  0.49322879]
 [ 0.81998697  0.87313284  0.40750217]]
■ B.shape (3,)
B: [ 0.42251695  0.66899528  0.16928182]
■ Y.shape (3,)
Y: [ 1.22782203  2.01677612  0.97162475]
```

上面的乘积运算，可以用下面的计算图表示:

![image](https://user-images.githubusercontent.com/18595935/44268316-0f337b80-a26c-11e8-9f14-acb447043813.png)

## 6.2 批版本的Affine层

上面是以单个数据为对象，现在考虑以N个数据进行正向传播，也就是批版本的Affine层。

![image](https://user-images.githubusercontent.com/18595935/44268857-bb299680-a26d-11e8-9811-aaed00ea580b.png)

假设上面X的形状是(4,2)，修改上面的代码

```python
X = np.random.rand(4,2)
W = np.random.rand(2,3)
B = np.random.rand(3)

Y = np.dot(X,W) + B

print("■ X.shape",X.shape)
print("X:",X)

print("■ W.shape",W.shape)
print("W:",W)

print("■ B.shape",B.shape)
print("B:",B)

print("■ Y.shape",Y.shape)
print("Y:",Y)
```


```python
■ X.shape (4, 2)
X: [[ 0.18474588  0.11781004]
 [ 0.09969628  0.22527226]
 [ 0.18807723  0.11648619]
 [ 0.27385227  0.97771642]]
■ W.shape (2, 3)
W: [[ 0.73291508  0.98707711  0.78022863]
 [ 0.04959705  0.95326781  0.10378382]]
■ B.shape (3,)
B: [ 0.94428108  0.32814772  0.90723177]
■ Y.shape (4, 3)
Y: [[ 1.08552715  0.62281067  1.06360257]
 [ 1.02852282  0.64130042  1.00839727]
 [ 1.08790309  0.62483698  1.06606439]
 [ 1.19348339  1.53048662  1.22237029]]
```

# 7. 误差反向传播法的实现

![image](http://static.zybuluo.com/road2ai/x2amkm6hdt08zeec22ccvmqb/image_1cl6j5i1a1uf861q12ddv7v1muv9.png)



