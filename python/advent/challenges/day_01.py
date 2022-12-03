from pathlib import Path
from typing import Iterable, List

import functools


_FILE = Path(__file__).parent.parent.parent.parent / "_data" / "day_01.txt"


def _retrieve_lines():
    with _FILE.open('r') as f:
        while True:
            line = f.readline()
            yield line.strip()

            if not line.endswith("\n"):
                break


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
    lines = _retrieve_lines()
    values = _pre_process(lines)
    
    def compute_next(acc: List, v: int) -> List: 
        if v > acc[0]:
            acc[0] = v
            return sorted(acc)
        else:
            return acc

    return sum(functools.reduce(compute_next, values, [0,] * n))
