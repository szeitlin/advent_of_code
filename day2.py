from collections import Counter
from typing import List, Tuple


def parse_input(day2_entries:List[str]) -> int:
    """
    Example: 
    1-3 a: abcde 
    
    The letter 'a' should appear at least 1 time and not more than 3 times
    in the password abcde
    
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


def part2(day2_entries:List[str]) -> int:
    """
    More like what I thought it was originally
    
    Two positions are listed; the letter must be in exactly one (only one!) of those
    
    Example: 
    1-3 a: abcde 
    valid because it has 'a' at position 1 and not at position 3
    
    """
    split_map = [x.split(': ') for x in day2_entries]
    rules = [x[0] for x in split_map]
    times = [x.split()[0].split('-') for x in rules]
    locs = [(int(x[0]), int(x[1])) for x in times]
    letters = [x.split()[1] for x in rules]
    passwords = [x[1] for x in split_map]
    result = 0
    for password,letter,loc in zip(passwords,letters,locs):
        result += check_letter_locs(password,letter,loc)
    return result

def check_letter_locs(password:str, letter:str, loc:Tuple[int,int]) -> int:
    """
    Helper function
    
    :param password: look in this string
    :param letter: for this letter
    :param loc: at these locations
    :return: 1 if valid, 0 if not
    """
    if (password[loc[0]-1]==letter) ^ (password[loc[1]-1]==letter):
        return 1
    else:
        return 0


if __name__ == '__main__':
    with open('day2_entries.txt', 'r') as f:
        day2_entries = f.readlines()
        result = parse_input(day2_entries)
        print(result)
        result2 = part2(day2_entries)
        print(result2)