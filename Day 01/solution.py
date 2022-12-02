# Day 1: Calorie Counting

import os
import sys
from typing import Tuple


def elf_mooch_engine(input_filepath: str) -> Tuple[int, int]:
    """Takes the filepath of a text file, which captures the Calories
    contained by the various meals, snacks, rations, etc. that the
    group of elves brought with them and identifies the total calories
    carried by the elf carrying the most.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        calorie count from elf carrying the most calories
    int
        total calorie count from top 3 elves carrying the most calories
    """
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input_file = f.read()

    food_groups = input_file.split("\n\n")
    elf_count = len(food_groups)
    elves = {}

    for elf in range(elf_count):
        calories_carried = []
        separated_group = food_groups[elf].split("\n")
        for food_item in separated_group:
            calories_carried.append(int(food_item))
        elves[elf] = sum(calories_carried)

    # Part 1 Solution
    elf_with_most_calories = max(elves.values())

    elves_sorted = dict(sorted(elves.items(), key=lambda item: item[1]))

    # Part 2 Solution
    total_calories_of_top_3 = sum(list(elves_sorted.values())[-3:])

    return elf_with_most_calories, total_calories_of_top_3
