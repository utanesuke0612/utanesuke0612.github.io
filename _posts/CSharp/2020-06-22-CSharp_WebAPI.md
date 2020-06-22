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

# 2. 示例代码(exe执行)：

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

# 3. 示例(nupkg导入UiPath使用)

示例代码：

```csharp

    public class ReadingUnitsExport : CodeActivity
    {
        protected override void Execute(CodeActivityContext context)
        {
            throw new NotImplementedException();
        }
    }

    public class SorterAdd : CodeActivity
    {
        protected override void Execute(CodeActivityContext context)
        {
            throw new NotImplementedException();
        }
    }

    public class SorterSend : CodeActivity 
    {
        protected override void Execute(CodeActivityContext context)
        {
            throw new NotImplementedException();
        }
    }

    public class SorterSorting : CodeActivity
    {
        protected override void Execute(CodeActivityContext context)
        {
            throw new NotImplementedException();
        }
    }

    public class SorterStatus : CodeActivity
    {
        protected override void Execute(CodeActivityContext context)
        {
            throw new NotImplementedException();
        }
    }

    //
    public class ReadingPagesAdd: DXSuiteCloudBase
    {
        [Category("Input")]
        [RequiredArgument]
        public InArgument<string> DocumentID { get; set; }
        
        [Category("Input")]
        [RequiredArgument]
        public InArgument<string> FilePath { get; set; }

        // オプション
        [Category("Option")]
        public InArgument<int> UnitID { get; set; }

        // 
        [Category("Output")]
        //public OutArgument<JObject> JsonResponse { get; set; }
        public OutArgument<string> StringResponse { get; set; }

        protected override void Execute(CodeActivityContext context)
        {
            HttpRequstPageAdd(context);
        }

        private void HttpRequstPageAdd(CodeActivityContext context) 
        {
            var in_APIKey = APIKey.Get(context);
            var in_URL = URL.Get(context);
            var in_DocumentID = DocumentID.Get(context);
            var in_FilePath = FilePath.Get(context);

            var in_UnitID = UnitID.Get(context);

            var in_ProxyUserName = ProxyUserName.Get(context);
            var in_ProxyPassword = ProxyPassword.Get(context);
            var in_ProxyURL = ProxyURL.Get(context);

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
            Console.WriteLine("run:ReadPagesAdd: {0}", out_Response);

            // 
            Console.WriteLine("APIKey: {0}", in_APIKey);
            Console.WriteLine("in_URL: {0}", in_URL);
            Console.WriteLine("in_DocumentID: {0}", in_DocumentID);
            Console.WriteLine("in_FilePath: {0}", in_FilePath);
            Console.WriteLine("in_UnitID: {0}", in_UnitID);
            Console.WriteLine("in_ProxyUserName: {0}", in_ProxyUserName);
            Console.WriteLine("in_ProxyPassword: {0}", in_ProxyPassword);
            Console.WriteLine("in_ProxyURL: {0}", in_ProxyURL);

            //
            StringResponse.Set(context,out_Response);
        }
    }
}
```

按照 [使用C#编写UiPath中的Activity](http://road2ai.info/2020/06/18/UiPathC-_Activity/)中的方式，使用NuGet Package Explorer生成nupkg文件。

![image](https://user-images.githubusercontent.com/18595935/85259725-80659a80-b4a4-11ea-9833-b8e3b9b58501.png)

然后在UiPath中导入该文件，既可以使用了：

![image](https://user-images.githubusercontent.com/18595935/85259882-c3c00900-b4a4-11ea-94db-b323d10fdf81.png)

