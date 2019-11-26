from points import Point
import math
import sys

class Rectangle:
   

    def __init__(self, x1, y1, x2, y2):
        if(x1<x2 and y1<y2):
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError

    def __str__(self):
        return  "[({},{}),({},{})]".format\
            (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        
        return "Rectangle({},{},{},{})".format\
            (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   
        return self.pt1==other.pt1 and\
         self.pt2==other.pt2

    def __ne__(self, other):
        return self.pt1!=other.pt1 or\
         self.pt2!=other.pt2

    def center(self):

        return Point( float(self.pt1.x + self.pt2.x)/2,\
         float(self.pt1.y + self.pt2.y)/2 )

    def area(self):            # pole powierzchni
        a = math.fabs(self.pt1.x - self.pt2.x)
        b = math.fabs(self.pt1.y - self.pt2.y)
        return a*b

    def move(self, x, y):      # przesuniecie o (x, y)
        try:
            return Rectangle(self.pt1.x+x, self.pt1.y+y, self.pt2.x+x, self.pt2.y+y)
        except ValueError:
            sys.stderr.write("Couldn't create a rectangle")
            return None


    def intersection(self, other):
        try:
            return Rectangle( max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), \
                                min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        except ValueError:
            sys.stderr.write("There is no intersection")
            return None

    def cover(self, other):
        try:
            return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), \
                                max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        except ValueError:
            return None

    def make4(self):
        dlugosc = math.sqrt(self.pt1.x**2 + self.pt2.x**2)
        wysokosc = math.sqrt(self.pt1.y**2 + self.pt2.y**2)
        
        r1 = Rectangle(self.pt1.x, self.pt1.y, self.pt1.x+dlugosc/2, self.pt1.y+wysokosc/2)
        r2 = Rectangle(self.pt1.x+dlugosc/2, self.pt1.y, self.pt2.x, self.pt1.y+wysokosc/2)
        r3 = Rectangle(self.pt1.x, self.pt1.y+wysokosc/2, self.pt1.x+dlugosc/2, self.pt2.y)
        r4 = Rectangle(self.pt1.x+dlugosc/2, self.pt1.y+wysokosc/2, self.pt2.x, self.pt2.y)
        
        return [r1,r2,r3,r4]

# Kod testujacy modul.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        pass


    def test_str_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).__str__(), "[(0,0),(1,1)]" )
        self.assertEqual( Rectangle(5,6,7,8).__str__(), "[(5,6),(7,8)]" )
        self.assertEqual( Rectangle(-12,0,22,16).__str__(), "[(-12,0),(22,16)]" )

    def test_repr_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).__repr__(), "Rectangle(0,0,1,1)" )
        self.assertEqual( Rectangle(5,6,7,8).__repr__(), "Rectangle(5,6,7,8)" )
        self.assertEqual( Rectangle(-12,0,22,16).__repr__(), "Rectangle(-12,0,22,16)" )

    def test_eq_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1)==(Rectangle(0,0,1,1)), True )
        self.assertEqual( Rectangle(5,6,7,8)==(Rectangle(5,6,7,8)), True )
        self.assertEqual( Rectangle(-2,2,18,4)==(Rectangle(0,-4,1,6)), False )

    def test_ne_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1)!=(Rectangle(0,0,1,1)), False )
        self.assertEqual( Rectangle(5,6,7,8)!=(Rectangle(5,6,7,8)), False )
        self.assertEqual( Rectangle(-2,2,18,4)!=(Rectangle(5,-4,6,6)), True )

    def test_center_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).center(), Point(0.5,0.5) )
        self.assertEqual( Rectangle(2,2,4,4).center(), Point(3,3) )
        self.assertEqual( Rectangle(12,-1,15,8).center(), Point(13.5,3.5) )

    def test_area_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).area(), 1 )
        self.assertEqual( Rectangle(2,2,4,4).area(), 4 )

    def test_move_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).move(1,1), Rectangle(1,1,2,2) )
        self.assertEqual( Rectangle(16,12,25,18).move(2,-6), Rectangle(18,6,27,12) )
        self.assertEqual( Rectangle(0,15,3,18).move(-7,-2), Rectangle(-7,13,-4,16) )

    def test_intersection_rectangle(self):
        self.assertEqual( Rectangle(0,0,1,1).intersection( Rectangle(0,0,2,2) ), Rectangle(0,0,1,1) )
        self.assertEqual( Rectangle(0,0,1,1).intersection( Rectangle(2,2,3,3) ), None )

    def test_cover_rectangle(self):
        self.assertEqual( Rectangle(0,0,5,5).cover( Rectangle(1,1,6,6) ), Rectangle(0,0,6,6) )
        self.assertEqual( Rectangle(1,2,3,4).cover( Rectangle(5,6,7,8) ), Rectangle(1,2,7,8) )

    def test_make4_rectangle(self):
        self.assertEqual( Rectangle(0,0,2,2).make4(), [Rectangle(0,0,1,1),Rectangle(1,0,2,1),Rectangle(0,1,1,2),Rectangle(1,1,2,2)] )
         


    def tearDown(self): pass

if __name__ == '__main__':
    
    unittest.main()     # uruchamia wszystkie testy

