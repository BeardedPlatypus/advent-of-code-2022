from advent.common import file_utils
from advent.common.parts import Part


def _find_first_unique_batch(data: str, batch_size: int) -> int:
    for i in range(len(data) - batch_size):
        if len(set(data[i:i+batch_size])) == batch_size:
            return i + batch_size
    return -1


def calculate(part: Part) -> int:
    data = next(file_utils.read_challenge_input_lines("day_06.txt"))
    batch_size = 4 if part == Part.one else 14
    return _find_first_unique_batch(data, batch_size)
