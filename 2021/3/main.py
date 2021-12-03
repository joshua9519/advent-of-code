import pytest
from statistics import multimode, mode


def part1(input_list):
    gamma = ""
    epsilon = ""
    for i in range(len(input_list[0])):
        e = "0"
        g = mode([row[i] for row in input_list])
        if g == "0":
            e = "1"
        gamma += g
        epsilon += e
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def part2(input_list):
    co2 = input_list
    oxy = input_list
    o = 0
    c = 0
    for i in range(len(input_list[0])):
        if len(co2) != 1:
            most = max(multimode([row[i] for row in co2]))
            co2 = [row for row in co2 if row[i] == most]
        if len(oxy) != 1:
            most = max(multimode([row[i] for row in oxy]))
            oxy = [row for row in oxy if row[i] != most]
    o = int(oxy[0], 2)
    c = int(co2[0], 2)
    return o*c


def compute(input_slist):

    return part1(input_slist), part2(input_slist)


@pytest.mark.parametrize(
    ('input_slist', 'expected'),
    (
        ([
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ], (198, 230)),
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
