
while True:
    reply = raw_input("Podaj liczbe: ")
    if(reply == "stop"):
        break
    else:
        try:
            number = float(reply)
            print("x = "+str(number) + " x^3 = "+str(number*number*number))
        except ValueError:
            print("To nie liczba")
