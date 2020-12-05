import argparse
from math import ceil

import pytest


def front_half(ran):
    return (ran[0], ran[0]+(ran[1]-ran[0])/2)


def back_half(ran):
    return (ran[0]+(ran[1] - ran[0])/2, ran[1])


def parse(ran, front_id, s):
    for j in s:
        if j == front_id:
            ran = front_half(ran)
        else:
            ran = back_half(ran)
    return int(ceil(ran[0]))


def compute(li):
    seat_ids = sorted([parse((0, 127), 'F', i[0:7])*8 +
                       parse((0, 7), 'L', i[7:10])
                       for i in li])

    missing_seats = [seat_ids[i]-1
                     for i in range(len(seat_ids))
                     if not seat_ids[i-1] == seat_ids[i]-1]

    return max(seat_ids), missing_seats[len(missing_seats)//2]


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        [
            ([
                "FBFBBFFRLR",  # 357
                "BFFFBBFRRR",  # 567
                "FFFBBBFRRR",  # 119
                "BBFFBBFRLL"  # 820
            ], (820, 566))
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
        print(compute(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
