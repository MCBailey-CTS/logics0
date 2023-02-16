from techniques.Technique import Technique


class Parks1Shapes(Technique):
    def solve0(self, puzzle) -> int:
        edits = 0
        # for fence in puzzle.fences():
        #     house = puzzle.house_fence(fence)
        #
        #     solved_parks1 = []
        #
        #     unsolved = []
        #
        #     for loc in house:
        #         candidates = puzzle.cell_candidates(loc)
        #         if len(candidates) == 2:
        #             unsolved.append(loc)
        #             continue
        #         if 1 in candidates:
        #             solved_parks1.append(loc)
        #
        #     if len(solved_parks1) == 1:
        #         continue
        #
        #     temp = puzzle.surrounding( unsolved[0])
        #
        #     surrounding = set(temp)
        #
        #     rows = set(puzzle.house_row(unsolved[0].row))
        #
        #     cols = set(puzzle.house_col(unsolved[0].col))
        #
        #     for index in range(1, len(unsolved)):
        #         surrounding = surrounding.intersection(puzzle.surrounding( unsolved[index]))
        #
        #         rows = rows.intersection(puzzle.house_row(unsolved[index].row))
        #
        #         cols = cols.intersection(puzzle.house_col(unsolved[index].col))
        #
        #     surrounding = surrounding.difference(unsolved)
        #     rows = rows.difference(unsolved)
        #     cols = cols.difference(unsolved)
        #
        #     edits += puzzle.rem(surrounding, [1])
        #     edits += puzzle.rem(rows, [1])
        #     edits += puzzle.rem(cols, [1])

        return edits
