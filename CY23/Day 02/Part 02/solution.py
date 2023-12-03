# Day 2: Cube Conundrum

from CY23 import input_load as load


def sum_power_sets(input_filepath: str) -> int:
    """Finds the minimum set of cubes that must
    have been present and calculates the power
    of a set of cubes, (the multiplied minimum
    color requirements) returning the sum of
    the powers from each set.

        Parameters
        ----------
        input_filepath : str
            filepath to input txt file

        Returns
        -------
        int
            set power sum
        """
    input_file = load.txt_to_str(input_filepath)
    games = input_file.split("\n")
    set_powers = []
    for game in games:
        pull_list = [pulls.strip().split(", ") for pulls in game.split(":")[1].split(";")]
        pull_max = {'red': 0, 'green': 0, 'blue': 0}
        for pull in pull_list:
            for colors in pull:
                color = colors.split(" ")[-1]
                count = int(colors.split(" ")[0])
                if count > pull_max[color]:
                    pull_max[color] = count
        power = pull_max['red']*pull_max['green']*pull_max['blue']
        set_powers.append(power)
    id_sum = sum(set_powers)
    return id_sum
