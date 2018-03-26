---
layout: post
title: Python中级进阶(intermediatePython)
date: 2018-03-22 07:00:00
categories: Python
tags: Python
---
* content
{:toc}

> [interpy-zh-v1.3.pdf](https://github.com/eastlakeside/interpy-zh/releases)

# 02. *args 和 **kwargs

```python
def test_ver_args(f_arg,*argv):
    print("first normal arg:",f_arg)
    for arg in argv:
        print("through *argv:",arg)

test_ver_args("yahoo","google","amazon","apple")

def test_ver_2args(**argv):
    for key,value in argv.items():
        print("{0}={1}".format(key,value))

test_ver_2args(name="lijun",age=9)
```

# 03. 调试

# 04. 生成器

# 05. Map，Filter 和 Reduce

# 06. set 数据结构

# 07. 三元运算符

# 08. 装饰器

# 09. Global和Return

# 10. 对象变动 Mutation

# 11. __slots__魔法 

# 12. 虚拟环境

# 13. 容器

# 14. 枚举

# 15. 对象自省

# 16. 推导式

# 17. 异常

# 18. lambda表达式

# 19. 一行式

# 20. For - Else

# 21. 使用C扩展

# 22. open函数

# 23. 目标Python

# 24. 协程 

# 25. 函数缓存

# 26. 上下文管理器