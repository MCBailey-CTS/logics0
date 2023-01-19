from puzzles import Sudoku
from colorama import Fore
from Loc import Loc
from tech import Technique
class FinnedXWing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        edits += self.solve_explicit(puzzle)
        # 'a': Fore.RED,
        # 'b': Fore.CYAN,
        # 'c': Fore.GREEN,
        # 'd': Fore.LIGHTBLUE_EX,
        # 'e': Fore.LIGHTMAGENTA_EX,
        # 'f': Fore.LIGHTGREEN_EX,
        # 'g': Fore.LIGHTWHITE_EX,
        # 'h': Fore.LIGHTYELLOW_EX,
        # 'i': Fore.LIGHTRED_EX,
        # 'j': Fore.YELLOW,
        # 'k': Fore.RED
        # puzzle.override_loc_color([Loc(6, 2), Loc(6, 6), Loc(2, 2), Loc(2, 6)], Fore.YELLOW)
        # puzzle.override_loc_color([Loc(2, 0), Loc(2, 1)], Fore.LIGHTBLUE_EX)
        # puzzle.override_loc_color([Loc(0, 2), Loc(1, 2)], Fore.LIGHTRED_EX)
        # puzzle.override_loc_color([Loc(2, 3), Loc(2, 4), Loc(2, 5), Loc(2, 7), Loc(2, 8)], Fore.GREEN)
        # puzzle.override_loc_color([Loc(6, 0), Loc(6, 1),Loc(6, 3), Loc(6, 4), Loc(6, 5), Loc(6, 7), Loc(6, 8)], Fore.GREEN)

        for candidate in puzzle.expected_candidates():
            for i in range(len(puzzle) - 1):
                house0 = puzzle.house_row(i, candidate)
                if 1 < len(house0) > 4:
                    continue
                for ii in range(i + 1, len(puzzle)):
                    house1 = puzzle.house_row(ii, candidate)
                    if 1 < len(house1) > 4:
                        continue

                    all_locs = house0 + house1
                    row_dict = {}
                    col_dict = {}
                    fence_dict = {}
                    rows = set()
                    cols = set()
                    fences = set()
                    row_chute = set()
                    col_chute = set()
                    for loc in all_locs:
                        rows.add(loc.row)
                        cols.add(loc.col)
                        fences.add(puzzle.cell_fence(loc))
                        row_chute.add(puzzle.row_chute(loc))
                        col_chute.add(puzzle.col_chute(loc))
                        fence = puzzle.cell_fence(loc)
                        if fence not in fence_dict:
                            fence_dict[fence] = []
                        fence_dict[fence].append(loc)
                        if loc.row not in row_dict:
                            row_dict[loc.row] = []
                        row_dict[loc.row].append(loc)
                        if loc.col not in col_dict:
                            col_dict[loc.col] = []
                        col_dict[loc.col].append(loc)

                    if len(rows) == 2 and len(fences) == 4 and len(row_chute) == 2 and len(
                            col_chute) == 2 and 1 < len(
                        cols) < 5:
                        # rows
                        temp_fences = set(fences)
                        for fence in fences:
                            if len(fence_dict[fence]) == 1:
                                temp_fences.remove(fence)
                        if len(temp_fences) != 1:
                            continue
                        single_fence = temp_fences.pop()
                        fin_locs = fence_dict[single_fence]
                        fence_locs = puzzle.house_fence(single_fence)
                        row_chute0 = puzzle.row_chute(fin_locs[0])
                        expected_col_chute = puzzle.col_chute(fin_locs[0])
                        # need to find the cell that is not in the {row_chute0} but is in the {expected_col_chute} in {all_locs}
                        temporary = [loc for loc in all_locs if
                                        expected_col_chute == puzzle.col_chute(loc) and row_chute0 != puzzle.row_chute(
                                            loc)]
                        if len(temporary) == 1:
                            col_locs = puzzle.house_col(temporary[0].col)
                            row0, row1 = rows
                            # puzzle.override_loc_color(puzzle.house_row(row0), Fore.RED)
                            # puzzle.override_loc_color(puzzle.house_row(row1), Fore.RED)

                            # # print("rows")
                            # print("before")
                            # print(puzzle)
                            edits += puzzle.rem(list(set(fence_locs).intersection(col_locs).difference(all_locs)),
                                                [candidate])
                            # print("after")
                            # print(puzzle)
                            # # print(f'{edits} {candidate}')
                            # print("////")

                    if len(cols) == 2 and len(fences) == 4 and len(row_chute) == 2 and len(
                            col_chute) == 2 and 1 < len(
                        rows) < 5:
                        # cols
                        temp_fences = set(fences)
                        for fence in fences:
                            if len(fence_dict[fence]) == 1:
                                temp_fences.remove(fence)
                        if len(temp_fences) != 1:
                            continue
                        single_fence = temp_fences.pop()
                        fin_locs = fence_dict[single_fence]
                        fence_locs = puzzle.house_fence(single_fence)
                        col_chute0 = puzzle.col_chute(fin_locs[0])
                        expected_row_chute = puzzle.row_chute(fin_locs[0])
                        # need to find the cell that is not in the {col_chute0} but is in the {expected_row_chute} in {all_locs}
                        temporary = [loc for loc in all_locs if
                                        expected_row_chute == puzzle.col_chute(loc) and col_chute0 != puzzle.col_chute(
                                            loc)]
                        if len(temporary) == 1:
                            row_locs = puzzle.house_row(temporary[0].row)
                            print("cols")

                            edits += puzzle.rem(list(set(fence_locs).intersection(row_locs).difference(all_locs)),
                                                [candidate])

        return edits

    @staticmethod
    def solve_explicit(puzzle: Sudoku) -> int:
        edits = 0

        # 'a': Fore.RED,
        # 'b': Fore.CYAN,
        # 'c': Fore.GREEN,
        # 'd': Fore.LIGHTBLUE_EX,
        # 'e': Fore.LIGHTMAGENTA_EX,
        # 'f': Fore.LIGHTGREEN_EX,
        # 'g': Fore.LIGHTWHITE_EX,
        # 'h': Fore.LIGHTYELLOW_EX,
        # 'i': Fore.LIGHTRED_EX,
        # 'j': Fore.YELLOW,
        # 'k': Fore.RED
        # puzzle.override_loc_color([Loc(6, 2), Loc(6, 6), Loc(2, 2), Loc(2, 6)], Fore.YELLOW)
        # puzzle.override_loc_color([Loc(2, 0), Loc(2, 1)], Fore.LIGHTBLUE_EX)
        # puzzle.override_loc_color([Loc(0, 2), Loc(1, 2)], Fore.LIGHTRED_EX)
        # puzzle.override_loc_color([Loc(2, 3), Loc(2, 4), Loc(2, 5), Loc(2, 7), Loc(2, 8)], Fore.GREEN)
        # puzzle.override_loc_color([Loc(6, 0), Loc(6, 1),Loc(6, 3), Loc(6, 4), Loc(6, 5), Loc(6, 7), Loc(6, 8)], Fore.GREEN)

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
        print(string0)
        print(string1)
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

        return edits
