# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/08/31 08:05
# @FILE:calculator.py
# @Software:Visual Studio Code
import math,itertools,random,re
from cmath import sqrt as csqrt
from sympy import *
from fractions import *

'''
函数名：FtemporCtemp
调用形式：a = FtemporCtemp(mode,FtemporCtemp)
:param mode 模式 ℃to℉（摄氏度转为华氏度）/℉to℃（华氏度转为摄氏度） 模式不在选择范围内会抛出异常
:return 转换后的温度（不带单位）
作用：华氏度与摄氏度转换
'''
def FtemporCtemp(mode:str,FtemporCtemp:float) -> float:
    if mode == "℃to℉":
        return FtemporCtemp*9/5+32
    elif mode == "℉to℃":
        return (FtemporCtemp-32)*5/9
    else:
        raise TypeError("TypeError:模式错误！")

'''
函数名：duihuan
调用形式：a = duihuan(mode,money)
:param mode 模式 1~16 对应不同的货币转换，汇率也不同 模式不在选择范围内会抛出异常
:param money 要兑换的金额（以模式箭头前的货币单位作为1单位量）
:return 转换后的货币数量
作用：货币交换
'''
def duihuan(mode:int,money:float) -> float:
    if mode == 1:
        return 0.14 * money #CNY to USD
    elif mode == 2:
        return 20.71 * money #CNY to JPY
    elif mode == 3:
        return 7.2 * money #USD to CNY
    elif mode == 4:
        return 149.02 * money #USD to JPY
    elif mode == 5:
        return 0.048 * money #JPY to CNY
    elif mode == 6:
        return 0.0067 * money #JPY to USD
    elif mode == 7:
        return 0.89 * money #MOP to CNY
    elif mode == 8:
        return 1.12 * money #CNY to MOP
    elif mode == 9:
        return 0.92 * money #HKD to CNY
    elif mode == 10:
        return 1.09 * money #CNY to HKD
    elif mode == 11:
        return 0.23 * money #TWD to CNY
    elif mode == 12:
        return 4.40 * money #CNY to TWD
    elif mode == 13:
        return 9.17 * money #GBP to CNY
    elif mode == 14:
        return 0.11 * money #CNY to GBP
    elif mode == 15:
        return 7.84 * money #EUR to CNY
    elif mode == 16:
        return 0.13 * money #CNY to EUR
    else:
        raise TypeError("TypeError:模式错误！")
'''
函数名：yiyuanerci
调用形式：a = yiyuanerci(float1,float2,float3)
:param fangcheng 方程 类型：str 要求：为ax+b=0 or ax^2+bx+c=0 or ax^3+bx^2+cx+d=0的形式
:param mode 方程的最高次数 类型：int 为1、2、3中的一个
:return gen 方程的解 类型：tuple
作用：求解一元一、二、三次方程
'''
def yiyuannci(fangcheng:str,mode:int) -> tuple:
    if mode == 1:
        l = fangcheng.split("=")
        l = l[0].split("+")
        for i in range(len(l)-1):
            l[i] = int(l[i][0])
        l[-1] = int(l[-1])
        return (-(l[1]/l[0]))
    elif mode == 2:
        match = re.match(r'(\d+)x\^2\s*([-+])\s*(\d*)x\s*([-+])\s*(\d+)\s*=\s*0', fangcheng)
        
        # 提取系数
        a = int(match.group(1))
        sign_b = match.group(2)
        b_str = match.group(3)
        sign_c = match.group(4)
        c = int(match.group(5))

        # 处理b和c的符号
        b = int(b_str) if sign_b == '+' else -int(b_str)
        c = int(c) if sign_c == '+' else -int(c)

        # 计算判别式
        delta = b**2 - 4*a*c

        # 根据判别式的值求解方程
        if delta >= 0:
            # 实数解
            root1 = (-b + math.sqrt(delta)) / (2*a)
            root2 = (-b - math.sqrt(delta)) / (2*a)
            return (root1, root2)
        else:
            # 复数解
            real_part = -b / (2*a)
            imag_part = csqrt(-delta) / (2*a)
            return (complex(real_part, imag_part.real), complex(real_part, -imag_part.real))

    elif mode == 3:
        fangcheng = fangcheng.replace("^","**")
        fangcheng = fangcheng.replace("=0","")
        # 定义符号
        x = symbols('x')
        
        # 使用sympify将字符串转换为表达式
        equation_expr = sympify(fangcheng)
        
        # 创建等式对象
        eq = Eq(equation_expr, 0)
        
        # 解方程
        solutions = solve(eq, x)
        
        return tuple(solutions)
    else:
        raise ValueError("param \"mode\" is >0 and <= 3 and \"mode\" is type int! mode参数需为1,2,3中的一个")

