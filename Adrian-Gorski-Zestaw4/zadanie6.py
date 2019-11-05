

def sum_seq(sequence):
    sum = 0
    for x in sequence:
        if(isinstance(x, (list, tuple))):
            sum = sum + sum_seq(x)
        else:
            sum = sum + x
    return sum
L=(1,2,3,(1,2,(1,2,3),1,2),(1,4,6),12,(1,2,(3,4,(4,5,(1,2,3,4)))))

print sum_seq(L)