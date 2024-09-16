# Author:Chay
# Time:2024/9/5 22:47
# Release:1.0.0

# 长度单位换算函数
def mmtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10.0


def mmtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 100.0


def mmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x / 1000.0


def mmtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 1000000.0


def cmtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10.0


def cmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x / 100.0


def cmtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 100000.0


def dmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10.0


def dmtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 10000.0


def mtokm(x: float) -> float:
    """
    :rtype: float
    """
    return x / 1000.0


def cmtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10.0


def dmtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 100.0


def mtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 1000.0


def kmtomm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 1000000.0


def dmtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10.0


def mtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 100.0


def kmtocm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 100000.0


def mtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10.0


def kmtodm(x: float) -> float:
    """
    :rtype: float
    """
    return x * 10000.0


def kmtom(x: float) -> float:
    """
    :rtype: float
    """
    return x * 1000.0

def μmtomm(x:float) -> float:
    '''
    :rtype:float
    '''
    return x/1000.0

def mmtoμm(x:float) -> float:
    '''
    :rtype:float
    '''
    return x*1000.0

def nmtoμm(x:float) -> float:
    '''
    :rtype:float
    '''
    return x/1000.0

def μmtonm(x:float) -> float:
    '''
    :rtype:float
    '''
    return x*1000.0
# 物理量换算函数


def ρ(V=0.0,m=0.0,g=9.8,h=0.0,p=0.0,Ffu=0.0) -> float:
    if V!=0.0 and m != 0.0:
        return m/V
    elif p!=0.0 and h != 0.0 and g != 0.0:
        return p/(g*h)
    elif Ffu != 0 and g!=0 and V!=0.0:
        return Ffu/(g*V)
    else:
        raise ValueError("参数无效！")


def m(G=0.0,g=9.8,V=0.0,ρ=0.0) -> float:
    if G!=0 and g!=0:
        return G/g
    elif V!=0 and ρ!=0:
        return ρ*V
    else:
        raise ValueError("参数无效！")


def Vtiji(m=0.0,ρ=0.0,g=9.8,Ffu=0.0) -> float:
    if m!=0 and ρ!=0:
        return m/ρ
    elif g!=0 and Ffu!=0 and ρ!=0:
        return Ffu/(g*ρ)
    else:
        raise ValueError("参数无效！")


def Vsudu(Slu=0.0,t=0.0) -> float:
    if Slu!=0 and t != 0:
        return Slu/t
    else:
        raise ValueError("参数无效！")


def p(F = 0.0,S = 0.0,ρ = 0.0,g = 9.8, h=0.0) -> float:
    if F != 0 and S != 0:
        return F/S
    elif ρ != 0 and h != 0 and g != 0:
        return ρ*g*h
    else:
        raise ValueError("参数无效！")


def I(U = 0.0,R = 0.0,Pgong = 0.0) -> float:
    if U != 0 and R != 0:
        return U/R
    elif U != 0 and Pgong != 0:
        return Pgong / U
    else:
        raise ValueError("参数无效！")


def U(I = 0.0,R = 0.0,Pgong = 0.0) -> float:
    if I != 0 and R != 0:
        return I*R
    elif I != 0 and Pgong != 0:
        return Pgong / I
    else:
        raise ValueError("参数无效！")


def R(I = 0.0,U = 0.0) -> float:
    if U != 0 and I != 0:
        return U/I
    else:
        raise ValueError("参数无效！")


def Pgong(U=0.0,I=0.0) -> float:
    if U != 0 and I != 0:
        return U*I
    else:
        raise ValueError("参数无效！")
