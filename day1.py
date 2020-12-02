from typing import List, Tuple

def report_repair(entries:List[int]) -> Tuple[int, int]:
    """
    Find the pair of numbers that sums to 2020, and then multiply them
    
    :param entries: this is a long list of integers
    :return: result of the multiplication 
    """
    total = 2020
    one, two = 0, 0
    for i, item in enumerate(entries):
        one = item
        while (total > 0) and (i < len(entries) - 1):
            total = total - one
            total = total - entries[i + 1]
            if total == 0:
                two = entries[i+1]
                return (one, two)
            else:
                i = i + 1
                total = 2020

if __name__ == '__main__':
    with open('entries.txt', 'r') as f:
        entries = [int(x) for x in f.readlines()]
        (one,two) = report_repair(entries)
        print(one * two)
