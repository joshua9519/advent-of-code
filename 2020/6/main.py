import argparse

import pytest


def parse_line(line):
    group = [set(s) for s in line.splitlines()]
    intersection = set.intersection(*group)
    union = set.union(*group)
    return len(union), len(intersection)


def compute(s):
    group_list = s.strip().split('\n\n')
    yes = 0
    intersect = 0
    for group in group_list:
        y, i = parse_line(group)
        yes += y
        intersect += i
    return yes, intersect


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""abc

a
b
c

ab
ac

a
a
a
a

b""", (11, 6)),
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
