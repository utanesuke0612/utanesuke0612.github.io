---
layout: post
title: Python中级进阶(intermediatePython)
date: 2018-03-22 07:00:00
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
详细参考[16.5 参数组合](http://road2autodrive.info/2017/09/11/Python3-Liao_02/#165-%E5%8F%82%E6%95%B0%E7%BB%84%E5%90%88)

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
- [16. 【重要！】函数的参数](http://road2autodrive.info/2017/09/11/Python3-Liao_02/#16-%E9%87%8D%E8%A6%81%E5%87%BD%E6%95%B0%E7%9A%84%E5%8F%82%E6%95%B0)

- [*argv和**argv](http://road2autodrive.info/2017/09/11/Python3-Liao_03/#31-%E8%A3%85%E9%A5%B0%E5%99%A8)


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

关于迭代，生成器等，可以参考[20. 迭代](http://road2autodrive.info/2017/09/11/Python3-Liao_02/#20-%E8%BF%AD%E4%BB%A3)

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

> 参考[map/filter/reduce](http://road2autodrive.info/2017/09/11/Python3-Liao_03/#26-mapreduce)

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

参考 [16.2 默认参数](http://road2autodrive.info/2017/09/11/Python3-Liao_02/#162-%E9%BB%98%E8%AE%A4%E5%8F%82%E6%95%B0)中，默认参数必须指向不变的对象的例子。

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

# 12. 虚拟环境

# 13. 容器

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

# 16. 推导式

# 17. 异常

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

# 21. 使用C扩展

# 22. open函数

# 23. 目标Python

# 24. 协程 

# 25. 函数缓存

# 26. 上下文管理器