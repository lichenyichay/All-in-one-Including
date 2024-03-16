# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:07
# @FILE:xiaogongju.py
# @Software:IDLE 3.9.6
import random,string

'''
函数名：daorxiao
调用形式：daorxiao(args,mode)
:param args 待转换的字符串
:param mode 模式 1（大写转小写）/2（小写转大写） 不在选择范围内则抛出异常
:return 0
作用：大小写转换
'''
def daorxiao(args,mode):
    zongzifu = []
    zifu2=""
    gongneng1 = mode
    if gongneng1 == 1:
        for i in args:
            if ord(i)>=65 and ord(i)<=90:
                zifu = i
                zifu1 = chr(ord(zifu) + 32)
                zongzifu.append(zifu1)
            else:
                zongzifu.append(i)                
        for i in zongzifu:
            zifu2 += i
        return zifu2
    elif gongneng1 == 2:
        for i in args:
            if ord(i)>=97 and ord(i)<=122:
                zifu = i
                zifu1 = chr(ord(zifu) - 32)
                zongzifu.append(zifu1)
            else:
                zongzifu.append(i)
        for i in zongzifu:
            zifu2 += i
        return zifu2
    else:
        raise TypeError("TypeError:模式错误！")

'''
函数名：twonumbers_TheBiggestCommonfactor
调用形式：a = twonumbers_TheBiggestCommonfactor(num1,num2)
:param num1 第一个数
:param num2 第二个数
:return num1和num2的最大公因数
作用：求最大公因数
'''
def twonumbers_TheBiggestCommonfactor(num1,num2):
    lst = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            lst.append(i)
    return max(lst)

'''
函数名：twonumbers_TheMinimumCommonmultiple
调用形式：a = twonumbers_TheMinimumCommonmultiple(num1,num2)
:param num1 第一个数
:param num2 第二个数
:return num1和num2的最小公倍数
作用：求最小公倍数
'''
def twonumbers_TheMinimumCommonmultiple(num1,num2):
    lst = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            lst.append(i)
    return num1 * num2 // max(lst)

'''
函数名：chouqusuiji
调用形式：a = chouqusuiji(num1,num2,mode,weishu)
:param num1 抽取随机数中区间的最小值
:param num2 抽取随机数中区间的最大值
:param mode 1:随机数   2:随机字符串    3:随机颜色代码（#......）
:param weishu 在随机字符串中字符串的位数
作用：抽取随机
'''
def chouqusuiji(num1,num2,mode,weishu):
    if mode==1:
        return random.randint(num1,num2)
    elif mode==2:
        chars = string.ascii_letters + string.digits
        a=""
        for i in range(weishu):
            a += random.choice(chars)
        return a
    elif mode==3:
        return "#"+chouqusuiji(1,10,2,6)
