import pytest


def part1(positions):
    fuel = []
    for possible in range(1, max(positions) + 1):
        fuel.append((possible, sum(abs(possible - pos) for pos in positions)))
    return min(fuel, key=lambda t: t[1])


def part2(positions):
    fuel = []
    for possible in range(1, max(positions) + 1):
        f = 0
        for pos in positions:
            d = abs(possible - pos)
            f += (d * (d + 1) // 2)
        fuel.append((possible, f))
    return min(fuel, key=lambda t: t[1])


def compute(positions):
    return part1(positions), part2(positions)


@pytest.mark.parametrize(
    ('positions', 'expected'),
    (
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], ((2, 37), (5, 168))),
    ),
)
def test(positions, expected):
    assert compute(positions) == expected


def main():
    with open('7/input.txt') as f:
        positions = [int(i) for i in f.read().split(",")]
        print(compute(positions))

    return 0


if __name__ == '__main__':
    exit(main())
