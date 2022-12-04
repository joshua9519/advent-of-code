import pytest


def parse(input_slist):
    assignments = []
    for i in input_slist:
        elf1, elf2 = i.split(",")
        assignments.append(
            (
                [int(num) for num in elf1.split("-")],
                [int(num) for num in elf2.split("-")]
            )
        )
    return assignments


def part1(assignments):
    return len(
        [
            assignment
            for assignment in assignments
            if min(assignment) == max(assignment, key=lambda t:t[1])
            or assignment[0][1] == assignment[1][1]
            or assignment[0][0] == assignment[1][0]
        ]
    )


def part2(assignments):
    return len(
        [
            assignment
            for assignment in assignments
            if max(assignment)[0] <= min(assignment, key=lambda t:t[1])[1]
        ]
    )


def compute(input_slist):
    assignments = parse(input_slist)
    return part1(assignments), part2(assignments)


@pytest.mark.parametrize(
    ('input_slist', 'expected'),
    (
        (
            [
                "2-4,6-8",
                "2-3,4-5",
                "5-7,7-9",
                "2-8,3-7",
                "6-6,4-6",
                "2-6,4-8"
            ],
            [
                ([2, 4], [6, 8]),
                ([2, 3], [4, 5]),
                ([5, 7], [7, 9]),
                ([2, 8], [3, 7]),
                ([6, 6], [4, 6]),
                ([2, 6], [4, 8])
            ]
        ),
    ),
)
def test_parse(input_slist, expected):
    assert parse(input_slist) == expected


@pytest.mark.parametrize(
    ('input_slist', 'expected'),
    (
        (
            [
                "2-4,6-8",
                "2-3,4-5",
                "5-7,7-9",
                "2-8,3-7",
                "6-6,4-6",
                "2-6,4-8"
            ],
            (2, 4)
        ),
    ),
)
def test(input_slist, expected):
    assert compute(input_slist) == expected


def main():
    with open('4/input.txt') as f:
        assignment_pairs_s = f.read().splitlines()
        print(compute(assignment_pairs_s))

    return 0


if __name__ == '__main__':
    exit(main())