'''
函数名：fanzhuanzifuchuan
调用形式：a = fanzhuanzifuchuan(s)
:param s 需要反转的字符串 类型：str
:return s1 翻转后的字符串 类型：str
作用：反转字符串
'''

def fanzhuanzifuchuan(s:str) -> str:
    s=str(s)
    s1=""
    for i in range(len(s)-1,-1,-1):
        j=0
        s1 += s[i]
        j+=1
    return s1

'''
函数名：isparam
调用形式：a = isparam(d)
:param d  类型：int
:return x 是否为质数 类型：bool(True or False)
作用：判断质数
'''
def isparam(d:int) -> bool:
    if d <= 1:
        return False
    for i in range(2,math.sqrt(d)+1):
        if d%i==0:
            return False
    return True

'''
函数名：ishuiwenshu
调用形式：a = ishuiwenshu(s)
:param d  类型：int
:return x 是否为回文数 类型：bool(True or False)
作用：判断回文数
'''
def ishuiwenshu(d:int) -> bool:
    d1=int(fanzhuanzifuchuan(str(d)))
    if d1==d:
        return True
    else:
        return False

'''
函数名：ishuiwenzhishu
调用形式：a = ishuiwenzhishu(d)
:param d  类型：int
:return x 是否为回文质数 类型：bool(True or False)
作用：判断回文质数
'''
def ishuiwenzhishu(d:int) -> bool:
    d1=int(fanzhuanzifuchuan(str(d)))
    if d1==d:
        if isparam(d):
            return True
        else:
            return False
    else:
        return False

'''
函数名：fab
调用形式：a = fab(d)
:param x  类型：int
:return a[x-1] 斐波那契数列的第x位
作用：求斐波那契数列的第x位
'''
def fab(x:int) -> int:
    a=[1,1]
    for i in range(2,x):
        a.append(a[i-1]+a[i-2])
    for i in range(x):
        print(a[i]," ")
    return a[x-1]

'''
函数名：isfab
调用形式：a = isfab(d)
:param d  类型：int(0<d<=12586269025)
:return x 是否为斐波那契数列中的一个数 类型：bool(True or False)
作用：是否为斐波那契数列中的一个数
'''
def isfab(x:int) -> bool:
    a=[1,1]
    for i in range(2,int(math.sqrt(x+2))):
        a.append(a[i-1]+a[i-2])
    if x not in a:
        return False
    else:
        return True

'''
函数名：isfabparam
调用形式：a = isfabparam(d)
:param d  类型：int(0<d<=12586269025)
:return x 是否是斐波那契质数 类型：bool(True or False)
作用：是否为斐波那契数列中的一个数且为一个质数
'''
def isfabparam(x:int) -> bool:
    if isfab(x) and isparam(x):
        return True
    else:
        return False

'''
函数名：isfabhuiwenshu
调用形式：a = isfabhuiwenshu(d)
:param d  类型：int(0<d<=12586269025)
:return x 是否是斐波那契回文数 类型：bool(True or False)
作用：是否为斐波那契数列中的一个数且为一个回文数
'''
def isfabhuiwenshu(x:int) -> bool:
    if isfab(x) and ishuiwenshu(x):
        return True
    else:
        return False

