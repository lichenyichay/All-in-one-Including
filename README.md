# Allinone Including 双语版Readme

## Index/目录

Line 9 中文版README

Line 348 Readme in English

## 中文版Readme

### All-in-one Including

多功能一体机库版本，现已更新至4.0.0版本
说明如下：

#### 模块说明

##### 目录

Line 40 Allinone.py 主文件

Line 70 shujuku.py 数据库文件

Line 94 xiaogongju.py 模块文件

Line 128 calculator.py 计算器模块

Line 205 numbertochinese.py 数字、中文互换模块

Line 237 lotterytickets.py 彩票一体机模块

Line 260 erfenchazhao_py.py 二分查找模块

Line 282 marh_cal.py math库计算器模块

Line 304 student_py.py 小学学生信息管理系统模块

Line 324 tuxing_cal.py 图形计算器模块

##### Allinone.py 主文件

```python

Help on module Allinone:

NAME
    Allinone

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/23 17:00
    # @FILE:Allinone.py
    # @version:4.0.1
    # @Software:Visual Studio Code

FUNCTIONS
    allinone(fuwu, mode, *args)
        :param fuwu 需要服务的功能
        :param mode 部分功能需要的模式（详见Github中All-in-one2.4.0分支的Wiki页）
        :param *args 可变参数，表示需要传入的参数，建议用元组或列表类型，具体所需类型见README.MD
        :return: 0：正常，1：不正常，其他返回值表示功能的结果

        功能（按代码顺序排序，不分先后）：大小写互换、抽取随机数、求最小公倍数、求最大公倍数、图形计算器、小学学生信息管理系统、二分查找、求余、向下取整、向上取整、多个数求和、多个数求差、多个数求积、判断闰年、判断是否为质数、整数、小数计算（加减乘除）、分数计算（加减乘除）......（具体见Github All-in-one2.4.0分支Readme.md文件）

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\allinone.py
```

##### shujuku.py 数据库文件

```python
Help on module shujuku:

NAME
    shujuku

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/23 17:00
    # @FILE:Allinone.py
    # @version:4.0.1
    # @Software:Visual Studio Code

FUNCTIONS
    
    sjc(fuwu: str, mode: int, canshu: str)

FILE
    d:\chay\project\all-in-one-including(git)\all-in-one_chaylichenyi\module\shujuku.py
```

##### xiaogongju.py 模块文件

```python
Help on module xiaogongju:

NAME
    xiaogongju

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 17:20
    # @FILE:xiaogongju.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    chouqusuiji(num1: int, num2: int, mode: int, weishu: int) -> str

    daorxiao(args: str, mode: int) -> str

    f(a: float, n: int, m: int) -> int

    kaisamima(arg: str, mode: int, n: int) -> str

    quzheng(num: float, mode: int) -> int

    twonumbers_TheBiggestCommonfactor(num1: int, num2: int) -> int

    twonumbers_TheMinimumCommonmultiple(num1: int, num2: int) -> int

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\xiaogongju.py
```

##### calculator.py 计算器模块

```python
Help on module calculator:

NAME
    calculator

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 17:20
    # @FILE:calculator.py
    # @Software:Visual Studio Code

FUNCTIONS
    FtemporCtemp(mode: str, FtemporCtemp: float) -> float

    duihuan(mode: int, money: float) -> float

    fab(x: int) -> int

    factorization(num: int) -> list[int]

    fanzhuanzifuchuan(s: str) -> str

    fenjisuan(num1: str, num2: str, mode: str) -> float

    isfab(x: int) -> bool

    isfabhuiwenshu(x: int) -> bool

    isfabhuiwenzhishu(x: int) -> bool

    isfabparam(x: int) -> bool

    isfabwanquanpingfangshu(num: int) -> bool

    ishuiwenshu(d: int) -> bool

    ishuiwenzhishu(d: int) -> bool

    isleapyear(x) -> bool

    isparam(d: int) -> bool

    istribonacci(n: int) -> bool

    istribonaccihuiwenshu(n: int) -> bool

    istribonaccihuiwenshuparam(n: int) -> bool

    istribonacciparam(n: int) -> bool

    istribonacciwanquanpingfangshu(num: int) -> bool

    iswanquanpingfangshu(num: int) -> bool

    jinzhizhuanhuan(a: int, b: int, c: str) -> str

    mima(num: int, n: int) -> int

    tribonacci(n: int) -> int

    wanquanpingfangshu(num: int) -> int

    xiaoorfen(num: str, mode: int) -> str

    xiaoorzhengjisuan(num1: float, num2: float, mode: str) -> float

    yiyuannci(fangcheng: str, mode: int) -> tuple

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\calculator.py

```

