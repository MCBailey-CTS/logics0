from puzzles import Kropki


class KropkiBw:

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

                if (puzzle.is_black(kropki0) and puzzle.is_white(kropki1)) or (
                        puzzle.is_black(kropki1) and puzzle.is_white(kropki0)):
                    edits += puzzle.rem([center_cell], [1])
        return edits
