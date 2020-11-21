---
layout: post
title: UiPath-Acedemy-Licensing
date: 2019-04-08 01:02:01
categories: RPA
tags: RPA
---
* content
{:toc}

> This information is applicable to 2018.4 and newer versions of the UiPath Platform.

> 内部资料「Bootcamp_Day2_Licensing勉強会_20190410.pptx」有关于License很详细的介绍，可以参考。


This course is divided into two sections:
- UiPath Licensing Model
- Demo Section,License Management in Orchestrator

# 0. Summary

# 1. Section Overview

- license types
- particularities of each license type
- restrictions applicable to each license type
- which license type is suitable in various business scenarios

# 2. Platform Components

Q: What are the UiPath Platform Components and how do they work together?

- **Studio**:needs a develpment License
    - run the workflow
    - connect the local studio instance to orchestrator
- **Robots**:execute the processes designed in UiPath Studio
    - Attended Robot: Attended Licenses
        - Require human intervention,speeding up repetitive front-office tasks,they reside on the employee's workstation
        - production environments
    - Unattended Robot: Unattended Licenses
        - without people intervention,maxmizing the cost and performance benefits for any variety of back-office activity
        - production environments
    - NonProduction Robot: NonProduction Licenses
        - NonProduction robots are used in UAT environments to test
- **Orchestrator**:
    - provides remote control and monitoring

![image](https://user-images.githubusercontent.com/18595935/57781096-767f4d00-7764-11e9-8cdb-841453ccbce9.png)

![image](https://user-images.githubusercontent.com/18595935/57781214-b6463480-7764-11e9-8a53-8b3b761f6618.png)

# 3. Licensing Models

Q: What are the licensing options available for each of the UiPath Platform components?

![image](https://user-images.githubusercontent.com/18595935/57822698-a879c900-77cf-11e9-9c69-f23af42e81e0.png)

![image](https://user-images.githubusercontent.com/18595935/57822745-d8c16780-77cf-11e9-95a0-b3b17a2f3978.png)

![image](https://user-images.githubusercontent.com/18595935/57827349-00213000-77e2-11e9-853e-ed5de0d7abf5.png)


# 4. Recommended Setup and License Distribution

Discuss the relation between the different environments of the automation and the available licensing options.

1. In the Pre-Production environments(Development and Testing),**Development and NonProduciton Robot licenses are required.**
2. In the Production Environment, the Attended and Unattended robots will be working to execute the automated processes.

Please refer to the above, we have explained how it works.

Tenants:
1. Can be licensed individually.
2. Can be licensed in a centralized manner through the Host Licensing option

# 5. Standalone Licenses

![image](https://user-images.githubusercontent.com/18595935/57829062-bb4cc780-77e8-11e9-9698-8c79ad434863.png)

What are the available standalone licenses?
- Named User
- Node Locked

# 6. Summary - Licensing Matrix

![image](https://user-images.githubusercontent.com/18595935/57829165-14b4f680-77e9-11e9-8382-ce38e240f9b2.png)

# 7. Demo Section - License Management in Orchestrator

At the end of this section you will be able to:

1. Activate your Orchestrator license
2. Upload and manage your orchestrator license in both a Tenant and Host licensing scenario
3. License a standard Robot and a Floating Robot in Orchestrator
4. Set up and manage a named user,concurrent user and concurrent Runtime license in Orchestrator


# 8. how does Tenant and host licensing work in Orchestrator?

参考[Activating and Uploading your License](https://orchestrator.uipath.com/lang-ja/docs/activating-and-uploading-your-license)

# 9. Orchestrator Licensing

## 

**Web Resources**
1. [UiPath Studio Guide
About Licensing](https://studio.uipath.com/docs/about-licensing)
2. [UiPath Robot Guide
About Licensing](https://robot.uipath.com/docs/about-licensing)
3. [UiPath Orchestrator Guide
About Licensing](https://orchestrator.uipath.com/docs/about-licensing)
4. [The Ultimate RPA Glossary
Definitions to Know](https://www.uipath.com/blog/ultimate-rpa-glossary-of-terms)


# 12. DIPLOMA

![image](https://user-images.githubusercontent.com/18595935/57830763-146b2a00-77ee-11e9-9703-540fd811d234.png)



