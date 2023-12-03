# Day 1: Trebuchet?!

from CY23 import input_load as load
import re
from word2number import w2n
import wordninja

def recover_calibration(input_filepath: str) -> int:
    """Takes the filepath of a text file, reads text file parses
    list of hard to read calibration values and recovers the correct
    numeric representation and returns the sum of those values.

        Parameters
        ----------
        input_filepath : str
            filepath to input txt file

        Returns
        -------
        int
            recovered calibration
        """
    input_file = load.txt_to_str(input_filepath)
    calibration_values = input_file.split("\n")
    calibration_doc = []
    # Run a split on first and last numeric
    # check any string that may exist outside of those for containing a spelled number.
    for art_value in calibration_values:
        split_values = wordninja.split(art_value)
        print(split_values)
        trimmed_values = []
        for val in split_values:
            try:
                trimmed_values.append(str(w2n.word_to_num(val)))
            except:
                pass
        numeric_value = int(trimmed_values[0][0] + trimmed_values[-1][-1])
        print(numeric_value)
        calibration_doc.append(numeric_value)
    calibration = sum(calibration_doc)
    print(calibration)
    return calibration

recover_calibration("test_input_p2.txt")
