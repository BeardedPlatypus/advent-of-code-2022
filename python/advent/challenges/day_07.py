from advent.common import file_utils
from advent.common.parts import Part
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


@dataclass
class ElfFile:
    path: Path
    size: int


@dataclass
class ElfDir:
    path: Path
    files: List[Path]
    subdirs: List[Path]
    size: Optional[int] = None


def _calculate_sizes(dirs: Dict[Path, ElfDir], files: Dict[Path, ElfFile]):
    to_evaluate = list(dirs.keys())
    while to_evaluate:
        next_dir_path = to_evaluate.pop()
        dir = dirs[next_dir_path]

        if dir.size is not None:
            continue

        subdirs = [dirs[sd] for sd in dir.subdirs]
        if any((sd).size is None for sd in subdirs):
            to_evaluate.append(next_dir_path)
            to_evaluate += dir.subdirs
        else:
            dir.size = sum((sd.size for sd in subdirs)) + sum(files[fp].size for fp in dir.files)


def _build_file_structure(lines: Iterable[str]):
    files = {}
    current_path = Path("/")
    current_dir = ElfDir(path = current_path, files=[], subdirs=[])
    dirs = {
        current_path: current_dir
    }

    lines = (l.strip() for l in lines)
    for l in lines:
        if not l or l == "$ ls":
            continue
        if l == "$ cd /":
            current_path = Path("/")
            current_dir =  dirs[current_path]
            continue
        if l == "$ cd ..":
            current_path = current_path.parent
            current_dir = dirs[current_path]
            continue
        if l.startswith("$ cd "):
            dir_name = l[5:]
            current_path = current_path / dir_name
            current_dir =  dirs.setdefault(
                current_path, ElfDir(path = current_path, files=[], subdirs=[])
            )
            continue
        if l.startswith("dir"):
            dir = l.split(" ", 1)[-1]
            current_dir.subdirs.append(current_path / dir)
            continue
        
        file_size, file_name = l.split(" ", 1)
        file_path = current_path / file_name
        current_dir.files.append(file_path)
        files[file_path] = ElfFile(path=file_path, size=int(file_size))
    return dirs, files


def calculate(part: Part) -> int:
    lines = file_utils.read_challenge_input_lines("day_07.txt")
    dirs, files = _build_file_structure(lines)
    _calculate_sizes(dirs, files)

    if part == Part.one:
        return sum((d.size for d in dirs.values() if d.size <= 100000))
    else:
        delete_size = 30000000 -(70000000 - dirs[Path("/")].size)
        return min((d.size for d in dirs.values() if d.size > delete_size))
