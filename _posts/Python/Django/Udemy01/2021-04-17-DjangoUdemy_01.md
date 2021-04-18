---
layout: post
title: Djangoの基礎をマスターして、3つのアプリを作ろう
date: 2021-04-17 01:01:01
categories: Python
tags: Django
---
* content
{:toc}

> Udemy Course: [【徹底的に解説！】Djangoの基礎をマスターして、3つのアプリを作ろう！](https://www.udemy.com/course/django-3app/learn/lecture/14152325#overview)

> 参考course: [Djangoスキルアップ講座](https://zeroichicollege.com/course/django-skillup)

> 难易度高点的:[Django Core | A Reference Guide to Core Django Concepts](https://www.udemy.com/course/django-core/)

# 1. 開発環境構築

## 環境構築の全体像

使用Windows10中的`Windows subsystem for linux`，Terminal:`bash`。

インストールの流れ:

|OS|パッケージマネージャー(OSの)|Pythonのパッケージマネージャー|
|:--|--:|:--:|
|Linux(Ubuntu)|apt|pip|
|macOS|Homebrew|pip|


## `WSL`のインストール

1. Microsoft storeでubuntuを検索し、ubuntuをインストールします。

2. Microsoft storeでubuntuを検索し、ubuntuをインストールします。

3. PowerShellのターミナル上で、以下のコマンドを実行して下さい

```python
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
/norestart
```

4. Ubuntu２を実行し、ユーザー名とパスワードを入力します。(junli/w...1107)

## VSCodeのインストール

安装完VSCode后，在VSCode中连接到Ubuntu。

参考: https://code.visualstudio.com/docs/remote/wsl#_getting-started

1. 先安装 Remote - WSL 插件，然后如下图：

![image](https://user-images.githubusercontent.com/18595935/115144880-ff5a3e00-a089-11eb-96cc-3909a2e59581.png)

2. 这样会打开一个新的窗口了，如下图：

![image](https://user-images.githubusercontent.com/18595935/115144920-2284ed80-a08a-11eb-8344-a2afce016d4b.png)

## PythonとDjangoのインストール

![image](https://user-images.githubusercontent.com/18595935/115145190-4d237600-a08b-11eb-9b19-1de99244b781.png)

## （任意）仮想環境の構築1

参考这里的Guide：[Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

- 先安装 pip

`junli@LAPTOP-4KOGTOIU:~$ curl -kL https://bootstrap.pypa.io/get-pip.py | python3`

确认安装后的版本：

```python
junli@LAPTOP-4KOGTOIU:~$ python3 -m pip --version
pip 21.0.1 from /home/junli/.local/lib/python3.8/site-packages/pip (python 3.8)
```

- 后续参考 [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

# 2. Hello worldアプリ(Django3)



