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
        if line != '\n':
            letters.extend([x.strip() for x in line])
            unique = set(letters)
    print(f"unique {unique}")

    return len(unique)

def generate_groups(big_list: List[str]) -> List[str]:
    """
    Yield each group delimited by blank lines
    
    :param big_list: input file imported via readlines
    :return: a few lines
    """
    group = []
    indices = []
    for i,line in enumerate(big_list):
        if line != '\n':
            group.append(line)
            indices.append(i)
        elif line == '\n':
            print(f"group is {group}")
            yield group
            print(f"indices are: {indices}")
            del big_list[min(indices):max(indices)]
            indices = [max(indices)]
            group = []



