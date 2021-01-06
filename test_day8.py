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

class TestStepper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        steps = """nop +0\n
        acc +1\n
        jmp +4\n
        acc +3\n
        jmp -3\n
        acc -99\n
        acc +1\n
        jmp -4\n
        acc +6"""
        step_list = steps.split('\n')
        cls.ex = Stepper(step_list)

    def test_move(self):
        pass

    def test_do_acc(self):
        accer = Step(6, 'acc -99')
        gohere = self.ex.do_step(accer)
        assert self.ex.acc == -99
        assert gohere == 7

    def test_do_nop(self):
        nopper = Step(1, 'nop +0')
        gohere = self.ex.do_step(nopper)
        assert self.ex.acc == 0
        assert gohere == 2

    def test_do_jump(self):
        jmper = Step(3, 'jmp +4')
        gohere = self.ex.do_step(jmper)
        assert self.ex.acc == 0
        assert gohere == 4

if __name__ == '__main__':
    unittest.main()
