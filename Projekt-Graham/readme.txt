Projekt: Implementacja algorytmu Grahama

Pseudokod algorytmu:

Graham(L):
1.  Niech p0 będzie punktem Z L o najmniejszej współrzędnej y, jeżeli kilka punktów
ma taką samą współrzędną y to wybieramy ten o najmniejszej współrzędnej x
2.  Sortujemy kolejne punkty wg. kąta między punktem p0
3.  hull.append(L[0])
4.  hull.append(L[1])
5.  for x=2 to len(L):
        while wektor(hull[-2], hull[-1]) jest na lewo od wektor(hull[-2], L[x]):
            hull.pop()
        hull.append(L[x])
6. return hull

Najbardziej złożoną operacją algorytmu jest sortowanie punktów, dlatego złożoność algorytmu Grahama zależy od wybranego
przez nas algorytmu sortującego. Dla algorytmu quicksort jest to O(nlogn). Reszta operacji zajmuje czas O(n) lub O(1)