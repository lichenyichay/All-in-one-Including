# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/3/29 22:55
# @FILE:calculator.py
# @Software:Visual Studio Code
import math
'''
函数名：FtemporCtemp
调用形式：a = FtemporCtemp(mode,FtemporCtemp)
:param mode 模式 ℃to℉（摄氏度转为华氏度）/℉to℃（华氏度转为摄氏度） 模式不在选择范围内会抛出异常
:return 转换后的温度（不带单位）
作用：华氏度与摄氏度转换
'''
def FtemporCtemp(mode,FtemporCtemp):
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
def duihuan(mode,money):
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
:param float1 系数1 类型：float
:param float2 系数2 类型：float
:param float3 系数3 类型：float
:return x1 实数根1 类型：float
:return x2 实数根2 类型：float
作用：求解一元二次方程
'''
def yiyuanerci(float1:float,float2:float,float3:float):
    dlt = float2 ** 2 - 4 * float1 * float3
    x1 = (-float2 + math.sqrt(dlt)) / 2 / float1
    x2 = (-float2 - math.sqrt(dlt)) / 2 / float1
    return f"x1 = {x1},x2 = {x2}"

'''
函数名：fanzhuanzifuchuan
调用形式：a = fanzhuanzifuchuan(s)
:param s 需要反转的字符串 类型：str
:return s1 翻转后的字符串 类型：str
作用：反转字符串
'''

def fanzhuanzifuchuan(s:str):
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
def isparam(d:int):
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
def ishuiwenshu(d:int):
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
def ishuiwenzhishu(d:int):
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
def fab(x):
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
def isfab(x):
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
def isfabparam(x:int):
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
def isfabhuiwenshu(x:int):
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
def isfabhuiwenzhishu(x:int):
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
def isleapyear(x):
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