import re

def read_batch_files(inputdoc:str) -> list:
    """
    Read unstructured text and split on blank lines
    :return: list of documents 
    """
    return [x.strip() for x in inputdoc.split('\n\n')]

def validate_passport_data(document:str) -> int:
    """
    Check if field values are consistent with stated requirements
    Split and convert to a dictionary
    """
    hashed = document.replace("# ", "#")
    colonated = re.sub(":\s*", ":", hashed)
    groups = find_fields(colonated)
    if check_fields_present(groups) == 1: #if all fields are present
        kv_pairs = colonated.split()
        try:
            kv_dict = {kv.split(':')[0]:kv.split(':')[1] for kv in kv_pairs}
        except IndexError:
            return 0
        #check if they're actually valid
        valid = 0
        for k,v in kv_dict.items():
            if k == 'byr':
                if (int(v) >= 1920) and (int(v) <= 2002):
                    valid +=1
                else:
                    print('byr invalid')
            elif k == 'iyr':
                if (int(v) >= 2010) and (int(v) <= 2020):
                    valid +=1
                else:
                    print('iyr invalid')
            elif k == 'eyr':
                if (int(v) >= 2020) and (int(v) <= 2030):
                    valid +=1
                else:
                    print('eyr invalid')
            elif k == 'hgt':
                raw_list = re.split('(\d+)(\D+)', v)
                v_list = list(filter(None, raw_list)) #remove empty strings
                try:
                    if 'cm' in v_list[1]:
                        h = int(v_list[0])
                        if (h >= 150) and (h <= 193):
                            valid +=1
                    elif 'in' in v_list[1]:
                        h = int(v_list[0])
                        if (h >= 59) and (h <= 76):
                            valid +=1
                    else:
                        print('hgt missing units')
                except IndexError:
                    print('invalid hgt')
            elif k == 'hcl':
                if v.startswith('#'):
                    m = re.match('(#[0-9_a-f]{6})', v)
                    if len(m.groups()) == 1:
                        valid +=1
                    else:
                        print("hcl invalid")
            elif k == 'ecl':
                if v in 'amb blu brn gry grn hzl oth':
                    valid +=1
                else:
                    print('ecl invalid')
            elif k == 'pid':
                if len(v) == 9:
                    valid += 1
                else:
                    print('pid invalid')
        if valid == 7:
            return 1
        else:
            print(f"Only this many {valid} are valid")
            return 0
    else:
        return 0
        
def find_fields(document:str) -> list:
    """
    Some minor cleanup to make this easier
    Find which fields (keys) are present
    
    :param document: string with fields
    :return: list of fields found
    """
    m = re.compile('(\w*:.*?)')
    groups = re.findall(m, document)
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
