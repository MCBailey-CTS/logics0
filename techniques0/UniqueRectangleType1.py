from Loc import Loc
from _puzzles import Sudoku


class UniqueRectangleType1:
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