'''
函数名：isfabhuiwenzhishu
调用形式：a = isfabhuiwenzhishu(d)
:param d  类型：int(0<d<=12586269025)
:return x 是否是斐波那契回文质数 类型：bool(True or False)
作用：是否为斐波那契数列中的一个数且为一个回文质数
'''
def isfabhuiwenzhishu(x:int) -> bool:
    if isfab(x) and ishuiwenzhishu(x):
        return True
    else:
        return False

'''
函数名：isleapyear
调用形式：a = isleapyear(d)
:param d  类型：int
:return x 对应年份是否是闰年 类型：bool(True or False)
作用：判断闰年
'''   
def isleapyear(x) -> bool:
    if x%4==0:
        if x%100==0:
            if x%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
函数名：tribonacci
调用形式：a = tribonacci(d)
:param x  类型：int
:return a[x-1] 泰波那契序列的第x位
作用：求泰波那契序列的第x位
'''
def tribonacci(n:int) -> int:
    d=[0,1,1]
    if n<=2:
        return d[n]
    else:
        for i in range(3,n+1):
            d.append(d[i-3]+d[i-2]+d[i-1])
        return d[n]

'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
函数名：istribonacci
调用形式：a = istribonacci(d)
:param x  类型：int
:return x 是否属于泰波那契序列中的一个数（True or False）
作用：判断是否属于泰波那契序列中的一个数
'''
def istribonacci(n:int) -> bool:
    a=[0,1,1]
    if n>=10000:
        for i in range(3,int(math.sqrt(n+3))):
            a.append(a[i-1]+a[i-2]+a[i-3])
    elif n>=1389537:
        for i in range(3,int(math.sqrt(int(math.sqrt(n+3))))):
            a.append(a[i-1]+a[i-2]+a[i-3])
    else:
        for i in range(3,int((n+3))):
            a.append(a[i-1]+a[i-2]+a[i-3])
    if n not in a:
        return False
    else:
        return True

'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
函数名：istribonaccihuiwenshu
调用形式：a = istribonaccihuiwenshu(d)
:param x  类型：int
:return x 是否是泰波那契序列回文数（True or False）
作用：判断泰波那契序列回文数
'''
def istribonaccihuiwenshu(n:int) -> bool:
    if istribonacci(n) and ishuiwenshu(n):
        return True
    else:
        return False

'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
函数名：istribonaccihuiwenshuparam
调用形式：a = istribonaccihuiwenshuparam(d)
:param x  类型：int
:return x 是否是泰波那契序列回文质数（True or False）
作用：判断泰波那契序列回文质数
'''
def istribonaccihuiwenshuparam(n:int) -> bool:
    if isfabhuiwenshu(n) and isparam(n):
        return True
    else:
        return False

'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
函数名：istribonacciparam
调用形式：a = istribonacciparam(d)
:param x  类型：int
:return x 是否是泰波那契序列质数（True or False）
作用：判断泰波那契序列质数
'''
def istribonacciparam(n:int) -> bool:
    if istribonacci(n) and isparam(n):
        return True
    else:
        return False

'''
函数名：iswanquanpingfangshu
调用形式：a = iswanquanpingfangshu(d)
:param d  类型：int
:return x d是否是完全平方数 类型：bool(True or False)
作用：判断完全平方数
'''   
def iswanquanpingfangshu(num:int) -> bool:
    a=math.sqrt(num)
    if int(a)==a:
        return True
    else:
        return False

'''
函数名：wanquanpingfangshu
调用形式：a = wanquanpingfangshu(d)
:param d  类型：int
:return x 第d个完全平方数
作用：求第d个完全平方数
'''
def wanquanpingfangshu(num:int) -> int:
    return num**2

'''
函数名：isfabwanquanpingfangshu
调用形式：a = isfabwanquanpingfangshu(d)
:param d  类型：int
:return x d是否是斐波那契完全平方数 类型：bool(True or False)
作用：判断斐波那契完全平方数
'''  
def isfabwanquanpingfangshu(num:int) -> bool:
    return isfab(num) and iswanquanpingfangshu(num)

'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
函数名：istribonacciwanquanpingfangshu
调用形式：a = istribonacciwanquanpingfangshu(d)
:param x  类型：int
:return x 是否是泰波那契序列完全平方数（True or False）
作用：判断泰波那契序列完全平方数
'''
def istribonacciwanquanpingfangshu(num:int) -> bool:
    return istribonacci(num) and iswanquanpingfangshu(num)

