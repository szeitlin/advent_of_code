import operator
import re
from typing import Tuple

def move_ship(start:Tuple[int, int], facing:str, instr:str) -> Tuple[int, int]:
    """
    Assuming a coordinate system of (-inf, inf) on the x and (-inf, inf) on the y
    
    :param start: wherever the ship is now, before executing a step
    :param facing: whichever way the ship is facing now, before executing a step
    :param instr: looks like NSEW, LR, or F (forward), plus a number
    Only LR (left and right) can change the direction the ship is facing
    
    :return: new coordinates
    """
    #Let's assume East is + and West is -
    #Let's also assume North is + and South is -

    #todo: probably have to use a regex here
    step_dir = re.match('^(\D)', instr).group()
    step_size = int(re.search('(\d+)', instr).group())

    direction_map = {'N': operator.add(start[1], step_size),
                     'S': operator.sub(start[1], step_size),
                      'E': operator.add(start[0], step_size),
                        'W': operator.sub(start[0], step_size),
                        'L':,
                        'R':}

#todo: write functions for left and right rotations

def manhattan_distance(start:Tuple[int,int], end:Tuple[int,int]):
    """
    sum of the absolute values of east/west and north/south position
    
    :param start: 
    :param end: 
    :return: 
    """

