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
            chars = [x.strip() for x in line]
            keep = [x for x in chars if x!='']
            letters.extend(keep)
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
    copy_big_list = big_list[:]
    for i,line in enumerate(copy_big_list):
        indices.append(i)
        if line != '\n':
            group.append(line)
        elif line == '\n':
            print(f"group is {group}")
            yield group
            print(f"indices are: {indices}")
            del big_list[min(indices):max(indices)-1]
            indices = [max(indices)]
            group = []
    yield(group)


if __name__ == '__main__':
    with open('day6_input.txt', 'r') as f:
        lines = f.readlines()
        grouper = generate_groups(lines)
        total = 0
        while grouper:
            try:
                group = next(grouper)
                total += count_yes(group)
                print(total)
            except StopIteration:
                break