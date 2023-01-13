from Loc import Loc
from puzzles import LightenUp
from techniques0.Technique import Technique


class LightenUpTech(Technique):
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

                solved_light = []
                solved_empty = []
                unsolved = []

                for loc0 in puzzle.surrounding_light(loc):
                    if puzzle.grid[loc0.row][loc0.col] == '+_':
                        solved_light.append(loc0)
                    if puzzle.grid[loc0.row][loc0.col] == '_-':
                        solved_empty.append(loc0)
                    if puzzle.grid[loc0.row][loc0.col] == '+-':
                        unsolved.append(loc0)

                if len(solved_light) == 0 and len(unsolved) == light_number:
                    edits += puzzle.rem(unsolved, ['-'])

                if len(solved_light) == light_number:
                    edits += puzzle.rem(unsolved, ['+'])

                if len(solved_light) == 2 and light_number == 3 and len(unsolved) == 1:
                    edits += puzzle.rem(unsolved, ['-'])

        return edits
