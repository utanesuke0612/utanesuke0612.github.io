---
layout: post
title: Linux中加载外部存储
date: 2017-10-30 22:48:59
categories: 虚拟化(网络/存储/vmware)
tags: vmware
---
* content
{:toc}


将一个外部存储，比如U盘插到一台PC上，如果PC的OS是windows，那么windows会自动识别并加载U盘，但是Linux中是不自动加载的，需要手动加载，另外，如果PC重新启动后，手动加载的外部存储又会无法识别，需要修改对应的设定文件，以保证在下次重启后仍然能加载即mount该外部存储。

# 1. 手动加载外部存储

```python
# 首先新建一个mount point，即挂载点 
mkdir /mnt/1

# 将存储设备sdb1 mount到上面新建的mount point上
mount /dev/sdb1 /mnt/1
    
# 确认是否mount成功
df -h
```

# 2. 为了保证每次重启都加载该外部存储

```python
# 确认该文件中当前有哪些存储被mount
cat /etc/fstab

# 添加上面的外部存储到设定文件中
vi /etc/fstab

# 下面是需要追加的list，后面的参数根据要求修改
/dev/sdb1 /mnt/1 nfs   defaults   1 2
```

这样在重启后就能保证外部存储sdb1被自动mount。