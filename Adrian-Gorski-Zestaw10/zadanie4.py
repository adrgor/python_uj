class QueueError:
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return "Queue error: "+self.message


class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise QueueError("Full queue")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise QueueError("Empty queue")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencje
        self.head = (self.head + 1) % self.n
        return data

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_empty(self):
        q = Queue(10)
        self.assertEqual(q.is_empty(), True)
        q.put(1)
        q.put(2)
        self.assertEqual(q.is_empty(), False)
        q.get()
        q.get()
        self.assertEqual(q.is_empty(), True)

    def test_is_full(self):
        q = Queue(3)
        self.assertEqual(q.is_full(), False)
        q.put(1)
        self.assertEqual(q.is_full(), False)
        q.put(2)
        q.put(3)
        self.assertEqual(q.is_full(), True)

    def test_push_error(self): 
        q = Queue(1)
        q.put(1)
        self.assertRaises(QueueError, q.put, 2)
    
    def test_get_error(self):
        q = Queue(5)
        self.assertRaises(QueueError, q.get)
        q.put(15)
        self.assertEqual(q.get(), 15)
        self.assertRaises(QueueError, q.get)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy