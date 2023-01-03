from _puzzles import Tenner


class TennerNakedPairColumn:
    def solve0(self, puzzle: Tenner) -> int:
        edits = 0
        for col in range(puzzle.col_length):
            house = puzzle.house_col_cell_locs(col)

            for index in range(puzzle.length - 1):
                loc0 = house[index]
                loc1 = house[index + 1]

                loc0_candidates = set(puzzle.cell_candidates(loc0))
                loc1_candidates = set(puzzle.cell_candidates(loc1))

                if len(loc0_candidates) != 2:
                    continue

                if not loc1_candidates.issuperset(loc0_candidates) or not loc0_candidates.issuperset(
                        loc1_candidates):
                    continue

                directions = [
                    loc0.west(),
                    loc0.east(),
                    loc1.west(),
                    loc1.east(),
                ]

                for direction in directions:
                    if direction.col < 0 or direction.col >= puzzle.col_length:
                        continue
                    edits += puzzle.rem([direction], loc0_candidates)

        return edits
