from Loc import Loc
from puzzles import LightenUp


class LightenUpTech:
    def solve0(self, puzzle: LightenUp) -> int:
        edits = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)

                if puzzle.grid[r][c] == '+-':
                    locs_to_remove = puzzle.extending_cell_locs(loc)

                    if all(puzzle.grid[loc0.row][loc0.col] == '_-' for loc0 in locs_to_remove):
                        edits += puzzle.rem([loc], ['-'])

                if puzzle.grid[r][c] == '+_':
                    locs_to_remove = puzzle.extending_cell_locs(loc)

                    edits += puzzle.rem(locs_to_remove, ['+'])

                if puzzle.grid[r][c] == '+_':
                    for loc0 in puzzle.surrounding_light(loc):
                        if puzzle.is_candidate_cell(loc0):
                            edits += puzzle.rem([loc0], ['+'])

                light_number = puzzle.light_number(loc)

                if light_number is None:
                    continue

                if light_number == 0:
                    edits += puzzle.rem(
                        list(filter(lambda loc1: puzzle.is_candidate_cell(loc1), puzzle.surrounding_light(loc))), ['+'])

                if light_number == 4:
                    edits += puzzle.rem(
                        list(filter(lambda loc1: puzzle.is_candidate_cell(loc1), puzzle.surrounding_light(loc))), ['-'])

                # print(f'"{puzzle.grid[r][c]}"')

        return edits
