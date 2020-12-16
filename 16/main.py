import re

import pytest


def make_range(s1, s2):
    return range(int(s1), int(s2) + 1)


def parse_rule(rule):
    g = re.match(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', rule).groups()
    return {
        'name': g[0],
        'range1': make_range(g[1], g[2]),
        'range2': make_range(g[3], g[4])
    }


def parse_ticket(s):
    return [int(i) for i in s.split(',')]


def parse(s):
    sections = s.split('\n\n')
    rules = [parse_rule(i) for i in sections[0].splitlines()]
    my_ticket = parse_ticket(sections[1].splitlines()[1])
    nearby = [parse_ticket(i) for i in sections[2].splitlines()[1:]]
    return rules, my_ticket, nearby


def check_rules(i, rules):
    for r in rules:
        if i in r['range1'] or i in r['range2']:
            return True
    return False


def part1(rules, nearby):
    invalid = []
    valid_nb = []
    for i in nearby:
        valid = True
        for n in i:
            if not check_rules(n, rules):
                invalid.append(n)
                valid = False
        if valid:
            valid_nb.append(i)
    return sum(invalid), valid_nb


def verify_rule(rule, li):
    for i in li:
        if i not in rule['range1'] and i not in rule['range2']:
            return False
    return True


def part2(rules, my_ticket, nearby):
    d = {i: [n[i] for n in nearby] for i in range(len(my_ticket))}
    columns = {}
    while len(columns) != len(my_ticket):
        for k, v in d.items():
            possibilities = []
            for rule in rules:
                if verify_rule(rule, v):
                    possibilities.append(rule['name'])
            if len(possibilities) == 1:
                columns[k] = possibilities[0]
                r = next(rule
                         for rule
                         in rules if rule["name"] == possibilities[0])
                rules.remove(r)
    i = 1
    for column, name in columns.items():
        if 'departure' in name:
            i *= my_ticket[column]
    return i


def compute(s):
    rules, my_ticket, nearby = parse(s)
    ans1, valid_nb = part1(rules, nearby)
    ans2 = part2(rules, my_ticket, valid_nb)
    return ans1, ans2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""", (71, [[7, 3, 47]])
        ),
    ),
)
def test_p1(input_s, expected):
    rules, my_ticket, nearby = parse(input_s)
    assert part1(rules, nearby) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            """departure class: 0-1 or 4-19
departure row: 0-5 or 8-19
class: 0-1 or 4-20
seat: 0-13 or 16-19

your ticket:
11,12,13,20

nearby tickets:
3,9,18,20
15,1,5,1
5,14,9,14""", 132
        ),
    ),
)
def test_p2(input_s, expected):
    rules, my_ticket, nearby = parse(input_s)
    _, v = part1(rules, nearby)
    assert part2(rules, my_ticket, v) == expected


def main():
    with open('16/input.txt') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