##### numbertochinese.py 数字、中文互换模块

```python
Help on module numbertochinese:

NAME
    numbertochinese

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 18:00
    # @FILE:numbertochinese.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    No2Cn(number: int) -> str

    chinese2digits(uchars_chinese: str) -> int

    maxdigit(number: int, count: int) -> tuple

DATA
    common_used_numerals = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '日': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
    digitdict = {1: '十', 2: '百', 3: '千', 4: '万'}
    numdict = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",0:"零"}

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\numbertochinese.py
```

##### lotterytickets.py 彩票一体机模块

```python
Help on module lotterytickets:

NAME
    lotterytickets

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/5/3 23:25
    # @FILE:lotterytickets.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    lotterytickets(user: str, mubiao: str, mode: int) -> str

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\lotterytickets.py
```

##### erfenchazhao_py.py 二分查找模块

```python
Help on module erfenchazhao_py:

NAME
    erfenchazhao_py

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2022/12/25 9:03
    # @FILE:erfenchazhao_py.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    erfenchazhao(yuanlst, shengxulst, target)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\erfenchazhao_py.py
```

##### math_cal.py math库计算器模块

```python
Help on module math_cal_py:

NAME
    math_cal_py

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2022/12/24 15:38
    # @FILE:math_cal_py.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    math_cal(mode, float1, float2)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\math_cal_py.py
```

##### student_py.py 小学学生信息管理系统模块

```python
Help on module student_py:

NAME
    student_py

DESCRIPTION
    函数名：student
    调用形式：student()
    作用：小学学生信息管理系统

FUNCTIONS
    student()

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\student_py.py
```

##### tuxing_cal.py 图形计算器模块

```python
Help on module tuxing_cal:

NAME
    tuxing_cal

DESCRIPTION
    函数名：tuxing
    调用形式：tuxing(huida)
    :param huida 图形
    :return 0
    作用：进行图形计算

FUNCTIONS
    tuxing(huida, mode, *args2)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\tuxing_cal.py
```

详见<https://github.com/lichenyichay/All-in-one> 和 <https://github.com/lichenyichay/All-in-one-Including/wiki>

##### UnitConvertChay.py 单位转换器&物理量计算模块（需导入UnitConvertChay）

###### 长度单位换算函数
毫米(mm)到其他单位的转换
mmtocm(x: float) -> float：将毫米转换为厘米。
mmtodm(x: float) -> float：将毫米转换为分米。
mmtom(x: float) -> float：将毫米转换为米。
mmtokm(x: float) -> float：将毫米转换为千米。
厘米(cm)到其他单位的转换
cmtodm(x: float) -> float：将厘米转换为分米。
cmtom(x: float) -> float：将厘米转换为米。
cmtokm(x: float) -> float：将厘米转换为千米。
cmtomm(x: float) -> float：将厘米转换为毫米（虽然看似逆向转换，但提供了完整性）。
分米(dm)到其他单位的转换
dmtom(x: float) -> float：将分米转换为米。
dmtokm(x: float) -> float：将分米转换为千米。
dmtomm(x: float) -> float：将分米转换为毫米。
dmtocm(x: float) -> float：将分米转换为厘米。
米(m)到其他单位的转换
mtokm(x: float) -> float：将米转换为千米。
mtomm(x: float) -> float：将米转换为毫米。
mtocm(x: float) -> float：将米转换为厘米（注意与mmtocm函数名相同，但功能不同）。
mtodm(x: float) -> float：将米转换为分米。
千米(km)到其他单位的转换
kmtomm(x: float) -> float：将千米转换为毫米。
kmtocm(x: float) -> float：将千米转换为厘米。
kmtodm(x: float) -> float：将千米转换为分米。
kmtom(x: float) -> float：将千米转换为米。
微米和纳米单位转换
μmtomm(x: float) -> float：将微米转换为毫米。
mmtoμm(x: float) -> float：将毫米转换为微米。
nmtoμm(x: float) -> float：将纳米转换为微米。
μmtonm(x: float) -> float：将微米转换为纳米。

