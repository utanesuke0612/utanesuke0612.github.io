---
layout: post
title: 【书】深度学习入门-06-与学习有关的技巧(ing)
date: 2018-07-28 00:00:06
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

# 0. 目录

![image](https://user-images.githubusercontent.com/18595935/51821575-ffd95380-231c-11e9-8998-a72362c606f2.png)

本章主要涉及寻找最优权重参数的最优化方法，权重参数的初始值，超参数的设定方法；另外，为了应对过拟合，本章还将介绍权值衰减，Dropout等正则化方法。

# 1. 参数的更新

神经网络学习的目的，是找到使损失函数值尽可能小的参数，这个寻找最优参数的过程，叫做**最优化**。这部分将介绍四种不同的更新方式：

![image](https://user-images.githubusercontent.com/18595935/51966658-6a6ec880-24b0-11e9-9193-70955c06315e.png)

1. SGD：梯度下降法，需要更新的权重参数记为W，用学习率乘以损失函数关于W的梯度去不断更新权重。
2. Momentum：与上面SGD类似，但是多了两个参数，v表示物理上的速度，a是一个参数，比如0.9等，对应地面摩擦或空气阻力等。
3. AdaGrad：为参数的每个元素适当的调整学习率，与此同时进行学习。
4. Adam：融合Momentum和AdaGrad方法，会设置三个参数，一个是学习率，另外两个是一次momentum系数β1和二次momentum系数β2。


## 1.1 SGD

之前介绍过一种方法，就是**梯度下降法SGD**，将参数的梯度(导数)作为线索，使用参数的梯度，沿梯度方向更新参数，并重复这个步骤多次，从而逐渐靠近最优参数。

SGD类的实现代码如下：

```python
class SGD:

    """随机梯度下降法（Stochastic Gradient Descent）"""

    def __init__(self, lr=0.01):
        self.lr = lr
        
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key] 
```

使用这个类进行神经网络参数的更新：

```python
network = TwoLayerNet(...)
optimizer = SGD()

for i in range(10000):
	...
	x_batch, t_batch = get_mini_batch(...) # mini-batch
	grads = network.gradient(x_batch, t_batch)
	params = network.params
	optimizer.update(params, grads)
	...
```

参数的更新，由optimizer负责完成，我们这里需要做的只是将参数和梯度信息传给optimizer。

**SGD的缺点：**

SGD低效的根本原因是，梯度的方向没有指向最小值的方向，如下图：

![image](https://user-images.githubusercontent.com/18595935/51967800-a22b3f80-24b3-11e9-8f88-97a22c0ff508.png)

## 1.2 Momentum

Momentum是动量的意思，与物理有关，实现代码如下：

```python
class Momentum:

    """Momentum SGD"""

    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
        
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():                                
                self.v[key] = np.zeros_like(val)
                
        for key in params.keys():
            self.v[key] = self.momentum*self.v[key] - self.lr*grads[key] 
            params[key] += self.v[key]
```

![image](https://user-images.githubusercontent.com/18595935/51968097-7066a880-24b4-11e9-8648-837c5103dbb4.png)

参考上图，与SGD相比，之字形的程度减轻了，虽然在X轴方向上受到的力非常小，但是一直在同一方向上受力，所以朝同一方向有一定的加速。

## 1.3 AdaGrad

神经网络的学习中，学习率非常重要，学习率过小，会导致学习花费过多时间，学习率过大会导致学习发散而不能正确进行。

这种算法的技巧是被称为**学习率衰减**，伴随着学习的进行，使学习率逐渐减小，一开始多，逐渐少的方法，在神经网络的学习中经常被使用。

实现代码如下：

```python
class AdaGrad:

    """AdaGrad"""

    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
            
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
```

![image](https://user-images.githubusercontent.com/18595935/51968304-f7b41c00-24b4-11e9-890a-5cae11758f94.png)

上图可以看到，函数的取值高效地向最小值移动。

## 1.4 Adam

Momentum参照小球在碗中滚动的物理规则进行移动， AdaGrad为参数的每个元素适当地调整更新步伐。Adam融合了这两种算法：

```python
class Adam:

    """Adam (http://arxiv.org/abs/1412.6980v8)"""

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None
        
    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)
        
        self.iter += 1
        lr_t  = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)         
        
        for key in params.keys():
            #self.m[key] = self.beta1*self.m[key] + (1-self.beta1)*grads[key]
            #self.v[key] = self.beta2*self.v[key] + (1-self.beta2)*(grads[key]**2)
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])
            
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
            
            #unbias_m += (1 - self.beta1) * (grads[key] - self.m[key]) # correct bias
            #unbisa_b += (1 - self.beta2) * (grads[key]*grads[key] - self.v[key]) # correct bias
            #params[key] += self.lr * unbias_m / (np.sqrt(unbisa_b) + 1e-7)

```

![image](https://user-images.githubusercontent.com/18595935/51968617-be2fe080-24b5-11e9-82f8-dc337aa8f0bc.png)

## 1.5 四种方式的比较

四种方式调用代码如下：

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from common.optimizer import *


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0*y

init_pos = (-7.0, 2.0)
params = {}
params['x'], params['y'] = init_pos[0], init_pos[1]
grads = {}
grads['x'], grads['y'] = 0, 0


optimizers = OrderedDict()
optimizers["SGD"] = SGD(lr=0.95)
optimizers["Momentum"] = Momentum(lr=0.1)
optimizers["AdaGrad"] = AdaGrad(lr=1.5)
optimizers["Adam"] = Adam(lr=0.3)

idx = 1

for key in optimizers:
    optimizer = optimizers[key]
    x_history = []
    y_history = []
    params['x'], params['y'] = init_pos[0], init_pos[1]
    
    for i in range(30):
        x_history.append(params['x'])
        y_history.append(params['y'])
        
        grads['x'], grads['y'] = df(params['x'], params['y'])
        optimizer.update(params, grads)
    

    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)
    
    X, Y = np.meshgrid(x, y) 
    Z = f(X, Y)
    
    # for simple contour line  
    mask = Z > 7
    Z[mask] = 0
    
    # plot 
    plt.subplot(2, 2, idx)
    idx += 1
    plt.plot(x_history, y_history, 'o-', color="red")
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, '+')
    #colorbar()
    #spring()
    plt.title(key)
    plt.xlabel("x")
    plt.ylabel("y")
    
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/51968701-f59e8d00-24b5-11e9-91e3-a2bc6c123378.png)

上图中可以看到，根据不同的方法，参数更新的路径也不同。但是并不存在在所有问题都表现良好的方法，这四种方式各有优缺点。

## 1.6  基于MNIST数据集的更新方法的比

下面以手写数字识别为例子，比较上面的四种方法：

```python
# coding: utf-8
import os
import sys
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.util import smooth_curve
from common.multi_layer_net import MultiLayerNet
from common.optimizer import *


# 0:读入MNIST数据==========
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000


# 1:进行实验的设置==========
optimizers = {}
optimizers['SGD'] = SGD()
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()
#optimizers['RMSprop'] = RMSprop()

networks = {}
train_loss = {}
for key in optimizers.keys():
    networks[key] = MultiLayerNet(
        input_size=784, hidden_size_list=[100, 100, 100, 100],
        output_size=10)
    train_loss[key] = []    


# 2:开始训练==========
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in optimizers.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print( "===========" + "iteration:" + str(i) + "===========")
        for key in optimizers.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 3.绘制图形==========
markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D"}
x = np.arange(max_iterations)
for key in optimizers.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 1)
plt.legend()
plt.show()

```

```python
===========iteration:0===========
Momentum:2.36538069223
SGD:2.42815475142
Adam:2.20110242329
AdaGrad:2.16691917906

......

===========iteration:1800===========
Momentum:0.0814914810944
SGD:0.193988179678
Adam:0.0342830398485
AdaGrad:0.0333877760757
===========iteration:1900===========
Momentum:0.0479927674446
SGD:0.227371311446
Adam:0.0330315246567
AdaGrad:0.0179410672926
```

![image](https://user-images.githubusercontent.com/18595935/51968955-86756880-24b6-11e9-8f6c-4b220d8b662c.png)

从上图可以看到，与SGD相比，其他3中方法可以学习得更快，有时最终的识别精度也更高。

# 2. 权重的初始值

在神经网络的学习中，权重初始值非常重要，很多时候权重初始值的设定关系到神经网络学习能否成功。

## 2.1 权重初始值可以设为0么？

权值衰减是一种以减少权重参数的值为目的进行学习的方法，通过减小权重参数的值来抑制过拟合的发生。
之前的权重初始值都是`0.01 * np.random.randn(10, 100)`，由高斯分布生成的值乘以0.01得到的值，即标准差为0.01的高斯分布。

如果我们把权重初始值都设为0以减少权重，将导致无法正确学习，严格的说，是将所有权重设置为相同的值。

![image](https://user-images.githubusercontent.com/18595935/44036419-b3f77cd4-9f4c-11e8-8746-d3d2ff9a0d3e.png)

比如上图中，如果将第一层苹果和橘子的权重设为相同，反向传播的时候也会被进行相同的更新，因此，权重被更新为相同的值，并拥有对称的值，这使得神经网络拥有不同的权重时区了意义，为了防止权重均一化，必须随机生成初始值。

## 2.2 隐藏层的激活值分布

下面的代码，用于观察权重初始值如何影响隐藏层的激活值分布，向一个5层神经网络(激活函数使用sigmoid函数)，传入随机生成的输入数据，用直方图绘制各层激活值的数据分布。

```python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)
    
input_data = np.random.randn(1000, 100)  # 1000个数据
node_num = 100  # 各隐藏层的节点（神经元）数
hidden_layer_size = 5  # 隐藏层有5层
activations = {}  # 激活值的结果保存在这里

x = input_data

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]

    # 改变初始值进行实验！
    w = np.random.randn(node_num, node_num) * 1
    # w = np.random.randn(node_num, node_num) * 0.01
    # w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num)
    # w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)


    a = np.dot(x, w)


    # 将激活函数的种类也改变，来进行实验！
    z = sigmoid(a)
    # z = ReLU(a)
    # z = tanh(a)

    activations[i] = z

# 绘制直方图
for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    if i != 0: plt.yticks([], [])
    # plt.xlim(0.1, 1)
    # plt.ylim(0, 7000)
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()

```

![image](https://user-images.githubusercontent.com/18595935/51970574-a149dc00-24ba-11e9-9e55-bddb2e0ad59e.png)

上图就是使用标准差为1的高斯分布作为权重初始值时的各层激活值的分布。由图可知，各层的激活值不断偏向0和1，随着不断靠近0和1，sigmoid函数导数的值逐渐接近0，这样会造成反向传播中梯度的值不断变小，最后消失，这就是**梯度消失问题**,层次越深，梯度消失越严重。


如果将标准差修改为0.01，呈集中在0.5附近的分布，激活值的分布有所偏向，说明在表现力上会有很大问题。

- 标准差修改为0.01时的分布：
![image](https://user-images.githubusercontent.com/18595935/51970810-2c2ad680-24bb-11e9-8f02-758159a0cef9.png)

- 标准差修改为0.1时的分布：
![image](https://user-images.githubusercontent.com/18595935/51970821-3220b780-24bb-11e9-8559-88d6ba481f0c.png)

**Xavier初始值：**

Xavier的论文中，为了使各层的激活值呈现具有相同广度的分布，推导了合适的权重尺度，结论是，如果前一层的节点数为n，则初始值用标准差为1/sqrt(t)的分布，修改代码如下：

```python
w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num)
```

![image](https://user-images.githubusercontent.com/18595935/51971228-018d4d80-24bc-11e9-9d3b-cf1095f3f29e.png)

使用Xavier初始值后，前一层的节点数越多，要设定为目标节点的初始值的权重尺度越小。

![image](https://user-images.githubusercontent.com/18595935/51971320-34374600-24bc-11e9-98be-b55fded2956a.png)

## 2.3 ReLU权重初始值

如果激活函数是ReLU函数，下面是几种标准差值的分布对比：

- 标准差0.01
![image](https://user-images.githubusercontent.com/18595935/51972869-c2f99200-24bf-11e9-9b0a-e9ad560bbab0.png)
- 标准差 Xavier初始值
![image](https://user-images.githubusercontent.com/18595935/51972891-cbea6380-24bf-11e9-821a-5280a5b7e589.png)
- 标准差 He初始值（标准差为 sqrt(2/n)）
![image](https://user-images.githubusercontent.com/18595935/51972907-d7d62580-24bf-11e9-8330-7c468c96b760.png)

He初始值使用的代码为：

```python
w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)
```

**总结：**
1. 当激活函数为sigmoid或tanh等S型曲线函数时，初始值使用Xavier初始值
2. 当激活函数为ReLU时，权重初始值使用He初始值

## 2.4 基于MNIST数据集的权重初始值的比较

```python
# coding: utf-8
import os
import sys

sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.util import smooth_curve
from common.multi_layer_net import MultiLayerNet
from common.optimizer import SGD


# 0:读入MNIST数据==========
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000


# 1:进行实验的设置==========
weight_init_types = {'std=0.01': 0.01, 'Xavier': 'sigmoid', 'He': 'relu'}
optimizer = SGD(lr=0.01)

networks = {}
train_loss = {}
for key, weight_type in weight_init_types.items():
    networks[key] = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100],
                                  output_size=10, weight_init_std=weight_type)
    train_loss[key] = []


# 2:开始训练==========
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in weight_init_types.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizer.update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print("===========" + "iteration:" + str(i) + "===========")
        for key in weight_init_types.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 3.绘制图形==========
markers = {'std=0.01': 'o', 'Xavier': 's', 'He': 'D'}
x = np.arange(max_iterations)
for key in weight_init_types.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 2.5)
plt.legend()
plt.show()
```

```python
===========iteration:0===========
He:2.37977141155
Xavier:2.30635119752
std=0.01:2.30253529702

...

===========iteration:1800===========
He:0.166992197315
Xavier:0.274103348063
std=0.01:2.30133710348
===========iteration:1900===========
He:0.299547360141
Xavier:0.388699873789
std=0.01:2.29987822777

```

![image](https://user-images.githubusercontent.com/18595935/51973299-a578f800-24c0-11e9-89f4-211cbb2b1430.png)

上面的代码，激活函数使用ReLU，权重更新方法用的SGD，当Xavier和He初始值时学习得很顺利，std为0.01的初始值时，完全无法学习。

# 3. Batch Normalization

上一节中，发现设定合适的权重初始值，对激活值的分布有影响，能影响到学习能否顺利进行，那么，为了使各层有适当的广度，强制性的调整激活值的分布呢？

## 3.1 Batch Normalization 的算法

这个算法有三个优点：

1. 可以使学习快速进行(可以增大学习率)
2. 不那么依赖初始值
3. 抑制过拟合(降低Dropout等的必要性)

如前面所述，Batch Norm的思路是调整各层的激活值分布使其拥有适当的广度，为此，要向神经网络中插入对数据分布进行正规化的层，即batch Norm层(进行数据分布的均值为0，方差为1的正规化)：

![image](https://user-images.githubusercontent.com/18595935/51974925-664ca600-24c4-11e9-8269-788a0eb6945a.png)


![image](https://user-images.githubusercontent.com/18595935/51975347-508bb080-24c5-11e9-8f6e-ba95a451ba15.png)

1. ε是一个微小值，防止除以0的情况
2. γ和β是参数。一开始γ = 1， β = 0，然后再通过学习调整到合
适的值。

这个算法是神经网络上的正向传播，用计算图表示如下：

![image](https://user-images.githubusercontent.com/18595935/51975395-70bb6f80-24c5-11e9-99ee-7fcf7e1e5b09.png)

## 3.2 Batch Normalization的评估

使用MNIST数据集，观察使用batch Norm层和不使用batchNorm层时的学习过程变化：

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.multi_layer_net_extend import MultiLayerNetExtend
from common.optimizer import SGD, Adam

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

# 减少学习数据
x_train = x_train[:1000]
t_train = t_train[:1000]

max_epochs = 20
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.01


def __train(weight_init_std):
    bn_network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100], output_size=10, 
                                    weight_init_std=weight_init_std, use_batchnorm=True)
    network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100], output_size=10,
                                weight_init_std=weight_init_std)
    optimizer = SGD(lr=learning_rate)
    
    train_acc_list = []
    bn_train_acc_list = []
    
    iter_per_epoch = max(train_size / batch_size, 1)
    epoch_cnt = 0
    
    for i in range(1000000000):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
    
        for _network in (bn_network, network):
            grads = _network.gradient(x_batch, t_batch)
            optimizer.update(_network.params, grads)
    
        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            bn_train_acc = bn_network.accuracy(x_train, t_train)
            train_acc_list.append(train_acc)
            bn_train_acc_list.append(bn_train_acc)
    
            #print("epoch:" + str(epoch_cnt) + " | " + str(train_acc) + " - " + str(bn_train_acc))
    
            epoch_cnt += 1
            if epoch_cnt >= max_epochs:
                break
                
    return train_acc_list, bn_train_acc_list


# 3.绘制图形==========
weight_scale_list = np.logspace(0, -4, num=16)
x = np.arange(max_epochs)

for i, w in enumerate(weight_scale_list):
    print( "============== " + str(i+1) + "/16" + " ==============")
    train_acc_list, bn_train_acc_list = __train(w)
    
    plt.subplot(4,4,i+1)
    plt.title("W:" + str(w))
    if i == 15:
        plt.plot(x, bn_train_acc_list, label='Batch Normalization', markevery=2)
        plt.plot(x, train_acc_list, linestyle = "--", label='Normal(without BatchNorm)', markevery=2)
    else:
        plt.plot(x, bn_train_acc_list, markevery=2)
        plt.plot(x, train_acc_list, linestyle="--", markevery=2)

    plt.ylim(0, 1.0)
    if i % 4:
        plt.yticks([])
    else:
        plt.ylabel("accuracy")
    if i < 12:
        plt.xticks([])
    else:
        plt.xlabel("epochs")
    plt.legend(loc='lower right')
    
plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/51975741-56ce5c80-24c6-11e9-9788-15d4d11a3a4e.png)

上面实线是使用BatchNorm，虚线是不使用的情况，可以看出：

1. 使用Batch Norm后，学习更快了
2. 另外，不合适的初始值时，没有Batch Norm几乎无法学习

上述的代码中，首先生成一个BatchNorm层：

```python
bn_network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100], output_size=10, 
                                    weight_init_std=weight_init_std, use_batchnorm=True)
```

MultiLayerNetExtend类的代码示例如下：

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir) # 为了导入父目录的文件而进行的设定
import numpy as np
from collections import OrderedDict
from common.layers import *
from common.gradient import numerical_gradient

class MultiLayerNetExtend:
    """扩展版的全连接的多层神经网络
    
    具有Weiht Decay、Dropout、Batch Normalization的功能

    Parameters
    ----------
    input_size : 输入大小（MNIST的情况下为784）
    hidden_size_list : 隐藏层的神经元数量的列表（e.g. [100, 100, 100]）
    output_size : 输出大小（MNIST的情况下为10）
    activation : 'relu' or 'sigmoid'
    weight_init_std : 指定权重的标准差（e.g. 0.01）
        指定'relu'或'he'的情况下设定“He的初始值”
        指定'sigmoid'或'xavier'的情况下设定“Xavier的初始值”
    weight_decay_lambda : Weight Decay（L2范数）的强度
    use_dropout: 是否使用Dropout
    dropout_ration : Dropout的比例
    use_batchNorm: 是否使用Batch Normalization
    """
    def __init__(self, input_size, hidden_size_list, output_size,
                 activation='relu', weight_init_std='relu', weight_decay_lambda=0, 
                 use_dropout = False, dropout_ration = 0.5, use_batchnorm=False):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size_list = hidden_size_list
        self.hidden_layer_num = len(hidden_size_list)
        self.use_dropout = use_dropout
        self.weight_decay_lambda = weight_decay_lambda
        self.use_batchnorm = use_batchnorm
        self.params = {}

        # 初始化权重
        self.__init_weight(weight_init_std)

        # 生成层
        activation_layer = {'sigmoid': Sigmoid, 'relu': Relu}
        self.layers = OrderedDict()
        for idx in range(1, self.hidden_layer_num+1):
            self.layers['Affine' + str(idx)] = Affine(self.params['W' + str(idx)],
                                                      self.params['b' + str(idx)])
            if self.use_batchnorm:
                self.params['gamma' + str(idx)] = np.ones(hidden_size_list[idx-1])
                self.params['beta' + str(idx)] = np.zeros(hidden_size_list[idx-1])
                self.layers['BatchNorm' + str(idx)] = BatchNormalization(self.params['gamma' + str(idx)], self.params['beta' + str(idx)])
                
            self.layers['Activation_function' + str(idx)] = activation_layer[activation]()
            
            if self.use_dropout:
                self.layers['Dropout' + str(idx)] = Dropout(dropout_ration)

        idx = self.hidden_layer_num + 1
        self.layers['Affine' + str(idx)] = Affine(self.params['W' + str(idx)], self.params['b' + str(idx)])

        self.last_layer = SoftmaxWithLoss()

    def __init_weight(self, weight_init_std):
        """设定权重的初始值

        Parameters
        ----------
        weight_init_std : 指定权重的标准差（e.g. 0.01）
            指定'relu'或'he'的情况下设定“He的初始值”
            指定'sigmoid'或'xavier'的情况下设定“Xavier的初始值”
        """
        all_size_list = [self.input_size] + self.hidden_size_list + [self.output_size]
        for idx in range(1, len(all_size_list)):
            scale = weight_init_std
            if str(weight_init_std).lower() in ('relu', 'he'):
                scale = np.sqrt(2.0 / all_size_list[idx - 1])  # 使用ReLU的情况下推荐的初始值
            elif str(weight_init_std).lower() in ('sigmoid', 'xavier'):
                scale = np.sqrt(1.0 / all_size_list[idx - 1])  # 使用sigmoid的情况下推荐的初始值
            self.params['W' + str(idx)] = scale * np.random.randn(all_size_list[idx-1], all_size_list[idx])
            self.params['b' + str(idx)] = np.zeros(all_size_list[idx])

    def predict(self, x, train_flg=False):
        for key, layer in self.layers.items():
            if "Dropout" in key or "BatchNorm" in key:
                x = layer.forward(x, train_flg)
            else:
                x = layer.forward(x)

        return x

    def loss(self, x, t, train_flg=False):
        """求损失函数
        参数x是输入数据，t是教师标签
        """
        y = self.predict(x, train_flg)

        weight_decay = 0
        for idx in range(1, self.hidden_layer_num + 2):
            W = self.params['W' + str(idx)]
            weight_decay += 0.5 * self.weight_decay_lambda * np.sum(W**2)

        return self.last_layer.forward(y, t) + weight_decay

    def accuracy(self, X, T):
        Y = self.predict(X, train_flg=False)
        Y = np.argmax(Y, axis=1)
        if T.ndim != 1 : T = np.argmax(T, axis=1)

        accuracy = np.sum(Y == T) / float(X.shape[0])
        return accuracy

    def numerical_gradient(self, X, T):
        """求梯度（数值微分）

        Parameters
        ----------
        X : 输入数据
        T : 教师标签

        Returns
        -------
        具有各层的梯度的字典变量
            grads['W1']、grads['W2']、...是各层的权重
            grads['b1']、grads['b2']、...是各层的偏置
        """
        loss_W = lambda W: self.loss(X, T, train_flg=True)

        grads = {}
        for idx in range(1, self.hidden_layer_num+2):
            grads['W' + str(idx)] = numerical_gradient(loss_W, self.params['W' + str(idx)])
            grads['b' + str(idx)] = numerical_gradient(loss_W, self.params['b' + str(idx)])
            
            if self.use_batchnorm and idx != self.hidden_layer_num+1:
                grads['gamma' + str(idx)] = numerical_gradient(loss_W, self.params['gamma' + str(idx)])
                grads['beta' + str(idx)] = numerical_gradient(loss_W, self.params['beta' + str(idx)])

        return grads
        
    def gradient(self, x, t):
        # forward
        self.loss(x, t, train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        for idx in range(1, self.hidden_layer_num+2):
            grads['W' + str(idx)] = self.layers['Affine' + str(idx)].dW + self.weight_decay_lambda * self.params['W' + str(idx)]
            grads['b' + str(idx)] = self.layers['Affine' + str(idx)].db

            if self.use_batchnorm and idx != self.hidden_layer_num+1:
                grads['gamma' + str(idx)] = self.layers['BatchNorm' + str(idx)].dgamma
                grads['beta' + str(idx)] = self.layers['BatchNorm' + str(idx)].dbeta

        return grads
```

# 4. 正则化

## 4.1 过拟合

## 4.2 权值衰减

## 4.3 Dropout

# 5. 超参数的验证

## 5.1 验证数据

## 5.2 超参数的最优化

## 5.3 超参数最优化的实现

# 6. 小结