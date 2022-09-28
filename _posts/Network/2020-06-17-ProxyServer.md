---
layout: post
title: ProxyServer构建与UiPath中的连接测试
date: 2020-06-17 01:00:00
categories: Infra技术
tags: 网络 RPA
---
* content
{:toc}

最近在某客户的RPA项目实施中，需要在客户的内部网络中，使用UiPath调用某AI OCR的Web API，但是客户的内部网络是「ProxyServerのパスポート付き認証」，为了对应ProxyServer，在本机上构建了一套类似的环境。

# 1. 环境结构

![image](https://user-images.githubusercontent.com/18595935/84871282-4fa7ee80-b0bb-11ea-9cd9-e877e7375e54.png)

- Client PC

客户端PC，类似于客户内部网络中员工所用的机器，该机器的IE中的设定了ProxyServer的IP和Port之后，就可以通过ProxyServer连接到Internet了。

- Proxy Server

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

- 打开Firefox时，会弹出这样一个画面，要求输入ProxyServer的用户名和密码：

![image](https://user-images.githubusercontent.com/18595935/84875299-c1366b80-b0c0-11ea-9e9d-6cde29347026.png)

- 正确输入后，就可以访问自定网站了，比如访问百度，可以显示出百度网页

![image](https://user-images.githubusercontent.com/18595935/84876917-ca283c80-b0c2-11ea-9701-12932353a968.png)

另外，在Proxy Server中，也可以看到这个访问履历：

![image](https://user-images.githubusercontent.com/18595935/84876764-8df4dc00-b0c2-11ea-9b9a-013218018665.png)

上面的显示 `via 10.0.2.15`，这是proxy server的外网IP：

![image](https://user-images.githubusercontent.com/18595935/84877311-4f135600-b0c3-11ea-99ae-65e9139cfbde.png)


通过上述方式可以确认Proxy Server设定成功，也已经开始运行了。

# 5. 补足：创建一个WebSever

有时需要自己创建另一个WebServer，可以在Proxy Server上创建一个，环境结构如下：

![image](https://user-images.githubusercontent.com/18595935/84878053-42dbc880-b0c4-11ea-8aaa-bdd1c6357986.png)

在Client PC上访问`http://192.168.56.101:8000/`，可以显示：

![image](https://user-images.githubusercontent.com/18595935/84878169-6e5eb300-b0c4-11ea-913a-7fbddfbf6a6c.png)

该WebServer通过Python创建，只需要几行代码，非常方便：

```python
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
```

然后cmd中启动即可：

```python
C:\该py所在目录\ > py pythonServerTester.py
```

# 6. 补足：在UiPath中进行ProxServer认证

使用Vb.net Code，在进行WebAPI访问的时候，设定WebProxy：

```csharp
Dim client As New RestSharp.RestClient(in_URL.TrimEnd("/"c, " "c, "　"c) + "/ConsoleWeb/api/v1/reading/units")
Dim myProxy As New System.Net.WebProxy(in_ProxyURL)
Dim myCredential As New System.Net.NetworkCredential(in_ProxyUserName, in_ProxyPassword)

client.Proxy = myProxy
client.Proxy.Credentials = myCredential

Dim request As New RestSharp.RestRequest(RestSharp.Method.GET)
request.AddHeader("X-ConsoleWeb-ApiKey", in_ApiKey)
request.AddParameter("readingUnitId", in_UnitID.ToString)

Dim response As RestSharp.IRestResponse = client.Execute(request)
out_Response = response.Contentt
```