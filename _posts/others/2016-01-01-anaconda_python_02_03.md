---
layout: post
title:  Anaconda中同时安装python2和python3的环境
date:   2016-01-01 01:08:00 +0800
categories: 其他
tag: Python
---
* content
{:toc}


> udacity上的课程是用python2.7，但是其他大部分资料中都是使用python3，所以要在anaconda环境中安装python2和python3的环境。

# 1. 当前的环境

- windows 10 64bit
- Anaconda for Windows (Python 2.7)

# 2. 配置python 3.x用的环境

- 启动anaconda 2.7环境下的 Anaconda Prompt命令行，输入如下`conda create -n py35 python=3.5 anaconda`。

- 查看当前环境

```
(C:\python2.7) C:\Users\utane>conda info -e
# conda environments:
#
py35                     C:\python2.7\envs\py35
root                  *  C:\python2.7

```

`*`标记的是有效的环境。

# 3. 切换环境

切换到python3.5环境下。

```
>activate py35
(C:\python2.7) C:\Users\utane>activate py35

(py35) C:\Users\utane>deactivate

```

`deactivate` 是退出当前环境。

或者是启动菜单下直接使用`Anaconda Prompt (py35)`。

# 4. Jupyter Notebook中Python 2 和 Python 3 的共存

要先安装kernel和用户。

```
(py35) C:\Users\utane>conda install notebook ipykernel
(py35) C:\Users\utane>ipython kernel install --user

```

完毕后，发现启动菜单中会有`Jupyter Notebook(py35)`，启动即可。
另外，以前的`Jupyter Notebook`也能照常使用。
