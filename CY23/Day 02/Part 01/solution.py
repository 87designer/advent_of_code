# Day 2: Cube Conundrum

from CY23 import input_load as load


def sum_game_ids(input_filepath: str, cube_counts: dict) -> int:
    """Determines which games would have been possible given
    loading the bag with the specified cube counts in the dictionary.

        Parameters
        ----------
        input_filepath : str
            filepath to input txt file
        cube_counts : dict
            number of each color cubes {r:#, g:#, b:#}

        Returns
        -------
        int
            possible ID sum
        """
    input_file = load.txt_to_str(input_filepath)
    games = input_file.split("\n")
    possible_games = []
    for game in games:
        game_index = int(game.split(":")[0].split(" ")[-1])
        pull_list = [pulls.strip().split(", ") for pulls in game.split(":")[1].split(";")]
        pull_max = {'red': 0, 'green': 0, 'blue': 0}
        for pull in pull_list:
            for colors in pull:
                color = colors.split(" ")[-1]
                count = int(colors.split(" ")[0])
                if count > pull_max[color]:
                    pull_max[color] = count
        if pull_max['red'] <= cube_counts['red'] \
                and pull_max['green'] <= cube_counts['green'] \
                and pull_max['blue'] <= cube_counts['blue']:
            possible_games.append(game_index)
    id_sum = sum(possible_games)
    return id_sum
