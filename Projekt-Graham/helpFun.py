from point import Point
from random import random, randint
# from isSorted import isSorted

# Generowanie listy punktow
def genPoints(od, do, x):
    return[Point(randint(od, do+1), randint(od, do+1)) for _ in range(x)]
    
    
# Znajdowanie punktu o najmniejszej wartosci y
def findMinY(points):
	y = min( [punkt.y for punkt in points] )
	x = None
	for point in points:
		if point.y == y and (x==None or point.x < x.x): x = point
	return x

def swap(L, left, right):
    L[left], L[right] = L[right], L[left]

def quicksort(L, left, right, anchor):
    if left >= right:   return

    pivot = partition(L, left, right, anchor)
    # pivot jest na swoim miejscu.
    quicksort(L, left, pivot - 1, anchor)
    quicksort(L, pivot + 1, right, anchor)
    

def partition(L, left, right, anchor):
    """Zwraca indeks elementu rozdzielajacego."""
    # Element rozdzielajacy to ostatni z prawej,
    # dlatego na koncu trzeba go przerzucic do srodka.
    # Bedzie on na docelowej pozycji ze wzgledu na sortowanie.
    x = L[right]   # element rozdzielajacy
    i = left
    for j in range(left, right):
        if L[j].angle_for_anchor(anchor) <= x.angle_for_anchor(anchor):
            swap(L, i, j)
            i += 1
    swap(L, i, right)
    return i


def det(p,q,r):
    return (q.x-p.x)*(r.y-p.y) \
			-(q.y-p.y)*(r.x-p.x)

def find_hull(L):   # Znajduje i zwraca otoczke wypukla
    anchor = findMinY(L)
    L.remove(anchor)
    quicksort(L, 0, len(L)-1, anchor)
    hull = [anchor, L[0]]
    for x in L:
        while len(hull)>1 and det(hull[-2], hull[-1], x) <= 0:
            hull.pop()
        hull.append(x)
    if det(hull[-2], hull[-1], anchor) == 0 and len(hull)>2:
        hull.pop()
    return hull