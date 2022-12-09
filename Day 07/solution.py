# Day 7: No Space Left On Device

import input_load as load
from typing import Tuple


def find_space(input_filepath: str) -> Tuple[int, int]:
    """Takes the filepath of a text file and reads lines from
    terminal output. Parses terminal commands and sums directories
    with a total size of at most 100000 as well as identifies size
    of smallest viable folder for deletion.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        sum size of folders <= 100000
    int
        size of smallest viable folder for deletion
    """
    folders = {}
    filepath = []

    # Parse Text File Identifying Terminal Output Lines
    input_file = load.txt_to_str(input_filepath)
    lines = [line for line in input_file.strip().split('\n')]
    for line in lines:
        line_data = line.strip().split()
        if line_data[1] == 'cd':
            if line_data[2] == '..':
                filepath.pop()
            else:
                filepath.append(line_data[2])
        elif line_data[1] == 'ls':
            continue
        elif line_data[0] == 'dir':
            continue
        else:
            folder_size = int(line_data[0])
            for i in range(1, len(filepath)+1):
                path = '/'.join(filepath[:i])
                if path in folders.keys():
                    size_count = {path: (folders.get(path) + folder_size)}
                    folders.update(size_count)
                else:
                    folders.setdefault(path, folder_size)

    # Disk Space
    total = 70000000
    needed = 30000000
    used = folders.get('/')
    used_target = total-needed

    # Puzzle Answers
    total_size = 0
    viable_folders = []

    for folder, size in folders.items():
        if size <= 100000:
            total_size += size
        if (used-size) <= used_target:
            viable_folders.append(size)

    smallest_viable = sorted(viable_folders)[0]

    return total_size, smallest_viable
