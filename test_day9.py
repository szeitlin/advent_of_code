import unittest
from day9 import sum_previous

class TestSumPrevious(unittest.TestCase):

    def test_sum_previous(self):
        xmaslist = list(range(1,26)) + [26] + [49] + [100]
        result = sum_previous(xmaslist)
        assert result == 100

if __name__ == '__main__':
    unittest.main()
