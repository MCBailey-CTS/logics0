from abc import abstractmethod
from turtle import pu, st
from typing import Optional

from Loc import Loc
from _puzzles import Sudoku, Magnets, Kropki, Parks1, Tenner, RobotFences, RobotCrosswords, Minesweeper, PowerGrid, \
    AbstractPainting, Clouds, Futoshiki, Mathrax, Sumscrapers, Skyscrapers

PLUS = "+"
MINUS = "-"
EMPTY = "."


class Solving:
    @staticmethod
    def sudoku_techniques() -> list:
        return [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.NakedPair(),
            Techs.LockedCandidatesPointing(),
            Techs.LockedCandidatesClaiming(),
            Techs.HiddenSingle(),
            # Techs.UniqueRectangleType1(),
            # Techs.UniqueRectangleType2(),
            # Techs.UniqueRectangleType4(),
            # Techs.XWing(),
            # Techs.Bug(),
            # Techs.NakedTriple(),
            # Techs.WWing(),
            # Techs.ShashimiXWingPlus1(),
            # Techs.XyWing(),
            # Techs.FinnedXWing(),
            # Techs.AvoidableRectangleType1(),
            # Techs.WxyzWing(),
            # Techs.SwordFish(),
            # Techs.JellyFish(),
        ]

    @staticmethod
    def kropki_techniques() -> list:
        return [
            Techs.KropkiBlack(),
            Techs.KropkiWhite(),
            Techs.KropkiEmpty(),
            Techs.KropkiNakedPair(),
        ]

    @staticmethod
    def robot_fences_techniques() -> list:
        return [Techs.CrossHatchRobotFences(), Techs.HiddenSingleRobotFences()]

    @staticmethod
    def parks1_techniques() -> list:
        return [
            Techs.Parks1CrossHatch(),
            Techs.Parks1HiddenSingle(),
            Techs.Parks1CrossHatchTouching(),
            Techs.Parks1LockedCandidatesPointing(),
            # Techs.Parks1LockedCandidatesClaiming(),
            Techs.Parks1Bent3(),
            Techs.Parks1Shape_00_01()
        ]

    @staticmethod
    def parks2_techniques() -> list:
        return []

    @staticmethod
    def tenner_techniques() -> list:
        return [Techs.TennerCrossHatch(),
                Techs.TennerNakedPair(),
                Techs.TennerHiddenPair(),
                Techs.TennerHiddenSingle(),
                Techs.TennerTotalHiddenSingle(),
                Techs.TennerPowerSetTotals(),
                Techs.TennerNakedPairColumn()]

    @staticmethod
    def futoshiki_techniques() -> list:
        return []

    @staticmethod
    def clouds_techniques() -> list:
        return []

    @staticmethod
    def knightoku_techniques() -> list:
        return [Techs.CrossHatchKnightoku()] + Solving.sudoku_techniques()

    @staticmethod
    def kakuro_techniques() -> list:
        return []

    @staticmethod
    def lighthouses_techniques() -> list:
        return []

    @staticmethod
    def walls_techniques() -> list:
        return []

    @staticmethod
    def tents_techniques() -> list:
        return []

    @staticmethod
    def mathrax_techniques() -> list:
        return []

    @staticmethod
    def sumscrapers_techniques() -> list:
        return [Techs.SumscrapersTech(), Techs.CrossHatchSumscrapers(), Techs.HiddenSingleSumscrapers(),
                Techs.SumscrapersSecondInLine(), Techs.SumscrapersLastIsMax(), Techs.SumscrapersNextToScraper()]

    @staticmethod
    def skyscrapers_techniques() -> list:
        return [
            Techs.SkyscrapersN(),
            Techs.CrossHatchSumscrapers(), Techs.HiddenSingleSumscrapers(), Techs.SkyscrapersN(), Techs.Skyscrapers1(),
            Techs.SkyscrapersRange()
        ]

    @staticmethod
    def minesweeper_techniques():
        return [Techs.MinesweeperSolver()]

    @staticmethod
    def snail3_techniques() -> list:
        return []

    @staticmethod
    def mine_ships_techniques() -> list:
        return []

    @staticmethod
    def sentinels_techniques() -> list:
        return []

    @staticmethod
    def nurikabe_techniques() -> list:
        return []

    @staticmethod
    def robot_crosswords_techniques() -> list:
        return [Techs.RobotCrosswordsHouses()]

    @staticmethod
    def power_grid_techniques() -> list:
        return [
            Techs.PowerGridTech(),
            Techs.PowerGridHiddenPower()
        ]

    @staticmethod
    def abstractpainting_techniques() -> list:
        return []

    @staticmethod
    def battle_ships_techniques() -> list:
        return []

    @staticmethod
    def hidden_stars_techniques() -> list:
        return []

    @staticmethod
    def magnets_techniques() -> list:
        return []

    @staticmethod
    def lightenup_techniques() -> list:
        return []