def UnitConverter(mode:int,args:dict) -> float:
    if type(args) != dict:
        raise TypeError("args参数需为dict类型！")
    if type(mode) != int:
        raise TypeError("mode参数需为int类型！")
    if mode > 33 or mode < 1:
        raise ValueError("mode参数需在1-33之间！")
    else:
        if mode == 1:
            if "mm" in args.keys():
                return mmtocm(args['mm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 2:
            if "mm" in args.keys():
                return mmtodm(args['mm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 3:
            if "mm" in args.keys():
                return mmtom(args['mm'])
            else:
                raise ValueError("缺少参数或参数类型错误！")   
        elif mode == 4:
            if "mm" in args.keys():
                return mmtom(args['mm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 5:
            if "cm" in args.keys():
                return cmtodm(args['cm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 6:
            if "cm" in args.keys():
                return cmtom(args['cm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 7:
            if "cm" in args.keys():
                return cmtokm(args['cm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 8:
            if "dm" in args.keys():
                return dmtom(args['dm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 9:
            if "dm" in args.keys():
                return dmtokm(args['dm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 10:
            if "m" in args.keys():
                return mtokm(args['m'])
            else:
                raise ValueError("缺少参数或参数类型错误！")  
        elif mode == 11:
            if "cm" in args.keys():
                return cmtomm(args['cm'])
            else:
                raise ValueError("缺少参数或参数类型错误！")  
        elif mode == 12:
            if "dm" in args.keys():
                return dmtomm(args['dm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 13:
            if "m" in args.keys():
                return mtomm(args['m'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 14:
            if "km" in args.keys():
                return kmtomm(args['km'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 15:
            if "dm" in args.keys():
                return dmtocm(args['dm'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 16:
            if "m" in args.keys():
                return mtocm(args['m'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 17:
            if "km" in args.keys():
                return kmtocm(args['km'])
            else:
                raise ValueError("缺少参数或参数类型错误！")   
        elif mode == 18:
            if "m" in args.keys():
                return mtodm(args['m'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 19:
            if "km" in args.keys():
                return kmtodm(args['km'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 20:
            if "km" in args.keys():
                return kmtom(args['km'])
            else:
                raise ValueError("缺少参数或参数类型错误！") 
        elif mode == 21:
            if "μm" in args.keys():
                return μmtomm(args['μm'])
            else:
                raise ValueError("缺少参数或参数类型错误！")
        elif mode == 22:
            if "mm" in args.keys():
                return mmtoμm(args['mm'])
            else:
                raise ValueError("缺少参数或参数类型错误！")
        elif mode == 23:
            if "nm" in args.keys():
                return nmtoμm(args['μm'])
            else:
                raise ValueError("缺少参数或参数类型错误！")
        elif mode == 24:
            if "μm" in args.keys():
                return μmtonm(args['μm'])
            else:
                raise ValueError("缺少参数或参数类型错误！")
        elif mode == 25:
            if ('V' in args.keys() and 'm' in args.keys()):
                return ρ(V=args['V'],m=args['m'])
            elif ('p' in args.keys() and 'h' in args.keys()):
                return ρ(p=args['p'],h=args['h'])
            elif ('Ffu' in args.keys() and 'V' in args.keys()):
                if 'g' in args.keys():
                    return ρ(g=args['g'],Ffu = args['Ffu'],V=args['V'])
                else:
                    return ρ(Ffu = args['Ffu'],V=args['V'])
            else:
                raise ValueError("缺少参数！")
        elif mode == 26:
            if ('G' in args.keys()):
                if 'g' in args.keys():
                    return m(G=args['G'],g=args['g'])
                else:
                    return m(G=args['G'])
            elif ('ρ' in args.keys() and 'V' in args.keys()):
                return m(ρ=args['ρ'],V=args['V'])
            else:
                raise ValueError("缺少参数！")
        elif mode == 27:
            if 'm' in args.keys() and 'ρ' in args.keys():
                return Vtiji(m=args['m'],ρ=args['ρ'])
            elif 'Ffu' in args.keys() and 'ρ' in args.keys():
                if 'g' in args.keys():
                    return Vtiji(Ffu=args['Ffu'],ρ=args['ρ'],g = args['g'])
                else:
                    return Vtiji(Ffu=args['Ffu'],ρ=args['ρ'])
            else:
                raise ValueError("缺少参数！")
        elif mode == 28:
            if ("Slu" in args.keys() and "t" in args.keys()):
                return Vsudu(args["Slu"],args['t'])
            else:
                raise ValueError("缺少参数！")
        elif mode == 29:
            if ('F' in args.keys() and 'S' in args.keys()):
                return p(F=args['F'],S=args['S'])
            elif ('ρ' in args.keys() and 'h' in args.keys()):
                if 'g' in args.keys():
                    return p(ρ=args['ρ'],h=args['h'],g=args['g'])
                else:
                    return p(ρ=args['ρ'],h=args['h'])
            else:
                raise ValueError("缺少参数！")
        elif mode == 30:
            if('U' in args.keys()):
                if 'R' in args.keys():
                    return I(U=args['U'],R=args['R'])
                elif 'Pgong' in args.keys():
                    return I(U=args['U'],Pgong=args['Pgong'])
                else:
                    raise ValueError("缺少参数！")
            else:
                raise ValueError("缺少参数！")
        elif mode == 31:
            if 'I' in args.keys():
                if 'R' in args.keys():
                    return U(I=args['I'],R=args['R'])
                elif 'Pgong' in args.keys():
                    return U(I=args['I'],Pgong=args['Pgong'])
                else:
                    raise ValueError("缺少参数！")
            else:
                raise ValueError("缺少参数！")
        elif mode == 32:
            if ("U" in args.keys() and "I" in args.keys()):
                return R(U=args["U"],I=args['I'])
            else:
                raise ValueError("缺少参数！")
        elif mode == 33:
            if 'U' in args.keys() and 'I' in args.keys():
                return Pgong(U=args['U'],I=args['I'])
            else:
                raise ValueError("参数错误！")
if __name__ == "__main__":
    pass
