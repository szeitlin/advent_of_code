import unittest
from day2 import parse_input

class TestParseInput(unittest.TestCase):

    def test_simple(self):
        day2_entries = ["1-3 a: abcde",
                        "1-3 b: cdefg",
                        "2-9 c: ccccccccc"]
        result = parse_input(day2_entries)
        assert result == 2

if __name__ == '__main__':
    unittest.main()
