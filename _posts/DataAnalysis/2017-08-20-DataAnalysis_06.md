---
layout: post
title: PythonDataAnalysis-05-matplotlib基础绘图函数示例
date: 2017-08-19 20:49:59
categories: 数据分析
tags: DataAnalysis
---
* content
{:toc}

> [PythonDataAnalysis-XX...]系列，参考[**Python数据分析与展示 嵩天@北京理工**](http://www.icourse163.org/course/BIT-1001870002)

根据第三方库内容特点，课程共分8个内容单元和4个实战单元：
 - 单元1：NumPy库入门：一维、二维、N维、高维数据表示和操作
 - 单元2：NumPy数据存取与函数：多维数据存储、随机数函数、统计函数、梯度函数
 - 单元3：**实战**：图像的手绘效果
 - 单元4：Matplotlib库的入门和基本使用
 - 单元5：Matplotlib基础绘图函数：饼图、直方图、极坐标图、散点图
 - 单元6：**实战**：引力波的绘制
 - 单元7：Pandas库入门：Series、DataFrame类型、基本操作
 - 单元8：Pandas数据特征分析：数据排序、基本统计分析、累计分析、相关分析

---
> 有非常多的图表，即使介绍了也记不住，等到需要用的时候再详细看。

# 1. pyplot基础图表函数概述

|                函数                |   说明   |
|:---------------------------------- |:-------- |
| plt.plot(x,y,fmt,...)              |绘制一个坐标图|
| plt.boxplot(data,notch,position)   |  绘制一个箱形图        |
| plt.bar(left,height,width,bottom)  |  绘制一个条形图        |
| plt.barh(width,bottom,left,height) |    绘制一个横向条形图      |
| plt.polar(theta, r)                |  绘制极坐标图        |
| plt.pie(data, explode)             |  绘制饼图        |
| plt.psd(x,NFFT=256,pad_to,Fs)      |  绘制功率谱密度图        |
| plt.specgram(x,NFFT=256,pad_to,F)  |   绘制谱图       |
| plt.cohere(x,y,NFFT=256,Fs)        | 绘制X‐Y的相关性函数         |
| plt.scatter(x,y)                   |  绘制散点图，其中，x和y长度相同        |
| plt.step(x,y,where)                | 绘制步阶图         |
| plt.hist(x,bins,normed)            | 绘制直方图         |
| plt.contour(X,Y,Z,N)               |   绘制等值图       |
| plt.vlines()                       | 绘制垂直图         |
| plt.stem(x,y,linefmt,markerfmt)    |绘制柴火图          |
| plt.plot_date()                                   |  绘制数据日期        |


# 2. pyplot饼图的绘制

```python
import matplotlib.pyplot as plt
import numpy as np

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [30,30,30,10]

# 其中一块饼离开中心
explode = (0,0.1,0,0)

# starttangle指第一个饼起始旋转的角度，逆时针旋转
plt.pie(sizes,explode = explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90)

plt.show()

```

图如下所示:

![image](https://user-images.githubusercontent.com/18595935/30643782-3df05e1e-9e4b-11e7-89c6-0f96f12a1aad.png)

在`plt.show()`调用之前，添加`plt.axis('equal')`后，饼图的形状有变化:

![image](https://user-images.githubusercontent.com/18595935/30643890-889939b8-9e4b-11e7-998c-4a5e86d425bf.png)

饼的半径相同了。





# 3. pyplot直方图的绘制

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

mu,sigma = 10,20

a = np.random.normal(mu,sigma,size=100)

plt.hist(a,20,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)

plt.title('Histogram')

plt.show()

```

![image](https://user-images.githubusercontent.com/18595935/30644155-7261d226-9e4c-11e7-95a1-e7e07cebc385.png)



# 4. pyplot极坐标图的绘制

```python
import matplotlib.pyplot as plt
import numpy as np


N = 20

theta = np.linspace(0.0,2*np.pi,N,endpoint=False)

radii = 10 * np.random.rand(N)

width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111,projection='polar')
bars = ax.bar(theta,radii,width=width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10,))
    bar.set_alpha(0.5)

plt.show()
```

![image](https://user-images.githubusercontent.com/18595935/30644952-1e24c88c-9e4f-11e7-858b-fe7b37daeff3.png)


# 5. pyplot散点图的绘制


```python
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simple Scatter')

plt.show()

```

![image](https://user-images.githubusercontent.com/18595935/30645026-63116298-9e4f-11e7-97c7-4f6e7e30b55c.png)


# 6. 绘制引力波

相关解释参考 [Github:引力波的绘制.pdf](https://github.com/utanesuke0612/utanesuke0612.github.io/blob/master/code/DataAnalysis/bjlg/DV06-%E5%AE%9E%E4%BE%8B2-%E5%BC%95%E5%8A%9B%E6%B3%A2%E7%9A%84%E7%BB%98%E5%88%B6.pdf)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate_h, hstrain= wavfile.read(r"H1_Strain.wav","rb")
rate_l, lstrain= wavfile.read(r"L1_Strain.wav","rb")
#reftime, ref_H1 = np.genfromtxt('GW150914_4_NR_waveform_template.txt').transpose()
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose() #使用python123.io下载文件

htime_interval = 1/rate_h
ltime_interval = 1/rate_l
fig = plt.figure(figsize=(12, 6))

# 丢失信号起始点
htime_len = hstrain.shape[0]/rate_h
htime = np.arange(-htime_len/2, htime_len/2 , htime_interval)
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time (seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

ltime_len = lstrain.shape[0]/rate_l
ltime = np.arange(-ltime_len/2, ltime_len/2 , ltime_interval)
pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time (seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time (seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')
fig.tight_layout()

plt.savefig("Gravitational_Waves_Original.png")
plt.show()
plt.close(fig)
```

![image](https://user-images.githubusercontent.com/18595935/30645622-3bdccb66-9e51-11e7-811c-d64ed617da6f.png)
