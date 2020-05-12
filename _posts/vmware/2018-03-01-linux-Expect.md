---
layout: post
title: linux中使用Expect Command 自动化运行脚本
date: 2018-02-20 00:00:06
categories: 虚拟化(网络/存储/Cloud)
tags: linux
---
* content
{:toc}

在工作中需要实现脚本的自动化运行，包括自动填写用户名，自动输入密码，以及自动输入各种命令，并将命令结果返回，这时需要用到expect相关命令。
本文参考[Expect Command And How To Automate Shell Scripts Like Magic](https://likegeeks.com/expect-command/)翻译而成。

expect不是linux中的标准安装，需要另外安装，比如在centos中使用`yum install expect`。


# 1. 关于 Expect Command

如下四个关键字的意义如下：

- `spawn`：开始一个新的脚本或程序，新起一个进程，比如 FTP, Telnet, SSH, SCP等
- `expect`：等待程序的输出
- `send`：发送一个输入给程序
- `interact`：允许与程序交互

## 1.1 `questions`示例

```
#!/bin/bash
 
echo "Hello, who are you?"
 
read $REPLY
 
echo "Can I ask you some questions?"
 
read $REPLY
 
echo "What is your favorite topic?"
 
read $REPLY

```

## 1.2 `answerbot`示例

```
#!/usr/bin/expect -f
 
set timeout -1
 
spawn ./questions
 
expect "Hello, who are you?\r"
 
send -- "Im Adam\r"
 
expect "Can I ask you some questions?\r"
 
send -- "Sure\r"
 
expect "What is your favorite topic?\r"
 
send -- "Technology\r"
 
expect eof
```

## 1.3 执行程序

- 赋予程序执行权限 `chmod +x ./answerbot`


运行结果如下：

```
[root@mypc linuxstudy]$ ./answerbot
spawn ./question
Hello, who are you?
Im lijun
Can I ask you some questions?
Sure
What is your favorite topic?
Sports
```




# 2. Using autoexpect

`autoexpect`与expect类似，能用来自动构建脚本，比如用 autoexpect命令运行question脚本：

```
[root@mypc linuxstudy]$ autoexpect ./question
autoexpect started, file is script.exp
Hello, who are you?
lijun
Can I ask you some questions?
ok
What is your favorite topic?
run
autoexpect done, file is script.exp
[root@mypc linuxstudy]$ ls
question  script.exp  answerbot
[root@mypc linuxstudy]$ vi script.exp
```



生成如下的文件`script.exp`:

```
set force_conservative 0  ;# set to 1 to force conservative mode even if
                          ;# script wasn't run conservatively originally
if {$force_conservative} {
        set send_slow {1 .1}
        proc send {ignore arg} {
                sleep .1
                exp_send -s -- $arg
        }
}

set timeout -1
spawn ./question
match_max 100000
expect -exact "Hello, who are you?\r
"
send -- "lijun\r"
expect -exact "lijun\r
Can I ask you some questions?\r
"
send -- "ok\r"
expect -exact "ok\r
What is your favorite topic?\r
"
send -- "run\r"
expect eof
~
```




# 3. Working with Variables

通过如下的方式能给变量赋值：

```
set MYVAR 5
set MYVAR [lindex $argv 0]
```


也可以如下的赋值方式 

```
host=$1
id=$2
```



- 实例程序 - `answerbot`：


```
#!/usr/bin/expect -f
 
set my_name [lindex $argv 0]
 
set my_favorite [lindex $argv 1]
 
set timeout -1
 
spawn ./questions
 
expect "Hello, who are you?\r"
 
send -- "Im $my_name\r"
 
expect "Can I ask you some questions?\r"
 
send -- "Sure\r"
 
expect "What is your favorite topic?\r"
 
send -- "$my_favorite\r"
 
expect eof
```



- 运行程序，并同时传递参数

```
[root@mypc linuxstudy]$ ./test.sh  lijun run
spawn ./questions.sh
Hello, who are you?
Im lijun
Can I ask you some questions?
Sure
What is your favorite topic?
run
[root@mypc linuxstudy]$
```


# 4. Conditional Tests

可以使用条件判断的方式：

```
expect {
 
    "something" { send -- "send this\r" }
 
    "*another" { send -- "send another\r" }
 
}
```


- `question`

```
#!/bin/bash

let number=$RANDOM
echo $number

if [ $number -gt 25000 ]

then

echo "What is your favorite topic?"

else

echo "What is your favorite movie?"

fi

read $REPLY
```


- `answerbot`

```
#!/usr/bin/expect -f

set timeout -1

spawn ./questions

expect {
     "*topic?" {send -- "Programming\r"}
     "*movie?" {send -- "Star wars\r"}
}

expect eof
```

- 运行脚本

```
[root@mypc linuxstudy]$ ./answerbot
spawn ./questions
7575
What is your favorite movie?
Star wars

[root@mypc linuxstudy]$ ./answerbot
spawn ./questions
25806
What is your favorite topic?
Programming
```








# 5. If else Conditions

- `answerbot`

```
#!/usr/bin/expect -f

set NUM 1

if { $NUM < 5 } {

puts "\Smaller than 5\n"

} elseif { $NUM > 5 } {

puts "\Bigger than 5\n"

} else {

puts "\Equals 5\n"

}
~
```

- 运行

```
[root@mypc linuxstudy]$ ./answerbot
Smaller than 5
```


# 6. While Loops

- `answerbot`

```
#!/usr/bin/expect -f
 
set NUM 0
 
while { $NUM <= 5 } {
 
puts "\nNumber is $NUM"
 
set NUM [ expr $NUM + 1 ]
 
}
 
puts ""

```


- 运行程序

```
[root@mypc linuxstudy]$ ./answerbot

Number is 0

Number is 1

Number is 2

Number is 3

Number is 4

Number is 5
```





# 7. For Loops

- `answerbot`

```
#!/usr/bin/expect -f
 
for {set NUM 0} {$NUM <= 5} {incr NUM} {
 
puts "\nNUM = $NUM"
 
}
 
puts ""

```


- 运行程序

```
[root@mypc linuxstudy]$ ./answerbot

NUM = 0

NUM = 1

NUM = 2

NUM = 3

NUM = 4

NUM = 5

```


# 8. User-defined Functions



- `answerbot`

```
#!/usr/bin/expect -f

# 定义函数
proc myfunc { TOTAL } {
 
set TOTAL [expr $TOTAL + 1]
 
return "$TOTAL"
 
}
 
set NUM 0
 
while {$NUM <= 5} {
 
puts "\nNumber $NUM"

# 使用函数
set NUM [myfunc $NUM]
 
}
 
puts ""


```


- 运行程序

```
[root@mypc linuxstudy]$ ./answerbot

NUM = 0

NUM = 1

NUM = 2

NUM = 3

NUM = 4

NUM = 5
```




# 9. Interact Command


- `question`

```
#!/bin/bash

echo "Hello,Who are you?"

read $REPLY

echo "What is your password?"

read $REPLY

echo "What is your favorite topic?"

read $REPLY

```

- `answerbot`

```
#!/usr/bin/expect -f

set timeout -1

spawn ./question

expect "Hello,Who are you?\r"

send -- "Hi Im Adam\r"

expect "*password?\r"

interact ++ return

send "\r"

expect "*topic?\r"

send -- "Technology\r"

expect eof
```


- 运行程序


```
[root@mypc linuxstudy]$ ./answerbot
spawn ./question
Hello,Who are you?
Hi Im Adam
What is your password?
123
What is your favorite topic?
run
send: spawn id exp6 not open
    while executing
"send "\r""
    (file "./answerbot" line 15)
[root@mypc linuxstudy]$

```