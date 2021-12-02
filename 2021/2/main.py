import pytest


def part1(input_list):
    x = 0
    d = 0
    for i in input_list:
        direction, v = i.split()
        v = int(v)
        if direction == "forward":
            x = x + v
        elif direction == "up":
            d -= v
        elif direction == "down":
            d += v
    return x*d


def part2(input_list):
    x = 0
    d = 0
    aim = 0
    for i in input_list:
        direction, v = i.split()
        v = int(v)
        if direction == "forward":
            x = x + v
            d += (aim * v)
        elif direction == "up":
            aim -= v
        elif direction == "down":
            aim += v
    return x*d


def compute(input_slist):

    return part1(input_slist), part2(input_slist)


@pytest.mark.parametrize(
    ('input_slist', 'expected'),
    (
        ([
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ], (150, 900)),
    ),
)
def test(input_slist, expected):
    assert compute(input_slist) == expected


def main():
    with open('2/input.txt') as f:
        print(compute(f.read().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
