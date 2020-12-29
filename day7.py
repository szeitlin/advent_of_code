from typing import List

def rule_parser(rule:str):
    """
    Helper function
     
    :param str: english sentences
    :return: dict of {color: [list of what's inside]}
    """
    parts = rule.split(' bags contain ')
    container = parts[0]
    try:
        contained = parts[1].split(', ')
    except IndexError:
        contained = parts[1]
    return {container:contained}

def all_rules(rule_list:List[str]) -> dict:
    """
    Parse all the lines in the rule list into a single dict. 
    :param rule_list: list with one set of rules per line
    :return: dictionary of {color: [what it contains]}
    """
    big_dict = dict()
    for rule in rule_list:
        big_dict.update(rule_parser(rule))
    return big_dict

def find_target_holders(big_dict:dict, target:str='shiny gold bag') -> List:
    """
    You have a shiny gold bag. 
    If you wanted to carry it in at least one other bag, 
    how many different bag colors would be valid for the outermost bag? 
    (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
    
    :param big_dict: 
    :param target bag type
    :return: set of bags
    """
    holders = []
    for k,v in big_dict.items():
        for item in v:
            if target in item:
                holders.append(k)
                print(k,v)
    unique = set(holders)
    return list(unique)

def find_holder_holders(big_dict:dict) -> List:
    """
    Trace upwards through the graph to find all the bags that can contain shiny gold ones
    :param big_dict: 
    :return: list of bags
    """
    #first, find any bags that can contain shiny gold (using find_shiny_gold_holders)
    holders = find_target_holders(big_dict)
    print(holders)
    #iterate back through the big_dict and find what bags contain those
    all_holders = holders[:]

    #todo: may need more iterations here?
    #todo: stopping criteria is if you're only seeing things you've seen before on this level
    for k in holders:
        print(k)
        hits = find_target_holders(big_dict=big_dict, target=k)
        print(hits)
        if set(hits).issubset(set(all_holders)):
            break
        else:
            all_holders.extend(hits)

    unique = set(all_holders)
    print(unique)
    return list(unique)

if __name__ == '__main__':
    with open('day7_input.txt', 'r') as f:
        rules = f.readlines()
        big_dict = all_rules(rules)
        holders = find_holder_holders(big_dict)
        print(len(holders))