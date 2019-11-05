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

liczba = int(raw_input("Podaj ktory element ciagu obliczyc: "))
print(str(liczba)+" element ciagu fibonacciego to: "+str(fibonacci(liczba)))
    