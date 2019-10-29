

dlugosc = int(raw_input("Podaj dlugosc: "))
wysokosc = int(raw_input("Podaj wysokosc: "))
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
print(s)