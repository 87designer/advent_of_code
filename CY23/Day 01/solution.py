# Day 1: Trebuchet?!

from CY23 import input_load as load
import re


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
    for art_value in calibration_values:
        numeric_extract = re.findall(r'\d+', art_value)
        numeric_value = int(numeric_extract[0][0] + numeric_extract[-1][-1])
        calibration_doc.append(numeric_value)
    calibration = sum(calibration_doc)
    return calibration
