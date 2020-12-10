import argparse

import pytest


def part2(li):
    routes = {}
    routes[0] = 1
    for num in li:
        routes[num] = routes.get(num-1, 0) + \
                            routes.get(num-2, 0) + \
                            routes.get(num-3, 0)

    return routes[li[-1]]


def compute(li):
    li.sort()
    ones = 1
    threes = 1
    for i in range(1, len(li)):
        diff = li[i] - li[i-1]
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1
    return ones*threes, part2(li)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        [
            ([
                16,
                10,
                15,
                5,
                1,
                11,
                7,
                19,
                6,
                12,
                4,
            ], (35, 8)),
        ]
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute([int(i) for i in f.read().strip().splitlines()]))

    return 0


if __name__ == '__main__':
    exit(main())
