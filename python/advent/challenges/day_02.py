from enum import Enum
from pathlib import Path
from typing import Iterable, Tuple

import functools
import typer


_FILE = Path(__file__).parent.parent.parent.parent / "_data" / "day_02.txt"


def _retrieve_lines():
    with _FILE.open('r') as f:
        while True:
            line = f.readline()
            yield line.strip()

            if not line.endswith("\n"):
                break



class Hand(Enum):
    rock = 0
    paper = 1
    scissors = 2

MAP_OPPONENT = {
    'A': Hand.rock,
    'B': Hand.paper,
    'C': Hand.scissors,
}

MAP_PLAYER = {
    'X': Hand.rock,
    'Y': Hand.paper,
    'Z': Hand.scissors,
}


def _pre_process(lines: Iterable[str]) -> Tuple[Hand, Hand]:
    for l in lines:
        oppenent, player = l.split(" ")
        yield (MAP_OPPONENT[oppenent], MAP_PLAYER[player])


HAND_SCORE = {
    Hand.rock : 1,
    Hand.paper : 2,
    Hand.scissors : 3,
}


PLAY_SCORE = {
    (Hand.rock, Hand.rock): 3,
    (Hand.rock, Hand.paper): 6,
    (Hand.rock, Hand.scissors): 0,
    (Hand.paper, Hand.rock): 0,
    (Hand.paper, Hand.paper): 3,
    (Hand.paper, Hand.scissors): 6,
    (Hand.scissors, Hand.rock): 6,
    (Hand.scissors, Hand.paper): 0,
    (Hand.scissors, Hand.scissors): 3,
}


def _calculate_score_player(opponent, player):
    return HAND_SCORE[player] + PLAY_SCORE[(opponent, player)]


def calculate():
    lines = _retrieve_lines()
    values = _pre_process(lines)
    return sum((_calculate_score_player(*v) for v in values))
