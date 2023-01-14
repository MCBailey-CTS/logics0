from abc import abstractmethod
from techniques0.Technique import Technique
from Loc import Loc
from puzzles import Tenner


class TennerCrossHatch(Technique):

    def solve0(self, puzzle: Tenner) -> int:
        edits = 0

        for r in range(len(puzzle)):
            for c in range(puzzle.col_length):
                cell = Loc(r, c)
                candidates = puzzle.cell_candidates(cell)
                if len(candidates) != 1:
                    continue
                solved_candidate = candidates[0]

                for c0 in range(puzzle.col_length):
                    if c0 == c:
                        continue
                    edits += puzzle.rem([Loc(r, c0)], [solved_candidate])
                directions = [
                    cell.north(),
                    cell.east(),
                    cell.south(),
                    cell.west(),
                    cell.north().east(),
                    cell.north().west(),
                    cell.south().east(),
                    cell.south().west()
                ]
                for direction in directions:
                    if direction.row < 0 or direction.col < 0:
                        continue
                    if direction.row >= len(puzzle) or direction.col >= 10:
                        continue
                    edits += puzzle.rem([direction], [solved_candidate])
        return edits
