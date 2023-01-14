from Loc import Loc
from puzzles import Sudoku
from techniques0.Technique import Technique
from colorama import Fore


class FinnedXWing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
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

        for candidate in puzzle.expected_candidates():
            for i in range(puzzle.__length - 1):
                house0 = puzzle.house_row(i, candidate)
                if 1 < len(house0) > 4:
                    continue
                for ii in range(i + 1, puzzle.__length):
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

                    if len(rows) == 2 and len(fences) == 4 and len(row_chute) == 2 and len(col_chute) == 2 and 1 < len(
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
                            puzzle.override_loc_color(puzzle.house_row(row0), Fore.RED)
                            puzzle.override_loc_color(puzzle.house_row(row1), Fore.RED)

                            # # print("rows")
                            # print("before")
                            # print(puzzle)
                            edits += puzzle.rem(list(set(fence_locs).intersection(col_locs).difference(all_locs)),
                                                [candidate])
                            # print("after")
                            # print(puzzle)
                            # # print(f'{edits} {candidate}')
                            # print("////")



                    if len(cols) == 2 and len(fences) == 4 and len(row_chute) == 2 and len(col_chute) == 2 and 1 < len(
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
