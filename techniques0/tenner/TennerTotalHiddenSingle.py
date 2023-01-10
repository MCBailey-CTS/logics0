from puzzles import Tenner


class TennerTotalHiddenSingle:
    def solve0(self, puzzle: Tenner) -> int:
        edits = 0
        for col in range(puzzle.col_length):
            col_house = puzzle.house_col_cell_locs(col)
            total = puzzle.total(col)
            if total is None:
                continue
            solved_locs = [loc for loc in col_house if puzzle.is_cell_solved(loc)]
            unsolved_locs = [loc for loc in col_house if not puzzle.is_cell_solved(loc)]

            if len(unsolved_locs) != 1:
                continue

            current_total = sum([puzzle.cell_candidates(loc)[0] for loc in solved_locs])

            needed_candidate = total - current_total

            for candidate in puzzle.expected_candidates():
                if candidate != needed_candidate:
                    edits += puzzle.rem([unsolved_locs[0]], [candidate])

        return edits
