---
layout: post
title: linux-script应用02(空格处理以及循环)
date: 2018-01-16 00:00:09
categories: 虚拟化(网络/存储/vmware)
tags: linux
---
* content
{:toc}

今天在工作中碰到了两个问题：
1. 文本文件的一行中，有空格隔开的话，读取后空格前后会被作为两个元素。
2. 循环的处理(for 与 while)

# 1.  示例代码

```python
$ vi nospace.txt
$ vi space.txt
$ vi test.sh
$ chmod u+x test.sh
$ ls -l
合計 12
-rw-r--r-- 1 a61041150 step_users  29  2月  5 17:02 nospace.txt
-rw-r--r-- 1 a61041150 step_users  31  2月  5 17:03 space.txt
-rwxr--r-- 1 a61041150 step_users 219  2月  5 17:08 test.sh
```

- `nospace.txt`

```python
lijun
wangling
utane
utasuke
```

- `space.txt`

```python
li jun
wang ling
utane
utasuke
```

- `test.sh`

```python
NOSPACE="nospace.txt"
SPACE="space.txt"
OUTFILE="result.txt"

nospacelist=`cat $NOSPACE`
spacelist=`cat $SPACE`

echo "-------------------"
# 循环读取
for text in $nospacelist;do
 echo $text
done

echo "-------------------"
# 循环读取，空格也作为分隔符
for text in $spacelist;do
 echo $text
done


echo "-------------------"
# 以一行一行的方式读取文件
while IFS= read line
do
 echo $line
done < "$SPACE"

echo "------------------"

echo "write the test to file" >> $OUTFILE

# 最后将当前文件夹中所有txt文件打包到result.tar中
tar -zcvf ./result.tar ./*.txt
```

- 代码输出：

```python
-------------------
lijun
wangling
utane
utasuke
-------------------
li
jun
wang
ling
utane
utasuke
-------------------
li jun
wang ling
utane
utasuke
```
