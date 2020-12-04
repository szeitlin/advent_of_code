from collections import Counter
from typing import List


def parse_input(day2_entries:List[str]) -> int:
    """
    Example: 
    1-3 a: abcde 
    
    The letter 'a' should appear at least 1 time and not more than 3 times
    in the password abcde
    
    :param list: 
    :return: 
    """
    split_map = [x.split(': ') for x in day2_entries]
    rules = [x[0] for x in split_map]
    times = [x.split()[0].split('-') for x in rules]
    num_times = [(int(x[0]), int(x[1])) for x in times]
    letters = [x.split()[1] for x in rules]
    passwords = [x[1] for x in split_map]
    counted = [count_letter_in_password(password,letter) for password,letter in zip(passwords,letters)]
    valid = [(counted >= x[0]) and (counted <= x[1]) for counted, x in zip(counted, num_times)]
    return sum(valid)


def count_letter_in_password(password:str, letter:str) -> int:
    """
    Helper function 
    """
    counts = Counter(password)
    return counts[letter]





if __name__ == '__main__':
    with open('day2_entries.txt', 'r') as f:
        day2_entries = f.readlines()
        result = parse_input(day2_entries)
        print(result)