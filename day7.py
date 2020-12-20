

def rule_parser(rule:str):
    """
    Helper function
     
    :param str: english sentences
    :return: dict of {color: [list of what's inside]}
    """
    parts = rule.split(' bags contain ')
    container = parts[0]
    contained = parts[1].split(', ')
    return {container:contained}
