from puzzles import Sudoku
from Loc import Loc
class HiddenSingle:
        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0

            unsolved = puzzle.unsolved_cells()

            if len(unsolved) == 0:
                return edits

            for house in puzzle.houses_rows_cols_fences():
                edits += HiddenSingle.solve1(puzzle, house)
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

