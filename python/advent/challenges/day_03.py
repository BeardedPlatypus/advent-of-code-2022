from pathlib import Path
from typing import Iterable, Set, Tuple

import string


_FILE = Path(__file__).parent.parent.parent.parent / "_data" / "day_03.txt"


def _retrieve_lines():
    with _FILE.open('r') as f:
        while True:
            line = f.readline()
            yield line.strip()

            if not line.endswith("\n"):
                break


_PRIORITY_MAPPING = { c: i+1 for i, c in enumerate(string.ascii_letters)}


Element = Tuple[Set[str], Set[str]]


def _pre_process(lines: Iterable[str]) -> Iterable[Element]:
    for l in lines:
        split_index = int(len(l) / 2)
        yield (set(l[:split_index]), set(l[split_index:]))


def calculate():
    lines = _retrieve_lines()
    values = _pre_process(lines)
    
    def compute(left, right):
        return _PRIORITY_MAPPING[next(iter(left & right))]

    return sum((compute(*v) for v in values))
