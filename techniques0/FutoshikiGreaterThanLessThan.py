from _puzzles import Futoshiki
    
class FutoshikiGreaterThanLessThan:  # (BaseFutoshikiTechnique):
    def solve0(self, puzzle: Futoshiki) -> int:
        edits = 0

        for r in range(puzzle.length * 2 - 1):
            for c in range(puzzle.length * 2 - 1):

                even_row = r % 2 == 0
                even_col = c % 2 == 0

                if even_row and even_col:
                    continue

                if not even_row and not even_col:
                    continue

                if even_row:
                    loc = Loc(r, c)
                    string = puzzle.cell_string(loc)

                    if string == '>':
                        edits += self.solve_greater_than(puzzle, loc.east(), loc.west())

                    # print(puzzle.cell_string(loc))
        # for row_house in puzzle.house_row_cells()

        return edits

    def solve_greater_than(self, puzzle: Futoshiki, lesser: Loc, greater: Loc):
        edits = 0
        lesser_candidates = puzzle.cell_candidates(lesser)
        greater_candidates = puzzle.cell_candidates(greater)

        min_greater = min(greater_candidates)
        max_lesser = max(lesser_candidates)

        print(min_greater)
        print(max_lesser)

        for candidate in lesser_candidates:
            if candidate >= min_greater:
                print(f'removing {candidate} from {lesser}')
                edits += puzzle.rem([lesser], [str(candidate)])

        # print(lesser_candidates)
        # print(greater_candidates)

        return edits


