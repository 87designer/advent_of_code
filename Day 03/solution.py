# Day 3: Rucksack Reorganization

import os
import sys
import re
import string
from typing import Tuple


def split_string(s: str) -> Tuple[str, str]:
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


def compare_compartments(input_filepath: str) -> Tuple[int, int]:
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
    int
        sum of the Badge Type Priorities
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
    groups = [x.strip().split('\n') for x in re.findall('((?:[^\n]+\n?){1,3})', input_file)]

    # Identify Item Rearrangement Priority
    item_rearrangement_priority = {}
    for rucksack in rucksacks:
        compartment1, compartment2 = split_string(rucksack)
        compartment1_lower, compartment2_lower = (list(filter(lambda c: c.islower(), c)) for c in [compartment1, compartment2])
        lower_item = list(set(compartment1_lower) & set(compartment2_lower))
        if lower_item:
            item_rearrangement_priority[rucksack] = {lower_item[0]: item_type_priority.get(lower_item[0])}

        compartment1_upper, compartment2_upper = (list(filter(lambda c: c.isupper(), c)) for c in [compartment1, compartment2])
        upper_item = list(set(compartment1_upper) & set(compartment2_upper))
        if upper_item:
            item_rearrangement_priority[rucksack] = {upper_item[0]: item_type_priority.get(upper_item[0])}

    # Identify Badge Rearrangement Priority
    badge_rearrangement_priority = {}
    for group in groups:
        pack1_lower, pack2_lower, pack3_lower = (list(filter(lambda c: c.islower(), g)) for g in group)
        lower_badge = list(set(pack1_lower) & set(pack2_lower) & set(pack3_lower))
        if lower_badge:
            badge_rearrangement_priority[tuple(group)] = {lower_badge[0]: item_type_priority.get(lower_badge[0])}

        pack1_upper, pack2_upper, pack3_upper = (list(filter(lambda c: c.isupper(), g)) for g in group)
        upper_badge = list(set(pack1_upper) & set(pack2_upper) & set(pack3_upper))
        if upper_badge:
            badge_rearrangement_priority[tuple(group)] = {upper_badge[0]: item_type_priority.get(upper_badge[0])}


    # Identify Sum of Item Type Priorities
    item_type_priorities = []
    for value in item_rearrangement_priority.values():
        for v in value.values():
            item_type_priorities.append(v)
    itp_sum = sum(item_type_priorities)

    # Identify Sum of Item Type Priorities
    badge_type_priorities = []
    for value in badge_rearrangement_priority.values():
        for v in value.values():
            badge_type_priorities.append(v)
    btp_sum = sum(badge_type_priorities)

    return itp_sum, btp_sum
