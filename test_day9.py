import unittest
from day9 import sum_previous

class TestSumPrevious(unittest.TestCase):

    def test_sum_previous(self):
        xmaslist = list(range(1,26)) + [26] + [49] + [100]
        result = sum_previous(xmaslist)
        assert result == 100

    def test_example(self):
        raw = """35
        20
        15
        25
        47
        40
        62
        55
        65
        95
        102
        117
        150
        182
        127
        219
        299
        277
        309
        576"""
        xmaslist = [int(x) for x in raw.split()]
        print(xmaslist)
        result = sum_previous(xmaslist, n=5)
        assert result == 127

if __name__ == '__main__':
    unittest.main()
