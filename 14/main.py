import re
from itertools import product

import pytest


def convert_to_int(b):
    return int(b, 2)


def convert_to_bin(num):
    return format(num, '036b')


def update_bits(bin, mask):
    s = []
    for i in range(36):
        if mask[i] != 'X':
            s.append(mask[i])
        else:
            s.append(bin[i])
    return ''.join(s)


def parse_file(s):
    d = {}
    for line in s.splitlines():
        maskLine = re.match(r'mask = ([X01]{36})', line)
        if maskLine:
            mask = maskLine.groups()[0]
            d[mask] = []
        else:
            i = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
            d[mask].append([int(i[0]), convert_to_bin(int(i[1]))])
    return d


def part1(data):
    mem = {}
    for k in data:
        for m in data[k]:
            mem[m[0]] = convert_to_int(update_bits(m[1], k))
    return sum(mem.values())


def part2(data):
    mem = {}
    for k in data:
        for m in data[k]:
            # convert m[0] to bin
            mem_idx = convert_to_bin(m[0])
            # use mask to replace: if mask is 1 or X use mask, else use
            # m[0] bin
            s = []
            for i in range(36):
                if k[i] in ['X', '1']:
                    s.append(k[i])
                else:
                    s.append(mem_idx[i])
            target = ''.join(s)
            # find all possible combinations of X values
            count = target.count('X')
            possible = list(product([0, 1], repeat=count))
            # loop over X tuples, substitute into bin, convert to int, assign
            # m[1] to mem[int just found]
            for t in possible:
                bin = target.replace('X', '%s') % t
                mem[convert_to_int(bin)] = convert_to_int(m[1])
    return sum(mem.values())


def compute(s):
    data = parse_file(s)
    return part1(data), part2(data)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX11XXX0X
mem[7] = 11
mem[12] = 101
mem[5] = 0""", 366),
    ),
)
def test_part1(input_s, expected):
    data = parse_file(input_s)
    assert part1(data) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""", 208),
    ),
)
def test_part2(input_s, expected):
    data = parse_file(input_s)
    assert part2(data) == expected


def main():
    with open('14/input.txt') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
