# All-in-one Including

注：导入时请使用

```py
from Allinoneincluding import *
```

或

```py
import Allinoneincluding as aioi #你没有安装aioi时
```

且本项目与All-in-one-chay库功能相同，由于库文件配置问题，导致源库无法正常使用，请下载Allinoneincluding库，谢谢！

多功能一体机库版本，现已更新至4.1.0版本
说明如下：

## 模块说明

### Allinone.py 主文件

```python

Help on module Allinone:

NAME
    Allinone

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/23 17:00
    # @FILE:Allinone.py
    # @version:4.0.1
    # @Software:Visual Studio Code

FUNCTIONS
    allinone(fuwu, mode, *args)
        :param fuwu 需要服务的功能
        :param mode 部分功能需要的模式（详见Github中All-in-one2.4.0分支的Wiki页）
        :param *args 可变参数，表示需要传入的参数，建议用元组或列表类型，具体所需类型见README.MD
        :return: 0：正常，1：不正常，其他返回值表示功能的结果

        功能（按代码顺序排序，不分先后）：大小写互换、抽取随机数、求最小公倍数、求最大公倍数、图形计算器、小学学生信息管理系统、二分查找、求余、向下取整、向上取整、多个数求和、多个数求差、多个数求积、判断闰年、判断是否为质数、整数、小数计算（加减乘除）、分数计算（加减乘除）......（具体见Github All-in-one2.4.0分支Readme.md文件）

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\allinone.py
```

### shujuku.py 数据库文件

```python
Help on module shujuku:

NAME
    shujuku

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/23 17:00
    # @FILE:Allinone.py
    # @version:4.0.1
    # @Software:Visual Studio Code

FUNCTIONS
    
    sjc(fuwu: str, mode: int, canshu: str)

FILE
    d:\chay\project\all-in-one-including(git)\all-in-one_chaylichenyi\module\shujuku.py
```

### xiaogongju.py 模块文件

```python
Help on module xiaogongju:

NAME
    xiaogongju

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 17:20
    # @FILE:xiaogongju.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    chouqusuiji(num1: int, num2: int, mode: int, weishu: int) -> str

    daorxiao(args: str, mode: int) -> str

    f(a: float, n: int, m: int) -> int

    kaisamima(arg: str, mode: int, n: int) -> str

    quzheng(num: float, mode: int) -> int

    twonumbers_TheBiggestCommonfactor(num1: int, num2: int) -> int

    twonumbers_TheMinimumCommonmultiple(num1: int, num2: int) -> int

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\xiaogongju.py
```

### calculator.py 计算器模块

```python
Help on module calculator:

NAME
    calculator

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 17:20
    # @FILE:calculator.py
    # @Software:Visual Studio Code

FUNCTIONS
    FtemporCtemp(mode: str, FtemporCtemp: float) -> float

    duihuan(mode: int, money: float) -> float

    fab(x: int) -> int

    factorization(num: int) -> list[int]

    fanzhuanzifuchuan(s: str) -> str

    fenjisuan(num1: str, num2: str, mode: str) -> float

    isfab(x: int) -> bool

    isfabhuiwenshu(x: int) -> bool

    isfabhuiwenzhishu(x: int) -> bool

    isfabparam(x: int) -> bool

    isfabwanquanpingfangshu(num: int) -> bool

    ishuiwenshu(d: int) -> bool

    ishuiwenzhishu(d: int) -> bool

    isleapyear(x) -> bool

    isparam(d: int) -> bool

    istribonacci(n: int) -> bool

    istribonaccihuiwenshu(n: int) -> bool

    istribonaccihuiwenshuparam(n: int) -> bool

    istribonacciparam(n: int) -> bool

    istribonacciwanquanpingfangshu(num: int) -> bool

    iswanquanpingfangshu(num: int) -> bool

    jinzhizhuanhuan(a: int, b: int, c: str) -> str

    mima(num: int, n: int) -> int

    tribonacci(n: int) -> int

    wanquanpingfangshu(num: int) -> int

    xiaoorfen(num: str, mode: int) -> str

    xiaoorzhengjisuan(num1: float, num2: float, mode: str) -> float

    yiyuannci(fangcheng: str, mode: int) -> tuple

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\calculator.py

```

### numbertochinese.py 数字、中文互换模块

```python
Help on module numbertochinese:

NAME
    numbertochinese

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 18:00
    # @FILE:numbertochinese.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    No2Cn(number: int) -> str

    chinese2digits(uchars_chinese: str) -> int

    maxdigit(number: int, count: int) -> tuple

DATA
    common_used_numerals = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '日': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
    digitdict = {1: '十', 2: '百', 3: '千', 4: '万'}
    numdict = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",0:"零"}

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\numbertochinese.py
```

### lotterytickets.py 彩票一体机模块

```python
Help on module lotterytickets:

NAME
    lotterytickets

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/5/3 23:25
    # @FILE:lotterytickets.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    lotterytickets(user: str, mubiao: str, mode: int) -> str

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\lotterytickets.py
```

### erfenchazhao_py.py 二分查找模块

```python
Help on module erfenchazhao_py:

NAME
    erfenchazhao_py

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2022/12/25 9:03
    # @FILE:erfenchazhao_py.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    erfenchazhao(yuanlst, shengxulst, target)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\erfenchazhao_py.py
```

### math_cal.py math库计算器模块

```python
Help on module math_cal_py:

NAME
    math_cal_py

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2022/12/24 15:38
    # @FILE:math_cal_py.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    math_cal(mode, float1, float2)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\math_cal_py.py
```

### student_py.py 小学学生信息管理系统模块

```python
Help on module student_py:

NAME
    student_py

DESCRIPTION
    函数名：student
    调用形式：student()
    作用：小学学生信息管理系统

FUNCTIONS
    student()

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\student_py.py
```

### tuxing_cal.py 图形计算器模块

```python
Help on module tuxing_cal:

NAME
    tuxing_cal

DESCRIPTION
    函数名：tuxing
    调用形式：tuxing(huida)
    :param huida 图形
    :return 0
    作用：进行图形计算

FUNCTIONS
    tuxing(huida, mode, *args2)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\tuxing_cal.py
```

### inequalitychay.py 不等式计算模块

```python
Help on module inequalitychay:

NAME
    inequalitychay

FUNCTIONS
    getrandbits(k, /) method of random.Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.

    random() method of random.Random instance
        random() -> x in the interval [0, 1).

    solveine(s: str) -> str
        Solves a linear inequality expression and returns the solution set.

        Args:
            s (str): The inequality expression as a string.

        Returns:
            str: The solution set of the inequality expression.

    suijiine(dif: int) -> str
        Generates a random inequality expression with a given level of difficulty.

        Args:
            dif (int): The difficulty level of the inequality expression, which determines the number of operations.

        Returns:
            str: A randomly generated inequality expression.

FILE
    d:\chay\project\inequality-including\src\inequalitychay\inequalitychay.py
```

详见<https://github.com/lichenyichay/All-in-one> 和 <https://github.com/lichenyichay/All-in-one-Including/wiki>
