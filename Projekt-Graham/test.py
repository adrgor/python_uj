import unittest
from point import Point
from helpFun import find_hull

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.list_test_1 = [Point(0,0), Point(0,2), Point(0,4),
                     Point(2,0), Point(2,2), Point(2,4),
                     Point(4,0), Point(4,2), Point(4,4)]
        self.list_test_2 = [Point(0,0), Point(2,0), Point(4,0), Point(6,0)]
        self.list_test_3 = [Point(2,0), Point(1,0), Point(3,1), Point(2,2), Point(4,3), Point(4,2), Point(3,2), Point(1,4)]

    def test_graham(self): 
        self.assertEqual(find_hull(list(self.list_test_1)), [self.list_test_1[0], self.list_test_1[6], self.list_test_1[8], self.list_test_1[2]])
        self.assertEqual(find_hull(list(self.list_test_2)), [self.list_test_2[0], self.list_test_2[3]])
        self.assertEqual(find_hull(list(self.list_test_3)), 
            [self.list_test_3[1], self.list_test_3[0],self.list_test_3[5], self.list_test_3[4], self.list_test_3[7]])

    

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy