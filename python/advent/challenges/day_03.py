from advent.common import file_utils

from enum import Enum
from typing import Iterable, Set, Sequence, Tuple

import functools
import string


_PRIORITY_MAPPING = { c: i+1 for i, c in enumerate(string.ascii_letters)}


ElementPart1 = Tuple[Set[str], Set[str]]
ElementPart2 = Tuple[Set[str], Set[str]]

def _pre_process_part1(lines: Iterable[str]) -> Iterable[ElementPart1]:
    for l in lines:
        split_index = int(len(l) / 2)
        yield (set(l[:split_index]), set(l[split_index:]))


def _pre_process_part2(lines: Iterable[str]) -> Iterable[ElementPart2]:
    i = 0
    acc = ()
    for l in lines:
        i += 1
        acc += (set(l),)

        if i == 3:
            yield acc
            acc = ()
            i = 0


class Mode(Enum):
    one = 0
    two = 1


def calculate(mode: Mode):
    lines = file_utils.read_challenge_input_lines("day_03.txt")

    if mode == Mode.one:
        values: Sequence[set[str]] = _pre_process_part1(lines)
    elif mode == Mode.two:
        values: Sequence[set[str]] = _pre_process_part2(lines)
    else:
        raise ValueError()
    
    def compute(elements: Sequence[Set[str]]):
        return _PRIORITY_MAPPING[next(iter(functools.reduce((lambda s1, s2: s1 & s2), elements)))]

    return sum((compute(v) for v in values))
