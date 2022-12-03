from enum import Enum
from pathlib import Path
from typing import Iterable, Tuple


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


def _pre_process_1(lines: Iterable[str]) -> Tuple[Hand, Hand]:
    for l in lines:
        oppenent, player = l.split(" ")
        yield (MAP_OPPONENT[oppenent], MAP_PLAYER[player])


class Strategy(Enum):
    loss = 0
    draw = 1
    win = 2


MAP_STRATEGY = {
    'X': Strategy.loss,
    'Y': Strategy.draw,
    'Z': Strategy.win,
}


MAP_PLAYER_STRATEGY = {
    (Hand.rock, Strategy.loss) : Hand.scissors,
    (Hand.rock, Strategy.draw) : Hand.rock,
    (Hand.rock, Strategy.win) : Hand.paper,
    (Hand.paper, Strategy.loss) : Hand.rock,
    (Hand.paper, Strategy.draw) : Hand.paper,
    (Hand.paper, Strategy.win) : Hand.scissors,
    (Hand.scissors, Strategy.loss) : Hand.paper,
    (Hand.scissors, Strategy.draw) : Hand.scissors,
    (Hand.scissors, Strategy.win) : Hand.rock,
}


def _pre_process_2(lines: Iterable[str]) -> Tuple[Hand, Hand]:
    for l in lines:
        oppenent, player = l.split(" ")
        opponent_hand = MAP_OPPONENT[oppenent]
        player_strategy = MAP_STRATEGY[player]
        player_hand = MAP_PLAYER_STRATEGY[(opponent_hand, player_strategy)]

        yield (opponent_hand, player_hand)


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


class Mode(Enum):
    one = 0
    two = 1


def calculate(mode: Mode):
    lines = _retrieve_lines()

    if mode == Mode.one:
        pre_process = _pre_process_1
    elif mode == Mode.two:
        pre_process = _pre_process_2
    else:
        raise RuntimeError("Not supported")

    values = pre_process(lines)
    return sum((_calculate_score_player(*v) for v in values))
