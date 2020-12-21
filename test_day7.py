import unittest
from day7 import rule_parser, all_rules, find_target_holders, find_holder_holders

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

    def test_all_rules(self):
        rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags."""
        raw_list = [x.lstrip() for x in rules.split('.')]
        rule_list = [x for x in raw_list if x != '']
        assert rule_list[0] == "light red bags contain 1 bright white bag, 2 muted yellow bags"
        assert rule_list[1] == "dark orange bags contain 3 bright white bags, 4 muted yellow bags"
        big_dict = all_rules(rule_list)
        assert len(big_dict.keys()) == 9
        print(big_dict)

class TestFindShinyGold(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags."""
        raw_list = [x.lstrip() for x in rules.split('.')]
        rule_list = [x for x in raw_list if x != '']
        cls.big_dict = all_rules(rule_list)

    def test_find_shiny_gold_holders(self):
        holders = find_target_holders(big_dict=self.big_dict)
        assert len(holders) == 2
        assert set(holders) == {'bright white', 'muted yellow'}

    def test_find_holder_holders(self):
        holders = find_holder_holders(big_dict = self.big_dict)
        print(holders)
        assert len(holders) == 4

if __name__ == '__main__':
    unittest.main()