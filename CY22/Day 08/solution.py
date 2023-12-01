# Day 08: Treetop Tree House

import numpy as np
import input_load as load
from typing import Tuple


def check_dir_viz(viz_dir: list[bool], dir_list: list[int]):
    """Check visibility in a certain direction.
    """
    if all(viz_dir):
        dir_list.append('True')


def check_tree_view(viz_dir: list[bool], view_distance: list[int], reverse: bool):
    """Check number of trees that are visible in a certain direction.
    """
    if viz_dir:
        trees_viewed = 0
        if reverse:
            tree_list = reversed(viz_dir)
        else:
            tree_list = viz_dir
        for tree in tree_list:
            if tree:
                trees_viewed += 1
            if not tree:
                trees_viewed += 1
                break
        view_distance.append(trees_viewed)
    else:
        view_distance.append(0)


def count_visible_trees(input_filepath: str) -> Tuple[int, int]:
    """Takes the filepath of a text file and reads lines. Parses
    tree heights into 2d array then identifies how many trees are
    visible from outside the grid given their respective height.
    Also identifies highest scenic score possible of any tree.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        count of visible trees
    int
        highest scenic score
    """
    # Parse Data and Build Array
    input_file = load.txt_to_str(input_filepath)
    lines = input_file.strip().split()
    shape = (len(lines), len(lines[0]))
    data = [int(x) for x in ''.join(lines)]
    heights = np.array(data).reshape(shape)

    # Establish Count Logic
    visible_trees = 0
    highest_scenic_score = 0
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            row_viz = [heights[row][c] < heights[row][col] for c in range(len(heights[0]))]
            col_viz = [heights[r][col] < heights[row][col] for r in range(len(heights))]

            left = row_viz[:col]
            right = row_viz[col + 1:]
            top = col_viz[:row]
            bottom = col_viz[row + 1:]
            dir_lists = [(left, True), (right, False), (top, True), (bottom, False)]

            directional_visibility = []
            viewing_distance = []

            # Exterior trees
            if row in [0, len(heights) - 1] or col in [0, len(heights[row]) - 1]:
                visible_trees += 1

            # Interior Trees
            else:
                for direction, reverse in dir_lists:
                    check_dir_viz(direction, directional_visibility)
                if 'True' in set(directional_visibility):
                    visible_trees += 1

            for direction, reverse in dir_lists:
                check_tree_view(direction, viewing_distance, reverse)

            scenic_score = np.prod(viewing_distance)
            if scenic_score >= highest_scenic_score:
                highest_scenic_score = scenic_score

    return visible_trees, highest_scenic_score
