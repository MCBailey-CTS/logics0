from _puzzles import Sudoku


class JellyFish:

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        for candidate in puzzle.expected_candidates():
            for i in range(0, 6):
                for ii in range(i + 1, 7):
                    for iii in range(ii + 1, 8):
                        for iiii in range(iii + 1, 9):
                            if len({i, ii, iii, iiii}) != 4:
                                continue

                            locs0 = [loc for loc in puzzle.house_row(i) if candidate in puzzle.cell_candidates(loc)]
                            locs1 = [loc for loc in puzzle.house_row(ii) if
                                     candidate in puzzle.cell_candidates(loc)]
                            locs2 = [loc for loc in puzzle.house_row(iii) if
                                     candidate in puzzle.cell_candidates(loc)]
                            locs3 = [loc for loc in puzzle.house_row(iiii) if
                                     candidate in puzzle.cell_candidates(loc)]

                            loc_set = set(locs0 + locs1 + locs2 + locs3)

                            cols = set([loc.col for loc in loc_set])

                            has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                            if any(has_solved_candidate):
                                continue

                            if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                                continue

                            if len(cols) != 4:
                                continue

                            edits += self.new_method(puzzle, candidate, locs0, locs1, locs2, locs3, cols)

        for candidate in puzzle.expected_candidates():
            for i in range(0, 6):
                for ii in range(i + 1, 7):
                    for iii in range(ii + 1, 8):
                        for iiii in range(iii + 1, 9):
                            if len({i, ii, iii, iiii}) != 4:
                                continue

                            locs0 = [loc for loc in puzzle.house_col(i) if candidate in puzzle.cell_candidates(loc)]
                            locs1 = [loc for loc in puzzle.house_col(ii) if
                                     candidate in puzzle.cell_candidates(loc)]
                            locs2 = [loc for loc in puzzle.house_col(iii) if
                                     candidate in puzzle.cell_candidates(loc)]
                            locs3 = [loc for loc in puzzle.house_col(iiii) if
                                     candidate in puzzle.cell_candidates(loc)]

                            loc_set = set(locs0 + locs1 + locs2 + locs3)

                            rows = set([loc.row for loc in loc_set])

                            has_solved_candidate = [len(puzzle.cell_candidates(loc)) == 1 for loc in loc_set]

                            if any(has_solved_candidate):
                                continue

                            if len(locs0) < 2 or len(locs1) < 2 or len(locs2) < 2:
                                continue

                            if len(rows) != 4:
                                continue

                            edits += self.new_method1(puzzle, candidate, locs0, locs1, locs2, locs3, rows)

        return edits

    def new_method1(self, puzzle, candidate, locs0, locs1, locs2, locs3, rows):
        edits = 0
        for row in rows:
            row_set = set(puzzle.house_row(row))
            for loc in row_set.difference(locs0 + locs1 + locs2 + locs3):
                edits += puzzle.rem(loc, [candidate])
        return edits

    def new_method(self, puzzle, candidate, locs0, locs1, locs2, locs3, cols):
        edits = 0
        for col in cols:
            col_set = set(puzzle.house_col(col))
            for loc in col_set.difference(locs0 + locs1 + locs2 + locs3):
                edits += puzzle.rem(loc, [candidate])
        return edits
