from techniques.Technique import Technique


class CrossHatch(Technique):
    def solve0(self, puzzle) -> int:
        edits = 0

        unsolved = puzzle.unsolved_cells()

        # print(len(unsolved))

        if len(unsolved) == 0:
            return edits

        for cell in list(puzzle.unsolved_cells()):
            neighbors = set(
                puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
            if puzzle.has_fences:
                for loc in puzzle.house_fence(puzzle.cell_fence(cell)):
                    neighbors.add(loc)
            neighbors.remove(cell)
            for neighbor in neighbors:
                if neighbor not in puzzle.unsolved_cells():
                    _candidates = puzzle.cell_candidates(neighbor)
                    if len(_candidates) == 1:
                        edits += puzzle.rem(cell, [list(_candidates)[0]])
        return edits
