# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/4/19 23:41
# @FILE:Allinone.py
# @version:2.4.8
# @Software:Visual Studio Code
import math,random
import module.book as book
import module.calculator as calculator
import module.erfenchazhao_py  as erfenchazhao_py
import module.math_cal_py as math_cal
import module.student_py as student_py
import module.tuxing_cal as tuxing_cal
import module.xiaogongju as xiaogongju
def allinone(fuwu,mode,*args):
    """
    :param fuwu 需要服务的功能
    :param mode 部分功能需要的模式（详见Github中All-in-one2.4.0分支的Wiki页）
    :param *args 可变参数，表示需要传入的参数，建议用元组或列表类型，具体所需类型见README.MD
    :return: 0：正常，1：不正常，其他返回值表示功能的结果

    功能（按代码顺序排序，不分先后）：大小写互换、抽取随机数、求最小公倍数、求最大公倍数、图形计算器、小学学生信息管理系统、二分查找、求余、向下取整、向上取整、多个数求和、多个数求差、多个数求积、判断闰年、判断是否为质数、整数、小数计算（加减乘除）、分数计算（加减乘除）......（具体见Github All-in-one2.4.0分支Readme.md文件）
    """
    if fuwu == "大小写互换":
        return xiaogongju.daorxiao(args[0],mode)
    elif fuwu == "抽取随机":
        return xiaogongju.chouqusuiji(args[0],args[1],mode,args[2])
    elif fuwu == "求最小公倍数":
        num1 = args[0]
        num2 = args[1]
        for i1 in range(max(num1, num2), num1 * num2 + 1):
            if i1 % num1 == 0 and i1 % num2 == 0:
                return i1
    elif fuwu == "求最大公因数":
        num1 = args[0]
        num2 = args[1]
        return xiaogongju.twonumbers_TheBiggestCommonfactor(num1,num2)
    # elif fuwu == "快速排列":
    #     kuaisupailie()
    elif fuwu=="反转字符串":
        return calculator.fanzhuanzifuchuan(args[0])
    elif fuwu=="判断质数":
        return calculator.isparam(args[0])
    elif fuwu=="判断回文数":
        return calculator.ishuiwenshu(args[0])
    elif fuwu=="判断回文质数":
        return calculator.ishuiwenzhishu(args[0])
    elif fuwu=="求斐波那契数列的第n项":
        return calculator.fab(args[0])
    elif fuwu=="判断斐波那契数":
        return calculator.isfab(args[0])
    elif fuwu=="判断斐波那契回文质数":
        return calculator.isfabhuiwenzhishu(args[0])
    elif fuwu=="判断斐波那契回文数":
        return calculator.isfabhuiwenshu(args[0])
    elif fuwu=="判断斐波那契质数":
        return calculator.isfabparam(args[0])
    elif fuwu=="求泰波那契序列的第n项":
        return calculator.tribonacci(args[0])
    elif fuwu=="判断泰波那契数":
        return calculator.istribonacci(args[0])
    elif fuwu=="判断泰波那契回文质数":
        return calculator.istribonaccihuiwenshuparam(args[0])
    elif fuwu=="判断泰波那契回文数":
        return calculator.istribonaccihuiwenshu(args[0])
    elif fuwu=="判断泰波那契质数":
        return calculator.istribonacciparam(args[0])
    elif fuwu=="求第n个完全平方数":
        return calculator.wanquanpingfangshu(args[0])
    elif fuwu=="判断完全平方数":
        return calculator.iswanquanpingfangshu(args[0])
    elif fuwu=="判断斐波那契完全平方数":
        return calculator.isfabwanquanpingfangshu(args[0])
    elif fuwu=="判断泰波那契序列完全平方数":
        return calculator.istribonacciwanquanpingfangshu(args[0])
    elif fuwu == "进制转换":
        return calculator.jinzhizhuanhuan(args[0],args[1],args[2])
    elif fuwu=="math库计算器":
        return math_cal.math_cal(mode,args[0],args[1])
    elif fuwu == "分解因式":
        return calculator.factorization(args[0])
    elif fuwu == "提取密码":
        return calculator.mima(args[0],args[1])
    elif fuwu == "图形计算器":
        while True:
            huida = args[0]
            try:
                args2=[]
                for i in range(1,len(args)):
                    args2.append(args[i])
                if tuxing_cal.tuxing(huida,mode,args2) != 1:
                    if tuxing_cal.tuxing(huida,mode,args2) != 2:
                        return tuxing_cal.tuxing(huida,mode,args2)
                    else:
                        return "不支持此图形的计算！"
                else:
                    return "不支持该功能！"
            except ValueError:
                return ("输入无效！")
    elif fuwu == "小学学生信息管理系统":
        student_py.student()
    elif fuwu == "二分查找":
        while True:
            d = args[0]
            if d == "yes":
                a = args
                b = sorted(a)
                c = args[-1]
                diaoyong  = erfenchazhao_py.erfenchazhao(a, b, c)
                return(diaoyong)
            elif d == "no":
                return 0
            else:
                return ("指令无效！")
    elif fuwu == "求余":
        while True:
            try:     
                w1 = args[0]
                w2 = args[1]
                w3 = w1 % w2
                return w3
            except Exception as e:
                raise Exception(repr(e))
    elif fuwu == "向下取整":
        while True:
            try:
                w1 = args[0]
                return int(w1)
            except Exception as e:
                raise Exception(repr(e))
    elif fuwu == "向上取整":
        while True:
            try:
                w1 = args[0]
                return (int(w1)+1)
            except Exception as e:
                raise Exception(repr(e))
    elif fuwu == "多个数求和":
        try:
            b = args
            b = tuple(b)
            b = math.fsum(b)
            return (b)
        except Exception as e:
            raise Exception(repr(e))
    elif fuwu == "多个数求差":
        try:
            b = 0
            e = args
            c = len(args)
            b = e[0]
            for i in range(c-1):
                b -= e[1+i]
            return (b)
        except Exception as e:
            raise Exception(repr(e))
    elif fuwu == "多个数求积":
        try:
            b = 0
            e = args
            c = len(args)
            b = e[0]
            for i in range(c-1):
                b *= e[1+i]
            return(b)
        except Exception as e:
            print(repr(e))
    elif fuwu == "判断闰年":
        return calculator.isleapyear(args[0])
    elif fuwu == "整数、小数计算-乘":
        if mode == "0":
            eee = args[0]
            aaa = args[1]
            qqq = eee * aaa
            return("等于",qqq)
        else:
            eee = args[0]
            aaa = args[1]
            qqq = eee / aaa
            return("等于",qqq)
    elif fuwu == "分数计算-加":
        try:
            qw = args[0]
            sd =args[1]
            ad = args[2]
            df = args[3]
            sva = (sd/qw)+(df/ad)
            return("等于",sva)
        except Exception as e:
            raise Exception(e)
    elif fuwu == "分数计算-减":
        try:
            qw = args[0]
            sd =args[1]
            ad = args[2]
            df = args[3]
            sva = (sd/qw)-(df/ad)
            return("等于",sva)
        except Exception as e:
            raise Exception(e)
    elif fuwu == "分数计算-乘":
        try:
            qw = args[0]
            sd =args[1]
            ad = args[2]
            df = args[3]
            sva = (sd/qw)*(df/ad)
            return("等于",sva)
        except Exception as e:
            raise Exception(e)
    elif fuwu == "分数计算-除":
        try:
            qw = args[0]
            sd =args[1]
            ad = args[2]
            df = args[3]
            sva = (sd/qw)/(df/ad)
            return("等于",sva)
        except Exception as e:
            raise Exception(e)
    elif fuwu == "比大小":
        return args[0]>args[1]
    elif fuwu == "年龄计算":
        return args[0]-args[1]
    elif fuwu == "开n次方":
        return args[0] ** (1/args[1])
    elif fuwu == "华氏度摄氏度转换":
        return calculator.FtemporCtemp(mode,args[0])
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
        return calculator.duihuan(mode,args[0]) 
    else:
        jieshulist = ["功能无效！", "无法实现服务！", "暂时还在开发！"]
        b = random.choice(jieshulist)
        return b
