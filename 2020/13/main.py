from math import ceil

import pytest


def parse_p1(s):
    split = s.splitlines()
    timestamp = int(split[0])
    li = [int(i) for i in split[1].split(',') if i != 'x']
    return timestamp, li


def closestMultiple(n, li):
    d = {}
    for id in li:
        d[id] = ceil(n/id)*id - n
    return d


def part1(s):
    timestamp, li = parse_p1(s)
    d = closestMultiple(timestamp, li)
    minID = min(d, key=d.get)
    return minID * d[minID]


def parse_p2(s):
    split = s.splitlines()
    li = split[1].split(',')
    d = {int(li[i]): int(i) for i in range(len(li)) if li[i] != 'x'}
    return d


def check_offset(d, timestamp):
    check = True
    for offset in d.keys():
        if offset != 0 and (d[offset] - (timestamp % d[offset]) != offset):
            check = False
    return check


def part2(s):
    d = parse_p2(s)
    ids = list(d.keys())
    step = ids[0]
    timestamp = 0
    for id in ids[1:]:
        offset = d[id]
        for i in range(timestamp, step*id, step):
            if not (i+offset) % id:
                step = step*id
                timestamp = i
    return timestamp


def compute(s):
    ans1 = part1(s)
    timestamp = part2(s)
    return ans1, timestamp


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""939
7,13,x,x,59,x,31,19""", (295, 1068781)),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('13/input-test.txt') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
