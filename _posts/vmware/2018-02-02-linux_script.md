---
layout: post
title: linux-script应用01(SSH远程连接与执行等)
date: 2018-01-15 00:00:09
categories: 虚拟化(网络/存储/Cloud)
tags: linux
---
* content
{:toc}


本次使用的script完成了如下的功能：
1. 从本地(centos)远程ssh连接host
2. 将本地的script文件复制到远程host
3. 执行远程host上的script，并将script生成log文件打包
4. 将远程host上的log文件复制到本地

包含如下的script文件：
- testhostlist： 配置文件，是远程host的IP列表
- prepare-script.sh： 准备工作，将本地的脚本(test.sh)复制到远程host
- execute-script.sh： 远程执行host上准备好的脚本(test.sh)
- test.sh： 远程host上待执行的脚本文件

- auto_scp.sh： 执行scp的文件发送与接收的脚本 
- auto_ssh_command.sh： 指示远程host执行script(test.sh)的脚本

# 1. `prepare-script.sh`解析：

```c
#!/bin/sh

HOSTLIST="testhostlist"

. auto_scp.sh
. auto_ssh_command.sh

# 循环读取hostlist中的IP地址
for nm in `cat $HOSTLIST`; do
  echo "------------------------------------------------------------------"
  # 首先进行SSH连接，再执行后面的命令，生成需要的目录
  auto_ssh_command $nm "username★" "password★" "cd /var/tmp;rm -f -r wl;mkdir wl"

  # 通过scp，将test.sh脚本文件传输到远程host的/var/tmp/wl目录上
  auto_scp_send $nm "username★" "password★" test.sh /var/tmp/wl
  echo "------------------------------------------------------------------"
done

echo ""

exit 0

```

# 2. `execute-script.sh`解析

```c
#!/bin/sh

HOSTLIST="testhostlist"

. auto_scp.sh
. auto_ssh_command.sh

for nm in `cat $HOSTLIST`; do
  echo "-------------------------------------------------------------"

  # 先ssh连接，在将命令传递给远程host，执行test.sh脚本
  auto_ssh_command $nm "username★" "password★" "cd /var/tmp/wl;./test.sh "

  # 新建以IP命名的文件夹
  mkdir -p output/$nm

  # 通过scp，将远程host上的文件复制到本地目录
  auto_scp_resv $nm "username★" "password★" "/var/tmp/wl/test.tar" output/$nm
  echo "--------------------------------------------------------------"
done

echo ""

exit 0

```

# 3. `test.sh`解析

```c
# 通过执行命令，将命令返回值传递给变量
DATE=`date +"%Y%m%d%H%M%S"`
filename=`hostname -s`_${DATE}.txt

# 执行命令，并将结果写入文件
date >> $filename
hostname >> $filename

# 将当前文件夹整体打包为test.tar文件
tar -zcvf ./test.tar ./

```

# 4. `auto_scp.sh`解析

```c
#!/bin/sh

# 通用函数：将本地文件传递给远程host 
auto_scp_send() {
host=$1
id=$2
pass=$3
file=$4
remotepath=$5
local PR='(#|\\$) $'

expect -c "
set timeout 30
# scp进行文件传输
spawn scp ${file} ${id}@${host}:${remotepath}
  # 这里根据系统的输出，给定特定的输入，比如rsa和dsa时直接enter，password的时候输入pass变量的值
  while (1) {
    expect timeout { break } \"rsa\" { send \"\r\" } \"dsa\" { send \"\r\" }  \"word: \" { send \"${pass}\r\" } -re \"$PR\" { send \"\r\";break }
  }
"
}

# 通用函数：将远程host上的log文件复制到本地
auto_scp_resv() {
host=$1
id=$2
pass=$3
remptefile=$4
localpath=$5
local PR='(#|\\$) $'

expect -c "
set timeout 10
# scp进行文件传输
spawn scp ${id}@${host}:${remptefile} ${localpath}
  while (1) {
    expect timeout { break } \"rsa\" { send \"\r\" } \"dsa\" { send \"\r\" }  \"word: \" { send \"${pass}\r\" } -re \"$PR\" { send \"\r\";break }
  }
"
}

```



# 5. `auto_ssh_command.sh`解析

```c
#!/ bin/sh

# 通用函数，ssh连接后，执行command
auto_ssh_command() {

host=$1
id=$2
pass=$3
local PR='(#|\\$) $'

expect -c "
    set timeout 3
    spawn ssh ${id}@${host}

    # 根据特定的输出，给定特定的输入，包括命令的执行
    while (1) {
     expect  \"Enter passphrase for key '/home/a61041150/.ssh/id_rsa':\"
     send \"\r\"

     expect  \"Enter passphrase for key '/home/a61041150/.ssh/id_dsa':\"
     send \"\r\"

     expect  \"word:\"
     send \"${pass}\r\"

     #接收用户输入
     expect -re \"$PR\"
     send \"${@:4:($#-2)}\n\"

     expect -re \"$PR\"
     send \"exit\n\"
 } "
}

```


虽然解析了上面的大部分处理过程，但是如`expect` `expect -re` `${@:4:($#-2)}` 等用法都没有完全理解。