###### 物理量换算函数
密度 ρ
函数定义：def ρ(V=0.0, m=0.0, g=9.8, h=0.0, p=0.0, Ffu=0.0) -> float:
功能说明：计算密度。支持多种计算方式：
如果给定体积 V 和质量 m，则直接计算密度（ρ = m/V）。
如果给定压强 p、重力加速度 g 和高度 h，则计算流体密度（ρ = p / (g * h)）。
如果给定流体浮力 Ffu、重力加速度 g 和体积 V，则通过浮力计算密度（ρ = Ffu / (g * V)）。
如果参数无效，则抛出 ValueError 异常。
质量 m
函数定义：def m(G=0.0, g=9.8, V=0.0, ρ=0.0) -> float:
功能说明：计算质量。支持多种计算方式：
如果给定重力 G 和重力加速度 g，则计算质量（m = G/g）。
如果给定体积 V 和密度 ρ，则计算质量（m = ρ * V）。
如果参数无效，则抛出 ValueError 异常。
体积 Vtiji
函数定义：def Vtiji(m=0.0, ρ=0.0, g=9.8, Ffu=0.0) -> float:
功能说明：根据质量和密度或其他物理量计算体积。支持多种计算方式：
如果给定质量 m 和密度 ρ，则计算体积（V = m/ρ）。
如果给定流体浮力 Ffu、重力加速度 g 和密度 ρ，则通过浮力计算体积（此处逻辑可能需要根据实际物理公式调整）。
如果参数无效，则抛出 ValueError 异常。
速度 Vsudu
函数定义：def Vsudu(Slu=0.0, t=0.0) -> float:
功能说明：计算流速。如果给定流过的距离 Slu 和时间 t，则计算流速（Vs = Slu/t）。如果参数无效，则抛出 ValueError 异常。
压强 p
函数定义：def p(F=0.0, S=0.0, ρ=0.0, g=9.8, h=0.0) -> float:
功能说明：计算压强。支持多种计算方式：
如果给定力 F 和受力面积 S，则计算压强（p = F/S）。
如果给定密度 ρ、高度 h 和重力加速度 g，则计算流体压强（p = ρ * g * h）。
如果参数无效，则抛出 ValueError 异常。
电流 I、电压 U、电阻 R 和功率 Pgong
这些函数（I, U, R, Pgong）分别用于计算电流、电压、电阻和功率，根据欧姆定律（U = I * R）和功率公式（Pgong = U * I）实现。它们各自接收不同的参数组合，并根据提供的参数计算相应的物理量。如果参数无效，则抛出 ValueError 异常。


## Readme in English

### Allinone Readme in English/英文版Allinone使用说明

#### Module Index

Line 364 Allinone Main Module Documentation

Line 370 Calculator Module Documentation

Line 673 Xiaogongju Module Documentation

Line 760 Math_calculator Module Documentation

Line 820 Tuxing_calculator Module Documentation

#### Allinone Main Module Documentation

Allinone.py
Main module for the Allinone Function.
mode:depending on your choice, you can choose the function you want to use.(such as you choose Ftemp or Ctemp you should incoming mode param in "℃to℉" or "℉to℃")

#### Calculator Module Documentation

FtemporCtemp
Converts temperature between Fahrenheit and Celsius.

```python
def FtemporCtemp(mode: str, FtemporCtemp: float) -> float
```

