# Day 1: Calorie Counting

import input_load as load
from typing import Tuple


def elf_mooch_engine(input_filepath: str) -> Tuple[int, int]:
    """Takes the filepath of a text file, reads text file parses
    list of calories and returns calorie count for the elf
    carrying the most calories as well as the total calorie count
    of the top 3 elves in terms of calorie count.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        calorie count from top elf
    int
        total calorie count from top 3 elves
    """
    input_file = load.txt_to_str(input_filepath)

    food_groups = input_file.split("\n\n")
    elf_count = len(food_groups)
    elf_roster = {}

    for elf in range(elf_count):
        calories_carried = []
        separated_group = food_groups[elf].split("\n")
        for food_item in separated_group:
            calories_carried.append(int(food_item))
        elf_roster[elf] = sum(calories_carried)

    # Part 1 Solution
    elf_with_most_calories = max(elf_roster.values())

    sorted_elf_roster = dict(sorted(elf_roster.items(), key=lambda item: item[1]))

    # Part 2 Solution
    total_calories_of_top_3 = sum(list(sorted_elf_roster.values())[-3:])

    return elf_with_most_calories, total_calories_of_top_3
