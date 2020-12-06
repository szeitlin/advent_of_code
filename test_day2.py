import unittest
from day2 import parse_input, part2

class TestParseInput(unittest.TestCase):

    def test_simple(self):
        day2_entries = ["1-3 a: abcde", #valid
                        "1-3 b: cdefg", #invalid
                        "2-9 c: ccccccccc"] #valid
        result = parse_input(day2_entries)
        assert result == 2

class TestPart2(unittest.TestCase):

    def test_simple(self):
        day2_entries = ["1-3 a: abcde", #valid
                        "1-3 b: cdefg", #example of neither
                        "2-9 c: ccccccccc"] #example of both
        result = part2(day2_entries)
        assert result == 1

    def test_longer(self):
        examples = ["5-10 b: bhbjlkbbbbbbb", #valid
                    "3-4 j: hjvj", #valid
                    "8-9 p: pmljtsttp", #valid
                    "3-4 t: hvtttqhdjmmnbqwbgfs", #invalid (both)
                    "4-6 m: mblwtzmvmdjkkmmtsckm"] #invalid (neither)
        result = part2(examples)
        assert result == 3

if __name__ == '__main__':
    unittest.main()
