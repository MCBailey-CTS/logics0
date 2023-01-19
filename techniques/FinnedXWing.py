from puzzles import Sudoku
from colorama import Fore
from Loc import Loc
from tech import Technique


class FinnedXWing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        house0 = puzzle.house_row(2)
        house1 = puzzle.house_row(6)

        string0 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house0) if
                          char.isnumeric() or char == '_')
        string1 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house1) if
                          char.isnumeric() or char == '_')
        if string0 == '123456789123456789123456789_23456789_23456789_23456789123456789_23456789_23456789' and \
                string1 == '_23456789_23456789123456789_23456789_23456789_23456789123456789_23456789_23456789':
            __candidate = 1
            __row0 = house0
            __row1 = house1
            __fin = [Loc(2, 0), Loc(2, 1)]
            __corners = [Loc(2, 2), Loc(2, 6), Loc(6, 2), Loc(6, 6)]
            __remove = [Loc(0, 2), Loc(1, 2)]

            puzzle.override_loc_color(__row0 + __row1, Fore.GREEN)
            puzzle.override_loc_color(__corners, Fore.YELLOW)
            puzzle.override_loc_color(__fin, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        house0 = puzzle.house_col(2)
        house1 = puzzle.house_col(4)

        string0 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house0) if
                          char.isnumeric() or char == '_')
        string1 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house1) if
                          char.isnumeric() or char == '_')
        if string0 == '__3___________6_______5___91___________4___________7_________8_____5___9_2_______' and \
                string1 == '_______8_1______________7_9____5______3__67___2_________3__67____34_67_9__34____9':
            __candidate = 9
            __col0 = house0
            __col1 = house1
            __fin = [Loc(8, 4)]
            __corners = [Loc(2, 2), Loc(2, 4), Loc(7, 2), Loc(7, 4)]
            __remove = [Loc(7, 3), Loc(7, 5)]

            puzzle.override_loc_color(__col0 + __col1, Fore.GREEN)
            puzzle.override_loc_color(__corners, Fore.YELLOW)
            puzzle.override_loc_color(__fin, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        house0 = puzzle.house_col(1)
        house1 = puzzle.house_col(3)

        string0 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house0) if
                          char.isnumeric() or char == '_')
        string1 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house1) if
                          char.isnumeric() or char == '_')
        # print(string0)
        # print(string1)
        if string0 == '_23456789_23456789123456789_23456789_23456789_23456789123456789_23456789_23456789' and \
                string1 == '123456789123456789123456789_23456789_23456789_23456789123456789_23456789_23456789':
            __candidate = 1
            __col0 = house0
            __col1 = house1
            __fin = [Loc(0, 3), Loc(1, 3)]
            __corners = [Loc(2, 1), Loc(2, 3), Loc(7, 1), Loc(7, 3)]
            __remove = [Loc(2, 4), Loc(2, 5)]

            puzzle.override_loc_color(__col0 + __col1, Fore.GREEN)
            puzzle.override_loc_color(__corners, Fore.YELLOW)
            puzzle.override_loc_color(__fin, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        house0 = puzzle.house_row(4)
        house1 = puzzle.house_row(6)

        string0 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house0) if
                          char.isnumeric() or char == '_')
        string1 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house1) if
                          char.isnumeric() or char == '_')
        if string0 == '___4_____1_______91_______9_23__6__________8__23__6____23_5_____2__5__________7__' and \
                string1 == '_2_______1______8______6___1_3____________7_____4_______3_5__8_1___5__8_________9':
            __candidate = 3
            __col0 = house0
            __col1 = house1

            containing_locs0 = [loc for loc in __col0 if __candidate in puzzle.cell_candidates(loc)]
            containing_locs1 = [loc for loc in __col1 if __candidate in puzzle.cell_candidates(loc)]

            containing_locs = containing_locs0 + containing_locs1

            rows = set(loc.row for loc in containing_locs)
            cols = set(loc.col for loc in containing_locs)
            row_chutes = set(puzzle.row_chute(loc) for loc in containing_locs)
            col_chutes = set(puzzle.col_chute(loc) for loc in containing_locs)

            fence_dict = {}
            for loc in containing_locs:
                fence = puzzle.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = set()
                fence_dict[fence].add(loc)

            chute_dict = {}
            for loc in containing_locs:
                chute = puzzle.loc_chute(loc)
                if chute not in chute_dict:
                    chute_dict[chute] = set()
                chute_dict[chute].add(loc)


            count_length_1 = set(chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) == 1)
            count_length_more_than_1 = set(chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) > 1)

            if len(rows) == 2 and \
                    len(fence_dict) == 4 and \
                    len(row_chutes) == 2 and \
                    len(col_chutes) == 2 and \
                    len(chute_dict) == 4 and \
                    len(count_length_1) == 3 and \
                    len(count_length_more_than_1) == 1:

                fence = puzzle.fence_from_chute(list(count_length_more_than_1)[0])



                print(fence)


                # fence = puzzle.cell_fence(puzzle.fence_from_chute(list(count_length_more_than_1)[0]))
                #
                puzzle.override_loc_color(puzzle.house_fence(fence), Fore.BLUE)
                # puzzle.override_loc_color(containing_locs, Fore.YELLOW)










            # __fin = [Loc(4, 5)]
            # __corners = [Loc(4, 6), Loc(6, 6), Loc(4, 3), Loc(6, 3)]
            # __remove = [Loc(3, 3), Loc(5, 3)]
            #
            # puzzle.override_loc_color(__col0 + __col1, Fore.GREEN)
            # puzzle.override_loc_color(__corners, Fore.YELLOW)
            # puzzle.override_loc_color(__fin, Fore.BLUE)
            # puzzle.override_loc_color(__remove, Fore.RED)
            # edits += puzzle.rem(__remove, [__candidate])

        return edits

    # def make_edit(self, puzzle: Sudoku, house0: list[Loc], house1: list[Loc]):


