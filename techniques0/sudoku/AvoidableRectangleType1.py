from Loc import Loc
from _puzzles import Sudoku


class AvoidableRectangleType1:

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        solved_cells = []
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                if len(puzzle.cell_candidates(loc)) == 1:
                    solved_cells.append(loc)

        for upper_corner in solved_cells:
            for lower_corner in solved_cells:
                other_upper = Loc(upper_corner.row, lower_corner.col)
                other_lower = Loc(lower_corner.row, upper_corner.col)
                corner_set = {upper_corner, lower_corner, other_upper, other_lower}

                if len(corner_set) != 4:
                    continue

                # if not corner_set.issuperset([Loc(0, 0), Loc(0, 1), Loc(8, 0), Loc(8, 1)]):
                #     continue

                row_set = set([loc.row for loc in corner_set])
                col_set = set([loc.col for loc in corner_set])
                fence_set = set([puzzle.cell_fence(loc) for loc in corner_set])

                if len(row_set) != 2 or len(col_set) != 2 or len(fence_set) != 2:
                    continue

                solved_cells = set([loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 1])

                if len(solved_cells) != 3:
                    continue

                unsolved_cells = set([loc for loc in corner_set if len(puzzle.cell_candidates(loc)) > 1])

                if len(unsolved_cells) != 1:
                    continue

                opposite_corners = set(corner_set)

                opposite_corners.remove(other_upper)
                opposite_corners.remove(other_lower)

                temp_opposite = list(opposite_corners)

                opposite_candidates0 = set(puzzle.cell_candidates(temp_opposite[0]))
                opposite_candidates1 = puzzle.cell_candidates(temp_opposite[1])

                if len(opposite_candidates0) != 1 or len(opposite_candidates1) != 1:
                    continue

                if not opposite_candidates0.issubset(opposite_candidates1):
                    continue

                # opposite_candidate = opposite_candidates0.pop()

                other_solved_cell = list(solved_cells.difference(opposite_corners))[0]

                solved_candidate = list(puzzle.cell_candidates(other_solved_cell))[0]

                edits += puzzle.rem(unsolved_cells.pop(), [solved_candidate])

                # print(solved_candidate)
                # print(f'{other_upper} {other_lower} {puzzle.cell_candidates(other_upper)} {puzzle.cell_candidates(other_lower)}')

                # unsolved_cell = unsolved_cells.pop()

                # solved_candidates = set([puzzle.solved_candidate(loc) for loc in solved_cells])

                # if len(solved_candidates) != 2:
                #     continue

                # solved_candidate_dict = {}

                # for loc in corner_set:
                #     candidates0 = puzzle.cell_candidates(loc)

                #     if len(candidates0) > 1:
                #         continue

                #     candidate = list(candidates0)[0]

                #     if candidate not in solved_candidate_dict:
                #         solved_candidate_dict[candidate] = 0

                #     solved_candidate_dict[candidate] += 1

                # if len(solved_candidate_dict) != 2:
                #     continue

                # corner_candidate = None

                # keys = list(solved_candidate_dict.keys())

                # if solved_candidate_dict[keys[0]] == 2:
                #     corner_candidate = keys[1]
                # elif solved_candidate_dict[keys[1]] == 2:
                #     corner_candidate = keys[0]

                # unsolved_cell_candidates = puzzle.cell_candidates(unsolved_cell)

                # if corner_candidate in unsolved_cell_candidates and len(unsolved_cell_candidates) == 1:
                #     continue

                # print(corner_set)

                # edits += puzzle.rem(unsolved_cell, [corner_candidate])

        return edits
