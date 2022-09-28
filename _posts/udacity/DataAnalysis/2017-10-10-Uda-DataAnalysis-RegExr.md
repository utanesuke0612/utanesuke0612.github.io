---
layout: post
title: Uda-DataAnalysis-PJ01-[扩展]-正则表达式
date: 2017-10-8 19:00:00
categories: 数据分析
tags: DataAnalysis 其他
---
* content
{:toc}


> 第一部分的课程主要集中在数据清理，清理的过程中遇到字符串的话，不可避免的要用到正则表达式。掌握好正则表达式是数据处理大有裨益，可以说是必不可少。
> 这是一个在线测试网站： [https://regexr.com/](https://regexr.com/)

参考用cheatsheet [regular exp](https://autodrivegroup.slack.com/files/U76LP2KL3/F7JG9QHL2/davechild_regular-expressions.pdf)

# 1. 匹配单个字符

1. `.`表示任意字符。
2. `\.` 斜杠是转义字符，这里表示就是要匹配`.`符号。
3. 如果需要搜索 `\`，则用`\\`，前者用来转义，后者用来表示要搜索的字符。
4. 下面是一组示例：

![image](https://user-images.githubusercontent.com/18595935/31585125-148c47f8-b1f7-11e7-94f2-e711c0b88344.png)

# 2. 匹配一组字符
1. `[A-Za-z0-9]`的字符集合，A到Z的所有字母，a到z的所有字母，0-9 的所有数字。
2. 如下的①②③，分别表示字符集合/数字集合/数字集合的取反。

![image](https://user-images.githubusercontent.com/18595935/31585148-c541b3b2-b1f7-11e7-8070-e62fe3840e26.png)

- ①:字母是n或s、紧接着a、后面是任意字母、然后是实际的.点号、最后xls
- ②:a的后面是1-9之间的数字，也可以写成[123456789]
- ③:^取反，除了1-9以外都OK

# 3. 使用元字符
- 元字符，是正则表达式中有特殊含义的字符，例如前面的`.`表示一个任意字符，`[ ]`也是元字符，用来表示字符集合。
- 上面的例子: Pattern：`\[[0-9]\]`  前后两个`[`和`]` 分别被转义，用来表示这两个字符，可以匹配出`if (myArray[0] == 0){` 中的`[0]`.
- `\` 本身也是元字符，所以在实际匹配 `\` 的时候，要转义 `\\` ，例如用 `\\`  匹配得到  `\home\ben\sales\`。
- 元字符大概分为两种，1种是用来匹配文本的，如`.` 点号；另1种是正则表达式语法要求的，比如`[` 和`]`，还有一种用来匹配空白字符的元字符。

![image](https://user-images.githubusercontent.com/18595935/31585203-0d3959c6-b1f9-11e7-9231-9e34307deeea.png)

- 匹配特定的字符类别 比如 [ns]a\d匹配了 na1 ，na2，sa1等。

![image](https://user-images.githubusercontent.com/18595935/31585231-80cbfd80-b1f9-11e7-9890-a7e93df3e7ae.png)


# 4. 重复匹配

## 4.1 `+`1个以上字符,`*`0个或多个字符，`?`0个或1个字符

- 通过`\w+@\w+\.\w+`，可以匹配出下面的三个邮件地址。

```python
Send personal email to ben@forta.com. For questions about a book use 
support@forta.com	email to spam@forta.com 
```

- 但如果添加一个邮件地址`abc.ben@forta.com`，就无法匹配了，因为`\w`无法匹配 dot`.`点号，需要修改为`[\w.]+@\w+\.\w+`,将`.`加入 `[ ]` 集合中。

- 上面的 `.`在 `[]` 中不需要转义，转义也OK，与 `[\w\.]`效果相同。

- `Hello .ben@forta.com is my email address. `， 在ben的前面有个笔误 `.` 号。通过`[\w.]+@[\w.]+\.\w+`的话，就会将前面的dot 也匹配进来，email地址第一个字符不能为 `.`号，要修改为 `\w+[\w.]*@[\w.]+\.\w+` ，限定第一个字符只能为 字母数字下划线。

- `https?:\/\/[\w./]+`，通过`?` 表示 s 可能有1个也可能没有，为了清晰表示，可以`[s]?`

```python
The URL is http://www.forta.com,to connect ，securely use https://www.forta.com/ instead.
```


## 4.2 重复次数
上面的元字符，都没有字数限制，设定重复次数，用 `{ }` 完成。

通过`#[0-9A-F]{6}`可以匹配出颜色值`#336633`和`#FFFFFF`。

```python
<BODY BGCOLOR="#336633" TEXT="#FFFFFF"
MARGINWINDTH="0" MARGINHEIGHT="0">

```

1. `{2,4}` 指2次到4次，如 `\d{2,4}`  
2. 重复的次数可以为0，`{0,1}` 与 ? 等价，都是0或1次
3. `{3,}` 指重复3次以及以上，例如，多于100美元的被过滤出来了 ，`\d+:\$\d{3,}\.\d{2}`

![image](https://user-images.githubusercontent.com/18595935/31585545-8b476d30-b1fe-11e7-87f7-bf6db060e879.png)


## 4.3 防止过度匹配

![image](https://user-images.githubusercontent.com/18595935/31585558-d2f79948-b1fe-11e7-98f5-35b92862a351.png)




# 5. 位置匹配

## 5.1 边界

```python
The cat scattered his food all over the room 
```

1. `cat` 匹配的话，会匹配出`cat`和`scattered`两个。
2. `\bcat`的话，只会匹配出`cat`，`\b` 匹配出来的是一个位置，这个位置位于 构成单词的字符 和 不能构成单词的字符之间。显然`scattered`不符合要求。
3. `\b`只匹配一个位置，不匹配任何字符。
4. 如果想不匹配单词边界，用`\B`, 如果Pattern为`\Bcat`的话，匹配出来的是`scattered` 中的`cat`。

## 5.2 字符串边界

```python
This is to bad
<?xml version="1.0" encoding="UTF-8" ?>
…
xmlns:apachesoap="http://xml.apache.org/xml-soap"
```
1. 上面不是正确的xml文件，因为第一行 是不是xml格式。如果用 `<\?xml.*\?>`去判断该文件是否xml的话，会得到匹配结果，显然是不正确的
2. 需要限定能匹配这个pattern的只能是第一行用 `^\s*<\?xml.*\?>` 匹配的话，就能正确判断该文件不符合xml格式。
3. `^\s*` ，`^`限定了第一行， `\s*` 排除了空白行。
4. `$` 用来表示末尾，用法完全一样，比如判断html文件的结尾是不是</html> ， `<\/[Hh][Tt][Mm][Ll]>\s*$`， \用来转义，\s* 用来排除空白字符，$表示字符串末尾

```python
<html>
    <body>
    </body>
</html>
```

# 6. 字表达式

![image](https://user-images.githubusercontent.com/18595935/31585641-5a594ed0-b200-11e7-8301-be3b4c39666b.png)


# 7. 回溯引用 ：前后一致匹配

![image](https://user-images.githubusercontent.com/18595935/31585698-3298f674-b201-11e7-9888-3c3ea0aa6696.png)


# 8. 前后查找

![image](https://user-images.githubusercontent.com/18595935/31585711-6673242e-b201-11e7-89e0-90fc4cbf528d.png)