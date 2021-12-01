import pytest


def initialise(s):
    li = s.split(',')
    d = {int(v): i+1 for i, v in enumerate(li[:-1])}
    prev = int(li[-1])
    return d, prev


def do(d, p, n):
    for i in range(len(d) + 1, n):
        old = p
        if old in d:
            p = i - d[old]
        else:
            p = 0
        d[old] = i
    return p


def compute(s):
    data, prev = initialise(s)
    ans1 = do(data, prev, 2020)
    data, prev = initialise(s)
    ans2 = do(data, prev, 30000000)
    return ans1, ans2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("0,3,6", 436),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('15/input.txt') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
