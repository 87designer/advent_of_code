# Day 4: Supply Stacks

from CY22 import input_load as load
import re


def rearrange_crates(input_filepath: str) -> str:
    """Takes the filepath of a text file, reads text file, parses stacks
    of supply crates and rearrangement procedure, and projects which supply
    crates will be on the top of each stack after rearrangement is complete.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    str
        characters identifying top top crate on each stack
    """
    # Parse Text File Identifying Supply Crate Stack Drawing & Rearrangement Procedures List
    input_file = load.txt_to_str(input_filepath)
    crate_drawing, rearrangement_procedure = (v for v in input_file.split("\n\n"))

    # Parse Crate Stacks
    crate_level_strings = crate_drawing.split("\n")
    number_of_stacks = int(crate_level_strings[-1][-1])
    crate_levels = []
    for string in crate_level_strings[:-1]:
        crate_levels.append(re.findall(r"[\w]", string.replace("    ", "_")))

    # Establish Matrix
    crate_matrix = {}
    for i in range(number_of_stacks):
        crate_matrix[i] = []
    for level in crate_levels:
        for i in range(len(level)):
            crate_matrix.get(i).insert(0, level[i])

    # Relabel stack names to align with procedure
    for i in reversed(range(number_of_stacks)):
        crate_matrix[i+1] = crate_matrix.pop(i)

    # Remove Placeholder
    for k, v in crate_matrix.items():
        crate_matrix[k] = [i for i in v if i != '_']

    # establish movement logic
    procedures = rearrangement_procedure.split("\n")
    procedure_matrix = []
    for p in procedures:
        procedure_matrix.append([int(x) for x in p.split() if x.isdigit()])

    # establish container matrix update logic
    for procedure in procedure_matrix:
        m, f, t = (i for i in procedure)
        crate_to_move = crate_matrix.get(f)[-m:]
        del crate_matrix.get(f)[-m:]
        crate_matrix.get(t).extend(crate_to_move)

    # concat top containers
    top_crates = ''.join([v[-1] for k, v in sorted(crate_matrix.items())])

    return top_crates
