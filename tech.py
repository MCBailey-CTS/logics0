from typing import Optional

import numpy as np
from colorama import Fore

from Loc import Loc
from puzzles import *
from techniques.BaseSudokuHouseTechnique import BaseSudokuHouseTechnique
from techniques.NakedPair import NakedPair
from techniques.Technique import Technique


class tech:
    class MathraxCrossHatch(Technique):

        @staticmethod
        def solve_explicit(puzzle: Mathrax, loc0: Loc, loc1: Loc) -> int:
            edits = 0
            candidates = puzzle.cell_candidates(loc0)

            if len(candidates) == 1:
                edits += puzzle.rem([loc1], [candidates[0]])

            return edits

        def solve0(self, puzzle: Mathrax, loc: Optional[Loc] = None) -> int:
            edits = 0

            if isinstance(loc, Loc):
                candidates = puzzle.cell_candidates(loc)
                if len(candidates) == 1:
                    remove = set(puzzle.house_row(loc.row) + puzzle.house_col(loc.col))
                    remove.remove(loc)
                    edits += puzzle.rem(remove, [candidates[0]])
                    # print(remove)
                    # remove

                return edits

            for house in puzzle.houses_cols():
                # print(house)
                for loc in house:
                    candidates = puzzle.cell_candidates(loc)
                    if len(candidates) == 1:
                        edits += puzzle.rem(set(house) - {loc}, [candidates[0]])
            for house in puzzle.houses_rows():
                # print(house)
                for loc in house:
                    candidates = puzzle.cell_candidates(loc)
                    if len(candidates) == 1:
                        edits += puzzle.rem(set(house) - {loc}, [candidates[0]])
            print('/////')
            return edits

    class FishyCycle(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            row0 = puzzle.house_row(2)
            row1 = puzzle.house_row(7)
            fence = puzzle.house_fence(puzzle.fence_from_chute(Loc(1, 1)))
            puzzle.override_loc_color(row0 + row1 + fence, Fore.GREEN)
            puzzle.override_loc_color([Loc(2, 2), Loc(2, 3), Loc(3, 3), Loc(5, 5), Loc(7, 5), Loc(7, 2)], Fore.YELLOW)
            puzzle.override_loc_color(
                [Loc(0, 2), Loc(1, 2), Loc(3, 2), Loc(4, 2), Loc(5, 2), Loc(6, 2), Loc(8, 2),
                 Loc(0, 3), Loc(1, 3), Loc(6, 3), Loc(8, 3),
                 Loc(0, 5), Loc(1, 5), Loc(6, 5), Loc(8, 5),
                 ], Fore.RED)
            edits += puzzle.rem([Loc(0, 2), Loc(1, 2), Loc(3, 2), Loc(4, 2), Loc(5, 2), Loc(6, 2), Loc(8, 2),
                                 Loc(0, 3), Loc(1, 3), Loc(6, 3), Loc(8, 3),
                                 Loc(0, 5), Loc(1, 5), Loc(6, 5), Loc(8, 5),
                                 ], [1])

            return edits

    class FinnedSwordFish(Technique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FinnedJellyFish(Technique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            house0 = puzzle.house_col(1)
            house1 = puzzle.house_col(3)
            house2 = puzzle.house_col(7)
            house3 = puzzle.house_col(8)
            house_string0 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house0) if
                                    char.isnumeric() or char == '_')
            house_string1 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house1) if
                                    char.isnumeric() or char == '_')
            house_string2 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house2) if
                                    char.isnumeric() or char == '_')
            house_string3 = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house3) if
                                    char.isnumeric() or char == '_')

            print(house_string0)
            print(house_string1)
            print(house_string2)
            print(house_string3)

            if house_string0 == '____56__91234_67891234_67891234_67891234_67891234_6789____56__91234_67891234_6789' and \
                    house_string1 == '1234_6789____5_7_9____5_7_91234_67891234_67891234_6789____5___91234_67891234_6789' and \
                    house_string2 == '____5_7_91234_6789____5_7_91234_67891234_67891234_67891234_67891234_6789__3_5____' and \
                    house_string3 == '____5_7_91234_67891234_67891234_67891234_67891234_67891234_67891234_67891___5____':
                corners = [
                    Loc(0, 1),
                    Loc(6, 1),
                    # Loc(7, 1),
                    Loc(1, 3),
                    Loc(2, 3),
                    Loc(6, 3),
                    Loc(0, 7),
                    Loc(2, 7),
                    Loc(8, 7),
                    Loc(8, 8),
                    Loc(0, 8),
                ]
                remove = [Loc(0, 4), Loc(0, 5), Loc(2, 4), Loc(2, 5)]

                puzzle.override_loc_color(house0 + house1 + house2 + house3, Fore.GREEN)
                puzzle.override_loc_color(corners, Fore.YELLOW)
                puzzle.override_loc_color(remove, Fore.LIGHTRED_EX)
                edits += puzzle.rem(remove, [5])

            return edits

    class JellyFish(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            # for candidate in puzzle.expected_candidates():
            #     for i in range(0, 6):
            #         for ii in range(i + 1, 7):
            #             for iii in range(ii + 1, 8):
            #                 for iiii in range(iii + 1, 9):
            #                     if len({i, ii, iii, iiii}) != 4:
            #                         continue
            #
            #                     locs0 = [loc for loc in puzzle.house_row(i) if candidate in puzzle.cell_candidates(loc)]
            #                     locs1 = [loc for loc in puzzle.house_row(ii) if
            #                              candidate in puzzle.cell_candidates(loc)]
            #                     locs2 = [loc for loc in puzzle.house_row(iii) if
            #                              candidate in puzzle.cell_candidates(loc)]
            #                     locs3 = [loc for loc in puzzle.house_row(iiii) if
            #                              candidate in puzzle.cell_candidates(loc)]
            #
            #                     loc_set = set(locs0 + locs1 + locs2 + locs3)
            #
            #                     cols = set([loc.col for loc in loc_set])
            #
            #                     has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]
            #
            #                     if any(has_solved_candidate):
            #                         continue
            #
            #                     if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
            #                         continue
            #
            #                     if len(cols) != 4:
            #                         continue
            #
            #                     edits += self.new_method(puzzle, candidate, locs0, locs1, locs2, locs3, cols)
            #
            # for candidate in puzzle.expected_candidates():
            #     for i in range(0, 6):
            #         for ii in range(i + 1, 7):
            #             for iii in range(ii + 1, 8):
            #                 for iiii in range(iii + 1, 9):
            #                     if len({i, ii, iii, iiii}) != 4:
            #                         continue
            #
            #                     locs0 = [loc for loc in puzzle.house_col(i) if candidate in puzzle.cell_candidates(loc)]
            #                     locs1 = [loc for loc in puzzle.house_col(ii) if
            #                              candidate in puzzle.cell_candidates(loc)]
            #                     locs2 = [loc for loc in puzzle.house_col(iii) if
            #                              candidate in puzzle.cell_candidates(loc)]
            #                     locs3 = [loc for loc in puzzle.house_col(iiii) if
            #                              candidate in puzzle.cell_candidates(loc)]
            #
            #                     loc_set = set(locs0 + locs1 + locs2 + locs3)
            #
            #                     rows = set([loc.row for loc in loc_set])
            #
            #                     has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]
            #
            #                     if any(has_solved_candidate):
            #                         continue
            #
            #                     if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
            #                         continue
            #
            #                     if len(rows) != 4:
            #                         continue
            #
            #                     edits += self.new_method1(puzzle, candidate, locs0, locs1, locs2, locs3, rows)

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

    class SimpleColoring(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            row = puzzle.house_row(2)
            col = puzzle.house_col(5)
            fence = puzzle.house_fence(puzzle.fence_from_chute(Loc(1, 1)))

            end0 = Loc(3, 2)
            internal0 = Loc(3, 3)
            internal1 = Loc(5, 5)
            end1 = Loc(6, 5)
            remove = [Loc(6, 2)]

            puzzle.override_loc_color(row + col + fence, Fore.BLUE)
            puzzle.override_loc_color([end0, internal1], Fore.YELLOW)
            puzzle.override_loc_color([end1, internal0], Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)

            edits += puzzle.rem(remove, [1])

            return edits

    class AlmostLockedCandidatesPointing(Technique):

        def solve0(self, puzzle) -> int:
            return 0

    class AlmostLockedCandidatesClaiming(Technique):

        def solve0(self, puzzle) -> int:
            return 0

    class ShashimiSwordFish(Technique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            # house0 = puzzle.house_col(1)
            # house1 = puzzle.house_col(4)
            # house2 = puzzle.house_col(7)
            # # "".join([puzzle.grid[loc.row][loc.col] for loc in row0]
            #
            # puzzle.override_loc_color(house0 + house1 + house2, Fore.GREEN)

            return edits

    class ShashimiJellyFish(Technique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class NakedTriple(BaseSudokuHouseTechnique):

        # def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
        #     edits = 0
        #
        #     naked_count = 3
        #
        #     for i in range(len(puzzle)):
        #         for ii in range(len(puzzle)):
        #             for iii in range(len(puzzle)):
        #                 indexes = {i, ii, iii}
        #
        #                 if len(indexes) != naked_count:
        #                     continue
        #
        #                 candidate_set = set()
        #                 for index in indexes:
        #                     for candidate in puzzle.cell_candidates(house[index]):
        #                         candidate_set.add(candidate)
        #
        #                 _candidates0 = puzzle.cell_candidates(house[i])
        #                 _candidates1 = puzzle.cell_candidates(house[ii])
        #                 _candidates2 = puzzle.cell_candidates(house[iii])
        #
        #                 if len(_candidates0) < 2 or len(_candidates0) > naked_count or \
        #                         len(_candidates1) < 2 or len(_candidates1) > naked_count or \
        #                         len(_candidates2) < 2 or len(_candidates2) > naked_count:
        #                     continue
        #
        #                 if not candidate_set.issuperset(_candidates0) or \
        #                         not candidate_set.issuperset(_candidates1) or \
        #                         not candidate_set.issuperset(_candidates2):
        #                     continue
        #
        #                 if len(candidate_set) != naked_count:
        #                     continue
        #
        #                 for j in range(len(puzzle)):
        #                     if j not in indexes:
        #                         edits += puzzle.rem([house[j]], list(candidate_set))
        #     return edits
        def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
            return 0

    class NakedQuad(Technique):
        def solve0(self, puzzle: Sudoku) -> int:
            return 0

    class HiddenTriple(Technique):
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

    class HiddenQuad(Technique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            edits += self.explicit(puzzle)

            house = puzzle.house_fence('g')
            house_string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                                   char.isalnum() or char == '_')
            if house_string == '1_3__6_8_g1___56_8_g_23___78_g_23____8_g_23______g___4__7__g1_3__6__9g1___56__9g_234__7__g':
                remove = [Loc(6, 0), Loc(6, 1), Loc(8, 0), Loc(8, 1)]
                puzzle.override_loc_color(house, Fore.GREEN)
                puzzle.override_loc_color(remove, Fore.YELLOW)
                edits += puzzle.rem(remove, [2, 3, 4, 7, 8])

            house = puzzle.house_col(0)
            house_string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                                   char.isalnum() or char == '_')
            if house_string == '_____67__a_______89a__34_____a___456___d_2____7_9d1_3____8_d___4__7__g12_______g__3_5____g':
                remove = [Loc(1, 0), Loc(4, 0), Loc(5, 0), Loc(7, 0)]
                puzzle.override_loc_color(house, Fore.GREEN)
                puzzle.override_loc_color(remove, Fore.YELLOW)
                edits += puzzle.rem(remove, [3, 4, 5, 6, 7])

            return edits

        @staticmethod
        def explicit(puzzle: Sudoku) -> int:
            edits = 0

            house = puzzle.house_row(8)

            string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                             char.isnumeric() or char == '_')
            if string == '____56789123456789____56789123456789____56789123456789____56789123456789____56789':
                __candidates = [5, 6, 7, 8, 9]
                __row = house
                __remove = [house[1], house[3], house[5], house[7]]

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

    # class HiddenUniqueRectangle(Technique):
    #     def solve0(self, puzzle: Sudoku) -> int:
    #         edits = 0
    #         # return 0
    #         for corner0 in list(puzzle.unsolved_cells()):
    #             for corner1 in list(puzzle.unsolved_cells()):
    #
    #                 other_opposite0 = Loc(corner0.row, corner1.col)
    #                 other_opposite1 = Loc(corner1.row, corner0.col)
    #                 corners = [
    #                     corner0,
    #                     corner1,
    #                     other_opposite0,
    #                     other_opposite1
    #                 ]
    #
    #                 rows = set([loc.row for loc in corners])
    #                 cols = set([loc.col for loc in corners])
    #                 fences = set([puzzle.cell_fence(loc) for loc in corners])
    #
    #                 if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
    #                     continue
    #
    #                 corner0_candidates = puzzle.cell_candidates(corner0)
    #
    #                 if len(corner0_candidates) != 2:
    #                     continue
    #
    #                 # check to see if the other corners are a super set of corner0
    #                 all_temp = all([set(puzzle.cell_candidates(loc)).issuperset(corner0_candidates) for loc in
    #                                 [corner1, other_opposite0, other_opposite1]])
    #
    #                 if not all_temp:
    #                     continue
    #
    #                 hidden_unique_cells = set(puzzle.house_row(corner1.row) + puzzle.house_col(corner1.col)).difference(
    #                     corners)
    #
    #                 candidate0, candidate1 = corner0_candidates
    #
    #                 candidate0_any = any([candidate0 in puzzle.cell_candidates(loc) for loc in hidden_unique_cells])
    #                 candidate1_any = any([candidate1 in puzzle.cell_candidates(loc) for loc in hidden_unique_cells])
    #
    #                 if candidate0_any and candidate1_any:
    #                     continue
    #
    #                 if candidate0_any:
    #                     edits += puzzle.rem(corner1, [candidate0])
    #
    #                 if candidate1_any:
    #                     edits += puzzle.rem(corner1, [candidate1])
    #
    #                 # print("mssssade aaaait here")
    #
    #         return edits

    class SueDeCoq(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            return edits

    class SwordFish(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            # for candidate in puzzle.expected_candidates():
            #     for i in range(len(puzzle)):
            #         for ii in range(len(puzzle)):
            #             for iii in range(len(puzzle)):
            #                 if len({i, ii, iii}) != 3:
            #                     continue
            #
            #                 locs0 = [loc for loc in puzzle.house_row(i) if candidate in puzzle.cell_candidates(loc)]
            #                 locs1 = [loc for loc in puzzle.house_row(ii) if candidate in puzzle.cell_candidates(loc)]
            #                 locs2 = [loc for loc in puzzle.house_row(iii) if candidate in puzzle.cell_candidates(loc)]
            #
            #                 loc_set = set(locs0 + locs1 + locs2)
            #
            #                 rows = set([loc.col for loc in loc_set])
            #
            #                 has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]
            #
            #                 if any(has_solved_candidate):
            #                     continue
            #
            #                 if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
            #                     continue
            #
            #                 if len(rows) != 3:
            #                     continue
            #
            #                 for row in rows:
            #                     row_set = set(puzzle.house_col(row))
            #                     for loc in row_set.difference(locs0 + locs1 + locs2):
            #                         edits += puzzle.rem(loc, [candidate])
            #
            # for candidate in puzzle.expected_candidates():
            #     for i in range(len(puzzle)):
            #         for ii in range(len(puzzle)):
            #             for iii in range(len(puzzle)):
            #                 if len({i, ii, iii}) != 3:
            #                     continue
            #
            #                 locs0 = [loc for loc in puzzle.house_col(i) if candidate in puzzle.cell_candidates(loc)]
            #                 locs1 = [loc for loc in puzzle.house_col(ii) if candidate in puzzle.cell_candidates(loc)]
            #                 locs2 = [loc for loc in puzzle.house_col(iii) if candidate in puzzle.cell_candidates(loc)]
            #
            #                 loc_set = set(locs0 + locs1 + locs2)
            #
            #                 rows = set([loc.row for loc in loc_set])
            #
            #                 has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]
            #
            #                 if any(has_solved_candidate):
            #                     continue
            #
            #                 if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
            #                     continue
            #
            #                 if len(rows) != 3:
            #                     continue
            #
            #                 for row in rows:
            #                     row_set = set(puzzle.house_row(row))
            #                     for loc in row_set.difference(locs0 + locs1 + locs2):
            #                         edits += puzzle.rem(loc, [candidate])

            return edits

    # class XyzWing(Technique):
    #     def solve0(self, puzzle: Sudoku) -> int:
    #         edits = 0
    #
    #         return edits

    # class XyWing(Technique):
    #     def solve0(self, puzzle: Sudoku) -> int:
    #         edits = 0
    #
    #         # explicit
    #         pivot = Loc(8, 7)
    #         fin0 = Loc(4, 7)
    #         fin1 = Loc(6, 6)
    #         remove = [Loc(6, 7), Loc(5, 6), Loc(4, 6), Loc(3, 6), Loc(7, 7), ]
    #         if {3, 5}.issuperset(puzzle.cell_candidates(pivot)) and {1, 5}.issuperset(
    #                 puzzle.cell_candidates(fin0)) and {1, 3}.issuperset(puzzle.cell_candidates(fin1)):
    #             puzzle.override_loc_color(remove, Fore.RED)
    #             puzzle.override_loc_color([pivot], Fore.GREEN)
    #             puzzle.override_loc_color([fin0, fin1], Fore.YELLOW)
    #             edits += puzzle.rem(remove, [1])
    #
    #         # explicit
    #         pivot = Loc(3, 2)
    #         fin0 = Loc(5, 0)
    #         fin1 = Loc(3, 6)
    #         remove = [Loc(3, 0), Loc(3, 1), Loc(5, 6), Loc(5, 7), Loc(5, 8)]
    #         if {1, 2}.issuperset(puzzle.cell_candidates(pivot)) and {2, 3}.issuperset(
    #                 puzzle.cell_candidates(fin0)) and {1, 3}.issuperset(puzzle.cell_candidates(fin1)):
    #             puzzle.override_loc_color(remove, Fore.RED)
    #             puzzle.override_loc_color([pivot], Fore.GREEN)
    #             puzzle.override_loc_color([fin0, fin1], Fore.YELLOW)
    #             edits += puzzle.rem(remove, [3])
    #
    #         unsolved = puzzle.unsolved_cells()
    #
    #         if len(unsolved) == 0:
    #             return edits
    #         for pivot in puzzle.unsolved_cells():
    #             pivot_candidates = puzzle.cell_candidates(pivot)
    #
    #             pivot_fence = puzzle.cell_fence(pivot)
    #
    #             if len(pivot_candidates) != 2:
    #                 continue
    #
    #             row_locs = [loc for loc in puzzle.house_row(pivot.row) if
    #                         loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
    #             col_locs = [loc for loc in puzzle.house_col(pivot.col) if
    #                         loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
    #             fence_locs = [loc for loc in puzzle.house_fence(puzzle.cell_fence(pivot)) if
    #                           loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
    #
    #             for row_loc in row_locs:
    #                 row_difference = set(puzzle.cell_candidates(row_loc)).difference(pivot_candidates)
    #                 row_fence = puzzle.cell_fence(row_loc)
    #                 if len(row_difference) != 1:
    #                     continue
    #                 for col_loc in col_locs:
    #                     col_difference = set(puzzle.cell_candidates(col_loc)).difference(pivot_candidates)
    #                     col_fence = puzzle.cell_fence(col_loc)
    #                     if col_fence == row_fence:
    #                         continue
    #                     if len(col_difference) != 1:
    #                         continue
    #                     if not row_difference.issubset(col_difference):
    #                         continue
    #                     # check if three fences
    #                     if row_fence != pivot_fence and col_fence != pivot_fence:
    #                         other_loc = Loc(col_loc.row, row_loc.col)
    #                         edits += puzzle.rem(other_loc, row_difference)
    #
    #         return edits
    #
    #     # @staticmethod
    #     # def solve1(puzzle: Sudoku, locs: list[Loc]) -> int:
    #     #     edits = 0
    #     #     if len(locs) != 3:
    #     #         return edits
    #     #
    #     #     candidate_set = set()
    #     #
    #     #     for loc in locs:
    #     #         for candidate in puzzle.cell_candidates(loc):
    #     #             candidate_set.add(candidate)
    #     #
    #     #     if len(candidate_set) != 3:
    #     #         return edits
    #     #
    #     #     # need to find a pivot
    #     #     for pivot in locs:
    #     #         pincers = set(locs)
    #     #         pincers.remove(pivot)
    #     #         pincer0, pincer1 = pincers
    #     #
    #     #         pincer_fence0 = puzzle.cell_fence(pincer0)
    #     #         pincer_fence1 = puzzle.cell_fence(pincer1)
    #     #
    #     #         if pincer_fence0 == pincer_fence1:
    #     #             continue
    #     #
    #     #         temp_pivot0 = Loc(pincer0.row, pincer1.col)
    #     #         temp_pivot1 = Loc(pincer1.row, pincer0.col)
    #     #
    #     #         pivot_candidates = puzzle.cell_candidates(pivot)
    #     #         pincer0_candidates = set(puzzle.cell_candidates(pincer0))
    #     #         pincer1_candidates = set(puzzle.cell_candidates(pincer1))
    #     #
    #     #         if len(pivot_candidates) != 2 or len(pincer0_candidates) != 2 or len(pincer1_candidates) != 2:
    #     #             continue
    #     #
    #     #         if pincer0_candidates.issubset(pincer1_candidates):
    #     #             continue
    #     #
    #     #         # print(f'{pivot} {pincer0} {pincer1}')
    #     #
    #     #         for candidate in pivot_candidates:
    #     #             if candidate in pincer0_candidates:
    #     #                 pincer0_candidates.remove(candidate)
    #     #             if candidate in pincer1_candidates:
    #     #                 pincer1_candidates.remove(candidate)
    #     #
    #     #         if len(pincer0_candidates) != 1 or len(pincer1_candidates) != 1 or not pincer1_candidates.issubset(
    #     #                 pincer0_candidates):
    #     #             continue
    #     #
    #     #         shared_candidate = list(pincer0_candidates)[0]
    #     #
    #     #         other_pivot = None
    #     #
    #     #         if pivot == temp_pivot0:
    #     #             other_pivot = temp_pivot1
    #     #
    #     #         if pivot == temp_pivot1:
    #     #             other_pivot = temp_pivot0
    #     #
    #     #         if other_pivot is None:
    #     #             continue
    #     #
    #     #         if len(puzzle.cell_candidates(other_pivot)) == 1:
    #     #             continue
    #     #
    #     #             #
    #     #         # print(f'{pivot} {pincer0} {pincer1} {other_pivot}')
    #     #         # print(f'{puzzle.cell_candidates(pivot)} {puzzle.cell_candidates(pincer0)} {self.cell_candidates(pincer1)} {self.cell_candidates(other_pivot)}')
    #     #         edits += puzzle.rem(other_pivot, [shared_candidate])
    #     #
    #     #     return edits

    class XChain(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            remove = [Loc(0, 1), Loc(1, 1), Loc(6, 2), Loc(8, 2)]
            puzzle.override_loc_color(puzzle.house_row(2) + puzzle.house_row(7) + puzzle.house_fence('e'), Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)
            puzzle.override_loc_color([Loc(2, 2), Loc(3, 3), Loc(2, 3), Loc(5, 5), Loc(7, 1), Loc(7, 5)], Fore.YELLOW)

            edits += puzzle.rem(remove, [1])

            return edits

    class AlsXz(Technique):
        def solve0(self, puzzle: Sudoku):
            return 0

    class XWing(Technique):

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
            # # print("here")
            # for r in range(len(puzzle)):
            #     for c in range(len(puzzle)):
            #         loc = Loc(r, c)
            #
            #         if puzzle.is_cell_solved(loc):
            #             continue
            #
            #         for candidate in puzzle.cell_candidates(loc):
            #             edits += self.solve_one_cell(puzzle, loc, candidate)

            return edits

    class XyChain(Technique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            end_loc0 = Loc(2, 2)
            end_loc1 = Loc(5, 1)
            non_end_locs = [Loc(2, 5), Loc(5, 5)]
            remove = [Loc(0, 1), Loc(1, 1), Loc(2, 1), Loc(3, 2), Loc(4, 2), Loc(5, 2)]

            puzzle.override_loc_color([end_loc0, end_loc1], Fore.YELLOW)
            puzzle.override_loc_color(non_end_locs, Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)

            edits += puzzle.rem(remove, [1])

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

    class Skyscrapers1(Technique):
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

    class SkyscrapersRange(Technique):
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

    class SkyscrapersN(Technique):
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

    class MinesweeperSolver(Technique):

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

    class FutoshikiGreaterThanLessThan(Technique):  # (BaseFutoshikiTechnique):
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

    class FutoshikiCrossHatch(Technique):
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0
            return edits

    class RobotCrosswordsHouses(Technique):
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

    class MagnetsFullHouse(Technique):
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

    class MagnetsPair(Technique):
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

    class MagnetsZero(Technique):
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

    class MathraxHiddenSingle(Technique):

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            return edits

    class MathraxMathAddition(Technique):
        @staticmethod
        def get_valid_and_number(puzzle: Mathrax, loc: Loc) -> tuple[bool, Optional[int]]:
            string = puzzle.grid[loc.row][loc.col]
            if '+' in string:
                return True, int(string.replace('+', ''))
            return False, None

        def math_predicate(self, number: int, candidate: int, candidates1) -> bool:
            return number - candidate in candidates1

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(1, len(puzzle) * 2 - 1, 2):
                for c in range(1, len(puzzle) * 2 - 1, 2):
                    loc = Loc(r, c)
                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()
                    valid, number = self.get_valid_and_number(puzzle, loc)
                    if valid:
                        edits += self.solve_math(puzzle, number, tl, br)
                        edits += self.solve_math(puzzle, number, br, tl)
                        edits += self.solve_math(puzzle, number, tr, bl)
                        edits += self.solve_math(puzzle, number, bl, tr)
            return edits

        def solve_math(self, puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = 0
            candidates1 = set(puzzle.cell_candidates(cell1))
            for candidate in puzzle.expected_candidates():
                if self.math_predicate(number, candidate, candidates1):
                    continue
                edits += puzzle.rem([cell0], [candidate])
            return edits

    class MathraxMathSubtraction(MathraxMathAddition):
        def get_valid_and_number(self, puzzle: Mathrax, loc: Loc) -> tuple[bool, Optional[int]]:
            string = puzzle.grid[loc.row][loc.col]
            if '-' in string:
                return True, int(string.replace('-', ''))
            return False, None

        def math_predicate(self, number: int, candidate: int, candidates1) -> bool:
            return candidate + number in candidates1 or candidate - number in candidates1

    class MathraxMathMultiplication(MathraxMathAddition):

        def get_valid_and_number(self, puzzle: Mathrax, loc: Loc) -> tuple[bool, Optional[int]]:
            string = puzzle.grid[loc.row][loc.col]
            if 'x' in string:
                return True, int(string.replace('x', ''))
            return False, None

        def math_predicate(self, number: int, candidate: int, candidates1) -> bool:
            return number % candidate == 0 and int(number / candidate) in candidates1

    class MathraxMathDivision(MathraxMathAddition):
        def get_valid_and_number(self, puzzle: Mathrax, loc: Loc) -> tuple[bool, Optional[int]]:
            string = puzzle.grid[loc.row][loc.col]
            if '/' in string:
                return True, int(string.replace('/', ''))
            return False, None

        def solve_math(self, puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = self.__solve_division(puzzle, number, cell0, cell1)
            edits += self.__solve_division(puzzle, number, cell1, cell0)
            return edits

        @staticmethod
        def __solve_division(puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
            edits = 0
            candidates1 = set(puzzle.cell_candidates(cell1))
            if number == 2:
                if 10 not in candidates1:
                    edits += puzzle.rem([cell0], [5])
                if 6 not in candidates1:
                    edits += puzzle.rem([cell0], [3])
                if 3 not in candidates1:
                    edits += puzzle.rem([cell0], [6])
                if 2 not in candidates1 or 8 not in candidates1:
                    edits += puzzle.rem([cell0], [4])
                if 1 not in candidates1 and 4 not in candidates1:
                    edits += puzzle.rem([cell0], [2])
                if 14 not in candidates1:
                    edits += puzzle.rem([cell0], [7])

            if number == 3:
                if 1 not in candidates1:
                    edits += puzzle.rem([cell0], [3])
                if 3 not in candidates1:
                    edits += puzzle.rem([cell0], [1])
                if 6 not in candidates1:
                    edits += puzzle.rem([cell0], [2])
                if 12 not in candidates1:
                    edits += puzzle.rem([cell0], [4])
                if 15 not in candidates1:
                    edits += puzzle.rem([cell0], [5])
                if 2 not in candidates1 and 18 not in candidates1:
                    edits += puzzle.rem([cell0], [6])
                # if 21 not in candidates1:
                #     edits += puzzle.rem([cell0], [7])

            # if number == 3:
            # edits += puzzle.rem([cell0, cell1], [5, 7])
            # if 1 not in candidates1 and 4 not in candidates1:
            #     edits += puzzle.rem([cell0], [2])
            # if 3 not in candidates1:
            #     edits += puzzle.rem([cell0], [6])

            # if
            # if 1 not in candidates1 and 3 not in candidates1:
            #     edits += puzzle.rem([cell0], [2])
            # if 3 not in candidates1 and 5 not in candidates1:
            #     edits += puzzle.rem([cell0], [4])
            # if 4 not in candidates1 and 6 not in candidates1:
            #     edits += puzzle.rem([cell0], [5])
            # return edits
            # edits = 0
            # candidates1 = set(puzzle.cell_candidates(cell1))
            # if number == 3:
            #     for candidate in puzzle.expected_candidates():
            #         # if candidate + number not in candidates1 and candidate - number not in candidates1:
            #         if (candidate % number == 0 and int(candidate / number) in candidates1) or  (number % candidate == 0 and int(number / candidate) in candidates1):
            #             continue
            #         edits += puzzle.rem([cell0], [candidate])
            return edits

    class MathraxMath04XWing(Technique):

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(len(puzzle) * 2 - 1):
                for c in range(len(puzzle) * 2 - 1):

                    if puzzle.grid[r][c] != '04x' and puzzle.grid[r][c] != '04+':
                        continue

                    loc = Loc(r, c)

                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()

                    remove = set(puzzle.house_row(tl.row) + puzzle.house_col(tl.col) + puzzle.house_row(
                        br.row) + puzzle.house_col(br.col)).difference([tl, tr, bl, br])

                    edits += puzzle.rem(remove, [2])

            return edits

    class MathraxOdd(Technique):
        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(len(puzzle) * 2 - 1):
                for c in range(len(puzzle) * 2 - 1):

                    if puzzle.grid[r][c] != 'OOO':
                        continue

                    loc = Loc(r, c)

                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()
                    edits += puzzle.rem([tl, tr, bl, br], [2, 4, 6])
            return edits

    class MathraxEven(Technique):
        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(len(puzzle) * 2 - 1):
                for c in range(len(puzzle) * 2 - 1):

                    if puzzle.grid[r][c] != 'EEE':
                        continue

                    loc = Loc(r, c)

                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()
                    edits += puzzle.rem([tl, tr, bl, br], [1, 3, 5, 7])
            return edits

    class MathraxMath01MinusXWing(Technique):

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(len(puzzle) * 2 - 1):
                for c in range(len(puzzle) * 2 - 1):

                    if puzzle.grid[r][c] != '01-':
                        continue

                    loc = Loc(r, c)

                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()

                    tl_candidates = puzzle.cell_candidates(tl)
                    bl_candidates = puzzle.cell_candidates(bl)
                    tr_candidates = puzzle.cell_candidates(tr)
                    br_candidates = puzzle.cell_candidates(br)

                    expected = {1, 2, 3}

                    if expected.issuperset(tl_candidates) and expected.issuperset(br_candidates):
                        edits += puzzle.rem([tr, bl], [2])

                    if expected.issuperset(tr_candidates) and expected.issuperset(bl_candidates):
                        edits += puzzle.rem([tl, br], [2])
            return edits

    class MathraxMath02MinusXWing(Technique):

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(len(puzzle) * 2 - 1):
                for c in range(len(puzzle) * 2 - 1):

                    if puzzle.grid[r][c] != '02-':
                        continue

                    loc = Loc(r, c)

                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()

                    tl_candidates = puzzle.cell_candidates(tl)
                    bl_candidates = puzzle.cell_candidates(bl)
                    tr_candidates = puzzle.cell_candidates(tr)
                    br_candidates = puzzle.cell_candidates(br)

                    expected = {2, 4}

                    if expected.issuperset(tl_candidates) and expected.issuperset(br_candidates):
                        edits += puzzle.rem([tr, bl], [2, 4])

                    if expected.issuperset(tr_candidates) and expected.issuperset(bl_candidates):
                        edits += puzzle.rem([tl, br], [2, 4])
            return edits

    class MathraxMath04MinusXWing(Technique):

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            for r in range(len(puzzle) * 2 - 1):
                for c in range(len(puzzle) * 2 - 1):

                    if puzzle.grid[r][c] != '04-':
                        continue

                    loc = Loc(r, c)

                    tl = loc.top_left()
                    tr = loc.top_right()
                    bl = loc.bottom_left()
                    br = loc.bottom_right()

                    tl_candidates = puzzle.cell_candidates(tl)
                    bl_candidates = puzzle.cell_candidates(bl)
                    tr_candidates = puzzle.cell_candidates(tr)
                    br_candidates = puzzle.cell_candidates(br)

                    expected = {1, 5}

                    if expected.issuperset(tl_candidates) and expected.issuperset(br_candidates):
                        edits += puzzle.rem([tr, bl], [1, 5])

                    if expected.issuperset(tr_candidates) and expected.issuperset(bl_candidates):
                        edits += puzzle.rem([tl, br], [1, 5])
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

    class TennerHiddenPair(Technique):
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

    class TennerNakedPair(Technique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for row in range(len(puzzle)):
                house = puzzle.house_row_cell_locs(row)
                edits += NakedPair.static_solve_house(puzzle, house)
            return edits

    class TennerNakedPairColumn(Technique):
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

    class TennerTotalHiddenSingle(Technique):
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

    class PowerGridCrossHatch(Technique):
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

    class PowerGridHiddenPower(Technique):
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

    class PowerGridTech(Technique):
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

    class PowerGridTechExplicit(Technique):
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

            if all(house[0].row == loc.row for loc in house):

                if len(puzzle) == 9 and power == 6:
                    edge_locs = [house[0], house[1], house[7], house[8]]
                    for loc in edge_locs:
                        north = loc.north()
                        south = loc.south()
                        if north.row >= 0:
                            edits += puzzle.rem([north], [POWER])
                        if south.row < len(puzzle):
                            edits += puzzle.rem([south], [POWER])

                if len(puzzle) == 9 and power == 5:
                    edge_locs = [house[1], house[7]]
                    for loc in edge_locs:
                        north = loc.north()
                        south = loc.south()
                        if north.row >= 0:
                            edits += puzzle.rem([north], [POWER])
                        if south.row < len(puzzle):
                            edits += puzzle.rem([south], [POWER])

                if len(puzzle) == 9 and power == 5:
                    indexes = set([index for index in range(len(house)) if
                                   puzzle.grid[house[index].row][house[index].col] == '10'])
                    if indexes == {0, 1, 6, 7}:

                        for loc in [house[index] for index in indexes]:
                            north = loc.north()
                            south = loc.south()
                            if north.row >= 0:
                                edits += puzzle.rem([north], [POWER])
                            if south.row < len(puzzle):
                                edits += puzzle.rem([south], [POWER])

                # pass

            # if all(house[0].col == loc.col for loc in house):
            #     pass

            return edits

    class KropkiBb(Technique):

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
                    # [
                    #     center_cell.west(2),
                    #     center_cell.west(),
                    #     center_cell.north(),
                    #     center_cell.north(2),
                    # ],
                    # east south
                    # [
                    #     center_cell.east(2),
                    #     center_cell.east(),
                    #     center_cell.south(),
                    #     center_cell.south(2)
                    # ],
                    # west south
                    # [
                    #     center_cell.west(2),
                    #     center_cell.west(),
                    #     center_cell.south(),
                    #     center_cell.south(2),
                    # ],
                    # east north
                    # [
                    #     center_cell.north(2),
                    #     center_cell.north(),
                    #     center_cell.east(),
                    #     center_cell.east(2),
                    # ],
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
                        cells_in_sets = cells_in_sets + puzzle.house_row(row_set.pop())

                    if len(col_set) == 1:
                        cells_in_sets = cells_in_sets + puzzle.house_col(col_set.pop())

                    # if puzzle.has_fences:
                    #     fence_set = {puzzle.cell_fence(other0), puzzle.cell_fence(center_cell),
                    #                  puzzle.cell_fence(other1)}
                    #     if len(fence_set) == 1:
                    #         cells_in_sets = cells_in_sets + puzzle.house_fence_cell_locs(fence_set.pop())

                    cells_to_remove_from = set(cells_in_sets).difference(cell_set)

                    edits += puzzle.rem(cells_to_remove_from, [2, 4])
                    edits += puzzle.rem([center_cell], [1, 3, 5, 6, 7, 8, 9])
                    edits += puzzle.rem([other0, other1], [3, 5, 6, 7, 9])

                    if {2, 4, 8}.issuperset(puzzle.cell_candidates(other0)) and \
                            {2, 4}.issuperset(puzzle.cell_candidates(center_cell)) and \
                            {2, 4, 8}.issuperset(puzzle.cell_candidates(other1)):
                        edits += puzzle.rem([center_cell], [2])

                    if {1, 2, 4, 8}.issuperset(puzzle.cell_candidates(other0)) and \
                            {2, 4}.issuperset(puzzle.cell_candidates(center_cell)) and \
                            {2, 4, 8}.issuperset(puzzle.cell_candidates(other1)):
                        edits += puzzle.rem([other0], [4])
                        edits += puzzle.rem([other1], [8])

            return edits

    class KropkiBlack(Technique):
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

                        string = puzzle.grid[center.row][center.col].replace(".", "", -1)

                        if string != "b" and string != "BB":
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

    class KropkiBw(Technique):

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
                    # # west north
                    # [
                    #     center_cell.west(2),
                    #     center_cell.west(),
                    #     center_cell.north(),
                    #     center_cell.north(2),
                    # ],
                    # # east south
                    # [
                    #     center_cell.east(2),
                    #     center_cell.east(),
                    #     center_cell.south(),
                    #     center_cell.south(2)
                    # ],
                    # # west south
                    # [
                    #     center_cell.west(2),
                    #     center_cell.west(),
                    #     center_cell.south(),
                    #     center_cell.south(2),
                    # ],
                    # # east north
                    # [
                    #     center_cell.north(2),
                    #     center_cell.north(),
                    #     center_cell.east(),
                    #     center_cell.east(2),
                    # ],
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

    class KropkiDiamondEbww(Technique):
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
                    #  b
                    # . w
                    #  w

                    # if puzzle.is_black(loc.north()) and \
                    #     puzzle.is_empty(loc.west()) and \
                    #     puzzle.is_white(loc.east()) and \
                    #     puzzle.is_white(loc.south()):
                    #     print('here')

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

    class KropkiDiamondEwbw(Technique):
        edits = 0

        def solve0(self, puzzle: Kropki) -> int:
            # black_empty = [5, 7, 9]
            black_white = [1]
            # white_empty = [3, 5, 7, 9]
            # white_white = [1, 4, 6, 8, 9]

            edits = 0
            for r in range(puzzle.grid_length):
                for c in range(puzzle.grid_length):
                    if r % 2 == 0 or c % 2 == 0:
                        continue

                    loc = Loc(r, c)

                    if puzzle.is_white(loc.north()) and \
                            puzzle.is_empty(loc.east()) and \
                            puzzle.is_white(loc.south()) and \
                            puzzle.is_black(loc.west()):
                        edits += puzzle.rem([loc.north().west(), loc.south().west()], black_white)
                        # edits += puzzle.rem([loc.south().west()], black_white)
                        # edits += puzzle.rem([loc.north().east()], white_empty)
                        # edits += puzzle.rem([loc.south().east()], white_white)

                    # if puzzle.is_empty(loc.east()) and puzzle.is_white(loc.south()) and puzzle.is_white(
                    #         loc.west()) and puzzle.is_black(loc.north()):
                    # edits += puzzle.rem([loc.north().west()], black_white)
                    # edits += puzzle.rem([loc.south().west()], white_white)
                    # edits += puzzle.rem([loc.north().east()], black_empty)
                    # edits += puzzle.rem([loc.south().east()], white_empty)

            return edits

    class KropkiDiamond(Technique):
        edits = 0

        def solve0(self, puzzle: Kropki) -> int:
            black_black = [1, 8]
            black_white = [1]

            edits = 0
            for r in range(puzzle.grid_length):
                for c in range(puzzle.grid_length):
                    if r % 2 == 0 or c % 2 == 0:
                        continue

                    loc = Loc(r, c)

                    north = puzzle.grid[loc.north().row][loc.north().col]
                    east = puzzle.grid[loc.east().row][loc.east().col]
                    south = puzzle.grid[loc.south().row][loc.south().col]
                    west = puzzle.grid[loc.west().row][loc.west().col]

                    nw = loc.north().west()
                    ne = loc.north().east()
                    sw = loc.south().west()
                    se = loc.south().east()

                    #  w
                    # b .
                    #  b
                    if north == 'w' and \
                            west == 'b' and east == '.' and \
                            south == 'b':
                        # black_white
                        edits += puzzle.rem([nw], [1, 3, 5, 6, 7, 9])
                        # black_black
                        edits += puzzle.rem([sw], [1, 3, 5, 6, 7, 8, 9])
                        # white_empty
                        edits += puzzle.rem([ne], [2, 4, 6, 8])
                        # black_empty
                        edits += puzzle.rem([se], [3, 5, 6, 7, 9])

                    #  w
                    # w b
                    #  b
                    if north == 'w' and \
                            west == 'w' and east == 'b' and \
                            south == 'b':
                        # white_white
                        edits += puzzle.rem([nw], [6, 8])
                        # white_black
                        edits += puzzle.rem([sw, se, ne], [5, 7, 9])

                    #  b
                    # w .
                    #  b
                    if north == 'b' and \
                            west == 'w' and east == '.' and \
                            south == 'b':
                        # black_white
                        edits += puzzle.rem([nw, sw], [1, 5, 7, 9])
                        # black_empty
                        edits += puzzle.rem([ne, se], [3, 5, 7, 9])

                    #  .
                    # w w
                    #  b
                    if north == '.' and \
                            west == 'w' and east == 'w' and \
                            south == 'b':
                        # black_white
                        edits += puzzle.rem([sw, se], [1, 5, 7, 9])
                        # white_empty
                        edits += puzzle.rem([nw, ne], [6, 8])

                    #  w
                    # b .
                    #  w
                    if north == 'w' and \
                            west == 'b' and east == '.' and \
                            south == 'w':
                        # black_white
                        edits += puzzle.rem([sw, nw], [1, 5, 7, 9])
                        # white_empty
                        edits += puzzle.rem([se, ne], [6, 8])

                    # edits += self.solve_bwwe(puzzle, loc)
                    #  w
                    # w .
                    #  b
                    if north == 'w' and \
                            west == 'w' and east == '.' and \
                            south == 'b':
                        # white_white
                        edits += puzzle.rem([nw], [1, 6, 8, 9])
                        # black_white
                        edits += puzzle.rem([sw], [1, 5, 7, 9])
                        # white_empty
                        edits += puzzle.rem([ne], [7, 9])
                        # black_empty
                        edits += puzzle.rem([se], [5, 7, 9])

                    #  w
                    # w b
                    #  w
                    if north == 'w' and \
                            west == 'w' and east == 'b' and \
                            south == 'w':
                        # white_black
                        edits += puzzle.rem([ne, se], [4, 5, 7, 8, 9])
                        # white_white
                        edits += puzzle.rem([nw, sw], [6, 7, 8, 9])

                    #  w
                    # w .
                    #  w
                    if north == 'w' and \
                            west == 'w' and east == '.' and \
                            south == 'w':
                        edits += self.solve_wwwe(puzzle, [ne, se], [nw, sw])

                    #  w
                    # w w
                    #  .
                    if north == 'w' and \
                            west == 'w' and east == 'w' and \
                            south == '.':
                        edits += self.solve_wwwe(puzzle, [sw, se], [nw, ne])

            return edits

        def solve_bwwe(self, puzzle: Kropki, loc: Loc) -> int:
            edits = 0
            north = puzzle.grid[loc.north().row][loc.north().col]
            east = puzzle.grid[loc.east().row][loc.east().col]
            south = puzzle.grid[loc.south().row][loc.south().col]
            west = puzzle.grid[loc.west().row][loc.west().col]

            nw = loc.north().west()
            ne = loc.north().east()
            sw = loc.south().west()
            se = loc.south().east()

            white_white = [1, 6, 8, 0]
            black_white = [1, 5, 7, 9]
            white_empty = [7, 9]
            black_empty = [5, 7, 9]

            news = np.array([[nw, ne], [sw, se]], Loc)
            candidate_groups = np.array([[black_white, white_white], [black_empty, white_empty]], object)
            letters = np.array([['w', 'w'], ['b', '.']], str)

            #  w
            # b w
            #  .
            if north == 'w' and \
                    west == 'b' and east == 'w' and \
                    south == '.':
                # white_white
                edits += puzzle.rem(news[0, 1], candidate_groups[0, 1])
                # black_white
                edits += puzzle.rem(news[0, 0], candidate_groups[0, 0])
                # white_empty
                edits += puzzle.rem(news[1, 1], candidate_groups[1, 1])
                # black_empty
                edits += puzzle.rem(news[1, 0], candidate_groups[1, 0])

            news = np.rot90(news, 1)
            candidate_groups = np.rot90(candidate_groups, 1)

            #  w
            # w .
            #  b
            if north == 'w' and \
                    west == 'w' and east == '.' and \
                    south == 'b':
                # white_white
                edits += puzzle.rem([nw], white_white)
                # black_white
                edits += puzzle.rem([sw], black_white)
                # white_empty
                edits += puzzle.rem([ne], white_empty)
                # black_empty
                edits += puzzle.rem([se], black_empty)

            #  b
            # . w
            #  w
            if north == 'b' and \
                    west == '.' and east == 'w' and \
                    south == 'w':
                # white_white
                edits += puzzle.rem([se], white_white)
                # black_white
                edits += puzzle.rem([ne], black_white)
                # white_empty
                edits += puzzle.rem([sw], white_empty)
                # black_empty
                edits += puzzle.rem([nw], black_empty)

            #  b
            # w .
            #  w
            if north == 'b' and \
                    west == 'w' and east == '.' and \
                    south == 'w':
                # white_white
                edits += puzzle.rem([sw], white_white)
                # black_white
                edits += puzzle.rem([ne], black_white)
                # white_empty
                edits += puzzle.rem([se], white_empty)
                # black_empty
                edits += puzzle.rem([nw], black_empty)

            return edits

        def solve_wwwe(self, puzzle: Kropki, white_empty, white_white) -> int:
            edits = 0
            # white_empty
            edits += puzzle.rem(white_empty, [3])
            # white_white
            edits += puzzle.rem(white_white, [1, 9])
            return edits

    class KropkiDiamondWwwe(Technique):
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

    class KropkiDominatingEmpty(Technique):

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

    class KropkiEmpty(Technique):

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

            if set(loc0_candidates) == {1, 8}:
                edits += puzzle.rem([loc1], [4])

            if len(loc0_candidates) != 1:
                return edits

            candidate = loc0_candidates[0]

            candidates_to_remove = [candidate + 1, candidate - 1, candidate * 2, candidate]

            if candidate % 2 == 0:
                candidates_to_remove.append(int(candidate / 2))

            edits += puzzle.rem([loc1], candidates_to_remove)

            return edits

    class KropkiWhite(Technique):

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

                        string = puzzle.grid[center.row][center.col].replace(".", "", -1)

                        if string != "w" and string != "WW":
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

    class KropkiWw(Technique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class SumscrapersSecondInLine(Technique):

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

    class SumscrapersLastIsMax(Technique):

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

    class SumscrapersNextToScraper(Technique):

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

    class SumscrapersTech(Technique):
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

    class Parks1Bent3(Technique):

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

    class Parks1CrossHatch(Technique):

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

    class Parks1CrossHatchTouching(Technique):

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

    class Parks1DominateFence(Technique):
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

    class Parks1HiddenSingle(Technique):
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

    class Parks1LockedCandidatesClaiming(Technique):

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

    class Parks1LockedCandidatesPointing(Technique):

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

    class Parks1Shape_00_01(Technique):

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
# 4742
