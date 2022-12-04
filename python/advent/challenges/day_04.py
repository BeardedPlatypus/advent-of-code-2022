from advent.common import file_utils
from advent.common.parts import Part

from typing import Iterable, Tuple

import functools


Element = Tuple[Tuple[int, int], Tuple[int, int]]


def _preprocess(lines: Iterable[str]) -> Iterable[Element]:
    for l in lines:
        if not any(l.strip()):
            continue

        elf1, elf2 = l.split(',', 1)
        elf1_low, elf1_high = elf1.split('-', 1)
        elf2_low, elf2_high = elf2.split('-', 1)

        yield (int(elf1_low), int(elf1_high)), (int(elf2_low), int(elf2_high))


def _contains(assignment1: Tuple[int, int], assignment2: Tuple[int, int]):
    return (assignment1[0] >= assignment2[0] and assignment1[1] <= assignment2[1])


def calculate():
    lines = file_utils.read_challenge_input_lines("day_04.txt")
    values = _preprocess(lines)

    def compute(acc: int, elem: Element) -> int:
        if _contains(elem[0], elem[1]) or _contains(elem[1], elem[0]):
            return acc + 1
        else:
            return acc

    return functools.reduce(compute, values, 0)
