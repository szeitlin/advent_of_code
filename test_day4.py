import re
import unittest
from day4 import read_batch_files, find_fields, validate_passport_data

class TestReadInput(unittest.TestCase):

    def test_read_and_split(self):
        example = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929\n\nhcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm\n\nhcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in'
        split_docs = read_batch_files(example)
        print(split_docs)
        assert len(split_docs) == 4

class TestFindFields(unittest.TestCase):

    def test_all_fields_found(self):
        valid = """ecl: gry
        pid: 860033327
        eyr: 2020
        hcl:  # fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm """
        groups = find_fields(valid)
        assert len(groups) == 8
        assert 'cid:' in groups

    def test_missing_one_field(self):
        invalid = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
                hcl:#cfa07d byr:1929"""
        groups = find_fields(invalid)
        assert len(groups) == 7
        assert 'hgt' not in groups

    def test_missing_optional_field(self):
        valid = """hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm"""
        groups = find_fields(valid)
        assert len(groups) == 7
        assert 'cid' not in groups

    def missing_one_of_each(self):
        invalid = """hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in"""
        groups = find_fields(invalid)
        assert len(groups) == 6


class TestExamples(unittest.TestCase):

    def test_height_inches_missing_optional(self):
        valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f"""
        assert validate_passport_data(valid) == 1

    def test_height_cm_missing_optional(self):
        valid = """eyr:2029 ecl:blu cid:129 byr:1989
        iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"""
        assert validate_passport_data(valid) == 1

    def test_invalid_missing_units(self):
        invalid = """eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"""
        assert validate_passport_data(invalid) == 0

    def test_invalid_eye_color(self):
        invalid = """hgt:59cm ecl:zzz
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007"""
        assert validate_passport_data(invalid) == 0

if __name__ == '__main__':
    unittest.main()