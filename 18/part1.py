import re

import pytest


def evaluate(s):
    i, op, j = s.split()
    if op == '+':
        return str(int(i) + int(j))
    elif op == '*':
        return str(int(i) * int(j))


def parse(s):
    parenthesis = re.findall(r'\(([0-9+* ]+)\)', s)
    while len(parenthesis) > 0:
        for p in parenthesis:
            v = parse(p)
            s = s.replace('(' + p + ')', v, 1)
        parenthesis = re.findall(r'\(([0-9+* ]+)\)', s)

    match = re.match(r'\d+ [+*] \d+', s)
    while match:
        m = match.group(0)
        v = evaluate(m)
        s = s.replace(m, v, 1)
        match = re.match(r'\d+ [+*] \d+', s)
    return s


def compute(s):
    sum = 0
    for i in s.splitlines():
        sum += int(parse(i))
    return sum


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("2 * 3 + (4 * 5)", '26'),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", '437'),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", '12240'),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", '13632'),
        ("1 + 2 * 3 + 4 * 5 + 6", '71'),
        ('((9 + 6 * 4 * 4 * 7 * 5) + 3 * 5 * 7 * 2) * 9 + 9 * (3 * (8 * 2 * 9 * 2 * 5 + 8) + (7 * 2 * 7) * 2)', '47030998716'),  # noqa: E501
    ),
)
def test_parse(input_s, expected):
    assert parse(input_s) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
1 + 2 * 3 + 4 * 5 + 6""", 26406),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('18/input.txt') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
