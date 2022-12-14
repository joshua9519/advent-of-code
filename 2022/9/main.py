import pytest


def move_piece(coord, direction):
    x, y = coord
    match direction:
        case "U":
            return (x, y + 1)
        case "D":
            return (x, y - 1)
        case "L":
            return (x - 1, y)
        case "R":
            return (x + 1, y)
        case "UL":
            return (x - 1, y + 1)
        case "UR":
            return (x + 1, y + 1)
        case "DL":
            return (x - 1, y - 1)
        case "DR":
            return (x + 1, y - 1)


def tail_move(head_coord, tail_coord):
    hx, hy = head_coord
    tx, ty = tail_coord

    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:  # touching - don't need to move
        return tail_coord

    if hx == tx:  # T is directly above or below H
        if ty > hy:
            return move_piece(tail_coord, "D")
        return move_piece(tail_coord, "U")
    elif hy == ty:  # T is directly left or right of H
        if tx > hx:
            return move_piece(tail_coord, "L")
        return move_piece(tail_coord, "R")
    elif ty > hy and tx > hx:
        return move_piece(tail_coord, "DL")
    elif ty > hy and tx < hx:
        return move_piece(tail_coord, "DR")
    elif ty < hy and tx < hx:
        return move_piece(tail_coord, "UR")
    elif ty < hy and tx > hx:
        return move_piece(tail_coord, "UL")


def part1(moves):
    H = (0, 0)
    T = (0, 0)
    visited = {T}
    for move in moves:
        direction, amount = move
        for _ in range(int(amount)):
            H = move_piece(H, direction)
            T = tail_move(H, T)
            visited.add(T)

    return len(visited)


def part2(moves):
    knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    visited = {knots[9]}

    for move in moves:
        direction, amount = move
        for _ in range(int(amount)):
            knots[0] = move_piece(knots[0], direction)
            for i in range(1, len(knots)):
                knots[i] = tail_move(knots[i - 1], knots[i])
            visited.add(knots[9])

    return len(visited)


def compute(input_):
    return part1(input_), part2(input_)


@pytest.mark.parametrize(
    ('input_', 'expected'),
    (
        (
            [
                ['R', '5'],
                ['U', '8'],
                ['L', '8'],
                ['D', '3'],
                ['R', '17'],
                ['D', '10'],
                ['L', '25'],
                ['U', '20']
            ],
            (88, 36)
        ),
    ),
)
def test(input_, expected):
    assert compute(input_) == expected


def main():
    with open('9/input.txt') as f:
        input_ = [s.split() for s in f.read().splitlines()]
        print(compute(input_))

    return 0


if __name__ == '__main__':
    exit(main())
