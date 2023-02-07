from typing import Optional

from Loc import Loc
from puzzles import Magnets
from techniques.Technique import Technique


class MagnetsTech(Technique):
    def __int__(self):
        self.EMPTY = 0

    def solve0(self, puzzle: Magnets) -> int:
        edits = 0

        # house = puzzle.house_col(0)
        #
        # plus = puzzle.plus_col_value(0)
        # minus = puzzle.minus_col_value(0)

        # print(house)
        # print(plus)
        # print(minus)

        for i in range(puzzle.length):
            edits += self.solve_house(puzzle, puzzle.house_row(i), puzzle.plus_row_value(i), puzzle.minus_row_value(i))
            edits += self.solve_house(puzzle, puzzle.house_col(i), puzzle.plus_col_value(i), puzzle.minus_col_value(i))

        return edits

    def solve_house(self, puzzle: Magnets, house: list[Loc], plus: Optional[int], minus: Optional[int]) -> int:
        edits = 0

        solved_plus = [loc for loc in house if
                       len(puzzle.cell_candidates(loc)) == 1 and '+' in puzzle.cell_candidates(loc)]
        solved_minus = [loc for loc in house if
                        len(puzzle.cell_candidates(loc)) == 1 and '-' in puzzle.cell_candidates(loc)]
        solved_empty = [loc for loc in house if
                        len(puzzle.cell_candidates(loc)) == 1 and '.' in puzzle.cell_candidates(loc)]
        unsolved = [loc for loc in house if len(puzzle.cell_candidates(loc)) > 1]

        has_plus = [loc for loc in house if '+' in puzzle.cell_candidates(loc)]
        has_minus = [loc for loc in house if '-' in puzzle.cell_candidates(loc)]
        has_empty = [loc for loc in house if '.' in puzzle.cell_candidates(loc)]

        for loc in house:
            __candidates = puzzle.cell_candidates(loc)
            if len(__candidates) != 1:
                continue

            # solved = __candidates[0]

            surrounding = [loc0 for loc0 in [loc.north(), loc.east(), loc.west(), loc.south()] if
                           loc0.is_valid_sudoku(len(puzzle))]

            if '+' in __candidates:
                edits += puzzle.rem(surrounding, ['+'])

            if '-' in __candidates:
                edits += puzzle.rem(surrounding, ['-'])

            # print(surrounding)

            # if solved ==

        # if len(solved_plus) == 0 and len(unsolved) == plus:
        #     #
        #     pass

        # if all(loc.col == 3 for loc in house):
        #     # edits += puzzle.rem(unsolved, ['-', '.'])
        #     print('/////////')
        #     print(f'Plus: {len(solved_plus)}')
        #     print(f'Minus: {len(solved_minus)}')
        #     print(f'Empty: {len(solved_empty)}')
        #     print(f'Unsolved: {len(unsolved)}')

        if len(solved_plus) == 0 and plus == len(has_plus):
            edits += puzzle.rem(has_plus, ['-', '.'])

        if len(solved_plus) == plus:
            edits += puzzle.rem(unsolved, ['+'])

        for tup in puzzle.house_fences():
            loc0, loc1 = tup
            loc0_candidates = puzzle.cell_candidates(loc0)
            loc1_candidates = puzzle.cell_candidates(loc1)

            if '+' not in loc0_candidates:
                edits += puzzle.rem([loc1], ['-'])

            if '+' not in loc1_candidates:
                edits += puzzle.rem([loc0], ['-'])

            if '-' not in loc0_candidates:
                edits += puzzle.rem([loc1], ['+'])
            #
            if '-' not in loc1_candidates:
                edits += puzzle.rem([loc0], ['+'])

            if '.' not in loc0_candidates:
                edits += puzzle.rem([loc1], ['.'])

            if '.' not in loc1_candidates:
                edits += puzzle.rem([loc0], ['.'])

        if plus is not None and plus == 0:
            edits += puzzle.rem(house, ['+'])

        if minus is not None and minus == 0:
            edits += puzzle.rem(house, ['-'])

        if plus is not None and minus is not None:
            total = plus + minus
            if total == len(puzzle):
                edits += puzzle.rem(house, ['.'])

        return edits
