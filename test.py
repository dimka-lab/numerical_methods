import unittest
import math
from numerical_methods import rectangle_method, bisection
def f(x):
    return -2*x**2 + 3
print(rectangle_method(f, -1, 2, 10)[0])
# help(rectangle_method)
print(bisection(f, 0, 1, 0.001))

class RectangleTest(unittest.TestCase):
    """
    Test rectangle method
    """
    def test_one(self):
        """ Test one """
        result = rectangle_method(f, -1, 2, 10)[0]
        self.assertEqual(result, 3.045)
        print(result)
        

    def test_two(self):
        result = rectangle_method(f, -1, 2, 1)[0]
        print(result)
        self.assertEqual(result, 7.5)

    def test_three(self):
        result = rectangle_method(f, -1, 2, 100)[0]
        print(result)
        self.assertEqual(result, 3.000449999999988)

if __name__ == '__main__':
    unittest.main()
        
