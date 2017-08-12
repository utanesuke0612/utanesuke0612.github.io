---
layout: post
title:  markdown模版
date:   2016-08-27 01:08:00 +0800
categories: document
tag: 模板
---
* content
{:toc}

Markdown記法 サンプル集
# <i class="fa fa-file-text" style="font-size:1em;"></i> Markdown記法 サンプル集
# <i class="fa fa-cubes" style="font-size:1em;"></i> 見出し

1個から6個シャープで見出しを記述する。

### <i class="fa fa-cube" style="font-size:1em;"></i> 記述例
~~~markdown
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6
~~~

### 表示例
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6

# <i class="fa fa-cube" style="font-size:1em;"></i> 箇条書きリスト
ハイフン、プラス、アスタリスクのいずれかで箇条書きリストを記述可能。

### 記述例
~~~markdown
- リスト1
    - ネスト リスト1_1
        - ネスト リスト1_1_1
        - ネスト リスト1_1_2
    - ネスト リスト1_2
- リスト2
- リスト3
~~~

### 表示例
- リスト1
    - ネスト リスト1_1
        - ネスト リスト1_1_1
        - ネスト リスト1_1_2
    - ネスト リスト1_2
- リスト2
- リスト3

# <i class="fa fa-cube" style="font-size:1em;"></i> 番号付きリスト

### 記述例
~~~markdown
1. 番号付きリスト1
    1. 番号付きリスト1_1
    1. 番号付きリスト1_2
1. 番号付きリスト2
1. 番号付きリスト3
~~~

### 表示例
1. 番号付きリスト1
    1. 番号付きリスト1_1
    1. 番号付きリスト1_2
1. 番号付きリスト2
1. 番号付きリスト3

# <i class="fa fa-cube" style="font-size:1em;"></i> 引用

~~~markdown
> お世話になります。xxxです。
>
> ご連絡いただいた、バグの件ですが、仕様です。
~~~

### 表示例
> お世話になります。xxxです。
>
> ご連絡いただいた、バグの件ですが、仕様です。

## <i class="fa fa-cube" style="font-size:1em;"></i> 二重引用

### 記述例
~~~markdown
> お世話になります。xxxです。
>
> ご連絡いただいた、バグの件ですが、仕様です。
>> お世話になります。 yyyです。
>>
>> あの新機能バグってるっすね
~~~

### 表示例
> お世話になります。xxxです。
>
> ご連絡いただいた、バグの件ですが、仕様です。
>> お世話になります。 yyyです。
>>
>> あの新機能バグってるっすね

# <i class="fa fa-cube" style="font-size:1em;"></i> pre記法(スペース4 or タブ)

半角スペース4個もしくはタブで、コードブロックをpre表示できます

### 記述例
~~~markdown
	# Tab
	class Hoge
		def hoge
			print 'hoge'
		end
	end

---

    # Space
    class Hoge
      def hoge
        print 'hoge'
      end
    end
~~~

### 表示例
	class Hoge
		def hoge
			print 'hoge'
		end
	end

---

    class Hoge
      def hoge
        print 'hoge'
      end
    end

# <i class="fa fa-cube" style="font-size:1em;"></i> code記法
バッククォートで文字列を囲むことでコードの一部を表示可能です。

### 記述例
~~~markdown
インストールコマンドは `gem install hoge` です
~~~

### 表示例
インストールコマンドは `gem install hoge` です

# <i class="fa fa-cube" style="font-size:1em;"></i> 強調：&lt;em&gt;
アスタリスクもしくはアンダースコア1個で文字列を囲むことで強調します。
見た目は斜体になります。

### 記述例
~~~markdown
normal *italic* normal
normal _italic_ normal
~~~

### 表示例
normal *italic* normal
normal _italic_ normal

## <i class="fa fa-cube" style="font-size:1em;"></i> 強調：&lt;strong&gt;
アスタリスクもしくはアンダースコア2個で文字列を囲むことで強調にします。
見た目は太字になります。

### 記述例
~~~markdown
normal **bold** normal
normal __bold__ normal
~~~

### 表示例
normal **bold** normal
normal __bold__ normal

## <i class="fa fa-cube" style="font-size:1em;"></i> 強調：&lt;em&gt; + &lt;strong&gt;
アスタリスクもしくはアンダースコア3個で文字列を囲むことで &lt;em&gt; と &lt;strong&gt; による強調を両方適用します。
見た目は斜体かつ太字になります。

### 記述例
~~~markdown
normal ***bold*** normal
normal ___bold___ normal
~~~

### 表示例
normal ***bold*** normal
normal ___bold___ normal

# <i class="fa fa-cube" style="font-size:1em;"></i> 水平線
アンダースコア、アスタリスク、ハイフンなどを3つ以上連続して記述することで水平線を表示します。
※連続するハイフンなどの間にはスペースがあっても良い

