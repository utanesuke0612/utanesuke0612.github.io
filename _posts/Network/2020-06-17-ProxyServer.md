---
layout: post
title: ProxyServer构建与UiPath中的连接测试
date: 2020-06-17 01:00:00
categories: 虚拟化(网络/存储/Cloud)
tags: 云服务,网络,RPA
---
* content
{:toc}

最近在某客户的RPA项目实施中，需要在客户的内部网络中，使用UiPath调用某AI OCR的Web API，但是客户的内部网络是「ProxyServerのパスポート付き認証」，为了对应ProxyServer，在本机上构建了一套类似的环境。

# 1. 环境结构

![image](https://user-images.githubusercontent.com/18595935/84871282-4fa7ee80-b0bb-11ea-9cd9-e877e7375e54.png)

1. Client PC

客户端PC，类似于客户内部网络中员工所用的机器，该机器的IE中的设定了ProxyServer的IP和Port之后，就可以通过ProxyServer连接到Internet了。

2. Proxy Server

在客户端PC上创建了一个虚拟机，在该虚拟机上安装了一个ProxyServer的软件之后，用该虚拟机充当ProxyServer的角色。

# 2. Proxy Server设定

安装工具 CCProxy8.0后，按照下面的方式进行设定：

- Port関連設定

![image](https://user-images.githubusercontent.com/18595935/84874194-386b0000-b0bf-11ea-9680-76f631323c5a.png)

- 制限関連設定

![image](https://user-images.githubusercontent.com/18595935/84874206-3dc84a80-b0bf-11ea-941c-9c55dc476831.png)

- WindowsOSのFirewall設定

![image](https://user-images.githubusercontent.com/18595935/84874216-41f46800-b0bf-11ea-9130-7c299052d139.png)

# 3. Client PC设定

打开IE的Internet Option:

![image](https://user-images.githubusercontent.com/18595935/84874675-ec6c8b00-b0bf-11ea-8176-a825263681e4.png)

如下面的画面中，设定ProxyServer的IP和设定的Port：

![image](https://user-images.githubusercontent.com/18595935/84874810-17ef7580-b0c0-11ea-89e3-bde937b385db.png)


# 4. 运行确认


