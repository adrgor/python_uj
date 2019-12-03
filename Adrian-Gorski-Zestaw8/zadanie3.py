import random
import math

def countPi(n):
    nTotal = n
    nInside = 0.0


    for i in range(nTotal):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if( math.sqrt(x*x+y*y) <= 1 ): nInside = nInside + 1

    pi = (nInside/nTotal)*4
    return pi

print("Wartosc pi dla 10000000 iteracji: ") + str(countPi(10000000))
print("Wartosc pi dla 1000000 iteracji: ") + str(countPi(1000000))
print("Wartosc pi dla 100000 iteracji: ") + str(countPi(100000))
print("Wartosc pi dla 10000 iteracji: ") + str(countPi(10000))
print("Wartosc pi dla 1000 iteracji: ") + str(countPi(1000))