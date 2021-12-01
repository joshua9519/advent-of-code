import argparse

import pytest


def jump(i, value):
    i += int(value)
    return i


def part1(li, acc, i):
    visited = set()
    while i not in visited:
        rule = li[i].split()
        visited.add(i)
        if rule[0] == 'nop':
            i += 1
        elif rule[0] == 'acc':
            acc = jump(acc, rule[1])
            i += 1
        elif rule[0] == 'jmp':
            i = jump(i, rule[1])

        if i == len(li):
            return acc, True, visited
    return acc, False, visited


def swap(li, i, rule, newRule):
    old = rule[0]
    rule[0] = newRule
    li[i] = ' '.join(rule)
    acc, isNotLoop, _ = part1(li, 0, 0)
    if isNotLoop:
        return acc
    else:
        rule[0] = old
        li[i] = ' '.join(rule)
        return


def part2(li, path):
    for i in path:
        rule = li[i].split()
        if rule[0] == 'nop':
            acc = swap(li, i, rule, 'jmp')
            if acc:
                return acc

        elif rule[0] == 'jmp':
            acc = swap(li, i, rule, 'nop')
            if acc:
                return acc


def compute(li):
    acc = 0
    i = 0
    acc1, _, visited = part1(li, acc, i)
    return acc1, part2(li, visited)


@pytest.mark.parametrize(
    ('input_li', 'expected'),
    (
        [
            ([
                "nop +0",
                "acc +1",
                "jmp +4",
                "acc +3",
                "jmp -3",
                "acc -99",
                "acc +1",
                "jmp -4",
                "acc +6"], (5, 8)),
        ]
    ),
)
def test(input_li, expected):
    assert compute(input_li) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
