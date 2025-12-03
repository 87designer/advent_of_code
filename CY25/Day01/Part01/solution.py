# Day 1: Secret Entrance
from CY25 import input_load as load


def zero_stop_count(input_filepath: str, starting_point: int = 50) -> int:
    """Takes the filepath of a text file, reads text file and parses
    dial rotation sequence and captures the number of times the dial
    is left pointing at 0 after any rotation in the sequence, the 
    sum of which is the password. Initial dial starting point is 50.

        Parameters
        ----------
        input_filepath : str
            filepath to input txt file
        
        starting_point : int
            filepath to input txt file

        Returns
        -------
        int
            password
        """
    combination_document = load.txt_to_str(input_filepath)
    rotation_sequence = combination_document.split("\n")  
    dial_numbers = [i for i in range(100)]
    stoping_point = starting_point
    password = 0

    for rotation in rotation_sequence:
        if rotation[0] == "L":
            clicks = -int(rotation[1:])
        else:
            clicks = int(rotation[1:])
        
        new_dial_index = (stoping_point + clicks) % 100
        new_dial_position = dial_numbers[new_dial_index]
        stoping_point = new_dial_position
        if stoping_point == 0:
            password += 1
    
    return password