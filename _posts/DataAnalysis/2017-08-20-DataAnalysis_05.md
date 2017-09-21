---
layout: post
title: PythonDataAnalysis-04-matplotlib库入门
date: 2017-08-19 20:48:59
categories: 数据分析
tags: Python 北理 DataAnalysis
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

# 1. Matplotlib库的使用

Matplotlib库由各种可视化类构成，内部结构复杂，受Matlab启发 matplotlib.pyplot是绘制各类可视化图形的命令子库，相当于快捷方式。

```python
import matplotlib.pyplot as plt

plt.plot([3,1,4,5,2])
plt.ylabel('grade')
plt.savefig('test.jpg',dpi=600) # 以PNG格式保存,dpi控制输出质量
plt.show()
```

输出图像为:

![image](https://user-images.githubusercontent.com/18595935/30594946-b0112b0c-9d8a-11e7-9b21-8114e94d4715.png)

- plt.plot()只有一个输入列表或数组时，参数被当作Y轴，X轴以索引自动生成。
- plt.plot(x,y)当有两个以上参数时，按照X轴和Y轴顺序绘制数据点。

将上面的 plot函数中的参数修改为`plt.plot([3,1,4,5,2],[1,2,3,4,5])`后，输出的图像如下：

![image](https://user-images.githubusercontent.com/18595935/30595091-2346e6c0-9d8b-11e7-88ac-be4dbf67a9cf.png)

# 2. 关于绘图区域
- plt.subplot(nrows, ncols, plot_number)
例如 `plt.subplot(3,2,4) `或`plt.subplot(324) `。
- 在全局绘图区域中创建一个分区体系，并定位到一个子绘图区域 。上面的代码中创建了一个3行2列的区域，当前绘图区域为第4部分。

![image](https://user-images.githubusercontent.com/18595935/30595177-6a2d28c4-9d8b-11e7-9b89-720216918596.png)

- 示例代码

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# 以0.02为间隔，从0到5之间取点，一共250个点
a = np.arange(0.0,5.0,0.02)

# 在2行一列中的第一区域绘图
plt.subplot(211)
plt.plot(a,f(a))

# 在2行一列中的第二区域绘图
plt.subplot(2,1,2)
# r--表示绘图线形
plt.plot(a,np.cos(2*np.pi*a),'r--')

plt.show()
```
> exp函数是求指数的意思

绘制图形如下：

![image](https://user-images.githubusercontent.com/18595935/30595476-490a9784-9d8c-11e7-9981-d078edbc14da.png)

# 3. plot()函数
- plt.plot(x, y, format_string, **kwargs)
1. x : X轴数据，列表或数组，可选
2. y :Y 轴数据，列表或数
3. format_string: 控制曲线的格式字符串，可选. 由`颜色字符`、`风格字符`和`标记字符`组成.
4. **kwargs : 第二组或更多(x,y,format_string)


## 3.1 format_string 详解

![image](https://user-images.githubusercontent.com/18595935/30596271-9d40240c-9d8e-11e7-9971-cca8af0bd4b3.png)

```python
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')

plt.show()

```

图像显示如下:

![image](https://user-images.githubusercontent.com/18595935/30596394-ec435664-9d8e-11e7-9ef5-37c1b3210afb.png)


# 4. pyplot中的中文显示

## 4.1 中文显示方法1

```python
import matplotlib.pyplot as plt

# 追加了声明
plt.rcParams['font.family'] = 'Simhei'
plt.plot([3,1,4,5,2])
plt.ylabel('纵轴(值)')
plt.savefig('test.jpg',dpi=600) # 以PNG格式保存,dpi控制输出质量
plt.show()

```

没有上面的字体声明的话会显示为乱码，如下是正确的显示。

![image](https://user-images.githubusercontent.com/18595935/30596622-a0b63760-9d8f-11e7-8617-b264fce897b0.png)

**关于字体**:
- 'font.family' 用于显示字体的名字
- 'font.style' 字体风格，正常'normal'或斜体'italic'
- 'font.size'字体大小，整数字号或者'large'、'x‐small'

常见中文字体有:

![image](https://user-images.githubusercontent.com/18595935/30596761-0b4637ba-9d90-11e7-93d6-993651ccdbd8.png)

## 4.2 中文显示方法2
下面的方法能够进行个别的设置:

```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Simhei'
plt.plot([3,1,4,5,2])
plt.ylabel('纵轴(值)',fontproperties='SimHei',fontsize=20)
plt.xlabel('横轴(值)',fontproperties='SimHeiSimHei',fontsize=10)
plt.savefig('test.jpg',dpi=600) # 以PNG格式保存,dpi控制输出质量
plt.show()

```

X和Y方向的字大小不一致，如下图:

![image](https://user-images.githubusercontent.com/18595935/30597280-7f5c5c6e-9d91-11e7-8522-29915348dc9b.png)


# 5. pyplot的文本显示函数

常用的文本显示函数如下:

![image](https://user-images.githubusercontent.com/18595935/30597906-5d39a11c-9d93-11e7-85a4-4c2418d40bbe.png)

```python
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.ylabel('纵轴(值)',fontproperties='SimHei',fontsize=20,color='green')
plt.xlabel('横轴(值)',fontproperties='SimHei',fontsize=20)

# $是一种Latex语法
plt.title(r'正弦波示例 $y=cos(2\pi x)$',fontproperties='SimHei',fontsize=25)
plt.text(2,1,r'$\mu=100$',fontsize=15)

# 使数字前的负号能正确显示
plt.rcParams['axes.unicode_minus'] = False

plt.axis([-1,6,-2,2])

plt.grid(True)

plt.show()

```

显示图像如下:

![image](https://user-images.githubusercontent.com/18595935/30598634-3d8af134-9d95-11e7-84a7-18c0886603e8.png)


还可以显示标注，如将上面的text函数部分修改为如下后

```python
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='blue',shrink=0.1,width=2))
```

图像显示为:

![image](https://user-images.githubusercontent.com/18595935/30598825-ced3819c-9d95-11e7-92c1-2e5b704eab52.png)

# 6. pyplot的复杂子绘图区域
通过函数`plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)`能构建更复杂的绘图区域。如下图

![image](https://user-images.githubusercontent.com/18595935/30598982-2d61df06-9d96-11e7-8c87-371d5426bfc1.png)

需要使用的时候再查manual吧。


# 7. 总结
使用什么函数进行绘图，都是次要的，关键是`如何选取恰当的图形展示数据含义`。
