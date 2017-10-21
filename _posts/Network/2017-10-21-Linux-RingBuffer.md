---
layout: post
title: Linux中网卡RingBufferSize的调整和确认
date: 2017-08-15 00:46:00
categories: 虚拟化(网络/存储/vmware)
tags: 网络
---
* content
{:toc}

# 1. 网卡的收包过程

网线上的packet首先被网卡获取，网卡取检查packet的CRC校验，保证完整性，然后将packet头去掉，得到frame。网卡会检查MAC包内的目的MAC地址，如果和本网卡的MAC地址不一样则丢弃。

然后网卡将frame拷贝到网卡内部的FIFO缓冲区(硬件缓冲,网卡与操作系统之间的缓冲)，触发硬件中断。每个网卡都有一个中断处理程序，用于通知网卡该中断已经被接收了，以及把网卡缓冲区的数据包拷贝到内存skb中，接下来的交给内核处理。

# 2. 什么是RingBuffer

如果是有ring buffer的网卡，frame先保存在ring buffer里再出发软件中断，ring buffer是网卡和驱动程序共享，是设备里的内存，但是对操作系统是可见的，内核可以直接访问，linux内核源码里网卡驱动程序使用kcalloc分配空间，所以ring buffer是有上限的，另外这个ring buffer size表示的应该是能存储的frame的个数，而不是字节大小。

网卡的ring buffer size根据不同网卡生产商，以及网卡的用途(服务器还是一般PC)其大小不同。通过调整Buffer size可以减少网卡丢包的可能性。

# 3. 如何调整Ring Buffer size

## 3.1 确认当前Ring buffer size `ethtool -g eth1`

```python
perf135:~ # ethtool -g eth1


Ring parameters for eth1:
Pre-set maximums:
RX:             4096
RX Mini:        0
RX Jumbo:       0
TX:             4096
Current hardware settings:
RX:             256
RX Mini:        0
RX Jumbo:       0
TX:             256

```

如上是确认网卡eth1的ring buffer size，输出结果中上面是预设的最大值，下面是当前设定值。

另外，在实际工作中只设定了与public internet关联的nic，即front侧的网卡，front侧的网卡随着设定的不同会变化，可以在vSphere client中查看，一般有两张网卡用于外网的连接。
- RX : Receive  eXchange(受信)
- TX : Transmit eXchange(送信)


## 3.2 调整Ring Buffer size `ethtool -G eth1 rx 4096 tx 4096`

```python
perf135:~ # ethtool -G eth1 rx 4096 tx 4096

perf135:~ # ethtool -g eth1

Ring parameters for eth1:
Pre-set maximums:
RX:             4096
RX Mini:        0
RX Jumbo:       0
TX:             4096
Current hardware settings:
RX:             4096
RX Mini:        0
RX Jumbo:       0
TX:             4096
```

上面将RX和TX都调整为了4096.


## 3.3 长久化修改Ring Buffer size

另外，请注意上面的设定在reboot后就失效了，为了将这种修改恒久化，可以修改配置文件。

```python
$ vi /etc/rc.d/rc.local

#!/bin/sh
ethtool -G eth1 rx 4096
```