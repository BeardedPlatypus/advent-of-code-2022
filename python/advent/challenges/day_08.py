from advent.common import file_utils
from advent.common.parts import Part
from typing import Iterable, Sequence, TypeVar


def _preprocess(lines: Iterable[str]) -> Sequence[Sequence[int]]:
    # Outer list contains the rows
    return [[int (v) for v in l.strip()] for l in lines if l.strip()]


def _update_visibility(visibility: Sequence[bool], heights: Sequence[int]):
    current_heighest = heights[0]

    for i in range(len(visibility)):
        if visibility[i]:
            break
        if heights[i+1] > current_heighest:
            current_heighest = heights[i+1]
            visibility[i] = True


def _compute_visibility(row: Sequence[int]):
    visibility = [False, ] * (len(row) - 2)
    _update_visibility(visibility, list(reversed(row)))
    visibility = list(reversed(visibility))
    _update_visibility(visibility, row)
    return visibility


def _calculate_visibility_grid(grid: Sequence[Sequence[int]]):
    return [_compute_visibility(row) for row in grid]


T = TypeVar('T')

def _swap_row_column(grid: Sequence[Sequence[T]]) -> Sequence[Sequence[T]]:
    swapped = [list() for _ in range(len(grid[0]))]

    for row in grid:
        for i, v in enumerate(row):
            swapped[i].append(v)

    return swapped


def _calculate_visibility(grid: Sequence[Sequence[int]]) -> Sequence[Sequence[bool]]:
    x_visibility = _calculate_visibility_grid(grid[1:-1])
    y_visibility = _swap_row_column(_calculate_visibility_grid(_swap_row_column(grid)[1:-1]))

    return [
        [x_vis or y_vis for x_vis, y_vis in zip(x_row, y_row)] 
        for x_row, y_row in zip(x_visibility, y_visibility)
    ]


def _calculate_n_visible(visibility: Sequence[Sequence[bool]]) -> int:
    outer = (len(visibility) + 2) * 2 + (len(visibility[0]) * 2)
    inner = len([v for r in visibility for v in r if v])
    return outer + inner


def _update_scenic_row(scenic_values: Sequence[int], row: Sequence[int]) -> Sequence[int]:
    trees_from_current = [0,] * 10

    for i, v in enumerate(row):
        scenic_values[i] *= trees_from_current[v]

        # update trees from current
        trees_from_current[:v] = [0, ] * v
        trees_from_current[v] = 1
        for j in range(v + 1, 10):
            trees_from_current[j] += 1


def _compute_scenic(row: Sequence[int]):
    scenic = [1, ] * len(row)
    _update_scenic_row(scenic, list(reversed(row)))
    scenic = list(reversed(scenic))
    _update_scenic_row(scenic, row)
    return scenic


def _calculate_scenic_grid(grid: Sequence[Sequence[int]]):
    return [_compute_scenic(row) for row in grid]


def _calculate_scenic(grid: Sequence[Sequence[int]]) -> Sequence[Sequence[bool]]:
    x_scenic = _calculate_scenic_grid(grid)
    y_scenic = _swap_row_column(_calculate_scenic_grid(_swap_row_column(grid)))

    return [
        [x_scenic * y_scenic for x_scenic, y_scenic in zip(x_row, y_row)] 
        for x_row, y_row in zip(x_scenic, y_scenic)
    ]


def _calculate_max_scenic(scenic: Sequence[Sequence[int]]) -> int:
    return max((max(row) for row in scenic))


def calculate(part: Part) -> int:
    lines = file_utils.read_challenge_input_lines("day_08.txt")
    grid = _preprocess(lines)

    if part == Part.one:
        visibility = _calculate_visibility(grid)
        return _calculate_n_visible(visibility)
    else:
        scenic = _calculate_scenic(grid)
        return _calculate_max_scenic(scenic)
