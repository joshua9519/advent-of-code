import pytest


def part1(computations):
    cycle = 1
    X = 1
    registers = {
        cycle: X
    }
    for command in computations:
        if command[0] == "noop":
            cycle += 1
            registers[cycle] = X
        else:
            prev_cycle = cycle
            cycle += 1
            while cycle - prev_cycle < 2:
                registers[cycle] = X
                cycle += 1
            X += int(command[1])
            registers[cycle] = X

    return sum([n * registers[n] for n in [20, 60, 100, 140, 180, 220]]),\
        registers


def part2(registers):
    crt = ["", "", "", "", "", ""]
    for cycle, register in registers.items():
        if 1 <= cycle <= 40:
            pos = cycle - 1
            if register - 1 <= pos <= register + 1:
                crt[0] += "#"
            else:
                crt[0] += "."
        elif 40 < cycle <= 80:
            pos = cycle - 41
            if register - 1 <= pos <= register + 1:
                crt[1] += "#"
            else:
                crt[1] += "."
        elif 80 < cycle <= 120:
            pos = cycle - 81
            if register - 1 <= pos <= register + 1:
                crt[2] += "#"
            else:
                crt[2] += "."
        elif 120 < cycle <= 160:
            pos = cycle - 121
            if register - 1 <= pos <= register + 1:
                crt[3] += "#"
            else:
                crt[3] += "."
        elif 160 < cycle <= 200:
            pos = cycle - 161
            if register - 1 <= pos <= register + 1:
                crt[4] += "#"
            else:
                crt[4] += "."
        elif 200 < cycle <= 240:
            pos = cycle - 201
            if register - 1 <= pos <= register + 1:
                crt[5] += "#"
            else:
                crt[5] += "."
    for i in crt:
        print(i)


def compute(input_):
    ans1, registers = part1(input_)
    part2(registers)
    return ans1


@pytest.mark.parametrize(
    ('input_', 'expected'),
    (
        (
            """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""",
            (13140)
        ),
    ),
)
def test(input_, expected):
    computations = [i.split() for i in input_.splitlines()]
    assert compute(computations) == expected


def main():
    with open('10/input.txt') as f:
        input_ = [line.split() for line in f.read().splitlines()]
        print(compute(input_))

    return 0


if __name__ == '__main__':
    exit(main())
