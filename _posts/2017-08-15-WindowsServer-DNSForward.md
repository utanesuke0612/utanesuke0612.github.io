---
layout: post
title: DNS服务器的转发及解析
date: 2017-08-15 00:45:59
categories: WindowsServer
tags: 网络
---
* content
{:toc}


# 1. 当前主机及网络配置介绍
- 管理主机: vCenter,运行vCenter，统一管理所有ESXi host，并作为其他管理系服务器(DB/跳板主机)的本地DNS服务器。
  - 作为DNS服务器，存储了管理系其他服务器和ESXi的HostName和IP地址。能直接在本地对ESXi Host和管理系Server进行域名解析。
- ESXi系: 若干台ESXi主机，采用vCenter作为DNS服务器。

- 当前管理主机vCenter能直接连接internet，即在vCenter上能查找上一级DNS服务器，对本地DNS服务器上存储之外(如通用的 www.yahoo.co.jp)的域名进行解析。

# 2.为什么要对vCenter设定DNS forward?
vCenter作为管理所有ESXI Host和其他管理系服务器的中枢，直接连接internet比较危险，需要将其internet连接断开。
但是当前vCenter作为ESXi Host和其他管理Server的DNS服务器，如果断开internet连接，就无法对非本地存储的域名进行解析了(如通用的 www.yahoo.co.jp)。

# 3. 解决方法：
给这个vCenter的DNS解析添加DNS Forward，实现在本地DNS无法解析到域名的情况下，转至这个上级的DNS Forward去继续解析。一般forward的地址设定为网关地址，通过网关统一进行DNS解析。

# 4. 影響範囲
- 变更前: 域名解析在本地DNS上完成。
- 变更后: 本地DNS服务器上存储的域名，继续能在本地DNS服务器上解析。其他的域名解析，被转到DNS Forward上添加的服务器上进行。

# 5. 域名解析流程

![image](https://user-images.githubusercontent.com/18595935/29279330-6c9e43e0-8152-11e7-9dd8-1c1366154da4.png)

1. 在浏览器中输入www.qq.com域名，操作系统会先检查自己本地的hosts文件是否有这个网址映射关系，如果有，就先调用这个IP地址映射，完成域名解析。
2. 如果hosts里没有这个域名的映射，则查找本地DNS解析器缓存，是否有这个网址映射关系，如果有，直接返回，完成域名解析。
3. 如果hosts与本地DNS解析器缓存都没有相应的网址映射关系，首先会找TCP/ip参数中设置的首选DNS服务器，在此我们叫它本地DNS服务器，此服务器收到查询时，如果要查询的域名，包含在本地配置区域资源中，则返回解析结果给客户机，完成域名解析，此解析具有权威性。
4. 如果要查询的域名，不由本地DNS服务器区域解析，但该服务器已缓存了此网址映射关系，则调用这个IP地址映射，完成域名解析，此解析不具有权威性。
5. 如果本地DNS服务器本地区域文件与缓存解析都失效，则根据本地DNS服务器的设置（是否设置转发器）进行查询，如果未用转发模式，本地DNS就把请求发至13台根DNS，根DNS服务器收到请求后会判断这个域名(.com)是谁来授权管理，并会返回一个负责该顶级域名服务器的一个IP。本地DNS服务器收到IP信息后，将会联系负责.com域的这台服务器。这台负责.com域的服务器收到请求后，如果自己无法解析，它就会找一个管理.com域的下一级DNS服务器地址(qq.com)给本地DNS服务器。当本地DNS服务器收到这个地址后，就会找qq.com域服务器，重复上面的动作，进行查询，直至找到www.qq.com主机。
6. 如果用的是转发模式，此DNS服务器就会把请求转发至上一级DNS服务器，由上一级服务器进行解析，上一级服务器如果不能解析，或找根DNS或把转请求转至上上级，以此循环。不管是本地DNS服务器用是是转发，还是根提示，最后都是把结果返回给本地DNS服务器，由此DNS服务器再返回给客户机。

例: 如下是直接通过本地DNS服务器进行的解析，但这里体现不了整个解析流程，只能反映到当前上一级主机。

```java
C:\Users\utane>nslookup www.baidu.com
Server:  UnKnown
Address:  192.168.11.1

Non-authoritative answer:
Name:    www.a.shifen.com
Address:  103.235.46.39
Aliases:  www.baidu.com
```


- 本地DNS服务器

```java
C:\Users\utane>ipconfig /all
...
   IPv4 Address. . . . . . . . . . . : 192.168.11.8(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : 2017年8月14日 23:56:27
   Lease Expires . . . . . . . . . . : 2017年8月16日 23:56:27
   Default Gateway . . . . . . . . . : 192.168.11.1
   DHCP Server . . . . . . . . . . . : 192.168.11.1
   DHCPv6 IAID . . . . . . . . . . . : 100161905
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-20-C2-71-EB-54-E1-AD-2D-45-B9
   DNS Servers . . . . . . . . . . . : 192.168.11.1
   NetBIOS over Tcpip. . . . . . . . : Enabled
...
```

## 6. 本地DNS配置转发与未配置转发数据包分析

1. 新建一DNS
2. DNS服务器不设转发
在192.168.145.228服务器上安装上wireshark软件，并打开它，设置数据包为UDP过滤，在192.168.145.12客户机上用nslookup命令查询一下www.sohu.com，马上可以看到本地DNS服务器直接查全球13台根域中的某几台，然后一步步解析，通过递代的方式，直到找到www.sohu.com对应的IP为220.181.118.87。
本地DNS服务器得到www.sohu.com的IP后，它把这个IP返回给192.168.145.12客户机，完成解析。
![image](https://user-images.githubusercontent.com/18595935/29279359-7f44502a-8152-11e7-8a78-2e7692e40d21.png)

3. DNS服务器设置转发

   ![image](https://user-images.githubusercontent.com/18595935/29279383-9102dbe2-8152-11e7-8523-936c44b4a49f.png)

 因www.sohu.com域名在第一步的验证中使用过，有缓存，为了不受上步实验干扰，我们在客户机上192.168.145.12上nslookup www.baidu.com。从图上看，本地DNS把请求转发至192.168.133.10服务器，133.10服务器把得到的IP返回给本地DNS，然后本地DNS再把IP告诉DNS客户机，完成解析。

  ![image](https://user-images.githubusercontent.com/18595935/29279398-9daa6702-8152-11e7-8507-fafa93180a19.png)

 >参考 http://369369.blog.51cto.com/319630/812889
