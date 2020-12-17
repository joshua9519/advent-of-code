from itertools import product
from operator import add

import numpy as np
import pytest

directions = list(product(range(-1, 2), repeat=4))
directions.remove((0, 0, 0, 0))


def parse(s):
    split = s.splitlines()
    a = np.full((3, 3, len(split), len(split[0])), '.')
    initial = []
    for i in s.splitlines():
        initial.append([s for s in i])
    a[1][1] = initial
    return a


def check_in_bounds(cube, ind):
    if ind[0] < 0 or ind[0] > len(cube) - 1:
        return False
    elif ind[1] < 0 or ind[1] > len(cube[0]) - 1:
        return False
    elif ind[2] < 0 or ind[2] > len(cube[0][0]) - 1:
        return False
    elif ind[3] < 0 or ind[3] > len(cube[0][0][0]) - 1:
        return False
    return True


def get_neighbours(cube, pos):
    neighbours = []
    for i in directions:
        ind = tuple(map(add, pos, i))

        if not check_in_bounds(cube, ind):
            continue

        neighbours.append(cube[ind])

    return neighbours


def update_active(current, count):
    if current == '#' and count not in [2, 3]:
        return '.'
    elif current == '.' and count == 3:
        return '#'
    return current


def update(init, new, pos):
    n = get_neighbours(init, pos)
    new[pos] = update_active(init[pos], n.count('#'))
    return new


def compute(s):
    init = parse(s)
    seq = 0
    while seq < 6:
        new = np.copy(init)
        for w in range(len(init)):
            for x in range(len(init[w])):
                for y in range(len(init[w][x])):
                    for z in range(len(init[w][x][y])):
                        pos = (w, x, y, z)
                        new = update(init, new, pos)
        init = np.copy(new)
        init = np.lib.pad(
            init,
            ((1, 1), (1, 1), (1, 1), (1, 1)),
            'constant',
            constant_values='.')
        seq += 1
    return np.count_nonzero(new == '#')


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            """.#.
..#
###""", 140
        ),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('17/input.txt') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
