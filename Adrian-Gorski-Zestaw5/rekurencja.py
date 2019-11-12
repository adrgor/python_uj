def factorial(n):
    wynik = 1
    if(n==0): 
        return 1
    else:
        while(n>0):
            wynik *= n
            n=n-1
        return wynik

def fibonacci(n):
    if(n<=2):
        return 1
    else:
        n1, n2=1,1
        for x in range(3,n+1):
            n0=n1+n2
            n1=n2
            n2=n0
    return n2
