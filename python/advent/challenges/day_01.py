from pathlib import Path
from typing import Iterable

import functools


_FILE = Path(__file__).parent.parent.parent.parent / "_data" / "day_01.txt"


def _retrieve_lines():
    with _FILE.open('r') as f:
        while True:
            line = f.readline()
            yield line.strip()

            if not line.endswith("\n"):
                break


def _pre_process(lines: Iterable[str]):
    value = 0
    for l in lines:
        if l.strip() == "":
            yield value
            value = 0
        else:
            value += int(l)

    if value != 0:
        yield value


def calculate():
    # open lines
    lines = _retrieve_lines()
    values = _pre_process(lines)
    return functools.reduce(max, values, 0)
