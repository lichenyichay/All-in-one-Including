# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/07/21 17:20
# @FILE:xiaogongju.py
# @Software:IDLE 3.9.6
import random,string
'''
函数名：quzheng
调用形式：quzheng(num,mode)
:param num 待取整的数字 float
:param mode 模式 1（向下取整）/2（向上取整） 不在选择范围内则抛出异常
:return 取整后的数字
作用：对数字进行取整
'''
def quzheng(num:float,mode:int) -> int:
    if mode == 1:
        return int(num)
    elif mode == 2:
        return int(num)+1
    else:
        raise ValueError("mode需在1、2两数之间，不得为其他数！")
'''
函数名：daorxiao
调用形式：daorxiao(args,mode)
:param args 待转换的字符串
:param mode 模式 1（大写转小写）/2（小写转大写） 不在选择范围内则抛出异常
:return zifu 转换后的字符串
作用：大小写转换
'''
def daorxiao(args:str,mode:int) ->str:
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
def twonumbers_TheBiggestCommonfactor(num1:int,num2:int) -> int:
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
def twonumbers_TheMinimumCommonmultiple(num1:int,num2:int) -> int:
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
def chouqusuiji(num1:int,num2:int,mode:int,weishu:int) -> str:
    if mode==1:
        return str(random.randint(num1,num2))
    elif mode==2:
        chars = string.ascii_letters + string.digits
        a=""
        for i in range(weishu):
            a += random.choice(chars)
        return a
    elif mode==3:
        return "#"+chouqusuiji(1,10,2,6)

'''
函数名：kaisamima
调用形式：a = kaisamima(arg,mode,n)
:param arg 需要加解密的字符串
:param mode 1:加密  2:解密
:param n 位移量
作用：加解密凯撒密码
'''
def kaisamima(arg:str,mode:int,n:int) -> str:
    a = []
    for i in range(97,123):
        a.append(chr(i))
    b = []
    for i in range(65,91):
        b.append(chr(i))
    a *= 2
    b *= 2
    c = ""
    if mode == 1:
        for i in range(len(arg)):
            if 65 <= ord(arg[i]) and ord(arg[i]) <= 90:
                c += b[b.index(arg[i])+n]
            elif 97 <= ord(arg[i]) and ord(arg[i]) <= 122:
                c += a[a.index(arg[i])+n]
            else:
                raise ValueError("arg应为只含字母的字符串")
        return c
    elif mode == 2:
        for i in range(len(arg)):
            if 65 <= ord(arg[i]) and ord(arg[i]) <= 90:
                c += b[b.index(arg[i])-n]
            elif 97 <= ord(arg[i]) and ord(arg[i]) <= 122:
                c += a[a.index(arg[i])-n]
            else:
                raise ValueError("arg应为只含字母的字符串")
        return c
    else:
        raise TypeError("TypeError:模式错误！")

def f(a:float,n:int,m:int) -> int:
    if 0<n and n<m and m <= 9:
        # 将浮点数 a 转换为整数部分和小数部分  
        integer_part = int(a)  
        decimal_part = round((a - integer_part) * 10, 2)  # 保留两位小数，以便比较  
        first_decimal_digit = int(decimal_part[1:])  # 提取小数部分的第一位  
    
        # 根据规则进行判断  
        if first_decimal_digit <= n:  
            return integer_part  
        elif first_decimal_digit >= m:  
            return integer_part + 1  
        else:  
            # 当 m-n > 1，并且小数部分第一位在 n 和 m 之间时  
            if integer_part % 2 == 1:  
                return integer_part + 1  
            else:  
                return integer_part
    else:
        raise ValueError("不符合规则")