from puzzles import Sudoku


class RobotFences(Sudoku):
    def __init__(self, puzzle: str) -> None:
        Sudoku.__init__(self, puzzle)

    def is_solved(self) -> bool:
        for house in self.houses_rows_cols():
            solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
                                 len(self.cell_candidates(loc)) == 1]

            if len(solved_candidates) != len(self):
                print("row or column wasn't completely solved")
                return False

            expected = set(self.expected_candidates())

            if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
                continue

            return False

        for house in self.houses_fences():
            solved_candidates = [list(self.cell_candidates(house[index]))[0] for index in range(len(house))]

            solved_candidates.sort()

            if len(solved_candidates) == 1:
                continue
            for index in range(len(house) - 1):
                if solved_candidates[index] + 1 != solved_candidates[index + 1]:
                    print("Fence house not solved")
                    return False

        return True
