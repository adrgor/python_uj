import unittest
import fracs

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
		self.assertEqual(fracs.sub_frac([3,15],[4,16]), [-1,20])

    def test_mul_frac(self):
		self.assertEqual(fracs.mul_frac([3,15],[4,16]), [1,20])

    def test_div_frac(self):
		self.assertEqual(fracs.div_frac([3,15],[4,16]), [4,5])
	
    def test_is_positive(self):
		self.assertEqual(fracs.is_positive([3,15]), True)

    def test_is_zero(self):
		self.assertEqual(fracs.is_zero([0,15]), True)
		
    def test_cmp_frac(self):
		self.assertEqual(fracs.cmp_frac([3,15],[4,16]), -1)

    def test_frac2float(self):
		self.assertEqual(fracs.frac2float([3,15]), 3.0/15.0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy