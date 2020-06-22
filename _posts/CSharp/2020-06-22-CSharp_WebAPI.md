---
layout: post
title: C#中调用WebAPI
date: 2020-06-22 01:01:01
categories: CSharp
tags: CSharp Python
---
* content
{:toc}

# 1. 添加需要的库

这段C#代码中使用了两个库，分别是Newtonsoft.Json和RestSharp，添加方式为：

![image](https://user-images.githubusercontent.com/18595935/85247320-53a38a00-b488-11ea-8c82-8db4b279b986.png)

# 2. 示例代码：

```csharp
using System;
using System.Linq;
using System.Threading.Tasks;
using System.IO;
using System.Net.Http;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System.Net;
using RestSharp;

namespace ConsoleApp
{
    class Reading_Pages_Add
    {
        string in_APIKey = "******";
        string in_URL = "https://uipath001.dx-suite.com/";
        string in_DocumentID = "306418";
        string in_FilePath = @"C:\Users\jun.li\OneDrive - UiPath\03.Customer\09.KDDI\2020年2月_AI-OCR☓UiPath PoC案件\03_AI OCR関連資料\01.アセスメント化\01.Sample帳票\請求書1.pdf";
        int in_UnitID = 0;

        string in_ProxyUserName = "lijun";
        string in_ProxyPassword = "123456";
        string in_ProxyURL = @"http://192.168.56.101:808/";

        JObject out_JsonResponse;

        public JObject Run()
        {
            RestClient client = new RestSharp.RestClient(in_URL.TrimEnd('/', ' ', '　') + "/ConsoleWeb/api/v1/reading/pages/add");
            WebProxy myProxy = new System.Net.WebProxy(in_ProxyURL);
            NetworkCredential myCredential = new System.Net.NetworkCredential(in_ProxyUserName, in_ProxyPassword);

            client.Proxy = myProxy;
            client.Proxy.Credentials = myCredential;

            RestRequest request = new RestSharp.RestRequest(RestSharp.Method.POST);
            request.AddHeader("X-ConsoleWeb-ApiKey", in_APIKey);
            request.AddParameter("documentId", in_DocumentID);

            request.AddFile("file", in_FilePath);

            IRestResponse response = client.Execute(request);
            string out_Response = response.Content;

            Console.WriteLine("run:ReadPagesAdd: {0}",out_Response);
            return out_JsonResponse;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Reading_Pages_Add readPagesAdd = new Reading_Pages_Add();
            readPagesAdd.Run();
            Console.ReadKey();
        }
    }
}

```