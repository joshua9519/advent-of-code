import argparse
import re

import pytest


def parse_line(li):
    tree = {}

    for s in li:
        outermost = ' '.join(s.split()[0:2])
        tree[outermost] = [{'name': i[2], 'weight': int(i[1])}
                           for i
                           in re.finditer(r'(\d) ([a-z]+ [a-z]+) bags?', s)]
    return tree


def find_colour(tree, value, colour):
    if value == colour:
        return True

    contains = False
    for i in tree[value]:
        e = i['name']
        contains |= find_colour(tree, e, colour)

    return contains


def find_colour_weight(tree, value):
    if not len(tree[value]):
        return 1

    sum = 1
    for i in tree[value]:
        sum += i['weight'] * find_colour_weight(tree, i['name'])

    return sum


def compute(li):
    tree = parse_line(li)
    colours = []
    for e in tree:
        if find_colour(tree, e, 'shiny gold') and e != 'shiny gold':
            colours.append(e)
    return len(colours), find_colour_weight(tree, 'shiny gold') - 1


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        [
            ([
                "light red bags contain 1 bright white bag, 2 muted yellow bags.",  # noqa: E501
                "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",  # noqa: E501
                "bright white bags contain 1 shiny gold bag.",
                "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",  # noqa: E501
                "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",  # noqa: E501
                "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",  # noqa: E501
                "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",  # noqa: E501
                "faded blue bags contain no other bags.",
                "dotted black bags contain no other bags."
            ], (4, 32)),
        ]
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
