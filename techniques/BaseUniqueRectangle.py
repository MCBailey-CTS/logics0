from Loc import Loc
from abc import abstractmethod

from tests_files.test_sudoku import Sudoku


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

                temp_edits = self.solve_rectangle(puzzle, list(corners))

                if temp_edits > 0:
                    return temp_edits

                # edits += self.solve_rectangle(puzzle, list(corners))
        return edits
