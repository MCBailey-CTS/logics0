from Loc import Loc
from puzzles import Kropki


class KropkiBlack:
    def solve0(self, puzzle: Kropki) -> int:
        edits = 0
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
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
