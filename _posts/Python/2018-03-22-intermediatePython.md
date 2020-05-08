---
layout: post
title: Python中级进阶(intermediatePython)
date: 2020-05-02 07:01:00
categories: Python
tags: Python
---
* content
{:toc}

> [interpy-zh-v1.3.pdf](https://github.com/eastlakeside/interpy-zh/releases)

# 02. *args 和 **kwargs

一个函数定义，如果并不知道函数使用者会传递多少个参数，这种场景下使用``和``两个关键字

- `*argv`:用来发送一个非键值对的可变数量参数列表


```python
def test_ver_args(f_arg,*argv):
    print("first normal arg:",f_arg)
    for arg in argv:
        print("through *argv:",arg)

test_ver_args("yahoo","google","amazon","apple")
```

输出如下:

```
first normal arg: yahoo
through *argv: google
through *argv: amazon
through *argv: apple
```

- `**argv`:允许将不定长度的键值对，作为参数传递给一个函数

```python
def test_ver_2args(**argv):
    for key,value in argv.items():
        print("{0}={1}".format(key,value))

test_ver_2args(name="lijun",age=9,gender="male")
```

输出如下:

```
name=lijun
age=9
gender=male
```


## 02.1 使用 *args 和 **kwargs 来调用函数 

- args和kwargs参数的个数，必须与函数中接受参数个数一致，否则会有编译错误

```python
def test_args_kwargs(arg1,arg2,arg3):
    print("arg1",arg1)
    print("arg2",arg2)
    print("arg3",arg3)

args = ("two",3,True)
test_args_kwargs(*args)

print("----------------------------")

kwargs = {"arg3":3,"arg2":2,"arg1":"One"}
test_args_kwargs(**kwargs)

```


```python
arg1 two
arg2 3
arg3 True
----------------------------
arg1 One
arg2 2
arg3 3
```

那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的： some_func(fargs, *args, **kwargs) 
详细参考[16.5 参数组合](http://road2ai.info/2017/09/11/Python3-Liao_02/#165-%E5%8F%82%E6%95%B0%E7%BB%84%E5%90%88)

## 02.2 什么场景下使用

> **下面的内容没有完全理解!**

什么时候使用它们？ 这还真的要看你的需求而定。 最常见的用例是在写函数装饰器的时候（会在另一章里讨论）。 

此外它也可以用来做猴子补丁(monkey patching)。猴子补丁的意思是在程序运行时 (runtime)修改某些代码。 
打个比方，你有一个类，里面有个叫get_info的函数会调用一 个API并返回相应的数据。如果我们想测试它，可以把API调用替换成一些测试数据。例 如： 

```python
import someclass 

def get_info(self, *args):
	return "Test data" 

someclass.get_info = get_info 

```

**参考:**
- [16. 【重要！】函数的参数](http://road2ai.info/2017/09/11/Python3-Liao_02/#16-%E9%87%8D%E8%A6%81%E5%87%BD%E6%95%B0%E7%9A%84%E5%8F%82%E6%95%B0)

- [*argv和**argv](http://road2ai.info/2017/09/11/Python3-Liao_03/#31-%E8%A3%85%E9%A5%B0%E5%99%A8)


# 03. 调试

- 从命令行运行

添加`-m pdb`在py文件前面，直接在第一行就进行调试模式

```
C:\Users\61041150\Desktop\20180203\shell\pyData>python -m pdb pylearn.py
> c:\users\61041150\desktop\20180203\shell\pydata\pylearn.py(1)<module>()
-> def test_ver_args(f_arg,*argv):
(Pdb)
```

- 从脚本内部运行

```python
import pdb 

def make_bread(m):
    i = m
    x = m +1
    pdb.set_trace()
    return "I don't have time" 

print(make_bread(3)) 
```

运行后效果如下，可以打印内存中参数的值，另外还能执行计算:

```
> c:\users\61041150\desktop\20180203\shell\pydata\pylearn.py(40)make_bread()
-> return "I don't have time"
(Pdb) i
3
(Pdb) m
3
(Pdb) x
4
(Pdb) i = m + 2
(Pdb) i
5

```
- 在pdb模式中，输入如下command：

`c`: 继续执行 
`w`: 显示当前正在执行的代码行的上下文信息 
`a`: 打印当前函数的参数列表 
`s`: 执行当前代码行，并停在第一个能停的地方（相当于单步进入） 
`n`: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）

单步跳过（next）和单步进入（step）的区别在于， 单步进入会进入当前行调用的函数内 部并停在里面， 而单步跳过会（几乎）全速执行完当前行调用的函数，并停在当前函数的 下一行。 

# 04. 生成器

关于迭代，生成器等，可以参考[20. 迭代](http://road2ai.info/2017/09/11/Python3-Liao_02/#20-%E8%BF%AD%E4%BB%A3)

## 04.1 可迭代对象(Iterable) 

Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了 可以支持下标索引的__getitem__方法(这些双下划线方法会在其他章节中全面解释)， 那么它就是一个可迭代对象。
简单说，可迭代对象就是能提供迭代器的任意对象。那迭代 器又是什么呢？

## 04.2 迭代器(Iterator) 

任意对象，只要定义了next(Python2) 或者__next__方法，它就是一个迭代器。就这么 简单。现在我们来理解迭代(iteration)  

## 04.3 迭代(Iteration)
用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一 个循环来遍历某个东西时，这个过程本身就叫迭代。现在既然我们有了这些术语的基本理 解，那我们开始理解生成器吧。 

## 04.4 生成器(Generators) 

生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在 内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它 们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而， 它们并不返回一个值，而是yield(暂且译作“生出”)一个值。这里有个生成器函数的简单 例子：

```python
def generator_function(m):
    for i in range(m):
        print("yield0:{}".format(i))
        yield i

for i in generator_function(4):
    print("print:{}".format(i))
```

- 输出结果如下:

```
yield0:0
print:0
yield0:1
print:1
yield0:2
print:2
yield0:3
print:3
```

上面的例子可以看出，生成器也是一种迭代器，可以用于for循环，每一次迭代，生成器被调用一次，即print一次yield0，再yield一个值供外面print，下一次迭代再重复上述过程。
所以生成的值并不是存储在内存中，而是需要的时候直接计算。

```python
def generator_function():
    for i in range(4):
        print("yield0:{}".format(i))
        yield i

g = generator_function()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
```python

输出如下:

```python
yield0:0
0
yield0:1
1
yield0:2
2
yield0:3
3
```

【未完】


# 05. Map，Filter 和 Reduce

## 05.1 Map

Map会将一个函数映射到一个输入列表的所有元素上。

规范为 `map(function_to_apply, list_of_inputs)`,大多数时候使用匿名函数lambda替代函数。

> 参考[map/filter/reduce](http://road2ai.info/2017/09/11/Python3-Liao_03/#26-mapreduce)

```python
items = [1,2,3,4,5]
squared = []

for i in items:
    squared.append(i*i)

print(squared)
 
squared1 = [i*i for i in items]
squared2 = list(map(lambda x: x**2, items)) 

print(squared1)
print(squared2)

print("--------------------------")

def multi(x):
    return x*x

def add(x):
    return x+x

funcs = [multi,add]

for i in items:
    value = map(lambda x: x(i), funcs)
    print(list(value))
```


输出如下:

```
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]
--------------------------
[1, 2]
[4, 4]
[9, 6]
[16, 8]
[25, 10]
```

上面 value = map(lambda x: x(i), funcs) ，将函数名存储到一个list funcs中，将函数名作为参数传递给匿名函数，示例如下：

```python
def multi(x):
    return x*x

def add(x):
    return x+x

funcs = [multi,add]

value = map(lambda x: x(10), funcs)
print(list(value))
```
输出:`[100, 20]`

下面是使用函数的形式，后面迭代器的元素，依次作为参数提供给前面的f函数

```python
def f(x):
    return x**3
    
lista = [1,2,3,4,5,6]
r = map(f,lista)
print(list(r))
```

输出如下:

```
[1, 8, 27, 64, 125, 216]
```


## 05.2 filter

顾名思义，filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列 表，符合要求即函数映射到该元素时返回值为True. 

```python
number_list = range(-5,5)
above_than_zero = filter(lambda x:x>0,number_list)
print(list(above_than_zero))
```

输出如下:

```
[1, 2, 3, 4]
```

与上面一样，除了匿名函数，还可以接受函数，如下判断偶数的函数，另外，filter()与map()一样，返回的都是迭代器，分别为filter对象和map对象，需要用list取出其中的元素。

```python
def check_even(x):
    if x%2 == 0:
        return True
    else:
        return False
even_number_list = filter(check_even,number_list)
print(list(even_number_list))
print((even_number_list))
```

输出如下:

```python
[-4, -2, 0, 2, 4]
<filter object at 0x0150F230>
```

## 05.3 Reduce

当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数。

举个例 子，当你需要计算一个整数列表的乘积时。 通常在 python 中你可能会使用基本的 for 循环来完成这个任务。 

现在我们来试试 reduce：

```python
from functools import reduce

product = reduce(lambda x,y:x*y,[1,2,3,4])
print(product)

print("---------------")

def testfunc(x,y):
    print("x:{0},y:{1}".format(x,y))
    return x*y

product1 = reduce(testfunc,[1,2,3,4])
print(product1)
```


输出为

```python
24
---------------
x:1,y:2
x:2,y:3
x:6,y:4
24
```

可以看到testfunc每次接受两个参数，第一次是前两个，第二次前一次的结果和第三个，第三次也是前一次的结果和第四个reduce中的函数需要接受两个参数。


# 06. set 数据结构

set集合不能包含重复的元素，没有顺序。

```python
some_list = ["A","B","C","A","B"]

duplicates = []

for i in some_list:
    if i not in duplicates:
        duplicates.append(i)

print("original:{}".format(some_list))

print("-------------")

print("method0:{}".format(duplicates))

print("-------------")

duplicates1 = set([x for x in some_list])
print("method1:{}".format(duplicates1))

print("-------------")

duplicates2 = set([x for x in some_list if some_list.count(x) > 1])
print("count>1:{}".format(duplicates2))

```

- 输出如下，另外，注意`some_list.count(x) > 1`的用法，能计算list中的元素个数：

```
original:['A', 'B', 'C', 'A', 'B']
-------------
method0:['A', 'B', 'C']
-------------
method1:{'A', 'C', 'B'}
-------------
count>1:{'A', 'B'}
```


- set集合的交集与并集，`{}`可以用于定义集合

```python
setA = set(["A","B","C","D"])

setB = {"A","B","E","F"}

print("intersection:{}".format(setA.intersection(setB)))
print("difference(A-B):{}".format(setA.difference(setB)))
print("difference(B-A):{}".format(setB.difference(setA)))
```
输出如下:

```
intersection:{'B', 'A'}
difference(A-B):{'C', 'D'}
difference(B-A):{'E', 'F'}
```

# 07. 三元运算符

三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(not)的条件判 断，在Python 2.4以上才有了三元操作。 

它允许用简单的一行快速判断，而不是使用复杂的多行if语句。 这在大多数时候非常有 用，而且可以使代码简单可维护。 

```python
is_fat = True
state = "fat" if is_fat else "not fat"

print(state)
```

上述输出`fat`

# 08. 装饰器

# 09. Global和Return

- global是全局变量

global变量意味着我们可以在函数以外的区域都能访问这个 变量。比较下面两个程序:

```python
def add1(x,y):
    return x+y

print(add1(3,5))

print("-----------")

def add2(x,y):
    global result
    result = x + y

add2(3,5)
print(result)

```

- 输出如下:

```
8
-----------
8
```

不过，在实际的编程时，你应该试着避开global关键字，它只会让生活变得艰难，因为它引入了多余的变量到全局作用域了。 

- 多个return值 

如果我们要返回多个值，有如下多种方式，尽量避免使用第一种global变量的方式，第三种方式最smart

```python
def profile1():
    global name
    global age
    name = "lj-1"
    age = "18-1"

def profile2():
    name = "lj-2"
    age = "18-2"
    return (name,age)

def profile3():
    name = "lj-3"
    age = "18-3"
    return name,age

profile1()
print("{0}:{1}".format(name,age))

name2 = profile2()[0]
age2 = profile2()[1]
print("{0}:{1}".format(name2,age2))

name3,age3 = profile3()
print("{0}:{1}".format(name3,age3))
```

输出如下:

```
lj-1:18-1
lj-2:18-2
lj-3:18-3
```


# 10. 对象变动 Mutation

参考 [16.2 默认参数](http://road2ai.info/2017/09/11/Python3-Liao_02/#162-%E9%BB%98%E8%AE%A4%E5%8F%82%E6%95%B0)中，默认参数必须指向不变的对象的例子。

在Python中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。你应该永远不要定义可变类型的 默认参数。

```python


foo = ["hi"]
print(foo)

bar = foo
bar += [",bye"]
print(foo)

print("--------------------")

def add_to(num,target=[]):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))

print("--------------------")

def add_to2(element,target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to2(1))
print(add_to2(2))
print(add_to2(3))
```

输出为

```
['hi']
['hi', ',bye']
--------------------
[1]
[1, 2]
[1, 2, 3]
--------------------
[1]
[2]
[3]
```

# 11. __slots__魔法 

> 参考: [42. 面向对象高级编程-使用__slots__](http://road2ai.info/2017/12/12/Python3-Liao_05/)

> [Saving 9 GB of RAM with Python’s __slots__](http://tech.oyster.com/save-ram-with-python-slots/)

在进入正文前，先看看python的动态属性和动态方法绑定，即一个对象在创建完毕后，还能给它追加属性和方法。
实例代码:

```python
class Student(object):
    def __init__(self,name):
        self.name = name

#
bob = Student("bob")
bob.age = 24

print("{0}:{1}".format(bob.name,bob.age))

# 
def showname(name):
    print("my name is:{}".format(name))

bob.showname = showname
bob.showname(bob.name)

```

运行后结果:

```
bob:24
my name is:bob
```

默认情况下Python用一个字典来保存一个对象的实例 属性。这非常有用，因为它允许我们在运行时去设置任意的新属性。然而，对于有着已知属性的小类来说，它可能是个瓶颈。这个字典浪费了很多内存。 Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。因此如果你创建 许多对象（我指的是成千上万个），它会消耗掉很多内存。 

- 使用__slots__来告诉Python不要使 用字典，而且只给一个固定集合的属性分配空间。 

```python
class Student2(object):
    __slot__ = ["name"]
    def __init__(self,name):
        self.name = name

wangling = Student2("wangling")

wangling.age = 24

print("{0}:{1}".format(wangling.name,wangling.age))

```

输出结果为: `wangling:24`

Python在构建类的时候，会检查__slots__变量是否存在，如果存在，为slots变量建立member_descriptor，并放入tp_dict里面，并且这个类的tp_dictoffset为0，它的实例将不会有自己的__dict__。


虽然上面的实例中也有动态的属性追加，但是估计是加到`member_descriptor`中，而不是每个实例中。

既然使用`__slots__`既能减少内存使用，也能实现动态属性追加，那是不是什么情况都需要使用呢？不是!只有在实例非常多的情况下，使用它才最有优势。

**Warning**: Don’t prematurely optimize and use this everywhere! It’s not great for code maintenance, and it really only saves you when you have thousands of instances.

# 12. 虚拟环境

# 13. 容器

python附带一个模块，包含了很多数据类型，名字叫做collections，这里讨论:
- defaultdict
- counter
- deque
- namedtuple
- enum.Enum

## defaultdict

我个人使用defaultdict较多，与dict类型不同，你不需要检查key是否存在，所以我 们能这样做： 

```python
from collections import defaultdict

colors = (
        ("1","red"),
        ("2","blue"),
        ("2","dark blue"),
        ("3","yellow"),
        ("3","pink"),
        )

favourite_colors = defaultdict(list)

for name,color in colors:
    favourite_colors[name].append(color)

print(favourite_colors)
```
输出为:

```
defaultdict(<class 'list'>, {'1': ['red'], '2': ['blue', 'dark blue'], '3': ['yellow', 'pink']})
```


- 在一个字典中对一个键进行嵌套赋值时，如果这个键不存 在，会触发keyError异常。 defaultdict允许我们用一个聪明的方式绕过这个问题。 

首先分享一个使用dict触发KeyError的例子

```python
some_dict = {}
some_dict["colors"]["favourite"] = "yellow"
```

错误如下:

```
Traceback (most recent call last):
  File "pylearn.py", line 3, in <module>
    some_dict["colors"]["favourite"] = "yellow"
KeyError: 'colors'
```

然后提供一个使用defaultdict的解决方案。 

```python
import collections 
tree = lambda:collections.defaultdict(tree)
some_dict = tree()
some_dict["colors"]["favourite"] = "yellow"

import json 
print(json.dumps(some_dict))
```

输出为:`{"colors": {"favourite": "yellow"}}`



但是如果是非嵌套形式的话，是可以直接赋值的，如下:

```python
some_dict = {}
some_dict["colors"] = "yellow"
print(some_dict)
```

输出为:`{'colors': 'yellow'}`

## counter

Counter是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色： 

```python
from collections import Counter

colors = (
        ("1","red"),
        ("2","blue"),
        ("2","blue"),
        ("3","blue"),
        ("9","blue"),
        ("3","pink"),
        )

favs = Counter((str(color)+"-"+str(num)) for num, color in colors)
favs2 = Counter(color for num, color in colors)

print(favs)
print(favs2)
```

输出如下:

```
Counter({'blue-2': 2, 'red-1': 1, 'blue-3': 1, 'blue-9': 1, 'pink-3': 1})
Counter({'blue': 4, 'red': 1, 'pink': 1})
```


我们也可以在利用它统计一个文件，例如： 
```python
with open('filename', 'rb') as f:
    line_count = Counter(f) 
    print(line_count) 
```

## deque

deque提供了一个双端队列，可以从头尾两端添加和删除元素。
示例程序如下:

```python
from collections import deque

d = deque()
d.append("1")
d.append("2")

print(d)
print(d[1])

print("------------------------")

d1 = deque(range(5))
print(d1)

x = d1.popleft()
y = d1.pop()

print("popleft:{0},pop:{1}".format(x,y))

```

输出结果如下:

```
deque(['1', '2'])
2
------------------------
deque([0, 1, 2, 3, 4])
popleft:0,pop:4
```

我们也可以限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出 去(pop)。 

```python
from collections import deque

d = deque(maxlen=8)
m = [d.append(x) for x in range(8)]

print(m)
print(d)

print("-----------------")

m = [d.append(x) for x in range(9,12)]
print(d)

```

输出如下:

```
[None, None, None, None, None, None, None, None]
deque([0, 1, 2, 3, 4, 5, 6, 7], maxlen=8)
-----------------
deque([3, 4, 5, 6, 7, 9, 10, 11], maxlen=8)
```

还可以从任一端扩展这个队列中的数据：

```python
from collections import deque

d = deque([1,2,3,4,5])

d.extendleft(["a","b"])
print(d)

d.extend(["A","B"])
print(d)
```

输出为:

```python
deque(['b', 'a', 1, 2, 3, 4, 5])
deque(['b', 'a', 1, 2, 3, 4, 5, 'A', 'B'])
```
## namedtuple

介绍命名tuple之前，先看看普通元祖，一个元组是一个不可变的列表，你可以存储一个数据的序列，它和命名元组 (namedtuples)非常像，但有几个关键的不同。 
主要相似点是都不像列表，你不能修改元组中的数据。为了获取元组中的数据，你需要使 用整数作为索引： 

```python
tuple1 = ("x",100)
print(tuple1[1])
```
上述代码输出`100`，如果试着修改tuple的话，如`tuple1[1] = 200`，则会出错`TypeError: 'tuple' object does not support item assignment`。


那namedtuples是什么呢？它把元组变成一个针对简单任务的容器。你不必使用整数索引来访问一个namedtuples的数据。你可以像字典(dict)一样访问namedtuples， 但namedtuples是不可变的。 


```python
from collections import namedtuple
Animal = namedtuple("Animal","name age type")
perry = Animal(name="perry",age=31,type="cat")

print(perry)
print(perry.name)

```

输出如下:

```
Animal(name='perry', age=31, type='cat')
perry
```

现在可以看到，我们可以用名字对tuple进行访问了，一个命名元组(namedtuple)有两个必须的参数，分别是元组名称和字段名称。

namedtuple的每个实例没有对象字典，所以它们很轻量，与普通的元组比，并不 需要更多的内存。这使得它们比字典更快。但是要记住它是一个元组，属性值在namedtuple中是不可变的。

另外，namedtuple还有两点:

- 本身是元组，仍然可以通过数字下标访问
- 可以将一个命名元组转换为字典

```python
from collections import namedtuple
Animal = namedtuple("Animal","name age type")
perry = Animal(name="perry",age=31,type="cat")

print(perry)
print(perry[2])
print(perry._asdict())
```

输出如下:

```
Animal(name='perry', age=31, type='cat')
cat
OrderedDict([('name', 'perry'), ('age', 31), ('type', 'cat')])
```

## enum.Enum (Python 3.4+) 

另一个有用的容器是枚举对象，它属于enum模块，存在于Python 3.4以上版本中。

让我们回顾一下上一个'Animal'命名元组的例子。 它有一个type字段，问题是，type是一个字符串。 那么问题来了，万一程序员输入了Cat，因为他按到了Shift键，或者输入了'CAT'，甚 至'kitten'？ 

枚举可以帮助我们避免这个问题，通过不使用字符串。考虑以下这个例子： 

```python
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    owl = 4
    
    # 
    kitten = 1
    puppy = 2

Animal = namedtuple("Animal","name age type")
perry = Animal(name="Perry",age=31,type=Species.cat)
tom = Animal(name="Tom",age=4,type=Species.dog)
charlie = Animal(name="Charlie",age=2,type=Species.kitten)

print(perry.type == charlie.type)
print(perry.type)

print(perry.type == tom.type)


print("{0}:{1}:{2}".format(Species(1),Species["cat"],Species.cat))

```


输出如下:

```
True
Species.cat
False
Species.cat:Species.cat:Species.cat
```


# 14. 枚举

枚举(enumerate)是Python内置函数。它的用处很难在简单的一行中说明，但是大多数的新人，甚至一些高级程序员都没有意识到它。 它允许我们遍历数据并自动计数。

- 接收参数

```python
setA = set(["A","B","C","D"])

for index,value in enumerate(setA):
    print("{0}:{1}".format(index,value))

print("-------------")

listA = ["A","B","C","D"]

# 可选参数允许我们定制从哪个数字开始枚举
for index,value in enumerate(listA,1):
    print("{0}:{1}".format(index,value))

print("-------------")

# 创建包含索引的元组列表
indexlistA = list(enumerate(listA,101))
print(indexlistA)
```

输出如下，注意两次的输出set的结果不同，说明set中的数据是无序的。

```
C:\Users\61041150\Desktop\20180203\shell\pyData>python pylearn.py
0:B
1:D
2:C
3:A
-------------
1:A
2:B
3:C
4:D
-------------
[(101, 'A'), (102, 'B'), (103, 'C'), (104, 'D')]


C:\Users\61041150\Desktop\20180203\shell\pyData>python pylearn.py
0:A
1:C
2:B
3:D
-------------
1:A
2:B
3:C
4:D
-------------
[(101, 'A'), (102, 'B'), (103, 'C'), (104, 'D')]

```



# 15. 对象自省

自省(introspection)，在计算机编程领域里，是指在运行时来判断一个对象的类型的能力。 它是Python的强项之一。Python中所有一切都是一个对象，而且我们可以仔细勘察那些对 象。

- dir

```python
>>> listA = [1,2,3]
>>> dir(listA)
```

上面的自省给了我们一个列表对象的所有方法的名字。当你没法回忆起一个方法的名字， 这会非常有帮助。如果我们运行dir()而不传入参数，那么它会返回当前作用域的所有名 字。 

- type与id

```python
>>> type(listA)
<class 'list'>
>>> type(" ")
<class 'str'>
>>> type(2)
<class 'int'>
>>> id(listA)
24097976
```

- inspect模块

inspect模块也提供了许多有用的函数，来获取活跃对象的信息。比方说，你可以查看一 个对象的成员，只需运行： 

```python
>>> import inspect

>>> print(inspect.getmembers(str))

```

# 16. 推导式


> 参考 [21. 列表生成式](http://road2ai.info/2017/09/11/Python3-Liao_02/#21-%E5%88%97%E8%A1%A8%E7%94%9F%E6%88%90%E5%BC%8F)

## 列表推导式（list comprehensions） 

如果我们要生成一个list的平方，可能会用下面for循环的方式，但是如果用列表推倒式，一行就搞定:

```python
squared1 = []
for x in range(5):
    squared1.append(x**2)

print(squared1)

# 
squared2 = [x**2 for x in range(5)]
print(squared2)

```

都输出 `[0, 1, 4, 9, 16]`。

同样，通过列表推倒式也可以用于过滤元素，输出`[0, 3, 6, 9, 12]`:

```python
mul = [i for i in range(15) if i % 3 is 0]
print(mul)
```

当然上面的也可以用map和filter来实现，但是列表推倒式还是更简明:

```python
print(list(filter(lambda x:x%3==0,range(15))))
print(list(map(lambda x:x**2,range(5))))
```

分别输出为`[0, 3, 6, 9, 12]`和`[0, 1, 4, 9, 16]`。

## 字典推导式（dict comprehensions） 

示例如下:

```python
# 1
mcase = {"a":10,"b":34,"A":7,"z":3,"Z":10}
mcase_frequency = {k.lower():mcase.get(k.lower(),0) + mcase.get(k.upper(),0) for k in mcase.keys()}

print(mcase_frequency)

# 2
mcase_change = {v:k for k,v in mcase_frequency.items()}
print(mcase_change)
```

上面`# 1`,将同一个字母，但是大小写不同的，其所对应的数字求和了:

- `k.lower()`是生成的字典的key，后面根据key去计算其大小写后取对应的数字，有可能没有对应的大写或是小写，则默认为0
- `for k in mcase.keys()` 这个是循环器，将字典的key取出来，大写A小写a虽然被计算两次，但因为数据结构是字典，最终只会保留一个

上面的`# 2`，将字典的key和value进行了反转。


## 集合推导式（set comprehensions） 

它们跟列表推导式也是类似的。 唯一的区别在于它们使用大括号{}。 举个例子： 

```python
squared_set = {x**2 for x in range(-5,6)}
print(squared_set)

squared_list = [x**2 for x in range(-5,6)]
print(squared_list)
```

输出如下:

```
{0, 1, 4, 9, 16, 25}
[25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
```

# 17. 异常

最基本的异常处理是  try/except从句，将可能触发异常的代码放到try语句中，而处理异常的代码在except中实现，如下是一个简单的例子:


```python
try:
    file = open("text.txt","rb")
except IOError as e:
    print("An IOError occurred:\n{}".format(e.args[-1]))
```

当一个文件不存存在时会触发异常，输出结果如下:

```
An IOError occurred:
No such file or directory
```

## 处理多个异常

通常有如下的三种方式来处理异常:

- 将多个异常放在一个元组里面

```python
try:
    file = open("text.txt","rb")
except (IOError,EOFError) as e:
    print("An Error occurred:\n{}".format(e.args[-1]))

```

- 使用多个except语句

```python
try:
    file = open("text.txt","rb")
except EOFError as e:
    print("An EOFError occurred.")
    raise e
except IOError as e:
    print("An IOError occurred.")
    raise e
```


- 不显式指定异常名，捕获所有异常

```python
try:
    file = open("text.txt","rb")
except Exception:
    print("An error occurred.")
    raise

```

上面通过`raise`显式引发异常，异常被触发后输出如下:

```python
An error occurred.
Traceback (most recent call last):
  File "pylearn.py", line 2, in <module>
    file = open("text.txt","rb")
FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
```




## finally从句


try...except..finally异常处理从句中，finally中代码是不管异常是否触发都将会被执行，这样可以用在脚本执行完的清理工作。


```python
try:
    file = open("test.txt","rb")
    print("Open Successfull!")
except IOError as e:
    print("An IOError occurred: {}".format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred")
```

- 没有触发异常，正常打开文件时的输出:

```
Open Successfull!
This would be printed whether or not an exception occurred
```

- 触发异常，没有找到可以打开的文件时的输出:

```
An IOError occurred: No such file or directory
This would be printed whether or not an exception occurred
```


## try/else从句

类似于for/else，感觉不是很常用的else语句，如果想在没有触发异常的时候执行一些代码，可以很简单的通过else从句来实现。
可能会有这样的疑问，既然只是想让代码在没有触发异常时被执行，为什么不直接放在try中呢？答案是如果放在try中这部分代码的异常会被捕获，而放在else中，不会被捕获。

> 实际的使用场景中，不知道什么case需要这样使用。

举例如下:

- 
try正常执行，没有触发异常，所以else会被执行:

```python
try:
    print("try: I am sure no exception is going to occur!")
    # 1
    # file = open("test1.txt","rb")
except Exception as e:
    print("except: exception")
else:
    print("else: This would only run if no exception occurs,and an error would not be caught")
    # 2
    # file = open("test1.txt","rb")
finally:
    print("finally: This would be printed in every case.")

```

输出为:

```
try: I am sure no exception is going to occur!
else: This would only run if no exception occurs,and an error would not be caugh
t
finally: This would be printed in every case.

```

- 
try异常结束，被except捕获异常，else不会被执行:

```python
try:
    print("try: I am sure exception is going to occur!")
    # 1
    file = open("test1.txt","rb")
except Exception as e:
    print("except: exception")
else:
    print("else: This would only run if no exception occurs,and an error would not be caught")
    # 2
    # file = open("test1.txt","rb")
finally:
    print("finally: This would be printed in every case.")
```

输出如下:

```
try: I am sure  exception is going to occur!
except: exception
finally: This would be printed in every case.
```

- try正常结束，else被执行，但是else中的异常不会被捕获，而是直接触发异常：

```python
try:
    print("try: I am sure no exception is going to occur!")
    # 1
    # file = open("test1.txt","rb")
except Exception as e:
    print("except: exception")
else:
    print("else: This would only run if no exception occurs,and an error would not be caught")
    # 2
    file = open("test1.txt","rb")
finally:
    print("finally: This would be printed in every case.")
```

输出如下:

```
try: I am sure no exception is going to occur!
else: This would only run if no exception occurs,and an error would not be caught
finally: This would be printed in every case.

Traceback (most recent call last):
  File 
"pylearn.py", line 10, in <module>
    file = open("test1.txt","rb")
FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
```

else从句只会在没有异常的情况下执行，而且它会在finally语句之前被执行。

# 18. lambda表达式

```python
add = lambda x,y:x+y
print(add(3,5))

a = [(1,2),(4,1),(9,10),(13,-3)]
a.sort(key=lambda x:x[1])
print(a)

print("-------------")

# 列表并行排序
list1 = (1,2,3,4)
list2 = (3,4,5,6)

data = zip(list1,list2)
print(type(data))
for x,y in data:
    print("{0}:{1}".format(x,y))
#data.sort()
#list1,list2 = map(lambda t:list(t),zip(*data))
```

输出如下:

```
8
[(13, -3), (4, 1), (1, 2), (9, 10)]
-------------
<class 'zip'>
1:3
2:4
3:5
4:6
```



# 19. 一行式

- 简易Web Server

```python
# Python 2
python -m SimpleHTTPServer

# Python 3
python -m http.server 
```python


- 漂亮打印 `pprint`

```python
from pprint import pprint

my_dict = {"name":"lj","age":20,"male":True,"wife":"wanling"}

pprint(my_dict)
print(my_dict)
```
输出如下:

```
{'age': 20, 'male': True, 'name': 'lj', 'wife': 'wanling'}
{'name': 'lj', 'age': 20, 'male': True, 'wife': 'wanling'}
```

这种方法在字典上更为有效。
此外，如果你想快速漂亮的从文件打印出json数据，那么可以这么做：`cat file.json | python -m json.tool`


 

- 脚本性能分析 

这可能在定位你的脚本中的性能瓶颈时，会非常奏效，`python -m cProfile my_script.py` 


- 列表扁平

```python
import itertools

a_list = [[1,2],[3,4],[5,6]]

print(list(itertools.chain.from_iterable(a_list)))

print(list(itertools.chain(*a_list)))

```
输出如下:

```
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
```

另外，关于一行式的构造器和CSV转换JSON，现在不知道有何用处，暂时跳过。

# 20. For - Else

for循环是每个程序语言中最基本的控制语句，但是大部分人不知道在python中for还有一个else子句，else子句会在循环正常结束(即不是被break中断)时被调用。常见的应用场景为，如果我们跑一个循环，查找一个元素，一旦找到就break，这个for循环有两个场景会停止循环:

- 找到元素，break
- 没找到元素，for循环完毕

如果我们想知道到底是如何停止循环的，即确认到底有没有找到元素，一个方法是做一个标记，在break前标记，另一个方式就是使用else子句，for else结构如下:

```python
for item in container:
	if search_something(item):
		# Found it!
		process(item)
		break 
else:
	# Didn't find anything..
	not_found_in_container() 
```

实例:

```python
listA = [1,4,5,6]
myelement = 40

# 方法1
founder = False
for i in listA:
    if i == myelement:
        founder = True

if founder == False:
    print("not found!")
else:
    print("found!")

#
print("-------------------")

# 方法2
for i in listA:
    if i == myelement:
        print("found!")
        break
else:
        print("not found!")
```

输出如下:

```
not found!
-------------------
not found!
```

上面的例子好像没有什么说服力，看下面的例子，直接将质数一起打印出来:

```python
for i in range(2,10):
    for n in range(2,i):
        if i%n == 0:
            print("{0}: {0} / {1}".format(i,n))
            break
    else:
        print("  prime:{}".format(i))
```

输出如下:

```
  prime:2
  prime:3
4: 4 / 2
  prime:5
6: 6 / 2
  prime:7
8: 8 / 2
9: 9 / 3
```

# 21. 使用C扩展

# 22. open函数(文件读取)

参考:[文件读写](http://road2ai.info/2017/12/12/Python3-Liao_07/)

下面是一段文件读取的极简代码，存在如下的问题:

- 如果文件open不成功，最后的close就不会被调用，那么这个文件的句柄就不会被释放
- 需要自己显式的关闭文件

```python
f = open("photo.jpg","r+")
jpgdata = f.read()
f.close()
```

使用with语句就能避免上述问题，示例如下:

> 如下程序中读取一个文件，检测它是否是JPG（提示：这些文件头部以字节FF D8开始），把对输入文件的描述写入一个文本文件。 

```python
import io

with open("photo.jpg","rb") as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b"\xff\xd8"):
    text = u"This is a JPEG file (%d bytes long) \n"
else:
    text = u"This is a random file (%d bytes long) \n"

with io.open("summary.txt","w",encoding="utf-8") as outf:
    outf.write(text % len(jpgdata))
```

关于open的第二个参数，有如下常用参数:

- `r`,读取
- `r+`,读取并写入
- `w`,覆盖写入文件
- `a`,文件末尾追加内容

# 23. 目标Python

# 24. 协程

python中的协程和生成器很相似但又稍有不同，主要区别为:

- 生成器是数据的生产者
- 协程是数据的消费者

例如下面的例子，这样做不仅快而且不会给内存带来压力，因为我们所需要的值都是动态生成，而不是将他们存储在列表中。

```python
def fib():
    a,b = 0,1
    while a < 100:
        yield a
        a,b = b,a+b

for i in fib():
    print(i)
```

更概括的说上面的例子中使用yield便可获得一个协程，协程会消费掉发送给它的值。

```python
def grep(pattern):
    print("Searching for",pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep("coroutine")
next(search)

search.send("I love you")
search.send("Dont you love me?")
search.send("I love coroutine instead")

```

输出结果为:

```
Searching for coroutine
I love coroutine instead
```

在这里yield成了一个协程，它将不再包含任何初始值，相反要从外部传值给它，我们可以通过send()方法向它传值,发送的值会被yield接收。

为什么要运行next()方法呢？这样做正是为了启动一个协程,就像协程中包含的生成器并不是立刻执行，而是通过next()方法来响应send()方 法。因此，你必须通过next()方法来执行yield表达式。 

可以通过调用close()方法来关闭一个协程。像这样： 

```
search = grep('coroutine')
search.close() 
```

如果在close之后继续使用send的话，会出现如下的error:

```python
Traceback (most recent call last):
  File "pylearn.py", line 17, in <module>
    search.send("I love coroutine instead")
StopIteration
```

# 25. 函数缓存

# 26. 上下文管理器