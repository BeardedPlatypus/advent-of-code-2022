from dataclasses import dataclass
from typing import Sequence
import re

from advent.common import file_utils
from advent.common.parts import Part


Stack = Sequence[str]


def _get_index_with_default(l: Sequence[Stack], index: int):
    for _ in range((index + 1) - len(l)):
        l.append([])
    return l[index]


def _read_initial_state(lines: Sequence[str]):
    result = []

    for l in lines:
        if "[" not in l:
            # Once lines no longer contain [], then we have finished parsing our
            # initial stack.
            break

        index = 0
        while l:
            next_elem = l[1]
            if next_elem != " ":
                _get_index_with_default(result, index).append(next_elem)
            l = l[4:]
            index += 1
    
    # Note that the elements are sorted from top to bottom.
    return result


@dataclass
class Instruction:
    n_crates: int
    src_stack: int
    dst_stack: int


instruction_regex = re.compile("^move (?P<n>\d+) from (?P<src>\d+) to (?P<dst>\d+)$")


def _read_instructions(lines: Sequence[str]):
    for l in lines:
        if not l.startswith("move"):
            continue

        matched = instruction_regex.match(l)
        yield Instruction(
            n_crates=int(matched.group('n')),
            src_stack=int(matched.group('src')) - 1,
            dst_stack=int(matched.group('dst')) - 1,
        )

def _execute_instruction(stacks: Sequence[Stack], instruction: Instruction, reverse: bool):
    elems_to_move = stacks[instruction.src_stack][:instruction.n_crates]
    if reverse:
        elems_to_move = list(reversed(elems_to_move))

    stacks[instruction.src_stack] = stacks[instruction.src_stack][instruction.n_crates:]
    stacks[instruction.dst_stack] = elems_to_move + stacks[instruction.dst_stack]


def calculate(part: Part) -> int:
    lines = file_utils.read_challenge_input_lines("day_05.txt")
    state = _read_initial_state(lines)

    reverse_crates = part == Part.one
    for instruction in _read_instructions(lines):
        _execute_instruction(state, instruction, reverse_crates)

    return "".join(s[0] if len(s) > 0 else " " for s in state)
