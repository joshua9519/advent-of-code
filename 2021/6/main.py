import pytest


def compute(fishes, days):
    arr = [0 for i in range(9)]
    for i in fishes:
        arr[i] += 1
    for i in range(days):
        births = arr.pop(0)
        arr.append(births)
        arr[6] += births
    return sum(arr)


@pytest.mark.parametrize(
    ('fishes', 'days', 'expected'),
    (
        ([3, 4, 3, 1, 2], 18, 26),
        ([3, 4, 3, 1, 2], 80, 5934),
    ),
)
def test(fishes, days, expected):
    assert compute(fishes, days) == expected


def main():
    with open('6/input.txt') as f:
        fishes = [int(i) for i in f.read().split(",")]
        print(compute(fishes, 80), compute(fishes, 256))

    return 0


if __name__ == '__main__':
    exit(main())
