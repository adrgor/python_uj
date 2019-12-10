class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   


class SingleList:
    

    def __init__(self):
        self.length = 0 
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):    
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:           
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node): 
        if self.length == 0:
            self.head = self.tail = node
        else:                   
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):      
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  
        self.length -= 1
        return node   

    def remove_tail(self):
        if self.length == 0: raise ValueError("pusta lista")
        if self.length == 1:
            return_node = self.head
            self.length = self.length - 1
            self.head = None
            return return_node

        node = self.head
        while(node.next.next != None):
            node = node.next
        return_node = node.next
        node.next = None
        tail = node
        self.length = self.length - 1
        return return_node

    def merge(self, other):
        self.tail.next = other.head
        self.tail = other.tail
        self.length = self.length + other.length

    def clear(self): 
        self.head.next = None
        self.head = None
        self.tail = None
        self.length = 0


listA = SingleList()
listA.insert_tail(Node(1))
listA.insert_tail(Node(2))
listA.insert_tail(Node(3))
listA.insert_tail(Node(4))
listA.insert_tail(Node(5))


listB = SingleList()
listB.insert_tail(Node(6))
listB.insert_tail(Node(7))
listB.insert_tail(Node(8))
listB.insert_tail(Node(9))
listB.insert_tail(Node(10))

listA.merge(listB)
while listA.count()>0:
    print(listA.remove_tail())

listB.clear()
print(listB.count())