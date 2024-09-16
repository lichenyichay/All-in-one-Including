# Allinone Readme in English/英文版Allinone使用说明

Using the Allinoneincluding library, you can use

```py
from Allinoneincluding import *
```

or

```py
import Allinoneincluding as aioi #When you didn't install aioi library
```

codes.

This project has the same functionality as the All-in-one-chay library. However,due to configuration issues with the library files, the original library cannot be used normally. Please download the Allinoneincluding library. Thank you!

## Module Index

Line 33 Allinone Main Module Documentation

Line 39 Calculator Module Documentation

Line 344 Xiaogongju Module Documentation

Line 431 Math_calculator Module Documentation

Line 493 Tuxing_calculator Module Documentation

Line 577 Inequaliity Module Documentation

## Allinone Main Module Documentation

Allinone.py
Main module for the Allinone Function.
mode:depending on your choice, you can choose the function you want to use.(such as you choose Ftemp or Ctemp you should incoming mode param in "℃to℉" or "℉to℃")

## Calculator Module Documentation

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

## Xiaogongju Module Documentation

### quzheng

def quzheng(num: float, mode: int) -> int:

Function to round numbers.

Parameters:
num: The number to be rounded (float)
mode: Rounding mode (1 for floor, 2 for ceiling)
Returns: The rounded number
Raises: ValueError if mode is not 1 or 2

### daorxiao

def daorxiao(args: str, mode: int) -> str:

Function to convert case of characters.

Parameters:
args: The string to be converted
mode: Conversion mode (1 for uppercase to lowercase, 2 for lowercase to uppercase)
Returns: The converted string
Raises: TypeError if mode is invalid

### twonumbers_TheBiggestCommonfactor

def twonumbers_TheBiggestCommonfactor(num1: int, num2: int) -> int:

Function to find the greatest common factor of two numbers.

Parameters:
num1: The first number
num2: The second number
Returns: The greatest common factor of num1 and num2

### twonumbers_TheMinimumCommonmultiple

def twonumbers_TheMinimumCommonmultiple(num1: int, num2: int) -> int:

Function to find the least common multiple of two numbers.

Parameters:
num1: The first number
num2: The second number
Returns: The least common multiple of num1 and num2

### chouqusuiji

def chouqusuiji(num1: int, num2: int, mode: int, weishu: int) -> str:

Function to generate random values.

Parameters:
num1: The minimum value in the random number range
num2: The maximum value in the random number range
mode: 1 for random number, 2 for random string, 3 for random color code (#......)
weishu: The number of characters in the random string
Returns: The generated random value as a string

### kaisamima

def kaisamima(arg: str, mode: int, n: int) -> str:

Function to encrypt or decrypt using Caesar cipher.

Parameters:
arg: The string to be encrypted or decrypted
mode: 1 for encryption, 2 for decryption
n: The shift value
Returns: The encrypted or decrypted string
Raises: ValueError if arg contains non-alphabetic characters, TypeError if mode is invalid

### f

def f(a: float, n: int, m: int) -> int:

Function to round numbers based on specific rules.

Parameters:
a: The float number to be rounded
n: Lower bound for rounding
m: Upper bound for rounding
Returns: The rounded integer
Raises: ValueError if the input doesn't meet the specified rules

## Math_cal Module Documentation

### Description

This function performs various mathematical calculations based on the specified mode.

### Definition

```python
def math_cal(mode:int,float1:float,float2:float)
```

### Using the function

```python
s = math_cal(mode,float1,float2)
```

### Parameters

mode (int): The calculation mode, ranging from 1 to 19. If the mode is outside this range, an exception will be raised.
float1 (float): First float parameter.
float2 (float): Second float parameter.

### Usage Notes

The parameters float1 and float2 are used based on the selected mode.
If a parameter is not needed for a particular mode, use 0 as a placeholder.

### Examples

Mode 3: math_cal(3, 5.2, 0)
Mode 4: math_cal(4, 0, 0)
Mode 1: math_cal(1, 5.92, -8)
Return Value
Returns the result of the calculation based on the selected mode.

### Modes and Operations

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

## Tuxing_calculator Module Documentation

Function: tuxing

### Description of the Function

Performs geometric calculations for various shapes.

### Usage

This function performs various geometric calculations based on the specified shape and mode.

```python
tuxing(huida, mode, *args2)
```

#### Parameters input

huida: The shape to calculate (e.g., "长方体", "正方体", "正方形", etc.)
mode: The calculation mode (e.g., "体积", "面积", "表面积", etc.)
*args2: Additional arguments required for the calculation

#### Return Value

The result of the calculation, or:

0: Successful calculation
1: Invalid calculation mode
2: Invalid shape

#### Supported Shapes and Calculations

##### 长方体 (Cuboid)

体积 (Volume)
表面积 (Surface Area)
染色问题 (Coloring Problem)
棱长总和 (Sum of Edge Lengths)
容积 (Capacity)

##### 正方体 (Cube)

体积 (Volume)
表面积 (Surface Area)
染色问题 (Coloring Problem)
棱长总和 (Sum of Edge Lengths)
容积 (Capacity)

##### 正方形 (Square)

面积 (Area)
边长之和 (Sum of Side Lengths)
折纸盒问题 (Paper Box Folding Problem)

##### 长方形 (Rectangle)

面积 (Area)
周长 (Perimeter)
折纸盒问题 (Paper Box Folding Problem)

##### 平行四边形 (Parallelogram)

面积 (Area)
周长 (Perimeter)
折纸盒问题 (Paper Box Folding Problem)

##### 菱形 (Rhombus)

面积 (Area)
周长 (Perimeter)

##### 三角形 (Triangle)

面积 (Area)
周长 (Perimeter)

##### 梯形 (Trapezoid)

面积 (Area)
周长 (Perimeter)

##### 圆形 (Circle)

面积 (Area)
周长 (Perimeter)
方中圆 (Circle in Square)
圆中方 (Square in Circle)

## inequality Module Documentation

### Function Overview

This code provides two main functionalities: suijiine for generating random inequality expressions based on a specified level of difficulty (i.e., the number of operations), and solveine for solving linear inequality expressions and returning the solution set.

### Function suijiine(dif: int) -> str

Functionality: Generates a random inequality expression based on the given difficulty level (dif).
Parameters:
dif (int): The difficulty level of the inequality expression, which determines the number of operations.
Returns:
str: A randomly generated inequality expression string.

### Function solveine(s: str) -> str

Functionality: Solves a given linear inequality expression and returns the solution set.
Parameters:
s (str): The linear inequality expression as a string.
Returns:
str: The solution set of the inequality expression.

### Notes

It assumes the input inequality is linear and has only one unknown x.
If a (the coefficient of x on the left side of the inequality) is 0, it returns "All real numbers" or "No solution" depending on the value of b.
Uses fractions.Fraction to handle fractions, ensuring that the solution set is returned in fractional form if possible.
