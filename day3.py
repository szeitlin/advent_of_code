
def count_trees(lines) -> int:
    """
    Tobaggan traveling!
    
    Open squares are '.' and trees are '#'
    Go over 3, down 1
    Count how many trees you encounter
    
    :param lines: list of strings
    :return: count of how many trees we landed on
    """
    trees = 0
    right = 0
    width = len(lines[0]) #length of one line
    for x in lines[1:]:
        right += 3  # over 3
        right = right % width #wrap around
        try:
            if x[right] == '#':
                trees += 1
        except IndexError as e:
            print('hit index error')
        print(trees)
    return trees

if __name__ == '__main__':

    with open('day3_input.txt', 'r') as f:
        inputmatrix = f.readlines()
    trees = count_trees(inputmatrix)