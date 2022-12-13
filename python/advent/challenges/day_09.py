from advent.common import file_utils
from advent.common.parts import Part
from dataclasses import dataclass
from typing import Iterable, Tuple, Set, Sequence


def direction_from_value(value):
    match value:
        case "D":
            return (0, -1)
        case "U":
            return (0, +1)
        case "L":
            return (-1, 0)
        case "R":
            return (+1, 0)


@dataclass
class Motion:
    direction: Tuple[int, int]
    steps: int


def _preprocess(lines: Iterable[str]) -> Iterable[Motion]:
    def _convert(line: str) -> Motion:
        d, step = line.strip().split(" ", 1)
        return Motion(direction=direction_from_value(d), steps=int(step))

    return [_convert(l) for l in lines if l]


def _add(pos: Tuple[int, int], dir: Tuple[int, int]):
    return (pos[0] + dir[0], pos[1] + dir[1])


def _calculate_tail(curr_head, curr_tail):
    diff_x = abs(curr_head[0] - curr_tail[0])
    diff_y = abs(curr_head[1] - curr_tail[1])

    x = 0
    y = 0

    if diff_x >= 2 or (diff_y >= 2 and diff_x == 1):
        x = 1 * (1 if curr_head[0] > curr_tail[0] else -1)
    if diff_y >= 2 or (diff_x >= 2 and diff_y == 1):
        y = 1 * (1 if curr_head[1] > curr_tail[1] else -1)

    return _add(curr_tail, (x, y))


def _move(
    rope: Sequence[Tuple[int, int]], 
    motion: Motion, 
    tail_positions: Set[Tuple[int, int]],
) -> Set[Tuple[int, int]]:
    curr_rope = list(rope)

    for _ in range(motion.steps):
        curr_rope[0] = _add(curr_rope[0], motion.direction)

        for i in range(1, len(rope)):
            curr_rope[i] = _calculate_tail(curr_rope[i-1], curr_rope[i])

        tail_positions.add(curr_rope[-1])

    return curr_rope


def calculate(part: Part):
    lines = file_utils.read_challenge_input_lines("day_09.txt")
    motions = _preprocess(lines)

    rope = [(0, 0),] * (2 if part == Part.one else 10)
    tail_positions = {rope[-1],}
    for m in motions:
        rope = _move(rope, m, tail_positions)

    return len(tail_positions)  
