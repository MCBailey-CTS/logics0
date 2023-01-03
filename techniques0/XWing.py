from Loc import Loc
from _puzzles import Sudoku


class XWing:
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


