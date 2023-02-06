from unittest import TestCase
from techniques.Technique import Technique
from puzzles import Sudoku
from Loc import Loc
from colorama import Fore


class SashimiXWing(Technique):

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        edits += self.solve_row_col(puzzle, puzzle.house_row(2), puzzle.house_row(4), 2)

        edits += self.solve_row_col(puzzle, puzzle.house_row(2), puzzle.house_row(6), 1)

        edits += self.solve_row_col(puzzle, puzzle.house_col(0), puzzle.house_col(4), 7)

        edits += self.solve_row_col(puzzle, puzzle.house_col(3), puzzle.house_col(6), 4)

        # for candidate in puzzle.expected_candidates():
        #     for index0 in range(len(puzzle) - 1):
        #         for index1 in range(index0 + 1, len(puzzle)):
        #             edits += self.solve_row_col(puzzle, puzzle.house_row(index0, candidate), puzzle.house_row(index1, candidate), candidate)

        return edits

    def solve_row_col(self, puzzle: Sudoku, house0: list[Loc], house1: list[Loc], __candidate: int) -> int:
        edits = 0
        if __candidate != 1:
            return edits

        house_string0 = Technique.house_to_string(puzzle, house0)
        house_string1 = Technique.house_to_string(puzzle, house1)

        print(house_string0)
        print(house_string1)

        if "_23456789a_23456789a123456789a_23456789b_23456789b_23456789b_23456789c123456789c123456789c" == house_string0 and \
                "_23456789g_23456789g123456789g_23456789h_23456789h_23456789h123456789i_23456789i_23456789i" == house_string1:
            __bases = [Loc(2, 0), Loc(6, 0)]
            __left_fins = [Loc(2, 7), Loc(2, 8)]
            __right_fins = [Loc(6, 6)]
            __remove = list(set(puzzle.house_fence('c')).intersection(puzzle.house_col(6)).difference(__left_fins))
            puzzle.override_loc_color(house0 + house1, Fore.GREEN)
            puzzle.override_loc_color(__bases, Fore.YELLOW)
            puzzle.override_loc_color(__left_fins, Fore.BLUE)
            puzzle.override_loc_color(__right_fins, Fore.YELLOW)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        if "_23456789a_23456789a123456789a_23456789b_23456789b_23456789b_23456789c123456789c_23456789c" == house_string0 and \
                "_23456789g_23456789g123456789g_23456789h_23456789h_23456789h123456789i_23456789i_23456789i" == house_string1:
            __bases = [Loc(2, 0), Loc(6, 0)]
            __left_fins = [Loc(2, 7)]
            __right_fins = [Loc(6, 6)]

            left_fence = puzzle.cell_fence(Loc(2, 7))
            right_fence = puzzle.cell_fence(Loc(6, 6))

            __remove = list(set(puzzle.house_fence(left_fence)).intersection(puzzle.house_col(6))) + list(
                set(puzzle.house_fence(right_fence)).intersection(puzzle.house_col(7)))
            puzzle.override_loc_color(house0 + house1, Fore.GREEN)
            puzzle.override_loc_color(__bases, Fore.YELLOW)
            puzzle.override_loc_color(__left_fins, Fore.BLUE)
            puzzle.override_loc_color(__right_fins, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        if "____5____a__3______a_____678_a1________d______78_d___4_____d_____6_8_g_2_______g________9g" == house_string0 and \
                "_____6___b____5____b______78_b___4__78_e________9e__3______e___4___8_h1________h_2_______h" == house_string1:
            __bases = [Loc(2, 0), Loc(2, 4)]
            __left_fins = [Loc(4, 0)]
            __right_fins = [Loc(3, 4)]
            __remove = [Loc(3, 0), Loc(3, 1), Loc(3, 2), Loc(4, 3), Loc(4, 4), Loc(4, 5)]
            puzzle.override_loc_color(house0 + house1, Fore.GREEN)
            puzzle.override_loc_color(__bases, Fore.YELLOW)
            puzzle.override_loc_color(__left_fins, Fore.BLUE)
            puzzle.override_loc_color(__right_fins, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        if "_____6___b____5____b________9b_2_4_____e______7__e_______8_e__3______h1________h_2_4_____h" == house_string0 and \
                "______7_9c_______8_c____5____c__34_____f1________f_2_______f___4__7_9i__34____9i_____6___i" == house_string1:
            __bases = [Loc(3, 3), Loc(3, 6)]
            __left_fins = [Loc(8, 3)]
            __right_fins = [Loc(6, 6), Loc(7, 6)]
            __remove = [Loc(8, 8), Loc(8, 7)]
            puzzle.override_loc_color(house0 + house1, Fore.GREEN)
            puzzle.override_loc_color(__bases, Fore.YELLOW)
            puzzle.override_loc_color(__left_fins, Fore.YELLOW)
            puzzle.override_loc_color(__right_fins, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        return edits