class Techs:
    class BasePuzzleTechnique:
        def __repr__(self) -> str:
            return f'{self.__class__.__name__}()'

        @abstractmethod
        def solve0(self, puzzle) -> int:
            raise NotImplementedError()

    class MinesweeperSolver:  # (BasePuzzleTechnique):

        @staticmethod
        def surrounding(puzzle: Minesweeper, loc: Loc) -> list[Loc]:
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
            for r in range(puzzle.length):
                for c in range(puzzle.length):
                    loc = Loc(r, c)
                    if puzzle.is_number_cell(loc):
                        number = int(self.grid[loc.row][loc.col])

                        if number == 0:
                            edits += puzzle.rem()

            return edits

    class CrossHatchKnightoku:
        def solve0(self):
            pass

    class SkyscrapersCrossHatch:
        def solve0(self):
            pass

    class SkyscrapersHiddenSingle:
        def solve0(self):
            pass

    class SkyscrapersEdges:
        def solve0(self):
            pass

    # @staticmethod
    # def _cross_hatch()

    class BaseSudokuTechnique:
        @abstractmethod
        def solve0(self, puzzle: Sudoku) -> int:
            raise NotImplementedError()

    class BaseMagnetsTechnique:
        @abstractmethod
        def solve0(self, puzzle: Magnets) -> int:
            raise NotImplementedError()

    class BaseKropkiTechnique:
        @abstractmethod
        def solve0(self, puzzle: Kropki) -> int:
            raise NotImplementedError()

    class HiddenQuad(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            return 0

    class NakedTriple(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            naked_count = 3
            for house in puzzle.houses_rows_cols_fences():
                for i in range(puzzle.length):
                    for ii in range(puzzle.length):
                        for iii in range(puzzle.length):
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

                            for j in range(puzzle.length):
                                if j not in indexes:
                                    edits += puzzle.rem(house[j], list(candidate_set))
            return edits

    class XyWing(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
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

    class CrossHatch:

        #

        # @staticmethod
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for cell in list(puzzle.unsolved_cells()):
                neighbors = set(
                    puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
                #  + puzzle.house_fence(
                #     puzzle.cell_fence(cell)))

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

    class HiddenSingle:
        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_rows_cols_fences():
                edits += Techs.HiddenSingle.solve1(puzzle, house)
            return edits

        @staticmethod
        def solve1(puzzle: Sudoku, house: list[Loc]) -> int:
            edits = 0
            # print(house)
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
                # print(candidates_to_remove)
                edits += puzzle.rem(locs_with_candidate[0], candidates_to_remove)

            return edits

    class Bug(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

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

            total = puzzle.length * puzzle.length

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

    class HiddenPair(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for house in puzzle.houses_rows_cols_fences():
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

    class LockedCandidatesPointing(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
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

    class LockedCandidatesClaiming(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
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

    class UniqueRectangleType4(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for r in range(puzzle.length):

                house = puzzle.house_row(r)

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

                        if not candidates0.issubset(candidates1):
                            continue

                        col0 = puzzle.house_col(l0.col)
                        col1 = puzzle.house_col(l1.col)

                        for j in range(puzzle.length):
                            corner0 = col0[j]
                            corner1 = col1[j]

                            loc_set = {l0, l1, corner0, corner1}

                            if len(loc_set) != 4:
                                continue

                            corner0_candidates = puzzle.cell_candidates(corner0)
                            corner1_candidates = puzzle.cell_candidates(corner1)

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

            for c in range(puzzle.length):

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

                        if not candidates0.issubset(candidates1):
                            continue

                        row0 = puzzle.house_row(l0.row)
                        row1 = puzzle.house_row(l1.row)

                        for j in range(puzzle.length):
                            corner0 = row0[j]
                            corner1 = row1[j]

                            loc_set = {l0, l1, corner0, corner1}

                            if len(loc_set) != 4:
                                continue

                            corner0_candidates = puzzle.cell_candidates(corner0)
                            corner1_candidates = puzzle.cell_candidates(corner1)

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

    class XWing(BaseSudokuTechnique):
        @staticmethod
        def solve1(puzzle: Sudoku, house0: list[Loc], house1: list[Loc]) -> int:
            edits = 0
            for candidate in puzzle.expected_candidates():
                locs0 = [loc for loc in house0 if candidate in puzzle.cell_candidates(loc)]
                locs1 = [loc for loc in house1 if candidate in puzzle.cell_candidates(loc)]

                if len(locs0) != 2 or len(locs1) != 2:
                    continue

                rows = set([loc.row for loc in locs0 + locs1])
                cols = set([loc.col for loc in locs0 + locs1])

                loc_set = set(locs0 + locs1)

                if len(cols) != 2 or len(rows) != 2:
                    continue

                for row in rows:
                    for loc in puzzle.house_row(row):
                        if loc not in loc_set:
                            edits += puzzle.rem(loc, [candidate])

                for col in cols:
                    for loc in puzzle.house_col(col):
                        if loc not in loc_set:
                            edits += puzzle.rem(loc, [candidate])

            return edits

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for i in range(puzzle.length):
                for ii in range(puzzle.length):
                    if i == ii:
                        continue
                    edits += self.solve1(
                        puzzle,
                        puzzle.house_row(i),
                        puzzle.house_row(ii),
                    )
                    edits += self.solve1(
                        puzzle,
                        puzzle.house_col(i),
                        puzzle.house_col(ii),
                    )
            return edits

    # class CrossHatchKnightoku:
    #     def solve0(self, puzzle: Knightoku) -> int:
    #         edits = 0
    #
    #         for cell in puzzle.unsolved_cells():
    #             _candidates = puzzle.cell_candidates(cell)
    #
    #             if len(_candidates) != 1:
    #                 continue
    #
    #             solved_candidate = list(_candidates)[0]
    #
    #             knights_moves = [
    #                 cell.north(2).west(),
    #                 cell.north(2).east(),
    #                 cell.north().west(2),
    #                 cell.north().east(2),
    #                 cell.south(2).west(),
    #                 cell.south(2).east(),
    #                 cell.south().west(2),
    #                 cell.south().east(2),
    #
    #             ]
    #
    #             print("made it here")
    #
    #             for knight_move in knights_moves:
    #                 if knight_move.is_valid_sudoku(puzzle.length):
    #                     edits += puzzle.rem([knight_move], [solved_candidate])
    #
    #             # neighors = puzzle.house_row(cell) + puzzle.house_col(cell)
    #
    #             # if puzzle.has_fences():
    #             #     neighbors = neighors + puzzle.house_fence(puzzle.cell_fence(cell))
    #
    #             # # row_set = puzzle.house_row(cell)
    #             # # col_set = puzzle.house_row(cell)
    #
    #             # # puzzle.houses_rows_cols()
    #
    #             # # for house
    #
    #             # edits += puzzle.rem()
    #
    #             # for loc in set(neighbors).difference([cell])
    #
    #         return edits

    class ShashimiXWingPlus1:
        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0
            for candidate in puzzle.expected_candidates():
                for i in range(puzzle.length):
                    for ii in range(puzzle.length):
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

    class UniqueRectangleStruct:
        def __init__(self, puzzle: Sudoku, corner: Loc, opposite: Loc):
            if corner.row == opposite.row or corner.col == opposite.col:
                raise ValueError("Cannot create a rectangle from given corners")

    class UniqueRectangleType1(BaseSudokuTechnique):
        @staticmethod
        def solve1(puzzle: Sudoku, corners: list[Loc]) -> int:
            edits = 0
            corner_set = set(corners)

            if len(corner_set) != 4:
                raise ValueError("number of corners didn't equal 4")

            rows = set([loc.row for loc in corners])
            cols = set([loc.col for loc in corners])
            fences = set([puzzle.cell_fence(loc) for loc in corners])

            if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                return edits

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

            edits += puzzle.rem(corner_unique_set.pop(), candidate_set)

            return edits

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            locs: list[Loc] = []
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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
                    edits += self.solve1(
                        puzzle,
                        [
                            l0,
                            l1,
                            Loc(l0.row, l1.col),
                            Loc(l1.row, l0.col)
                        ])
            return edits

    class UniqueRectangleType2(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for corner0 in puzzle.unsolved_cells():
                for corner1 in puzzle.unsolved_cells():
                    corners = [
                        corner0,
                        corner1,
                        Loc(corner0.row, corner1.col),
                        Loc(corner1.row, corner0.col),
                    ]

                    rows = set([loc.row for loc in corners])
                    cols = set([loc.col for loc in corners])
                    fences = set([puzzle.cell_fence(loc) for loc in corners])

                    if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                        continue
                    length_2 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 2]
                    length_3 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 3]

                    if len(length_2) != 2 or len(length_3) != 2:
                        continue

                    length_2_candidates = [puzzle.cell_candidates(loc) for loc in length_2]
                    length_3_candidates = [puzzle.cell_candidates(loc) for loc in length_3]

                    if not length_2_candidates[0].issubset(length_2_candidates[1]) or not length_2_candidates[
                        0].issuperset(length_2_candidates[1]):
                        continue

                    if not length_3_candidates[0].issubset(length_3_candidates[1]) or not length_3_candidates[
                        0].issuperset(length_3_candidates[1]):
                        continue

                    candidate_to_remove = list(set(length_3_candidates[0]).difference(length_2_candidates[0]))[0]

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

            return edits

        def solve1(self, puzzle: Sudoku, corners: list[Loc]) -> int:
            edits = 0

            corner_set = set(corners)

            if len(corner_set) != 4:
                raise ValueError(f'cannot make uniqe rectangle from {len(corner_set)} corner(s)')

            rows = set([loc.row for loc in corner_set])
            if len(rows) != 2:
                raise ValueError(f'cannot make uniqe rectangle from {len(rows)} row(s)')

            cols = set([loc.col for loc in corner_set])
            if len(cols) != 2:
                raise ValueError(f'cannot make uniqe rectangle from {len(cols)} col(s)')

            fences = set([puzzle.cell_fence(loc) for loc in corner_set])
            if len(fences) != 2:
                raise ValueError(f'cannot make uniqe rectangle from {len(fences)} fence(s)')

            two_candidates = [loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 2]
            three_candidates = [loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 3]

            if len(two_candidates) != 2:
                return edits

            if len(three_candidates) != 2:
                return edits

            two_candidates_set0 = set(puzzle.cell_candidates(two_candidates[0]))
            two_candidates_set1 = set(puzzle.cell_candidates(two_candidates[1]))

            three_candidates_set0 = set(puzzle.cell_candidates(three_candidates[0]))
            three_candidates_set1 = set(puzzle.cell_candidates(three_candidates[1]))

            if puzzle.cell_fence(two_candidates[0]) != puzzle.cell_fence(two_candidates[1]):
                return edits

            if puzzle.cell_fence(three_candidates[0]) != puzzle.cell_fence(three_candidates[1]):
                return edits

            # checks to see if the two_candidates are the same set
            if not two_candidates_set0.issubset(two_candidates_set1):
                return edits

            # checks to see if the three_candidates are the same set
            if not three_candidates_set0.issubset(three_candidates_set1):
                return edits

            # checks to see that three_candidates is a superset of two_candidates
            if not three_candidates_set0.issuperset(two_candidates_set0):
                return edits

            if three_candidates[0].row == three_candidates[1].row:
                row = three_candidates[0].row
                fence = puzzle.cell_fence(three_candidates[0])
                row_house_set = set(puzzle.house_row(row))
                fence_house_set = set(puzzle.house_fence(fence))

                row_house_set.discard(three_candidates[0])
                row_house_set.discard(three_candidates[1])
                fence_house_set.discard(three_candidates[0])
                fence_house_set.discard(three_candidates[1])

                for loc in list(row_house_set) + list(fence_house_set):
                    edits += puzzle.rem(loc, set(three_candidates_set0).difference(two_candidates_set0))

            return edits

    class WxyzWing(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            return edits

    class AvoidableRectangleType1(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for upper_corner in list(puzzle.solved_cells()):
                for lower_corner in list(puzzle.solved_cells()):
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

                    opposite_candidates0 = puzzle.cell_candidates(temp_opposite[0])
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

    class SwordFish(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for candidate in puzzle.expected_candidates():
                for i in range(puzzle.length):
                    for ii in range(puzzle.length):
                        for iii in range(puzzle.length):
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
                for i in range(puzzle.length):
                    for ii in range(puzzle.length):
                        for iii in range(puzzle.length):
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

    class JellyFish(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            # row_dict = {}
            # col_dict = {}

            # for i in range(puzzle.length):
            #     row_dict[i] = 

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

    class HiddenSingleRobotFences:

        @staticmethod
        def get_required_candidates(puzzle: RobotFences, house: list[Loc]) -> list[int]:
            length = puzzle.length
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

                if len(fence_house) == puzzle.length:
                    edits += Techs.HiddenSingle.solve1(puzzle, fence_house)
                    continue

                #  get the solve candidates in the fence_house
                solved_candidates = [puzzle.cell_candidates(loc)[0] for loc in fence_house if
                                     len(puzzle.cell_candidates(loc)) == 1]

                if len(solved_candidates) == 0:
                    continue

                length = len(fence_house)

                minimum = min(solved_candidates)
                maximum = max(solved_candidates)

                temp_min = max([1, maximum - length + 1])
                temp_max = max([length, minimum + length - 1])

                expected_candidates = Techs.HiddenSingleRobotFences.get_required_candidates(puzzle, fence_house)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(expected_candidates))
                # print(candidates_to_remove)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(range(temp_min, temp_max + 1)))
                # print(candidates_to_remove)

                for loc in fence_house:
                    edits += puzzle.rem(loc, candidates_to_remove)

            return edits

    class WWing(BaseSudokuTechnique):
        def solve1(self, puzzle: Sudoku, left: Loc, right: Loc) -> int:
            edits = 0

            left_candidate_set = puzzle.cell_candidates(left)
            right_candidate_set = puzzle.cell_candidates(right)

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

            for r0 in range(puzzle.length):
                for c0 in range(puzzle.length):
                    loc0 = Loc(r0, c0)
                    candidates0 = puzzle.cell_candidates(loc0)

                    if len(candidates0) != 2:
                        continue

                    for r1 in range(puzzle.length):
                        for c1 in range(puzzle.length):
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

    class HiddenTriple(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            return 0

    class CrossHatchRows(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_rows():
                for loc0 in house:
                    for loc1 in house:
                        if loc0 == loc1:
                            continue

                        candidates = puzzle.cell_candidates(loc0)

                        if len(candidates) != 1:
                            continue

                        candiate = list(candidates)[0]

                        edits += puzzle.rem(loc1, [candiate])

            return edits

    class CrossHatchCols(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_cols():
                print(house)
                for loc0 in house:
                    for loc1 in house:
                        if loc0 == loc1:
                            continue

                        candidates = puzzle.cell_candidates(loc0)

                        if len(candidates) != 1:
                            continue

                        candiate = list(candidates)[0]

                        edits += puzzle.rem(loc1, [candiate])

            return edits

    class CrossHatchFences(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_fences():
                for loc0 in house:
                    for loc1 in house:
                        if loc0 == loc1:
                            continue

                        candidates = puzzle.cell_candidates(loc0)

                        if len(candidates) != 1:
                            continue

                        candiate = list(candidates)[0]

                        edits += puzzle.rem(loc1, [candiate])

            return edits

    class NakedQuad(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            return 0

    class AvoidableRectangleType2(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            return 0

    class CrossHatchCols(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_cols():
                print(house)
                for loc0 in house:
                    for loc1 in house:
                        if loc0 == loc1:
                            continue

                        candidates = puzzle.cell_candidates(loc0)

                        if len(candidates) != 1:
                            continue

                        candiate = list(candidates)[0]

                        edits += puzzle.rem(loc1, [candiate])

            return edits

    class HiddenSingleRows(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_rows():
                edits += Techs.HiddenSingle.solve1(puzzle, house)
            return edits

    class HiddenSingleCols(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_cols():
                edits += Techs.HiddenSingle.solve1(puzzle, house)
            return edits

    class HiddenSingleFences(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_fences():
                edits += Techs.HiddenSingle.solve1(puzzle, house)
            return edits

    class NakedPair:
        @staticmethod
        def solve1(puzzle: Sudoku, house: list[Loc]) -> int:
            edits = 0
            for i in range(puzzle.length):
                for ii in range(puzzle.length):
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

                    for j in range(puzzle.length):
                        if j not in index_set:
                            edits += puzzle.rem(house[j], list(candidate_set))
            return edits

        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0

            for house in puzzle.houses_rows_cols_fences():
                edits += Techs.NakedPair.solve1(puzzle, house)

            return edits

    class NakedPairFences(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_fences():
                edits += Techs.NakedPair.solve1(puzzle, house)
            return edits

    class NakedPairRows(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_rows():
                edits += Techs.NakedPair.solve1(puzzle, house)
            return edits

    class NakedPairCols(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_cols():
                edits += Techs.NakedPair.solve1(puzzle, house)
            return edits

    class ShashimiJellyFish(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class ShashimiSwordFish(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class ShashimiXWing(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FinnedJellyFish(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FinnedSwordFish(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FinnedXWing(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for index0 in range(puzzle.length):
                for index1 in range(puzzle.length):

                    col_house0 = puzzle.house_col(index0)
                    col_house1 = puzzle.house_col(index1)

                    row_house0 = puzzle.house_row(index0)
                    row_house1 = puzzle.house_row(index1)

                    for candidate in puzzle.expected_candidates():

                        row_house0_with_candidate = [loc for loc in row_house0 if
                                                     candidate in puzzle.cell_candidates(loc)]
                        row_house1_with_candidate = [loc for loc in row_house1 if
                                                     candidate in puzzle.cell_candidates(loc)]

                        row_locs_set = set(row_house0_with_candidate + row_house1_with_candidate)

                        fence_dict = puzzle.fence_dict(row_locs_set)

                        if len(fence_dict) != 4:
                            continue

                        fence_with_multiples = [fence for fence in fence_dict if len(fence_dict[fence]) > 1]

                        if len(fence_with_multiples) != 1:
                            continue

                        fence_with_fin = fence_with_multiples[0]

                        for loc in fence_dict[fence_with_fin]:
                            row_locs_set.remove(loc)

                        # need to find the two cells that are in the same col right now
                        loc0, loc1, loc2 = row_locs_set

                        col_set = None

                        if loc0.col == loc1.col:
                            col_set = set(puzzle.house_col(loc2.col)).difference([loc2])
                        elif loc0.col == loc2.col:
                            col_set = set(puzzle.house_col(loc1.col)).difference([loc1])
                        elif loc1.col == loc2.col:
                            col_set = set(puzzle.house_col(loc0.col)).difference([loc0])

                        fence_set = set(puzzle.house_fence(fence_with_fin)).difference(fence_dict[fence_with_fin])

                        if col_set is None or fence_set is None:
                            continue

                        intersection = col_set.intersection(fence_set)

                        for loc in intersection:
                            edits += puzzle.rem(loc, [candidate])

                    for candidate in puzzle.expected_candidates():

                        col_house0_with_candidate = [loc for loc in col_house0 if
                                                     candidate in puzzle.cell_candidates(loc)]
                        col_house1_with_candidate = [loc for loc in col_house1 if
                                                     candidate in puzzle.cell_candidates(loc)]

                        col_locs_set = set(col_house0_with_candidate + col_house1_with_candidate)

                        fence_dict = puzzle.fence_dict(col_locs_set)

                        if len(fence_dict) != 4:
                            continue

                        fence_with_multiples = [fence for fence in fence_dict if len(fence_dict[fence]) > 1]

                        if len(fence_with_multiples) != 1:
                            continue

                        fence_with_fin = fence_with_multiples[0]

                        for loc in fence_dict[fence_with_fin]:
                            col_locs_set.remove(loc)

                        # need to find the two cells that are in the same row right now
                        loc0, loc1, loc2 = col_locs_set

                        row_set = None

                        if loc0.row == loc1.row:
                            row_set = set(puzzle.house_row(loc2.row)).difference([loc2])
                        elif loc0.row == loc2.row:
                            row_set = set(puzzle.house_row(loc1.row)).difference([loc1])
                        elif loc1.row == loc2.row:
                            row_set = set(puzzle.house_row(loc0.row)).difference([loc0])

                        fence_set = set(puzzle.house_fence(fence_with_fin)).difference(fence_dict[fence_with_fin])

                        if row_set is None or fence_set is None:
                            continue

                        intersection = row_set.intersection(fence_set)

                        # if intersection is not None:

                        for loc in intersection:
                            edits += puzzle.rem(loc, [candidate])

            return edits

    class AlmostLockedCandidatesClaiming(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class AlmostLockedCandidatesPointing(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class HiddenUniqueRectangle(BaseSudokuTechnique):
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
                    all_temp = all([puzzle.cell_candidates(loc).issuperset(corner0_candidates) for loc in
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

    class UniqueRectangleType3(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class XyzWing(BaseSudokuTechnique):
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0

            for pivot in puzzle.unsolved_cells():
                pivot_candidates = puzzle.cell_candidates(pivot)

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

                        if loc_in_row_candidates.issuperset(loc_in_fence_candidates):
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

                        if loc_in_col_candidates.issuperset(loc_in_fence_candidates):
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

    class XChain(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class XyChain(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class FishyCycle(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class SimpleColoring(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class SueDeCoq(BaseSudokuTechnique):

        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            return edits

    class KropkiBlack(BasePuzzleTechnique):
        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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

    class KropkiWhite(BasePuzzleTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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

    class KropkiEmpty(BasePuzzleTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            # print("in here")
            edits = 0
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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

    class KropkiWw(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiBb(BaseKropkiTechnique):

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

    class KropkiDominatingEmpty(BaseKropkiTechnique):

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

    class KropkiBw(BaseKropkiTechnique):

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

    class KropkiHiddenSingle(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiHiddenPair(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiHiddenTriple(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiHiddenQuad(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiNakedPair(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiNakedTriple(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiNakedQuad(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiLockedCandidatesPointing(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class KropkiLockedCandidatesClaiming(BaseKropkiTechnique):

        def solve0(self, puzzle: Kropki) -> int:
            edits = 0
            return edits

    class MagnetsZero(BaseMagnetsTechnique):
        def solve0(self, puzzle: Magnets) -> int:
            edits = 0

            for i in range(puzzle.length):
                plus_row_value = puzzle.plus_row_value(i)
                row_house = puzzle.house_row(i)

                if plus_row_value == 0:
                    for loc in row_house:
                        edits += puzzle.rem([loc], [PLUS])

                plus_col_value = puzzle.plus_col_value(i)
                col_house = puzzle.house_col(i)

                if plus_col_value == 0:
                    for loc in col_house:
                        edits += puzzle.rem([loc], [PLUS])

                minus_row_value = puzzle.minus_row_value(i)

                row_house = puzzle.house_row(i)

                if minus_row_value == 0:
                    for loc in row_house:
                        edits += puzzle.rem([loc], [MINUS])

                minus_col_value = puzzle.minus_col_value(i)
                col_house = puzzle.house_col(i)
                print(minus_col_value)
                if minus_col_value == 0:
                    for loc in col_house:
                        edits += puzzle.rem([loc], [MINUS])

            return edits

    class MagnetsFullHouse(BaseMagnetsTechnique):
        def solve0(self, puzzle: Magnets) -> int:
            edits = 0

            for i in range(puzzle.length):
                plus_row_value = puzzle.plus_row_value(i)
                minus_row_value = puzzle.minus_row_value(i)
                row_house = puzzle.house_row(i)

                if plus_row_value + minus_row_value == puzzle.length:
                    edits += puzzle.rem(row_house, [EMPTY])

                plus_col_value = puzzle.plus_col_value(i)
                minus_col_value = puzzle.minus_col_value(i)
                col_house = puzzle.house_col(i)

                if plus_col_value + minus_col_value == puzzle.length:
                    edits += puzzle.rem(col_house, [EMPTY])

            return edits

    class MagnetsPair(BaseMagnetsTechnique):

        def solve1(self, puzzle: Magnets, loc0: Loc, loc1: Loc) -> int:
            edits = 0
            candidates0 = puzzle.cell_candidates(loc0)
            candidates1 = puzzle.cell_candidates(loc1)

            if EMPTY not in candidates0:
                edits += puzzle.rem([loc1], [EMPTY])

            if EMPTY not in candidates1:
                edits += puzzle.rem([loc0], [EMPTY])

            if PLUS not in candidates0:
                edits += puzzle.rem([loc1], [MINUS])

            if PLUS not in candidates1:
                edits += puzzle.rem([loc0], [MINUS])

            if MINUS not in candidates0:
                edits += puzzle.rem([loc1], [PLUS])

            if MINUS not in candidates1:
                edits += puzzle.rem([loc0], [PLUS])

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

    class KropkiDiamondEbww(BaseKropkiTechnique):
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

    class KropkiDiamondWwwe(BaseKropkiTechnique):
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

    class TennerCrossHatch(BasePuzzleTechnique):
        # def __repr__(self)->str:
        #     return f'{self.__class__.__name__}()'

        def solve0(self, puzzle: Tenner) -> int:
            edits = 0

            for r in range(puzzle.length):
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
                        if direction.row >= puzzle.length or direction.col >= 10:
                            continue
                        edits += puzzle.rem([direction], [solved_candidate])
            return edits

    class TennerTotalHiddenSingle(BasePuzzleTechnique):
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

    class TennerHiddenSingle(BasePuzzleTechnique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for row in range(puzzle.length):
                house = puzzle.house_row_cell_locs(row)
                edits += Techs.HiddenSingle.solve1(puzzle, house)
            return edits

    class TennerNakedPair(BasePuzzleTechnique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for row in range(puzzle.length):
                house = puzzle.house_row_cell_locs(row)
                edits += Techs.NakedPair.solve1(puzzle, house)
            return edits

    class TennerHiddenPair(BasePuzzleTechnique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for index in range(puzzle.length):
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

    class TennerNakedPairColumn(BasePuzzleTechnique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)

                for index in range(puzzle.length - 1):
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

    class TennerPowerSetTotals(BasePuzzleTechnique):
        def solve0(self, puzzle: Tenner) -> int:
            edits = 0
            edits = self.solve3(puzzle)
            edits += self.solve4(puzzle)
            edits += self.solve5(puzzle)
            edits += self.solve6(puzzle)
            return edits

        # class TennerPowerSetTotals3(BasePuzzleTechnique):
        def solve3(self, puzzle: Tenner) -> int:
            edits = 0
            TOTAL = 3
            if puzzle.length != TOTAL:
                return edits
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)
                total = puzzle.total(col)
                if total is None:
                    continue
                valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            candidates = [candidate0, candidate1, candidate2]
                            self.mid(puzzle, valid_candidates_dict, candidates, house, total)
                edits += self.end(puzzle, valid_candidates_dict, house)
            return edits

        def solve4(self, puzzle: Tenner) -> int:
            edits = 0
            TOTAL = 4
            if puzzle.length != TOTAL:
                return edits
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)
                total = puzzle.total(col)
                if total is None:
                    continue
                valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            for candidate3 in puzzle.cell_candidates(house[3]):
                                candidates = [candidate0, candidate1, candidate2, candidate3]
                                self.mid(puzzle, valid_candidates_dict, candidates, house, total)
                edits += self.end(puzzle, valid_candidates_dict, house)
            return edits

        # class TennerPowerSetTotals5(BasePuzzleTechnique):
        def solve5(self, puzzle: Tenner) -> int:
            edits = 0
            TOTAL = 5
            if puzzle.length != TOTAL:
                return edits
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)
                total = puzzle.total(col)
                if total is None:
                    continue
                valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            for candidate3 in puzzle.cell_candidates(house[3]):
                                for candidate4 in puzzle.cell_candidates(house[4]):
                                    candidates = [candidate0, candidate1, candidate2, candidate3, candidate4]
                                    self.mid(puzzle, valid_candidates_dict, candidates, house, total)
                edits += self.end(puzzle, valid_candidates_dict, house)
            return edits

        # class TennerPowerSetTotals6(BasePuzzleTechnique):
        def solve6(self, puzzle: Tenner) -> int:
            edits = 0
            TOTAL = 6
            if puzzle.length != TOTAL:
                return edits
            for col in range(puzzle.col_length):
                house = puzzle.house_col_cell_locs(col)
                total = puzzle.total(col)
                if total is None:
                    continue
                valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
                for candidate0 in puzzle.cell_candidates(house[0]):
                    for candidate1 in puzzle.cell_candidates(house[1]):
                        for candidate2 in puzzle.cell_candidates(house[2]):
                            for candidate3 in puzzle.cell_candidates(house[3]):
                                for candidate4 in puzzle.cell_candidates(house[4]):
                                    for candidate5 in puzzle.cell_candidates(house[5]):
                                        candidates = [candidate0, candidate1, candidate2, candidate3, candidate4,
                                                      candidate5]
                                        self.mid(puzzle, valid_candidates_dict, candidates, house, total)
                edits += self.end(puzzle, valid_candidates_dict, house)

            return edits

        def mid(self, puzzle, valid_candidates_dict, candidates, house, total):
            if sum(candidates) != total:
                return
            is_valid_column = [candidates[index] != candidates[index + 1] for index in
                               range(puzzle.length - 1)]
            if not all(is_valid_column):
                return
            for index in range(puzzle.length):
                valid_candidates_dict[house[index]].add(candidates[index])

        def end(self, puzzle: Tenner, valid_candidates_dict, house) -> int:
            edits = 0
            for index in range(puzzle.length):
                edits += puzzle.rem([house[index]],
                                    list(set(puzzle.expected_candidates()).difference(
                                        valid_candidates_dict[house[index]])))
            return edits

    class Parks1CrossHatchTouching(BasePuzzleTechnique):

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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

    class Parks1CrossHatch(BasePuzzleTechnique):

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            houses = []
            fence_dict = {}
            for r in range(puzzle.length):
                for c in range(puzzle.length):
                    loc = Loc(r, c)
                    fence = puzzle.cell_fence(loc)

                    if fence not in fence_dict:
                        fence_dict[fence] = []

                    fence_dict[fence].append(loc)

            for fence in fence_dict.keys():
                houses.append(fence_dict[fence])

            for row in range(puzzle.length):
                house = []
                for col in range(puzzle.length):
                    house.append(Loc(row, col))
                houses.append(house)
            for col in range(puzzle.length):
                house = []
                for row in range(puzzle.length):
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

    class Parks1HiddenSingle(BasePuzzleTechnique):

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fence_dict = {}
            # for house in puzzle.
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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

    class Parks1LockedCandidatesPointing(BasePuzzleTechnique):

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fence_dict = {}

            # for house in puzzle.
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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
                if len(unsolved) == 2:
                    rows = set([loc.row for loc in unsolved])
                    cols = set([loc.col for loc in unsolved])
                    if len(rows) == 1:
                        temp = set(puzzle.house_row(rows.pop())).difference(unsolved)
                        edits += puzzle.rem(list(temp), [1])
                    if len(cols) == 1:
                        temp = set(puzzle.house_col(cols.pop())).difference(unsolved)
                        edits += puzzle.rem(list(temp), [1])
            return edits

    class Parks1Bent3(BasePuzzleTechnique):

        def solve0(self, puzzle: Parks1) -> int:
            edits = 0
            fence_dict = {}
            for r in range(puzzle.length):
                for c in range(puzzle.length):
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

                    # south east
                    if unsolved.issuperset([pivot.east(), pivot.south()]):
                        remove = [pivot.south().east()]

                        if pivot.north().is_valid_parks(puzzle.grid):
                            remove.append(pivot.north())

                        edits += puzzle.rem(remove, [1])

            return edits

    class Parks1Shape_00_01(BasePuzzleTechnique):
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

            return edits

    class RobotCrosswordsHouses:  # (BasePuzzleTechnique):
        def solve0(self, puzzle: RobotCrosswords) -> int:
            edits = 0

            houses = []

            for row in range(puzzle.length):
                house = []
                for col in range(puzzle.length):
                    house.append(Loc(row, col))
                houses.append(house)

            for col in range(puzzle.length):
                house = []
                for row in range(puzzle.length):
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

    class PowerGridTech:
        def solve0(self, puzzle: PowerGrid) -> int:
            edits = 0

            for index in range(puzzle.length):
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

            for index in range(puzzle.length):
                left_index = index - power - 1
                right_index = index + power + 1

                # valid_left =

                if left_index < 0 and right_index >= puzzle.length:
                    edits += puzzle.rem([house[index]], [POWER])

                if left_index < 0 and right_index < puzzle.length and POWER not in puzzle.cell_candidates(
                        house[right_index]):
                    edits += puzzle.rem([house[index]], [POWER])

                if left_index >= 0 and right_index >= puzzle.length and POWER not in puzzle.cell_candidates(
                        house[left_index]):
                    edits += puzzle.rem([house[index]], [POWER])

                if left_index >= 0 and right_index < puzzle.length and POWER not in puzzle.cell_candidates(
                        house[left_index]) and POWER not in puzzle.cell_candidates(house[right_index]):
                    edits += puzzle.rem([house[index]], [POWER])

            return edits

    class PowerGridHiddenPower:
        def solve0(self, puzzle: PowerGrid) -> int:
            edits = 0

            for index in range(puzzle.length):
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

            #     left_index = index - power - 1
            #     right_index = index + power + 1
            #
            #     # valid_left =
            #
            #     if left_index < 0 and right_index >= puzzle.length:
            #         edits += puzzle.rem([house[index]], [POWER])
            #
            #     if left_index < 0 and right_index < puzzle.length and POWER not in puzzle.cell_candidates(house[right_index]):
            #         edits += puzzle.rem([house[index]], [POWER])
            #
            #     if left_index >= 0 and right_index >= puzzle.length and POWER not in puzzle.cell_candidates(house[left_index]):
            #         edits += puzzle.rem([house[index]], [POWER])
            #
            #     if left_index >= 0 and right_index < puzzle.length and POWER not in puzzle.cell_candidates(house[left_index]) and POWER not in puzzle.cell_candidates(house[right_index]):
            #         edits += puzzle.rem([house[index]], [POWER])

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

    class FutoshikiCrossHatch:  # (BaseFutoshikiTechnique):
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0
            return edits

    class FutoshikiHiddenSingle:  # (BaseFutoshikiTechnique):
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0
            return edits

    class MathraxCrossHatch:

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            return edits

    class MathraxHiddenSingle:

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            return edits

    class CrossHatchSumscrapers(BasePuzzleTechnique):
        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0
            houses = []
            for index in range(puzzle.length):
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

    class HiddenSingleSumscrapers(BasePuzzleTechnique):
        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0
            houses = []
            for index in range(puzzle.length):
                houses.append(puzzle.house_row(index))
                houses.append(puzzle.house_col(index))

            for house in houses:
                candidate_dict = {}
                for index in range(puzzle.length):
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

    class SumscrapersLastIsMax(BasePuzzleTechnique):

        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(puzzle.length):
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

                candidates_n = puzzle.cell_candidates(house[puzzle.length - 1])

                if len(candidates_n) != 1:
                    continue
                if candidates_n[0] != puzzle.length:
                    continue

                difference = scraper - puzzle.length

                expected = set(puzzle.expected_candidates())

                expected.remove(puzzle.length)

                max0 = max(expected)

                if scraper == max0 + puzzle.length:
                    edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([max0]))
                else:
                    edits += puzzle.rem([house[0]], [max0])
                # print(scraper)
                # print(house)
            return edits

    class SumscrapersNextToScraper(BasePuzzleTechnique):

        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(puzzle.length):
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

                if scraper > puzzle.length:
                    edits += puzzle.rem([house[0]], [puzzle.length])

            return edits

    class SumscrapersSecondInLine(BasePuzzleTechnique):

        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(puzzle.length):
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
                if candidates1[0] != puzzle.length:
                    continue
                difference = scraper - puzzle.length

                edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([difference]))

                print(scraper)
                print(house)
            return edits

    class SumscrapersTech(BasePuzzleTechnique):
        def solve0(self, puzzle: Sumscrapers) -> int:
            edits = 0

            for index in range(puzzle.length):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == puzzle.length:
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference([puzzle.length]))

                if south == puzzle.length:
                    edits += puzzle.rem([Loc(puzzle.length - 1, index)],
                                        set(puzzle.expected_candidates()).difference([puzzle.length]))

                if east == puzzle.length:
                    edits += puzzle.rem([Loc(index, puzzle.length - 1)],
                                        set(puzzle.expected_candidates()).difference([puzzle.length]))
                #
                if west == puzzle.length:
                    edits += puzzle.rem([Loc(index, 0)],
                                        set(puzzle.expected_candidates()).difference([puzzle.length]))

                total = sum(puzzle.expected_candidates())

                if south == total:
                    expected = set(puzzle.expected_candidates())
                    current = Loc(puzzle.length - 1, index)
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
                    current = Loc(0, puzzle.length - 1)
                    while len(expected) > 0:
                        min0 = min(expected)
                        # print(min0)
                        edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                        expected.remove(min0)
                        current = current.west()

            return edits

    class SkyscrapersN(BasePuzzleTechnique):
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(puzzle.length):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == puzzle.length:
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if south == puzzle.length:
                    edits += puzzle.rem([Loc(puzzle.length - 1, index)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if west == puzzle.length:
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if east == puzzle.length:
                    edits += puzzle.rem([Loc(index, puzzle.length - 1)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

            return edits

    class Skyscrapers1(BasePuzzleTechnique):
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(puzzle.length):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == 1:
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if south == 1:
                    edits += puzzle.rem([Loc(puzzle.length - 1, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if west == 1:
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if east == 1:
                    edits += puzzle.rem([Loc(index, puzzle.length - 1)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

            return edits

    class SkyscrapersRange(BasePuzzleTechnique):
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0
            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(puzzle.length):
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
# 2865
