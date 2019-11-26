import math
from points import Point

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return math.pi*(self.radius**2)

    def move(self, x, y):     # przesuniecie o (x, y)
        return Circle(self.pt.x+x, self.pt.y+y, self.radius)

    def contains(self, other):
        d = math.sqrt((other.pt.x-self.pt.x)**2 + (other.pt.y - self.pt.y)**2)
        return self.radius > (d+other.radius)


    def cover(self, other):   # okrag pokrywajacy oba
        if(self.contains(other)): return self
        else:
            x = (self.pt.x+other.pt.x)/2
            y = (self.pt.y+other.pt.y)/2
            r = self.radius + (math.sqrt((self.pt.x-x)**2 + (self.pt.y-y)**2))
            return Circle(x,y,r)

# Kod testujacy modul.

import unittest

class TestCircle(unittest.TestCase):

    def test_repr_circle(self):
        self.assertEqual(Circle(0,0,5).__repr__(), "Circle(0, 0, 5)")
        self.assertEqual(Circle(3,-13,8).__repr__(), "Circle(3, -13, 8)")

    def test_eq_circle(self):
        self.assertEqual(Circle(0,0,5) == Circle(0,0,5), True)
        self.assertEqual(Circle(1,2,3) == Circle(2,3,4), False)

    def test_ne_circle(self):
        self.assertEqual(Circle(0,0,5) != Circle(0,0,5), False)
        self.assertEqual(Circle(1,2,3) != Circle(2,2,3), True)

    def test_area_circle(self):
        self.assertEqual(Circle(0,0,5).area(), math.pi*25)
        self.assertEqual(Circle(-1,25,2).area(), math.pi*4)

    def test_move_circle(self):
        self.assertEqual(Circle(0,0,5).move(2,-2), Circle(2,-2,5))
        self.assertEqual(Circle(50,-6,5).move(-12,16), Circle(38,10,5))
    
    def test_contains_test(self):
        self.assertEqual(Circle(0,0,50).contains(Circle(1,1,5)), True)
        self.assertEqual(Circle(0,0,5).contains(Circle(25,-30,1)), False)

    def test_cover_circle(self):
        self.assertEqual(Circle(0,0,5).cover(Circle(10,0,5)), Circle(5,0,10))
        self.assertEqual(Circle(0,0,50).cover(Circle(1,1,5)), Circle(0,0,50))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy