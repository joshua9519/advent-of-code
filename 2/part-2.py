import argparse
import re
from operator import xor

import pytest


def compute(li):
    count = 0
    for line in li:
        splitted = line.split(' ')
        rule = splitted[0].split('-')
        letter = splitted[1][0]
        pwd = splitted[2]

        pos1 = int(rule[0]) - 1
        pos2 = int(rule[1]) - 1
        if xor(pwd[pos1] == letter, pwd[pos2] == letter):
            count += 1
    return count


def computeBetter(li):
    recs = [
        re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups()
        for line
        in li
    ]

    return sum(
        (xor((pwd[int(lo)-1] == c), (pwd[int(hi)-1] == c))
            for lo, hi, c, pwd
            in recs)
    )


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    [
        (
            [
                "13-16 k: kkkkkgmkbvkrkrshd",  # one match = y
                "5-6 p: qvzwrgf",  # no match = n
                "3-4 p: psppxhlfpvkh",  # both match = n
            ], 1),
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
