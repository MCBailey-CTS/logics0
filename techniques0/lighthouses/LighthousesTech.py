from techniques0.Technique import Technique
from puzzles import Lighthouses
from Loc import Loc


class LighthousesTech(Technique):
    def solve0(self, puzzle: Lighthouses) -> int:
        edits = 0

        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)

                number = puzzle.light_number(loc)

                if puzzle.grid[r][c] == '+_':
                    edits += puzzle.rem(puzzle.surrounding(loc), ['+'])

                if number is not None:
                    edits += puzzle.rem(puzzle.surrounding(loc), ['+'])
                    row_locs = puzzle.house_row(r)
                    col_locs = puzzle.house_col(c)
                    extending = [loc0 for loc0 in set(row_locs + col_locs) if
                                 puzzle.is_candidate_cell(loc0) and loc0 != loc]
                    if number == 0:
                        edits += puzzle.rem(extending, ['+'])

                    solved_light = []
                    solved_empty = []
                    unsolved = []

                    for loc0 in extending:
                        if puzzle.grid[loc0.row][loc0.col] == '+-':
                            unsolved.append(loc0)
                        if puzzle.grid[loc0.row][loc0.col] == '+_':
                            solved_light.append(loc0)
                        if puzzle.grid[loc0.row][loc0.col] == '_-':
                            solved_empty.append(loc0)

                    if len(unsolved) == 1 and len(solved_light) == 1 and number == 2:
                        edits += puzzle.rem(unsolved, ['-'])

                    # if len(unsolved) == 2 and number == 2 and len(solved_light) == 0:
                    #     edits += puzzle.rem(unsolved, ['-'])
                    #
                    if number == 1 and len(unsolved) == 1:
                        edits += puzzle.rem(unsolved, ['-'])

                    if len(solved_light) == 1 and len(unsolved) == 2 and number == 3:
                        edits += puzzle.rem(unsolved, ['-'])

                    if len(solved_light) == 0 and len(unsolved) == 3 and number == 2:
                        for un in unsolved:
                            temp_set = set(unsolved)

                            temp_set.remove(un)

                            other0, other1 = temp_set

                            if un.is_next_to(other0) and not un.is_next_to(other1):
                                edits += puzzle.rem([other1], ['-'])

                                if un.col == other0.col:
                                    surrounding0 = puzzle.surrounding(un)
                                    surrounding1 = puzzle.surrounding(other0)

                                    intersection = set(surrounding0).intersection(surrounding1)

                                    locs_to_rem = [loc1 for loc1 in intersection if
                                                   loc1.row == un.row or loc1.row == other0.row]
                                    edits += puzzle.rem(locs_to_rem, ['+'])

        return edits
