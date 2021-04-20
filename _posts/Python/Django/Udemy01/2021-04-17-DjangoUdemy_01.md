---
layout: post
title: Djangoの基礎をマスターして、3つのアプリを作ろう
date: 2021-04-17 01:01:01
categories: Python
tags: Django
---
* content
{:toc}

> 本课Udemy Course: [【徹底的に解説！】Djangoの基礎をマスターして、3つのアプリを作ろう！](https://www.udemy.com/course/django-3app/learn/lecture/14152325#overview)

> 参考Linux命令:[linux-01-Linux基础命令(1)](http://road2ai.info/2017/11/26/linux_01/)

> 参考course: [Djangoスキルアップ講座](https://zeroichicollege.com/course/django-skillup)

> 难易度高点的:[Django Core - A Reference Guide to Core Django Concepts](https://www.udemy.com/course/django-core/)

> 参考以前的blog: [DjangoBasic-01-环境部署](http://road2ai.info/2020/05/02/DjangoBasic_01/)

> 参考以前的blog：[自强学堂-Django基础教程(1)-视图与URL](http://road2ai.info/2020/05/02/zqxt_django_01/)

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

2. PowerShellを管理者権限で実行します。

3. PowerShellのターミナル上で、以下のコマンドを実行して下さい。

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

安装完毕后确认版本：

```python
junli@LAPTOP-T3CVDQDD:~$ python3 -m django --version
2.2.12
```

## [任意] 仮想環境の構築

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

## 1. startproject 

- 删除文件夹 `rmdir`，如果目录中有文件的话，使用`rm -r`进行删除
- 新建文件夹 `mkdir`
- 跳转目录 `cd`
- 确认目录 `ls`

```python
# 创建新的Django project
junli@LAPTOP-T3CVDQDD:~/DjangoStudy/UdemyPJ01$ django-admin startproject helloworldproject
junli@LAPTOP-T3CVDQDD:~/DjangoStudy/UdemyPJ01$ ls
helloworldproject
junli@LAPTOP-T3CVDQDD:~/DjangoStudy/UdemyPJ01$ cd helloworldproject/

# 启动Local WebServer
junli@LAPTOP-T3CVDQDD:~/DjangoStudy/UdemyPJ01/helloworldproject$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

April 19, 2021 - 06:54:09
Django version 2.2.12, using settings 'helloworldproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## startprojectでできるファイル

![image](https://user-images.githubusercontent.com/18595935/115212851-e90cba80-a13b-11eb-8d8c-1a516edf879b.png)

### settings.pyファイルの中身
Django 的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。

### urls.pyファイル
网址入口，关联到对应的views.py中的一个函数，访问网址就对应一个函数。

### views.pyファイル
处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。


