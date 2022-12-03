# Day 3: Rucksack Reorganization

import os
import sys
import string
from typing import Tuple


def split_string(s:str) -> Tuple[str, str]:
    """Takes a string with an even amount of characters and splits it into 2 strings.

        Parameters
        ----------
        s : str
            string to be split into 2 separate strings

        Returns
        -------
        str
            first half of original string
        str
            second half of original string
        """
    string1, string2 = s[:len(s) // 2], s[len(s) // 2:]
    return string1, string2


def compare_compartments(input_filepath: str) -> int:
    """Takes the filepath of a text file, reads text file parses
    rucksack item contents from 2 different pouches and identifies
    which item is present in each. Then prioritizes that item for
    rearrangement and returns the sum of the priority values.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        sum of the Item Type Priorities
    """
    # Establish Item Type Priority
    items = list(string.ascii_letters)
    item_type_priority = {}
    for i in range(len(items)):
        item_type_priority[items[i]] = i + 1

    # Parse Text File Identifying Individual Rucksacks
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input_file = f.read()
    rucksacks = input_file.split("\n")

    # Identify Item Rearrangement Priority
    rearrangement_priority = {}
    for rucksack in rucksacks:
        compartment1, compartment2 = split_string(rucksack)
        compartment1_lower = list(filter(lambda c: c.islower(), compartment1))
        compartment2_lower = list(filter(lambda c: c.islower(), compartment2))
        item_in_both_compartments = set(compartment1_lower) & set(compartment2_lower)
        lower_item = list(item_in_both_compartments)
        if lower_item:
            rearrangement_priority[rucksack] = {lower_item[0]: item_type_priority.get(lower_item[0])}

        compartment1_upper = list(filter(lambda c: c.isupper(), compartment1))
        compartment2_upper = list(filter(lambda c: c.isupper(), compartment2))
        item_in_both_compartments = set(compartment1_upper) & set(compartment2_upper)
        upper_item = list(item_in_both_compartments)
        if upper_item:
            rearrangement_priority[rucksack] = {upper_item[0]: item_type_priority.get(upper_item[0])}

    # Identify Sum of Item Type Priorities
    item_type_priorities = []
    for value in rearrangement_priority.values():
        for v in value.values():
            item_type_priorities.append(v)
    itp_sum = sum(item_type_priorities)

    return itp_sum
