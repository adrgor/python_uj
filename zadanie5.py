dlugosc = raw_input("Podaj dlugosc miarki: ")

s=""

try:
    dlugosc = int(dlugosc)
    for x in range(dlugosc):
        s+="|...."
    s+="|\n"

    for x in range(dlugosc+1):
        s+=(str(x))
        for i in range(5-len(str(x+1))):
            s+=" "
            
        

    


    print(s)
    
except ValueError:
    print("Podano liczbe w blednym formacie")
