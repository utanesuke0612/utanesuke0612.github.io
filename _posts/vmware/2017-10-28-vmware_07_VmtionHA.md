---
layout: post
title: 四. vMotion / HA / FT简介
date: 2017-08-16 22:48:59
categories: 虚拟化(网络/存储/Cloud)
tags: vmware
---
* content
{:toc}

# 1. vMotion与vSphere HA的区别

vMotion / HA / FT 几个在功能上比较类似，但是在使用场景上各不相同，下面看看几个具体的使用场景：

(1) 需要交换物理服务器上的CPU，但是服务器上运行的服务在工作日不能停止，需要周末来做CPU的交换。又或者某台机器的负担太重，需要将一些服务移动到其他机器上去。

 `有了vMotion之后...`, 在服务正常运行(服务通常运行在虚拟机上，即物理服务器->ESXi OS->VM->Service)，在VM正常工作的情况下，将VM挂载到其他ESXi Host上。

(2) 如果物理服务器出现故障，导致服务器上的VM全部强行停止。另外，为了应对突发的事故，需要不间断的对VM进行监视。

 `有了HA之后...`，一台服务器出现故障后，HA功能发挥作用，将全部VM转移到其他服务器上。


![image](https://user-images.githubusercontent.com/18595935/32130678-c75840e6-bbd7-11e7-96a4-f145de1418a2.png)


通过上面的使用场景可以了解，vMotion是针对计划内的作业，而HA是针对突发状况的处理。
比如日常的机器维护机器检查等，可以使用vMotion的移动功能，但是HA因为是针对突发状况，需要一直保持有效状态。
另外，虚拟机在进行vMotion之后，其Mac地址和IP地址不变。

# 2. 在vSphere中完成vMotion与HA

## 2.1 vMotion的实现

vMotion指在VM运行的状态上，从一台物理主机迁移到另一台主机上。如下图:

![image](https://user-images.githubusercontent.com/18595935/32140616-bf5ece72-bcaa-11e7-8a1a-7d015249a9fb.png)

在操作上非常简单，直接选中正在运行的虚拟机，右键选中移动即可。

![image](https://user-images.githubusercontent.com/18595935/32140623-f7e1d1b8-bcaa-11e7-8ff3-9a97d8b89432.png)

为了实现vMotion，对服务器有如下要求:
1. 两台物理主机的CPU具有互换性。
2. 两台物理主机共享物理存储。

另外，
1. 虚拟机移动前后，其MAC地址和IP地址不会变化。
2. vMotion会将执行中的虚拟机内存以及系统状态都复制到目标物理主机，同时将虚拟机切换到暂停状态，复制完毕后，将虚拟机恢复运行，这样就保证了事务的一致性。
3. 根据网络状态不同，一般vMotion在几秒到几分钟内完成。

## 2.2 HA / FT的实现

在介绍HA/FT之前，需要先介绍cluster的概念，因为HA/FT的实现必须以Cluster的存在为前提。
cluster是将多台物理主机组合起来，将组合起来的服务器看作一个巨大的资源池。

![image](https://user-images.githubusercontent.com/18595935/32140680-eea160b2-bcac-11e7-9154-503f53c16876.png)

实际工作中将16台相同构成的物理主机组成一个Cluster，将cluster上的HA功能有效化后，就能将这个Cluster内的虚拟机置于HA的保护下。
FT是针对单个虚拟机的设置，虚拟机的FT有效化后，能自动在其他物理主机内复制一个。

- HA（「High Availabili）高可用

预先将该Cluster的HA启用后，如果一台服务器出现了故障，能迁移到该Cluster的其他host，并自动重启，这样约耗费几分钟的时间。

![image](https://user-images.githubusercontent.com/18595935/32140719-2dc502ca-bcae-11e7-9a0d-9c098ade2007.png)

- FT（Fault Tolerance）容错性

即一台虚拟机所在的物理主机出现故障后，这台虚拟机上的服务也不会中断。如下图，因为不断的将被设定了FT的虚拟机进行同步到另一台物理主机上。

![image](https://user-images.githubusercontent.com/18595935/32140734-ccb5f092-bcae-11e7-8473-90f56b40069a.png)


# 3. vMotion/HA/FT总结

|功能|目的|设置对象|VM是否停止|停止时间|设定|
|:--|--:|:--:|:--:|:--:|:--:|
|vMotion|应对计划内的VM移动|VM|否|0|手动指定目的地主机|
|HA|物理服务器故障|Cluster(cluster要再构成)|`有`|`几分钟`|自动failover|
|FT|物理服务器故障|VM|否|0|自动failover|