'''
函数名：jinzhizhuanhuan
调用形式：a =  jinzhizhuanhuan(a,b,c)
:param a c的进制数 (2<=a<=36)
:param b 结果的进制数 (2<=a<=36)
:param c 需转换的数 无需前缀且需符合a进制规则
:return z 结果
作用：进行进制转换
'''
def jinzhizhuanhuan(a:int,b:int,c:str) -> str:
    if a == b:
        return c
    elif a == 10  and b != 10:
        num = int(c)  
        result = ""  
        while num > 0:  
            remainder = num % b  
            if remainder >= 10:  
                result += chr(remainder - 10 + ord('A'))  
            else:  
                result += str(remainder)  
            num //= b
        return result[::-1] 
    elif a != 10 and b == 10:
        ans=0
        tmp=1
        n=len(c)
        for i in range(n-1,-1,-1):
            base = 0
            if c[i] >= 'A' and c[i] <= 'Z':
                base = c[i]-'A'+10
            else:
                base = ord(c[i])-ord('0')
            ans += tmp*base
            tmp *= a
        return str(ans)

    else:
        return jinzhizhuanhuan(10,b,jinzhizhuanhuan(a,10,c))
    
'''
函数名：factorization
调用形式：a = facforization(num)
:param num 需因式分解的自然数
:return factor 因式分解的结果
作用：对一个数进行因式分解
'''
def factorization(num:int) -> list[int]:
    factor = []
    while num > 1:
        for i in range(num - 1):
            k = i + 2
            if num % k == 0:
                factor.append(k)
                num = int(num / k)
                break
    return factor

'''
函数名：mima
调用形式：a = mima(num,n)
:param num 提取密码的数字
:param n 密码位数
:return z 结果
作用：对一个数提取密码
'''
def mima(num:int,n:int) -> int:
    factor = factorization(num)
    y = []
    if n <= len(str(max(factor))):
        for i in itertools.combinations(factor,n):
            y.append(int(''.join('%d'%o for o in i)))
        return random.choice(y)
    else:
        return 0
def xiaoorfen(num:str,mode:int) -> str:
    if mode == 1: #小化分
        return Fraction(float(num)).limit_denominator()
    elif mode == 2: #分化小
        return eval(num)
    else:
        raise ValueError("mode Error!")
'''
函数名：xiaoorzhengjisuan
调用形式：a = xiaoorzhengjisuan(num1,num2,mode)
:param num1 运算数字1
:param num2 运算数字2
:param mode 模式（运算符+-*/**（乘方）中的一个）
:return z 结果
作用：小数、整数计算
'''
def xiaoorzhengjisuan(num1:float,num2:float,mode:str) -> float:
    return eval(str(num1)+mode+str(num2))

'''
函数名：fenjisuan
调用形式：a = fenjisuan(num1,num2,mode)
:param num1 运算数字1
:param num2 运算数字2
:param mode 模式（运算符+-*/**（乘方）中的一个）
:return z 结果
作用：分数计算
'''
def fenjisuan(num1:str,num2:str,mode:str) -> float:
    return Fraction(eval(str(xiaoorfen(num1,2))+mode+str(xiaoorfen(num2,2)))).limit_denominator()

'''
函数名：bmi
调用形式：a = bmi(weight,height)
:param weight 体重（KG）
:param height 身高（m）
:return BMI BMI指数
作用：计算BMI指数
'''
def bmi(weight:int,height:int) -> float:
    return weight/(height**2)