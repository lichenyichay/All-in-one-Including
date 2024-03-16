# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:29
# @FILE:calculator.py
# @Software:IDLE 3.9.6
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
调用形式：yiyuanerci(float1,float2,float3)
:param float1 系数1
:param float2 系数2
:param float3 系数3
:return x1 实数根1
:return x2 实数根2
作用：求解一元二次方程
'''
def yiyuanerci(float1,float2,float3):
    dlt = float2 ** 2 - 4 * float1 * float3
    x1 = (-float2 + math.sqrt(dlt)) / 2 / float1
    x2 = (-float2 - math.sqrt(dlt)) / 2 / float1
    return f"x1 = {x1},x2 = {x2}"
