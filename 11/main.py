from copy import deepcopy

import pytest


def get_adj(li, i, j, d=1):
    if i-d < 0:
        x0 = 0
    else:
        x0 = i - d
    if i + d + 1 > len(li):
        x1 = len(li)
    else:
        x1 = i + d + 1

    if j-d < 0:
        y0 = 0
    else:
        y0 = j - d
    if j + d + 1 > len(li[i]):
        y1 = len(li[i])
    else:
        y1 = j + d + 1
    print(x0, x1, y0, y1)
    return li[x0:x1, y0:y1].flatten()


def is_seat(g, r, c):
    return g[r][c] == '#' or g[r][c] == 'L'


def get_adjacent(li, i, j, visible):
    rc, cc = len(li) - 1, len(li[0]) - 1
    adj = []
    directions = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]

    def in_boundary(r, c, d):
        return (r + d[0] >= 0 and r + d[0] <= rc) and \
                (c + d[1] >= 0 and c + d[1] <= cc)

    for d in directions:
        od = d
        while in_boundary(i, j, d):
            if not visible:
                adj.append(li[i + d[0]][j + d[1]])
                break
            elif is_seat(li, i + d[0], j + d[1]):
                adj.append(li[i + d[0]][j + d[1]])
                break
            else:
                d = (d[0] + od[0], d[1] + od[1])

    return adj


def empty(g, r, c):
    return g[r][c] == "L"


def occupied(g, r, c):
    return g[r][c] == '#'


def any_adj_occupied(g, r, c, visible, adj_func):
    return any(i == '#' for i in adj_func(g, r, c, visible))


def x_or_more_adj_occupied(g, x, r, c, visible, adj_func):
    return adj_func(g, r, c, visible).count("#") >= x


def arrive(g, x, r, c, visible=False):
    if empty(g, r, c) and not any_adj_occupied(g, r, c, visible, get_adjacent):
        return '#'
    if occupied(g, r, c) and \
            x_or_more_adj_occupied(g, x, r, c, visible, get_adjacent):
        return 'L'
    return g[r][c]


def part1(li):
    new = deepcopy(li)
    for i in range(len(li)):
        for j in range(len(li[i])):
            new[i][j] = arrive(li, 4, i, j)
    if new == li:
        count = 0
        for i in new:
            count += i.count('#')
        return count

    return part1(new)


def part2(li):
    new = deepcopy(li)
    for i in range(len(li)):
        for j in range(len(li[i])):
            new[i][j] = arrive(li, 5, i, j, True)
    if new == li:
        count = 0
        for i in new:
            count += i.count('#')
        return count

    return part2(new)


def compute(li):
    li = [[i for i in line] for line in li]
    return part1(li), part2(li)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (
            [
                "L.LL.LL.LL",
                "LLLLLLL.LL",
                "L.L.L..L..",
                "LLLL.LL.LL",
                "L.LL.LL.LL",
                "L.LLLLL.LL",
                "..L.L.....",
                "LLLLLLLLLL",
                "L.LLLLLL.L",
                "L.LLLLL.LL"
            ], (37, 26)
        ),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('11/input.txt') as f:
        print(compute(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
