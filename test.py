#import factions module from standard library
from fractions import Fraction

#testing sum()

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

#Add test with an Assertion expecting incorrect value to see test result examples 
#with incorrect value:
def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


#Command line entry point. The command line withh call this to 
#execute the test runner
if __name__ == '__main__':
    unittest.main()

