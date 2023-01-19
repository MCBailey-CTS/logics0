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
            __fin = [Loc(4, 5)]
            __corners = [Loc(4, 6), Loc(6, 6), Loc(4, 3), Loc(6, 3)]
            __remove = [Loc(3, 3), Loc(5, 3)]

            puzzle.override_loc_color(__col0 + __col1, Fore.GREEN)
            puzzle.override_loc_color(__corners, Fore.YELLOW)
            puzzle.override_loc_color(__fin, Fore.BLUE)
            puzzle.override_loc_color(__remove, Fore.RED)
            edits += puzzle.rem(__remove, [__candidate])

        return edits


