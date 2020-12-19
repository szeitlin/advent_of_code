import unittest
from day6 import count_yes, generate_groups

class TestSimple(unittest.TestCase):

    def test_count_yes(self):
        answers = ['abcx','abcy', 'abcz']
        total = count_yes(answers)
        assert total == 6

class TestGenerateGroups(unittest.TestCase):

    def test_generate_groups(self):
        big_list = ["abc",
                    "\n",
                    "a\n",
                    "b\n",
                    "c\n",
                    "\n",
                    "ab\n",
                    "ac\n",
                    "\n",
                    "a\n",
                    "a\n",
                    "a\n",
                    "a\n",
                    "\n",
                    "b",]
        grouper = generate_groups(big_list)
        group1 = next(grouper)
        assert group1 == ["abc", '\n']

    def test_count_groups(self):
        big_list = ["abc",
                    "\n",
                    "a\n",
                    "b\n",
                    "c\n",
                    "\n",
                    "ab\n",
                    "ac\n",
                    "\n",
                    "a\n",
                    "a\n",
                    "a\n",
                    "a\n",
                    "\n",
                    "b", ]
        grouper = generate_groups(big_list)
        total = 0
        while grouper:
            try:
                group = next(grouper)
                total += count_yes(group)
                print(total)
            except StopIteration:
                break
        assert total == 11

if __name__ == '__main__':
    unittest.main()
