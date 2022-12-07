import pytest
import re


def parse(input_s):
    crates, moves = input_s.split('\n\n')

    crate_arr = [
        [i[j] for j in range(1, len(i), 4)]
        for i in crates.splitlines()
        if i.__contains__("[")
    ]
    crate_map = {
        (i+1): [
            j[i] for j in crate_arr if j[i] != ' '
        ]
        for i in range(int(crates[-2]))
    }

    moves_arr = [
        re.findall(r"move (\d+) from (\d+) to (\d+)", i)[0]
        for i in moves.splitlines()
    ]
    moves_arr = [[int(i) for i in move] for move in moves_arr]
    return crate_map, moves_arr


def part1(crate_map, moves_arr):
    for move in moves_arr:
        crate_map[move[2]] = crate_map[move[1]][0:move[0]][::-1] + \
            crate_map[move[2]]
        crate_map[move[1]] = crate_map[move[1]][move[0]:]

    return "".join(
        [
            crate_map[i][0]
            for i in crate_map
        ]
    )


def part2(crate_map, moves_arr):
    for move in moves_arr:
        crate_map[move[2]] = crate_map[move[1]][0:move[0]] + \
            crate_map[move[2]]
        crate_map[move[1]] = crate_map[move[1]][move[0]:]

    return "".join(
        [
            crate_map[i][0]
            for i in crate_map
        ]
    )


def compute(input_slist):
    crate_map, moves_arr = parse(input_slist)
    return part1(crate_map.copy(), moves_arr), \
        part2(crate_map.copy(), moves_arr)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
            (
                {
                    1: ['N', 'Z'],
                    2: ['D', 'C', 'M'],
                    3: ['P']
                },
                [
                    [1, 2, 1],
                    [3, 1, 3],
                    [2, 2, 1],
                    [1, 1, 2]
                ]
            )
        ),
    ),
)
def test_parse(input_s, expected):
    assert parse(input_s) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
            ('CMZ', 'MCD')
        ),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('5/input.txt') as f:
        assignment_pairs_s = f.read()
        print(compute(assignment_pairs_s))

    return 0


if __name__ == '__main__':
    exit(main())
