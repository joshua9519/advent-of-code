import pytest


def parse(s):
    elves = s.strip().split('\n\n')

    elves_list = [[int(i) for i in li.splitlines()] for li in elves]
    return elves_list


def part1(input_list):
    totals = [sum(v) for v in input_list]
    return max(totals)


def part2(input_list):
    totals = [sum(v) for v in input_list]
    totals.sort(reverse=True)
    total = sum(totals[0:3])
    return total


def compute(elves):
    return part1(elves), part2(elves)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000]
]),
    ),
)
def test_parse(input_s, expected):
    assert parse(input_s) == expected



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", (24000,45000)),
    ),
)
def test(input_s, expected):
    assert compute(parse(input_s)) == expected


def main():
    with open('input.txt') as f:
        elves = parse(f.read())
        print(compute(elves))

    return 0


if __name__ == '__main__':
    exit(main())
