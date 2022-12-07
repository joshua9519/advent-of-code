import pytest


def get_marker_char(input_s, n):
    for i in range(len(input_s)):
        char_slice = input_s[i:(i + n)]
        if len(char_slice) == len(set(char_slice)):
            return i + n


def part1(input_s):
    return get_marker_char(input_s, 4)


def part2(input_s):
    return get_marker_char(input_s, 14)


def compute(input_s):
    return part1(input_s), part2(input_s)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            (7, 19)
        ),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('6/input.txt') as f:
        assignment_pairs_s = f.read()
        print(compute(assignment_pairs_s))

    return 0


if __name__ == '__main__':
    exit(main())
