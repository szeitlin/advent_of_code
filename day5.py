
def plane_seat(seat:str) -> int:
    """
    Ticket looks like this: FBFBBFFRLR
    
    There are rows 0 through 127
    F means lower half
    B means upper half
    
    Then there are columns 0 through 7
    L means lower half
    R means upper half
    
    seat ID: row * 8 + column
    
    :param seat: string
    :return: seat ID 
    """
    ticket = seat.strip()
    rows = ticket[0:7]
    row = get_row(rows)
    print(f"row is {row}")
    cols = ticket[7:]
    col = get_column(cols)
    print(f"col is {col}")
    seat_id = row * 8 + col
    return seat_id


def get_row(rows:str) -> int:
    """
    This is hacky but works so far
    
    Just look at the F and B parts
    
    There are rows 0 through 127
    F means lower half
    B means upper half
    
    :param rows: list of F and B cuts to make
    :return: row
    """
    all_rows = list(range(128))
    for char in rows[0:-1]:
        if char == 'F':
            all_rows = all_rows[0:len(all_rows)//2]
        elif char == 'B':
            all_rows = all_rows[len(all_rows)//2:]

    if rows[-1] == 'F':
        return all_rows[0]
    elif rows[-1] == 'B':
        return all_rows[1]

def get_column(cols:str) -> int:
    """
    Try the same logic as before, but seems dumb to repeat it
    
    There are columns 0 through 7
    L means lower half
    R means upper half
    
    :param cols: string with only R or L cuts to make
    :return: col
    """
    all_cols = list(range(8))
    for char in cols[0:-1]:
        if char == 'R':
            all_cols = all_cols[len(all_cols)//2:]
        elif char == 'L':
            all_cols = all_cols[0:len(all_cols)//2]
        print(all_cols)

    if cols[-1] == 'R':
        return all_cols[1]
    elif cols[-1] == 'L':
        return all_cols[0]

if __name__ == '__main__':
    with open('day5_input.txt', 'r') as f:
        seats = f.readlines()
        seat_ids = []
        for seat in seats:
            print(seat)
            seat_ids.append(plane_seat(seat))
            print(max(seat_ids))