mode: "℃to℉" (Celsius to Fahrenheit) or "℉to℃" (Fahrenheit to Celsius)
FtemporCtemp: Temperature to convert
Returns: Converted temperature (without unit)

duihuan
Performs currency exchange.

```python
def duihuan(mode: int, money: float) -> float
```

mode: 1-16, corresponding to different currency conversions
money: Amount to exchange (in the currency unit before the arrow in the mode)
Returns: Converted currency amount

yiyuannci
Solves linear, quadratic, and cubic equations.

```python
def yiyuannci(fangcheng: str, mode: int) -> tuple
```

fangcheng: Equation in the form ax+b=0, ax^2+bx+c=0, or ax^3+bx^2+cx+d=0
mode: Highest degree of the equation (1, 2, or 3)
Returns: Tuple containing the solution(s) of the equation

fanzhuanzifuchuan
Reverses a string.

```python
def fanzhuanzifuchuan(s: str) -> str
```

s: String to reverse
Returns: Reversed string
isparam
Checks if a number is prime.

```python
def isparam(d: int) -> bool
```

d: Number to check
Returns: True if prime, False otherwise

ishuiwenshu
Checks if a number is a palindrome.

```python
def ishuiwenshu(d: int) -> bool
```

d: Number to check
Returns: True if palindrome, False otherwise

ishuiwenzhishu
Checks if a number is a palindromic prime.

```python
def ishuiwenzhishu(d: int) -> bool
```

d: Number to check
Returns: True if palindromic prime, False otherwise

fab
Calculates the xth number in the Fibonacci sequence.

```python
def fab(x: int) -> int
```

x: Position in the Fibonacci sequence
Returns: The xth Fibonacci number

isfab
Checks if a number is in the Fibonacci sequence.

```python
def isfab(x: int) -> bool
```

x: Number to check (0 < x <= 12586269025)
Returns: True if in Fibonacci sequence, False otherwise

isfabparam
Checks if a number is both in the Fibonacci sequence and prime.

```python
def isfabparam(x: int) -> bool
```

x: Number to check (0 < x <= 12586269025)
Returns: True if Fibonacci prime, False otherwise

isfabhuiwenshu
Checks if a number is both in the Fibonacci sequence and a palindrome.

```python
def isfabhuiwenshu(x: int) -> bool
```

x: Number to check (0 < x <= 12586269025)
Returns: True if Fibonacci palindrome, False otherwise

isfabhuiwenzhishu
Checks if a number is in the Fibonacci sequence, a palindrome, and prime.

```python
def isfabhuiwenzhishu(x: int) -> bool
```

x: Number to check (0 < x <= 12586269025)
Returns: True if Fibonacci palindromic prime, False otherwise

isleapyear
Checks if a year is a leap year.

```python
def isleapyear(x) -> bool
```

x: Year to check
Returns: True if leap year, False otherwise

tribonacci
Calculates the xth number in the Tribonacci sequence.

```python
def tribonacci(n: int) -> int
```

n: Position in the Tribonacci sequence
Returns: The nth Tribonacci number

istribonacci
Checks if a number is in the Tribonacci sequence.

```python
def istribonacci(n: int) -> bool
```

n: Number to check
Returns: True if in Tribonacci sequence, False otherwise

istribonaccihuiwenshu
Checks if a number is both in the Tribonacci sequence and a palindrome.

```python
def istribonaccihuiwenshu(n: int) -> bool
```

n: Number to check
Returns: True if Tribonacci palindrome, False otherwise

istribonaccihuiwenshuparam
Checks if a number is in the Tribonacci sequence, a palindrome, and prime.

```python
def istribonaccihuiwenshuparam(n: int) -> bool
```

n: Number to check
Returns: True if Tribonacci palindromic prime, False otherwise

istribonacciparam
Checks if a number is both in the Tribonacci sequence and prime.

```python
def istribonacciparam(n: int) -> bool
```

n: Number to check
Returns: True if Tribonacci prime, False otherwise

iswanquanpingfangshu
Checks if a number is a perfect square.

