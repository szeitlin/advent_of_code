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
    def setUp(cls):
        steps = """nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6"""
        raw_step_list = steps.split('\n')
        step_list = [x.lstrip() for x in raw_step_list]
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
        assert gohere == 7

if __name__ == '__main__':
    unittest.main()
