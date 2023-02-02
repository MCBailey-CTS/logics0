# from Loc import Loc


def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))




if __name__ == "__main__":
    # next()
    # breakpoint()
    #
    # print("hello world")

    import os, glob


# @pytest.mark.skip("skipped")
# def test_minesweeper_005():
#     puzzle_string = f"""
#     005.minesweeper
#     6
#     +- 02 04 +- +- +-
#     +- +- +- +- 04 +-
#     01 +- +- +- 05 +-
#     +- 01 02 +- +- 03
#     01 01 +- 02 +- +-
#     +- +- 00 +- 01 +-
#     """
#     assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())

    # def test_power_grid_001():
    #     puzzle_string = f"""
    #     001.power_grid
    #     9
    #     10 10 10 10 10 10 10 10 10 01
    #     10 10 10 10 10 10 10 10 10 06
    #     10 10 10 10 10 10 10 10 10 01
    #     10 10 10 10 10 10 10 10 10 06
    #     10 10 10 10 10 10 10 10 10 02
    #     10 10 10 10 10 10 10 10 10 06
    #     10 10 10 10 10 10 10 10 10 01
    #     10 10 10 10 10 10 10 10 10 01
    #     10 10 10 10 10 10 10 10 10 01
    #     05 01 06 01 05 05 01 06 01 $$
    #     """
    #     assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())

    path = 'C:\Repos\logics0\solve_files'
    for filename in glob.glob(os.path.join(path, '*')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            temp = os.path.split(filename)

            result = '@pytest.mark.skip("skipped")\n'
            name = temp[1].split(".")[0]
            result += f'def test_{name}():\n'
            result += f'    puzzle_string = f"""\n'
            result += f'    {name}.sudoku\n'
            result += f'    9\n'
            result += f.read().replace('9 $ $ $ $ $ $ $ $', '', -1) + '\n'
            result += f'    """\n'
            result += f'    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())\n'

            print(result)
            # print(f.read())
