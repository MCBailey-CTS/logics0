from puzzles import RobotFences
from Loc import Loc
from techniques.HiddenSingle import HiddenSingle
from techniques.Technique import Technique


class HiddenSingleRobotFences(Technique):

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

    def solve0(self, puzzle: RobotFences) -> int:
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
                edits += HiddenSingle.solve1(puzzle, fence_house)
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

            expected_candidates = HiddenSingleRobotFences.get_required_candidates(puzzle, fence_house)

            candidates_to_remove = list(set(puzzle.expected_candidates()).difference(expected_candidates))
            # print(candidates_to_remove)

            candidates_to_remove = list(set(puzzle.expected_candidates()).difference(range(temp_min, temp_max + 1)))
            # print(candidates_to_remove)

            for loc in fence_house:
                edits += puzzle.rem(loc, candidates_to_remove)

        return edits
