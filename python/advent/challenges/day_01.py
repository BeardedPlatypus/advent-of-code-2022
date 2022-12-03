from advent.common import file_utils
from typing import Iterable, List

import functools


def _pre_process(lines: Iterable[str]) -> Iterable[int]:
    value = 0
    for l in lines:
        if l.strip() == "":
            yield value
            value = 0
        else:
            value += int(l)

    if value != 0:
        yield value


def calculate(n: int):
    lines = file_utils.read_challenge_input_lines("day_01.txt")
    values = _pre_process(lines)
    
    def compute_next(acc: List, v: int) -> List: 
        if v > acc[0]:
            acc[0] = v
            return sorted(acc)
        else:
            return acc

    return sum(functools.reduce(compute_next, values, [0,] * n))
