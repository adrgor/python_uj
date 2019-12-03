import math

def solve1(a, b, c):

    if(a == 0 and b == 0 and c != 0): return "Sprzecznosc"
    if(a == 0 and b == 0 and c == 0): return "Tozsamosc"

    if(b==0):
        if(a*c<0): znak = 1
        else: znak = -1
        return "Linia pionowa: x={}/{}".format(znak*math.fabs(c),math.fabs(a))

    if(a==0):
        if(a*c<0): znak = 1
        else: znak = -1
        return "Linia pionowa: y={}/{}".format(znak*math.fabs(c),math.fabs(b))

    if(a*b<0): znakX = 1
    else: znakX=-1

    if(a*c<0): znakC=1
    else: znakC=-1
    return "Linia ukosna: y=({}/{})x+({}/{})".format(znakX*math.fabs(a),math.fabs(b), znakC*math.fabs(c), math.fabs(b))

print solve1(2,-3,-11)


