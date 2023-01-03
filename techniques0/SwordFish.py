from _puzzles import Sudoku


class SwordFish:

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        for candidate in puzzle.expected_candidates():
            for i in range(puzzle.length):
                for ii in range(puzzle.length):
                    for iii in range(puzzle.length):
                        if len({i, ii, iii}) != 3:
                            continue

                        locs0 = [loc for loc in puzzle.house_row(i) if candidate in puzzle.cell_candidates(loc)]
                        locs1 = [loc for loc in puzzle.house_row(ii) if candidate in puzzle.cell_candidates(loc)]
                        locs2 = [loc for loc in puzzle.house_row(iii) if candidate in puzzle.cell_candidates(loc)]

                        loc_set = set(locs0 + locs1 + locs2)

                        rows = set([loc.col for loc in loc_set])

                        has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                        if any(has_solved_candidate):
                            continue

                        if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                            continue

                        if len(rows) != 3:
                            continue

                        for row in rows:
                            row_set = set(puzzle.house_col(row))
                            for loc in row_set.difference(locs0 + locs1 + locs2):
                                edits += puzzle.rem(loc, [candidate])

        for candidate in puzzle.expected_candidates():
            for i in range(puzzle.length):
                for ii in range(puzzle.length):
                    for iii in range(puzzle.length):
                        if len({i, ii, iii}) != 3:
                            continue

                        locs0 = [loc for loc in puzzle.house_col(i) if candidate in puzzle.cell_candidates(loc)]
                        locs1 = [loc for loc in puzzle.house_col(ii) if candidate in puzzle.cell_candidates(loc)]
                        locs2 = [loc for loc in puzzle.house_col(iii) if candidate in puzzle.cell_candidates(loc)]

                        loc_set = set(locs0 + locs1 + locs2)

                        rows = set([loc.row for loc in loc_set])

                        has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                        if any(has_solved_candidate):
                            continue

                        if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                            continue

                        if len(rows) != 3:
                            continue

                        for row in rows:
                            row_set = set(puzzle.house_row(row))
                            for loc in row_set.difference(locs0 + locs1 + locs2):
                                edits += puzzle.rem(loc, [candidate])

        return edits

