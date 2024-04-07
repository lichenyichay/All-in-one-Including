# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/25 9:03
# @FILE:erfenchazhao_py.py
# @Software:IDLE 3.9.6

import time

'''
函数名：erfenchazhao
调用形式：a = erfenchazhao(yuanlst,shengxulst,target)
:param yuanlst 原序列
:param shengxulst 升序列表（原序列改编）
:param target 查找值
:return 查找结果（索引，用时，次数）
作用：查找列表中的值
'''
def erfenchazhao(yuanlst,shengxulst,target):
    start = 0
    count = 0
    end = len(shengxulst)-1
    if target not in shengxulst:
        return None
    while True:
        count += 1
        mid = (start+end)//2
        if target < shengxulst[mid]:
            end = mid-1
            continue
        elif target > shengxulst[mid]:
            start = mid + 1
            continue
        else:
            return yuanlst.index(target)