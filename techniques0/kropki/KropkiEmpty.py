from Loc import Loc
from puzzles import Kropki


class KropkiEmpty:

    def solve0(self, puzzle: Kropki) -> int:
        # print("in here")
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

                    empty = [s == "." for s in puzzle.grid[center.row][center.col]]

                    if not all(empty):
                        continue

                    edits += self.solve1(puzzle, loc, other)
        return edits

    def solve1(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
        return self.solve2(puzzle, loc0, loc1) + self.solve2(puzzle, loc1, loc0)

    def solve2(self, puzzle: Kropki, loc0: Loc, loc1: Loc) -> int:
        edits = 0

        loc0_candidates = puzzle.cell_candidates(loc0)

        if len(loc0_candidates) != 1:
            return edits

        candidate = loc0_candidates[0]

        candidates_to_remove = [candidate + 1, candidate - 1, candidate * 2, candidate]

        if candidate % 2 == 0:
            candidates_to_remove.append(int(candidate / 2))

        edits += puzzle.rem([loc1], candidates_to_remove)

        return edits

