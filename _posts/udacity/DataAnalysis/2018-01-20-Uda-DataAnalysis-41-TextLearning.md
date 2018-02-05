---
layout: post
title: Uda-DataAnalysis-41-机器学习-文本学习
date: 2018-01-16 11:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}

# 5. 词袋属性

![image](https://user-images.githubusercontent.com/18595935/35776020-eb31dd08-09d7-11e8-804a-6a2ea853e4c1.png)

![image](https://user-images.githubusercontent.com/18595935/35776024-0cb60db4-09d8-11e8-98d4-ef50c354c368.png)

# 8. 停止词

![image](https://user-images.githubusercontent.com/18595935/35776853-42fc18dc-09e7-11e8-8ac5-aaf0a128ecbb.png)

在文本处理之前，非常常见的一个操作就是去除停止词，这些都是底信息词汇。

# 9. 从 NLTK 中获取停止词

```python
>>> from nltk.corpus import stopwords
>>> import nltk
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> sw = stopwords.words("english")
>>> sw[0]
u'i'
>>> len(sw)
179
```

# 10. 词干化以合并词汇

有很多不同的单词有相同的意思，这时这些单词可以合并为一个词干，在NLTK库中有函数可供使用

![image](https://user-images.githubusercontent.com/18595935/35777009-cb4d187e-09e9-11e8-9237-9ada8650522e.png)

- 使用 NLTK 进行词干化

```python
>>> from nltk.stem.snowball import SnowballStemmer
>>> stemmer = SnowballStemmer("english")
>>> stemmer.stem("responsiveness")
u'respons'
>>> stemmer.stem("responsivity")
u'respons'
>>> stemmer.stem("unresponsive")
u'unrespons'
```

文本处理中的运算符顺序，先进行词干处理，再进行词袋处理。

# 16. 文本学习迷你项目 - 部署词干化


```python
#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        
        # 下面是追加的代码：
        from nltk.stem.snowball import SnowballStemmer
        stemmer = SnowballStemmer("english")

        text_word = text_string.split()

        for myword in text_word:
            words = words + stemmer.stem(myword) + " "

    return words

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text

if __name__ == '__main__':
    main()
```

最后运行结果为：`hi everyon if you can read this messag your proper use parseouttext pleas proceed to the next part of the project`。


# 19. 清除“签名文字”

```python
#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            # 如下是追加的代码，先使用parseOutText进行词干处理
            ### use parseOutText to extract the text from the opened email
            new_email = parseOutText(email)

            # 删除部分词
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            new_email = new_email.replace("sara","")
            new_email = new_email.replace("chris","")
            new_email = new_email.replace("germani","")

            ### append the text to word_data
            word_data.append(new_email)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
                from_data.append(0)
            else:
                from_data.append(1)

            email.close()

print "emails processed"
print "----152:",word_data[152]
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

### in Part 4, do TfIdf vectorization here
```

# 20. 进行 TfIdf

使用 sklearn TfIdf 转换将 word_data 转换为 tf-idf 矩阵。删除英文停止词。
使用 get_feature_names() 访问单词和特征数字之间的映射，该函数返回一个包含词汇表所有单词的列表。有多少不同的单词？


```python
### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")
word_data = vectorizer.fit_transform(word_data)
vec = vectorizer.get_feature_names()
print len(vec)
print vec[34597]
```

- 输出为：

```python
38768
stengel
```

但是与标准答案不同，原因未知！