from points import Point
import math

class Rectangle:
   

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return  "[({},{}),({},{})]".format\
            (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        
        return "Rectangle({},{},{},{})".format\
            (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   
        return self.pt1.__eq__(other.pt1) and\
         self.pt2.__eq__(other.pt2)

    def __ne__(self, other):
        return self.pt1.__ne__(other.pt1) or\
         self.pt2.__ne__(other.pt2)

    def center(self):

        return Point( float(self.pt1.x + self.pt2.x)/2,\
         float(self.pt1.y + self.pt2.y)/2 )

    def area(self):            # pole powierzchni
        a = math.fabs(self.pt1.x - self.pt2.x)
        b = math.fabs(self.pt1.y - self.pt2.y)
        return a*b

    def move(self, x, y):      # przesuniecie o (x, y)
        return Rectangle(self.pt1.x+x, self.pt1.y+y, self.pt2.x+x, self.pt2.y+y)

# Kod testujacy modul.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def test_str_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).__str__(), "[(0,0),(1,1)]" )
        self.assertEqual( Rectangle(5,6,7,8).__str__(), "[(5,6),(7,8)]" )
        self.assertEqual( Rectangle(-12,16,22,0).__str__(), "[(-12,16),(22,0)]" )

    def test_repr_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).__repr__(), "Rectangle(0,0,1,1)" )
        self.assertEqual( Rectangle(5,6,7,8).__repr__(), "Rectangle(5,6,7,8)" )
        self.assertEqual( Rectangle(-12,16,22,0).__repr__(), "Rectangle(-12,16,22,0)" )

    def test_eq_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).__eq__(Rectangle(0,0,1,1)), True )
        self.assertEqual( Rectangle(5,6,7,8).__eq__(Rectangle(5,6,7,8)), True )
        self.assertEqual( Rectangle(-2,2,18,4).__eq__(Rectangle(5,-4,1,6)), False )

    def test_ne_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).__ne__(Rectangle(0,0,1,1)), False )
        self.assertEqual( Rectangle(5,6,7,8).__ne__(Rectangle(5,6,7,8)), False )
        self.assertEqual( Rectangle(-2,2,18,4).__ne__(Rectangle(5,-4,1,6)), True )

    def test_center_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).center(), Point(0.5,0.5) )
        self.assertEqual( Rectangle(2,2,4,4).center(), Point(3,3) )
        self.assertEqual( Rectangle(12,-1,15,8).center(), Point(13.5,3.5) )
        self.assertEqual( Rectangle(-12,-1,-15,-8).center(), Point(-13.5,-4.5) )

    def test_area_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).area(), 1 )
        self.assertEqual( Rectangle(2,2,4,4).area(), 4 )
        self.assertEqual( Rectangle(-5,16,11,8).area(), 128 )

    def test_move_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).move(1,1), Rectangle(1,1,2,2) )
        self.assertEqual( Rectangle(16,12,-5,8).move(2,-6), Rectangle(18,6,-3,2) )
        self.assertEqual( Rectangle(0,15,-9,-8).move(-7,-2), Rectangle(-7,13,-16,-10) )

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy