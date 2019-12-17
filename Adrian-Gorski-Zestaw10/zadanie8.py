import random

class QueueError:
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return "Queue error: "+self.message

class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def insert(self, data):
        if self.is_full():
            raise QueueError("Pelna kolejka")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise QueueError("Pusta kolejka")
        r = random.randint(self.head,self.tail-1)
        head_value = self.items[self.head]
        self.items[self.head] = self.items[r]
        self.items[r] = head_value
        return self.__get()

    def __get(self):
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencje
        self.head = (self.head + 1) % self.n
        return data

    def clear(self):
        self.head = 0
        self.tail = 0

q = RandomQueue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

print q.remove()
print q.remove()
print q.remove()
print q.remove()

print q.is_empty()

print q.remove()

print q.is_empty()

