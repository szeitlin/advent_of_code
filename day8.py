"""
You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. 

For example, acc +7 would increase the accumulator by 7. 
The accumulator starts at 0. 
After an acc instruction, the instruction immediately below it is executed next.

jmp jumps to a new instruction relative to itself. 
The next instruction to execute is found using the argument as an offset from the jmp instruction; 
for example, 
jmp +2 would skip the next instruction, 
jmp +1 would continue to the instruction immediately below it, 
and jmp -20 would cause the instruction 20 lines above to be executed next.

nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

Run your copy of the boot code. 

Immediately before any instruction is executed a second time, what value is in the accumulator?

"""

#need three things: 1. what's the accumulator value, 2. track execution of each line 3. index the lines

from collections import defaultdict
import re
from typing import List

class Step:

    def __init__(self, i:int, stepstr:str):
        """
        :param i: line number
        :param stepstr: raw instruction at that line 
        """
        self.index = i
        self.action = stepstr.split(' ')[0]
        direction = re.search('\W{1}\d+', stepstr)
        self.size = int(direction.group())

class Stepper:

    def __init__(self, steplist:List[str]):
        """
        :param steplist: full list of raw instructions
        """
        #create a list of enumerated Step objects
        self.step_dict = {i:Step(i, instr) for (i,instr) in enumerate(steplist)}

        #initialize accumulator
        self.acc = 0

        #initialize execution counter
        self.exec_count = defaultdict(int) #todo: what is the key here? the index?

    def move(self, i:int=0):
        """
        Executes each step by looking up the item by index in the step_dict
        Increments the exec_count as it goes
        :param i: index of the current step, starts at 0
        """
        while 2 not in self.exec_count.values():
            #stopping criteria
            if self.exec_count[i] == 1:
                break
            else:
                self.exec_count[i] += 1
                gohere = self.do_step(self.step_dict[i])
                self.move(gohere)
        return self.acc

    def do_step(self, step:Step) -> int:
        """
        Execute the current step
        :param step: Step object
        """
        gohere = step.index
        if step.action == 'acc':
            self.acc += step.size
            gohere += 1
        elif step.action == 'nop':
            gohere += 1
        elif step.action == 'jmp':
            gohere += step.size
        return gohere

if __name__ == '__main__':
    with open('day8_input.txt', 'r') as f:
        steplist = f.readlines()
        stepthis = Stepper(steplist)
        acc = stepthis.move()
        print(acc)

