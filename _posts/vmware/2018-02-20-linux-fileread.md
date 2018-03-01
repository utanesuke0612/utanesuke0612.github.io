---
layout: post
title: linux中逐行文件读取以及外部函数调用
date: 2018-02-19 00:00:01
categories: 虚拟化(网络/存储/vmware)
tags: vmware linux
---
* content
{:toc}

# 0. 程序作用

- 将不同类型机器的用户名和密码存储在单独的文本文件，脚本进行读取
- 根据传入的机器类型，返回对应类型机器的用户名和密码

# 1. readhostbmc.sh

```
#!/bin/bash
filename=$1
bmctype=$2

userid=""
password=""

while read -r line
do
  OIFS=$IFS

  # IFS是分割符
  IFS=";"
  
  # 将每一行的内容，通过分隔符`;`分割后，存储到pass_string中
  pass_string=()
  counter=0
  for x in $line
  do
   pass_string[counter]=$x
   counter=$counter+1
  done

  # 将pass_string中的内容取出来，判断是否是bmctype(imm/ilo/ibmc)
  counter_y=0
  for y in "${pass_string[@]}"
  do
   if [ $y == $bmctype ];then
     echo "get"
     userid=${pass_string[${counter_y}-2]}
     password=${pass_string[${counter_y}-1]}
   fi
   counter_y=$counter_y+1
  done

  # 还原为默认的分割符
  IFS=$OIFS

done < "$filename"

echo $userid
echo $password
```

# 2. hostpass-bmc.txt

```
USERID;PASSW0RD;#imm
USERID2;PASSW0RD2;#imm2
USERID3;PASSW0RD3;#imm3
```

# 3. 运行结果：

```
[root@mypc readline]$ ./readhostbmc.sh "hostpass-bmc.txt" "#imm"
get
USERID
PASSW0RD

[root@mypc readline]$ ./readhostbmc.sh "hostpass-bmc.txt" "#imm2"
get
USERID2
PASSW0RD2

[root@mypc readline]$ ./readhostbmc.sh "hostpass-bmc.txt" "#imm3"
get
USERID3
PASSW0RD3
```

# 4. 外部函数调用

将上面读取密码的script作成一个函数，使得其他的script可以调用它，改造后如下：

- `password.txt`：存储的密码文件
- `getpassword.sh`：读取密码文件
- `mainex.sh`：调用上面的读取密码文件函数

## 4.1 `password.txt`

```
USERID1;PASSW0RD1;#pass1
USERID2;PASSW0RD2;#pass2
USERID3;PASSW0RD3;#pass3
```

## 4.2 `getpassword.sh`

```
#!/bin/bash

getpassword(){

filename=$1
bmctype=$2

userid=""
password=""

while read -r line
do
  OIFS=$IFS

  IFS=";"

  pass_string=()
  counter=0
  for x in $line
  do
   pass_string[counter]=$x
   counter=$counter+1
  done

  counter_y=0
  for y in "${pass_string[@]}"
  do
   if [ $y == $bmctype ];then
     userid=${pass_string[${counter_y}-2]}
     password=${pass_string[${counter_y}-1]}
   fi
   counter_y=$counter_y+1
  done

  IFS=$OIFS

done < "$filename"
}
```


## 4.3 `mainex.sh`

```
#!/bin/sh

source ./getpassword.sh

getpassword "password.txt" "#pass1"

echo "pass1 ${userid}"
echo "pass1 ${password}"


getpassword "password.txt" "#pass2"

echo "pass2 ${userid}"
echo "pass2 ${password}"
```

## 4.4 执行

```
[root@CMDBServerDev01 studylinux]# ./mainex.sh
pass1 USERID1
pass1 PASSW0RD1
pass2 USERID2
pass2 PASSW0RD2
```

通过上面的例子说明，通过引用一个script文件，调用它的函数后，能将该script中的变量也直接拿过来用。