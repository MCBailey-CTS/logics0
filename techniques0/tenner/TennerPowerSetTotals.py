from typing import Optional

from Loc import Loc
from _puzzles import Tenner
from techniques0 import *


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
        valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
        for candidates in TennerPowerSetTotals.power_set_candidates(puzzle, house):
            self.mid(puzzle, valid_candidates_dict, candidates, house, total)
        edits += self.end(puzzle, valid_candidates_dict, house)
        return edits

    @staticmethod
    def mid(puzzle, valid_candidates_dict, candidates, house, total):
        if sum(candidates) != total:
            return
        is_valid_column = [candidates[index] != candidates[index + 1] for index in
                           range(puzzle.length - 1)]
        if not all(is_valid_column):
            return
        for index in range(puzzle.length):
            valid_candidates_dict[house[index]].add(candidates[index])

    @staticmethod
    def end(puzzle: Tenner, valid_candidates_dict, house) -> int:
        edits = 0
        for index in range(puzzle.length):
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
