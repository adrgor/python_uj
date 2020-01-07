import random

class QueueError:
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return "Queue error: "+self.message

class RandomQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pelna
        return False

    def insert(self, data):
        self.items.append(data)

    def size(self):
        return len(self.items)

    def remove(self):
        if(len(self.items) > 1):
            r = random.randrange( len(self.items)-1)
            self.items[r], self.items[len(self.items)-1] = self.items[len(self.items)-1], self.items[r]
            return self.items.pop()
        else: return self.items.pop()

    def clear(self):
        self.items = []

q = RandomQueue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.insert(6)

print q.remove()
print q.remove()
print q.remove()
print q.remove()
print q.remove()

print q.is_empty()

print q.remove()

print q.is_empty()
