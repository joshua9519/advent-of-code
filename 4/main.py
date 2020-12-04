import argparse
import re

import pytest


def valid_w_bounds(s, lb, ub):
    # print('Checking {} is between {} and {}'.format(s, lb, ub))
    if lb <= int(s) <= ub:
        return True
    return False


def valid_byr(s):
    return valid_w_bounds(s, 1920, 2020)


def valid_iyr(s):
    return valid_w_bounds(s, 2010, 2020)


def valid_eyr(s):
    return valid_w_bounds(s, 2020, 2030)


def valid_hgt(s):
    if 'cm' in s:
        return valid_w_bounds(s.strip('cm'), 150, 193)
    elif 'in' in s:
        return valid_w_bounds(s.strip('in'), 59, 76)


def valid_hcl(s):
    if re.match(r'^#[a-f0-9]{6}$', s):
        # print('{} matches hcl'.format(s))
        return True
    return False


def valid_ecl(s):
    valid_colours = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]
    if s in valid_colours:
        # print('{} is a valid colour'.format(s))
        return True
    return False


def valid_pid(s):
    if re.match(r'^[0-9]{9}$', s):
        # print('{} matches pid'.format(s))
        return True
    return False


def get_detail(s, di):
    key, value = s.split(':')
    di[key] = value


def parse_lines(li):
    parsed = []
    for line in li:
        di = {}
        for i in line.split(' '):
            if '\n' in i:
                for j in i.split('\n'):
                    get_detail(j, di)
            else:
                get_detail(i, di)
        parsed.append(di)
    return parsed


def check_keys(di):
    requiredCodes = {
        'byr': valid_byr,
        'iyr': valid_iyr,
        'eyr': valid_eyr,
        'hgt': valid_hgt,
        'hcl': valid_hcl,
        'ecl': valid_ecl,
        'pid': valid_pid,
    }
    for c in requiredCodes:
        if c not in di:
            return False
        else:
            f = requiredCodes[c]
            if not f(di[c]):
                return False
    return True


def compute(s):
    li = s.strip().split('\n\n')
    details = parse_lines(li)
    valid = 0
    for i in details:
        if check_keys(i):
            valid += 1
    return valid


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""ecl:gry pid:060033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:76075310 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""", 1),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
