x = 1,25,12,14,2,5
y = 1,8,12,23,25,5,2

l=set()

# Podpunkt a)
print("\nPodpunkt a)")
for i in range(len(x)):
    for j in range(len(y)):
        if(x[i]==y[j]): 
            l.add(y[j])

print(l)

# Podpunkt b)
print("\nPodpunkt b)")
l.clear()
for i in range(len(x)):
    l.add(x[i])
for i in range(len(y)):
    l.add(y[i])

print(l)