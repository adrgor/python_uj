import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "("+ str(self.x) + "," + str(self.y)+")"
    
    def __repr__(self):
        return "Point"+"("+ str(self.x) + "," + str(self.y)+")"

    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        else: 
            return False

    def __ne__(self, other):
        return not self==other
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def test_str_point(self):
        self.assertEqual(Point(1,2).__str__(), "(1,2)")
        self.assertEqual(Point(5,6).__str__(), "(5,6)")
        self.assertEqual(Point(0,-2).__str__(), "(0,-2)")

    def test_repr_point(self):
        self.assertEqual(Point(1,2).__repr__(), "Point(1,2)")
        self.assertEqual(Point(5,6).__repr__(), "Point(5,6)")
        self.assertEqual(Point(0,-2).__repr__(), "Point(0,-2)")

    def test_eq_point(self): 
        self.assertEqual(Point(1,2)==(Point(1,2)), True)
        self.assertEqual(Point(1,2)==(Point(2,5)), False)
        self.assertEqual(Point(0,0)==(Point(6,-5)), False)

    def test_ne_point(self):
        self.assertEqual(Point(1,2)!=(Point(1,2)), False)
        self.assertEqual(Point(1,2)!=(Point(2,5)), True)
        self.assertEqual(Point(0,0)!=(Point(6,-5)), True)

    def test_add_point(self): 
        self.assertEqual( Point(1,2)+(Point(1,2)), Point(2,4) )
        self.assertEqual( Point(1,2)+(Point(0,0)), Point(1,2) )
        self.assertEqual( Point(12,56)+(Point(-12,-122)), Point(0,-66) )

    def test_sub_point(self): 
        self.assertEqual( Point(1,2)-(Point(1,2)), Point(0,0) )
        self.assertEqual( Point(1,2)-(Point(0,0)), Point(1,2) )
        self.assertEqual( Point(12,56)-(Point(-12,-122)), Point(24,178) )

    def test_mul_point(self): 
        self.assertEqual( Point(1,2)*(Point(12,2)), 16 )
        self.assertEqual( Point(12,51)*(Point(2,0)), 24 )
        self.assertEqual( Point(-14,-2)*(Point(24,-14)), -308 )        

    def test_cross_point(self): 
        self.assertEqual( Point(1,2).cross(Point(12,2)), -22 )
        self.assertEqual( Point(12,51).cross(Point(2,0)), -102 )
        self.assertEqual( Point(-14,-2).cross(Point(24,-14)), 244 )

    def test_length_point(self): 
        self.assertEqual( Point(0,2).length(), 2 )
        self.assertEqual( Point(-12,0).length(), 12 )
        self.assertEqual( Point(-5,16).length(), math.sqrt(281) )

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy