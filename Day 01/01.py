# Day 1: Calorie Counting

import os
import sys

def elf_mooch_engine(input_filepath: str) -> int:
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
    """
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input = f.read()

    food_groups = input.split("\n\n")
    elf_count = len(food_groups)
    elves = {}

    for elf in range(elf_count):
        calories_carried = []
        separated_group = food_groups[elf].split("\n")
        for food_item in separated_group:
            calories_carried.append(int(food_item))
        elves[elf] = sum(calories_carried)

    return max(elves.values())
