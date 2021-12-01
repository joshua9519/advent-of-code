import argparse
from math import ceil, prod

import pytest


def parseLines(li, x, y):
    return [li[y*i][x*i % len(li[i])] for i in range(int(ceil(len(li)/y)))]


def trees(li, x, y=1):
    path = parseLines(li, x, y)
    return sum(
        i == '#'
        for i
        in path
    )


def compute(li):
    x3y1 = trees(li, 3)
    return x3y1, prod(
                    (x3y1,
                     trees(li, 1),
                     trees(li, 5),
                     trees(li, 7),
                     trees(li, 1, 2)))


@pytest.mark.parametrize(
    ('input_li', 'expected'),
    [
       ([
            ".#...",
            "..##.",
            "#..#.",
            "...##",
            "..#.#",
            "..#..",
            "###..",
            "....#"
        ], (3, 108))
    ],
)
def test(input_li, expected):
    assert compute(input_li) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
