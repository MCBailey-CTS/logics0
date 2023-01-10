from Loc import Loc
from puzzles import Parks1

class Parks1Shape_00_01:

    def shape_w_south_east(self, center: Loc) -> tuple[list[Loc], list[Loc]]:
        return ([
                    center.north(),
                    center.north().east(),
                    center,
                    center.west(),
                    center.west().south(),
                ], [center.north().west()])

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0

        for house in puzzle.houses_rows() + puzzle.houses_cols():
            solved_empty = [loc for loc in house if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in house if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
            unsolved = list(set(house).difference(solved_tree + solved_empty))
            if len(solved_tree) == 1:
                continue
            if len(unsolved) == 2:
                loc0, loc1 = unsolved
                if loc0.is_next_to(loc1):
                    if loc0.col == loc1.col:
                        if loc0.east().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc0.east()], [1])
                        if loc0.west().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc0.west()], [1])
                        if loc1.east().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc1.east()], [1])
                        if loc1.west().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc1.west()], [1])

                    if loc0.row == loc1.row:
                        if loc0.north().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc0.north()], [1])
                        if loc0.south().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc0.south()], [1])
                        if loc1.north().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc1.north()], [1])
                        if loc1.south().is_valid_parks(puzzle.grid):
                            edits += puzzle.rem([loc1.south()], [1])

                # print(unsolved)

        # for fence in puzzle.fences():
        #     house = set(puzzle.house_fence(fence))
        #     solved_parks = [loc for loc in house if puzzle.is_cell_solved(loc, 1)]
        #     if len(solved_parks) > 1:
        #         raise Exception("Found a park fence that is solved with more than one fence")
        #     if len(solved_parks) == 1:
        #         continue
        #     unsolved = [loc for loc in house if puzzle.is_cell_solved(loc, 1)]

        return edits