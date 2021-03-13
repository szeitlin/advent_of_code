import re
import unittest
from day_12 import Ship

class TestInstructions(unittest.TestCase):

    def test_simple(self):
        instr = 'F10'
        step_dir = re.match('^(\D)', instr).group()
        step_size = int(re.search('(\d+)', instr).group())
        assert step_dir == 'F'
        assert step_size == 10

class TestMoveShip(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ship = Ship()

    def test_move_ship_north(self):
        instr= 'N3'
        moved = self.ship.move_ship(instr)
        assert moved == [0,3]

    def test_move_ship_west(self):
        start = [0,0]
        instr='W11'
        moved = self.ship.move_ship(instr)
        assert moved == [-11, 0]

class TestRotate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ship = Ship()

    def test_rotate_left(self):
        step_dir = 'L'
        step_size = 5
        facing = self.ship.rotate(step_dir, step_size)
        assert facing == 'N'

class TestManhattanDistance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ship = Ship()

    def test_manhattan_distance(self):
        end = [17, 8]
        dist = self.ship.manhattan_distance(end)
        assert dist == 25

class TestExecuteMovements(unittest.TestCase):

    def test_execute_movements(self):
        instr_list = ['F10', 'N3', 'F7', 'R90', 'F11']
        
if __name__ == '__main__':
    unittest.main()


