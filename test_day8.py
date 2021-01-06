import unittest
from day8 import Step, Stepper

class TestStep(unittest.TestCase):

    def test_step_single_digit(self):
        ex = Step(1, 'nop +0')
        assert ex.index == 1
        assert ex.action == 'nop'
        assert ex.size == 0

    def test_step_multi_digit(self):
        ex = Step(6, 'acc -99')
        assert ex.index == 6
        assert ex.action == 'acc'
        assert ex.size == -99

if __name__ == '__main__':
    unittest.main()