```python
def iswanquanpingfangshu(num: int) -> bool
```

num: Number to check
Returns: True if perfect square, False otherwise

wanquanpingfangshu
Calculates the dth perfect square.

```python
def wanquanpingfangshu(num: int) -> int
```

num: Position of the perfect square
Returns: The dth perfect square

isfabwanquanpingfangshu
Checks if a number is both in the Fibonacci sequence and a perfect square.

```python
def isfabwanquanpingfangshu(num: int) -> bool
```

num: Number to check
Returns: True if Fibonacci perfect square, False otherwise

istribonacciwanquanpingfangshu
Checks if a number is both in the Tribonacci sequence and a perfect square.

```python
def istribonacciwanquanpingfangshu(num: int) -> bool
```

num: Number to check
Returns: True if Tribonacci perfect square, False otherwise

jinzhizhuanhuan
Converts numbers between different bases.

```python
def jinzhizhuanhuan(a: int, b: int, c: str) -> str
```

a: Base of input number (2 <= a <= 36)
b: Base of output number (2 <= b <= 36)
c: Number to convert (without prefix, must follow rules of base a)
Returns: Converted number as a string

factorization
Performs prime factorization of a number.

```python
def factorization(num: int) -> list[int]
```

num: Number to factorize
Returns: List of prime factors

mima
Extracts a password from a number.

```python
def mima(num: int, n: int) -> int
```

num: Number to extract password from
n: Number of digits in the password
Returns: Extracted password

xiaoorfen
Converts between decimal and fraction representations.

```python
def xiaoorfen(num: str, mode: int) -> str
```

num: Number to convert
mode: 1 (decimal to fraction) or 2 (fraction to decimal)
Returns: Converted number as a string

xiaoorzhengjisuan
Performs arithmetic operations on decimals or integers.

```python
def xiaoorzhengjisuan(num1: float, num2: float, mode: str) -> float
```

num1: First operand
num2: Second operand
mode: Operation (+, -, *, or ** for exponentiation)
Returns: Result of the operation

fenjisuan
Performs arithmetic operations on fractions.

```python
def fenjisuan(num1: str, num2: str, mode: str) -> float
```

num1: First fraction
num2: Second fraction
mode: Operation (+, -, *, or ** for exponentiation)
Returns: Result of the operation as a fraction

bmi
Calculates BMI (Body Mass Index).

```python
def bmi(weight: int, height: int) -> float
```

weight: Weight in kg
height: Height in meters
Returns: BMI inde

#### Xiaogongju Module Documentation

##### quzheng

def quzheng(num: float, mode: int) -> int:

Function to round numbers.

Parameters:
num: The number to be rounded (float)
mode: Rounding mode (1 for floor, 2 for ceiling)
Returns: The rounded number
Raises: ValueError if mode is not 1 or 2

##### daorxiao

def daorxiao(args: str, mode: int) -> str:

Function to convert case of characters.

Parameters:
args: The string to be converted
mode: Conversion mode (1 for uppercase to lowercase, 2 for lowercase to uppercase)
Returns: The converted string
Raises: TypeError if mode is invalid

##### twonumbers_TheBiggestCommonfactor

def twonumbers_TheBiggestCommonfactor(num1: int, num2: int) -> int:

Function to find the greatest common factor of two numbers.

Parameters:
num1: The first number
num2: The second number
Returns: The greatest common factor of num1 and num2

##### twonumbers_TheMinimumCommonmultiple

def twonumbers_TheMinimumCommonmultiple(num1: int, num2: int) -> int:

Function to find the least common multiple of two numbers.

Parameters:
num1: The first number
num2: The second number
Returns: The least common multiple of num1 and num2

##### chouqusuiji

def chouqusuiji(num1: int, num2: int, mode: int, weishu: int) -> str:

Function to generate random values.

