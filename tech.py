from abc import abstractmethod
from typing import Optional

from colorama import Fore

from Loc import Loc
from puzzles import *


class Technique:

    @abstractmethod
    def solve0(self, puzzle) -> int:
        raise NotImplementedError()

    def __repr__(self):
        return f'{self.__class__.__name__}()'


class tech:
    class AbstractPaintingScraperAndHouse:
        @abstractmethod
        def solve1(self, puzzle: AbstractPainting, scraper: Optional[int], house: list[Loc]) -> int:
            raise NotImplementedError()

        def solve0(self, puzzle: AbstractPainting) -> int:
            edits = 0
            for index in range(len(puzzle)):
                row_house = puzzle.house_row(index)
                row_scraper = puzzle.east_scraper(index)
                edits += self.solve1(puzzle, row_scraper, row_house)
                col_house = puzzle.house_col(index)
                col_scraper = puzzle.south_scraper(index)
                edits += self.solve1(puzzle, col_scraper, col_house)
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    candidates = puzzle.cell_candidates(loc)
                    if len(candidates) != 1:
                        continue
                    fence = puzzle.cell_fence(loc)
                    if 1 in candidates:
                        edits += puzzle.rem(puzzle.house_fence(fence), [0])
                    if 0 in candidates:
                        edits += puzzle.rem(puzzle.house_fence(fence), [1])
            return edits

    class AbstractPaintingTech(AbstractPaintingScraperAndHouse):
        def solve1(self, puzzle: AbstractPainting, scraper: Optional[int], house: list[Loc]) -> int:
            edits = 0
            solved_abstract = []
            solved_empty = []
            unsolved = []
            for index in range(len(house)):
                candidates = puzzle.cell_candidates(house[index])
                if len(candidates) > 1:
                    unsolved.append(house[index])
                    continue
                if 1 in candidates:
                    solved_abstract.append(house[index])
                if 0 in candidates:
                    solved_empty.append(house[index])
            # full house
            if scraper == len(house):
                edits += puzzle.rem(house, [0])
            if scraper == len(solved_abstract):
                edits += puzzle.rem(unsolved, [1])
            # hidden paint
            if len(unsolved) == scraper and len(solved_abstract) == 0:
                edits += puzzle.rem(unsolved, [0])
            # check fence length
            fence_dict = {}
            for loc in house:
                fence = puzzle.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = []
                fence_dict[fence].append(loc)
            for fence in fence_dict:
                if scraper is not None and len(fence_dict[fence]) > scraper:
                    edits += puzzle.rem(puzzle.house_fence(fence), [1])
            return edits

    class BaseSudokuHouseTechnique(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits

            for house in puzzle.houses_rows_cols_fences():
                edits += self.solve_house(puzzle, house)

            return edits

        @abstractmethod
        def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
            raise NotImplementedError()

    class AlmostLockedCandidatesClaiming:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class AlmostLockedCandidatesPointing:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class AvoidableRectangleType1:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            solved_cells = []
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    if len(puzzle.cell_candidates(loc)) == 1:
                        solved_cells.append(loc)

            for upper_corner in solved_cells:
                for lower_corner in solved_cells:
                    other_upper = Loc(upper_corner.row, lower_corner.col)
                    other_lower = Loc(lower_corner.row, upper_corner.col)
                    corner_set = {upper_corner, lower_corner, other_upper, other_lower}

                    if len(corner_set) != 4:
                        continue

                    # if not corner_set.issuperset([Loc(0, 0), Loc(0, 1), Loc(8, 0), Loc(8, 1)]):
                    #     continue

                    row_set = set([loc.row for loc in corner_set])
                    col_set = set([loc.col for loc in corner_set])
                    fence_set = set([puzzle.cell_fence(loc) for loc in corner_set])

                    if len(row_set) != 2 or len(col_set) != 2 or len(fence_set) != 2:
                        continue

                    solved_cells = set([loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 1])

                    if len(solved_cells) != 3:
                        continue

                    unsolved_cells = set([loc for loc in corner_set if len(puzzle.cell_candidates(loc)) > 1])

                    if len(unsolved_cells) != 1:
                        continue

                    opposite_corners = set(corner_set)

                    opposite_corners.remove(other_upper)
                    opposite_corners.remove(other_lower)

                    temp_opposite = list(opposite_corners)

                    opposite_candidates0 = set(puzzle.cell_candidates(temp_opposite[0]))
                    opposite_candidates1 = puzzle.cell_candidates(temp_opposite[1])

                    if len(opposite_candidates0) != 1 or len(opposite_candidates1) != 1:
                        continue

                    if not opposite_candidates0.issubset(opposite_candidates1):
                        continue

                    # opposite_candidate = opposite_candidates0.pop()

                    other_solved_cell = list(solved_cells.difference(opposite_corners))[0]

                    solved_candidate = list(puzzle.cell_candidates(other_solved_cell))[0]

                    edits += puzzle.rem(unsolved_cells.pop(), [solved_candidate])

                    # print(solved_candidate)
                    # print(f'{other_upper} {other_lower} {puzzle.cell_candidates(other_upper)} {puzzle.cell_candidates(other_lower)}')

                    # unsolved_cell = unsolved_cells.pop()

                    # solved_candidates = set([puzzle.solved_candidate(loc) for loc in solved_cells])

                    # if len(solved_candidates) != 2:
                    #     continue

                    # solved_candidate_dict = {}

                    # for loc in corner_set:
                    #     candidates0 = puzzle.cell_candidates(loc)

                    #     if len(candidates0) > 1:
                    #         continue

                    #     candidate = list(candidates0)[0]

                    #     if candidate not in solved_candidate_dict:
                    #         solved_candidate_dict[candidate] = 0

                    #     solved_candidate_dict[candidate] += 1

                    # if len(solved_candidate_dict) != 2:
                    #     continue

                    # corner_candidate = None

                    # keys = list(solved_candidate_dict.keys())

                    # if solved_candidate_dict[keys[0]] == 2:
                    #     corner_candidate = keys[1]
                    # elif solved_candidate_dict[keys[1]] == 2:
                    #     corner_candidate = keys[0]

                    # unsolved_cell_candidates = puzzle.cell_candidates(unsolved_cell)

                    # if corner_candidate in unsolved_cell_candidates and len(unsolved_cell_candidates) == 1:
                    #     continue

                    # print(corner_set)

                    # edits += puzzle.rem(unsolved_cell, [corner_candidate])

            return edits

    class AvoidableRectangleType2:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            edits += self.explicit(puzzle)
            return edits

        @staticmethod
        def explicit(puzzle: Sudoku) -> int:
            edits = 0

            base0 = Loc(3, 5)
            base1 = Loc(5, 5)
            opp_base0 = Loc(5, 6)
            opp_base1 = Loc(3, 6)

            if \
            set(puzzle.cell_candidates(base0)) == {1}\
            and\
            set(puzzle.cell_candidates(base1)) == {2} \
            and \
            set(puzzle.cell_candidates(opp_base0)) == {2, 3} \
            and \
            set(puzzle.cell_candidates(opp_base1)) == {1, 3}\
            :
                __fence = 'f'
                __col = 6
                __candidates = [3]
                __base = [base0, base1]
                __opp_base = [opp_base0, opp_base1]
                __intersection = puzzle.house_fence(__fence) + puzzle.house_col(__col)
                __remove = set(__intersection).difference(__opp_base)
                puzzle.override_loc_color(__intersection, Fore.RED)
                puzzle.override_loc_color(__base, Fore.GREEN)
                puzzle.override_loc_color(__opp_base, Fore.YELLOW)
                edits += puzzle.rem(__remove, __candidates)

            base0 = Loc(6, 3)
            base1 = Loc(6, 5)
            opp_base0 = Loc(2, 3)
            opp_base1 = Loc(2, 5)

            if set(puzzle.cell_candidates(base0)) == {1} and \
                    set(puzzle.cell_candidates(base1)) == {2} and \
                    set(puzzle.cell_candidates(opp_base0)) == {2, 3} and \
                    set(puzzle.cell_candidates(opp_base1)) == {1, 3}:
                __fence = 'b'
                __row = 2
                __candidates = [3]
                __base = [base0, base1]
                __opp_base = [opp_base0, opp_base1]
                __intersection = puzzle.house_fence(__fence) + puzzle.house_row(__row)
                __remove = set(__intersection).difference(__opp_base)
                puzzle.override_loc_color(__intersection, Fore.RED)
                puzzle.override_loc_color(__base, Fore.GREEN)
                puzzle.override_loc_color(__opp_base, Fore.YELLOW)
                edits += puzzle.rem(__remove, __candidates)

            return edits

    class BaseUniqueRectangle:

        @abstractmethod
        def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]):
            raise NotImplementedError()

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits
            locs: list[Loc] = []
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    locs.append(Loc(r, c))
            length = len(locs)
            for i in range(length):
                for ii in range(length):
                    if i == ii:
                        continue
                    l0: Loc = locs[i]
                    l1: Loc = locs[ii]
                    if l0.row == l1.row:
                        continue
                    if l0.col == l1.col:
                        continue
                    fences = set([puzzle.cell_fence(l) for l in [l0, l1]])
                    if len(fences) != 2:
                        continue

                    corners = {l0, l1, Loc(l0.row, l1.col), Loc(l1.row, l0.col)}

                    if len(corners) != 4:
                        raise ValueError("number of corners didn't equal 4")

                    rows = set([loc.row for loc in corners])
                    cols = set([loc.col for loc in corners])
                    fences = set([puzzle.cell_fence(loc) for loc in corners])

                    if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                        continue

                    edits += self.solve_rectangle(puzzle, list(corners))
            return edits

    class Bug:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits

            length_1: list[Loc] = list()
            length_2: list[Loc] = list()
            length_3: list[Loc] = list()

            for loc in puzzle.list_all_cell_locs():
                _candidates = puzzle.cell_candidates(loc)

                if len(_candidates) == 1:
                    length_1.append(loc)
                    continue
                if len(_candidates) == 2:
                    length_2.append(loc)
                    continue

                if len(_candidates) == 3:
                    length_3.append(loc)
                    continue

                return edits

            total = len(puzzle) * len(puzzle)

            if len(length_3) != 1 or total != len(length_3) + len(length_2) + len(length_1):
                return edits

            row_house, col_house, fence_house = puzzle.houses_rows_cols_fences(length_3[0])

            for candidate in list(puzzle.cell_candidates(length_3[0])):
                row_count = [l for l in row_house if candidate in puzzle.cell_candidates(l)]
                col_count = [l for l in col_house if candidate in puzzle.cell_candidates(l)]
                fence_count = [l for l in fence_house if candidate in puzzle.cell_candidates(l)]

                if len(row_count) == 3 and len(col_count) == 3 and len(fence_count) == 3:
                    for c in list(puzzle.cell_candidates(length_3[0])):
                        if c == candidate:
                            continue
                        edits += puzzle.rem(length_3[0], [c])

            return edits

    class CrossHatch:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            unsolved = puzzle.unsolved_cells()

            # print(len(unsolved))

            if len(unsolved) == 0:
                return edits

            for cell in list(puzzle.unsolved_cells()):
                neighbors = set(
                    puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
                if puzzle.has_fences:
                    for loc in puzzle.house_fence(puzzle.cell_fence(cell)):
                        neighbors.add(loc)
                neighbors.remove(cell)
                for neighbor in neighbors:
                    if neighbor not in puzzle.unsolved_cells():
                        _candidates = puzzle.cell_candidates(neighbor)
                        if len(_candidates) == 1:
                            edits += puzzle.rem(cell, [list(_candidates)[0]])
            return edits

    class FishyCycle:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FinnedSwordFish:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FinnedJellyFish:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

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
        def solve_explicit(puzzle: Sudoku)->int:
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
                __remove = [Loc(0,2), Loc(1,2)]

                puzzle.override_loc_color(__row0 + __row1, Fore.GREEN)
                puzzle.override_loc_color(__corners, Fore.YELLOW)
                puzzle.override_loc_color(__fin, Fore.BLUE)
                puzzle.override_loc_color(__remove, Fore.RED)
                edits += puzzle.rem(__remove, [__candidate])

            return edits

    class LockedCandidatesPointing:

        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0
            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits
            for house in puzzle.houses_rows_cols_fences():
                for candidate in puzzle.expected_candidates():
                    locs = [loc for loc in house if candidate in puzzle.cell_candidates(loc)]
                    loc_set = set(locs)
                    if len(locs) < 2:
                        continue
                    if all([locs[0].row == loc.row for loc in locs]):
                        for loc in puzzle.house_row(locs[0].row):
                            if loc not in loc_set:
                                edits += puzzle.rem(loc, [candidate])
                    if all([locs[0].col == loc.col for loc in locs]):
                        for loc in puzzle.house_col(locs[0].col):
                            if loc not in loc_set:
                                edits += puzzle.rem(loc, [candidate])
            return edits

    class LockedCandidatesClaiming:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits
            for house in puzzle.houses_rows_cols():
                for candidate in puzzle.expected_candidates():
                    locs = [
                        loc
                        for loc in house
                        if candidate in puzzle.cell_candidates(loc)
                    ]
                    fences = set([puzzle.cell_fence(l) for l in locs])
                    if len(fences) != 1:
                        continue
                    fence = list(fences)[0]
                    loc_set = set(locs)
                    for loc in puzzle.house_fence(fence):
                        if loc not in loc_set:
                            edits += puzzle.rem(loc, [candidate])
            return edits

    class JellyFish:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for candidate in puzzle.expected_candidates():
                for i in range(0, 6):
                    for ii in range(i + 1, 7):
                        for iii in range(ii + 1, 8):
                            for iiii in range(iii + 1, 9):
                                if len({i, ii, iii, iiii}) != 4:
                                    continue

                                locs0 = [loc for loc in puzzle.house_row(i) if candidate in puzzle.cell_candidates(loc)]
                                locs1 = [loc for loc in puzzle.house_row(ii) if
                                         candidate in puzzle.cell_candidates(loc)]
                                locs2 = [loc for loc in puzzle.house_row(iii) if
                                         candidate in puzzle.cell_candidates(loc)]
                                locs3 = [loc for loc in puzzle.house_row(iiii) if
                                         candidate in puzzle.cell_candidates(loc)]

                                loc_set = set(locs0 + locs1 + locs2 + locs3)

                                cols = set([loc.col for loc in loc_set])

                                has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                                if any(has_solved_candidate):
                                    continue

                                if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                                    continue

                                if len(cols) != 4:
                                    continue

                                edits += self.new_method(puzzle, candidate, locs0, locs1, locs2, locs3, cols)

            for candidate in puzzle.expected_candidates():
                for i in range(0, 6):
                    for ii in range(i + 1, 7):
                        for iii in range(ii + 1, 8):
                            for iiii in range(iii + 1, 9):
                                if len({i, ii, iii, iiii}) != 4:
                                    continue

                                locs0 = [loc for loc in puzzle.house_col(i) if candidate in puzzle.cell_candidates(loc)]
                                locs1 = [loc for loc in puzzle.house_col(ii) if
                                         candidate in puzzle.cell_candidates(loc)]
                                locs2 = [loc for loc in puzzle.house_col(iii) if
                                         candidate in puzzle.cell_candidates(loc)]
                                locs3 = [loc for loc in puzzle.house_col(iiii) if
                                         candidate in puzzle.cell_candidates(loc)]

                                loc_set = set(locs0 + locs1 + locs2 + locs3)

                                rows = set([loc.row for loc in loc_set])

                                has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                                if any(has_solved_candidate):
                                    continue

                                if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                                    continue

                                if len(rows) != 4:
                                    continue

                                edits += self.new_method1(puzzle, candidate, locs0, locs1, locs2, locs3, rows)

            return edits

        def new_method1(self, puzzle, candidate, locs0, locs1, locs2, locs3, rows):
            edits = 0
            for row in rows:
                row_set = set(puzzle.house_row(row))
                for loc in row_set.difference(locs0 + locs1 + locs2 + locs3):
                    edits += puzzle.rem(loc, [candidate])
            return edits

        def new_method(self, puzzle, candidate, locs0, locs1, locs2, locs3, cols):
            edits = 0
            for col in cols:
                col_set = set(puzzle.house_col(col))
                for loc in col_set.difference(locs0 + locs1 + locs2 + locs3):
                    edits += puzzle.rem(loc, [candidate])
            return edits

    class SimpleColoring:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class ShashimiXWingPlus1:
        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0
            for candidate in puzzle.expected_candidates():
                for i in range(len(puzzle)):
                    for ii in range(len(puzzle)):
                        if i == ii:
                            continue

                        house0 = [loc for loc in puzzle.house_col(i) if
                                  candidate in puzzle.cell_candidates(loc) and len(puzzle.cell_candidates(loc)) != 1]
                        house1 = [loc for loc in puzzle.house_col(ii) if
                                  candidate in puzzle.cell_candidates(loc) and len(puzzle.cell_candidates(loc)) != 1]

                        if len(house0) != 2 or len(house0) != 2:
                            continue

                        loc_set = set(house0 + house1)

                        fence_dict = puzzle.fence_dict(loc_set)

                        if len(fence_dict) != 4:
                            continue

                        if not all([len(fence_dict[fence]) == 1 for fence in fence_dict]):
                            continue

                        rows = set([loc.row for loc in loc_set])
                        cols = set([loc.col for loc in loc_set])

                        if len(cols) == 2 and len(rows) == 3:
                            row_dict = {}

                            for loc in loc_set:
                                if loc.row not in row_dict:
                                    row_dict[loc.row] = []
                                row_dict[loc.row].append(loc)

                            # print(row_dict)

                            if len(row_dict) == 3:
                                shashimi_set = set(loc_set)
                                for r in row_dict:
                                    if len(row_dict[r]) == 2:
                                        for loc in row_dict[r]:
                                            shashimi_set.remove(loc)

                                pincer0, pincer1 = shashimi_set

                                fence0 = puzzle.cell_fence(pincer0)
                                fence1 = puzzle.cell_fence(pincer1)

                                fence0_locs = set(puzzle.house_fence(fence0))
                                fence1_locs = set(puzzle.house_fence(fence1))
                                row0_locs = set(puzzle.house_row(pincer0.row))
                                row1_locs = set(puzzle.house_row(pincer1.row))

                                pincer0_intersection = fence1_locs.intersection(row0_locs)
                                pincer1_intersection = fence0_locs.intersection(row1_locs)

                                for loc in list(pincer0_intersection) + list(pincer1_intersection):
                                    if loc == pincer0 or loc == pincer1:
                                        continue
                                    edits += puzzle.rem(loc, [candidate])

            return edits

    class ShashimiXWing:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            candidate = 1

            row0 = 2
            row1 = 6

            row_house0 = puzzle.house_row(row0, candidate)
            row_house1 = puzzle.house_row(row1, candidate)

            all_locs = set(row_house0 + row_house1)

            row_dict = {}
            col_dict = {}
            fence_dict = {}

            for loc in all_locs:
                if loc.row not in row_dict:
                    row_dict[loc.row] = []
                row_dict[loc.row].append(loc)

                if loc.col not in col_dict:
                    col_dict[loc.col] = []
                col_dict[loc.col].append(loc)

                fence = puzzle.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = []
                fence_dict[fence].append(loc)

            if len(fence_dict) != 4:
                return 0

            if len(row_dict) == 2 and len(col_dict) == 3:
                return self.solve_length_4(puzzle)

            if len(row_dict) == 2 and 1 < len(col_dict) < 5:
                col_chute_dict = {}

                for loc in all_locs:
                    col_chute = puzzle.col_chute(loc)
                    if col_chute not in col_chute_dict:
                        col_chute_dict[col_chute] = []
                    col_chute_dict[col_chute].append(loc)

                if len(col_chute_dict) == 2 and len(all_locs) == 4:
                    print("made it here")

                if len(col_chute_dict) == 2:
                    # need to find the col_chute that has a length more than 2
                    greater_than_2 = list(filter(lambda key: len(col_chute_dict[key]) > 2, col_chute_dict.keys()))

                    if len(greater_than_2) == 1:
                        locs_in_col_chute = col_chute_dict[greater_than_2[0]]
                        sorted_fence_dict = {}

                        for loc in locs_in_col_chute:
                            fence0 = puzzle.cell_fence(loc)
                            if fence0 not in sorted_fence_dict:
                                sorted_fence_dict[fence0] = []
                            sorted_fence_dict[fence0].append(loc)

                        if len(sorted_fence_dict) == 2:
                            fence0, fence1 = sorted_fence_dict.keys()
                            if len(sorted_fence_dict[fence0]) == 1 and len(sorted_fence_dict[fence1]) > 1:
                                fence_house = puzzle.house_fence(fence1)
                                col_house = puzzle.house_col(sorted_fence_dict[fence0][0].col)
                                locs_to_remove = set(fence_house).intersection(col_house).difference(all_locs)
                                print(locs_to_remove)
                                edits += puzzle.rem(list(locs_to_remove), [candidate])

                            if len(sorted_fence_dict[fence0]) == 1 and len(sorted_fence_dict[fence1]) == 1:
                                print("made it here")
                                # fence_house = puzzle.house_fence(fence1)
                                # col_house = puzzle.house_col(sorted_fence_dict[fence0][0].col)
                                # locs_to_remove = set(fence_house).intersection(col_house).difference(all_locs)
                                # print(locs_to_remove)
                                # edits += puzzle.rem(list(locs_to_remove), [candidate])

            return edits

        def solve_length_4(self, puzzle):
            pass

    class ShashimiSwordFish:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class ShashimiJellyFish:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class NakedTriple(BaseSudokuHouseTechnique):

        def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
            edits = 0

            naked_count = 3

            for i in range(len(puzzle)):
                for ii in range(len(puzzle)):
                    for iii in range(len(puzzle)):
                        indexes = {i, ii, iii}

                        if len(indexes) != naked_count:
                            continue

                        candidate_set = set()
                        for index in indexes:
                            for candidate in puzzle.cell_candidates(house[index]):
                                candidate_set.add(candidate)

                        _candidates0 = puzzle.cell_candidates(house[i])
                        _candidates1 = puzzle.cell_candidates(house[ii])
                        _candidates2 = puzzle.cell_candidates(house[iii])

                        if len(_candidates0) < 2 or len(_candidates0) > naked_count or \
                                len(_candidates1) < 2 or len(_candidates1) > naked_count or \
                                len(_candidates2) < 2 or len(_candidates2) > naked_count:
                            continue

                        if not candidate_set.issuperset(_candidates0) or \
                                not candidate_set.issuperset(_candidates1) or \
                                not candidate_set.issuperset(_candidates2):
                            continue

                        if len(candidate_set) != naked_count:
                            continue

                        for j in range(len(puzzle)):
                            if j not in indexes:
                                edits += puzzle.rem([house[j]], list(candidate_set))
            return edits

    class NakedQuad:
        def solve0(self, puzzle: Sudoku) -> int:
            return 0

    class NakedPair(BaseSudokuHouseTechnique):
        @staticmethod
        def static_solve_house(puzzle: Sudoku, house: list[Loc]) -> int:
            edits = 0
            for i in range(0, len(puzzle) - 1):
                for ii in range(i + 1, len(puzzle)):
                    if i == ii:
                        continue
                    index_set = {i, ii}
                    candidate_set = set()
                    candidates0 = puzzle.cell_candidates(house[i])
                    candidates1 = puzzle.cell_candidates(house[ii])
                    if len(candidates0) == 1 or len(candidates1) == 1:
                        continue
                    for c in candidates0:
                        candidate_set.add(c)
                    for c in candidates1:
                        candidate_set.add(c)
                    if len(candidate_set) != 2:
                        continue
                    for j in range(len(puzzle)):
                        if j not in index_set:
                            edits += puzzle.rem([house[j]], list(candidate_set))
            return edits

        def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
            return tech.NakedPair.static_solve_house(puzzle, house)

    class HiddenTriple:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            edits += self.explicit(puzzle)
            return edits

        @staticmethod
        def explicit(puzzle: Sudoku) -> int:
            edits = 0

            house = puzzle.house_col(0)

            string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                             char.isnumeric() or char == '_')
            if string == '____5_______4_____1_3__6_8912___6__9_____67891_3___789_2______9_2___6__912___6__9':
                edits += puzzle.rem([house[2], house[4], house[5]], [1, 6, 9])

            house = puzzle.house_row(8)

            string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                             char.isnumeric() or char == '_')
            if string == '___456789___456789123456789___456789123456789___456789123456789___456789___456789':
                edits += puzzle.rem([house[2], house[4], house[6]], [4, 5, 6, 7, 8, 9])

            house = puzzle.house_fence('c')

            string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                             char.isnumeric() or char == '_')
            if string == '_2___67___2___678__2___6___1_345_7_____4__7__1_345______3_567_______678_________9':
                edits += puzzle.rem([house[3], house[5], house[6]], [4, 6, 7])

            return edits

    class HiddenSingle:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits

            for house in puzzle.houses_rows_cols_fences():
                edits += self.solve1(puzzle, house)
            return edits

        @staticmethod
        def solve1(puzzle: Sudoku, house: list[Loc]) -> int:
            edits = 0
            for cand in puzzle.expected_candidates():
                locs_with_candidate = []
                locs_without_candidate = []
                for loc in house:
                    if cand in puzzle.cell_candidates(loc):
                        locs_with_candidate.append(loc)
                    else:
                        locs_without_candidate.append(loc)
                if len(locs_with_candidate) != 1:
                    continue
                candidates_to_remove = set(puzzle.expected_candidates())
                candidates_to_remove.remove(cand)
                edits += puzzle.rem(locs_with_candidate[0], candidates_to_remove)

            return edits

    class HiddenQuad:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            edits += self.explicit(puzzle)
            return edits

        @staticmethod
        def explicit(puzzle: Sudoku) -> int:
            edits = 0

            house = puzzle.house_row(8)

            string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                             char.isnumeric() or char == '_')
            if string == '____56789123456789____56789123456789____56789123456789____56789123456789____56789':
                __candidates = [5,6,7,8,9]
                __row = house
                __remove = [house[1] , house[3], house[5], house[7]]

                puzzle.override_loc_color(__row, Fore.GREEN)
                puzzle.override_loc_color(__remove, Fore.YELLOW)
                edits += puzzle.rem(__remove, __candidates)


            return edits

    class HiddenPair(BaseSudokuHouseTechnique):

        def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
            edits = 0
            expected = puzzle.expected_candidates()
            for i in range(len(expected) - 1):
                for ii in range(i, len(expected)):
                    if expected[i] == expected[ii]:
                        continue
                    locs0 = [loc for loc in house if expected[i] in puzzle.cell_candidates(loc)]
                    locs1 = [loc for loc in house if expected[ii] in puzzle.cell_candidates(loc)]
                    if len(locs0) != 2 or len(locs1) != 2:
                        continue
                    loc_set = set(locs0 + locs1)
                    if len(loc_set) != 2:
                        continue
                    temp_locs = list(loc_set)
                    for k in set(expected).difference([expected[i], expected[ii]]):
                        edits += puzzle.rem([temp_locs[0]], [k])
                        edits += puzzle.rem([temp_locs[1]], [k])

            return edits

    class HiddenUniqueRectangle:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            # return 0
            for corner0 in list(puzzle.unsolved_cells()):
                for corner1 in list(puzzle.unsolved_cells()):

                    other_opposite0 = Loc(corner0.row, corner1.col)
                    other_opposite1 = Loc(corner1.row, corner0.col)
                    corners = [
                        corner0,
                        corner1,
                        other_opposite0,
                        other_opposite1
                    ]

                    rows = set([loc.row for loc in corners])
                    cols = set([loc.col for loc in corners])
                    fences = set([puzzle.cell_fence(loc) for loc in corners])

                    if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                        continue

                    corner0_candidates = puzzle.cell_candidates(corner0)

                    if len(corner0_candidates) != 2:
                        continue

                    # check to see if the other corners are a super set of corner0
                    all_temp = all([set(puzzle.cell_candidates(loc)).issuperset(corner0_candidates) for loc in
                                    [corner1, other_opposite0, other_opposite1]])

                    if not all_temp:
                        continue

                    hidden_unique_cells = set(puzzle.house_row(corner1.row) + puzzle.house_col(corner1.col)).difference(
                        corners)

                    candidate0, candidate1 = corner0_candidates

                    candidate0_any = any([candidate0 in puzzle.cell_candidates(loc) for loc in hidden_unique_cells])
                    candidate1_any = any([candidate1 in puzzle.cell_candidates(loc) for loc in hidden_unique_cells])

                    if candidate0_any and candidate1_any:
                        continue

                    if candidate0_any:
                        edits += puzzle.rem(corner1, [candidate0])

                    if candidate1_any:
                        edits += puzzle.rem(corner1, [candidate1])

                    # print("mssssade aaaait here")

            return edits

    class WxyzWing:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            # row = 4

            puzzle.override_loc_color(puzzle.house_row(4), Fore.LIGHTBLUE_EX)
            puzzle.override_loc_color([Loc(4, 4)], Fore.GREEN)
            puzzle.override_loc_color([Loc(4, 3), Loc(4, 5)], Fore.RED)
            puzzle.override_loc_color([
                Loc(4, 1),
                Loc(5, 3),
                Loc(4, 7)
            ], Fore.YELLOW)

            




            # extensions = [
            #     Loc(4, 1)
            # ]




            # print("hello")

            return edits

    class WWing:
        def solve1(self, puzzle: Sudoku, left: Loc, right: Loc) -> int:
            edits = 0

            left_candidate_set = set(puzzle.cell_candidates(left))
            right_candidate_set = set(puzzle.cell_candidates(right))

            if len(left_candidate_set) != 2 or len(right_candidate_set) != 2 or not left_candidate_set.issubset(
                    right_candidate_set):
                return edits

            left_chute = puzzle.loc_chute(left)
            right_chute = puzzle.loc_chute(right)

            left_fence = puzzle.cell_fence(left)
            right_fence = puzzle.cell_fence(right)

            left_fence_house = puzzle.house_fence(left_fence)
            right_fence_house = puzzle.house_fence(right_fence)

            if right_fence == left_fence:
                return edits

            if left_chute.in_same_row(right_chute):
                cols_in_chute = {left_chute.col, right_chute.col}
                if len(cols_in_chute) == 2:
                    difference = {0, 1, 2}.difference(cols_in_chute)
                    if len(difference) == 1:
                        other_col_chute = difference.pop()
                        other_chute = Loc(left_chute.row, other_col_chute)
                        center_fence = puzzle.fence_from_chute(other_chute)
                        if center_fence != left_fence and center_fence != right_fence:
                            left_row_house = puzzle.house_row(left.row)
                            right_row_house = puzzle.house_row(right.row)
                            fence_house = puzzle.house_fence(center_fence)
                            connector_in_chute = set(fence_house).difference(left_row_house + right_row_house)
                            for candidate in left_candidate_set:
                                cells_in_connector = [loc for loc in connector_in_chute if
                                                      candidate in puzzle.cell_candidates(loc)]
                                if len(cells_in_connector) > 0:
                                    continue
                                candidate_to_remove = list(left_candidate_set.difference([candidate]))[0]
                                left_intersection = set(left_row_house).intersection(right_fence_house)
                                right_intersection = set(right_row_house).intersection(left_fence_house)
                                cells_to_remove = set(list(left_intersection) + list(right_intersection)).difference(
                                    [left, right])
                                for loc in cells_to_remove:
                                    edits += puzzle.rem(loc, [candidate_to_remove])

            if left_chute.in_same_col(right_chute):
                rows_in_chute = {left_chute.row, right_chute.row}
                if len(rows_in_chute) == 2:
                    difference = {0, 1, 2}.difference(rows_in_chute)
                    if len(difference) == 1:
                        other_row_chute = difference.pop()
                        other_chute = Loc(other_row_chute, left_chute.col)
                        center_fence = puzzle.fence_from_chute(other_chute)
                        if center_fence != left_fence and center_fence != right_fence:
                            left_col_house = puzzle.house_col(left.col)
                            right_col_house = puzzle.house_col(right.col)
                            fence_house = puzzle.house_fence(center_fence)
                            connector_in_chute = set(fence_house).difference(left_col_house + right_col_house)
                            for candidate in left_candidate_set:
                                cells_in_connector = [loc for loc in connector_in_chute if
                                                      candidate in puzzle.cell_candidates(loc)]
                                if len(cells_in_connector) > 0:
                                    continue
                                candidate_to_remove = list(left_candidate_set.difference([candidate]))[0]
                                left_intersection = set(left_col_house).intersection(right_fence_house)
                                right_intersection = set(right_col_house).intersection(left_fence_house)
                                cells_to_remove = set(list(left_intersection) + list(right_intersection)).difference(
                                    [left, right])
                                for loc in cells_to_remove:
                                    edits += puzzle.rem(loc, [candidate_to_remove])

            return edits

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for r0 in range(len(puzzle)):
                for c0 in range(len(puzzle)):
                    loc0 = Loc(r0, c0)
                    candidates0 = set(puzzle.cell_candidates(loc0))
                    if len(candidates0) != 2:
                        continue
                    for r1 in range(len(puzzle)):
                        for c1 in range(len(puzzle)):
                            loc1 = Loc(r1, c1)
                            if loc0 == loc1:
                                continue
                            candidates1 = puzzle.cell_candidates(loc1)
                            if len(candidates1) != 2:
                                continue
                            if not candidates0.issubset(candidates1):
                                continue

                            # print(loc0)
                            # print(loc1)

                            # left_loc = Loc(3, 2)
                            # right_loc = Loc(4, 6)
                            #
                            edits += self.solve1(puzzle, loc0, loc1)

            return edits

    class UniqueRectangleType4:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits

            for r in range(len(puzzle)):

                house = puzzle.house_row(r)

                for i in range(len(house)):
                    for ii in range(len(house)):
                        if i == ii:
                            continue

                        l0 = house[i]
                        l1 = house[ii]

                        candidates0 = set(puzzle.cell_candidates(l0))
                        candidates1 = puzzle.cell_candidates(l1)

                        if len(candidates0) != 2 or len(candidates1) != 2:
                            continue

                        if not candidates0.issubset(candidates1):
                            continue

                        col0 = puzzle.house_col(l0.col)
                        col1 = puzzle.house_col(l1.col)

                        for j in range(len(puzzle)):
                            corner0 = col0[j]
                            corner1 = col1[j]

                            loc_set = {l0, l1, corner0, corner1}

                            if len(loc_set) != 4:
                                continue

                            corner0_candidates = set(puzzle.cell_candidates(corner0))
                            corner1_candidates = set(puzzle.cell_candidates(corner1))

                            if not corner0_candidates.issuperset(candidates0) or not corner1_candidates.issuperset(
                                    candidates1):
                                continue

                            row_indexes = set([l.row for l in loc_set])
                            col_indexes = set([l.col for l in loc_set])
                            fence_indexes = set([puzzle.cell_fence(l) for l in loc_set])

                            if len(row_indexes) != 2 or len(col_indexes) != 2 or len(fence_indexes) != 2:
                                continue

                            opposite_row = puzzle.house_row(corner0.row)

                            for _candidate in candidates0:
                                locs_with_candidate = [l for l in opposite_row if
                                                       _candidate in puzzle.cell_candidates(l)]

                                if len(locs_with_candidate) != 2:
                                    continue

                                if not {corner0, corner1}.issuperset(locs_with_candidate):
                                    continue

                                temp_candidates = set(candidates0)

                                temp_candidates.remove(_candidate)

                                other = list(temp_candidates)[0]

                                for loc in [corner0, corner1]:
                                    edits += puzzle.rem(loc, [other])

            for c in range(len(puzzle)):

                house = puzzle.house_col(c)

                for i in range(len(house)):
                    for ii in range(len(house)):
                        if i == ii:
                            continue

                        l0 = house[i]
                        l1 = house[ii]

                        candidates0 = puzzle.cell_candidates(l0)
                        candidates1 = puzzle.cell_candidates(l1)

                        if len(candidates0) != 2 or len(candidates1) != 2:
                            continue

                        if not set(candidates0).issubset(candidates1):
                            continue

                        row0 = puzzle.house_row(l0.row)
                        row1 = puzzle.house_row(l1.row)

                        for j in range(len(puzzle)):
                            corner0 = row0[j]
                            corner1 = row1[j]

                            loc_set = {l0, l1, corner0, corner1}

                            if len(loc_set) != 4:
                                continue

                            corner0_candidates = set(puzzle.cell_candidates(corner0))
                            corner1_candidates = set(puzzle.cell_candidates(corner1))

                            if not corner0_candidates.issuperset(candidates0) or not corner1_candidates.issuperset(
                                    candidates1):
                                continue

                            row_indexes = set([loc.row for loc in loc_set])
                            col_indexes = set([loc.col for loc in loc_set])
                            fence_indexes = set([puzzle.cell_fence(l) for l in loc_set])

                            if len(row_indexes) != 2 or len(col_indexes) != 2 or len(fence_indexes) != 2:
                                continue

                            opposite_col = puzzle.house_col(corner0.col)

                            for _candidate in candidates0:
                                locs_with_candidate = [loc for loc in opposite_col if
                                                       _candidate in puzzle.cell_candidates(loc)]

                                if len(locs_with_candidate) != 2:
                                    continue

                                if not {corner0, corner1}.issuperset(locs_with_candidate):
                                    continue

                                temp_candidates = set(candidates0)

                                temp_candidates.remove(_candidate)

                                other = list(temp_candidates)[0]

                                for loc in [corner0, corner1]:
                                    edits += puzzle.rem(loc, [other])

            return edits

    class UniqueRectangleType3:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class SueDeCoq:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class SwordFish:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for candidate in puzzle.expected_candidates():
                for i in range(len(puzzle)):
                    for ii in range(len(puzzle)):
                        for iii in range(len(puzzle)):
                            if len({i, ii, iii}) != 3:
                                continue

                            locs0 = [loc for loc in puzzle.house_row(i) if candidate in puzzle.cell_candidates(loc)]
                            locs1 = [loc for loc in puzzle.house_row(ii) if candidate in puzzle.cell_candidates(loc)]
                            locs2 = [loc for loc in puzzle.house_row(iii) if candidate in puzzle.cell_candidates(loc)]

                            loc_set = set(locs0 + locs1 + locs2)

                            rows = set([loc.col for loc in loc_set])

                            has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                            if any(has_solved_candidate):
                                continue

                            if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                                continue

                            if len(rows) != 3:
                                continue

                            for row in rows:
                                row_set = set(puzzle.house_col(row))
                                for loc in row_set.difference(locs0 + locs1 + locs2):
                                    edits += puzzle.rem(loc, [candidate])

            for candidate in puzzle.expected_candidates():
                for i in range(len(puzzle)):
                    for ii in range(len(puzzle)):
                        for iii in range(len(puzzle)):
                            if len({i, ii, iii}) != 3:
                                continue

                            locs0 = [loc for loc in puzzle.house_col(i) if candidate in puzzle.cell_candidates(loc)]
                            locs1 = [loc for loc in puzzle.house_col(ii) if candidate in puzzle.cell_candidates(loc)]
                            locs2 = [loc for loc in puzzle.house_col(iii) if candidate in puzzle.cell_candidates(loc)]

                            loc_set = set(locs0 + locs1 + locs2)

                            rows = set([loc.row for loc in loc_set])

                            has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                            if any(has_solved_candidate):
                                continue

                            if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                                continue

                            if len(rows) != 3:
                                continue

                            for row in rows:
                                row_set = set(puzzle.house_row(row))
                                for loc in row_set.difference(locs0 + locs1 + locs2):
                                    edits += puzzle.rem(loc, [candidate])

            return edits

    class UniqueRectangleType1(BaseUniqueRectangle):
        def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]) -> int:
            edits = 0
            corner_set = set(corners)

            length_2 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 2]

            if len(length_2) != 3:
                return edits

            candidate_set = set()

            for loc in length_2:
                cell = puzzle.cell_candidates(loc)

                if len(cell) == 1:
                    return edits
                for c in cell:
                    candidate_set.add(c)

            if len(candidate_set) != 2:
                return edits

            corner_unique_set = corner_set.difference(length_2)

            if len(corner_unique_set) != 1:
                return edits

            edits += puzzle.rem([corner_unique_set.pop()], candidate_set)

            return edits

    class UniqueRectangleType2:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for corner0 in list(puzzle.unsolved_cells()):
                for corner1 in list(puzzle.unsolved_cells()):
                    corners = [
                        corner0,
                        corner1,
                        Loc(corner0.row, corner1.col),
                        Loc(corner1.row, corner0.col),
                    ]

                    rows = set([loc.row for loc in corners])
                    cols = set([loc.col for loc in corners])
                    fences = set([puzzle.cell_fence(loc) for loc in corners])
                    try:
                        if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                            continue
                        length_2 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 2]
                        length_3 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 3]

                        if len(length_2) != 2 or len(length_3) != 2:
                            continue

                        length_2_candidates = [puzzle.cell_candidates(loc) for loc in length_2]
                        length_3_candidates = [puzzle.cell_candidates(loc) for loc in length_3]

                        if not set(length_2_candidates[0]).issubset(length_2_candidates[1]) or \
                                not set(length_2_candidates[0]).issuperset(length_2_candidates[1]):
                            continue

                        if not set(length_3_candidates[0]).issubset(length_3_candidates[1]) or not set(
                                length_3_candidates[0]).issuperset(length_3_candidates[1]):
                            continue

                        if not set(length_3_candidates[0]).issuperset(length_2_candidates[0]):
                            continue

                        # print(length_2_candidates[0])
                        # print(length_3_candidates[0])

                        candidate_to_remove = list(set(length_3_candidates[0]).difference(length_2_candidates[0]))[0]

                        # print(candidate_to_remove)

                        if length_3[0].col == length_3[1].col:
                            locs_to_remove_from = set(puzzle.house_col(length_3[0].col)).difference(length_3)

                            for loc in locs_to_remove_from:
                                edits += puzzle.rem(loc, [candidate_to_remove])

                        if length_3[0].row == length_3[1].row:
                            locs_to_remove_from = set(puzzle.house_row(length_3[0].row)).difference(length_3)

                            for loc in locs_to_remove_from:
                                edits += puzzle.rem(loc, [candidate_to_remove])

                        if puzzle.cell_fence(length_3[0]) == puzzle.cell_fence(length_3[1]):
                            locs_to_remove_from = set(puzzle.house_fence(puzzle.cell_fence(length_3[0]))).difference(
                                length_3)

                            for loc in locs_to_remove_from:
                                edits += puzzle.rem(loc, [candidate_to_remove])
                    except Exception as e:
                        print(corners)
                        print(puzzle)
                        raise e

            return edits

        # def solve1(self, puzzle: Sudoku, corners: list[Loc]) -> int:
        #     edits = 0

        #     corner_set = set(corners)

        #     if len(corner_set) != 4:
        #         raise ValueError(f'cannot make unique rectangle from {len(corner_set)} corner(s)')

        #     rows = set([loc.row for loc in corner_set])
        #     if len(rows) != 2:
        #         raise ValueError(f'cannot make unique rectangle from {len(rows)} row(s)')

        #     cols = set([loc.col for loc in corner_set])
        #     if len(cols) != 2:
        #         raise ValueError(f'cannot make unique rectangle from {len(cols)} col(s)')

        #     fences = set([puzzle.cell_fence(loc) for loc in corner_set])
        #     if len(fences) != 2:
        #         raise ValueError(f'cannot make unique rectangle from {len(fences)} fence(s)')

        #     two_candidates = [loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 2]
        #     three_candidates = [loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 3]

        #     if len(two_candidates) != 2:
        #         return edits

        #     if len(three_candidates) != 2:
        #         return edits

        #     two_candidates_set0 = set(puzzle.cell_candidates(two_candidates[0]))
        #     two_candidates_set1 = set(puzzle.cell_candidates(two_candidates[1]))

        #     three_candidates_set0 = set(puzzle.cell_candidates(three_candidates[0]))
        #     three_candidates_set1 = set(puzzle.cell_candidates(three_candidates[1]))

        #     if puzzle.cell_fence(two_candidates[0]) != puzzle.cell_fence(two_candidates[1]):
        #         return edits

        #     if puzzle.cell_fence(three_candidates[0]) != puzzle.cell_fence(three_candidates[1]):
        #         return edits

        #     # checks to see if the two_candidates are the same set
        #     if not two_candidates_set0.issubset(two_candidates_set1):
        #         return edits

        #     # checks to see if the three_candidates are the same set
        #     if not three_candidates_set0.issubset(three_candidates_set1):
        #         return edits

        #     # checks to see that three_candidates is a superset of two_candidates
        #     if not three_candidates_set0.issuperset(two_candidates_set0):
        #         return edits

        #     if three_candidates[0].row == three_candidates[1].row:
        #         row = three_candidates[0].row
        #         fence = puzzle.cell_fence(three_candidates[0])
        #         row_house_set = set(puzzle.house_row(row))
        #         fence_house_set = set(puzzle.house_fence(fence))

        #         row_house_set.discard(three_candidates[0])
        #         row_house_set.discard(three_candidates[1])
        #         fence_house_set.discard(three_candidates[0])
        #         fence_house_set.discard(three_candidates[1])

        #         for loc in list(row_house_set) + list(fence_house_set):
        #             edits += puzzle.rem(loc, set(three_candidates_set0).difference(two_candidates_set0))

        #     return edits

    class XyzWing:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for pivot in puzzle.unsolved_cells():
                pivot_candidates = set(puzzle.cell_candidates(pivot))

                if len(pivot_candidates) != 3:
                    continue

                pivot_fence = puzzle.cell_fence(pivot)

                pivot_fence_set = set(puzzle.house_fence(pivot_fence)).difference([pivot])

                for loc_in_fence in pivot_fence_set:
                    loc_in_fence_candidates = puzzle.cell_candidates(loc_in_fence)

                    if len(loc_in_fence_candidates) != 2:
                        continue

                    # print(pivot_candidates)

                    if not pivot_candidates.issuperset(loc_in_fence_candidates):
                        continue

                    pivot_row_set = set(puzzle.house_row(pivot.row)).difference([pivot, loc_in_fence])

                    for loc_in_row in pivot_row_set:
                        loc_in_row_candidates = puzzle.cell_candidates(loc_in_row)

                        if len(loc_in_row_candidates) != 2:
                            continue

                        if not pivot_candidates.issuperset(loc_in_row_candidates):
                            continue

                        if set(loc_in_row_candidates).issuperset(loc_in_fence_candidates):
                            continue

                        if not pivot_candidates.issuperset(list(loc_in_row_candidates) + list(loc_in_fence_candidates)):
                            continue

                        intersection = pivot_candidates.intersection(loc_in_row_candidates).intersection(
                            loc_in_fence_candidates)

                        if len(intersection) != 1:
                            continue

                        candidate_to_remove = list(intersection)[0]

                        intersection_locs = pivot_fence_set.intersection(pivot_row_set)

                        for loc in intersection_locs:
                            edits += puzzle.rem(loc, [candidate_to_remove])

                    pivot_col_set = set(puzzle.house_col(pivot.col)).difference([pivot, loc_in_fence])

                    for loc_in_col in pivot_col_set:
                        loc_in_col_candidates = puzzle.cell_candidates(loc_in_col)

                        if len(loc_in_col_candidates) != 2:
                            continue

                        if not pivot_candidates.issuperset(loc_in_col_candidates):
                            continue

                        if set(loc_in_col_candidates).issuperset(loc_in_fence_candidates):
                            continue

                        if not pivot_candidates.issuperset(list(loc_in_col_candidates) + list(loc_in_fence_candidates)):
                            continue

                        intersection = pivot_candidates.intersection(loc_in_col_candidates).intersection(
                            loc_in_fence_candidates)

                        if len(intersection) != 1:
                            continue

                        candidate_to_remove = list(intersection)[0]

                        intersection_locs = pivot_fence_set.intersection(pivot_col_set)

                        for loc in intersection_locs:
                            edits += puzzle.rem(loc, [candidate_to_remove])
            return edits

    class XyWing:
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits
            for pivot in puzzle.unsolved_cells():
                pivot_candidates = puzzle.cell_candidates(pivot)

                pivot_fence = puzzle.cell_fence(pivot)

                if len(pivot_candidates) != 2:
                    continue

                row_locs = [loc for loc in puzzle.house_row(pivot.row) if
                            loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
                col_locs = [loc for loc in puzzle.house_col(pivot.col) if
                            loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
                fence_locs = [loc for loc in puzzle.house_fence(puzzle.cell_fence(pivot)) if
                              loc != pivot and len(puzzle.cell_candidates(loc)) == 2]

                for row_loc in row_locs:
                    row_difference = set(puzzle.cell_candidates(row_loc)).difference(pivot_candidates)
                    row_fence = puzzle.cell_fence(row_loc)
                    if len(row_difference) != 1:
                        continue
                    for col_loc in col_locs:
                        col_difference = set(puzzle.cell_candidates(col_loc)).difference(pivot_candidates)
                        col_fence = puzzle.cell_fence(col_loc)
                        if col_fence == row_fence:
                            continue
                        if len(col_difference) != 1:
                            continue
                        if not row_difference.issubset(col_difference):
                            continue
                        # check if three fences
                        if row_fence != pivot_fence and col_fence != pivot_fence:
                            other_loc = Loc(col_loc.row, row_loc.col)
                            edits += puzzle.rem(other_loc, row_difference)

            return edits

        # @staticmethod
        # def solve1(puzzle: Sudoku, locs: list[Loc]) -> int:
        #     edits = 0
        #     if len(locs) != 3:
        #         return edits
        #
        #     candidate_set = set()
        #
        #     for loc in locs:
        #         for candidate in puzzle.cell_candidates(loc):
        #             candidate_set.add(candidate)
        #
        #     if len(candidate_set) != 3:
        #         return edits
        #
        #     # need to find a pivot
        #     for pivot in locs:
        #         pincers = set(locs)
        #         pincers.remove(pivot)
        #         pincer0, pincer1 = pincers
        #
        #         pincer_fence0 = puzzle.cell_fence(pincer0)
        #         pincer_fence1 = puzzle.cell_fence(pincer1)
        #
        #         if pincer_fence0 == pincer_fence1:
        #             continue
        #
        #         temp_pivot0 = Loc(pincer0.row, pincer1.col)
        #         temp_pivot1 = Loc(pincer1.row, pincer0.col)
        #
        #         pivot_candidates = puzzle.cell_candidates(pivot)
        #         pincer0_candidates = set(puzzle.cell_candidates(pincer0))
        #         pincer1_candidates = set(puzzle.cell_candidates(pincer1))
        #
        #         if len(pivot_candidates) != 2 or len(pincer0_candidates) != 2 or len(pincer1_candidates) != 2:
        #             continue
        #
        #         if pincer0_candidates.issubset(pincer1_candidates):
        #             continue
        #
        #         # print(f'{pivot} {pincer0} {pincer1}')
        #
        #         for candidate in pivot_candidates:
        #             if candidate in pincer0_candidates:
        #                 pincer0_candidates.remove(candidate)
        #             if candidate in pincer1_candidates:
        #                 pincer1_candidates.remove(candidate)
        #
        #         if len(pincer0_candidates) != 1 or len(pincer1_candidates) != 1 or not pincer1_candidates.issubset(
        #                 pincer0_candidates):
        #             continue
        #
        #         shared_candidate = list(pincer0_candidates)[0]
        #
        #         other_pivot = None
        #
        #         if pivot == temp_pivot0:
        #             other_pivot = temp_pivot1
        #
        #         if pivot == temp_pivot1:
        #             other_pivot = temp_pivot0
        #
        #         if other_pivot is None:
        #             continue
        #
        #         if len(puzzle.cell_candidates(other_pivot)) == 1:
        #             continue
        #
        #             #
        #         # print(f'{pivot} {pincer0} {pincer1} {other_pivot}')
        #         # print(f'{puzzle.cell_candidates(pivot)} {puzzle.cell_candidates(pincer0)} {self.cell_candidates(pincer1)} {self.cell_candidates(other_pivot)}')
        #         edits += puzzle.rem(other_pivot, [shared_candidate])
        #
        #     return edits

    class XChain:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class XWing:

        def solve_two_cell(self, puzzle: Sudoku, cell0: Loc, cell1: Loc, candidate: int) -> int:
            edits = 0

            if cell0.row == cell1.row:
                for row in set(range(len(puzzle))).difference([cell0.row]):
                    other0 = Loc(row, cell0.col)
                    other1 = Loc(row, cell1.col)
                    corners = [cell0, cell1, other0, other1]
                    other_candidates0 = puzzle.cell_candidates(other0)
                    other_candidates1 = puzzle.cell_candidates(other1)
                    if len(other_candidates0) == 1 or \
                            len(other_candidates1) == 1 or \
                            candidate not in other_candidates0 or \
                            candidate not in other_candidates1:
                        continue
                    other_row_house = puzzle.house_row(other0.row, candidate)
                    if len(other_row_house) != 2:
                        continue
                    if {other0, other1} != set(other_row_house):
                        continue
                    locs_to_remove_from = set(puzzle.house_col(other0.col) + puzzle.house_col(other1.col)).difference(
                        corners)
                    edits += puzzle.rem(locs_to_remove_from, [candidate])

            if cell0.col == cell1.col:
                for col in set(range(len(puzzle))).difference([cell0.col]):
                    other0 = Loc(cell0.row, col)
                    other1 = Loc(cell1.row, col)
                    corners = [cell0, cell1, other0, other1]
                    other_candidates0 = puzzle.cell_candidates(other0)
                    other_candidates1 = puzzle.cell_candidates(other1)
                    if len(other_candidates0) == 1 or \
                            len(other_candidates1) == 1 or \
                            candidate not in other_candidates0 or \
                            candidate not in other_candidates1:
                        continue
                    other_col_house = puzzle.house_col(other0.col, candidate)
                    if len(other_col_house) != 2:
                        continue
                    if {other0, other1} != set(other_col_house):
                        continue
                    locs_to_remove_from = set(puzzle.house_row(other0.row) + puzzle.house_row(other1.row)).difference(
                        corners)
                    edits += puzzle.rem(locs_to_remove_from, [candidate])

            return edits

        def solve_one_cell(self, puzzle: Sudoku, cell0: Loc, candidate: int) -> int:

            edits = 0
            # need to find the next cell to form a base

            row_cells = set(puzzle.house_row(cell0.row, candidate))
            col_cells = set(puzzle.house_col(cell0.col, candidate))

            if len(row_cells) == 2:
                row_cells.remove(cell0)
                edits += self.solve_two_cell(puzzle, cell0, row_cells.pop(), candidate)

            if len(col_cells) == 2:
                col_cells.remove(cell0)
                edits += self.solve_two_cell(puzzle, cell0, col_cells.pop(), candidate)

            return edits

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            # print("here")
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)

                    if puzzle.is_cell_solved(loc):
                        continue

                    for candidate in puzzle.cell_candidates(loc):
                        edits += self.solve_one_cell(puzzle, loc, candidate)
            return edits

    class XyChain:

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class LighthousesTech(Technique):

        def solve0(self, puzzle: Lighthouses) -> int:
            edits = 0

            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)

                    number = puzzle.light_number(loc)

                    if puzzle.grid[r][c] == '+_':
                        edits += puzzle.rem(puzzle.surrounding(loc), ['+'])

                    if number is not None:
                        edits += puzzle.rem(puzzle.surrounding(loc), ['+'])
                        row_locs = puzzle.house_row(r)
                        col_locs = puzzle.house_col(c)
                        extending = [loc0 for loc0 in set(row_locs + col_locs) if
                                     puzzle.is_candidate_cell(loc0) and loc0 != loc]
                        if number == 0:
                            edits += puzzle.rem(extending, ['+'])

                        solved_light = []
                        solved_empty = []
                        unsolved = []

                        for loc0 in extending:
                            if puzzle.grid[loc0.row][loc0.col] == '+-':
                                unsolved.append(loc0)
                            if puzzle.grid[loc0.row][loc0.col] == '+_':
                                solved_light.append(loc0)
                            if puzzle.grid[loc0.row][loc0.col] == '_-':
                                solved_empty.append(loc0)

                        if len(unsolved) == 1 and len(solved_light) == 1 and number == 2:
                            edits += puzzle.rem(unsolved, ['-'])

                        # if len(unsolved) == 2 and number == 2 and len(solved_light) == 0:
                        #     edits += puzzle.rem(unsolved, ['-'])
                        #
                        if number == 1 and len(unsolved) == 1:
                            edits += puzzle.rem(unsolved, ['-'])

                        if len(solved_light) == 1 and len(unsolved) == 2 and number == 3:
                            edits += puzzle.rem(unsolved, ['-'])

                        if len(solved_light) == 0 and len(unsolved) == 3 and number == 2:
                            for un in unsolved:
                                temp_set = set(unsolved)

                                temp_set.remove(un)

                                other0, other1 = temp_set

                                if un.is_next_to(other0) and not un.is_next_to(other1):
                                    edits += puzzle.rem([other1], ['-'])

                                    if un.col == other0.col:
                                        surrounding0 = puzzle.surrounding(un)
                                        surrounding1 = puzzle.surrounding(other0)

                                        intersection = set(surrounding0).intersection(surrounding1)

                                        locs_to_rem = [loc1 for loc1 in intersection if
                                                       loc1.row == un.row or loc1.row == other0.row]
                                        edits += puzzle.rem(locs_to_rem, ['+'])

            return edits

    class Skyscrapers1:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(len(puzzle)):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == 1:
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if south == 1:
                    edits += puzzle.rem([Loc(len(puzzle) - 1, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if west == 1:
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if east == 1:
                    edits += puzzle.rem([Loc(index, len(puzzle) - 1)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

            return edits

    class SkyscrapersRange:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0
            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(len(puzzle)):
                house = puzzle.house_row(index)
                tuples.append((puzzle.west_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.east_scraper(index), house))
                house = puzzle.house_col(index)
                tuples.append((puzzle.north_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.south_scraper(index), house))

            for tuple0 in tuples:
                scraper, house = tuple0
                if scraper is None:
                    continue

                string = "".join([puzzle.grid[loc.row][loc.col] for loc in house])

                if string == "1____23__23____4" and scraper == 4:
                    edits += puzzle.rem([house[1]], [3])

                if string == "1____23__23____4" and scraper == 3:
                    edits += puzzle.rem([house[1]], [2])

                if string == "123_1_3_12_____4" and scraper == 2:
                    edits += puzzle.rem([house[0]], [1, 2, 4])

                if string == "123_123_123____4" and scraper == 2:
                    edits += puzzle.rem([house[0]], [1, 2, 4])

                if string == "12__12_____4__3_" and scraper == 3:
                    edits += puzzle.rem([house[0]], [1])

                if string == "_23__23____41___" and scraper == 3:
                    edits += puzzle.rem([house[0]], [3])

                if string == "_23__23____41___" and scraper == 2:
                    edits += puzzle.rem([house[0]], [2])

                if string == "123_123_123____4" and scraper == 3:
                    edits += puzzle.rem([house[0]], [3])

                if string == "123_123_12341234" and scraper == 3:
                    edits += puzzle.rem([house[0]], [3])

                if string == "12__12____3____4" and scraper == 3:
                    edits += puzzle.rem([house[0]], [1])

                if string == "_2_4_2_41_____3_" and scraper == 2:
                    edits += puzzle.rem([house[0]], [4])

                if string == "1_3__2_____41_3_" and scraper == 2:
                    edits += puzzle.rem([house[0]], [1])

                if string == "1234123412341234" and scraper == 3:
                    edits += puzzle.rem([house[0]], [4])

                if string == "1234123412341234" and scraper == 2:
                    edits += puzzle.rem([house[0]], [4])

            # 1___ ___4 _23_ _23_

            # print(string)

            # house_candidates = [puzzle.cell_candidates(loc) for loc in house]
            # for index in range(puzzle.length):
            #     candidates = house_candidates[index]
            #     if len(candidates) != 1:
            #         continue
            #     solved_candidate = candidates[0]
            #     if solved_candidate != puzzle.length:
            #         continue
            #     if index == 0 or index == puzzle.length - 1:
            #         continue
            #
            #
            #     print("her111r")

            # candidates1 = puzzle.cell_candidates(house[1])
            #
            # if len(candidates1) != 1:
            #     continue
            # if candidates1[0] != puzzle.length:
            #     continue
            # difference = scraper - puzzle.length
            #
            # edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([difference]))

            return edits

    class SkyscrapersN:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(len(puzzle)):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == len(puzzle):
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if south == len(puzzle):
                    edits += puzzle.rem([Loc(len(puzzle) - 1, index)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if west == len(puzzle):
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if east == len(puzzle):
                    edits += puzzle.rem([Loc(index, len(puzzle) - 1)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

            return edits

    class MinesweeperSolver:

        @staticmethod
        def surrounding(puzzle, loc: Loc) -> list[Loc]:
            valid = []
            directions = [
                loc.north(),
                loc.east(),
                loc.south(),
                loc.west(),
                loc.north().east(),
                loc.north().west(),
                loc.south().east(),
                loc.south().west(),
            ]

            for temp in directions:
                if temp.is_valid_parks(puzzle.grid):
                    valid.append(temp)

            return valid

        def solve0(self, puzzle: Minesweeper) -> int:
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    if puzzle.is_number_cell(loc):
                        number = int(puzzle.grid[loc.row][loc.col])

                        if number == 0:
                            edits += puzzle.rem()

            return edits

    class CrossHatchRobotFences:
        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0
            for cell in list(puzzle.unsolved_cells()):
                neighbors = set(puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
                neighbors.remove(cell)
                for neighbor in neighbors:
                    if neighbor not in puzzle.unsolved_cells():
                        _candidates = puzzle.cell_candidates(neighbor)
                        if len(_candidates) == 1:
                            edits += puzzle.rem(cell, [list(_candidates)[0]])
            return edits

    class HiddenSingleRobotFences:

        @staticmethod
        def get_required_candidates(puzzle: RobotFences, house: list[Loc]) -> list[int]:
            length = len(puzzle)
            solved_candidates = [puzzle.cell_candidates(loc)[0] for loc in house if
                                 len(puzzle.cell_candidates(loc)) == 1]

            minimum = min(solved_candidates)
            maximum = max(solved_candidates)

            temp_min = max([1, maximum - length + 1])
            temp_max = max([length, minimum + length - 1])

            return list(range(temp_min, temp_max + 1))

        @staticmethod
        def solve0(puzzle: RobotFences) -> int:
            edits = 0
            # return edits
            for cell in list(puzzle.unsolved_cells()):
                neighbors = set(puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
                neighbors.remove(cell)
                for neighbor in neighbors:
                    if neighbor not in puzzle.unsolved_cells():
                        _candidates = puzzle.cell_candidates(neighbor)
                        if len(_candidates) == 1:
                            edits += puzzle.rem(cell, [list(_candidates)[0]])

            for fence_house in puzzle.houses_fences():

                if len(fence_house) == len(puzzle):
                    edits += tech.HiddenSingle.solve1(puzzle, fence_house)
                    continue

                #  get the solved candidates in the fence_house
                solved_candidates = [puzzle.cell_candidates(loc)[0] for loc in fence_house if
                                     len(puzzle.cell_candidates(loc)) == 1]

                if len(solved_candidates) == 0:
                    continue

                length = len(fence_house)

                minimum = min(solved_candidates)
                maximum = max(solved_candidates)

                temp_min = max([1, maximum - length + 1])
                temp_max = max([length, minimum + length - 1])

                expected_candidates = tech.HiddenSingleRobotFences.get_required_candidates(puzzle, fence_house)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(expected_candidates))
                # print(candidates_to_remove)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(range(temp_min, temp_max + 1)))
                # print(candidates_to_remove)

                for loc in fence_house:
                    edits += puzzle.rem(loc, candidates_to_remove)

            return edits

    class FutoshikiGreaterThanLessThan:  # (BaseFutoshikiTechnique):
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0

            for r in range(puzzle.length * 2 - 1):
                for c in range(puzzle.length * 2 - 1):

                    even_row = r % 2 == 0
                    even_col = c % 2 == 0

                    if even_row and even_col:
                        continue

                    if not even_row and not even_col:
                        continue

                    if even_row:
                        loc = Loc(r, c)
                        string = puzzle.cell_string(loc)

                        if string == '>':
                            edits += self.solve_greater_than(puzzle, loc.east(), loc.west())

                        # print(puzzle.cell_string(loc))
            # for row_house in puzzle.house_row_cells()

            return edits

        def solve_greater_than(self, puzzle: Futoshiki, lesser: Loc, greater: Loc):
            edits = 0
            lesser_candidates = puzzle.cell_candidates(lesser)
            greater_candidates = puzzle.cell_candidates(greater)

            min_greater = min(greater_candidates)
            max_lesser = max(lesser_candidates)

            print(min_greater)
            print(max_lesser)

            for candidate in lesser_candidates:
                if candidate >= min_greater:
                    print(f'removing {candidate} from {lesser}')
                    edits += puzzle.rem([lesser], [str(candidate)])

            # print(lesser_candidates)
            # print(greater_candidates)

            return edits

    class FutoshikiCrossHatch:
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0
            return edits

    class RobotCrosswordsHouses:
        def solve0(self, puzzle: RobotCrosswords) -> int:
            edits = 0

            houses = []

            for row in range(len(puzzle)):
                house = []
                for col in range(len(puzzle)):
                    house.append(Loc(row, col))
                houses.append(house)

            for col in range(len(puzzle)):
                house = []
                for row in range(len(puzzle)):
                    house.append(Loc(row, col))
                houses.append(house)

            for house in houses:

                # temp_house = list(house)
                #
                #
                #
                #
                #
                #
                # continue

                string = ""

                all_crosswords = []

                in_crossword = False

                crossword = []

                for index in range(len(house)):
                    if 'x' in puzzle.grid[house[index].row][house[index].col]:
                        if in_crossword:
                            all_crosswords.append(list(crossword))
                            crossword = []
                            in_crossword = False
                            # continue
                    elif in_crossword:
                        crossword.append(house[index])
                    else:
                        crossword.append(house[index])
                        in_crossword = True
                # for cross in

                print(all_crosswords)

                # loc = house[index]

                #     string += f'{puzzle.grid[loc.row][loc.col]} '
                #
                # string = string.replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).strip()
                # .split(" ")

                # string = string.strip()

                # print(string)

            return edits

    class MagnetsFullHouse:
        def __int__(self):
            self.EMPTY = 0

        def solve0(self, puzzle: Magnets) -> int:
            edits = 0

            for i in range(puzzle.length):
                plus_row_value = puzzle.plus_row_value(i)
                minus_row_value = puzzle.minus_row_value(i)
                row_house = puzzle.house_row(i)

                if plus_row_value + minus_row_value == puzzle.length:
                    edits += puzzle.rem(row_house, [self.EMPTY])

                plus_col_value = puzzle.plus_col_value(i)
                minus_col_value = puzzle.minus_col_value(i)
                col_house = puzzle.house_col(i)

                if plus_col_value + minus_col_value == puzzle.length:
                    edits += puzzle.rem(col_house, [self.EMPTY])

            return edits

    class MagnetsPair:
        def __int__(self):
            self.PLUS = 1
            self.MINUS = 0
            self.EMPTY = self.MINUS

        def solve1(self, puzzle: Magnets, loc0: Loc, loc1: Loc) -> int:
            edits = 0
            candidates0 = puzzle.cell_candidates(loc0)
            candidates1 = puzzle.cell_candidates(loc1)

            if self.EMPTY not in candidates0:
                edits += puzzle.rem([loc1], [self.EMPTY])

            if self.EMPTY not in candidates1:
                edits += puzzle.rem([loc0], [self.EMPTY])

            if self.PLUS not in candidates0:
                edits += puzzle.rem([loc1], [self.MINUS])

            if self.PLUS not in candidates1:
                edits += puzzle.rem([loc0], [self.MINUS])

            if self.MINUS not in candidates0:
                edits += puzzle.rem([loc1], [self.PLUS])

            if self.MINUS not in candidates1:
                edits += puzzle.rem([loc0], [self.PLUS])

            return edits

        def solve0(self, puzzle: Magnets) -> int:
            edits = 0

            # loc0 = Loc(1, 1)
            # loc1 = Loc(1, 2)

            for magnets_fence_pair in puzzle.house_fences():
                loc0, loc1 = magnets_fence_pair
                #
                #     if puzzle.house_fence(loc0) != 'a':
                #         continue
                #
                edits += self.solve1(puzzle, loc0, loc1)

            return edits

    class MagnetsZero:
        def __int__(self):
            self.PLUS = 1
            self.MINUS = 0
            self.EMPTY = self.MINUS

        def solve0(self, puzzle: Magnets) -> int:
            edits = 0
            for i in range(puzzle.length):
                plus_row_value = puzzle.plus_row_value(i)
                row_house = puzzle.house_row(i)
                if plus_row_value == 0:
                    for loc in row_house:
                        edits += puzzle.rem([loc], [self.PLUS])
                plus_col_value = puzzle.plus_col_value(i)
                col_house = puzzle.house_col(i)
                if plus_col_value == 0:
                    for loc in col_house:
                        edits += puzzle.rem([loc], [self.PLUS])
                minus_row_value = puzzle.minus_row_value(i)
                row_house = puzzle.house_row(i)
                if minus_row_value == 0:
                    for loc in row_house:
                        edits += puzzle.rem([loc], [self.MINUS])
                minus_col_value = puzzle.minus_col_value(i)
                col_house = puzzle.house_col(i)
                print(minus_col_value)
                if minus_col_value == 0:
                    for loc in col_house:
                        edits += puzzle.rem([loc], [self.MINUS])
            return edits

    class MathraxHiddenSingle:

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            return edits

    class MathraxMath:

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(1, len(puzzle) * 2 - 1, 2):
                for c in range(1, len(puzzle) * 2 - 1, 2):
                    loc = Loc(r, c)
                    string = puzzle.grid[r][c]
                    if '+' in string:
                        number = int(string.replace('+', ''))
                        edits += self.solve_addition(puzzle, number, loc.top_left(), loc.bottom_right())
                        edits += self.solve_addition(puzzle, number, loc.top_right(), loc.bottom_left())

                    if '/' in string:
                        number = int(string.replace('/', ''))
                        edits += self.solve_division(puzzle, number, loc.top_left(), loc.bottom_right())
                        edits += self.solve_division(puzzle, number, loc.top_right(), loc.bottom_left())

                    if '-' in string:
                        number = int(string.replace('-', ''))
                        edits += self.solve_subtraction(puzzle, number, loc.top_left(), loc.bottom_right())
                        edits += self.solve_subtraction(puzzle, number, loc.top_right(), loc.bottom_left())
            return edits

        @staticmethod
        def __solve_addition(puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = 0
            candidates1 = set(puzzle.cell_candidates(cell1))
            for candidate0 in puzzle.cell_candidates(cell0):
                if any(candidate0 + candidate1 == number for candidate1 in candidates1):
                    continue
                edits += puzzle.rem([cell0], [candidate0])
            return edits

        def solve_addition(self, puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = self.__solve_addition(puzzle, number, cell0, cell1)
            edits += self.__solve_addition(puzzle, number, cell1, cell0)
            return edits

        def solve_division(self, puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = self.__solve_division(puzzle, number, cell0, cell1)
            edits += self.__solve_division(puzzle, number, cell1, cell0)
            return edits

        @staticmethod
        def __solve_division(puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = 0
            candidates1 = set(puzzle.cell_candidates(cell1))
            for candidate0 in puzzle.cell_candidates(cell0):
                if any(candidate0 % candidate1 == 0 and int(candidate0 / candidate1) == number for candidate1 in
                       candidates1):
                    continue
                if any(candidate1 % candidate0 == 0 and int(candidate1 / candidate0) == number for candidate1 in
                       candidates1):
                    continue
                edits += puzzle.rem([cell0], [candidate0])
            return edits

        def solve_subtraction(self, puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = self.__solve_subtraction(puzzle, number, cell0, cell1)
            edits += self.__solve_subtraction(puzzle, number, cell1, cell0)
            return edits

        @staticmethod
        def __solve_subtraction(puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = 0
            candidates1 = set(puzzle.cell_candidates(cell1))
            for candidate0 in puzzle.cell_candidates(cell0):
                if any(candidate0 - candidate1 == number for candidate1 in candidates1):
                    continue
                if any(candidate1 - candidate0 == number for candidate1 in candidates1):
                    continue
                edits += puzzle.rem([cell0], [candidate0])
            return edits

    class TennerCrossHatch(Technique):

        def solve0(self, puzzle: Tenner) -> int:
            edits = 0

            for r in range(len(puzzle)):
                for c in range(puzzle.col_length):
                    cell = Loc(r, c)
                    candidates = puzzle.cell_candidates(cell)
                    if len(candidates) != 1:
                        continue
                    solved_candidate = candidates[0]

                    for c0 in range(puzzle.col_length):
                        if c0 == c:
                            continue
                        edits += puzzle.rem([Loc(r, c0)], [solved_candidate])
                    directions = [
                        cell.north(),
                        cell.east(),
                        cell.south(),
                        cell.west(),
                        cell.north().east(),
                        cell.north().west(),
                        cell.south().east(),
                        cell.south().west()
                    ]
                    for direction in directions:
                        if direction.row < 0 or direction.col < 0:
                            continue
                        if direction.row >= len(puzzle) or direction.col >= 10:
                            continue
                        edits += puzzle.rem([direction], [solved_candidate])
            return edits

    class TennerHiddenPair:
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for index in range(len(puzzle)):
                house = puzzle.house_row_cell_locs(index)
                expected = puzzle.expected_candidates()

                for i in range(len(expected) - 1):
                    for ii in range(i, len(expected)):
                        if expected[i] == expected[ii]:
                            continue

                        locs0 = [loc for loc in house if expected[i] in puzzle.cell_candidates(loc)]
                        locs1 = [loc for loc in house if expected[ii] in puzzle.cell_candidates(loc)]

                        if len(locs0) != 2 or len(locs1) != 2:
                            continue

                        loc_set = set(locs0 + locs1)

                        if len(loc_set) != 2:
                            continue

                        temp_locs = list(loc_set)

                        for k in set(expected).difference([expected[i], expected[ii]]):
                            edits += puzzle.rem(temp_locs[0], [k])
                            edits += puzzle.rem(temp_locs[1], [k])
            return edits

    class TennerHiddenSingle:
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for row in range(len(puzzle)):
                house = puzzle.house_row_cell_locs(row)
                edits += tech.HiddenSingle.solve1(puzzle, house)
            return edits

    class TennerNakedPair:
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for row in range(len(puzzle)):
                house = puzzle.house_row_cell_locs(row)
                edits += tech.NakedPair.static_solve_house(puzzle, house)
            return edits

    class TennerNakedPairColumn:
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)

                for index in range(len(puzzle) - 1):
                    loc0 = house[index]
                    loc1 = house[index + 1]

                    loc0_candidates = set(puzzle.cell_candidates(loc0))
                    loc1_candidates = set(puzzle.cell_candidates(loc1))

                    if len(loc0_candidates) != 2:
                        continue

                    if not loc1_candidates.issuperset(loc0_candidates) or not loc0_candidates.issuperset(
                            loc1_candidates):
                        continue

                    directions = [
                        loc0.west(),
                        loc0.east(),
                        loc1.west(),
                        loc1.east(),
                    ]

                    for direction in directions:
                        if direction.col < 0 or direction.col >= puzzle.col_length:
                            continue
                        edits += puzzle.rem([direction], loc0_candidates)

            return edits

    class TennerPowerSetTotals(Technique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)
                total = puzzle.total(col)
                edits += self.solve1(puzzle, house, total)
            return edits

        def solve1(self, puzzle: Tenner, house: list[Loc], total: Optional[int]) -> int:
            edits = 0
            if total is None:
                return edits
            valid_candidates_dict = {house[i]: set() for i in range(len(puzzle))}
            for candidates in tech.TennerPowerSetTotals.power_set_candidates(puzzle, house):
                self.mid(puzzle, valid_candidates_dict, candidates, house, total)
            edits += self.end(puzzle, valid_candidates_dict, house)
            return edits

        @staticmethod
        def mid(puzzle, valid_candidates_dict, candidates, house, total):
            if sum(candidates) != total:
                return
            is_valid_column = [candidates[index] != candidates[index + 1] for index in
                               range(len(puzzle) - 1)]
            if not all(is_valid_column):
                return
            for index in range(len(puzzle)):
                valid_candidates_dict[house[index]].add(candidates[index])

        @staticmethod
        def end(puzzle: Tenner, valid_candidates_dict, house) -> int:
            edits = 0
            for index in range(len(puzzle)):
                edits += puzzle.rem([house[index]],
                                    list(set(puzzle.expected_candidates()).difference(
                                        valid_candidates_dict[house[index]])))
            return edits

        @staticmethod
        def power_set_candidates(puzzle: Tenner, house: list[Loc]):
            if len(house) == 3:
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            yield [candidate0, candidate1, candidate2]
            if len(house) == 4:
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            for candidate3 in puzzle.cell_candidates(house[3]):
                                yield [candidate0, candidate1, candidate2, candidate3]
            if len(house) == 5:
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            for candidate3 in puzzle.cell_candidates(house[3]):
                                for candidate4 in puzzle.cell_candidates(house[4]):
                                    yield [candidate0, candidate1, candidate2, candidate3, candidate4]
            if len(house) == 6:
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            for candidate3 in puzzle.cell_candidates(house[3]):
                                for candidate4 in puzzle.cell_candidates(house[4]):
                                    for candidate5 in puzzle.cell_candidates(house[5]):
                                        yield [candidate0, candidate1, candidate2, candidate3, candidate4,
                                               candidate5]

    class TennerTotalHiddenSingle:
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for col in range(puzzle.col_length):
                col_house = puzzle.house_col_cell_locs(col)
                total = puzzle.total(col)
                if total is None:
                    continue
                solved_locs = [loc for loc in col_house if puzzle.is_cell_solved(loc)]
                unsolved_locs = [loc for loc in col_house if not puzzle.is_cell_solved(loc)]

                if len(unsolved_locs) != 1:
                    continue

                current_total = sum([puzzle.cell_candidates(loc)[0] for loc in solved_locs])

                needed_candidate = total - current_total

                for candidate in puzzle.expected_candidates():
                    if candidate != needed_candidate:
                        edits += puzzle.rem([unsolved_locs[0]], [candidate])

            return edits

    class LightenUpTech(Technique):
        def solve0(self, puzzle: LightenUp) -> int:
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)

                    if puzzle.grid[r][c] == '+-':
                        locs_to_remove = puzzle.extending_cell_locs(loc)

                        if all(puzzle.grid[loc0.row][loc0.col] == '_-' for loc0 in locs_to_remove):
                            edits += puzzle.rem([loc], ['-'])

                    if puzzle.grid[r][c] == '+_':
                        locs_to_remove = puzzle.extending_cell_locs(loc)

                        edits += puzzle.rem(locs_to_remove, ['+'])

                    if puzzle.grid[r][c] == '+_':
                        for loc0 in puzzle.surrounding_light(loc):
                            if puzzle.is_candidate_cell(loc0):
                                edits += puzzle.rem([loc0], ['+'])

                    light_number = puzzle.light_number(loc)

                    if light_number is None:
                        continue

                    if light_number == 0:
                        edits += puzzle.rem(
                            list(filter(lambda loc1: puzzle.is_candidate_cell(loc1), puzzle.surrounding_light(loc))),
                            ['+'])

                    if light_number == 4:
                        edits += puzzle.rem(
                            list(filter(lambda loc1: puzzle.is_candidate_cell(loc1), puzzle.surrounding_light(loc))),
                            ['-'])

                    solved_light = []
                    solved_empty = []
                    unsolved = []

                    for loc0 in puzzle.surrounding_light(loc):
                        if puzzle.grid[loc0.row][loc0.col] == '+_':
                            solved_light.append(loc0)
                        if puzzle.grid[loc0.row][loc0.col] == '_-':
                            solved_empty.append(loc0)
                        if puzzle.grid[loc0.row][loc0.col] == '+-':
                            unsolved.append(loc0)

                    if len(solved_light) == 0 and len(unsolved) == light_number:
                        edits += puzzle.rem(unsolved, ['-'])

                    if len(solved_light) == light_number:
                        edits += puzzle.rem(unsolved, ['+'])

                    if len(solved_light) == 2 and light_number == 3 and len(unsolved) == 1:
                        edits += puzzle.rem(unsolved, ['-'])

            return edits

    class PowerGridCrossHatch:
        def solve0(self, puzzle: PowerGrid) -> int:
            edits = 0
            POWER = 1
            EMPTY = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    candidates = puzzle.cell_candidates(loc)
                    if len(candidates) > 1:
                        continue
                    if POWER in candidates:
                        directions = [
                            loc.west(),
                            loc.north(),
                            loc.east(),
                            loc.south(),
                            loc.north().east(),
                            loc.north().west(),
                            loc.south().east(),
                            loc.south().west(),
                        ]

                        for direction in directions:
                            if direction.is_valid_sudoku(len(puzzle)):
                                edits += puzzle.rem([direction], [POWER])

            return edits

    class PowerGridHiddenPower:
        def solve0(self, puzzle: PowerGrid) -> int:
            edits = 0

            for index in range(len(puzzle)):
                row_house = puzzle.house_row(index)
                row_scraper = puzzle.east_scraper(index)
                # if row_scraper is None:
                #     continue
                edits += self.solve1(puzzle, row_scraper, row_house)
                col_house = puzzle.house_col(index)
                col_scraper = puzzle.south_scraper(index)
                # if col_scraper is None:
                #     continue
                edits += self.solve1(puzzle, col_scraper, col_house)
            return edits

        def solve1(self, puzzle: PowerGrid, power: int, house: list[Loc]) -> int:
            edits = 0

            POWER = 1
            EMPTY = 0

            solved_power = []
            solved_empty = []
            unsolved = []

            # for index

            for index in range(len(house)):
                candidates = puzzle.cell_candidates(house[index])

                if len(candidates) > 1:
                    unsolved.append(house[index])
                    continue

                if POWER in candidates:
                    solved_power.append(house[index])

                if EMPTY in candidates:
                    solved_empty.append(house[index])

            if len(solved_power) == 2:
                edits += puzzle.rem(unsolved, [POWER])

            if len(solved_power) == 0 and len(unsolved) == 2:
                edits += puzzle.rem(unsolved, [EMPTY])

            if len(solved_power) == 1 and len(unsolved) == 1:
                edits += puzzle.rem(unsolved, [EMPTY])

            return edits

    class PowerGridTech:
        def solve0(self, puzzle: PowerGrid) -> int:
            edits = 0

            for index in range(len(puzzle)):
                row_house = puzzle.house_row(index)
                row_scraper = puzzle.east_scraper(index)
                if row_scraper is None:
                    continue
                edits += self.solve1(puzzle, row_scraper, row_house)
                col_house = puzzle.house_col(index)
                col_scraper = puzzle.south_scraper(index)
                if col_scraper is None:
                    continue
                edits += self.solve1(puzzle, col_scraper, col_house)
            return edits

        def solve1(self, puzzle: PowerGrid, power: int, house: list[Loc]) -> int:
            edits = 0

            POWER = 1
            EMPTY = 0

            for index in range(len(puzzle)):
                left_index = index - power - 1
                right_index = index + power + 1

                # valid_left =

                if left_index < 0 and right_index >= len(puzzle):
                    edits += puzzle.rem([house[index]], [POWER])

                if left_index < 0 and right_index < len(puzzle) and POWER not in puzzle.cell_candidates(
                        house[right_index]):
                    edits += puzzle.rem([house[index]], [POWER])

                if left_index >= 0 and right_index >= len(puzzle) and POWER not in puzzle.cell_candidates(
                        house[left_index]):
                    edits += puzzle.rem([house[index]], [POWER])

                if left_index >= 0 and right_index < len(puzzle) and POWER not in puzzle.cell_candidates(
                        house[left_index]) and POWER not in puzzle.cell_candidates(house[right_index]):
                    edits += puzzle.rem([house[index]], [POWER])

            return edits

    class KropkiBb:

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0

            for center_cell in puzzle.iterate_cells():
                directions = [
                    [
                        center_cell.west(2),
                        center_cell.west(),
                        center_cell.east(),
                        center_cell.east(2),
                    ],
                    [
                        center_cell.north(2),
                        center_cell.north(),
                        center_cell.south(),
                        center_cell.south(2),
                    ],
                    # west north
                    [
                        center_cell.west(2),
                        center_cell.west(),
                        center_cell.north(),
                        center_cell.north(2),
                    ],
                    # east south
                    [
                        center_cell.east(2),
                        center_cell.east(),
                        center_cell.south(),
                        center_cell.south(2)
                    ],
                    # west south
                    [
                        center_cell.west(2),
                        center_cell.west(),
                        center_cell.south(),
                        center_cell.south(2),
                    ],
                    # east north
                    [
                        center_cell.north(2),
                        center_cell.north(),
                        center_cell.east(),
                        center_cell.east(2),
                    ],
                ]
                for direction in directions:
                    other0, kropki0, kropki1, other1 = direction

                    cell_set = {other0, center_cell, other1}

                    all_our_valid = all([loc.is_valid_kropki(puzzle.grid_length) for loc in cell_set])

                    if not all_our_valid:
                        continue

                    if not puzzle.is_black(kropki0) or not puzzle.is_black(kropki1):
                        continue

                    row_set = {other0.row, center_cell.row, other1.row}
                    col_set = {other0.col, center_cell.col, other1.col}

                    cells_in_sets = []

                    if len(row_set) == 1:
                        cells_in_sets = cells_in_sets + puzzle.house_row_cell_locs(row_set.pop())

                    if len(col_set) == 1:
                        cells_in_sets = cells_in_sets + puzzle.house_col_cell_locs(col_set.pop())

                    if puzzle.has_fences:
                        fence_set = {puzzle.cell_fence(other0), puzzle.cell_fence(center_cell),
                                     puzzle.cell_fence(other1)}
                        if len(fence_set) == 1:
                            cells_in_sets = cells_in_sets + puzzle.house_fence_cell_locs(fence_set.pop())

                    cells_to_remove_from = set(cells_in_sets).difference(cell_set)

                    edits += puzzle.rem(cells_to_remove_from, [2, 4])
                    edits += puzzle.rem([center_cell], [1, 3, 5, 6, 7, 8, 9])
                    edits += puzzle.rem([other0, other1], [3, 5, 6, 7, 9])

            return edits

    class KropkiBlack:
        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r * 2, c * 2)
                    directions = [
                        [loc.north(), loc.north(2)],
                        [loc.south(), loc.south(2)],
                        [loc.east(), loc.east(2)],
                        [loc.west(), loc.west(2)],
                    ]
                    for direction in directions:
                        center, other = direction
                        if not center.is_valid_kropki(puzzle.grid_length):
                            continue
                        if not puzzle.grid[center.row][center.col].replace(".", "", -1) == "BB":
                            continue
                        edits += self.solve1(puzzle, loc, other)
            return edits

        def solve1(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
            return self.solve2(puzzle, loc0, loc1) + self.solve2(puzzle, loc1, loc0)

        def solve2(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
            edits = 0
            other_candidates = set(puzzle.cell_candidates(loc1))
            for candidate in puzzle.cell_candidates(loc0):
                if candidate * 2 in other_candidates:
                    continue
                if candidate % 2 == 0 and candidate / 2 in other_candidates:
                    continue
                edits += puzzle.rem([loc0], [candidate])
            return edits

    class KropkiBw:

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for center_cell in puzzle.iterate_cells():
                directions = [
                    [
                        center_cell.west(2),
                        center_cell.west(),
                        center_cell.east(),
                        center_cell.east(2),
                    ],
                    [
                        center_cell.north(2),
                        center_cell.north(),
                        center_cell.south(),
                        center_cell.south(2),
                    ],
                    # west north
                    [
                        center_cell.west(2),
                        center_cell.west(),
                        center_cell.north(),
                        center_cell.north(2),
                    ],
                    # east south
                    [
                        center_cell.east(2),
                        center_cell.east(),
                        center_cell.south(),
                        center_cell.south(2)
                    ],
                    # west south
                    [
                        center_cell.west(2),
                        center_cell.west(),
                        center_cell.south(),
                        center_cell.south(2),
                    ],
                    # east north
                    [
                        center_cell.north(2),
                        center_cell.north(),
                        center_cell.east(),
                        center_cell.east(2),
                    ],
                ]
                for direction in directions:
                    other0, kropki0, kropki1, other1 = direction

                    cell_set = {other0, center_cell, other1}

                    all_our_valid = all([loc.is_valid_kropki(puzzle.grid_length) for loc in cell_set])

                    if not all_our_valid:
                        continue

                    if (puzzle.is_black(kropki0) and puzzle.is_white(kropki1)) or (
                            puzzle.is_black(kropki1) and puzzle.is_white(kropki0)):
                        edits += puzzle.rem([center_cell], [1])
            return edits

    class KropkiDiamondEbww:
        edits = 0

        def solve0(self, puzzle: Kropki) -> int:
            black_empty = [5, 7, 9]
            black_white = [1, 5, 7, 9]
            white_empty = [3, 5, 7, 9]
            white_white = [1, 4, 6, 8, 9]

            edits = 0
            for r in range(puzzle.grid_length):
                for c in range(puzzle.grid_length):
                    if r % 2 == 0 or c % 2 == 0:
                        continue

                    loc = Loc(r, c)

                    if puzzle.is_empty(loc.north()) and puzzle.is_white(loc.east()) and puzzle.is_white(
                            loc.south()) and puzzle.is_black(loc.west()):
                        edits += puzzle.rem([loc.north().west()], black_empty)
                        edits += puzzle.rem([loc.south().west()], black_white)
                        edits += puzzle.rem([loc.north().east()], white_empty)
                        edits += puzzle.rem([loc.south().east()], white_white)

                    if puzzle.is_empty(loc.east()) and puzzle.is_white(loc.south()) and puzzle.is_white(
                            loc.west()) and puzzle.is_black(loc.north()):
                        edits += puzzle.rem([loc.north().west()], black_white)
                        edits += puzzle.rem([loc.south().west()], white_white)
                        edits += puzzle.rem([loc.north().east()], black_empty)
                        edits += puzzle.rem([loc.south().east()], white_empty)

            return edits

    class KropkiDiamondWwwe:
        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for r in range(puzzle.grid_length):
                for c in range(puzzle.grid_length):
                    if r % 2 == 0 or c % 2 == 0:
                        continue

                    loc = Loc(r, c)

                    kropki_directions = [
                        loc.north(),
                        loc.east(),
                        loc.south(),
                        loc.west()
                    ]

                    all_our_valid = all([loc.is_valid_kropki(puzzle.grid_length) for loc in kropki_directions])

                    if not all_our_valid:
                        continue

                    empty_kropki = [loc for loc in kropki_directions if puzzle.is_empty(loc)]

                    white_kropki = [loc for loc in kropki_directions if puzzle.is_white(loc)]

                    if len(empty_kropki) != 1 or len(white_kropki) != 3:
                        continue

                    empty = empty_kropki[0]

                    if empty == loc.south():
                        edits += puzzle.rem([empty.west(), empty.east()], [3])
                        edits += puzzle.rem([empty.west().north(2), empty.east().north(2)], [1, 9])

                    if empty == loc.north():
                        edits += puzzle.rem([empty.west(), empty.east()], [3])
                        edits += puzzle.rem([empty.west().south(2), empty.east().south(2)], [1, 9])

                    if empty == loc.west():
                        edits += puzzle.rem([empty.north(), empty.south()], [3])
                        edits += puzzle.rem([empty.north().east(2), empty.south().east(2)], [1, 9])

                    if empty == loc.east():
                        edits += puzzle.rem([empty.north(), empty.south()], [3])
                        edits += puzzle.rem([empty.north().west(2), empty.south().west(2)], [1, 9])

            return edits

    class KropkiDominatingEmpty:

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for cell in puzzle.iterate_cells():
                directions = [
                    [cell.west(), cell.west(2)],
                    [cell.east(), cell.east(2)],
                    [cell.north(), cell.north(2)],
                    [cell.south(), cell.south(2)],
                ]
                for direction in directions:
                    if not puzzle.all_locs_are_valid(direction):
                        continue

                    kropki, other = direction

                    if not puzzle.is_empty(kropki):
                        continue

                    cell_candidates = puzzle.cell_candidates(cell)

                    # 1
                    if {1, 2}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [1, 2])

                    # 2
                    if {1, 2, 3, 4}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [2])

                    # 3
                    if {2, 3, 4, 6}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [3])

                    # 4
                    if {2, 3, 4, 5, 8}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [4])

                    # 5
                    if {4, 5, 6}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [5])

                    # 6
                    if {3, 5, 6, 7}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [6])

                    # 7
                    if {6, 7, 8}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [7])

                    # 8
                    if {4, 7, 8, 9}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [8])

                    # 9
                    if {8, 9}.issuperset(cell_candidates):
                        edits += puzzle.rem([other], [8, 9])

            return edits

    class KropkiEmpty:

        def solve0(self, puzzle: Kropki) -> int:
            # print("in here")
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r * 2, c * 2)
                    directions = [
                        [loc.north(), loc.north(2)],
                        [loc.south(), loc.south(2)],
                        [loc.east(), loc.east(2)],
                        [loc.west(), loc.west(2)],
                    ]
                    for direction in directions:
                        center, other = direction
                        if not center.is_valid_kropki(puzzle.grid_length):
                            continue

                        empty = [s == "." for s in puzzle.grid[center.row][center.col]]

                        if not all(empty):
                            continue

                        edits += self.solve1(puzzle, loc, other)
            return edits

        def solve1(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
            return self.solve2(puzzle, loc0, loc1) + self.solve2(puzzle, loc1, loc0)

        def solve2(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
            edits = 0

            loc0_candidates = puzzle.cell_candidates(loc0)

            if len(loc0_candidates) != 1:
                return edits

            candidate = loc0_candidates[0]

            candidates_to_remove = [candidate + 1, candidate - 1, candidate * 2, candidate]

            if candidate % 2 == 0:
                candidates_to_remove.append(int(candidate / 2))

            edits += puzzle.rem([loc1], candidates_to_remove)

            return edits

    class KropkiWhite:

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r * 2, c * 2)
                    directions = [
                        [loc.north(), loc.north(2)],
                        [loc.south(), loc.south(2)],
                        [loc.east(), loc.east(2)],
                        [loc.west(), loc.west(2)],
                    ]
                    for direction in directions:
                        center, other = direction
                        if not center.is_valid_kropki(puzzle.grid_length):
                            continue
                        if not puzzle.grid[center.row][center.col].replace(".", "", -1) == "WW":
                            continue
                        edits += self.solve1(puzzle, loc, other)
            return edits

        def solve1(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
            return self.solve2(puzzle, loc0, loc1) + self.solve2(puzzle, loc1, loc0)

        def solve2(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
            edits = 0
            other_candidates = set(puzzle.cell_candidates(loc1))
            for candidate in puzzle.cell_candidates(loc0):
                if candidate + 1 in other_candidates:
                    continue
                if candidate - 1 in other_candidates:
                    continue
                edits += puzzle.rem([loc0], [candidate])
            return edits

    class KropkiWw:

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class SumscrapersSecondInLine:

        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(len(puzzle)):
                house = puzzle.house_row(index)
                tuples.append((puzzle.west_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.east_scraper(index), house))
                house = puzzle.house_col(index)
                tuples.append((puzzle.north_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.south_scraper(index), house))

            for tuple0 in tuples:
                scraper, house = tuple0
                if scraper is None:
                    continue

                candidates1 = puzzle.cell_candidates(house[1])

                if len(candidates1) != 1:
                    continue
                if candidates1[0] != len(puzzle):
                    continue
                difference = scraper - len(puzzle)

                edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([difference]))

                print(scraper)
                print(house)
            return edits

    class CrossHatchSumscrapers:
        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0
            houses = []
            for index in range(len(puzzle)):
                houses.append(puzzle.house_row(index))
                houses.append(puzzle.house_col(index))
            for house in houses:
                for index0 in range(len(house)):
                    for index1 in range(len(house)):
                        if index0 == index1:
                            continue
                        loc0 = house[index0]
                        loc1 = house[index1]
                        candidates0 = puzzle.cell_candidates(loc0)
                        if len(candidates0) == 1:
                            edits += puzzle.rem([loc1], [candidates0[0]])
            return edits

    class HiddenSingleSumscrapers:
        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0
            houses = []
            for index in range(len(puzzle)):
                houses.append(puzzle.house_row(index))
                houses.append(puzzle.house_col(index))

            for house in houses:
                candidate_dict = {}
                for index in range(len(puzzle)):
                    for candidate in puzzle.cell_candidates(house[index]):
                        if candidate not in candidate_dict:
                            candidate_dict[candidate] = []
                        candidate_dict[candidate].append(house[index])
                for candidate in candidate_dict.keys():
                    locs = candidate_dict[candidate]

                    if len(locs) == 1:
                        edits += puzzle.rem(candidate_dict[candidate],
                                            set(puzzle.expected_candidates()).difference([candidate]))

            return edits

    class SumscrapersLastIsMax:

        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(len(puzzle)):
                house = puzzle.house_row(index)
                tuples.append((puzzle.west_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.east_scraper(index), house))
                house = puzzle.house_col(index)
                tuples.append((puzzle.north_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.south_scraper(index), house))

            for tuple0 in tuples:
                scraper, house = tuple0
                if scraper is None:
                    continue

                candidates_n = puzzle.cell_candidates(house[len(puzzle) - 1])

                if len(candidates_n) != 1:
                    continue
                if candidates_n[0] != len(puzzle):
                    continue

                difference = scraper - len(puzzle)

                expected = set(puzzle.expected_candidates())

                expected.remove(len(puzzle))

                max0 = max(expected)

                if scraper == max0 + len(puzzle):
                    edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([max0]))
                else:
                    edits += puzzle.rem([house[0]], [max0])
                # print(scraper)
                # print(house)
            return edits

    class SumscrapersNextToScraper:

        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(len(puzzle)):
                house = puzzle.house_row(index)
                tuples.append((puzzle.west_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.east_scraper(index), house))
                house = puzzle.house_col(index)
                tuples.append((puzzle.north_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.south_scraper(index), house))

            for tuple0 in tuples:
                scraper, house = tuple0
                if scraper is None:
                    continue

                if scraper > len(puzzle):
                    edits += puzzle.rem([house[0]], [len(puzzle)])

            return edits

    class SumscrapersTech:
        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            for index in range(len(puzzle)):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == len(puzzle):
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference([len(puzzle)]))

                if south == len(puzzle):
                    edits += puzzle.rem([Loc(len(puzzle) - 1, index)],
                                        set(puzzle.expected_candidates()).difference([len(puzzle)]))

                if east == len(puzzle):
                    edits += puzzle.rem([Loc(index, len(puzzle) - 1)],
                                        set(puzzle.expected_candidates()).difference([len(puzzle)]))
                #
                if west == len(puzzle):
                    edits += puzzle.rem([Loc(index, 0)],
                                        set(puzzle.expected_candidates()).difference([len(puzzle)]))

                total = sum(puzzle.expected_candidates())

                if south == total:
                    expected = set(puzzle.expected_candidates())
                    current = Loc(len(puzzle) - 1, index)
                    while len(expected) > 0:
                        min0 = min(expected)
                        edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                        expected.remove(min0)
                        current = current.north()

                # if north == total:
                #     expected = set(puzzle.expected_candidates())
                #     current = Loc(0, index)
                #     while len(expected) > 0:
                #         min0 = min(expected)
                #         edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                #         expected.remove(min0)
                #         current = current.south()

                if east == total:
                    expected = set(puzzle.expected_candidates())
                    current = Loc(0, len(puzzle) - 1)
                    while len(expected) > 0:
                        min0 = min(expected)
                        # print(min0)
                        edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                        expected.remove(min0)
                        current = current.west()

            return edits

    class Parks1Bent3:

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fence_dict = {}
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    fence = puzzle.cell_fence(loc)
                    if fence not in fence_dict:
                        fence_dict[fence] = []
                    fence_dict[fence].append(loc)

            for fence in fence_dict.keys():
                fence_locs = fence_dict[fence]
                solved_empty = [loc for loc in fence_locs if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree = [loc for loc in fence_locs if
                               len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved = set(fence_locs).difference(solved_tree + solved_empty)
                if len(solved_tree) == 1:
                    continue

                if len(unsolved) != 3:
                    continue

                rows = set([loc.row for loc in unsolved])
                cols = set([loc.col for loc in unsolved])

                if len(rows) == 1 or len(cols) == 1:
                    continue

                for pivot in unsolved:
                    pincers = set(unsolved).difference([pivot])

                    all_next_to = [loc.is_next_to(pivot) for loc in pincers]

                    if not all(all_next_to):
                        continue

                    # south-east
                    if unsolved.issuperset([pivot.east(), pivot.south()]):
                        remove = [pivot.south().east()]

                        if pivot.north().is_valid_parks(puzzle.grid):
                            remove.append(pivot.north())

                        edits += puzzle.rem(remove, [1])

            return edits

    class Parks1CrossHatch:

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            houses = []
            fence_dict = {}
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    fence = puzzle.cell_fence(loc)

                    if fence not in fence_dict:
                        fence_dict[fence] = []

                    fence_dict[fence].append(loc)

            for fence in fence_dict.keys():
                houses.append(fence_dict[fence])

            for row in range(len(puzzle)):
                house = []
                for col in range(len(puzzle)):
                    house.append(Loc(row, col))
                houses.append(house)
            for col in range(len(puzzle)):
                house = []
                for row in range(len(puzzle)):
                    house.append(Loc(row, col))
                houses.append(house)
            for house in houses:
                for i in range(len(house)):
                    for ii in range(len(house)):
                        if i == ii:
                            continue
                        candidates0 = puzzle.cell_candidates(house[i])
                        if len(candidates0) == 1 and candidates0[0] == 1:
                            edits += puzzle.rem([house[ii]], [1])
            return edits

    class Parks1CrossHatchTouching:

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)

                    candidates = puzzle.cell_candidates(loc)

                    if len(candidates) != 1 or candidates[0] != 1:
                        continue

                    directions = [
                        loc.north().west(),
                        loc.north().east(),
                        loc.south().west(),
                        loc.south().east(),
                    ]

                    for direction in directions:
                        if direction.is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([direction], [1])

            return edits

    class Parks1DominateFence:
        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            for fence in puzzle.fences():
                fence_locs = puzzle.house_fence(fence)
                surrounding_cells = set()

                solved_empty = [loc for loc in fence_locs if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree = [loc for loc in fence_locs if
                               len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved = list(set(fence_locs).difference(solved_tree + solved_empty))

                if len(solved_tree) == 1:
                    continue

                for loc in unsolved:
                    # from Techniques import Techs
                    for surrounding in puzzle.surrounding(loc):
                        if fence == puzzle.cell_fence(surrounding):
                            continue
                        surrounding_cells.add(surrounding)
                for edge_cell in surrounding_cells:
                    candidates = puzzle.cell_candidates(edge_cell)
                    if len(candidates) == 1 and 1 in candidates:
                        continue
                    fence_house = set(unsolved)
                    while len(fence_house) > 0:
                        first = list(fence_house)[0]
                        if edge_cell.row == first.row or edge_cell.col == first.col:
                            fence_house.remove(first)
                            continue
                        # from Techniques import Techs
                        if first in puzzle.surrounding(edge_cell):
                            fence_house.remove(first)
                            continue
                        break
                    if len(fence_house) == 0:
                        edits += puzzle.rem([edge_cell], [1])
            return edits

    # class Parks1DominateFenceAgain:
    #     def solve0(self, puzzle: Parks1) -> int:
    #         edits = 0
    #         for fence in puzzle.fences():
    #             if fence != 'b':
    #                 continue
    #             house = puzzle.house_fence(fence)
    #             print(house)
    #
    #             # surrounding_cells = set()
    #             # for loc in house:
    #             #     # from Techniques import Techs
    #             #     for surrounding in puzzle.surrounding( loc):
    #             #         if fence == puzzle.cell_fence(surrounding):
    #             #             continue
    #             #         surrounding_cells.add(surrounding)
    #             # for edge_cell in surrounding_cells:
    #             #     candidates = puzzle.cell_candidates(edge_cell)
    #             #     if len(candidates) == 1 and 1 in candidates:
    #             #         continue
    #             #     fence_house = set(house)
    #             #     while len(fence_house) > 0:
    #             #         first = list(fence_house)[0]
    #             #         if edge_cell.row == first.row or edge_cell.col == first.col:
    #             #             fence_house.remove(first)
    #             #             continue
    #             #         # from Techniques import Techs
    #             #         if first in puzzle.surrounding( edge_cell):
    #             #             fence_house.remove(first)
    #             #             continue
    #             #         break
    #             #     if len(fence_house) == 0:
    #             #         edits += puzzle.rem([edge_cell], [1])
    #         return edits

    class Parks1HiddenSingle:
        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fence_dict = {}
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    fence = puzzle.cell_fence(loc)
                    if fence not in fence_dict:
                        fence_dict[fence] = []
                    fence_dict[fence].append(loc)
            for fence in fence_dict.keys():
                fence_locs = fence_dict[fence]
                solved_empty = [loc for loc in fence_locs if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree = [loc for loc in fence_locs if
                               len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved = list(set(fence_locs).difference(solved_tree + solved_empty))
                if len(solved_tree) == 1:
                    continue
                if len(unsolved) == 1:
                    edits += puzzle.rem(unsolved, [0])
            return edits

    class Parks1LockedCandidatesClaiming:

        def solve1(self, puzzle: Parks1, row_col_house: list[Loc]) -> int:
            edits = 0

            solved_empty = [loc for loc in row_col_house if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in row_col_house if
                           len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
            unsolved = list(set(row_col_house).difference(solved_tree + solved_empty))

            if len(solved_tree) == 1:
                return edits

            fence = puzzle.cell_fence(unsolved[0])

            if not all(fence == puzzle.cell_fence(loc) for loc in unsolved):
                return edits

            fence_locs = set(puzzle.house_fence(fence))

            locs_to_remove = list(fence_locs.difference(unsolved))

            return puzzle.rem(locs_to_remove, [1])

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0

            for index in range(len(puzzle)):
                edits += self.solve1(puzzle, puzzle.house_row(index)) + self.solve1(puzzle, puzzle.house_col(index))

            return edits

    class Parks1LockedCandidatesPointing:

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fence_dict = {}

            # for house in puzzle.
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    fence = puzzle.cell_fence(loc)
                    if fence not in fence_dict:
                        fence_dict[fence] = []
                    fence_dict[fence].append(loc)

            for fence in fence_dict.keys():
                fence_locs = fence_dict[fence]
                solved_empty = [loc for loc in fence_locs if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree = [loc for loc in fence_locs if
                               len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved = list(set(fence_locs).difference(solved_tree + solved_empty))
                if len(solved_tree) == 1:
                    continue
                if len(unsolved) >= 2:
                    rows = set([loc.row for loc in unsolved])
                    cols = set([loc.col for loc in unsolved])
                    if len(rows) == 1:
                        temp = set(puzzle.house_row(rows.pop())).difference(unsolved)
                        edits += puzzle.rem(list(temp), [1])
                    if len(cols) == 1:
                        temp = set(puzzle.house_col(cols.pop())).difference(unsolved)
                        edits += puzzle.rem(list(temp), [1])
            return edits

    class Parks1Shape_00_01:

        def shape_w_south_east(self, center: Loc) -> tuple[list[Loc], list[Loc]]:
            return ([
                        center.north(),
                        center.north().east(),
                        center,
                        center.west(),
                        center.west().south(),
                    ], [center.north().west()])

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0

            for house in puzzle.houses_rows() + puzzle.houses_cols():
                solved_empty = [loc for loc in house if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree = [loc for loc in house if
                               len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved = list(set(house).difference(solved_tree + solved_empty))
                if len(solved_tree) == 1:
                    continue
                if len(unsolved) == 2:
                    loc0, loc1 = unsolved
                    if loc0.is_next_to(loc1):
                        if loc0.col == loc1.col:
                            if loc0.east().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc0.east()], [1])
                            if loc0.west().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc0.west()], [1])
                            if loc1.east().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc1.east()], [1])
                            if loc1.west().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc1.west()], [1])

                        if loc0.row == loc1.row:
                            if loc0.north().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc0.north()], [1])
                            if loc0.south().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc0.south()], [1])
                            if loc1.north().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc1.north()], [1])
                            if loc1.south().is_valid_parks(puzzle.grid):
                                edits += puzzle.rem([loc1.south()], [1])

                    # print(unsolved)

            # for fence in puzzle.fences():
            #     house = set(puzzle.house_fence(fence))
            #     solved_parks = [loc for loc in house if puzzle.is_cell_solved(loc, 1)]
            #     if len(solved_parks) > 1:
            #         raise Exception("Found a park fence that is solved with more than one fence")
            #     if len(solved_parks) == 1:
            #         continue
            #     unsolved = [loc for loc in house if puzzle.is_cell_solved(loc, 1)]

            return edits

    class Parks1Shapes:
        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            # for fence in puzzle.fences():
            #     house = puzzle.house_fence(fence)
            #
            #     solved_parks1 = []
            #
            #     unsolved = []
            #
            #     for loc in house:
            #         candidates = puzzle.cell_candidates(loc)
            #         if len(candidates) == 2:
            #             unsolved.append(loc)
            #             continue
            #         if 1 in candidates:
            #             solved_parks1.append(loc)
            #
            #     if len(solved_parks1) == 1:
            #         continue
            #
            #     temp = puzzle.surrounding( unsolved[0])
            #
            #     surrounding = set(temp)
            #
            #     rows = set(puzzle.house_row(unsolved[0].row))
            #
            #     cols = set(puzzle.house_col(unsolved[0].col))
            #
            #     for index in range(1, len(unsolved)):
            #         surrounding = surrounding.intersection(puzzle.surrounding( unsolved[index]))
            #
            #         rows = rows.intersection(puzzle.house_row(unsolved[index].row))
            #
            #         cols = cols.intersection(puzzle.house_col(unsolved[index].col))
            #
            #     surrounding = surrounding.difference(unsolved)
            #     rows = rows.difference(unsolved)
            #     cols = cols.difference(unsolved)
            #
            #     edits += puzzle.rem(surrounding, [1])
            #     edits += puzzle.rem(rows, [1])
            #     edits += puzzle.rem(cols, [1])

            return edits

    class Parks1FenceWing:

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fences = list(puzzle.fences())
            for fence0 in range(0, len(fences) - 1):
                if fences[fence0] != 'a':
                    continue

                fence_locs0 = puzzle.house_fence(fences[fence0])
                solved_empty0 = [loc for loc in fence_locs0 if
                                 len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree0 = [loc for loc in fence_locs0 if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved0 = list(set(fence_locs0).difference(solved_tree0 + solved_empty0))
                if len(solved_tree0) == 1:
                    continue
                for fence1 in range(1, len(fences)):
                    if fences[fence1] != 'c':
                        continue
                    fence_locs1 = puzzle.house_fence(fences[fence1])
                    solved_empty1 = [loc for loc in fence_locs1 if
                                     len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                    solved_tree1 = [loc for loc in fence_locs1 if
                                    len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                    unsolved1 = list(set(fence_locs1).difference(solved_tree1 + solved_empty1))
                    if len(solved_tree1) == 1:
                        continue
                    edits += self.solve1(puzzle, unsolved0, unsolved1)
            return edits

        def solve1(self, puzzle: Parks1, unsolved0: list[Loc], unsolved1: list[Loc]) -> int:
            edits = 0
            row_set0 = set([loc.row for loc in unsolved0])
            col_set0 = set([loc.col for loc in unsolved0])
            row_set1 = set([loc.row for loc in unsolved1])
            col_set1 = set([loc.col for loc in unsolved1])

            if col_set0 == col_set1:
                print("fence set cols")

            if row_set0 == row_set1:
                row_locs = []
                for row in row_set0:
                    row_locs = row_locs + puzzle.house_row(row)
                locs_to_remove = set(row_locs).difference(unsolved0 + unsolved1)
                edits += puzzle.rem(locs_to_remove, [1])
            return edits

    class Parks1XWing:

        def solve_two_cell(self, puzzle: Parks1, cell0: Loc, cell1: Loc, candidate: int) -> int:
            edits = 0
            # edits = Parks1FenceWing().solve0(puzzle)

            if cell0.row == cell1.row:
                for row in set(range(len(puzzle))).difference([cell0.row]):
                    other0 = Loc(row, cell0.col)
                    other1 = Loc(row, cell1.col)
                    corners = [cell0, cell1, other0, other1]
                    other_candidates0 = puzzle.cell_candidates(other0)
                    other_candidates1 = puzzle.cell_candidates(other1)
                    if len(other_candidates0) == 1 or \
                            len(other_candidates1) == 1 or \
                            candidate not in other_candidates0 or \
                            candidate not in other_candidates1:
                        continue
                    other_row_house = puzzle.house_row(other0.row, candidate)
                    if len(other_row_house) != 2:
                        continue
                    if {other0, other1} != set(other_row_house):
                        continue
                    locs_to_remove_from = set(puzzle.house_col(other0.col) + puzzle.house_col(other1.col)).difference(
                        corners)
                    edits += puzzle.rem(locs_to_remove_from, [candidate])

            if cell0.col == cell1.col:
                for col in set(range(len(puzzle))).difference([cell0.col]):
                    other0 = Loc(cell0.row, col)
                    other1 = Loc(cell1.row, col)
                    corners = [cell0, cell1, other0, other1]
                    other_candidates0 = puzzle.cell_candidates(other0)
                    other_candidates1 = puzzle.cell_candidates(other1)
                    if len(other_candidates0) == 1 or \
                            len(other_candidates1) == 1 or \
                            candidate not in other_candidates0 or \
                            candidate not in other_candidates1:
                        continue
                    other_col_house = puzzle.house_col(other0.col, candidate)
                    if len(other_col_house) != 2:
                        continue
                    if {other0, other1} != set(other_col_house):
                        continue
                    locs_to_remove_from = set(puzzle.house_row(other0.row) + puzzle.house_row(other1.row)).difference(
                        corners)
                    edits += puzzle.rem(locs_to_remove_from, [candidate])

            return edits

        def solve_one_cell(self, puzzle: Parks1, cell0: Loc, candidate: int) -> int:

            edits = 0
            # need to find the next cell to form a base

            row_cells = set(puzzle.house_row(cell0.row, candidate))
            col_cells = set(puzzle.house_col(cell0.col, candidate))

            if len(row_cells) == 2:
                row_cells.remove(cell0)
                edits += self.solve_two_cell(puzzle, cell0, row_cells.pop(), candidate)

            if len(col_cells) == 2:
                col_cells.remove(cell0)
                edits += self.solve_two_cell(puzzle, cell0, col_cells.pop(), candidate)

            return edits

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            # print("heresssss")
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)

                    if puzzle.is_cell_solved(loc):
                        continue

                    for candidate in [1]:
                        edits += self.solve_one_cell(puzzle, loc, candidate)
            return edits
