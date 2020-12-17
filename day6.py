from typing import List

def count_yes(answers:List[str]) -> int:
    """
    Read answers from each group as a list of strings
    Count the number of unique letters that appear per group
    Then sum them up
    
    :param answers: one letter per answer
    :return: total number of unique letters seen
    """
    letters = []
    unique = None
    for line in answers:
        letters.extend([x.strip() for x in line])
        unique = set(letters)
        print(unique)

    return len(unique)

def generate_groups(big_list: List[str]) -> List[str]:
    """
    Yield each group delimited by blank lines
    
    :param big_list: input file imported via readlines
    :return: a few lines
    """
    j = 0 #last line to keep
    for i,line in enumerate(big_list):
        if line == '\n':
            j += i
            yield big_list[0:j]