### 記述例
~~~markdown

***

___

---

*    *    *

~~~

### 表示例

***

___

---

* * *

# <i class="fa fa-cube" style="font-size:1em;"></i> リンク
`[表示文字](リンクURL)`形式でリンクを記述できます

~~~markdown
[Google先生](https://www.google.co.jp/)
~~~

[Google先生](https://www.google.co.jp/)

## <i class="fa fa-cube" style="font-size:1em;"></i> 定義参照リンク
Markdownの文書の途中に長いリンクを記述したくない場合は、
同じリンクの参照を何度も利用する場合は、リンク先への参照を定義することができます。

~~~markdown
[こっちからgoogle][google]
その他の文章
[こっちからもgoogle][google]

[google]: https://www.google.co.jp/
~~~

[こっちからgoogle][google]
その他の文章
[こっちからもgoogle][google]

[google]: https://www.google.co.jp/

# <i class="fa fa-cube" style="font-size:1em;"></i> GitHub Flavored Markdown(GFM)
GitHub Flavored Markdown(GFM)はGitHubの独自仕様を加えたMarkdown記法。
以降、GFMと記載します。

## <i class="fa fa-cube" style="font-size:1em;"></i> GFM:リンクテキスト簡易記法
URLは記述するだけで自動的にリンクになります。

### 記述例
~~~markdown
https://www.google.co.jp/
~~~

### 表示例
https://www.google.co.jp/

## <i class="fa fa-cube" style="font-size:1em;"></i> GFM:取り消し線
チルダ2個で文字列を囲むことで取り消し線を利用できます。

### 記述例
~~~markdown
~~取り消し線~~
~~~

### 表示例
~~取り消し線~~

## <i class="fa fa-cube" style="font-size:1em;"></i> GFM:pre記法(チルダ×3)

### 記述例

```markdown
　~~~
　class Hoge
　  def hoge
　    print 'hoge'
　  end
　end
　~~~
```

### 表示例
~~~
class Hoge
  def hoge
    print 'hoge'
  end
end
~~~

## <i class="fa fa-cube" style="font-size:1em;"></i> GFM:pre記法(バッククォート×3)

### 記述例
~~~markdown
　```
　class Hoge
　  def hoge
　    print 'hoge'
　  end
　end
　```
~~~

### 表示例
```
class Hoge
  def hoge
    print 'hoge'
  end
end
```

## <i class="fa fa-cube" style="font-size:1em;"></i> GFM:pre記法(シンタックスハイライト)

チルダ、もしくはバッククォート3つの後ろに対象シンタックスの言語名を記述します。

### 記述例

```markdown
　~~~ruby
　class Hoge
　  def hoge
　    print 'hoge'
　  end
　end
　~~~
```

### 表示例

~~~ruby
class Hoge
  def hoge
    print 'hoge'
  end
end
~~~

## <i class="fa fa-cube" style="font-size:1em;"></i> GFM:表組み

### 記述例
~~~markdown
|header1|header2|header3|
|:--|--:|:--:|
|align left|align right|align center|
|a|b|c|
~~~
### 表示例
|header1|header2|header3|
|:--|--:|:--:|
|align left|align right|align center|
|a|b|c|

## GFM:ページ内リンク
GitHubのMarkdownを利用すると、見出し記法を利用した際に
アンカーが自動的に作成されます。
そのアンカーを利用したページ内リンクを簡単に作成できます。

~~~markdown
## <i class="fa fa-cube" style="font-size:1em;"></i> menu
* [to header1](#header1)
* [to header2](#header2)

<!-- some long code -->

[return to menu](#menu)
### header1
### header2
~~~

少し省略してますが、こんなかんじのHTMLになります。

~~~html
<h2><a name="user-content-menu" href="#menu">menu</a></h2>
<a href="#header1">to header1</a>
<a href="#header2">to header2</a>

<!-- some long code -->

<a href="#menu">to menu</a>
<h3><a name="user-content-header1" href="#header1">header1</a></h3>
<h3><a name="user-content-header2" href="#header2">header2</a></h3>
~~~

# <i class="fa fa-book" style="font-size:1em;"></i> 参照
## [1. check the icon](http://fontawesome.io/icons/)
<i class="fa fa-cube" style="font-size:1em;"></i>
<i class="fa fa-cubes" style="font-size:1em;"></i>
<i class="fa fa-book" style="font-size:1em;"></i>
<i class="fa fa-file-text" style="font-size:1em;"></i>

~~~
<i class="fa fa-cube" style="font-size:1em;"></i>
<i class="fa fa-cubes" style="font-size:1em;"></i>
<i class="fa fa-book" style="font-size:1em;"></i>
<i class="fa fa-file-text" style="font-size:1em;"></i>

~~~
