import pytest
import numpy as np


def parse(s):
    lines = s.strip().split('\n\n')

    called = [int(c) for c in lines[0].split(",")]
    boards = []
    for li in lines[1:]:
        board = li.splitlines()
        for i, v in enumerate(board):
            board[i] = [int(j) for j in v.split()]
        boards.append(board)
    return called, boards


def has_won(board, called_numbers):
    return any(all(num in called_numbers for num in line) for line in [*board, *zip(*board)])


def score(board, called_numbers, last_number):
    return last_number * sum(num for line in board for num in line if num not in called_numbers)


def part1(numbers, boards):
    called_numbers = set()
    for num in numbers:
        called_numbers.add(num)
        for board in boards:
            if has_won(board, called_numbers):
                return score(board, called_numbers, num)
    return -1


def part2(numbers, boards):
    called_numbers = set()
    for num in numbers:
        called_numbers.add(num)
        if len(boards) == 1 and has_won(boards[0], called_numbers):
            return score(boards[0], called_numbers, num)
        boards = [board for board in boards if not has_won(board, called_numbers)]
    return -1


def compute(called, boards):

    return part1(called, boards), part2(called, boards)


@pytest.mark.parametrize(
    ('called', 'boards', 'expected'),
    (
        (
            [7, 4, 9, 5, 11, 17, 56],
            [
                [
                    [22, 13, 17, 11, 0],
                    [7, 4, 9, 5, 17],
                    [1, 13, 17, 11, 0],
                    [1, 13, 17, 12, 0],
                    [1, 13, 17, 13, 0]
                ],
                [
                    [3, 15, 0, 2, 22],
                    [9, 18, 13, 17, 5],
                    [7, 4, 9, 5, 56],
                    [9, 18, 13, 17, 5],
                    [3, 15, 0, 2, 22],
                ]
            ], (1734, 8176)),
        (
            [7, 4, 9, 5, 11, 17, 56],
            [
                [
                    [22, 13, 17, 11, 0],
                    [7, 56, 11, 5, 17],
                    [1, 13, 5, 11, 0],
                    [1, 13, 4, 12, 0],
                    [1, 13, 9, 13, 0]
                ],
                [
                    [3, 15, 0, 4, 22],
                    [9, 18, 13, 9, 5],
                    [3, 15, 0, 5, 22],
                    [9, 18, 13, 11, 5],
                    [3, 15, 0, 56, 22],
                ]
            ], (2686, 10192)),
        (
            [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1],
            [
                [
                    [22, 13, 17, 11,  0],
                    [8, 2, 23, 4, 24],
                    [21,  9, 14, 16,  7],
                    [6, 10, 3, 18, 5],
                    [1, 12, 20, 15, 19]
                ],
                [
                    [3, 15, 0, 2, 22],
                    [9, 18, 13, 17, 5],
                    [19, 8, 7, 25, 23],
                    [20, 11, 10, 24, 4],
                    [14, 21, 16, 12, 6]
                ],
                [
                    [14, 21, 17, 24, 4],
                    [10, 16, 15, 9, 19],
                    [18, 8, 23, 26, 20],
                    [22, 11, 13, 6, 5],
                    [2, 0, 12, 3, 7]
                ],
                [
                    [14, 21, 17, 24, 4],
                    [10, 16, 15, 9, 19],
                    [18, 8, 23, 26, 20],
                    [22, 11, 56, 6, 5],
                    [2, 0, 12, 3, 7]
                ]
            ], (4512, 1924))
    ),
)
def test(called, boards, expected):
    p1, p2 = compute(called, boards)
    print(p1, expected[0])
    assert np.array_equal(p1, expected[0])


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("""7,4,9,5,11,17

22 13 17 11  0
 8  2 23  4 24

 3 15  0  2 22
 9 18 13 17  5""", (
            [7, 4, 9, 5, 11, 17],
            [
                [
                    [22, 13, 17, 11, 0],
                    [8, 2, 23, 4, 24]
                ],
                [
                    [3, 15, 0, 2, 22],
                    [9, 18, 13, 17, 5]
                ]
            ])),
    ),
)
def test_parse(input_s, expected):
    p = parse(input_s)
    assert p[0] == expected[0]
    assert all([np.array_equal(p[1][i], expected[1][i])
               for i in range(len(p[1]))])


def main():
    with open('4/input.txt') as f:
        called, boards = parse(f.read())
        print(compute(called, boards))

    return 0


if __name__ == '__main__':
    exit(main())
