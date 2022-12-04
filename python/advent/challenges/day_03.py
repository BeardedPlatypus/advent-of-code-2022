from advent.common import file_utils
from advent.common.parts import Part

from typing import Iterable, Set, Sequence, Tuple

import functools
import string


_PRIORITY_MAPPING = { c: i+1 for i, c in enumerate(string.ascii_letters)}


Element = Sequence[Set[str]]

def _pre_process_part1(lines: Iterable[str]) -> Iterable[Element]:
    for l in lines:
        split_index = int(len(l) / 2)
        yield (set(l[:split_index]), set(l[split_index:]))


def _pre_process_part2(lines: Iterable[str]) -> Iterable[Element]:
    i = 0
    acc = ()
    for l in lines:
        i += 1
        acc += (set(l),)

        if i == 3:
            yield acc
            acc = ()
            i = 0


PREPROCESSES = {
    Part.one: _pre_process_part1,
    Part.two: _pre_process_part2,
}


def calculate(part: Part):
    lines = file_utils.read_challenge_input_lines("day_03.txt")
    values = PREPROCESSES[part](lines)

    def compute(elements: Sequence[Set[str]]):
        return _PRIORITY_MAPPING[next(iter(functools.reduce((lambda s1, s2: s1 & s2), elements)))]

    return sum((compute(v) for v in values))
