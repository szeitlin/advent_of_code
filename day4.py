import re

def read_batch_files(inputdoc:str) -> list:
    """
    Read unstructured text and split on blank lines
    :return: list of documents 
    """
    return [x.strip() for x in inputdoc.split('\n\n')]

def validate_passport_data(document:str) -> int:
    """
    Convert unstructured text to dictionaries and 
    
    
    :return: 
    """
    groups = find_fields(document)
    if check_fields_present(groups) == 1:
        #check if they're actually valid
        #byr: (v >= 1920) and (v <= 2002)
        #iyr: (v >= 2010) and (v <= 2020)
        #eyr: (v >= 2020) and (v <= 2030)
        #hgt: if cm (v >= 150) and (v <= 193)
              #if in (v >= 59) and (v <= 76)
        #hcl: v.startswith('#') and [0-9]{6} or [a-f]{6}
        #ecl: v in 'amb blu brn gry grn hzl oth'
        #pid: len(v) == 9
        
def find_fields(document:str) -> list:
    """
    Find which fields are present
    
    :param document: string with fields
    :return: list of fields found
    """
    cleaned = document.replace(": ", ":")
    m = re.compile('(\w*:.*?)')
    groups = re.findall(m, cleaned)
    return groups

def check_fields_present(groups:list) -> int:
    """
    check for missing fields
        
    cid is optional, all others are required
    
    :param groups: keys
    :return: valid as 1 or invalid as 0
    """
    required = {'ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'cid:', 'hgt:'}
    missing = required - set(groups)
    if len(missing) == 0:
        return 1
    if missing == {'cid:'}:
        return 1
    elif len(missing) > 1:
        return 0
    elif len(missing) == 1 and missing != {'cid:'}:
        return 0

def count_valid(inputdoc) -> int:
    """
    Read from the text file and output counts
    :param inputdoc: str
    :return: number of valid documents
    """
    documents = read_batch_files(inputdoc)
    valid = 0
    for doc in documents:
        valid += validate_passport_data(doc)
    return valid

if __name__ == '__main__':
    with open('day4_input.txt', 'r') as f:
        inputdoc = f.read()
    valid = count_valid(inputdoc)
    print(valid)
