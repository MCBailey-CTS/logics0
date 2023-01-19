from puzzles import Sudoku

class UniqueRectangleType4:

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits

        for r in range(len(puzzle)):

            house = puzzle.house_row(r)

            for i in range(len(house)):
                for ii in range(len(house)):
                    if i == ii:
                        continue

                    l0 = house[i]
                    l1 = house[ii]

                    candidates0 = set(puzzle.cell_candidates(l0))
                    candidates1 = puzzle.cell_candidates(l1)

                    if len(candidates0) != 2 or len(candidates1) != 2:
                        continue

                    if not candidates0.issubset(candidates1):
                        continue

                    col0 = puzzle.house_col(l0.col)
                    col1 = puzzle.house_col(l1.col)

                    for j in range(len(puzzle)):
                        corner0 = col0[j]
                        corner1 = col1[j]

                        loc_set = {l0, l1, corner0, corner1}

                        if len(loc_set) != 4:
                            continue

                        corner0_candidates = set(puzzle.cell_candidates(corner0))
                        corner1_candidates = set(puzzle.cell_candidates(corner1))

                        if not corner0_candidates.issuperset(candidates0) or not corner1_candidates.issuperset(
                                candidates1):
                            continue

                        row_indexes = set([l.row for l in loc_set])
                        col_indexes = set([l.col for l in loc_set])
                        fence_indexes = set([puzzle.cell_fence(l) for l in loc_set])

                        if len(row_indexes) != 2 or len(col_indexes) != 2 or len(fence_indexes) != 2:
                            continue

                        opposite_row = puzzle.house_row(corner0.row)

                        for _candidate in candidates0:
                            locs_with_candidate = [l for l in opposite_row if
                                                    _candidate in puzzle.cell_candidates(l)]

                            if len(locs_with_candidate) != 2:
                                continue

                            if not {corner0, corner1}.issuperset(locs_with_candidate):
                                continue

                            temp_candidates = set(candidates0)

                            temp_candidates.remove(_candidate)

                            other = list(temp_candidates)[0]

                            for loc in [corner0, corner1]:
                                edits += puzzle.rem(loc, [other])

        for c in range(len(puzzle)):

            house = puzzle.house_col(c)

            for i in range(len(house)):
                for ii in range(len(house)):
                    if i == ii:
                        continue

                    l0 = house[i]
                    l1 = house[ii]

                    candidates0 = puzzle.cell_candidates(l0)
                    candidates1 = puzzle.cell_candidates(l1)

                    if len(candidates0) != 2 or len(candidates1) != 2:
                        continue

                    if not set(candidates0).issubset(candidates1):
                        continue

                    row0 = puzzle.house_row(l0.row)
                    row1 = puzzle.house_row(l1.row)

                    for j in range(len(puzzle)):
                        corner0 = row0[j]
                        corner1 = row1[j]

                        loc_set = {l0, l1, corner0, corner1}

                        if len(loc_set) != 4:
                            continue

                        corner0_candidates = set(puzzle.cell_candidates(corner0))
                        corner1_candidates = set(puzzle.cell_candidates(corner1))

                        if not corner0_candidates.issuperset(candidates0) or not corner1_candidates.issuperset(
                                candidates1):
                            continue

                        row_indexes = set([loc.row for loc in loc_set])
                        col_indexes = set([loc.col for loc in loc_set])
                        fence_indexes = set([puzzle.cell_fence(l) for l in loc_set])

                        if len(row_indexes) != 2 or len(col_indexes) != 2 or len(fence_indexes) != 2:
                            continue

                        opposite_col = puzzle.house_col(corner0.col)

                        for _candidate in candidates0:
                            locs_with_candidate = [loc for loc in opposite_col if
                                                    _candidate in puzzle.cell_candidates(loc)]

                            if len(locs_with_candidate) != 2:
                                continue

                            if not {corner0, corner1}.issuperset(locs_with_candidate):
                                continue

                            temp_candidates = set(candidates0)

                            temp_candidates.remove(_candidate)

                            other = list(temp_candidates)[0]

                            for loc in [corner0, corner1]:
                                edits += puzzle.rem(loc, [other])

        return edits

