# Day 4: Supply Stacks

import os
import sys
import re
from typing import Tuple


def main(input_filepath):
    # Parse Text File Identifying Individual Rucksacks
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input_file = f.read()
    crate_drawing, rearrangement_procedure = (v for v in input_file.split("\n\n"))

    # Parse Crate Stacks
    crate_rows = crate_drawing.split("\n")
    number_of_stacks = int(crate_rows[-1][-1])
    row_list = []
    for crate_row in crate_rows[:-1]:
        row_list.append(re.findall(r"[\w]", crate_row.replace("    ", "_")))

    # Establish Matrix
    crate_matrix = {}
    for i in range(number_of_stacks):
        crate_matrix[i] = []
    for row in row_list:
        for i in range(len(row)):
            crate_matrix.get(i).insert(0, row[i])

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
        for i in range(m):
            crate_to_move = crate_matrix.get(f).pop(-1)
            crate_matrix.get(t).append(crate_to_move)

    # concat top containers
    ans = ''.join([c[-1] for c in sorted(crate_matrix.values())])

    return ans
