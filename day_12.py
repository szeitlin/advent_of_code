from itertools import cycle
import operator
import re


class Ship:

    def __init__(self):
        """
        :param facing: direction the ship is facing right now
        """
        self.start = [0,0]
        self.current = [0,0]
        self.start_facing = 'E'
        self.current_facing = self.start_facing

    def move_ship(self, instr:str) -> list:
        """
        Assuming a coordinate system of (-inf, inf) on the x and (-inf, inf) on the y
        
        :param instr: looks like NSEW, LR, or F (forward), plus a number
    
        :return: new coordinates
        """
        #Let's assume East is + and West is -
        #Let's also assume North is + and South is -

        #initialize output coordinate
        result = self.current

        #initialize step. Assume going nowhere unless we say otherwise
        step = 0

        step_dir = re.match('^(\D)', instr).group()
        step_size = int(re.search('(\d+)', instr).group())

        direction_map = {'N': operator.add(self.current[1], step_size),
                         'S': operator.sub(self.current[1], step_size),
                          'E': operator.add(self.current[0], step_size),
                            'W': operator.sub(self.current[0], step_size)}

        #look up how far to go according to the direction
        if step_dir in 'NSEW':
            step = direction_map[step_dir]
            print(step)
        elif step_dir == 'F':
            step_dir = self.current_facing
            step = direction_map[step_dir]
            print(f'facing step: {step}')
        elif step_dir in 'LR':
            step_dir = self.rotate(step_dir, step_size)
            self.current_facing = step_dir
            step = self.current[1] #not going anywhere, have to keep this
            print(f'rotation: {step_dir}')

        print(step_dir)

        if step_dir in 'NS':
            result = [self.current[0], step]
            print(result)

        elif step_dir in 'EW':
            result = [step, self.current[1]]
            print(result)

        return result

    def rotate(self, step_dir:str, step_size:int) -> list:
        """
        Ship starts out facing east (we'll call that 'E')
        
        :param step_dir: has to be L or R
        :param step_size: int
        
        Only LR (left and right) can change the direction the ship is facing
        """
        #input format is direction + degrees, e.g. R90 from East would be South
        rot_steps = step_size//90
        direction_map = {'L' :cycle('NWSE'), 'R': cycle('SWNE')}
        steps = direction_map[step_dir]

        for i in range(rot_steps):
            facing = next(steps)

        return facing


    def manhattan_distance(self, end:list) -> int:
        """
        sum of the absolute values of east/west and north/south position
        
        abs(x2-x1) + abs(y2-y1)
        
        :param end: final location, after executing all steps in the sequence
        :return: distance
        """
        y = operator.abs(end[1] - self.start[1])
        x = operator.abs(end[0] - self.start[0])
        return x + y

    def execute_movements(self, instr_list:list) -> list:
        """
        Take a list of instructions and move the ship accordingly
        :param instr_list: list of str
        :return: ending coordinate
        """
        #save the original starting point, because we're going to overwrite it

        for instr in instr_list:
            result = self.move_ship(instr)
            self.current = result
        print(self.current)

        end = self.current #final result
        dist = self.manhattan_distance(end)
        print(dist)
        return dist


if __name__ == '__main__':
    #todo: read in the list of instructions
    ship = Ship()
    end = ship.execute_movements(instr_list)
    distance = ship.manhattan_distance(end)


