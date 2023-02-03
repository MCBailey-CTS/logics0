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

    temp = [1,2,3,4,]
    print(temp)
    print([*temp])
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

    # path = 'C:\Repos\logics0\solve_files'
    # for filename in glob.glob(os.path.join(path, '*')):
    #     with open(os.path.join(os.getcwd(), filename), 'r') as f:
    #         temp = os.path.split(filename)
    #
    #         result = '@pytest.mark.skip("skipped")\n'
    #         name = temp[1].split(".")[0]
    #         result += f'def test_{name}():\n'
    #         result += f'    puzzle_string = f"""\n'
    #         result += f'    {name}.sudoku\n'
    #         result += f'    9\n'
    #         result += f.read().replace('9 $ $ $ $ $ $ $ $', '', -1) + '\n'
    #         result += f'    """\n'
    #         result += f'    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())\n'
    #
    #         print(result)
    #         # print(f.read())
    import itertools
    from itertools import permutations

    # list0 = [1, 2, 3, 4, 5, 7, 8, 9]
    # list1 = [1, 2, 3, 4, 5, 7, 8, 9]
    # list2 = [6]
    # unique_combinations = []
    #
    # # Getting all permutations of list_1
    # # with length of list_2
    # permut = itertools.permutations(list0, len(list1))
    #
    # # zip() is called to pair each permutation
    # # and shorter list element into combination
    # for comb in permut:
    #     zipped = zip(comb, list1)
    #     unique_combinations.append(list(zipped))
    #
    # # printing unique_combination list
    # print(unique_combinations)
    # # print("main")
    # import itertools
    # a = [list0, list1, list2]
    #
    # for house in list(itertools.product(*a)):

    # print()
    # [(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 4, 10), (1, 5, 7), (1, 5, 8), (1, 5, 9), (1, 5, 10), (1, 6, 7), (1, 6, 8),
    #  (1, 6, 9), (1, 6, 10), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 4, 10), (2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 5, 10),
    #  (2, 6, 7), (2, 6, 8), (2, 6, 9), (2, 6, 10), (3, 4, 7), (3, 4, 8), (3, 4, 9), (3, 4, 10), (3, 5, 7), (3, 5, 8),
    #  (3, 5, 9), (3, 5, 10), (3, 6, 7), (3, 6, 8), (3, 6, 9), (3, 6, 10)]
