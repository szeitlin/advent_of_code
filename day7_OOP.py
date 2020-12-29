class Bag:
    def __init__(self):
        """
        
        """

class BagMaker:
    def __init__(self, rule:str):
        """
        :param rule: english sentences
        """
        parts = rule.split(' bags contain ')
        self.color = parts[0]
        try:
            self.contains = parts[1].split(', ')
        except IndexError:
            self.contains = parts[1]

