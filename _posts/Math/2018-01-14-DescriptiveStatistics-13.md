---
layout: post
title: Udacity-描述统计学-05-归一化(理论正态分布,Z值,归一化)
date: 2018-01-14 05:00:0
categories: 数学
tags: 统计学
---
* content
{:toc}


# 4. 相对频率分布与绝对频率分布

![image](https://user-images.githubusercontent.com/18595935/34911710-29f62998-f913-11e7-8615-8222c31f1119.png)


# 11. Z

![image](https://user-images.githubusercontent.com/18595935/34911806-17034314-f915-11e7-929a-77600b5fa6e1.png)

# 15. 对比两者的标准差

![image](https://user-images.githubusercontent.com/18595935/34911893-a9221ad0-f916-11e7-9724-3fe897f91046.png)

- 计算两个人的Z值，即与mean之间相差多少个标准差

```python
>>> 127/36
3.5277777777777777
>>> 154/60
2.566666666666667
```

从上面的计算结果看，我(facebook)比Andy更不受欢迎。

![image](https://user-images.githubusercontent.com/18595935/34911903-fc137a90-f916-11e7-8dba-410cbec8f707.png)

# 16. 标准差数量公式-Z值

![image](https://user-images.githubusercontent.com/18595935/34912088-b46039c8-f91a-11e7-9843-6e875e129808.png)

一个负的Z值表示，其原始值比平均值要小。(The original value is less than the mean.)

# 19. 归一化分布后的均值

将原始值，全部转换为对应的Z值，转换后的分布的均值为0.

![image](https://user-images.githubusercontent.com/18595935/34912136-70e93e86-f91c-11e7-9a32-7657b9cb6b1a.png)

# 20. 归一化分布后的标准偏差

![image](https://user-images.githubusercontent.com/18595935/34912166-3aa2f848-f91d-11e7-8c1c-7ffcd157473c.png)

# 21. 标准正态分布

通过下面的方式，可以将任何一个正态分布转换为标准正态分布：

Standard Normal Distribution:
- subtracting the mean,shifting it to 0.
- dividing by the standard deviation, which makes the standard deviation 1

![image](https://user-images.githubusercontent.com/18595935/34912194-dcd40a26-f91d-11e7-90c3-7d39aacce477.png)


- 加入Chris的好友数量是平均值以上2.5个标准差：

![image](https://user-images.githubusercontent.com/18595935/34912211-745cf196-f91e-11e7-86d6-c6fe1325c22b.png)

# 24. 转换为受欢迎值

![image](https://user-images.githubusercontent.com/18595935/34912241-62d71856-f91f-11e7-8b28-c8ac46822fd9.png)

# 练习1:分布的对应关系

![image](https://user-images.githubusercontent.com/18595935/34912247-9ba98f74-f91f-11e7-8e0f-5b64bdbc09ec.png)

# 练习5:使用时长的Z值

![image](https://user-images.githubusercontent.com/18595935/34912266-2e94f1f2-f920-11e7-981d-f26e2ebad357.png)


# 练习10:分数计算

![image](https://user-images.githubusercontent.com/18595935/34912286-bb076930-f920-11e7-82e7-d9a4f301a2b1.png)


# 练习14:判断对错

![image](https://user-images.githubusercontent.com/18595935/34912317-e31e3eb6-f921-11e7-9049-55ded00a653c.png)

