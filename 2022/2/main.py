import pytest
import string


def parse(slist):
    slist = [i.translate(str.maketrans('', '', ' \n\t\r')) for i in slist]
    rounds = [[i[0], i[1]] for i in slist]

    return rounds


def part1(rounds):
    score_matrix = {
        "A": {
            "X": 4,
            "Y": 8,
            "Z": 3
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C": {
            "X": 7,
            "Y": 2,
            "Z": 6
        },
    }
    scores = [score_matrix[i[0]][i[1]] for i in rounds]
    return sum(scores)


def part2(rounds):
    score_matrix = {
        "A": {
            "X": 3,
            "Y": 4,
            "Z": 8
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C": {
            "X": 2,
            "Y": 6,
            "Z": 7
        },
    }
    scores = [score_matrix[i[0]][i[1]] for i in rounds]
    return sum(scores)


def compute(rounds):
    return part1(rounds), part2(rounds)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (["A Y",
"B X",
"C Z"], [["A", "Y"], ["B", "X"], ["C", "Z"]]),
    ),
)
def test_parse(input_s, expected):
    assert parse(input_s) == expected


@pytest.mark.parametrize(
    ('rounds', 'expected'),
    (
        ([["A", "Y"], ["B", "X"], ["C", "Z"]],
        (15, 12)),
    ),
)
def test(rounds, expected):
    assert compute(rounds) == expected


def main():
    with open('input.txt') as f:
        rounds = parse(f.read().splitlines())
        print(compute(rounds))

    return 0


if __name__ == '__main__':
    exit(main())
