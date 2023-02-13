from math import pi
fncs = ['square', 'hollow_square', 'rotated_square', 'rotated_hollow_square', 'rectangle', 'triangle', 'hex', 'trapezoid', 'circle', 'hollow_circle', 'elipse', 'TUL', 'I', 'H']

def square(a):
    Area = a**2
    Jx = a**4/12
    Wo = a**3/6
    Jp = 0.141*a**4
    Wk = 0.204*a**3
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3\nJp = {round(Jp,3)}mm4\nWk = {round(Wk, 3)}mm3"])


def hollow_square(H, h):
    Area = H**2-h**2
    Jx = (H**4-h**4)/12
    Wo = (H**4-h**4)/(6*H)
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3"])


def rotated_square(a):
    Area = a**2
    Jx = a**4/12
    Wo = ((a**3)*(2**(1/2)))/12
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3"])


def rotated_hollow_square(H,h):
    Area = H**2-h**2
    Jx = (H**4-h**4)/12
    Wo = ((2**(1/2))*(H**4-h**4))/12*H
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3"])


def rectangle(b, h):
    Area = b*h
    Jx = (b*h**3)/12
    Jz = (b**3*h)/12
    Wox = (b*h**2)/6
    Woz = (b**2*h)/6
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nJz = {Jz}mm4\nWo = {round(Wox, 3)}mm3\nWoz = {round(Woz, 3)}mm3"])


def triangle(b, h):
    Area = (b*h)/2
    Jx = (b*h**3)/36
    Jx2 = (b*h**3)/12
    Wx = (b*h**2)/24
    Wx2 = (b*h**2)/12
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nJx' = {Jx2}mm4\nWx = {round(Wx, 3)}mm3\nWx = {round(Wx2, 3)}mm3"])


def hex(s, e):
    Area = ((3*3**(1/3))/8)*e**2
    Jx = 0.04*e**4
    WoA = 0.068*e**3
    WoB = 0.078*e**3
    Jp = 0.015*s**4
    Wk = 0.189*s**3
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWoA = {round(WoA, 3)}mm3\nWoB = {round(WoB, 3)}mm3\nJp = {round(Jp,3)}mmm\nWk = {round(Wk, 3)}mm3"])


def trapezoid(b, b1, h):
    Area = ((2*b + b1)/2)*h
    Jx = ((6*b**2 + 6*b*b1 + b1**2)/(36*(2*b+b1)))*h**3
    Wo = ((6*b**2 + 6*b*b1 + b1**2)/(12*(3*b+2*b1)))*h**2
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3"])


def circle(d):
    Area = (pi*d**3)/4
    Jx = (pi*d**4)/64
    Wo = (pi*d**3)/32
    Jp = (pi*d**4)/32
    Wk = (pi*d**3)/16
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3\nJp = {round(Jp,3)}mm4\nWk = {round(Wk, 3)}mm3"])


def hollow_circle(D,d):
    Area = (pi/4)*(D**2-d**2)
    Jx = (pi/64)*(D**4-d**4)
    Wo = (pi/32)*((D**4-d**4)/D)
    Jp = (pi/32)*(D**4-d**4)
    Wk = (pi/16)*((D**4-d**4)/D)
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3\nJp = {round(Jp,3)}mm4\nWk = {round(Wk, 3)}mm3"])


def elipse(b, h):
    Area = (pi/4)*b*h
    Jx = (pi/64)*b*h**3
    Wo = (pi/32)*b*h**3
    Jp = (pi/16)*((b**3*h**3)/(b**2+h**2))
    Wk1 = (pi/16)*b**2*h
    Wk2 = (pi/16)*b*h**2
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}\nWo = {round(Wo, 3)}mm3\nJp = {round(Jp,3)}mm4\nWk1 = {round(Wk1, 3)}mm3\nWk2 = {round(Wk2, 3)}mm3"])


def TUL(a, H, t, B, h):
    b =   B-a
    Area =   a*H + B*t
    e1 =  (a*H**2+b*t**2)/(2*(a*H+b*t))
    e2 =  H - e1
    Jx =  (1/3)*(B*e1**3 - b*h**3+a*e2**3)
    Wo1 = Jx/e1
    Wo2 = Jx/e2
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\ne1 = {round(e1, 3)}\ne2 = {round(e2, 3)}\nWo1 = {round(Wo1, 3)}mm3\nWo2 = {round(Wo2, 3)}mm3"])


def H_profile(B, b, H, h):
    Area = B*H + b*h
    Jx = (B*H**3 + b*h**3)/12
    Wo = (B*H**3 + b*h**3)/6*H
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3"])
    

def I_profile(B, b, H ,h):
    Area = B*H - b*H
    Jx = (B*H**3 + b*h**3)/12
    Wo = (B*H**3 + b*h**3)/6*H
    return ([Jx, f"A = {round(Area, 3)}mm2\nJx = {round(Jx, 3)}mm4\nWo = {round(Wo, 3)}mm3"])


fncsstr = ['Čtverec', 'Dutý čtverec', 'Čtverec otočený o 45°', 'Dutý čtverec otočený o 45°', 'Obdelník', 'Trojúhelník', 'Šestiúhelník', 'Lichoběžník', 'Kruh', 'Mezikruží', 'Elipsa', 'Profily T, U, L, apod.', 'Profil H apod.', 'Profil I apod.']
fncs = [square, hollow_square, rotated_square, rotated_hollow_square, rectangle, triangle, hex, trapezoid, circle, hollow_circle, elipse, TUL, I_profile, H_profile]


def get_args(fnc):
    argcount = fnc.__code__.co_argcount
    varnames = fnc.__code__.co_varnames
    args = []
    for i in range(argcount):
        args.append(varnames[i])
    return args

