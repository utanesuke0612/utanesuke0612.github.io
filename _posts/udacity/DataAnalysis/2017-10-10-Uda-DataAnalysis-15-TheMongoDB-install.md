---
layout: post
title: Uda-DataAnalysis-15-[扩展]-MongoDB在32bit window7上的安装
date: 2017-10-8 04:00:00
categories: 数据分析
tags: MongoDB Udacity DataAnalysis 
---
* content
{:toc}

家里的PC是64位，很简单的就把MongoDB安装上去了，但是公司的电脑是32bit，为了把mongoDB安装并启动起来，可是费了一番功夫。

中间出错的过程就不记述了，这个也只是做个memo备忘，以后出现类似问题不用到处找了。

# 1. 找到MongoDB的32bit版

官网download首页上的版本，都是64bit版的，通过如下的链接找到了对应的32bit版。

 > https://fastdl.mongodb.org/win32/mongodb-win32-i386-3.2.17.zip

上面的link最后的版本后可以自己修改，以获得最新的版本。

# 2. 解压到本地

1. 将上面的解压到 C:\mongodb中

2. 在mongodb中新建一个文件夹 db，存储数据

# 3. 启动mongodb

1. 这里是32bit与64bit的区别部分，启动cmd，跳转到 上面的mongodb\bin目录，执行```mongod -dbpath c:\mongodb\db --storageEngine=mmapv1```，启动mongdb服务器。
2. 启动完毕后，在bin目录中打开mongo.exe，这个是mongo的shell，通过它与mongodb进行交互。
3. 为了方便，可以mongodb目录下新建一个bat文件，写入```c:\mongodb\bin\mongod -dbpath c:\mongodb\db --storageEngine=mmapv1```，以后直接通过这个bat直接启动mongodb服务器。

# 4. 使用mongo shell

1. 显示当前的所有db，```show dbs```
2. 切换 ```use mydb```
3. 显示该db中的所有集合，```db.getCollectionNames()```
