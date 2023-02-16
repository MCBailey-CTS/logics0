from typing import Optional

from Loc import Loc
from techniques.Technique import Technique
from tests_files.test_magnets import Magnets


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

        fence_dict = {}

        for loc in house:
            fence = puzzle.cell_fence(loc)

            if fence not in fence_dict:
                fence_dict[fence] = []
            fence_dict[fence].append(loc)

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

        no_plus = [loc for loc in house if '+' not in puzzle.cell_candidates(loc)]
        no_minus = [loc for loc in house if '-' not in puzzle.cell_candidates(loc)]
        no_empty = [loc for loc in house if '.' not in puzzle.cell_candidates(loc)]

        if minus is not None and minus == len(has_minus):
            edits += puzzle.rem(has_minus, ['+', '.'])

        if plus is not None and minus is not None and len(no_empty) == plus + minus:
            edits += puzzle.rem(list(set(house).difference(no_empty)), ['+', '-'])

        if plus is not None and minus is not None and plus + minus == len(puzzle) and (
                plus + minus) % 2 != 0 and plus > minus:
            edits += puzzle.rem([house[0]], ['-'])

        if plus is not None and \
                minus is not None and \
                plus != minus and \
                len(no_empty) == plus + minus and \
                len(no_empty) == 3:
            loc0: Loc
            loc1: Loc
            loc2: Loc
            loc0, loc1, loc2 = no_empty
            minor = '-' if plus > minus else '+'
            if loc0.is_next_to(loc1) and not loc1.is_next_to(loc2):
                edits += puzzle.rem([loc2], [minor])

            if not loc0.is_next_to(loc1) and loc1.is_next_to(loc2):
                edits += puzzle.rem([loc0], [minor])

            if loc0.is_next_to(loc1) and loc1.is_next_to(loc2):
                edits += puzzle.rem([loc1], [minor])

        if plus is not None and \
                minus is not None and \
                plus != minus and \
                len(no_empty) == plus + minus and \
                len(no_empty) == 3:
            loc0: Loc
            loc1: Loc
            loc2: Loc
            loc0, loc1, loc2 = no_empty
            minor = '-' if plus > minus else '+'
            if loc0.is_next_to(loc1) and not loc1.is_next_to(loc2):
                edits += puzzle.rem([loc2], [minor])

            if not loc0.is_next_to(loc1) and loc1.is_next_to(loc2):
                edits += puzzle.rem([loc0], [minor])

            if loc0.is_next_to(loc1) and loc1.is_next_to(loc2):
                edits += puzzle.rem([loc1], [minor])

        for loc in house:
            __candidates = puzzle.cell_candidates(loc)
            if len(__candidates) != 1:
                continue

            surrounding = [loc0 for loc0 in [loc.north(), loc.east(), loc.west(), loc.south()] if
                           loc0.is_valid_sudoku(len(puzzle))]

            if '+' in __candidates:
                edits += puzzle.rem(surrounding, ['+'])

            if '-' in __candidates:
                edits += puzzle.rem(surrounding, ['-'])

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

        if minus is not None and minus == len(solved_empty):
            edits += puzzle.rem(unsolved, ['-'])

        if plus is not None and minus is not None:
            total = plus + minus
            if total == len(puzzle):
                edits += puzzle.rem(house, ['.'])

        if plus is not None and minus is not None:
            total = plus + minus
            if total == len(puzzle) - 1:
                for fence in fence_dict:
                    if len(fence_dict[fence]) == 2:
                        edits += puzzle.rem(fence_dict[fence], ['.'])

        if plus is not None and \
                minus is not None and \
                plus + minus == 3 and \
                set(has_plus) == set(has_minus) and \
                len(has_plus) == 3:
            edits += puzzle.rem(has_plus, ['.'])

        if plus is not None and \
                minus is not None and \
                plus + minus % 2 != 0 and \
                set(has_plus) == set(has_minus) and \
                len(has_plus) == 3:
            edits += puzzle.rem(has_plus, ['.'])

        return edits
