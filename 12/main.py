import math
import re

import pytest

compass = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

angles = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

rotation = {
    0: (1, 1),
    90: (1, -1),
    180: (-1, -1),
    270: ()
}


def parse(li):
    parsed = []
    for i in li:
        g = re.match(r'([NESWLRF])(\d+)', i).groups()
        parsed.append([g[0], int(g[1])])
    return parsed


def move(current_pos, current_dir, dir, value):
    if dir != 'F':
        movement = [i*value for i in compass[dir]]
    else:
        movement = [i*value for i in compass[current_dir]]
    new_pos = [sum(x) for x in zip(current_pos, movement)]
    return new_pos


def change_direction(current, dir, deg):
    if dir == 'R':
        new = (current + deg) % 360
    if dir == 'L':
        new = (current - deg) % 360
    return angles[new], new


def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])


def part1(li):
    pos = [0, 0, 90]
    direction = 'E'
    for i in li:
        if i[0] in ['L', 'R']:
            direction, pos[2] = change_direction(pos[2], i[0], i[1])
        else:
            pos[0:2] = move(pos[0:2], direction, i[0], i[1])
    return manhattan(pos)


def rotate(wp, angle):
    x0, y0 = wp
    x = int(x0*math.cos(angle) + y0*math.sin(angle))
    y = int(y0*math.cos(angle) - x0*math.sin(angle))
    return x, y


def move_to_wp(current, wp, value):
    movement = [i * value for i in wp]
    new = [sum(x) for x in zip(current, movement)]
    return new


def part2(li):
    wp_pos = [10, 1]
    boat = [0, 0]
    for i in li:
        if i[0] == 'L':
            for x in range(i[1] // 90):
                wp_pos = (-wp_pos[1], wp_pos[0])
        elif i[0] == 'R':
            for x in range(i[1] // 90):
                wp_pos = (wp_pos[1], -wp_pos[0])
        elif i[0] == 'F':
            boat = move_to_wp(boat, wp_pos, i[1])
        else:
            wp_pos = move(wp_pos, '', i[0], i[1])
    return manhattan(boat)


def compute(li):
    li = parse(li)
    pt1 = part1(li)
    pt2 = part2(li)
    return pt1, pt2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ([
            "F10",
            "N3",
            'E5',
            'S1',
            'W2',
            "F7",
            "R90",
            "L180",
            "F11"
        ], (33, 332)),
    ),
)
def test(input_s, expected):
    assert compute(input_s) == expected


def main():
    with open('12/input.txt') as f:
        print(compute(f.read().strip().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
