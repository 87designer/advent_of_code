# Day 2: Rock Paper Scissors

import os
import sys
from collections import namedtuple


def encrypted_strategy_score_projector(input_filepath: str) -> int:
    """Takes the filepath of a text file, reads text file parses
    encrypted strategy guide for a game of Rock, Paper, Scissors
    and returns the total score if the guide is followed given
    assumptions outline in the puzzle.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        projected total score based on assumptions
    """
    # Construct Classes
    EncryptedStrategy = namedtuple("EncryptedStrategy", "opponent_play response")
    Outcome = namedtuple("Outcome", "score")
    HandShape = namedtuple("Shape", "score A B C")

    # Establish Outcome Rules
    win = Outcome(6)
    draw = Outcome(3)
    lose = Outcome(0)

    # Establish Assumed Hand Shapes
    x = HandShape(1, "draw", "lose", "win")
    y = HandShape(2, "win", "draw", "lose")
    z = HandShape(3, "lose", "win", "draw")

    # Parse Text File Identifying Individual Rounds
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input_file = f.read()
    input_lines = input_file.split("\n")
    rps_rounds = []
    for line in input_lines:
        line_items = line.split(" ")
        rps_rounds.append(EncryptedStrategy(line_items[0], line_items[1]))

    # Calculate Resulting Scores
    round_scores = []
    for rnd in rps_rounds:
        outcome = eval(f'{rnd.response.lower()}.{rnd.opponent_play}')
        score = eval(f'{outcome}.score + {rnd.response.lower()}.score')
        round_scores.append(score)

    projected_total_score = sum(round_scores)

    return projected_total_score
