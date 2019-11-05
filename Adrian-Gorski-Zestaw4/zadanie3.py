def factorial(n):
    wynik = 1
    if(n==0): 
        return 1
    else:
        while(n>0):
            wynik *= n
            n=n-1
        return wynik

liczba = int(raw_input("Podaj liczbe calkowita: "))
print(str(liczba)+"! = "+str(factorial(liczba)))