Parameters:
num1: The minimum value in the random number range
num2: The maximum value in the random number range
mode: 1 for random number, 2 for random string, 3 for random color code (#......)
weishu: The number of characters in the random string
Returns: The generated random value as a string

##### kaisamima

def kaisamima(arg: str, mode: int, n: int) -> str:

Function to encrypt or decrypt using Caesar cipher.

Parameters:
arg: The string to be encrypted or decrypted
mode: 1 for encryption, 2 for decryption
n: The shift value
Returns: The encrypted or decrypted string
Raises: ValueError if arg contains non-alphabetic characters, TypeError if mode is invalid

##### f

def f(a: float, n: int, m: int) -> int:

Function to round numbers based on specific rules.

Parameters:
a: The float number to be rounded
n: Lower bound for rounding
m: Upper bound for rounding
Returns: The rounded integer
Raises: ValueError if the input doesn't meet the specified rules

#### Math_cal Module Documentation

##### Description

This function performs various mathematical calculations based on the specified mode.

##### Definition

```python
def math_cal(mode:int,float1:float,float2:float)
```

##### Using the function

```python
s = math_cal(mode,float1,float2)
```

##### Parameters

mode (int): The calculation mode, ranging from 1 to 19. If the mode is outside this range, an exception will be raised.
float1 (float): First float parameter.
float2 (float): Second float parameter.

##### Usage Notes

The parameters float1 and float2 are used based on the selected mode.
If a parameter is not needed for a particular mode, use 0 as a placeholder.

##### Examples

Mode 3: math_cal(3, 5.2, 0)
Mode 4: math_cal(4, 0, 0)
Mode 1: math_cal(1, 5.92, -8)
Return Value
Returns the result of the calculation based on the selected mode.

##### Modes and Operations

Copysign
Cosine
Degrees
e (Euler's number)
π (Pi)
Tangent
Square root
Sine
Radians
Power
Modf
Logarithm
Ldexp
Not isnan
Not isinf
Factorial
Absolute value
Exp
Exceptions
Raises a TypeError if the mode is not within the valid range (1-19).

#### Tuxing_calculator Module Documentation

Function: tuxing

##### Description of the Function

Performs geometric calculations for various shapes.

##### Usage

This function performs various geometric calculations based on the specified shape and mode.

```python
tuxing(huida, mode, *args2)
```

###### Parameters input

huida: The shape to calculate (e.g., "长方体", "正方体", "正方形", etc.)
mode: The calculation mode (e.g., "体积", "面积", "表面积", etc.)
*args2: Additional arguments required for the calculation

###### Return Value

The result of the calculation, or:

0: Successful calculation
1: Invalid calculation mode
2: Invalid shape

###### Supported Shapes and Calculations

###### 长方体 (Cuboid)

体积 (Volume)
表面积 (Surface Area)
染色问题 (Coloring Problem)
棱长总和 (Sum of Edge Lengths)
容积 (Capacity)

###### 正方体 (Cube)

体积 (Volume)
表面积 (Surface Area)
染色问题 (Coloring Problem)
棱长总和 (Sum of Edge Lengths)
容积 (Capacity)

###### 正方形 (Square)

面积 (Area)
边长之和 (Sum of Side Lengths)
折纸盒问题 (Paper Box Folding Problem)

###### 长方形 (Rectangle)

面积 (Area)
周长 (Perimeter)
折纸盒问题 (Paper Box Folding Problem)

###### 平行四边形 (Parallelogram)

面积 (Area)
周长 (Perimeter)
折纸盒问题 (Paper Box Folding Problem)

###### 菱形 (Rhombus)

面积 (Area)
周长 (Perimeter)

###### 三角形 (Triangle)

面积 (Area)
周长 (Perimeter)

###### 梯形 (Trapezoid)

面积 (Area)
周长 (Perimeter)

###### 圆形 (Circle)

面积 (Area)
周长 (Perimeter)
方中圆 (Circle in Square)
圆中方 (Square in Circle)
#### UnitConvertChay Module Documention

##### Length Unit Conversion Functions
mm to Other Units

mmtocm(x: float) -> float: Converts millimeters to centimeters.
mmtodm(x: float) -> float: Converts millimeters to decimeters.
mmtom(x: float) -> float: Converts millimeters to meters.
mmtokm(x: float) -> float: Converts millimeters to kilometers.
cm to Other Units

cmtodm(x: float) -> float: Converts centimeters to decimeters.
cmtom(x: float) -> float: Converts centimeters to meters.
cmtokm(x: float) -> float: Converts centimeters to kilometers.
cmtomm(x: float) -> float: Converts centimeters to millimeters (reverse conversion for completeness).
dm to Other Units

dmtom(x: float) -> float: Converts decimeters to meters.
dmtokm(x: float) -> float: Converts decimeters to kilometers.
dmtomm(x: float) -> float: Converts decimeters to millimeters.
dmtocm(x: float) -> float: Converts decimeters to centimeters.
m to Other Units

mtokm(x: float) -> float: Converts meters to kilometers.
mtomm(x: float) -> float: Converts meters to millimeters.
mtocm(x: float) -> float: Converts meters to centimeters (same function name as mmtocm but different functionality).
mtodm(x: float) -> float: Converts meters to decimeters.
km to Other Units

kmtomm(x: float) -> float: Converts kilometers to millimeters.
kmtocm(x: float) -> float: Converts kilometers to centimeters.
kmtodm(x: float) -> float: Converts kilometers to decimeters.
kmtom(x: float) -> float: Converts kilometers to meters.
Micron and Nanometer Unit Conversions

μmtomm(x: float) -> float: Converts microns to millimeters.
mmtoμm(x: float) -> float: Converts millimeters to microns.
nmtoμm(x: float) -> float: Converts nanometers to microns.
μmtonm(x: float) -> float: Converts microns to nanometers.

##### Physical Quantity Conversion Functions
Density ρ

Function Definition: def ρ(V=0.0, m=0.0, g=9.8, h=0.0, p=0.0, Ffu=0.0) -> float:
Calculates density. Supports multiple calculation methods:
Given volume V and mass m, directly calculates density (ρ = m/V).
Given pressure p, gravitational acceleration g, and height h, calculates fluid density (ρ = p / (g * h)).
Given fluid buoyancy Ffu, gravitational acceleration g, and volume V, calculates density via buoyancy (ρ = Ffu / (g * V)).
Raises ValueError if parameters are invalid.
Mass m

Function Definition: def m(G=0.0, g=9.8, V=0.0, ρ=0.0) -> float:
Calculates mass. Supports multiple calculation methods:
Given gravity G and gravitational acceleration g, calculates mass (m = G/g).
Given volume V and density ρ, calculates mass (m = ρ * V).
Raises ValueError if parameters are invalid.
Volume V

Function Definition: def Vtiji(m=0.0, ρ=0.0, g=9.8, Ffu=0.0) -> float:
Calculates volume based on mass, density, or other physical quantities. Supports multiple methods:
Given mass m and density ρ, calculates volume (V = m/ρ).
May adjust logic for calculating volume via fluid buoyancy Ffu, gravitational acceleration g, and density ρ based on actual physics formulas.
Raises ValueError if parameters are invalid.
Velocity Vs

Function Definition: def Vsudu(Slu=0.0, t=0.0) -> float:
Calculates flow velocity. If given the distance traveled Slu and time t, calculates velocity (Vs = Slu/t). Raises ValueError if parameters are invalid.
Pressure p

Function Definition: def p(F=0.0, S=0.0, ρ=0.0, g=9.8, h=0.0) -> float:
Calculates pressure. Supports multiple calculation methods:
Given force F and area S, calculates pressure (p = F/S).
Given density ρ, height h, and gravitational acceleration g, calculates fluid pressure (p = ρ * g * h).
Raises ValueError if parameters are invalid.
Electrical Current I, Voltage U, Resistance R, and Power P

These functions (I, U, R, Pgong) are for calculating electrical current, voltage, resistance, and power respectively, based on Ohm's Law (U = I * R) and the power formula (Pgong = U * I). They accept different parameter combinations and calculate the corresponding physical quantity based on the provided parameters. Raises ValueError if parameters are invalid.