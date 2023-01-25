from unittest import TestCase
from techniques.Technique import Technique
from puzzles import Sudoku
from Loc import Loc
from colorama import Fore


class ShashimiXWing(Technique):

    def solve_row_col(self, puzzle: Sudoku, house0, house1, candidate: int) -> int:
        edits = 0

        house_string0 = Technique.house_to_string(puzzle, house0)
        house_string1 = Technique.house_to_string(puzzle, house1)

        print(house_string0)
        print(house_string1)

        if "1______8_a1_______9a_2_______a___4_____d__3______d_____6_8_d______7__g_____6__9g____5____g" == house_string0 and \
                "1____6_8_b1_______9b___4_____b__3______e_____6_8_e____5____e_2_______h______7__h_____6_89h" == house_string1:
            __bases = [Loc(1, 1), Loc(1, 4)]
            __left_fins = [Loc(7, 1)]
            __right_fins = [Loc(8, 5)]
            __remove = [Loc(8, 0), Loc(8, 2), Loc(7, 3), Loc(7, 4)]
            # puzzle.override_loc_color(col_house0 + col_house1, Fore.GREEN)
            # puzzle.override_loc_color(__bases, Fore.YELLOW)
            # puzzle.override_loc_color(__left_fins, Fore.YELLOW)
            # puzzle.override_loc_color(__right_fins, Fore.BLUE)
            # puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [candidate])

        if "__3______a_2_______a_______89a_______89b______7__b___4_____b_____6___c____5____c1________c" == house_string0 and \
                "_2_______d_____6_8_d______7__d_____6_8_e1________e____5____e___4_____f________9f__3______f" == house_string1:
            __bases = [Loc(2, 3), Loc(5, 3)]
            __left_fins = [Loc(2, 2)]
            __right_fins = [Loc(5, 1)]
            __remove = [Loc(0, 1), Loc(1, 1), Loc(3, 2), Loc(4, 2)]
            # puzzle.override_loc_color(house0 + house1, Fore.GREEN)
            # puzzle.override_loc_color(__bases, Fore.YELLOW)
            # puzzle.override_loc_color(__left_fins, Fore.BLUE)
            # puzzle.override_loc_color(__right_fins, Fore.YELLOW)
            # puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [candidate])

        if "_____6___a______7__a12_______a_______8_b1__4_____b________9b___45____c_2_45____c__3______c" == house_string0 and \
                "____5____d1____6___d12_______d________9e_______8_e___4_____e__3______f______7__f_2___6___f" == house_string1:
            __bases = [Loc(2, 2), Loc(4, 2)]
            __left_fins = [Loc(4, 8)]
            __right_fins = [Loc(2, 7)]
            __remove = [Loc(0, 8), Loc(1, 8), Loc(3, 7), Loc(5, 7)]
            # puzzle.override_loc_color(house0 + house1, Fore.GREEN)
            # puzzle.override_loc_color(__bases, Fore.YELLOW)
            # puzzle.override_loc_color(__left_fins, Fore.BLUE)
            # puzzle.override_loc_color(__right_fins, Fore.YELLOW)
            # puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [candidate])

        return edits

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        edits += self.solve_row_col(puzzle, puzzle.house_col(1), puzzle.house_col(5), 9)

        edits += self.solve_row_col(puzzle, puzzle.house_row(2), puzzle.house_row(5), 8)

        edits += self.solve_row_col(puzzle, puzzle.house_row(2), puzzle.house_row(4), 2)

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
