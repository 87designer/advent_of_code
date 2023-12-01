# Day 6: Tuning Trouble

import os
import sys


def comms_signal_lock(input_filepath: str, protocol: int) -> int:
    """Takes the filepath of a text file and reads datastream from
    text file. Following set protocol subroutine returns number of
    characters to process before start-of-packet marker.

    Parameters
    ----------
    input_filepath : str
        filepath to input txt file
    protocol : int
        sequence of n characters that are all different

    Returns
    -------
    int
        number of characters before start-of-packet marker
    """
    with open(os.path.join(sys.path[0], input_filepath), "r") as f:
        datastream = f.read()
    characters_to_process = protocol
    tuning = True
    while tuning:
        buffer = datastream[characters_to_process-protocol: characters_to_process]
        if len(set(buffer)) < protocol:
            characters_to_process += 1
        else:
            tuning = False

    return characters_to_process
