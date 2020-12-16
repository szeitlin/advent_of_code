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
        row = get_row(ticket[0:7])
        print(row)
        assert row == 14
        col = get_column(ticket[7:])
        print(col)
        assert col == 7
        seat_id = plane_seat(ticket)
        assert seat_id == 119

    def test_get_seat4(self):
        ticket = "BBFFBBFRLL"
        row = get_row(ticket[0:7])
        print(row)
        assert row == 102
        col = get_column(ticket[7:])
        print(col)
        assert col == 4
        seat_id = plane_seat(ticket)
        assert seat_id == 820


if __name__ == '__main__':
    unittest.main()