import unittest
from day1 import report_repair, report_repair_trio

class TestSimpleCase(unittest.TestCase):

    def test_short_list(self):
        ls = [1721,979,366,299,675,1456]
        (one, two) = report_repair(ls)
        assert (one, two) ==  (1721, 299)

class TestHarderCase(unittest.TestCase):

    def test_short_list(self):
        ls = [1721, 979, 366, 299, 675, 1456]
        (one, two, three) = report_repair_trio(ls)
        assert (one, two, three) == (979, 366, 675)

if __name__ == '__main__':
    unittest.main()