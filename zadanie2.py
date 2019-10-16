import re

line = "ab Python\tef\ngh\tij\tkl\nmn GvR op qr"
word = "word"

### Zadanie 2.10 ###
print("Zadanie 2.10")
whitespaceSplit = line.split()
print("Ilość wyrazów w napisie line: "+str(len(whitespaceSplit)))

### Zadanie 2.11 ###
print("\nZadanie 2.11")
listOfWord = list(word)
print("_".join(listOfWord))

### Zadanie 2.12 ###
print("\nZadanie 2.12")
lineSplit = line.splitlines()
print("Napis z pierwszych liter w wierszu:")
for x in range(len(lineSplit)):
    print(lineSplit[x][0], end='')

print("\nNapis z ostatnich liter w wierszu:")
for x in range(len(lineSplit)):
    print(lineSplit[x][len(lineSplit[x])-1], end='')

### Zadanie 2.13 ###
print("\n\nZadanie 2.13")
sum=0
for x in range(len(whitespaceSplit)):
    sum+=len(whitespaceSplit[x])
print("Łączna dłuość wyrazów:  "+str(sum))

### Zadanie 2.14 ###
print("\n\nZadanie 2.14")
indexMax = 0
for x in range(len(whitespaceSplit)):
    if len(whitespaceSplit[x]) > len(whitespaceSplit[indexMax]):
        indexMax = x
print("Najdluzszy wyraz: "+whitespaceSplit[indexMax])
print("Dlugosc najdluzszego wyrazu: "+str(len(whitespaceSplit[indexMax])))

### Zadanie 2.15###
print("\nZadanie 2.15")
L = [12,578,1235]
s = ""
for x in range(len(L)):
    for y in range(len(str(L[x]))):
        s += str(L[x])[y]
print(s)

### Zadanie 2.16 ###
print("\nZadanie 2.16")
newString = re.sub(r"GvR", "Guido van Rossum",line,0)
print(newString)

### Zadanie 2.17 ###
print("\nZadanie 2.17")
print("Alfabetycznie: "+str(sorted(whitespaceSplit,key=str.lower)))
print("Po długości: " + str(sorted(whitespaceSplit,key=len)))

### Zadanie 2.18 ###
print("\nZadanie 2.18")
liczba = 1200000050400400400340003000100050
liczbaS = str(liczba)
sum = 0
for x in range(len(liczbaS)):
    if(liczbaS[x] == '0'):
        sum += 1
print("Ilość zer w liczbie "+liczbaS+" wynosi "+str(sum))

### Zadanie 2.19 ###
print("\nZadanie 2.19")
L = [1,25,354,266,12,5,9,35]
for x in range(len(L)):
    print(str(L[x]).zfill(3), end=' ')
