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

    breakpoint()

    print("hello world")


    # if re.match('file_check_\d+'):
    #
    #
    # prCyan("Hello World, ")
    # prYellow("It's")
    # prGreen("Geeks")
    # prRed("For")
    # prGreen("Geeks")
    #
    # f = open('C:\\repos\\logics0\\solve_files\\' + "finned_x_wing_00.sudoku", 'r')
    # from puzzles import Sudoku
    #
    # string = f'id.sudoku\n{f.read()}'.replace('$', '', -1)
    # f.close()
    #
    # # print(string)
    #
    # puzzle = Sudoku(string)
    # from techniques.CrossHatch import CrossHatch
    #
    # edits = 0
    #
    # puzzle.solve([CrossHatch(), HiddenSingle(), LockedCandidatesPointing(),
    #               # UniqueRectangleType4()
    #               ])
    # # in_cols = True
    #
    # for candidate in puzzle.expected_candidates():
    #     for i in range(len(puzzle)):
    #         house_col0 = puzzle.house_col(i, candidate)
    #         for ii in range(len(puzzle)):
    #             house_col1 = puzzle.house_col(ii, candidate)
    #
    #             containing_locs = house_col0 + house_col1
    #
    #             chute_dict = {}
    #             for loc in containing_locs:
    #                 chute = puzzle.loc_chute(loc)
    #                 if chute not in chute_dict:
    #                     chute_dict[chute] = set()
    #                 chute_dict[chute].add(loc)
    #
    #             fence_dict = {}
    #             for loc in containing_locs:
    #                 chute = puzzle.cell_fence(loc)
    #                 if chute not in fence_dict:
    #                     fence_dict[chute] = set()
    #                 fence_dict[chute].add(loc)
    #
    #             if len(chute_dict) != 4 or len(fence_dict) != 4:
    #                 continue
    #
    #             if not is_rectangle(list(chute_dict.keys())):
    #                 continue
    #
    #             fence_length_1 = [fence for fence in fence_dict.keys() if len(fence_dict[fence]) == 1]
    #             fence_greater_length_1 = [fence for fence in fence_dict.keys() if len(fence_dict[fence]) > 1]
    #
    #             if len(fence_length_1) != 3 or len(fence_greater_length_1) != 1:
    #                 continue
    #
    #             min_row_chute = min(chute0.row for chute0 in chute_dict.keys())
    #             max_row_chute = max(chute0.row for chute0 in chute_dict.keys())
    #
    #             min_col_chute = min(chute0.col for chute0 in chute_dict.keys())
    #             max_col_chute = max(chute0.col for chute0 in chute_dict.keys())
    #
    #             house_fence00 = puzzle.house_fence(fence_greater_length_1[0])
    #
    #             chute_temp = puzzle.loc_chute(house_fence00[0])
    #
    #             if chute_temp == Loc(min_row_chute, min_col_chute):
    #                 other_chute = Loc(min_row_chute, max_col_chute)
    #                 other_fence_house = puzzle.house_fence(puzzle.fence_from_chute(other_chute))
    #                 # need to check that the two cells in the lower are in the same row
    #                 lower_left_chute = Loc(max_row_chute, min_col_chute)
    #                 lower_right_chute = Loc(max_row_chute, max_col_chute)
    #                 temp0 = chute_dict[lower_left_chute]
    #                 temp1 = chute_dict[lower_right_chute]
    #                 temp2 = chute_dict[other_chute]
    #                 if len(temp0) == 1 and len(temp1) == 1 and len(temp2) == 1:
    #                     lower_left_loc: Loc = list(temp0)[0]
    #                     lower_right_loc: Loc = list(temp1)[0]
    #                     top_right_loc: Loc = list(temp2)[0]
    #
    #                     if lower_left_loc.row == lower_right_loc.row:
    #                         puzzle.override_loc_color(
    #                             puzzle.house_row(lower_left_loc.row) + puzzle.house_row(top_right_loc.row),
    #                             Fore.LIGHTMAGENTA_EX)
    #                         puzzle.override_loc_color(puzzle.house_col(i) + puzzle.house_col(ii), Fore.GREEN)
    #                         puzzle.override_loc_color(containing_locs, Fore.YELLOW)
    #                         fin = set(containing_locs).difference(
    #                             puzzle.house_row(lower_left_loc.row) + puzzle.house_row(top_right_loc.row))
    #                         remove = set(house_fence00).intersection(puzzle.house_row(top_right_loc.row)).difference(
    #                             containing_locs)
    #
    #                         puzzle.override_loc_color(list(fin), Fore.BLUE)
    #                         puzzle.override_loc_color(list(remove), Fore.RED)
    #                         edits += puzzle.rem(list(remove), [candidate])
    #
    # print(puzzle.to_string())
