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
        if i in range(0,n):
            continue
        else:
            window = xmaslist[i-n:i]
            for j in window:
                if num - j < 0:
                    continue
                elif num - j > 0:
                    half = j
                    if (num - half) in window:
                        print(f" found: {num} = {half}, {(num-half)}")
                        continue
                    else:
                        print(f" found one: {num}")
                        break
        return num
