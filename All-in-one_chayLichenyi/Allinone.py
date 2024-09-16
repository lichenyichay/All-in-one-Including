# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/08/31 16:29
# @FILE:Allinone.py
# @version:4.0.2
# @Software:Visual Studio Code
import random
from .calculator import *
from .erfenchazhao_py import *
from .math_cal_py import *
from .student_py import *
from .tuxing_cal import *
from .xiaogongju import *
import lotterytickets as lt
import numberandchinese as ntoc
import inequalitychay as ic
def allinone(fuwu,mode,*args):
    """
    :param fuwu 需要服务的功能
    :param mode 部分功能需要的模式（详见Github中All-in-one2.4.0分支的Wiki页）
    :param *args 可变参数，表示需要传入的参数，建议用元组或列表类型，具体所需类型见README.MD
    :return: 0：正常，1：不正常，其他返回值表示功能的结果

    功能（按代码顺序排序，不分先后）：大小写互换、抽取随机数、求最小公倍数、求最大公倍数、图形计算器、小学学生信息管理系统、二分查找、求余、向下取整、向上取整、多个数求和、多个数求差、多个数求积、判断闰年、判断是否为质数、整数、小数计算（加减乘除）、分数计算（加减乘除）......（具体见Github All-in-one2.4.0分支Readme.md文件）
    """
    if fuwu == "大小写互换":
        return daorxiao(args[0],mode)
    elif fuwu == "抽取随机":
        return chouqusuiji(args[0],args[1],mode,args[2])
    elif fuwu == "求最小公倍数":
        num1 = args[0]
        num2 = args[1]
        for i1 in range(max(num1, num2), num1 * num2 + 1):
            if i1 % num1 == 0 and i1 % num2 == 0:
                return i1
    elif fuwu == "求最大公因数":
        num1 = args[0]
        num2 = args[1]
        return twonumbers_TheBiggestCommonfactor(num1,num2)
    # elif fuwu == "快速排列":
    #     kuaisupailie()
    elif fuwu == "求解方程":
        return yiyuannci(args[0],args[1])
    elif fuwu=="反转字符串":
        return fanzhuanzifuchuan(args[0])
    elif fuwu=="判断质数":
        return isparam(args[0])
    elif fuwu=="判断回文数":
        return ishuiwenshu(args[0])
    elif fuwu=="判断回文质数":
        return ishuiwenzhishu(args[0])
    elif fuwu=="求斐波那契数列的第n项":
        return fab(args[0])
    elif fuwu=="判断斐波那契数":
        return isfab(args[0])
    elif fuwu=="判断斐波那契回文质数":
        return isfabhuiwenzhishu(args[0])
    elif fuwu=="判断斐波那契回文数":
        return isfabhuiwenshu(args[0])
    elif fuwu=="判断斐波那契质数":
        return isfabparam(args[0])
    elif fuwu=="求泰波那契序列的第n项":
        return tribonacci(args[0])
    elif fuwu=="判断泰波那契数":
        return istribonacci(args[0])
    elif fuwu=="判断泰波那契回文质数":
        return istribonaccihuiwenshuparam(args[0])
    elif fuwu=="判断泰波那契回文数":
        return istribonaccihuiwenshu(args[0])
    elif fuwu=="判断泰波那契质数":
        return istribonacciparam(args[0])
    elif fuwu=="求第n个完全平方数":
        return wanquanpingfangshu(args[0])
    elif fuwu=="判断完全平方数":
        return iswanquanpingfangshu(args[0])
    elif fuwu=="判断斐波那契完全平方数":
        return isfabwanquanpingfangshu(args[0])
    elif fuwu=="判断泰波那契序列完全平方数":
        return istribonacciwanquanpingfangshu(args[0])
    elif fuwu == "进制转换":
        return jinzhizhuanhuan(args[0],args[1],args[2])
    elif fuwu=="math库计算器":
        return math_cal.math_cal(mode,args[0],args[1])
    elif fuwu == "分解因式":
        return factorization(args[0])
    elif fuwu == "提取密码":
        return mima(args[0],args[1])
    elif fuwu == "凯撒密码计算":
        return kaisamima(args[0],mode,args[1])
    elif fuwu == "彩票一体机":
        return lt.lotterytickets(args[0],args[1],mode)
    elif fuwu == "数字中文互转":
        if mode == 1:
            return ntoc.No2Cn(args[0])
        else:
            return ntoc.chinese2digits(args[0])
    elif fuwu == "图形计算器":
        while True:
            huida = args[0]
            try:
                args2=[]
                for i in range(1,len(args)):
                    args2.append(args[i])
                if tuxing(huida,mode,args2) != 1:
                    if tuxing(huida,mode,args2) != 2:
                        return tuxing(huida,mode,args2)
                    else:
                        return "不支持此图形的计算！"
                else:
                    return "不支持该功能！"
            except ValueError:
                return ("输入无效！")
    elif fuwu == "小学学生信息管理系统":
        student()
    elif fuwu == "二分查找":
        while True:
            d = args[0]
            if d == "yes":
                a = args
                b = sorted(a)
                c = args[-1]
                diaoyong  = erfenchazhao(a, b, c)
                return(diaoyong)
            elif d == "no":
                return 0
            else:
                return ("指令无效！")
    elif fuwu == "取整":
        return quzheng(args[0],args[1])
    elif fuwu == "判断闰年":
        return isleapyear(args[0])
    elif fuwu == "整数/小数计算":
        return xiaoorzhengjisuan(args[0],args[1],args[2])
    elif fuwu == "分数计算":
        return fenjisuan(args[0],args[1],args[2])
    elif fuwu == "分数小数转换":
        return xiaoorfen(args[0],mode)
    elif fuwu == "比大小":
        return args[0]>args[1]
    elif fuwu == "年龄计算":
        return args[0]-args[1]
    elif fuwu == "开n次方":
        return args[0] ** (1/args[1])
    elif fuwu == "华氏度摄氏度转换":
        return FtemporCtemp(mode,args[0])
    elif fuwu == "混合运算":
        if mode == 1:
            return args[0]+args[1]-args[2]
        elif mode == 2:
            return (args[0]+args[1])*args[2]
        elif mode == 3:
            return (args[0]+args[1])/args[2]
        elif mode == 4:
            return args[0]-args[1]+args[2]
        elif mode == 5:
            return (args[0]-args[1])*args[2]
        elif mode == 6:
            return (args[0]-args[1])/args[2]
        elif mode == 7:
            return args[0]*args[1]+args[2]
        elif mode == 8:
            return args[0]*args[1]-args[2]
        elif mode == 9:
            return args[0]*args[1]/args[2]
        elif mode == 10:
            return args[0]/args[1]+args[2]
        elif mode == 11:
            return args[0]/args[1]-args[2]
        elif mode == 12:
            return args[0]/args[1]*args[2]
        elif mode == 13:
            return args[0]/args[1]/args[2]
    elif fuwu == "货币转换":
        return duihuan(mode,args[0]) 
    elif fuwu == "随机不等式":
        return ic.suijiine(mode)
    elif fuwu == "解不等式":
        return ic.solveine(args[0])
    else:
        jieshulist = ["功能无效！", "无法实现服务！", "暂时还在开发！"]
        b = random.choice(jieshulist)
        return b
