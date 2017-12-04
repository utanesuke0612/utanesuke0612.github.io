---
layout: post
title: Uda-DataAnalysis-22-[扩展]-R语言实战(第二版)-19-使用ggplot2进行高级绘图
date: 2017-10-21 03:00:19
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 1. 四种图形系统

如下是R中经常使用的四种图形系统：

![image](https://user-images.githubusercontent.com/18595935/33510263-74b2db58-d74d-11e7-835a-29a98e94c606.png)


后续将用三个数据集解释ggplot2的使用：
- 第一个是从lattice包中的singer数据集，它包括纽约合唱团歌手的高度和语音变量。
- 第二个是在本书中已经使用过的mtcars数据集，它包含32辆汽车的详细信息。
- 最后一个是在第8章中讨论的car包中的Salaries数据集。Salaries数据集包含大学教授的收入信息，并用来探索性别差异对他们收入的影响。

# 2. ggplot2 包介绍 

在ggplot2中，图是采用串联起来（+）号函数创建的。每个函数修改属于自己的部分。下面给出了一个最简单的例子：

- 示例1：简单示例

1. ggplot初始化图形并指定要用到的数据来源data,和变量aes(aes:aesthetics 视觉呈现信息)
2. aes()函数指定每个变量扮演的角色
3. geom_point()表示创建一个散点图
4. labs()函数是可选函数，可添加注释(包括轴标签和标题)

```{r}
ggplot(data=mtcars,aes(x=wt,y=mpg)) + 
  geom_point() +
  labs(title="Automobile Data",x="Weight",y="Miles Per Gallon")
```

![image](https://user-images.githubusercontent.com/18595935/33513042-97866f7e-d77e-11e7-8d2f-5ba4e618ceaf.png)

- 示例2
1. geom_point函数中，pch=17表示三角形，size=2点的大小加倍
2. geom_smooth()函数增加了一条平滑的曲线，这里需要线性拟合(method="lm"),红色的虚线

```{r}
ggplot(data=mtcars,aes(x=wt,y=mpg)) + 
  geom_point(pch=17,color="blue",size=2) +
  geom_smooth(method="lm",color="red",linetype=2) + 
  labs(title="Automobile Data",x="Weight",y="Miles Per Gallon")
```

![image](https://user-images.githubusercontent.com/18595935/33513116-b73d0ac0-d77f-11e7-9601-de2b46bcdf4a.png)

- 示例3：分组和小面化(faceting)

分组指在一个图形中显示两组或多组结果，小面化是再单独并排的图形上显示观察组。
ggplot2包在定义组或面时使用因子。


先需要将am(手动，自动)，vs(V型发动机与直列式发动机)，cyl(发动机气缸数量)转化为因子


```{r}
mtcars$am <- factor(mtcars$am,levels = c(0,1),
                    labels = c("Automatic","Manual"))

mtcars$vs <- factor(mtcars$vs,levels = c(0,1),
                    labels = c("V-Engine","Straght Engine"))

mtcars$cyl <- factor(mtcars$cyl)
```


```{r}
ggplot(data=mtcars,aes(x=hp,y=mpg,shape=cyl,color=cyl)) +
  geom_point(size=3) +
  facet_grid(am~vs) +
  labs(title="Automobile Data by Engine Type",x="Horsepower",y="Miles Per Gallon")
  
```

![image](https://user-images.githubusercontent.com/18595935/33513282-cd748c52-d782-11e7-8c3e-fecd6c3cf1f1.png)

参考上面图，包含了变速箱类型，发动机类型每个组合的分离的离散点，每个点的颜色形状表示发动机气缸的数量。
在本例中，am和vs是刻面变量，cyl是分组变量。


# 3. 用几何函数指定图的类型

ggplot()函数指定要绘制的数据源和变量，几何函数则指定这些变量如何在视觉上进行表示(使用点/条/线/阴影区)，下面是常见的几何函数。

![image](https://user-images.githubusercontent.com/18595935/33513351-fde89a44-d783-11e7-8404-e4c38c0a9d2f.png)

如下是几何函数的常见选项：

![image](https://user-images.githubusercontent.com/18595935/33513357-3beef96e-d784-11e7-9e8b-fba01608ac03.png)

![image](https://user-images.githubusercontent.com/18595935/33513359-50585cc4-d784-11e7-90a9-9df1bb7eadfd.png)

- 示例1：

```{r}
data(singer,package = "lattice")

ggplot(data=singer,aes(x=height)) + geom_histogram()
```

![image](https://user-images.githubusercontent.com/18595935/33513384-0a0ba0a4-d785-11e7-9550-85a4666b7f82.png)


- 示例2：

```{r}
ggplot(data=singer,aes(x=voice.part,y=height)) + geom_boxplot()
```

![image](https://user-images.githubusercontent.com/18595935/33513400-5bc85f2c-d785-11e7-935f-f5beba88d0da.png)

上图可以看到，低音歌唱家的身高，比高音的更高。

创建直方图只用指定变量x，y默认为count，但创建箱线图变量时，变量x和y都需要指定。

- 示例3，不同学术地位对应薪水的缺口箱线图。

1. 实际的观测值(教师)是重叠的，因而给了一定的透明度0.5.
2. 使用了抖动jitter以减少重叠。
3. 最后一个地毯图在左侧显示薪水的一般扩散。


```{r}
#install.packages("car") 
data(Salaries,package = "car")
```


```{r}
ggplot(data=Salaries,aes(x=rank,y=salary)) +
        geom_boxplot(fill="cornflowerblue",
        color="black",notch=TRUE) +
        geom_point(position = "jitter",color="blue",alpha=.5) +
        geom_rug(side="1",color="black")
```

![image](https://user-images.githubusercontent.com/18595935/33513477-004fc624-d787-11e7-9d96-e8af2f89fdac.png)

从上图可以看出，助理教授/副教授/教授的工资显著不同。


# 4. 分组

# 5. 刻面

# 6. 添加光滑曲线

# 7. 修改ggplot2图形的外观

# 8. 保存图形
