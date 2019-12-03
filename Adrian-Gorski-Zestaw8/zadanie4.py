import math

def obliczPoleTrojkata(a, b, c):
    if( a>=b+c or b>=a+c or c>=a+b):
        raise ValueError
    else:
        p = 0.5*(a+b+c)
        
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

print ("Pole trojkata o bokach 1, 1, 1 wynosi:" + str(obliczPoleTrojkata(1,1,1)))
print ("Pole trojkata o bokach 2, 2, 3 wynosi:" + str(obliczPoleTrojkata(2,2,3)))
print ("Pole trojkata o bokach 15, 3, 15 wynosi:" + str(obliczPoleTrojkata(15,3,15)))