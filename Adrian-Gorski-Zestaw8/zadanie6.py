import time

def recursiveP(i,j):
    if(i == 0 and j == 0): return 0.5
    elif(i>0 and j == 0): return 0.0
    elif(j>0 and i == 0): return 1.0
    elif(i>0 and j>0): return 0.5*( recursiveP(i-1,j) + recursiveP(i,j-1) )

def dynapicP(i,j):
    
    A = [None] * (i+1)
    for z in range(i+1):
        A[z] = [None] * (j+1)
    
    for x in range(i+1):
        A[x][0] = 0.0
    for x in range(j+1):
        A[0][x] = 1.0
    A[0][0] = 0.5
    
    x = 1 #i
    y = 1 #j
    for x in range(1,i+1):
        for y in range (1,j+1):
            A[x][y] = 0.5*( A[x-1][y] + A[x][y-1] )
            


    return A[i][j]
start_time = time.time()
print recursiveP(16,8)
end_time = time.time()
print "Czas dla rozwiazania rekurencyjnego: "+str(end_time-start_time)

start_time = time.time()
print dynapicP(16,8)
end_time = time.time()
print "Czas dla rozwiazania dynamicznego: "+str(end_time-start_time)