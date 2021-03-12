import re
import unittest
from day_12 import manhattan_distance, move_ship

class TestInstructions(unittest.TestCase):

    def test_simple(self):
        instr = 'F10'
        step_dir = re.match('^(\D)', instr).group()
        step_size = int(re.search('(\d+)', instr).group())
        assert step_dir == 'F'
        assert step_size == 10

class TestMoveShip(unittest.TestCase):

    def test_move_ship_north(self):
        start = [0,0]
        instr= 'N3'
        moved = move_ship(start, instr)
        assert moved == [0,3]

    def test_move_ship_west(self):
        start = [0,0]
        instr='W11'
        moved = move_ship(start, instr)
        assert moved == [-11, 0]

class TestManhattanDistance(unittest.TestCase):

    def test_manhattan_distance(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()


