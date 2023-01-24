from unittest import TestCase
from techniques.Technique import Technique
from puzzles import Sudoku
from Loc import Loc
from colorama import Fore


class ShashimiXWing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        # row0 = puzzle.house_row(2)
        # row1 = puzzle.house_row(6)
        #
        # row0_string = Technique.house_to_string(puzzle, row0)
        # row1_string = Technique.house_to_string(puzzle, row1)
        #
        # if row0_string == '_23456789a_23456789a123456789a_23456789b_23456789b_23456789b_23456789c123456789c123456789c' and \
        #         row1_string == '_23456789g_23456789g123456789g_23456789h_23456789h_23456789h123456789i_23456789i_23456789i':
        #     base0 = Loc(2, 2)
        #     base1 = Loc(6, 2)
        #     single_fin = Loc(6, 6)
        #     two_fin = [Loc(2, 7), Loc(2, 8)]
        #     remove = [Loc(1, 6), Loc(0, 6)]
        #     puzzle.override_loc_color(row0 + row1, Fore.GREEN)
        #     puzzle.override_loc_color(two_fin, Fore.LIGHTBLUE_EX)
        #     puzzle.override_loc_color(remove, Fore.LIGHTRED_EX)
        #     puzzle.override_loc_color([base0, base1, single_fin], Fore.YELLOW)
        #     edits += puzzle.rem(remove, [1])
        #
        # if row0_string == '_23456789a_23456789a123456789a_23456789b_23456789b_23456789b_23456789c123456789c_23456789c' and \
        #         row1_string == '_23456789g_23456789g123456789g_23456789h_23456789h_23456789h123456789i_23456789i_23456789i':
        #     base0 = Loc(2, 2)
        #     base1 = Loc(6, 2)
        #     single_fin = [Loc(6, 6), Loc(2, 7)]
        #     remove = [Loc(1, 6), Loc(0, 6), Loc(8, 7), Loc(7, 7)]
        #     puzzle.override_loc_color(row0 + row1, Fore.GREEN)
        #     puzzle.override_loc_color(single_fin, Fore.LIGHTBLUE_EX)
        #     puzzle.override_loc_color(remove, Fore.LIGHTRED_EX)
        #     puzzle.override_loc_color([base0, base1], Fore.YELLOW)
        #     edits += puzzle.rem(remove, [1])
        #
        # # row0 = puzzle.house_col(3)
        # # row1 = puzzle.house_col(6)
        #
        # row0_string = "".join([puzzle.grid[loc.row][loc.col] for loc in row0])
        # row1_string = "".join([puzzle.grid[loc.row][loc.col] for loc in row1])
        #
        # if row0_string == '_____6___b____5____b________9b_2_4_____e______7__e_______8_e__3______h1________h_2_4_____h' and \
        #         row1_string == '______7_9c_______8_c____5____c__34_____f1________f_2_______f___4__7_9i__34____9i_____6___i':
        #     base0 = Loc(3, 3)
        #     base1 = Loc(3, 6)
        #     single_fin = Loc(8, 3)
        #     two_fin = [Loc(6, 6), Loc(7, 6)]
        #     remove = [Loc(8, 7), Loc(8, 8)]
        #     puzzle.override_loc_color(row0 + row1, Fore.GREEN)
        #     puzzle.override_loc_color(two_fin, Fore.LIGHTBLUE_EX)
        #     puzzle.override_loc_color(remove, Fore.LIGHTRED_EX)
        #     puzzle.override_loc_color([base0, base1, single_fin], Fore.YELLOW)
        #     edits += puzzle.rem(remove, [4])
        #
        # row0 = puzzle.house_col(0)
        # row1 = puzzle.house_col(4)
        #
        # row0_string = "".join([puzzle.grid[loc.row][loc.col] for loc in row0])
        # row1_string = "".join([puzzle.grid[loc.row][loc.col] for loc in row1])
        #
        # # print(row0_string)
        # # print(row1_string)
        #
        # if row0_string == '____5____a__3______a_____678_a1________d______78_d___4_____d_____6_8_g_2_______g________9g' and \
        #         row1_string == '_____6___b____5____b______78_b___4__78_e________9e__3______e___4___8_h1________h_2_______h':
        #     base0 = Loc(2, 0)
        #     base1 = Loc(2, 4)
        #     two_fin = [Loc(4, 0), Loc(3, 4)]
        #     remove = [Loc(3, 1), Loc(3, 2), Loc(4, 3), Loc(4, 5)]
        #     puzzle.override_loc_color(row0 + row1, Fore.GREEN)
        #     puzzle.override_loc_color(two_fin, Fore.LIGHTBLUE_EX)
        #     puzzle.override_loc_color(remove, Fore.LIGHTRED_EX)
        #     puzzle.override_loc_color([base0, base1] + two_fin, Fore.YELLOW)
        #     edits += puzzle.rem(remove, [7])
        #
        # if puzzle.id() == "annoying_26.sudoku":
        #     print('here')

        return edits

    def solve_length_4(self, puzzle):
        pass
