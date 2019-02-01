---
layout: post
title: 【书】深度学习入门-07-卷积神经网络(ing)
date: 2018-07-28 00:00:07
categories: DeepLearning
tags: DeepLearning
---
* content
{:toc}

![image](https://user-images.githubusercontent.com/18595935/52058008-e3058000-25a9-11e9-8d0a-67377e60ab7d.png)

本章非常重要，主题是卷积神经网络(Convolutional Neural Network,CNN),CNN被用于图像识别，语音识别等各种场合。

# 1. 整体结构

之前介绍的神经网络中，相邻层的所有神经元之间都有连接，这叫做“全连接(Fully-connected)”，另外我们使用的Affine层实现全连接层。

CNN中新出现了卷积层(Convolution)和池化层(Pooling)，对比的构造图如下：

![image](https://user-images.githubusercontent.com/18595935/52058940-d5e99080-25ab-11e9-9615-fe2523626abf.png)

> Affine层，进行仿射变换的处理。 神经网络的正向传播中进行矩阵的乘积运算在几何学中称为“仿射变换”。几何中，仿射变换包括一次线性变换和一次平移，分别对应神经网络的加权和运算与加偏置运算。
> ![image](https://user-images.githubusercontent.com/18595935/52058601-26142300-25ab-11e9-88f3-4441adae450e.png)

# 2. 卷积层

## 2.1 全连接层存在的问题

之前介绍的全连接神经网络中使用了全连接层(Affine层)，全连接存在什么问题呢？那就是数据的形状被忽视了，以MNIST数据集为例，高28像素长28像素的数据，会被排成一列，以784个数据的形式作为输入进行Affine层。
> 比如之前代码中的`print(x_train.shape)`，输出`(60000, 784)`

图像在空间上临近的像素为相似的值，RBG各个通道之间有密切的关联性等，这些重要的信息，因为全连接层会忽视形状，将全部的输入数据作为相同的神经元处理，所以无法利用形状相关的信息。

而卷积层可以保持形状不变，当数据数据是图像时，卷积层会以3维数据的形式接收输入数据，并同样以3维数据的形式输出到下一层。

其中，卷积层的输入数据称为**输入特征图(input feature map)**，输出数据称为**输出特征图(output feature map)**。

## 2.2 卷积运算

卷积运算相同于图像处理中的滤波器运算，如下图：

![image](https://user-images.githubusercontent.com/18595935/52060730-295ddd80-25b0-11e9-8af4-760db3940bed.png)

如上图中，输入数据和滤波器一样，都是有高长方向上的维度，输入数据维度为(4,4)，滤波器为(3,3),输出数据为(2,2)。

对于输入数据，卷积运算以一定间隔滑动滤波器窗口并应用，如上面的各个色块，逐个滑动，滑动四次，分别和滤波器的元素相乘，然后再求和，最后将这个结果保存到输出的对应位置。这个运算叫做**乘积累加运算**。

**含有偏置的卷积运算**处理如下图：
> CNN中，滤波器的参数相当于权重，下图中，向应用了滤波器的数据加上了偏置，偏置通常只有1个(1*1),这个值会被加到应用了滤波器的所有元素上。

![image](https://user-images.githubusercontent.com/18595935/52061211-2e6f5c80-25b1-11e9-8479-e3aed27945c0.png)

## 2.3 填充

上面大小为(4,4)的输入数据，使用(3,3)的滤波器时，输出大小变为了(2,2)，相当于比输入大小缩小了2个元素，如果多次进行卷积运算，那么某个时刻输出大小就有可能变为1，而导致无法再进行卷积运算。

为了避免上面的情况出现，要使用填充，调整输出的大小。

**填充**:在进行卷积层处理之前，向输入数据的周围填入固定的数据。
如下图中，对大小为(4,4)的输入数据应用了幅度为1的填充，最终生成了(4,4)的输出数据。

![image](https://user-images.githubusercontent.com/18595935/52103274-33232780-2628-11e9-9b9d-88f5ff9ebd28.png)

## 2.4 步幅

之前讨论的步幅都是1，即逐个移动滤波器的位置。如果步幅设为2，则间隔为2个元素：

![image](https://user-images.githubusercontent.com/18595935/52103342-872e0c00-2628-11e9-88ed-c0df36f451e7.png)

看上图，增大步幅后，输出大小会变小，而增大填充，输出大小会变大，写成数学式子如下：

![image](https://user-images.githubusercontent.com/18595935/52103390-c9574d80-2628-11e9-9aee-4813e5173ed5.png)

注意，S是步幅，需要保证根据上述的计算，其(H+2P-FH)能够整除S，根据深度学习框架的不同，值无法除尽时，有的会四舍五入，有的会报错无法运行。

## 2.5 3维数据的卷积运算

上面的卷积运算中，都是2维形状的数据，比如(28,28)，高和长方向上，各有28个像素点

但是图像数据是3维的，除了高和长以外，还需要处理通道方向，如下图是3维数据的卷积运算，可以发现通道方向上有多个特征图，会按照通道进行输入数据和滤波器的卷积运算，并将结果相加，从而得到输出。

需要注意的是：**在3维数据的卷积运算中，输入数据和滤波器的通道数要设为相同的值。**

![image](https://user-images.githubusercontent.com/18595935/52103519-5dc1b000-2629-11e9-8721-acd997b38e37.png)

## 2.6 结合方块思考

将数据和滤波器结合长方体的方块来考虑，3维数据的卷积运算会很容易理解，如下图：

![image](https://user-images.githubusercontent.com/18595935/52104104-315b6300-262c-11e9-984b-93000222e8ae.png)

3维数据书写顺序是(channel,height,width),上面的数据输出是1张特征图，即通道数为1的特征图，如果要在通道方向上也有多个卷积运算输出的话，需要多个滤波器(权重)：

![image](https://user-images.githubusercontent.com/18595935/52104251-e857de80-262c-11e9-8f04-21633df17707.png)

上面有FN个滤波器，最终得到形状(FN,OH,OW)的方块输出。

同样的，这里也有偏置，每个通道只有一个偏置，偏置的形状为(FN,1,1),滤波器的输出结果的形状是(FN,OH,OW)。这两个方块相加时，要对滤波器的输出结果(FN,OH,OW)按通道加上相同的偏置值。

![image](https://user-images.githubusercontent.com/18595935/52104512-581a9900-262e-11e9-9d44-f9c6e5e9deff.png)

## 2.7 批处理

神经网络的处理中进行了将输入数据打包的批处理，通过批处理，能够实现处理的高效化和学习时对mini-batch的对应。

如果卷积运算也同样进行批处理，需要按照(batch_num, channel, height, width)的顺序保存数据，那么传递的就是4维数据，处理流如下图：

![image](https://user-images.githubusercontent.com/18595935/52104599-b778a900-262e-11e9-8867-de198a3ff6a6.png)

# 3. 池化层

池化是缩小高，长方向上的空间的运算，如下图，将2*2区域集约成1个元素的处理，缩小空间大小。

![image](https://user-images.githubusercontent.com/18595935/52104688-13dbc880-262f-11e9-87d5-259da2aecdb8.png)

除了Max池化之外，还有Average池化，相对于Max池化取最大值，Average池化则是计算目标区域的平均值。

**池化层的特征：**

1. 没有需要学习的参数，池化只是从目标区域取最大值或是平均值，不存在要学习的参数。
2. 通道数不发生变化，经过池化运算，输入数据和输出数据的通道数都不会发生变化，计算时按通道独立进行的。
3. 对微小位置变化具有健壮性，池化会吸收输入数据的偏差。


# 4. 卷积层和池化层的实现

## 4.1 4维数组

CNN中各层间传递的数据是4维数据，比如下图，通过代码生成一个4为数组(mini-batch为3，表示3个输入数据，2个通道，高和长分别为4和5)：

```python
x = np.random.rand(3,2,4,5)
```

![image](https://user-images.githubusercontent.com/18595935/52105096-a16be800-2630-11e9-8b1b-af8c6d55512f.png)

## 4.2 基于im2col的展开

im2col是一个函数，能将输入数据展开以适合滤波器，具体说，对于输入数据，将应用滤波器的区域(3维方块)横向展开为1列，如下图：

![image](https://user-images.githubusercontent.com/18595935/52105547-6bc7fe80-2632-11e9-8639-4dbd054e97ed.png)

## 4.3 卷积层的实现

下面是im2col的实现代码：

```python
def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
    """

    Parameters
    ----------
    input_data : 由(数据量, 通道, 高, 长)的4维数组构成的输入数据
    filter_h : 滤波器的高
    filter_w : 滤波器的长
    stride : 步幅
    pad : 填充

    Returns
    -------
    col : 2维数组
    """
    N, C, H, W = input_data.shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1

    img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    return col
```

im2col会考虑滤波器大小，步幅，填充，将输入数据展开为2维数组，实际如下代码如下：

```python
import sys,os
sys.path.append(os.pardir)

# 批大小为1，通道为3的7*7数据
x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape) # (9, 75)

x2 = np.random.rand(10, 3, 7, 7) # 10个数据
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape) # (90, 75)
```

分别输出为(9,75)和(90,75)，第二个元素的元素个数均为75，这是滤波器(通道为3，大小为5*5)的元素个数总和。

**使用im2col来实现卷积层：**

```python
class Convolution:
    def __init__(self,W,b,stride=1,pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
    
    def forward(self,x):
        FN,C,FH,FW = self.W.shape
        N,C,H,W = x.shape
        out_h = int(1 + (H + 2*self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2*self.pad - FW) / self.stride)

        # 卷积层实现的重要部分
        col = im2col(x,FH,FW,self.stride,self.pad)
        col_W = self.W.reshape(FN,-1).T # 滤波器的展开
        out =  np.dot(col,col_W) + self.b
        
        out = out.reshape(N,out_h,out_w,-1).transpose(0,3,1,2)
        
        return out
```

1. 卷积层的初始化方法将滤波器，偏置，步幅，填充，作为参数接收。
2. 滤波器是(FN, C, FH, FW)，分别为Filter Number滤波器数量，Channel通道数，高和宽。
3. 卷积层的实现部分中，用im2col展开输入数据，并用reshape将滤波器展开为2维数组，最后计算展开后的矩阵的乘积。
4. `col_W = self.W.reshape(FN,-1).T`，将各个滤波器的方块展开为1列，这里通过reshape(FN,-1),比如，(10, 3, 5, 5)形状的数组的元素个数共有750个，指定 reshape(10,-1)后，就会转换成(10, 75)形状的数组。
5. `out = out.reshape(N,out_h,out_w,-1).transpose(0,3,1,2)`，最终将输出大小转换成合适的形状，transpose函数更改多维数组的轴的顺序，如下图示：
![image](https://user-images.githubusercontent.com/18595935/52106982-f828f000-2637-11e9-98e2-210ada57edf6.png)

以上就是卷积层的forward处理的实现。卷积层的反向传播代码如下：

```python
def col2im(col, input_shape, filter_h, filter_w, stride=1, pad=0):
    """

    Parameters
    ----------
    col :
    input_shape : 输入数据的形状（例：(10, 1, 28, 28)）
    filter_h :
    filter_w
    stride
    pad

    Returns
    -------

    """
    N, C, H, W = input_shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1
    col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

    img = np.zeros((N, C, H + 2*pad + stride - 1, W + 2*pad + stride - 1))
    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

    return img[:, :, pad:H + pad, pad:W + pad]
```

## 4.4 池化层的实现

池化层的实现与卷积层相同，都使用im2col展开输入数据，不过池化层在通道方向是独立的，这点和卷积层不同(卷积层是一个方块即一个输入数据(含多个通道)，展开为一行)。
具体说，池化的应用区域，按照通道单独展开：

![image](https://user-images.githubusercontent.com/18595935/52107390-88b40000-2639-11e9-9cb1-ce39baa00a90.png)

如上图，池化层的实现按下面三个阶段进行：

1. 将数据按照应用区域展开，一个应用区域展开为一行
2. 按行取最大值
3. 将最大值的输出，reshape成指定大小

对应代码如下：

```python
class Pooling:
    def __init__(self,pool_h,pool_w,stride=1,pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad
    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)
        
        # 展开(1)
        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h*self.pool_w)
        
        # 最大值(2)
        out = np.max(col, axis=1)
        
        # 转换(3)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)
        
        return out
```

# 5. CNN的实现

下面着手实现如下的CNN网络：

![image](https://user-images.githubusercontent.com/18595935/52108364-0d544d80-263d-11e9-86e6-14fc61985b98.png)

## 5.1 实现代码(CNN类的实现)：

网络的构成是“Convolution - ReLU - Pooling -Afne -
ReLU - Afne - Softmax”，我们将它实现为名为SimpleConvNet的类。

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import pickle
import numpy as np
from collections import OrderedDict
from common.layers import *
from common.gradient import numerical_gradient


class SimpleConvNet:
    """简单的ConvNet

    conv - relu - pool - affine - relu - affine - softmax
    
    Parameters
    ----------
    input_size : 输入大小（MNIST的情况下为784）
    hidden_size_list : 隐藏层的神经元数量的列表（e.g. [100, 100, 100]）
    output_size : 输出大小（MNIST的情况下为10）
    activation : 'relu' or 'sigmoid'
    weight_init_std : 指定权重的标准差（e.g. 0.01）
        指定'relu'或'he'的情况下设定“He的初始值”
        指定'sigmoid'或'xavier'的情况下设定“Xavier的初始值”
    """
    # input_dim―输入数据的维度：（ 通道，高，长）
    def __init__(self, input_dim=(1, 28, 28), 
                 conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1},
                 hidden_size=100, output_size=10, weight_init_std=0.01):
    	# 取出卷积层的超参数方便使用
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_size']
        filter_pad = conv_param['pad']
        filter_stride = conv_param['stride']
        input_size = input_dim[1]

        # 计算卷积层的输出大小
        conv_output_size = (input_size - filter_size + 2*filter_pad) / filter_stride + 1
        pool_output_size = int(filter_num * (conv_output_size/2) * (conv_output_size/2))

        # 初始化权重
        # 学习所需的参数是第1层的卷积层和剩余两个全连接层的权重和偏置。

        self.params = {}
        self.params['W1'] = weight_init_std * \
                            np.random.randn(filter_num, input_dim[0], filter_size, filter_size)
        self.params['b1'] = np.zeros(filter_num)
        self.params['W2'] = weight_init_std * \
                            np.random.randn(pool_output_size, hidden_size)
        self.params['b2'] = np.zeros(hidden_size)
        self.params['W3'] = weight_init_std * \
                            np.random.randn(hidden_size, output_size)
        self.params['b3'] = np.zeros(output_size)

        # 生成层
        # 从最前面开始按顺序向有序字典（OrderedDict）的 layers中添加层。
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                           conv_param['stride'], conv_param['pad'])
        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
        self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

        # 只有最后的SoftmaxWithLoss层被添加到别的变量lastLayer中。
        self.last_layer = SoftmaxWithLoss()

    # 进行推理的predict方法
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        """求损失函数
        参数x是输入数据、t是教师标签
        """
        y = self.predict(x)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        acc = 0.0
        
        for i in range(int(x.shape[0] / batch_size)):
            tx = x[i*batch_size:(i+1)*batch_size]
            tt = t[i*batch_size:(i+1)*batch_size]
            y = self.predict(tx)
            y = np.argmax(y, axis=1)
            acc += np.sum(y == tt) 
        
        return acc / x.shape[0]

    def numerical_gradient(self, x, t):
        """求梯度（数值微分）

        Parameters
        ----------
        x : 输入数据
        t : 教师标签

        Returns
        -------
        具有各层的梯度的字典变量
            grads['W1']、grads['W2']、...是各层的权重
            grads['b1']、grads['b2']、...是各层的偏置
        """
        loss_w = lambda w: self.loss(x, t)

        grads = {}
        for idx in (1, 2, 3):
            grads['W' + str(idx)] = numerical_gradient(loss_w, self.params['W' + str(idx)])
            grads['b' + str(idx)] = numerical_gradient(loss_w, self.params['b' + str(idx)])

        return grads

    def gradient(self, x, t):
        """求梯度（误差反向传播法）

        Parameters
        ----------
        x : 输入数据
        t : 教师标签

        Returns
        -------
        具有各层的梯度的字典变量
            grads['W1']、grads['W2']、...是各层的权重
            grads['b1']、grads['b2']、...是各层的偏置
        """
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W2'], grads['b2'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W3'], grads['b3'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

        return grads
        
    def save_params(self, file_name="params.pkl"):
        params = {}
        for key, val in self.params.items():
            params[key] = val
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)

    def load_params(self, file_name="params.pkl"):
        with open(file_name, 'rb') as f:
            params = pickle.load(f)
        for key, val in params.items():
            self.params[key] = val

        for i, key in enumerate(['Conv1', 'Affine1', 'Affine2']):
            self.layers[key].W = self.params['W' + str(i+1)]
            self.layers[key].b = self.params['b' + str(i+1)]
```




## 5.2 实现代码(调用CNN类进行学习)：

```python
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from simple_convnet import SimpleConvNet
from common.trainer import Trainer

# 读入数据
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)

# 处理花费时间较长的情况下减少数据 
#x_train, t_train = x_train[:5000], t_train[:5000]
#x_test, t_test = x_test[:1000], t_test[:1000]

max_epochs = 20

network = SimpleConvNet(input_dim=(1,28,28), 
                        conv_param = {'filter_num': 30, 'filter_size': 5, 'pad': 0, 'stride': 1},
                        hidden_size=100, output_size=10, weight_init_std=0.01)
                        
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=max_epochs, mini_batch_size=100,
                  optimizer='Adam', optimizer_param={'lr': 0.001},
                  evaluate_sample_num_per_epoch=1000)
trainer.train()

# 保存参数
network.save_params("params.pkl")
print("Saved Network Parameters!")

# 绘制图形
markers = {'train': 'o', 'test': 's'}
x = np.arange(max_epochs)
plt.plot(x, trainer.train_acc_list, marker='o', label='train', markevery=2)
plt.plot(x, trainer.test_acc_list, marker='s', label='test', markevery=2)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()

```

通过CNN，使得训练数据的识别率达到了99.82%，测试数据的识别率为96.1%，这是一个非常高的识别率。

```python
test acc:0.961
Saved Network Parameters!
```

![image](https://user-images.githubusercontent.com/18595935/52109223-0e3aae80-2640-11e9-9dc7-cc323529d58b.png)

如上所述，卷积层和池化层是图像识别中必备的模块，CNN可以有效读取图形中的某种特性，在手写数字识别中，可以提高识别精度。

# 6. CNN的可视化

## 6.1 第一层权重的可视化

上面示例中我们对MNIST数据集进行了简单的CNN学习，第一层卷积层的滤波器(权重)形状为(30,1,5,5)，即30个大小为5*5，通道为1的滤波器。
滤波器大小是5 × 5、通道数是1，意味着滤波器可以可视化为1通道的
灰度图像。

参考如下代码，比较学习前后学习后的权重：

```python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from simple_convnet import SimpleConvNet

def filter_show(filters, nx=8, margin=3, scale=10):
    """
    c.f. https://gist.github.com/aidiary/07d530d5e08011832b12#file-draw_weight-py
    """
    FN, C, FH, FW = filters.shape
    ny = int(np.ceil(FN / nx))

    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    for i in range(FN):
        ax = fig.add_subplot(ny, nx, i+1, xticks=[], yticks=[])
        ax.imshow(filters[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


network = SimpleConvNet()
# 随机进行初始化后的权重
filter_show(network.params['W1'])

# 学习后的权重
network.load_params("params.pkl")
filter_show(network.params['W1'])
```

![image](https://user-images.githubusercontent.com/18595935/52110032-b6517700-2642-11e9-9d69-2af5e33689ff.png)

学习前的滤波器时随机初始化的，所在黑白色的深浅没有规律，但学习后的滤波器有了规律。

卷积层的滤波器会提取边缘或斑块等原始信息，而刚才实现的CNN会将这些原始信息传递给后面的层。

## 6.2 基于分层结构的信息提取

上面的结果是针对第1层的卷积层得出的。第1层的卷积层中提取了边
缘或斑块等“低级”信息。

根据深度学习的可视化相关的研究，随着层次加深，提
取的信息（正确地讲，是反映强烈的神经元）也越来越抽象。

![image](https://user-images.githubusercontent.com/18595935/52110141-0defe280-2643-11e9-9637-85adde06f047.png)

上图是进行一般物体识别的8层CNN，这个就是AlexNet，该网络结构堆叠了多层卷积层和池化层，最后经过全连接层输出结果。

如果堆叠了多层卷积层，则随着层次加深，提取的信息也更加复杂和抽象。

# 7. 具有代表性的CNN

1. 一个是在1998年首次被提出的CNN元祖LeNet。
2. 另一个是在深度学习受到关注的2012年被提出的AlexNet。

## 7.1 LeNet

LeNet是进行手写数字识别的网络，它有连续的卷积层和池化层，最后经全连接层输出结果，和当前的CNN相比，LeNet有几个不同点：

1. 激活函数使用sigmoid，而现在的CNN主要使用ReLU函数
2. 原始的LeNet中使用采样缩小中间数据大小，而当前的CNN使用Max函数池化是主流。

![image](https://user-images.githubusercontent.com/18595935/52110343-a4240880-2643-11e9-8ddc-64b9823ec3d6.png)

## 7.2 AlexNet

AlexNet叠有多个卷积层和池化层，最后经由全连接层输出结果。虽然
结构上AlexNet和LeNet没有大的不同，但有以下几点差异。

1. 激活函数使用ReLU
2. 使用进行局部正规化的LRU(Local Response Normalization)层
3. 使用Dropout

![image](https://user-images.githubusercontent.com/18595935/52110350-ac7c4380-2643-11e9-8c0e-b5987986b3e5.png)

# 8. 小结

在图像处理领域，几乎毫无例外的都使用CNN，CNN的理解非常重要。本章内容小结如下：

1. CNN在此前的全连接层网络中，新增了卷积层和池化层。
2. 使用im2col函数可以简单，高效地实现卷积层和池化层。
3. 通过CNN的可视化，可以知道随着层次变深，提取信息就更抽象。
4. LeNet和AlexNet是CNN的代表性网络。