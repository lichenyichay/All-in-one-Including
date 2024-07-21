# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/5/3 23:25
# @FILE:lotterytickets.py
# @version:4.0.0
# @Software:Visual Studio Code
import random

numdict = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",0:"零"} #个位数的字典
digitdict = {1:"十",2:"百",3:"千",4:"万"} #位称的字典
 
 
def maxdigit(number:int,count:int) -> tuple:
    num = number//10 #整除是//
    if num != 0:
        return maxdigit(num,count+1) #加上return才能进行递归
    else:
        digit_num = number%10 #digit_num是最高位上的数字
        return count,digit_num #count记录最高位

def No2Cn(number:int) -> str:
    max_digit,digit_num = maxdigit(number,0)
 
    temp = number
    num_list = [] #储存各位数字（最高位的数字也可以通过num_list[-1]得到
    while temp > 0:
        position = temp%10
        temp //= 10 #整除是//
        num_list.append(position)
 
    chinese = ""
    if max_digit == 0: #个位数
        chinese = numdict[number]
    elif max_digit == 1: #十位数
        if digit_num == 1: #若十位上是1，则称为“十几”，而一般不称为“一十几”（与超过2位的数分开讨论的原因）
            chinese = "十"+numdict[num_list[0]]
        else:
            chinese = numdict[num_list[-1]]+"十"+numdict[num_list[0]]
    elif max_digit > 1: #超过2位的数
        while max_digit > 0:
            if num_list[-1] != 0: #若当前位上数字不为0，则加上位称
                chinese += numdict[num_list[-1]]+digitdict[max_digit]
                max_digit -= 1
                num_list.pop(-1)
            else: #若当前位上数字为0，则不加上位称
                chinese += numdict[num_list[-1]]
                max_digit -= 1
                num_list.pop(-1)
        chinese += numdict[num_list[-1]]
        
    while chinese.endswith("零") and len(chinese) > 1: #个位数如果为0，不读出
        chinese = chinese[:-1]
    if chinese.count("零") > 1: #中文数字中最多只有1个零
        count_0 = chinese.count("零")
        chinese = chinese.replace("零","",count_0-1)
    return chinese

'''
函数名：lotterytickets
调用形式： a = lotterytickets(user,mubiao,mode)
:param user 你的彩票号（以空格隔开）（兑奖）
:param mubiao 开奖号（以空格隔开）（兑奖）
:param mode 模式，具体见下
:return 结果
兑奖：对应号码是否相同
作用：彩票一体机
'''
def lotterytickets(user:str,mubiao:str,mode:int) -> str:
    if mode == 1:
        # 大乐透
        if user != "" and mubiao != "":
            # 兑奖
            x = 0
            for i in range(7):
                if user.split()[i] == mubiao.split()[i]:
                    print(user.split()[i])
                    x += 1
            return No2Cn(8 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(5):
                s += str(random.randint(1,35))
                s += " "
            for i in range(2):
                s += str(random.randint(1,12))
                s += " "
            return s
    elif mode == 2:
        # 双色球
        if user != "" and mubiao != "":
            # 兑奖
            x = 0
            for i in range(7):
                if user.split()[i] == mubiao.split()[i]:
                    print(user.split()[i])
                    x += 1
            return No2Cn(8 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(6):
                s += str(random.randint(1,33))
                s += " "
            s += str(random.randint(1,16))
            return s
    elif mode == 3:
        # 排列3/3D
        if user != "" and mubiao != "":
            # 兑奖
            x = 0
            for i in range(3):
                if user.split()[i] == mubiao.split()[i]:
                    print(user.split()[i])
                    x += 1
            return No2Cn(4 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(3):
                s += str(random.randint(0,9))
                s += " "
            return s
    elif mode == 4:
        # 排列5
        if user != "" and mubiao != "":
            # 兑奖
            x = 0
            for i in range(5):
                if user.split()[i] == mubiao.split()[i]:
                    print(user.split()[i])
                    x += 1
            return No2Cn(6 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(5):
                s += str(random.randint(0,9))
                s += " "
            return s
    elif mode == 5:
        # 七星彩
        if user != "" and mubiao != "":
            # 兑奖
            x = 0
            for i in range(7):
                if user.split()[i] == mubiao.split()[i]:
                    print(user.split()[i])
                    x += 1
            return No2Cn(8 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(6):
                s += str(random.randint(0,9))
                s += " "
            s += random.randint(1,14)
            return s
    elif mode == 6:
        # 七乐彩
        if user != "" and mubiao != "":
            # 兑奖
            x = 0
            for i in range(7):
                if user.split()[i] == mubiao.split()[i]:
                    print(user.split()[i])
                    x += 1
            return No2Cn(8 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(7):
                s += str(random.randint(1,30))
                s += " "
            return s
    else:
        raise TypeError("模式错误！")