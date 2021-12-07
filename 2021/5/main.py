import pytest
import re
from collections import Counter
import itertools


def parse(input_l):
    out = []
    for li in input_l:
        x1, y1, x2, y2 = map(int, re.match(
            r"(\d+),(\d+) -> (\d+),(\d+)", li).groups())
        out.append(((x1, y1), (x2, y2)))
    return out


def vec_to_pts(vector, include_diagonals):
    ((x1, y1), (x2, y2)) = vector
    if x1 == x2:
        return [(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))]
    elif y2 == y1:
        return [(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    elif include_diagonals:
        slope = round((y2-y1) / (x2-x1))
        intercept = y2-slope*x2
        return [(x, round(slope*x+intercept)) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    else:
        return []


def find_overlap_pts(vectors, include_diagonals):
    all_points = itertools.chain(*[vec_to_pts(vector, include_diagonals) for vector in vectors])
    occurrences = Counter(all_points)
    return [(point, count) for (point, count) in occurrences.items() if count > 1]


def part1(coords):
    overlapped_points = find_overlap_pts(coords, include_diagonals=False)
    return len(overlapped_points)


def part2(coords):
    overlapped_points = find_overlap_pts(coords, include_diagonals=True)
    return len(overlapped_points)


def compute(coords):

    return part1(coords), part2(coords)


@pytest.mark.parametrize(
    ('coords', 'expected'),
    (
        (
            ([
                ((0, 9), (5, 9)),
                ((8, 0), (0, 8)),
                ((9, 4), (3, 4)),
                ((2, 2), (2, 1)),
                ((7, 0), (7, 4)),
                ((6, 4), (2, 0)),
                ((0, 9), (2, 9)),
                ((3, 4), (1, 4)),
                ((0, 0), (8, 8)),
                ((5, 5), (8, 2)),
            ]), (5, 12)),
    ),
)
def test(coords, expected):
    assert compute(coords) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ([
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2"
        ], ([
            ((0, 9), (5, 9)),
            ((8, 0), (0, 8)),
            ((9, 4), (3, 4)),
            ((2, 2), (2, 1)),
            ((7, 0), (7, 4)),
            ((6, 4), (2, 0)),
            ((0, 9), (2, 9)),
            ((3, 4), (1, 4)),
            ((0, 0), (8, 8)),
            ((5, 5), (8, 2)),
        ])),
    ),
)
def test_parse(input_s, expected):
    assert parse(input_s) == expected


def main():
    with open('5/input.txt') as f:
        coords = parse(f.read().splitlines())
        print(compute(coords))

    return 0


if __name__ == '__main__':
    exit(main())
