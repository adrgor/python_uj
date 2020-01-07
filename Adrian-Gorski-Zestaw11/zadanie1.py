import random

def rand(n):
    numbers = []
    for x in range(n):
        numbers.append(x)
    random.shuffle(numbers)
    return numbers

def nearlySort(n):
    numbers = []
    for x in range(n):
        numbers.append(x)
    
    for x in range(n-1):
        if random.random() < 0.5:
            numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
    return numbers

def nearlyRev(n):
    numbers = []
    for x in range(n-1, -1, -1):
        numbers.append(x)
    
    for x in range(n-1):
        if random.random() < 0.5:
            numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
    return numbers

def gauss(n):
    random.seed(1)
    numbers = []
    for x in range(n):
        numbers.append(random.gauss(0,1))
    return numbers

def fromSet(n, set):
    numbers = []
    for x in range(n):
        numbers.append(random.choice(set))
    return numbers