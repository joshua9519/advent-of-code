import argparse
from itertools import combinations

import pytest


def check_sum(li, value):
    possible_sum = [sum(i) for i in combinations(li, 2)]
    if value in possible_sum:
        return True
    return False


def part1(li, preamble):
    counter = 0
    while preamble + counter <= len(li):
        n = preamble + counter
        pre_list = li[counter:n]
        if not check_sum(pre_list, li[n]):
            return li[n]
        counter += 1
    return None


def part2(n, li):
    indices = list(range(len(li)+1))
    for i, j in combinations(indices, 2):
        if j > i + 1 and sum(li[i:j]) == n:
            return min(li[i:j]) + max(li[i:j])
    return None


def compute(li, preamble):
    a1 = part1(li, preamble)
    a2 = part2(a1, li)
    return a1, a2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        [
            (
                [
                    35,
                    20,
                    15,
                    25,
                    47,
                    40,
                    62,
                    55,
                    65,
                    95,
                    102,
                    117,
                    150,
                    182,
                    127,
                    219,
                    299,
                    277,
                    309,
                    576,
                ], (127, 62)
            ),
        ]
    ),
)
def test(input_s, expected):
    assert compute(input_s, 5) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute([int(i) for i in f.read().strip().splitlines()], 25))

    return 0


if __name__ == '__main__':
    exit(main())
