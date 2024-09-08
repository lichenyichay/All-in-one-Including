# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/5/3 23:25
# @FILE:Allinone.py
# @version:2.4.8
# @Software:Visual Studio Code
import random
import numberandchinese as ntoc
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
            return ntoc.No2Cn(8 - x)+"等奖"
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
            return ntoc.No2Cn(8 - x)+"等奖"
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
            return ntoc.No2Cn(4 - x)+"等奖"
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
            return ntoc.No2Cn(6 - x)+"等奖"
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
            return ntoc.No2Cn(8 - x)+"等奖"
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
            return ntoc.No2Cn(8 - x)+"等奖"
        else:
            # 随机
            s = ""
            for i in range(7):
                s += str(random.randint(1,30))
                s += " "
            return s
    else:
        raise TypeError("模式错误！")