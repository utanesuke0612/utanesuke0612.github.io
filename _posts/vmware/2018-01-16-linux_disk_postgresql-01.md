---
layout: post
title: LinuxでDisk追加してPostgresqlDBの保存場所を変更
date: 2018-01-14 00:00:09
categories: Infra技术
tags: linux
---
* content
{:toc}

# 1. 背景

サーバーを作成するときに、root diskの容量が15Gしかなくて、アプリのインストールやDBデータの増加などに伴って、ディスク容量もう満杯になってしまいました。

# 2. 解決方法

もう一個DataDisk 100Gを作成して、DBの保存場所をroot disk から data diskへ変更する。

# 3(1). 新しいディスクをAttachして、マウントする

- IDCFサイトでDatadisk 100Gのボリュームを作成して、サーバーへAttachする。

- サーバーのSSH経由で、現在AttachされたDiskを確認する。

```python
[root@CMDBServerDev01 dev]# lsblk -o KNAME,TYPE,SIZE,MODEL
KNAME TYPE  SIZE MODEL
sda   disk   15G Virtual disk
sda1  part   15G
sdb   disk  100G Virtual disk
sr0   rom  1024M VMware IDE CDR00
```

- 記のコマンドを実行してマウントするつもりでしたが、エラーになってしまった。 

```python
[root@CMDBServerDev01 mnt]# mount /dev/sdb /mnt/dbdisk
mount: /dev/sdb is write-protected, mounting read-only
mount: unknown filesystem type '(null)'
```

- 上記エラーの原因が下記の二つあります、先に進める前にこれを解決しなければならない：
	
	1. パーティションがない
	2. ファイルシステムが作成されていない

- パーティションを作成する：

```python
[root@CMDBServerDev01 dev]# fdisk/dev/sdb
```

- ファイルシステムを作成する：

```python
[root@CMDBServerDev01 dev]# mkfs -t ext3 -c /dev/sdb
```

- 再度マウントする：

```python
[root@CMDBServerDev01 dev]# mount /dev/sdb /mnt/dbdisk
```

- df でマウントされたディスクを確認する：

```python
[root@CMDBServerDev01 dbdisk]# df
ファイルシス   1K-ブロック     使用   使用可 使用% マウント位置
/dev/sda1         15717376 14251340  1466036   91% /
devtmpfs           4071064        0  4071064    0% /dev
tmpfs              4080276        4  4080272    1% /dev/shm
tmpfs              4080276     8656  4071620    1% /run
tmpfs              4080276        0  4080276    0% /sys/fs/cgroup
tmpfs               816056        0   816056    0% /run/user/0
/dev/sdb         103081248    61180 97777188    1% /mnt/dbdisk
```

- 上記のマウントがOS再起動したら消えちゃうので、下記のファイルに設定して起動時自動マウントする:

```python
[root@CMDBServerDev01 dbdisk]# vi /etc/fstab
# 下記のを追加する：
/dev/sdb /mnt/dbdisk ext3   defaults   1 2
```

- 再起動めんどくさくて、fstabに書いた内容をすぐに反映させたい。

```python
[root@CMDBServerDev01 dbdisk]# sudo mount -a
```

- mountされたディスクとタイプのリストが下記の通りです：

```python
[root@CMDBServerDev01 ~]# mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
......
/dev/sdb on /mnt/dbdisk type ext3 (rw,relatime,data=ordered)
```

# 3(2). Postgresqlのデータフォルダを新しい場所へ移動する

- 現在のPostgresSQLデータフォルダを確認する

```python
[root@CMDBServerDev01 ~]# sudo -u postgres psql
postgres=# SHOW data_directory;
       data_directory
----------------------------
 /var/lib/pgsql/9.4/data    
(1 row)
postgres=# \q
```

- 実行されているのpostgresを停止する

```python
[root@CMDBServerDev01 ~]# systemctl stop postgresql-9.4
[root@CMDBServerDev01 ~]# systemctl status postgresql-9.4
```

- 関連のpostgresファイルを新しいフォルダへ同期する

```python
[root@CMDBServerDev01 ~]# sudo rsync -av /var/lib/pgsql  /mnt/dbdisk
```

- 同期が終わったら、元のデータファイルをバックアップする。

```python
[root@CMDBServerDev01 ~]# sudo mv /var/lib/pgsql/9.4/data    /var/lib/pgsql/9.4/data.bak
```

- 上記の準備作業が終わったら、関連の設定ファイルを修正する。

```python
[root@CMDBServerDev01 ~]# vi /var/lib/pgsql/.bash_profile
    修改为: PGDATA=/mnt/dbdisk/pgsql/9.4/data
```

```python
[root@CMDBServerDev01 ~]# vi /usr/lib/systemd/system/postgresql-9.4.service
修改为:
# Location of database directory
Environment=PGDATA=/mnt/dbdisk/pgsql/9.4/data
```

- サービスを再起動

```python
[root@CMDBServerDev01 ~]# systemctl daemon-reload
[root@CMDBServerDev01 ~]# systemctl enable  postgresql-9.4.service
[root@CMDBServerDev01 ~]# systemctl start  postgresql-9.4.service
```

- 再度Postgresのデータフォルダ場所を確認する

```python
[root@CMDBServerDev01 ~]# sudo -u postgres psql
postgres=# SHOW data_directory;
        data_directory
----------------------------
/mnt/dbdisk/pgsql/9.4/data
(1 row)
```

# 9. 参照

1. http://www.sfentona.net/?p=2756
2. https://www.digitalocean.com/community/tutorials/how-to-move-a-postgresql-data-directory-to-a-new-location-on-ubuntu-16-04