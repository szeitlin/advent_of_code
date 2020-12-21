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
    #print(holders)
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

    #iterate back through the big_dict and find what bags contain those
    #again, using find_target_holders()
    all_holders = holders[:]
    for k in holders:
        for item in k:
        #todo: what is the stopping criteria if we did this with a while loop or recursion?
            all_holders.extend(find_target_holders(big_dict=big_dict, target=item))

    unique = set(all_holders)
    return list(unique)


