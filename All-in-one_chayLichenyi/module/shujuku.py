# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2024/07/23 17:00
# @FILE:Allinone.py
# @version:4.0.1
# @Software:Visual Studio Code

from sqlite3 import *
from os import * 
def sjc(fuwu:str,mode:int,canshu:str):
    makedirs("D:\\all-in-one", exist_ok=True)   
    conn = connect("D:\\all-in-one\\All in one 库使用数据.db")  
    cursor = conn.cursor()  
    sql_create_table = """  
    CREATE TABLE IF NOT EXISTS "All-in-one库使用数据" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "使用功能"	TEXT NOT NULL,
        "模式" TEXT
        "参数"	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
    );
    """
    cursor.execute(sql_create_table)
    conn.commit() 

    sql_insert='''
    INSERT INTO "All-in-one库使用数据" ("使用功能","模式","参数")  
    VALUES (?, ?, ?);
    '''
    cursor.execute(sql_insert, (fuwu,mode,canshu))
    conn.commit()

    cursor.close()  
    conn.close() 