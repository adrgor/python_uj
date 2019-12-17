class StackError:
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return "Stack error: "+self.message


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementow na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise StackError("Full stack")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise StackError("Empty stack")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencje
        return data

import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_empty(self):
        s = Stack(10)
        self.assertEqual(s.is_empty(), True)
        s.push(1)
        s.push(2)
        self.assertEqual(s.is_empty(), False)
        s.pop()
        s.pop()
        self.assertEqual(s.is_empty(), True)

    def test_is_full(self):
        s = Stack(3)
        self.assertEqual(s.is_full(), False)
        s.push(1)
        self.assertEqual(s.is_full(), False)
        s.push(2)
        s.push(3)
        self.assertEqual(s.is_full(), True)

    def test_push_error(self): 
        s = Stack(1)
        s.push(1)
        self.assertRaises(StackError, s.push, 2)
    
    def test_pop_error(self):
        s = Stack(5)
        self.assertRaises(StackError, s.pop)
        s.push(15)
        self.assertEqual(s.pop(), 15)
        self.assertRaises(StackError, s.pop)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy