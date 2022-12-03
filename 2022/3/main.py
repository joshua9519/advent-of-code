import pytest
import string


def parse_1(slist):
    rucksacks = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in slist]

    return rucksacks


def get_score(common):
    if common.isupper():
        return ord(common) - 38
    elif common.islower():
        return ord(common) - 96
    return 0


def part1(rucksacks):
    score = 0
    for compartments in rucksacks:
        common = ""
        for i in compartments[0]:
            for j in compartments[1]:
                if i == j:
                    common = i
                    break
        score += get_score(common)

    return score


def parse_2(slist):
    groups = []
    for i in range(int(len(slist)/3)):
        groups.append(slist[i*3:(i+1)*3])
    return groups


def part2(rucksacks):
    score = 0
    for group in rucksacks:
        common = ""
        group.sort(key=len, reverse=True)
        for i in group[0]:
            for j in group[1]:
                if i == j:
                    for k in group[2]:
                        if i == k:
                            common = i
        score += get_score(common)
        
    return score


def compute(rucksacks):
    return part1(parse_1(rucksacks)), part2(parse_2(rucksacks))


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ([
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ],[
            ["vJrwpWtwJgWr", "hcsFMMfFFhFp"],
            ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"],
            ["PmmdzqPrV", "vPwwTWBwg"],
            ['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'],
            ['ttgJtRGJ', 'QctTZtZT'],
            ['CrZsJsPPZsGz', 'wwsLwLmpwMDw']
        ]),
    ),
)
def test_parse_1(input_s, expected):
    assert parse_1(input_s) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ([
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ],[
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg"
            ],
            [
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw"
            ],
        ]),
    ),
)
def test_parse_2(input_s, expected):
    assert parse_2(input_s) == expected


@pytest.mark.parametrize(
    ('rucksacks', 'expected'),
    (
        ([
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ],
        (157, 0)),
    ),
)
def test(rucksacks, expected):
    assert compute(rucksacks) == expected


def main():
    with open('input.txt') as f:
        rucksacks = f.read().splitlines()
        print(compute(rucksacks))

    return 0


if __name__ == '__main__':
    exit(main())
