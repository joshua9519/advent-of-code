import pytest
import math


def is_visible(tree_list, target):
    for tree in tree_list:
        if tree >= target:
            return False
    return True


def blocked_by_count(tree_list, target):
    blocked_by = 0
    for tree in tree_list:
        if tree < target:
            blocked_by += 1
        else:
            return blocked_by + 1

    return blocked_by


def part1(input_list):
    outer = (len(input_list[0]) + len(input_list) - 2) * 2
    visible = []
    for i, row in enumerate(input_list):
        if 0 < i < (len(input_list) - 1):
            for j, tree in enumerate(row):
                if 0 < j < (len(row) - 1):
                    tree_lists = [
                        input_list[i][:j][::-1],
                        input_list[i][j+1:],
                        [input_list[num][j] for num in range(i)][::-1],
                        [input_list[num][j]
                            for num in range(i + 1, len(input_list))]
                    ]
                    if any([is_visible(tree_list, tree) for tree_list in tree_lists]):
                        visible.append((i, j))
    return outer + len(visible)


def part2(input_list):
    blocked_by = []
    for i, row in enumerate(input_list):
        if 0 < i < (len(input_list) - 1):
            for j, tree in enumerate(row):
                if 0 < j < (len(row) - 1):
                    tree_lists = [
                        input_list[i][:j][::-1],
                        input_list[i][j+1:],
                        [input_list[num][j] for num in range(i)][::-1],
                        [input_list[num][j]
                            for num in range(i + 1, len(input_list))]
                    ]
                    blocked_by_arr = [blocked_by_count(
                        tree_list, tree) for tree_list in tree_lists]

                    blocked_by.append((tree, math.prod(blocked_by_arr)))
    return max(blocked_by, key=lambda t: t[1])[1]


def compute(trees_list):
    return part1(trees_list), part2(trees_list)


@pytest.mark.parametrize(
    ('input_list', 'expected'),
    (
        (
            [
                "30373",
                "25512",
                "65332",
                "33549",
                "35390"
            ],
            (21, 8)
        ),
    ),
)
def test(input_list, expected):
    assert compute(input_list) == expected


def main():
    with open('8/input.txt') as f:
        trees_list = f.read().splitlines()
        print(compute(trees_list))

    return 0


if __name__ == '__main__':
    exit(main())
