import argparse
import re

import pytest


def compute(li):
    count = 0
    for line in li:
        splitted = line.split(' ')
        rule = splitted[0].split('-')
        letter = splitted[1][0]
        pwd = splitted[2]

        occ = pwd.count(letter)
        min_r = int(rule[0])
        max_r = int(rule[1])

        if occ in range(min_r, max_r + 1):
            count += 1
    return count


def computeBetter(li):
    recs = [
        re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups()
        for line
        in li
    ]

    return sum(
        int(lo) <= pwd.count(c) <= int(hi)
        for lo, hi, c, pwd
        in recs
    )


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    [
        (("13-16 k: kkkkkgmkbvkkrskhd", "5-6 p: qvz",
          "3-4 p: psppxhlfpvkh", "3-10 w: wwwwwwwwwwdwww"), 1),
    ]
)
def test_compute(input_s, expected):
    assert computeBetter(input_s) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(computeBetter(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
