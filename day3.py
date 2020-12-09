import math

def prep_input(inputmatrix:list) -> list:
    """
    Seems like they want you to replicate the input several fold,
    since the initial input they give is very narrow, 
    but then the examples they show are wider
    :param inputmatrix: narrow input
    :return: wider input
    """
    #how wide to make it? it's a triangle
    length = len(inputmatrix) #number of rows
    #y = mx + b where b is 0, solve for x
    replicates = int(length//3) #this has to be an int
    wider = [replicates * x for x in inputmatrix]
    return wider



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
    for i, x in enumerate(lines):
        i += 1  # down 1
        right += 3  # over 3
        try:
            if lines[i][right] == '#':
                trees += 1
        except IndexError as e:
            print('hit index error')
        print(trees)
    return trees

if __name__ == '__main__':

    with open('day3_input.txt', 'r') as f:
        inputmatrix = f.readlines()
    lines = prep_input(inputmatrix)
    trees = count_trees(lines)