---
layout: post
title: Uda-DataAnalysis-22-[扩展]-free R tutorial by datacamp
date: 2017-10-21 00:00:00
categories: Uda-数据分析进阶
tags: R Udacity DataAnalysis 
---
* content
{:toc}

>根据Quick R的推荐，先使用[R tutorial by datacamp](https://www.datacamp.com/courses/free-introduction-to-r)入门。

笔记参考 [notebook](http://www.utanesuke.shop/03-R-action/tutorial-datacamp.nb.html)

# 1. Intro to basics

## 1.1 Arithmetic with R

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation 幂运算: `^`
- Modulo 取余: `%%`, `如 5 %% 3 is 2.`

## 1.2 Variable assignment

使用 `<-`赋值，如`my_var <- 4`。

## 1.3 Basic data types in R

- Decimals values like 4.5 are called `numerics`.
- Natural numbers like 4 are called integers. Integers are also `numerics`.
- Boolean values (TRUE or FALSE) are called `logical`.
- Text (or string) values are called `characters`.


```python
> # Declare variables of different types
> my_numeric <- 42
> my_character <- "universe"
> my_logical <- FALSE
> 
> # Check class of my_numeric
> class(my_numeric)
[1] "numeric"

> # Check class of my_character
> class(my_character)
[1] "character"
 
> # Check class of my_logical
> class(my_logical)
[1] "logical"
 
```

# 2. Vectors

## 2.1 Create a vector

Vectors are one-dimension arrays that can hold numeric data, character data, or logical data. In other words, a vector is a simple tool to store data. 

vector使用`c()`连接函数创建，如下示例，注意vector中可以混合不同的数据类型:

```python
> numeric_vector <- c(1, 10, 49)
> numeric_vector
[1]  1 10 49
> 
> character_vector <- c("a", "b", "c")
> character_vector
[1] "a" "b" "c"
> 

> boolean_vector <- c(TRUE,"a",TRUE)
> boolean_vector
[1] "TRUE" "a"    "TRUE"
```

## 2.2 Naming a vector

命名类似于给vector每个元素一个标签，使用`names(roulette_vector)` 函数。

```python
> # Poker winnings from Monday to Friday
> poker_vector <- c(140, -50, 20, -120, 240)
> 
> # Roulette winnings from Monday to Friday
> roulette_vector <- c(-24, -50, 100, -350, 10)
> 
> # Assign days as names of poker_vector
> names(poker_vector) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
> poker_vector
   Monday   Tuesday Wednesday  Thursday    Friday 
      140       -50        20      -120       240
> 
> # Assign days as names of roulette_vectors
> names(roulette_vector) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
> roulette_vector
   Monday   Tuesday Wednesday  Thursday    Friday 
      -24       -50       100      -350        10
```


当然也可以定义一个标签的vector，然后将这个定义的变量赋值给已有vector的names()函数

```python
> # The variable days_vector
> days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
> 
> # Assign the names of the day to roulette_vector and poker_vector
> names(poker_vector) <-   days_vector
> names(roulette_vector) <- days_vector
```

## 2.3 计算vector

- 一维数组的计算:

```python
> A_vector <- c(1, 2, 3)
> B_vector <- c(4, 5, 6)
> 
> # Take the sum of A_vector and B_vector
> total_vector <- A_vector + B_vector
> 
> # Print out total_vector
> total_vector
[1] 5 7 9
```


- 如果维度不同会出现警告信息，但是可以计算:

```python
> A_vector <- c(1, 2, 3,4,5)
> B_vector <- c(4, 5, 6)
 
> # Take the sum of A_vector and B_vector
> total_vector <- A_vector + B_vector
Warning message:
In A_vector + B_vector :
  longer object length is not a multiple of shorter object length

> # Print out total_vector
> total_vector
[1]  5  7  9  8 10
```


- 如果计算用的vector有name属性，相加之后，name属性会被结果继承:

```python
> # Poker and roulette winnings from Monday to Friday:
> poker_vector <- c(140, -50, 20, -120, 240)
> roulette_vector <- c(-24, -50, 100, -350, 10)
> days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
> names(poker_vector) <- days_vector
> names(roulette_vector) <- days_vector
 
> # Assign to total_daily how much you won/lost on each day
> total_daily <- poker_vector + roulette_vector
> total_daily
   Monday   Tuesday Wednesday  Thursday    Friday 
      116      -100       120      -470       250
> 
```

- sum用于计算vector内各元素的和:

```python
> # Poker and roulette winnings from Monday to Friday:
> poker_vector <- c(140, -50, 20, -120, 240)
> roulette_vector <- c(-24, -50, 100, -350, 10)
> days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
> names(poker_vector) <- days_vector
> names(roulette_vector) <- days_vector
 
> # Total winnings with poker
> total_poker <- sum(poker_vector)
 
> # Total winnings with roulette
> total_roulette <-  sum(roulette_vector)
 
> # Total winnings overall
> total_week <- total_poker + total_roulette
 
> # Print out total_week
> total_week
[1] -84

```

- mean(poker_start)用于计算平均值。


## 2.4 通过下标取vector中的元素

这个取法太变态了，不是从0开始取值。

- select the `first` element of the vector, you type poker_vector[1]. 
- To select the `second` element of the vector, you type poker_vector[2]
- 选取第一天和第五天: use the vector c(1, 5)，`poker_vector[c(1, 5)]`
- 选取第一天至第五天，`poker_vector[1:5]`
- 还可以通过name 标签选取 `poker_vector[c("Monday","Tuesday")]`


## 2.5 通过比较运算符选取

- `<`  for less than
- `>` for greater than
- `<=` for less than or equal to
- `>=` for greater than or equal to
- `==` for equal to each other
- `!=` not equal to each other


```python
> c(4, 5, 6) > 5
[1] FALSE FALSE TRUE
```

通过计算出来的bool的vector，可以作为vector的选择器。这些功能都跟python的pandas库类似。

```python
> poker_vector <- c(140, -50, 20, -120, 240)
> roulette_vector <- c(-24, -50, 100, -350, 10)
> days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
> names(poker_vector) <- days_vector
> names(roulette_vector) <- days_vector
> 
> selection_vector <- poker_vector > 0
> 
> poker_winning_days <- poker_vector[selection_vector]
> poker_winning_days
   Monday Wednesday    Friday 
      140        20       240
```

# 3. Matrices 矩阵

在R中，用矩阵表示一组相同数据类型元素的集合，给定一个固定的行和列，它是二维的。

使用函数`matrix()`来创建，例如`matrix(1:9, byrow = TRUE, nrow = 3)`，表示:
1. 第一个参数表示填充到矩阵的参数，`c(1,2,3,4,5,6,7,8,9)`与其等同。
2. 第二个参数byrow，表示是否是按照行进行填充，TRUE的话，从行开始填充，否则从列开始填充
3. 第三个参数表示行数目。

```python
> # Construct a matrix with 3 rows that contain the numbers 1 up to 9
> matrix(1:9, byrow = TRUE, nrow = 3)
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9

> # Construct a matrix with 3 rows that contain the numbers 1 up to 9
> matrix(1:9, byrow = FALSE, nrow = 3)
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```

## 3.1 分析矩阵

```python
> # Box office Star Wars (in millions!)
> new_hope <- c(460.998, 314.4)
> empire_strikes <- c(290.475, 247.900)
> return_jedi <- c(309.306, 165.8)
 
> # Create box_office
> box_office <- c(new_hope,empire_strikes,return_jedi)
 
> # Construct star_wars_matrix
> star_wars_matrix <- matrix(box_office,byrow=TRUE,nrow=3)
> star_wars_matrix
        [,1]  [,2]
[1,] 460.998 314.4
[2,] 290.475 247.9
[3,] 309.306 165.8
```

上面的示例，先用`c(new_hope,empire_strikes,return_jedi)`，将三个小的vector合并为一个，然后用这个合并后的vector去生成一个矩阵。

## 3.2 矩阵命名

类似上面的vector，也可以给矩阵命名，使用函数`rownames()`和`colnames()`

```python
# Box office Star Wars (in millions!)
> new_hope <- c(460.998, 314.4)
> empire_strikes <- c(290.475, 247.900)
> return_jedi <- c(309.306, 165.8)
> 
> # Construct matrix
> star_wars_matrix <- matrix(c(new_hope, empire_strikes, return_jedi), nrow = 3, byrow = TRUE)
> 
> # Vectors region and titles, used for naming
> region <- c("US", "non-US")
> titles <- c("A New Hope", "The Empire Strikes Back", "Return of the Jedi")
> 
> # Name the columns with region
> colnames(star_wars_matrix) <- region
> 
> # Name the rows with titles
> rownames(star_wars_matrix) <- titles
> 
> # Print out star_wars_matrix
> star_wars_matrix
                             US non-US
A New Hope              460.998  314.4
The Empire Strikes Back 290.475  247.9
Return of the Jedi      309.306  165.8

```

## 3.3 计算

- rowSums()，行求和
注意下面的`matrix()`，在定义矩阵的时候就直接给其命名了，另外通过`rowSums`计算每行数据的和，即每部电影的所有票房。

```python
# Calculate worldwide box office figures
> worldwide_vector <- rowSums(star_wars_matrix)
> # Construct star_wars_matrix
> box_office <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)

> star_wars_matrix <- matrix(box_office, nrow = 3, byrow = TRUE,
                             dimnames = list(c("A New Hope", "The Empire Strikes Back", "Return of the Jedi"), 
                                             c("US", "non-US")))
 
> star_wars_matrix
                             US non-US
A New Hope              460.998  314.4
The Empire Strikes Back 290.475  247.9
Return of the Jedi      309.306  165.8
 
> # Calculate worldwide box office figures
> worldwide_vector <- rowSums(star_wars_matrix)
> worldwide_vector
            A New Hope The Empire Strikes Back      Return of the Jedi 
              775.398                 538.375                 475.106
> 
```

## 3.4 矩阵合并

- cbind()，列增加

使用函数`cbind()`对多个矩阵进行连接，rowSums计算得到的是行上的和，矩阵相加后，为每行数据上增加了一个列(sum)。

```python
 # Construct star_wars_matrix
> box_office <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)
> star_wars_matrix <- matrix(box_office, nrow = 3, byrow = TRUE,
                             dimnames = list(c("A New Hope", "The Empire Strikes Back", "Return of the Jedi"), 
                                             c("US", "non-US")))
> 
> # The worldwide box office figures
> worldwide_vector <- rowSums(star_wars_matrix)
> worldwide_vector
             A New Hope The Empire Strikes Back      Return of the Jedi 
                775.398                 538.375                 475.106
> 
> # Bind the new variable worldwide_vector as a column to star_wars_matrix
> all_wars_matrix <- cbind(star_wars_matrix,worldwide_vector)
> all_wars_matrix
                             US non-US worldwide_vector
A New Hope              460.998  314.4          775.398
The Empire Strikes Back 290.475  247.9          538.375
Return of the Jedi      309.306  165.8          475.106
```


- rbind()，行增加

```python
> # star_wars_matrix and star_wars_matrix2 are available in your workspace
> star_wars_matrix
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
> star_wars_matrix2
                        US non-US
The Phantom Menace   474.5  552.5
Attack of the Clones 310.7  338.7
Revenge of the Sith  380.3  468.5
> 
> # Combine both Star Wars trilogies in one matrix
> all_wars_matrix <- cbind(star_wars_matrix,star_wars_matrix2)
> all_wars_matrix
                           US non-US    US non-US
A New Hope              461.0  314.4 474.5  552.5
The Empire Strikes Back 290.5  247.9 310.7  338.7
Return of the Jedi      309.3  165.8 380.3  468.5


 # Combine both Star Wars trilogies in one matrix
> all_wars_matrix <- rbind(star_wars_matrix,star_wars_matrix2)
> all_wars_matrix
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
The Phantom Menace      474.5  552.5
Attack of the Clones    310.7  338.7
Revenge of the Sith     380.3  468.5
```

- colSums()，列求和

```python
 # all_wars_matrix is available in your workspace
> all_wars_matrix
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
The Phantom Menace      474.5  552.5
Attack of the Clones    310.7  338.7
Revenge of the Sith     380.3  468.5
> 
> # Total revenue for US and non-US
> total_revenue_vector <- colSums(all_wars_matrix)
> 
> # Print out total_revenue_vector
> total_revenue_vector
    US non-US 
2226.3 2087.8
```


## 3.5 矩阵中的元素选取

- my_matrix[1,2]，选取第一行和第二列
- my_matrix[1:3,2:4] ，选取1,2,3行 的 2,3,4列
- my_matrix[,1],所有行的第一列
- my_matrix[1,]，所有列的第一行

```python
> # all_wars_matrix is available in your workspace
> all_wars_matrix
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
The Phantom Menace      474.5  552.5
Attack of the Clones    310.7  338.7
Revenge of the Sith     380.3  468.5
> 
> # Select the non-US revenue for all movies
> non_us_all <- all_wars_matrix[,2]
> 
> # Average non-US revenue
> mean(non_us_all)
[1] 347.9667
> 
> # Select the non-US revenue for first two movies
> non_us_some <- all_wars_matrix[1:2,2]
> 
> # Average non-US revenue for first two movies
> mean(non_us_some)
[1] 281.15
```

## 3.6 矩阵的数学运算

`+, -, /, *`，这些标准数学运算符，同样适合于矩阵中，针对矩阵中每个元素进行运算。


```python
 # all_wars_matrix and ticket_prices_matrix are available in your workspace
> all_wars_matrix
                           US non-US
A New Hope              461.0  314.4
The Empire Strikes Back 290.5  247.9
Return of the Jedi      309.3  165.8
The Phantom Menace      474.5  552.5
Attack of the Clones    310.7  338.7
Revenge of the Sith     380.3  468.5
> ticket_prices_matrix
                         US non-US
A New Hope              5.0    5.0
The Empire Strikes Back 6.0    6.0
Return of the Jedi      7.0    7.0
The Phantom Menace      4.0    4.0
Attack of the Clones    4.5    4.5
Revenge of the Sith     4.9    4.9
> 
> # Estimated number of visitors
> visitors <- all_wars_matrix / ticket_prices_matrix
> 
> # US visitors
> us_visitors <- all_wars_matrix[,1]/ticket_prices_matrix[,1]
> 
> # Average number of US visitors
> mean(us_visitors)
[1] 75.01401
```

# 4.  Factors(因素,因子)

factor是一种用于存储分类变量(categorical variables)的统计型数据类型，分类变量从属于一组有限个数的分类集合，比如性别。连续变量(continuous variable)对应无限的数据值。

## 4.1 factor()

使用`factor()`创建factor，如下示例中其`'factor levels'`为`Female和male`

```python
> # Gender vector
> gender_vector <- c("Male", "Female", "Female", "Male", "Male")
> 
> # Convert gender_vector to a factor
> factor_gender_vector <-factor(gender_vector)
> 
> # Print out factor_gender_vector
> factor_gender_vector
[1] Male   Female Female Male   Male  
Levels: Female Male
```

分类变量，可以分为两种类型，
- nominal categorical variable，比如`猩猩，大象，鳄鱼`等分类之间没有等级和大小之分
- ordinal categorical variable，比如`大，中，小`，分类之间有等级之分。


## 4.2 Factor levels

通过`levels()`可以给factor定义level，要注意其顺序

```python
> # Code to build factor_survey_vector
> survey_vector <- c("M", "F", "F", "M", "M")
> factor_survey_vector <- factor(survey_vector)
> factor_survey_vector
[1] M F F M M
Levels: F M
> 
> # Specify the levels of factor_survey_vector
> levels(factor_survey_vector) <-c("Female", "Male")
> 
> factor_survey_vector
[1] Male   Female Female Male   Male  
Levels: Female Male
```

## 4.3 summary()概要函数

```python
> # Build factor_survey_vector with clean levels
> survey_vector <- c("M", "F", "F", "M", "M")
> factor_survey_vector <- factor(survey_vector)
> levels(factor_survey_vector) <- c("Female", "Male")
> factor_survey_vector
[1] Male   Female Female Male   Male  
Levels: Female Male
> 
> # Generate summary for survey_vector
> summary(survey_vector)
   Length     Class      Mode 
        5 character character
> 
> # Generate summary for factor_survey_vector
> summary(factor_survey_vector)
Female   Male 
     2      3

```


## 4.4 factor的比较运算

factor在使用下标运算后，得到的factor，其level不变。factor之间不能进行比较运算。

```python
 survey_vector <- c("M", "F", "F", "M", "M","N")
> factor_survey_vector <- factor(survey_vector)
> levels(factor_survey_vector) <- c("Female", "Male","Newhalf")
> 
> # Male
> male <- factor_survey_vector[1]
> male
[1] Male
Levels: Female Male Newhalf
> 
> # Female
> female <- factor_survey_vector[2]
> female
[1] Female
Levels: Female Male Newhalf
> 
> # Battle of the sexes: Male 'larger' than female?
> male > female
Warning message: '>' not meaningful for factors
[1] NA
```

## 4.5 Ordered factors

在前面我们说了factor分为两类，一类是没有等级大小之分的，还有一类是有的，通过factor()函数默认建立的是前者即无等级之分的，如果要创建第二种，需要传入参数:

```python
factor(some_vector,
       ordered = TRUE,
       levels = c("lev1", "lev2" ...))
```


```python
> # Create speed_vector
> speed_vector <- c("fast", "slow", "slow", "fast", "insane")
> 
> # Convert speed_vector to ordered factor vector
> factor_speed_vector <- factor(speed_vector,ordered = TRUE,levels=c("slow","fast","insane"))
> 
> # Print factor_speed_vector
> factor_speed_vector
[1] fast   slow   slow   fast   insane
Levels: slow < fast < insane
> summary(factor_speed_vector)
  slow   fast insane 
     2      2      1
```

## 4.6 比较ordered facotrs

ordered factors在定义的时候，已经给出了顺序，所以能使用比较运算符

```python
> # Create factor_speed_vector
> speed_vector <- c("fast", "slow", "slow", "fast", "insane")
> factor_speed_vector <- factor(speed_vector, ordered = TRUE, levels = c("slow", "fast", "insane"))
> 
> # Factor value for second data analyst
> da2 <- factor_speed_vector[2]
> 
> # Factor value for fifth data analyst
> da5 <- factor_speed_vector[5]
> 
> # Is data analyst 2 faster than data analyst 5?
> da2 > da5
[1] FALSE
```

# 5. Data frames

类似二维矩阵的，但是可以混合多种数据类型

- head()和tail()分别取数据的前部分，和后面部分

```python

 mtcars
                     mpg cyl  disp  hp drat    wt  qsec vs am gear carb
Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
> head(mtcars)
                   mpg cyl disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
> tail(mtcars)
                mpg cyl  disp  hp drat    wt qsec vs am gear carb
Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.7  0  1    5    2
Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.9  1  1    5    2
Ford Pantera L 15.8   8 351.0 264 4.22 3.170 14.5  0  1    5    4
Ferrari Dino   19.7   6 145.0 175 3.62 2.770 15.5  0  1    5    6
Maserati Bora  15.0   8 301.0 335 3.54 3.570 14.6  0  1    5    8
Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.6  1  1    4    2
> 
```

- 通过`str()`也可以获取data frame的概要

```python
> # Investigate the structure of mtcars
> str(mtcars)
'data.frame':	32 obs. of  11 variables:
 $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
 $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
 $ disp: num  160 160 108 258 360 ...
 $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
 $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
 $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
 $ qsec: num  16.5 17 18.6 19.4 17 ...
 $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
 $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
 $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
 $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
```


## 5.1 创建 data frame `data.frame()`

```python
> # Definition of vectors
> name <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
> type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet", 
            "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
> diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
> rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
> rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)
 
> # Create a data frame from the vectors
> planets_df <- data.frame(name,type,diameter,rotation,rings)
> planets_df
     name               type diameter rotation rings
1 Mercury Terrestrial planet    0.382    58.64 FALSE
2   Venus Terrestrial planet    0.949  -243.02 FALSE
3   Earth Terrestrial planet    1.000     1.00 FALSE
4    Mars Terrestrial planet    0.532     1.03 FALSE
5 Jupiter          Gas giant   11.209     0.41  TRUE
6  Saturn          Gas giant    9.449     0.43  TRUE
7  Uranus          Gas giant    4.007    -0.72  TRUE
8 Neptune          Gas giant    3.883     0.67  TRUE

> # Check the structure of planets_df
> str(planets_df)
'data.frame':	8 obs. of  5 variables:
 $ name    : Factor w/ 8 levels "Earth","Jupiter",..: 4 8 1 3 2 6 7 5
 $ type    : Factor w/ 2 levels "Gas giant","Terrestrial planet": 2 2 2 2 1 1 1 1
 $ diameter: num  0.382 0.949 1 0.532 11.209 ...
 $ rotation: num  58.64 -243.02 1 1.03 0.41 ...
 $ rings   : logi  FALSE FALSE FALSE FALSE TRUE TRUE ...
```

取元素的方法，与矩阵的下标方式完全一致，如`planets_df[1:5,"diameter"]`，取diameter列的第1到5行数据。

另外还有一种简单的方式如`planets_df$rings`，通过`$`直接获取了rings列的数据。


通过一组bool的vector，获取对应为TRUE的元素

```python
> # Adapt the code to select all columns for planets with rings
> rings_vector
[1] FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE
> planets_df[rings_vector, ]
     name      type diameter rotation rings
5 Jupiter Gas giant   11.209     0.41  TRUE
6  Saturn Gas giant    9.449     0.43  TRUE
7  Uranus Gas giant    4.007    -0.72  TRUE
8 Neptune Gas giant    3.883     0.67  TRUE
> 
```

## 5.2 通过subset()获取子dataframe

```python
> subset(planets_df, subset = diameter < 1)
     name               type diameter rotation rings
1 Mercury Terrestrial planet    0.382    58.64 FALSE
2   Venus Terrestrial planet    0.949  -243.02 FALSE
4    Mars Terrestrial planet    0.532     1.03 FALSE
> 
```

获取直径大于1的数据。

## 5.3 排序

下面是数值型，如果是文字列，则按字母顺序排序。

```python
> a <- c(100, 10, 1000)
> order(a)
[1] 2 1 3
> a[order(a)]
[1]   10  100 1000
```

上面是一维vector排序，下面是二维dataframe的排序，注意下标取元素时与vector的差异

```python
# planets_df is pre-loaded in your workspace
> 
> # Use order() to create positions
> positions <-  order(planets_df$diameter)
> positions
[1] 1 4 2 3 8 7 6 5
> 
> # Use positions to sort planets_df
> planets_df[positions,]
     name               type diameter rotation rings
1 Mercury Terrestrial planet    0.382    58.64 FALSE
4    Mars Terrestrial planet    0.532     1.03 FALSE
2   Venus Terrestrial planet    0.949  -243.02 FALSE
3   Earth Terrestrial planet    1.000     1.00 FALSE
8 Neptune          Gas giant    3.883     0.67  TRUE
7  Uranus          Gas giant    4.007    -0.72  TRUE
6  Saturn          Gas giant    9.449     0.43  TRUE
5 Jupiter          Gas giant   11.209     0.41  TRUE
> 
```


# 6. Lists

先总结下上面学习过的数据类型:

- vectors,能存储数值，字符和bool，vector中的数据有相同的数据类型
- matrices，二维，也只能存储相同数据类型
- data frames,二维，同一列数据类型相同，但是不同列之间可以是不同的数据类型

## 6.1 生成一个list，`list()`

list中可以存储完全不同的数据结构。

```python
 # Vector with numerics from 1 up to 10
> my_vector <- 1:10
> 
> # Matrix with numerics from 1 up to 9
> my_matrix <- matrix(1:9, ncol = 3)
> 
> # First 10 elements of the built-in data frame mtcars
> my_df <- mtcars[1:10,]
> 
> # Construct list with these different elements:
> my_list <- list(my_vector,my_matrix,my_df)
> my_list
[[1]]
 [1]  1  2  3  4  5  6  7  8  9 10

[[2]]
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9

[[3]]
                   mpg cyl  disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
Datsun 710        22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive    21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout 18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
Valiant           18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
Duster 360        14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
Merc 240D         24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
Merc 230          22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
Merc 280          19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
```

## 6.2 给list命名

两种方式：

```python
# 定义时命名
my_list <- list(name1 = your_comp1, 
                name2 = your_comp2)

# 定义之后再命名
my_list <- list(your_comp1, your_comp2)
names(my_list) <- c("name1", "name2")
```

```python
 # Finish the code to build shining_list
> shining_list <- list(moviename = mov,actors=act,reviews=rev)
> shining_list
$moviename
[1] "The Shining"

$actors
[1] "Jack Nicholson"   "Shelley Duvall"   "Danny Lloyd"      "Scatman Crothers"
[5] "Barry Nelson"    

$reviews
  scores sources                                              comments
1    4.5   IMDb1                     Best Horror Film I Have Ever Seen
2    4.0   IMDb2 A truly brilliant and scary film from Stanley Kubrick
3    5.0   IMDb3                 A masterpiece of psychological horror
```



## 6.3 从list中取得元素

比如，如果要取得上面的reviews，可以使用`shining_list[["reviews"]]`和`shining_list$reviews`，
如果取得一个特定的元素 `shining_list[[2]][1]`,将取得 `"Jack Nicholson"`，即列表第二组元素中的第一个。


## 6.4 向list中添加movie信息

```python
ext_list <- c(my_list, my_name = my_val)
```

向my_list中添加一个新的`my_val`元素，生成新的list `ext_list`。

下面的示例中，向shining_list中添加name为year的元素，值为1980

```python
> shining_list_full <- c(shining_list,year=1980)
> 
> # Have a look at shining_list_full
> str(shining_list_full)
List of 4
 $ moviename: chr "The Shining"
 $ actors   : chr [1:5] "Jack Nicholson" "Shelley Duvall" "Danny Lloyd" "Scatman Crothers" ...
 $ reviews  :'data.frame':	3 obs. of  3 variables:
  ..$ scores  : num [1:3] 4.5 4 5
  ..$ sources : Factor w/ 3 levels "IMDb1","IMDb2",..: 1 2 3
  ..$ comments: Factor w/ 3 levels "A masterpiece of psychological horror",..: 3 2 1
 $ year     : num 1980
> 
> 
```