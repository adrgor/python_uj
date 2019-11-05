def odwracanie(L, left, right):
    while(left<right):
        L[left], L[right] = L[right], L[left]
        left = left+1
        right = right-1

L = [1,2,3,4,5,6,7,8,9]
odwracanie(L, 0 , 5)
print(L)
