import zadanie1
import random
import time
import copy

def swap(L, left, right):
    L[left], L[right] = L[right], L[left]

def bubblesort(L, left, right):
    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j+1]:
                swap(L, j+1, j)

def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podzialu
    pivot = left                      # przesun do L[left]
    for i in range(left + 1, right + 1):   # podzial
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtworz element podzialu
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2   # wyznaczanie srodka 
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie

def merge(L, left, middle, right):
    """laczenie posortowanych sekwencji."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:   # mniejsze lub rowne
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa czesc moze miec elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left +1):
        L[left + i] = T[i]


# N = 10**2
numbers = zadanie1.rand(100)
print "Dla N=10**2"
start = time.time()
bubblesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu bubblesort dla tablicy N=10**2 to "+str(end-start)+" s"

start = time.time()
quicksort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu quicksort dla tablicy N=10**2 to "+str(end-start)+" s"

start = time.time()
mergesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu mergesort dla tablicy N=10**2 to "+str(end-start)+" s"

# N = 10**3
numbers = zadanie1.rand(1000)
print "Dla N=10**3"
start = time.time()
bubblesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu bubblesort dla tablicy N=10**3 to "+str(end-start)+" s"

start = time.time()
quicksort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu quicksort dla tablicy N=10**3 to "+str(end-start)+" s"

start = time.time()
mergesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu mergesort dla tablicy N=10**3 to "+str(end-start)+" s"

# N = 10**4
numbers = zadanie1.rand(10000)
print "Dla N=10**4"
start = time.time()
bubblesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu bubblesort dla tablicy N=10**4 to "+str(end-start)+" s"

start = time.time()
quicksort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu quicksort dla tablicy N=10**4 to "+str(end-start)+" s"

start = time.time()
mergesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu mergesort dla tablicy N=10**4 to "+str(end-start)+" s"

# N = 10**5
numbers = zadanie1.rand(100000)
print "Dla N=10**5"
""" Bubblesort za bardzo opoznial dzialanie algorytmu dla tak duzej list dluzszych od 10**4, dlatego potanowilem go wykomentowac """
# start = time.time()
# bubblesort(copy.copy(numbers), 0, len(numbers)-1)
# end = time.time()
# print "Czas dzialania algorytmu bubblesort dla tablicy N=10**5 to "+str(end-start)+" s"

start = time.time()
quicksort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu quicksort dla tablicy N=10**5 to "+str(end-start)+" s"

start = time.time()
mergesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu mergesort dla tablicy N=10**5 to "+str(end-start)+" s"

# N = 10**6
numbers = zadanie1.rand(1000000)
print "Dla N=10**6"
# start = time.time()
# bubblesort(copy.copy(numbers), 0, len(numbers)-1)
# end = time.time()
# print "Czas dzialania algorytmu bubblesort dla tablicy N=10**6 to "+str(end-start)+" s"

start = time.time()
quicksort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu quicksort dla tablicy N=10**6 to "+str(end-start)+" s"

start = time.time()
mergesort(copy.copy(numbers), 0, len(numbers)-1)
end = time.time()
print "Czas dzialania algorytmu mergesort dla tablicy N=10**6 to "+str(end-start)+" s"

