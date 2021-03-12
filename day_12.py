import operator
import re

def move_ship(start:list, instr:str) -> list:
    """
    Assuming a coordinate system of (-inf, inf) on the x and (-inf, inf) on the y
    
    :param start: wherever the ship is now, before executing a step
    :param instr: looks like NSEW, LR, or F (forward), plus a number

    
    :return: new coordinates
    """
    #Let's assume East is + and West is -
    #Let's also assume North is + and South is -

    step_dir = re.match('^(\D)', instr).group()
    step_size = int(re.search('(\d+)', instr).group())

    direction_map = {'N': operator.add(start[1], step_size),
                     'S': operator.sub(start[1], step_size),
                      'E': operator.add(start[0], step_size),
                        'W': operator.sub(start[0], step_size)}

    step = direction_map[step_dir]
    print(step)

    result = start

    if step_dir in 'NS':
        print('North or South')
        result = [start[0], step]
        print(result)

    elif step_dir in 'EW':
        print('East or West')
        result = [step, start[1]]
        print(result)

    return result

#todo: write functions for handling facing, left and right rotations
#Only LR (left and right) can change the direction the ship is facing


def manhattan_distance(start:list, end:list) -> int:
    """
    sum of the absolute values of east/west and north/south position
    
    abs(x2-x1) + abs(y2-y1)
    
    :param start: starting location
    :param end: final location, after executing all steps in the sequence
    :return: distance
    """
    y = operator.abs(end[1] - start[1])
    x = operator.abs(end[0] - start[0])
    return x + y

