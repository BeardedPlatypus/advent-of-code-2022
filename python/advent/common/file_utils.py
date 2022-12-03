from pathlib import Path


_DATA_DIRECTORY = Path(__file__).parent.parent.parent.parent / "_data"


def read_challenge_input_lines(file_name: str):
    file_path = _DATA_DIRECTORY / file_name

    with file_path.open('r') as f:
        while True:
            line = f.readline()
            yield line.strip()

            if not line.endswith("\n"):
                break
