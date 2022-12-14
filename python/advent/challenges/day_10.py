from advent.common import file_utils
from advent.common.parts import Part
from enum import Enum
from typing import Iterable, Tuple, Union


class Operation(Enum):
    noop = 1
    addx = 2


Element = Union[Operation.noop, Tuple[Operation.addx, int]]


def _preprocess(lines: Iterable[str]) -> Iterable[Element]:
    lines = (l.strip() for l in lines)
    for l in lines:
        if not l:
            continue

        if l == "noop":
            yield Operation.noop
        else:
            val = int(l.split(" ", 1)[-1])
            yield (Operation.addx, val)


def _calculate(elements: Iterable[Element], values_to_verify) -> int:
    result = 0

    curr_value = 1
    prev_value = None
    cycle = 1

    # pop defaults to end, so we reverse the elems
    to_verify = list(reversed(values_to_verify))  
    next_element = to_verify.pop()

    for e in elements:
        prev_value = curr_value
        if e == Operation.noop:
            cycle += 1
        else:
            cycle += 2
            curr_value += e[1]

        if cycle >= next_element:
            if cycle == next_element:
                result += curr_value * next_element
            else:
                result += prev_value * next_element

            if to_verify:
                next_element = to_verify.pop()
            else:
                break

    return result


def _calculate_screen(elements: Iterable[Element]) -> str:
    pixels = ""
    cycle = 1
    value = 1

    def add_pixel(c, v):
        if abs((c % 40)  - v) <= 1:
            return "#"
        else:
            return "."

    for e in elements:
        if e == Operation.noop:
            pixels += add_pixel(cycle, value)
            cycle += 1
        else:
            pixels += add_pixel(cycle, value)
            cycle += 1
            value += e[1]
            pixels += add_pixel(cycle, value)
            cycle += 1

        if cycle > 240:
            break

    return "\n" + "\n".join((
        pixels[:40], 
        pixels[40:80], 
        pixels[80:120], 
        pixels[120:160], 
        pixels[160:200], 
        pixels[200:240],
    ))


def calculate(part: Part):
    lines = file_utils.read_challenge_input_lines("day_10.txt")
    elements = _preprocess(lines)

    if part == Part.one:
        return _calculate(elements, [20, 60, 100, 140, 180, 220])
    else:
        return _calculate_screen(elements)
