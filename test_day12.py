import re
import unittest

class TestInstructions(unittest.TestCase):

    def test_simple(self):
        instr = 'F10'
        step_dir = re.match('^(\D)', instr).group()
        step_size = int(re.search('(\d+)', instr).group())
        assert step_dir == 'F'
        assert step_size == 10

if __name__ == '__main__':
    unittest.main()


