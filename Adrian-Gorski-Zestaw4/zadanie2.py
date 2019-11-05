def miarka():
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
                
            

        


        return s
        
    except ValueError:
        print("Podano liczbe w blednym formacie")





def kratka():
    dlugosc = int(raw_input("Podaj dlugosc kratki: "))
    wysokosc = int(raw_input("Podaj wysokosc kratki: "))
    s=""

    for x in range(wysokosc):
        s+="\n+"
        for i in range(dlugosc):
            s+="---+"
        s+="\n|"
        for i in range(dlugosc):
            s+="   |"
        
    s+="\n+"
    for i in range(dlugosc):
        s+="---+"
    return s


miarka = miarka()
print(miarka)

kratka=kratka()
print(kratka)
