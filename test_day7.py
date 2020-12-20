import unittest
from day7 import rule_parser

class TestRuleParser(unittest.TestCase):

    def test_compound_lists(self):
        test1 = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        parsed = rule_parser(test1)
        assert parsed == {'light red':['1 bright white bag', '2 muted yellow bags.']}
        test2 = "dark orange bags contain 3 bright white bags, 4 muted yellow bags."
        parsed2 = rule_parser(test2)
        assert parsed2 == {'dark orange': ['3 bright white bags', '4 muted yellow bags.']}
        test3 = "pale olive bags contain 3 striped blue bags, 5 faded magenta bags, 3 light white bags."
        parsed3 = rule_parser(test3)
        assert parsed3 == {'pale olive': ['3 striped blue bags', '5 faded magenta bags', '3 light white bags.']}
        test4 = "faded blue bags contain no other bags."
        parsed4 = rule_parser(test4)
        assert parsed4 == {'faded blue': ['no other bags.']}

if __name__ == '__main__':
    unittest.main()