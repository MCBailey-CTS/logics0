import itertools
from abc import abstractmethod

from techniques.Technique import Technique
from Loc import Loc


# class TennerPowerSetTotals(Technique):
#     def solve0(self, puzzle: Tenner) -> int:
#         edits = 0
#         for col in range(puzzle.col_length):
#             house = puzzle.house_col_cell_locs(col)
#             total = puzzle.total(col)
#             edits += self.solve1(puzzle, house, total)
#         return edits
#
#     def solve1(self, puzzle: Tenner, house: list[Loc], total: Optional[int]) -> int:
#         edits = 0
#         if total is None:
#             return edits
#         valid_candidates_dict = {house[i]: set() for i in range(len(puzzle))}
#         for candidates in tech.TennerPowerSetTotals.power_set_candidates(puzzle, house):
#             self.mid(puzzle, valid_candidates_dict, candidates, house, total)
#         edits += self.end(puzzle, valid_candidates_dict, house)
#         return edits
#
#     @staticmethod
#     def mid(puzzle, valid_candidates_dict, candidates, house, total):
#         if sum(candidates) != total:
#             return
#         is_valid_column = [candidates[index] != candidates[index + 1] for index in
#                            range(len(puzzle) - 1)]
#         if not all(is_valid_column):
#             return
#         for index in range(len(puzzle)):
#             valid_candidates_dict[house[index]].add(candidates[index])
#
#     @staticmethod
#     def end(puzzle: Tenner, valid_candidates_dict, house) -> int:
#         edits = 0
#         for index in range(len(puzzle)):
#             edits += puzzle.rem([house[index]],
#                                 list(set(puzzle.expected_candidates()).difference(
#                                     valid_candidates_dict[house[index]])))
#         return edits
#
#     @staticmethod
#     def power_set_candidates(puzzle: Tenner, house: list[Loc]):
#         if len(house) == 3:
#             for candidate0 in puzzle.cell_candidates(house[0]):
#                 for candidate1 in puzzle.cell_candidates(house[1]):
#                     for candidate2 in puzzle.cell_candidates(house[2]):
#                         yield [candidate0, candidate1, candidate2]
#         if len(house) == 4:
#             for candidate0 in puzzle.cell_candidates(house[0]):
#                 for candidate1 in puzzle.cell_candidates(house[1]):
#                     for candidate2 in puzzle.cell_candidates(house[2]):
#                         for candidate3 in puzzle.cell_candidates(house[3]):
#                             yield [candidate0, candidate1, candidate2, candidate3]
#         if len(house) == 5:
#             for candidate0 in puzzle.cell_candidates(house[0]):
#                 for candidate1 in puzzle.cell_candidates(house[1]):
#                     for candidate2 in puzzle.cell_candidates(house[2]):
#                         for candidate3 in puzzle.cell_candidates(house[3]):
#                             for candidate4 in puzzle.cell_candidates(house[4]):
#                                 yield [candidate0, candidate1, candidate2, candidate3, candidate4]
#         if len(house) == 6:
#             for candidate0 in puzzle.cell_candidates(house[0]):
#                 for candidate1 in puzzle.cell_candidates(house[1]):
#                     for candidate2 in puzzle.cell_candidates(house[2]):
#                         for candidate3 in puzzle.cell_candidates(house[3]):
#                             for candidate4 in puzzle.cell_candidates(house[4]):
#                                 for candidate5 in puzzle.cell_candidates(house[5]):
#                                     yield [candidate0, candidate1, candidate2, candidate3, candidate4,
#                                            candidate5]


class BaseRobotCrosswordsTech(Technique):
    @abstractmethod
    def solve1(self, puzzle, house: list[Loc]) -> int:
        raise NotImplementedError()

    def solve0(self, puzzle) -> int:
        edits = 0
        for i in range(len(puzzle)):

            for house in [puzzle.house_row(i), puzzle.house_col(i)]:
                actual_cells = set(
                    [loc for index, loc in enumerate(house) if 'x' not in puzzle.grid[loc.row][loc.col]])
                house_chunks = []
                while len(actual_cells) > 0:
                    current = actual_cells.pop()
                    current_set = {current}

                    for other in list(actual_cells):
                        if any(other.is_next_to(loc) for loc in current_set):
                            actual_cells.remove(other)
                            current_set.add(other)
                    if len(current_set) > 1:
                        house_chunks.append(current_set)
                for house0 in house_chunks:
                    edits += self.solve1(puzzle, list(house0))

        return edits


class RobotCrosswordsTech(BaseRobotCrosswordsTech):
    def solve1(self, puzzle, house: list[Loc]) -> int:
        edits = 0

        for loc0 in house:
            __candidates = puzzle.cell_candidates(loc0)
            if len(__candidates) != 1:
                continue
            for loc1 in house:
                if loc1 == loc0:
                    continue
                edits += puzzle.rem([loc1], [__candidates[0]])

        return edits


class RobotCrosswordsPowerSet(BaseRobotCrosswordsTech):
    def solve1(self, puzzle, house: list[Loc]) -> int:
        edits = 0

        house_set = set(house)

        if puzzle.id() == "004.robot_crosswords" and \
                not (
                        house_set == {Loc(0, 0), Loc(0, 1)}
                        or
                        house_set == {Loc(0, 3), Loc(1, 3)}
                        or
                        house_set == {Loc(2, 0), Loc(2, 1), Loc(2, 2)}
                        or
                        house_set == {Loc(1, 2), Loc(1, 3), Loc(1, 4)}
                        or
                        house_set == {Loc(3, 0), Loc(3, 1), Loc(3, 2), Loc(3, 3)}
                        or
                        house_set == {Loc(0, 0), Loc(1, 0), Loc(2, 0), Loc(3, 0)}
                ):
            return edits

        # if not (house_set == {Loc(0, 0), Loc(1, 0), Loc(2, 0)} or
        #         house_set == {Loc(1, 0), Loc(1, 1), Loc(1, 2), Loc(1, 3)}):
        #     return edits

        house_candidates = [puzzle.cell_candidates(loc) for _, loc in enumerate(house)]

        candidate_dict = {}

        for index in range(len(house)):
            candidate_dict[index] = set(candidate for candidate in [1, 2, 3, 4, 5, 6, 7, 8, 9])

        for candidates in list(itertools.product(*house_candidates)):
            candidate_set = set(candidates)

            if len(candidate_set) != len(house):
                continue

            __sorted = sorted(candidate_set)

            if not all(__sorted[i] + 1 == __sorted[i + 1] for i in range(len(house) - 1)):
                continue

            for index in range(len(house)):
                candidate_dict[index].discard(candidates[index])

        for index, loc in enumerate(house):
            edits += puzzle.rem([loc], list(candidate_dict[index]))

        return edits
