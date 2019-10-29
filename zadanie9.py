x = [[],[15,1],(1,2,2,8),[3,4],(5,6,7),(1,9)]

l=[]

for i in range(len(x)):
    l.append(sum(x[i]))

print(l)