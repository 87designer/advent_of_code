# Day 4: Camp Cleanup

from CY22 import input_load as load
from typing import Tuple


def assignment_overlap_detector(input_filepath: str) -> Tuple[int, int]:
    """Takes the filepath of a text file, reads text file, parses pairs
    of section clean-up ranges, then returns the count of pairs where
    one range is completely contained in the other, followed by the count
    of pairs where there is any overlap at all.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        count of fully contained ranges
    int
        count of overlapping ranges
    """
    # Parse Text File Identifying Section Clean-up Pairs
    input_file = load.txt_to_str(input_filepath)

    pairs = [pair.split(",") for pair in input_file.split("\n")]
    full_range_pairs = []
    for pair in pairs:
        int_ranges = []
        for range_str in pair:
            start_stop_values = range_str.split("-")
            int_range = [i for i in range(int(start_stop_values[0]), int(start_stop_values[1]) + 1)]
            int_ranges.append(int_range)
        full_range_pairs.append(int_ranges)

    fully_contained_ranges = 0
    overlapping_ranges = 0

    for range_a, range_b in full_range_pairs:
        if range_a is range_b:
            fully_contained_ranges += 1
        else:
            if set(range_a).issubset(range_b) | set(range_b).issubset(range_a):
                fully_contained_ranges += 1
        if len(list(set(range_a) & set(range_b))) > 0:
            overlapping_ranges += 1

    return fully_contained_ranges, overlapping_ranges
