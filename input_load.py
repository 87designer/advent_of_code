import os
import sys


def txt_to_str(input_filepath: str) -> str:
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input_file = f.read()
    return input_file
