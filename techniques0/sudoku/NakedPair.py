from Loc import Loc
from _puzzles import Sudoku


class NakedPair:
    @staticmethod
    def solve1(puzzle: Sudoku, house: list[Loc]) -> int:
        edits = 0
        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits
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
            edits += NakedPair.solve1(puzzle, house)

        return edits

