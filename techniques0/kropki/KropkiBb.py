from _puzzles import Kropki


class KropkiBb:

    def solve0(self, puzzle: Kropki) -> int:
        edits = 0

        for center_cell in puzzle.iterate_cells():
            directions = [
                [
                    center_cell.west(2),
                    center_cell.west(),
                    center_cell.east(),
                    center_cell.east(2),
                ],
                [
                    center_cell.north(2),
                    center_cell.north(),
                    center_cell.south(),
                    center_cell.south(2),
                ],
                # west north
                [
                    center_cell.west(2),
                    center_cell.west(),
                    center_cell.north(),
                    center_cell.north(2),
                ],
                # east south
                [
                    center_cell.east(2),
                    center_cell.east(),
                    center_cell.south(),
                    center_cell.south(2)
                ],
                # west south
                [
                    center_cell.west(2),
                    center_cell.west(),
                    center_cell.south(),
                    center_cell.south(2),
                ],
                # east north
                [
                    center_cell.north(2),
                    center_cell.north(),
                    center_cell.east(),
                    center_cell.east(2),
                ],
            ]
            for direction in directions:
                other0, kropki0, kropki1, other1 = direction

                cell_set = {other0, center_cell, other1}

                all_our_valid = all([loc.is_valid_kropki(puzzle.grid_length) for loc in cell_set])

                if not all_our_valid:
                    continue

                if not puzzle.is_black(kropki0) or not puzzle.is_black(kropki1):
                    continue

                row_set = {other0.row, center_cell.row, other1.row}
                col_set = {other0.col, center_cell.col, other1.col}

                cells_in_sets = []

                if len(row_set) == 1:
                    cells_in_sets = cells_in_sets + puzzle.house_row_cell_locs(row_set.pop())

                if len(col_set) == 1:
                    cells_in_sets = cells_in_sets + puzzle.house_col_cell_locs(col_set.pop())

                if puzzle.has_fences:
                    fence_set = {puzzle.cell_fence(other0), puzzle.cell_fence(center_cell),
                                 puzzle.cell_fence(other1)}
                    if len(fence_set) == 1:
                        cells_in_sets = cells_in_sets + puzzle.house_fence_cell_locs(fence_set.pop())

                cells_to_remove_from = set(cells_in_sets).difference(cell_set)

                edits += puzzle.rem(cells_to_remove_from, [2, 4])
                edits += puzzle.rem([center_cell], [1, 3, 5, 6, 7, 8, 9])
                edits += puzzle.rem([other0, other1], [3, 5, 6, 7, 9])

        return edits
