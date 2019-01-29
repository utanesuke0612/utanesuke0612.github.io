---
layout: post
title: 【书】深度学习入门-05-误差反向传播法
date: 2018-07-28 00:00:05
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

上一章介绍了神经网络的学习，并通过数值微分计算了神经网络的权重参数的梯度(**损失函数关于权重参数的梯度**)，数值微分虽然简单容易实现，但是比较费时间。本章介绍能高效计算权重参数的梯度的方法-误差反向传播法，非常重要，反向传播法是深度学习的基础，必须较好的掌握。本章结构如下：

![image](https://user-images.githubusercontent.com/18595935/51784126-befc0600-2187-11e9-9aca-efaaea52943b.png)


# 1. 计算图

计算题通过节点和箭头表示计算过程，节点用O表示,O中是计算的内容，计算中间结果在箭头上方。

![image](https://user-images.githubusercontent.com/18595935/43989774-50de30a6-9d8b-11e8-97dc-6891df5aae6f.png)

使用计算图最大的原因是 **可以通过反向传播高效计算导数**。

在介绍计算图的反向传播时，思考一个如下的例子，计算购买2个苹果时加上消费税最终需要支付的金额。

![image](https://user-images.githubusercontent.com/18595935/43989882-8e822ece-9d8d-11e8-8c37-23cf72a4e03c.png)

假设我们这里想知道苹果价格上涨会多大程度上影响支付金额，即支付金额关于苹果的价格导数，上图可知是2.2，其他因素，比如个数和消费税对支付金额的影响，也可以通过类似的方式求得。

# 2. 链式法则

前面介绍的计算图的正向传播将计算结果正向传递，其计算过程是我们日常接触的计算过程。而反向传播将局部导数向正方形的反方向传递。

局部导数的反向传递，是基于**链式法则(chain rule)**.

![image](https://user-images.githubusercontent.com/18595935/43989945-cdbf0930-9d8e-11e8-8c98-8a440dc2c4f0.png)

如上图所示，反向传播的计算顺序，将信号E乘以节点的局部导数(y关于x的导数)，假设y=f(x)=x**2，则局部导数为2x.

## 2.1 链式法则

链式法则是关于符合函数的导数的性质: 
**如果某个函数由复合函数表示，则该复合函数的导数可以用构成复合函数的各个函数的导数乘积表示。**

![image](https://user-images.githubusercontent.com/18595935/43990269-c2592214-9d94-11e8-89f2-dece6035f46d.png)

将链式法则的计算，用计算图表示出来，如下:

![image](https://user-images.githubusercontent.com/18595935/44035401-63db9462-9f4a-11e8-8c17-4147f5be4a4f.png)

# 3. 反向传播

- 加法节点的反向传播，将上游的值原封不动的输出到下游，因为加法节点的导数为1.
- 乘法的反向传播会乘以输入信号的翻转值.

加法的反向传播只是将上游的值传给下游，并不需要正向传播的输入信号，但是，乘法的反向传播需要正向传播时的输入信号值。
因此，**实现乘法节点的反向传播时，要保存正向传播的输入信号**。

![image](https://user-images.githubusercontent.com/18595935/44035940-98266408-9f4b-11e8-9dea-8dd06361a58f.png)

购买苹果的反向传播例子,乘法节点的反向传播会将**输入信号**翻转后传给下游，加法节点会直接传给下游:

![image](https://user-images.githubusercontent.com/18595935/44036419-b3f77cd4-9f4c-11e8-8746-d3d2ff9a0d3e.png)

> 比如上面橘子个数上的导数为165, 165 = 1.1*150，即上一级的导数1.1乘以翻转的输入信号150(单价)，得到165.

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
    
    # 反向的话，对应两个输出,dout是上一级的导数
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

> 加法节点的反向传播，将上游的值原封不动的输出到下游，因为加法节点的导数为1,所以下图中加法节点下游的两个导数为1.1，与其上游导数相同。

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

> 上面掩码的用法，在计算机视觉中，对过滤特定RGB值时经常用到，参考如下代码：(读取图形，设定阈值，将阈值外的像素设置为1)

```python
image = mpimg.imread('./L10/test6.jpg')
thresh = (180, 255)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
binary = np.zeros_like(gray)
binary[(gray > thresh[0]) & (gray <= thresh[1])] = 1
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

**偏置的正向传播：**

```python
x_dot_W = np.array([[0,0,0],[10,10,10]])
B = np.array([1,2,3])

print(x_dot_W + B)
```

根据矩阵的广播法则，所以值都被加上了偏置B。

```python
[[ 1  2  3]
 [11 12 13]]
```

**偏置的反向传播：**
> 反向传播时的值需要汇总为偏置的元素，这里使用了dB = np.sum(dY,axis=0)，对第0轴方向上的元素求和。


```python
dY = np.array([[1,2,3],[4,5,6]])

dB = np.sum(dY,axis=0)
print(dB)

dB = np.sum(dY,axis=1)
print(dB)

dB = np.sum(dY)
print(dB)
```

结果如下(分别为：整列相加、整行相加 、所有值相加)：

```python
[5 7 9]
[ 6 15]
21
```

## 6.3 softmax-with-loss层

![image](https://user-images.githubusercontent.com/18595935/51879606-86427380-23b7-11e9-9fc6-57e66000bc3b.png)

上面的输入图像经过affine层(矩阵乘积)和ReLU层进行转换，10个输入通过softmax函数进行正规化，因为手写识别数字有10个分类，所以最终的输出也有10个。

神经网络中进行的处理有**推理(inference)**和**学习**两个阶段：
- 推理：神经网络的推理通常不使用softmax层，因为推理只需要给出一个答案，因为此时只对得分最大值感兴趣，所以不需要softmax层。
- 学习：神经网络学习阶段需要softmax层。

**下图是Softmax-with-Loss层的计算图：**

![image](https://user-images.githubusercontent.com/18595935/51880014-087f6780-23b9-11e9-81a1-77337392c03f.png)

1. softmax层将输入(a1,a2,a3)正规化，输出(y1,y2,y3).
2. CrossEntropyError层接收Softmax的输出(y1,y2,y3)和标签(t1,t2,t3)，从这些数据中输出损失L

上图简化后如下：

![image](https://user-images.githubusercontent.com/18595935/51880153-88a5cd00-23b9-11e9-9fa8-ba8bab8a50ac.png)

请注意上面的反向传播的结果，softmax层的反向传播得到了(y1-t1,y2-t2,y3-t3)的结果，由于y是softmax层输出，t是监督数据吗，所以y-t就是softmax层输出与标签之间的差分，神经网络学习的目的就是调整权重参数，使得softmax层输出与标签之间的差分达到最小。

Softmax-with-Loss的实现代码如下：

```python
class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # 损失
        self.y = None # softmax输出
        self.t = None # 监督数据
    
    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        
        self.loss = cross_entropy_error(self.y,self.t)
        
        return self.loss
    
    def backward(self,dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        
        return dx
```

上述代码使用了之前的softmax()和cross_entropy_error()函数，所以实现十分简单，这两个函数代码参考如下：

```python
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta)) 
```

# 7. 误差反向传播法的实现

神经网络中有合适的权重和偏置，调整权重和偏置以便拟合训练数据的过程，称为学习，神经网络学习的步骤如下：

1. mini-batch，从训练数据中随机选择一部分数据。
2. **计算梯度**，计算损失函数关于各个权重参数的梯度。
3. 更新参数，将权重参数沿梯度方向进行微小的更新。
4. 重复上面的步骤。

> 之前介绍的误差反向传播法，在上面的步骤2中出现，上一章中，我们利用数值微分求得梯度，数值微分虽然实现简单，但计算耗时，误差反向传播法可以快速高效计算梯度。

在这里我们要把2层神经网络实现为TwoLayerNet，将这个类的实例变量和方法整理如下：

1. **params**，保存在神经网络的参数的字典型变量，如权重和偏置
2. **layers**，保存神经网络各个层的有序型字典变量，比如：layers['Affine1']、 layers['ReLu1']、 layers['Affine2']
3. **lastLayer**，神经网络的最后一层，这里是SoftmaxWithLoss层
4. **__init__()**，进行初始化
5. **predict(self, x)**，识别处理，输入是图像数据
6. **loss(self, x, t)**，损失函数的计算，x是输入，t是正确标签
7. **accuracy(self, x, t)**，识别精度计算
8. **numerical_gradient(self, x, t)**，通过数值微分计算关于权重参数的梯度
9. **gradient(self, x, t)**，通过误差反向传播法计算关于权重参数的梯度

## 7.1 TwoLayerNet的代码

```python
import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict

class TwoLayerNet:
    def __init__(self,input_size,hidden_size,output_size,
                weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * \
            np.random.randn(input_size,hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * \
            np.random.randn(hidden_size,output_size)
        self.params["b2"] = np.zeros(output_size)
        
        
        # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = \
            Affine(self.params["W1"],self.params["b1"])
        self.layers["Relu1"] = Relu()
        self.layers["Affine2"] = \
            Affine(self.params["W2"],self.params["b2"])
            
        self.lastLayer = SoftmaxWithLoss()
        
    
    def predict(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)
            
        return x
    
    def loss(self,x,t):
        y = self.predict(x)
        return self.lastLayer.forward(y,t)
    
    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        
        if t.ndim != 1:
            t = np.argmax(t,axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        
        return accuracy
    
    def numerical_gradient(self,x,t):
        loss_W = lambda W:self.loss(x,t)
        
        grads = {}
        grads["W1"] = numerical_gradient(loss_W,self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W,self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W,self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W,self.params["b2"])
        
        return grads
    
    
    def gradient(self,x,t):
        # forward
        self.loss(x,t)
        
        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)        
        
        # 设定
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db

        return grads
```

**初始化权重：**

随机生成权重和偏置，注意其维度。

```python
        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * \
            np.random.randn(input_size,hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * \
            np.random.randn(hidden_size,output_size)
        self.params["b2"] = np.zeros(output_size)
```

**生成层：**

下面将神经网络的层保存为OrderedDict，OrderedDict是有序字典，因此正向传播只需要按照元素的顺序，调用各层的forward()方法即可，而反向传播只需要按照相反的顺序调用各层即可。

```python
 # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = \
            Affine(self.params["W1"],self.params["b1"])
        self.layers["Relu1"] = Relu()
        self.layers["Affine2"] = \
            Affine(self.params["W2"],self.params["b2"])
            
        self.lastLayer = SoftmaxWithLoss()
```

**预测：**

```python
    def predict(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)
            
        return x
```

**计算误差：**

```python
    def loss(self,x,t):
        y = self.predict(x)
        return self.lastLayer.forward(y,t)
```

**评价精度：**

```python
    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        
        if t.ndim != 1:
            t = np.argmax(t,axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        
        return accuracy
```

**微分法求梯度：**

```python
    def numerical_gradient(self,x,t):
        loss_W = lambda W:self.loss(x,t)
        
        grads = {}
        grads["W1"] = numerical_gradient(loss_W,self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W,self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W,self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W,self.params["b2"])
        
        return grads
```

微分法求梯度函数：

```python
def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 还原值
        it.iternext()   
        
    return grad
```

**反向传播法求梯度：**

```python
    def gradient(self,x,t):
        # forward
        self.loss(x,t)
        
        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())
        # 反向传播只需要按照相反的顺序调用各层
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)        
        
        # 设定
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db

        return grads
```

## 7.2 误差反向传播法的梯度确认

上面说过微分法计算量量，不适合实际的去计算梯度，但有个好处就是计算方式简单，所以常用于验证反向传播法的实现是否正确。
确认数值微分求出的梯度，与误差反向传播法求出的结果是否一致，叫做**梯度确认**。

实现代码如下：

```python
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
#from two_layer_net import TwoLayerNet

# 读入数据
(x_train,t_train),(x_test,t_test) = \
                load_mnist(normalize=True,one_hot_label = True)   

network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch,t_batch)
grad_backprop = network.gradient(x_batch,t_batch)

for key in grad_numerical.keys():
    diff = np.average(np.abs(grad_backprop[key] - \
                            grad_numerical[key]))
    print(key + ":" + str(diff))

    
```

```python
b1:5.59066227433e-06
b2:1.39361826149e-07
W2:5.29915498019e-09
W1:5.46059483329e-07
```

![image](https://user-images.githubusercontent.com/18595935/51892372-03d0a880-23e5-11e9-8491-812bf2457768.png)

上面可以看出两者的差异非常小。

## 7.3 使用误差反向传播法的学习

学习的实现方式，与前一章类似，不同之处仅在于，这里通过误差反向传播法求梯度这一点：
> grad = network.gradient(x_batch,t_batch) 

代码如下：

```python
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
import matplotlib.pyplot as plt
#from two_layer_net import TwoLayerNet

# 读入数据
(x_train,t_train),(x_test,t_test) = \
                load_mnist(normalize=True,one_hot_label = True)   

network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 通过误差反向传播法求梯度
    grad = network.gradient(x_batch,t_batch)
    # grad = network.numerical_gradient(x_batch,t_batch)

    # 更新
    for key in ("W1","b1","W2","b2"):
        network.params[key] -= learning_rate * grad[key]
        
    loss = network.loss(x_batch,t_batch)
    train_loss_list.append(loss)
    
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc,",",test_acc)

# 绘制图形
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
```

```python
0.1043 , 0.1041
0.904633333333 , 0.9079
0.921 , 0.9236
0.9321 , 0.9338
0.9436 , 0.9426
0.95025 , 0.9494
0.956133333333 , 0.9531
0.960166666667 , 0.9564
0.9638 , 0.959
0.965933333333 , 0.9607
0.9682 , 0.9619
0.970266666667 , 0.9621
0.97075 , 0.9641
0.973583333333 , 0.9669
0.974083333333 , 0.9663
0.975666666667 , 0.9664
0.9777 , 0.9683
```

![image](https://user-images.githubusercontent.com/18595935/51892759-36c76c00-23e6-11e9-9a50-3d26f3242b75.png)

# 8. 小结

本章与前一章相对应，上一章通过数值微分法求梯度，本章通过反向传播方式求梯度，本章中涉及的有ReLU层，Softmax-with-Loss层，Affine层，Softmax层，这些层中实现了forward和backward方法，通过将数据正向和反向传播，可以高效地计算权重参数的梯度。

1. 计算图的正向传播进行一般的计算(如预测值，softmax值)，反向传播可以计算各个节点的导数。
2. 通过将神经网络的组成元素实现为层，可以高效地计算梯度。
3. 通过比较数值微分和误差反向传播法的结果，可以确认误差反向传播法的实现是否正确。(梯度确认)