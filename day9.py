from typing import List

#preamble of 25 numbers
#each subsequent number should be the sum of any two of the 25 previous numbers
#the two numbers will have different values, and there might be more than one pair

def sum_previous(xmaslist: List[int], n:int=25,) -> int:
    """
    :param n: how many previous numbers to look at
    :param xmaslist: the list of numbers to evaluate
    :return: first number in the list that is NOT the sum of two numbers of the n numbers before it
    """
    #for each number after 25
        #in the 25 preceding numbers (lookback)
        #is there a pair that can sum to this number

    #want everything to be indexed
    for i, num in enumerate(xmaslist):
        print(i, num)
        if i in range(0,n):
            continue
        else:
            #todo: may want to keep track of pairs we've seen since order doesn't matter?
            window = xmaslist[i-n:i]
            print(window)
            for j in window:
                if num - j < 0:
                    continue
                elif num - j > 0:
                    half = j
                    if (num - half) in window:
                        print(f" found: {num} = {half}, {(num-half)}")
                        break
            else:
                print(f" no match found: {num}")
                return num

if __name__ == '__main__':
    with open('day9_input.txt', 'r') as f:
        raw = f.readlines()
        xmaslist = [int(x) for x in raw]
        result = sum_previous(xmaslist)
        print(result)