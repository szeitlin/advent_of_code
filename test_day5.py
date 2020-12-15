import unittest
from day5 import plane_seat, get_row, get_column

class TestExamples(unittest.TestCase):

    def test_get_row(self):
        ticket = "FBFBBFFRLR"
        rows = ticket[0:7]
        row = get_row(rows)
        assert row == 44

    def test_get_column(self):
        ticket = "FBFBBFFRLR"
        cols = ticket[7:]
        col = get_column(cols)
        assert col == 5

class TestWholeExamples(unittest.TestCase):

    def test_get_seat(self):
        ticket = "FBFBBFFRLR"
        seat_id = plane_seat(ticket)
        assert seat_id == 357

    def test_get_seat2(self):
        ticket = "BFFFBBFRRR"
        seat_id = plane_seat(ticket)
        assert seat_id == 567

    def test_get_seat3(self):
        ticket = "FFFBBBFRRR"
        seat_id = plane_seat(ticket)
        assert seat_id == 119

    def test_get_seat4(self):
        ticket = "BBFFBBFRLL"
        seat_id = plane_seat(ticket)
        assert seat_id == 820


if __name__ == '__main__':
    unittest.main()