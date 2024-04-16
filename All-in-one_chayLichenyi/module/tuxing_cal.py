# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:17
# @FILE:tuxing_cal.py
# @Software:IDLE 3.9.6
'''
函数名：tuxing
调用形式：tuxing(huida)
:param huida 图形
:return 0
作用：进行图形计算
'''
import math
def tuxing(huida,mode,*args2):
    while True:
        if huida == "长方体":
            huida1 = mode   #体积/面积/表面积/染色问题/容积/棱长总和
            huida2 = args2[0]
            huida3 = args2[1]
            huida4 = args2[2]
            if huida1 == "体积":
                shuchu = huida2 * huida3 * huida4
                return shuchu
            elif huida1 == "表面积":
                shuchu = (huida2 * huida3 + huida2 * huida4 + huida3 * huida4) * 2
                return shuchu
            elif huida1 == "染色问题":
                huida2 = int(huida2)
                huida3 = int(huida3)
                huida4 = int(huida4)
                if huida4 == 1:
                    return("4个面染色的小正方体有4个。","3个面染色的小正方体有" + str((huida2 - 2) * 2 + (huida3 - 2) * 2) + "个。","2个面染色的小正方体有" + str((huida2 - 2) * (huida3 - 2)) + "个。")
                else:
                    return("3个面染色的小正方体有8个。","2个面染色的小正方体有" + str(((huida2-2)+(huida3-2)+(huida4-2))*4) +"个。","1个面染色的小正方体有" + str(((huida2-2)*(huida3-2)+(huida2-2)*(huida4-2)+(huida3-2)*(huida4-2))*2) + "个。","0个面染色的小正方体有" + str((huida2-2)*(huida3-2)*(huida4-2)) + "个")
            elif huida1 == "棱长总和":
                shuchu = (huida2+huida3+huida4)*4
                return shuchu
            elif huida1 == "容积":
                shuchu = huida2*huida3*huida4
                return shuchu
            else:
                return 1
        elif huida == "正方体":
            huida1 = mode     #体积/面积/表面积/染色问题/容积/棱长总和
            huida2 = args2[0]
            if huida1 == "体积":
                shuchu = huida2 ** 3
                return shuchu
            elif huida1 == "表面积":
                shuchu = huida2 ** 2 * 6
                return shuchu
            elif huida1 == "棱长总和":
                shuchu = huida2 * 12
                return shuchu
            elif huida1 == "容积":
                shuchu = huida2 ** 3
                return shuchu
            elif huida1 == "染色问题":
                huida2 = int(huida2)
                if huida2 == 1:
                    return("6个面染色的小正方体有1个")
                else:
                    return("3个面染色的小正方体有8个。","2个面染色的小正方体有" + str((huida2-2)*12) + "个。","1个面染色的小正方体有" + str((huida2-2)**2*6) + "个。","0个面染色的小正方体有" + str((huida2-2)**3) + "个。")
            else:
                return 1
        elif huida == "正方形":
            huida1 = mode
            huida2 = args2[0]
            if huida1 == "面积":
                shuchu = huida2**2
                return shuchu
            elif huida1 == "边长之和":
                shuchu = huida2*4
                return shuchu
            elif huida1 == "折纸盒问题":
                huida3 = args2[1]
                V = (huida2-2*huida3)**2
                S = huida2**2-((huida3**2)*4)
                return("体积是：" + str(V) + "表面积是：" + str(S))
            else:
                return(1)
        elif huida == "长方形":
            huida1 = mode
            huida2 = args2[0]
            huida3 = args2[1]
            if huida1 == "面积":
                shuchu = huida2*huida3
                return shuchu
            elif huida1 == "周长":
                shuchu = (huida2+huida3)*2
                return shuchu
            elif huida1 == "折纸盒问题":
                huida4 = args2[2]
                V = (huida2-(2*huida4))*(huida3-(2*huida4))
                S = huida2*huida3-(huida4**2*4)
                return("体积是：" + str(V) + "表面积是：" + str(S))
            else:
                return 1
        elif huida == "平行四边形":
            huida1 = mode
            huida2 = args2[0]
            huida3 = args2[1]
            huida4 = args2[2]
            if huida1 == "面积":
                shuchu = huida2*huida3
                return shuchu
            elif huida1 == "周长":
                shuchu = (huida2+huida4)*2
                return shuchu
            elif huida1 == "折纸盒问题":
                huida5 = args2[3]
                S = huida2*huida3-(huida4**2)*4
                V = huida5*((huida4-2*huida5)*(huida2-2*huida5))
                return(f"体积是：{str(V)},表面积是：{str(S)}")
            else:
                return 1
        elif huida == "菱形":
            huida1 = mode
            huida2 = args2[0]
            huida3 = args2[1]
            if huida1 == "面积":
                shuchu = huida2*huida3
                return shuchu
            elif huida1 == "周长":
                shuchu = huida2*4
                return shuchu
            else:
                return 1
        elif huida == "三角形":
            huida1 = mode
            huida2 = args2[0]
            huida3 = args2[1]
            if huida1 == "面积":
                shuchu = huida2*huida3/2
                return shuchu
            elif huida1 == "周长":
                huida4 = args2[2]
                huida5 = args2[3]
                shuchu = huida2+huida4+huida5
                return shuchu
            else:
                return 1
        elif huida == "梯形":
            huida1 = mode
            huida2 = args2[0]
            huida3 = args2[1]
            huida4 = args2[2]
            if huida1 == "面积":
                shuchu = (huida2+huida3)*huida4/2
                return shuchu
            elif huida1 == "周长":
                huida5 = args2[3]
                huida6 = args2[4]
                shuchu = huida2+huida3+huida5+huida6
                return shuchu
            else:
                return 1
        elif huida == "圆形":
            huida1 = mode
            huida2 = args2[0]
            if huida1 == "面积":
                shuchu = math.pi*(huida2**2)
                return shuchu
            elif huida1 == "周长":
                shuchu = 2*math.pi*huida2
                return shuchu
            elif huida1 == "方中圆":
                shuchu = 0.86 * (huida2 ** 2)
                return shuchu
            elif huida1 == "圆中方":
                shuchu = 1.14 * (huida2 ** 2)
                return shuchu
            else:
                return 1
        else:
            return 2

