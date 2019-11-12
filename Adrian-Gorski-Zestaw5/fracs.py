def nwd(a, b):
	pom = 0
	while(b != 0):
		pom = b
		b = a % b
		a = pom
	return a

def add_frac(frac1, frac2):
	myNwd = 0
	licznik = frac1[0]*frac2[1]+frac1[1]*frac2[0]
	mianownik = frac1[1]*frac2[1]
	myNwd = nwd(licznik,mianownik)
	licznik /= myNwd
	mianownik /= myNwd
	return [licznik, mianownik]

def sub_frac(frac1, frac2):
	myNwd = 0
	licznik = frac1[0]*frac2[1]-frac1[1]*frac2[0]
	mianownik = frac1[1]*frac2[1]
	myNwd = nwd(licznik,mianownik)
	licznik /= myNwd
	mianownik /= myNwd
	return [licznik, mianownik]

def mul_frac(frac1, frac2):
	myNwd = 0
	licznik = frac1[0]*frac2[0]
	mianownik = frac1[1]*frac2[1]
	myNwd = nwd(licznik, mianownik)
	licznik /= myNwd
	mianownik /= myNwd
	return [licznik, mianownik]

def div_frac(frac1, frac2):
	myNwd = 0
	licznik = frac1[0]*frac2[1]
	mianownik = frac1[1]*frac2[0]
	myNwd = nwd(licznik, mianownik)
	licznik /= myNwd
	mianownik /= myNwd
	return [licznik, mianownik]

def is_positive(frac):
	if(frac[0]*frac[1] > 0): return True
	else:
		return False

def is_zero(frac):
	if(frac[0] == 0): return True
	else: return False

def cmp_frac(frac1, frac2):
	sf = sub_frac(frac1, frac2)
	wynik = sf[1]*sf[0]
	if(wynik < 0): return -1
	elif(wynik > 0): return 1
	else: return 0
	

def frac2float(frac):
	return float(frac[0])/float(frac[1])

