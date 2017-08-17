---
layout: post
title: DjangoBasic-01-环境部署
date: 2017-08-11 11:45:59
categories: Python
tags: DjangoBasic Git
---
* content
{:toc}

>[DjangoGirls tutorial](https://tutorial.djangogirls.org/zh/django_urls/)的入门课程,这个课程非常浅显易懂，完全小白只要参考这个系列，也能做出自己的博客网站。

本系列参考上面的tutorial，进行了部分修改和增补，系列目录如下,代码参考 [here](https://github.com/utanesuke0612/pythonBlog)：
1.  运行环境部署
2.  显示出你的第一个网页
3.  模板扩展-blog详情页面
4.  Django表单
5.  添加草稿/发布/删除/编辑功能
6.  让网站更安全
7.  给网页添加评论


---


# 1. 在IDCF上创建Ubuntu服务器

1.  登录IDCF，注册账号，按如下配置生成VM:
 - SSH必要 *(注意保存SSH文件)*
 - Ubuntu Server 16.04 LTS 64-bit 無償
2.  进入该VM的控制台，修改密码。
 - 进入控制台时需要输入初始密码，初始密码会由IDCF发送至注册时的邮箱。
 - 用`passwd`命令，在控制台中修改密码。
3. 在Firewall和portforward中添加允许端口号，如下表

| コメント    |     ソースCIDR| タイプ  | ポートレンジ |
| :-------- | --------:| :------: |:------: |
| HTTP8000   |   Any |  TCP  |8000|
| HTTP   |   Any |  TCP  |80|
| SSH   |   Any |  TCP  |22|

| コメント    |     パブリックポート| プライベートポート  |
| :-------- | --------:| :------: |
| HTTP   |   TCP |  8000  |
| HTTP   |   TCP |  80  |
| SSH   |   TCP |  22  |

在IDCF的网站上设定完毕后，就可以通过TeraTerm远程连接服务器了。


# 2. Ubuntu服务器上部署Django

1. 安装python，在Ubuntu16中自带了python，不需要另外安装
```
root@utaServer:~# python3 --version
Python 3.5.2
```
2. 安装虚拟环境
```
root@utaServer:~# mkdir djangogirls
root@utaServer:~# cd djangogirls
root@utaServer:~/djangogirls# apt-get install python3-venv
root@utaServer:~/djangogirls# python3 -m venv myvenv
root@utaServer:~/djangogirls# ls
myvenv
```
3. 启动虚拟环境，看到目录先出现`(myvenv)`说明启动成功。
```
root@utaServer:~/djangogirls# source myvenv/bin/activate
(myvenv) root@utaServer:~/djangogirls#
```

4. 安装Django
```
(myvenv) root@utaServer:~/djangogirls#　pip install django==1.11
```
5. 生成项目
```
(myvenv) root@utaServer:~/djangogirls# django-admin startproject mysite .
(myvenv) root@utaServer:~/djangogirls# ls
manage.py mysite myvenv
```
会自动在djangogirls目录下生成manage.py和mysite文件夹。
```
myste
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
 - manage.py是管理网站的脚本，可以使用它来启动一个简单的web服务器，这个对于开发调试非常有用。
 - setting.py是工程的核心配置文件。
 - urls.py是路径配置文件，可以配置URL到实际Controller的映射关系。

6. 修改配置,将TIME_ZONE修改为「ASIA/TOKYO」,并追加设定static文件。
```
(myvenv) root@utaServer:~/djangogirls/mysite# vi settings.py
```
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')#← 一行を追加
```

7.  为我们的博客系统生成DB
```
python manage.py migrate
```
出现如下消息，说明生成成功
```
Operations to perform:
  Apply all migrations: sessions, contenttypes, admin, auth
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK
```

8. 启动web服务器(确保命令执行的所在目录下有manage.py)
```
python manage.py runserver 0:8000
```
然后访问` python manage.py runserver 0:8000 `应该可以看到"It worked!
"的页面，如果访问出错，在 mysite/setting.py中添加服务器的GlobalIP：
```
ALLOWED_HOSTS = ['210.140.220.13', 'localhost', '127.0.0.1']
```


# 3. Ubuntu服务器与Github关联

1. 在Ubuntu服务器上安装git，并创建本地仓库
```
root@utaServer:~/djangogirls# cd ..
root@utaServer:~# sudo apt-get install git
root@utaServer:~# git init
Initialized empty Git repository in /root/djangogirls/.git/
root@utaServer:~/djangogirls# git config --global user.name utanesuke0612
root@utaServer:~/djangogirls# git config --global user.email utanesuke@outlook.com
```
2. djangogirls目录下创建`.gitignore`文件，输入不需要远程同步的文件
```
*.pyc
__pycache__
myvenv
db.sqlite3
.DS_Store *.pyc
```
3. Github上创建repository,完毕后复制其URL。

4. 将本地仓库与github上的库进行关联
```
root@utaServer:~/djangogirls# git remote add origin https://github.com/utanesuke0612/pythonBlog.git
```

5. 从Github上获取文件到本地
```
root@utaServer:~/djangogirls# git pull origin master
```

6. 将本地文件上传到Github
```
root@utaServer:~/djangogirls# git status
root@utaServer:~/djangogirls# git add --all
root@utaServer:~/djangogirls# git commit -m "comment"
root@utaServer:~/djangogirls# git push -u origin master
```

# 4. 本地window上部署相同的环境

1. 生成专用文件夹
```
mkdir djangogirls
cd djangogirls
```

2. 创建虚拟环境
```
C:\Users\utane\AppData\Local\Programs\Python\Python36\Python -m venv myvenv
```
3. 进入虚拟环境
```
myvenv\Scripts\activate
```
4. 安装 Django
```
pip install django==1.11
```
5. git安装
从 git-scm.com 下载Git。 在所有的安装步骤中点击"next next next"，除了第5步"Adjusting your PATH environment"，需要选择"Run Git and associated Unix tools from the Windows command-line"(底部的选项)。
除此之外，默认值都没有问题。签出时使用 Windows 风格的换行符，提交时使用 Unix 风格的换行符，这样比较好。
如果安装前开启了cmd控制台，这时git命令不生效，重启cmd控制台后就OK了。

6. 初始化本地git仓库
```
git init
git config --global user.name utanesuke0612
git config --global user.email utanesuke@outlook.com
```
7. 关联到Github的远程库，并克隆到本地
```
git remote add origin https://github.com/utanesuke0612/pythonBlog.git
git remote -v
git clone https://github.com/utanesuke0612/pythonBlog.git
```
8. 从Github上获取文件到本地
```
root@utaServer:~/djangogirls# git pull origin master
```
9. 将本地文件上传到Github
```
root@utaServer:~/djangogirls# git status
root@utaServer:~/djangogirls# git add --all
root@utaServer:~/djangogirls# git commit -m "comment"
root@utaServer:~/djangogirls# git push -u origin master
```

10. 启动服务器，访问 `http://127.0.0.1:8000/`可以看到上面相同的web页面。
```
python manage.py runserver 0:80
```


# 参考: 手动开启端口

1. 开启和关闭端口
 - ufwのインストール`$ sudo apt-get install uf
 - 現状確認`$ sudo ufw status`
 - 所有端口关闭`$ sudo ufw default DENY`
 - 根据需要开启端口,例如打开80端口和8000及22端口
```
$ sudo ufw allow 80/tcp
$ sudo ufw allow 8000/tcp
$ sudo ufw allow 22/tcp
# 下面是删除
$ sudo ufw delete allow 80/tcp
```
2. 启动web服务器，默认打开80端口
```
apt-get update
sudo apt-get install apache2
sudo /etc/init.d/apache2 start
sudo /etc/init.d/apache2 restart
sudo /etc/init.d/apache2 stop
```
访问`210.140.220.13`后可以看到apache的欢迎页面，这个是/var/www/html中的静态页面。
如果将上面的Apache的web服务器关闭，执行`python manage.py runserver 0:80`后，django的web服务器开始使用80端口，访问`210.140.220.13`可以看到同样的DjangoPage，
