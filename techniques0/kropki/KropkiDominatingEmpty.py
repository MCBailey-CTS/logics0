from puzzles import Kropki


class KropkiDominatingEmpty:

    def solve0(self, puzzle: Kropki) -> int:
        edits = 0
        for cell in puzzle.iterate_cells():
            directions = [
                [cell.west(), cell.west(2)],
                [cell.east(), cell.east(2)],
                [cell.north(), cell.north(2)],
                [cell.south(), cell.south(2)],
            ]
            for direction in directions:
                if not puzzle.all_locs_are_valid(direction):
                    continue

                kropki, other = direction

                if not puzzle.is_empty(kropki):
                    continue

                cell_candidates = puzzle.cell_candidates(cell)

                # 1
                if {1, 2}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [1, 2])

                # 2
                if {1, 2, 3, 4}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [2])

                # 3
                if {2, 3, 4, 6}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [3])

                # 4
                if {2, 3, 4, 5, 8}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [4])

                # 5
                if {4, 5, 6}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [5])

                # 6
                if {3, 5, 6, 7}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [6])

                # 7
                if {6, 7, 8}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [7])

                # 8
                if {4, 7, 8, 9}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [8])

                # 9
                if {8, 9}.issuperset(cell_candidates):
                    edits += puzzle.rem([other], [8, 9])

        return edits
