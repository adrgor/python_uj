slownik = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

 #lub

slownik = {}

slownik.update({"I": 1})
slownik.update({"V": 5})
slownik.update({"X": 10})
slownik.update({"L": 50})
slownik.update({"C": 100})
slownik.update({"D": 500})
slownik.update({"M": 1000})

# ewentualnie symulowanie slownika za pomoca funkcji

def slownik(x):
    if x == "I":
        return 1
    elif x == "V":
        return 5
    elif x == "X":
        return 10
    elif x == "L":
        return 50
    elif x == "C":
        return 100
    elif x == "D":
        return 500
    elif x == "M":
        return 1000
    else:
        return "Podano zly klucz"

cyfra = raw_input("Podaj cyfre w systemie rzymskim: ")
print(slownik(cyfra))