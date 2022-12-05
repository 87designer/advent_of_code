# Day 2: Rock Paper Scissors

import os
import sys
from collections import namedtuple


def encrypted_strategy_score_projector(input_filepath: str) -> int:
    """Takes the filepath of a text file, reads text file parses
    encrypted strategy guide for a game of Rock, Paper, Scissors
    and returns the total score if the guide is followed given
    confirmed rules outlined in part 2 of the puzzle.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file

    Returns
    -------
    int
        projected total score based on updated rules
    """
    # Construct Classes
    EncryptedStrategy = namedtuple("EncryptedStrategy", "opponent_play desired_outcome")
    DesiredOutcome = namedtuple("DesiredOutcome", "score A B C")
    HandShapeScore = namedtuple("HandShapeScore", "score")

    # Establish HandShape Scores
    a = HandShapeScore(1)
    b = HandShapeScore(2)
    c = HandShapeScore(3)

    # Establish Desired Output Scores & HandShapes
    x = DesiredOutcome(0, "c", "a", "b")
    y = DesiredOutcome(3, "a", "b", "c")
    z = DesiredOutcome(6, "b", "c", "a")

    # Parse Text File Identifying Individual Rounds
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        input_file = f.read()
    input_lines = input_file.split("\n")
    rps_rounds = []
    for line in input_lines:
        line_items = line.split(" ")
        rps_rounds.append(EncryptedStrategy(line_items[0], line_items[1]))

    # Calculate Resulting Scores
    projected_total_score = 0
    for rnd in rps_rounds:
        strategic_hand_shape = eval(f'{rnd.desired_outcome.lower()}.{rnd.opponent_play}')
        projected_total_score += eval(f'{rnd.desired_outcome.lower()}.score + {strategic_hand_shape}.score')

    return projected_total_score
