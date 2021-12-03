import pytest


def part1(input_list):
    count = 0
    prev = 0
    for i, v in enumerate(input_list):
        if i == 0:
            continue
        if prev < v:
            count += 1
        prev = v
    return count


def part2(input_list):
    count = 0
    length = len(input_list)
    prev = 0
    for i in range(length):
        if (i+2) < length:
            s = sum(input_list[i:i+3])
            if i != 0 and s > prev:
                count += 1
            prev = s
    return count


def compute(input_slist):
    i = [int(v) for v in input_slist]

    return part1(i), part2(i)


@pytest.mark.parametrize(
    ('input_slist', 'expected'),
    (
        ([
            "199",
            "200",
            "208",
            "210",
            "200",
            "207",
            "240",
            "269",
            "260",
            "263"
        ], (7, 5)),
    ),
)
def test(input_slist, expected):
    assert compute(input_slist) == expected


def main():
    with open('3/input.txt') as f:
        print(compute(f.read().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
