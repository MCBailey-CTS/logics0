import json
from typing import Optional

import pytest

from Loc import Loc
from Constants import Constants



# hidden_stars_001 = json.loads(
#     '{ '
#     '   "id"     : "001.hidden_stars", '
#     '   "length" : 4, '
#     '   "stars"  : 0, '
#     '   "grid"   : '
#     '       ['
#     '           [["+", "-"], ["+", "-"], ["+", "-"], "ww"      , 2], '
#     '           [["+", "-"], "se"      , ["+", "-"], ["+", "-"], 1], '
#     '           [["+", "-"], ["+", "-"], "ww"      , ["+", "-"], 1], '
#     '           ["ne"      , ["+", "-"], "nn"      , ["+", "-"], 1], '
#     '           [1,          2,          1,          1,          $], '
#     '       ]'
#     '}'
# )

PLUS = '+'
MINUS = '-'


class BotanicalPark:
    def __init__(self, __json) -> None:
        self.__json = __json
        self.id = self.__json['id']
        self.trees = self.__json['trees']
        temp = self.__json['grid']
        self.grid: list[list[list]] = []
        for k in temp:
            self.grid.append(k)

    def __len__(self) -> int:
        return int(self.__json['length'])

    def is_solved(self) -> bool:
        for _r in range(len(self)):
            for _c in range(len(self)):
                obj = self.grid[_r][_c]
                if isinstance(obj, str):
                    continue
                if len(obj) > 1:
                    return False
        return True

    def __str__(self):
        string = f'{self.id}\n{len(self)}\n'
        for r in range(len(self)):
            for c in range(len(self)):
                string += f'{str(self.grid[r][c]).ljust(10)} '
            string += '\n'
        return string



def pointing_hidden(puzzle: BotanicalPark, __loc: Optional[Loc] = None) -> int:
    edits = 0

    if __loc is not None:
        _cell_string = puzzle.grid[__loc.row][__loc.col]

        # print(_cell_string)

        __house: list[Loc]

        match _cell_string:
            case 'nn':
                __house = __loc.north_locs()
            case 'ww':
                __house = __loc.west_locs()
            case 'ss':
                __house = __loc.south_locs(len(puzzle))
            case 'ee':
                __house = __loc.east_locs(len(puzzle))
            case 'ne':
                __house = __loc.north_east_locs(len(puzzle))
            case 'nw':
                __house = __loc.north_west_locs(len(puzzle))
            # case 'se':
            #     __house = __loc.south_east_locs(len(puzzle))
            case 'sw':
                __house = __loc.south_west_locs(len(puzzle))

            case _:
                return edits

        __house = [_l for _l in __house if
                   len(puzzle.grid[_l.row][_l.col]) and PLUS in puzzle.grid[_l.row][_l.col]]

        # print(__house)

        if len(__house) == 1 and MINUS in puzzle.grid[__house[0].row][__house[0].col]:
            temp: list = puzzle.grid[__house[0].row][__house[0].col]
            temp.remove(MINUS)
            edits += 1
            # edits += puzzle.rem([__house[0]], [MINUS])

    return edits


def pointing_required(puzzle: BotanicalPark, __loc: Optional[Loc] = None) -> int:
    edits = 0

    if __loc is not None:
        _cell_string = puzzle.grid[__loc.row][__loc.col]

        # print(_cell_string)

        __house: list[Loc]

        # print(_cell_string)

        match _cell_string:
            case 'nn':
                __house = __loc.north_locs()
            case 'ww':
                __house = __loc.west_locs()
            case 'ss':
                __house = __loc.south_locs(len(puzzle))
            case 'ee':
                __house = __loc.east_locs(len(puzzle))
            case 'ne':
                __house = __loc.north_east_locs(len(puzzle))
            case 'nw':
                __house = __loc.north_west_locs(len(puzzle))
            # case 'se':
            #     __house = __loc.south_east_locs(len(puzzle))
            # case 'sw':
            #     __house = __loc.south_west_locs(len(puzzle))
            case _:
                return edits

        if len(__house) == 2 and __house[0].is_next_to(__house[1]):
            __l0 = __house[0]
            __l1 = __house[1]

            __remove: Optional[list[Loc]] = None

            if __house[0].in_same_row(__house[1]):
                __remove = [__loc for __loc in
                            [__house[0].south(), __house[0].north(), __house[1].south(), __house[1].north()]
                            if __loc.is_valid_sudoku(len(puzzle))]
            elif __house[0].in_same_col(__house[1]):
                __remove = [__loc for __loc in
                            [__house[0].west(), __house[0].east(), __house[1].west(), __house[1].east()]
                            if __loc.is_valid_sudoku(len(puzzle))]

            if __remove is not None:
                for __loc in __remove:
                    __candidates: list = puzzle.grid[__loc.row][__loc.col]

                    if PLUS in __candidates:
                        __candidates.remove(PLUS)
                        edits += 1

            # print("length 2")

        # __house = [_l for _l in __house if
        #            len(puzzle.grid[_l.row][_l.col]) and PLUS in puzzle.grid[_l.row][_l.col]]
        #
        # # print(__house)
        #
        # if len(__house) == 1 and MINUS in puzzle.grid[__house[0].row][__house[0].col]:
        #     temp: list = puzzle.grid[__house[0].row][__house[0].col]
        #     temp.remove(MINUS)
        #     edits += 1
        #     # edits += puzzle.rem([__house[0]], [MINUS])

    return edits


def pointing_opposite_nsew(puzzle: BotanicalPark, __loc: Optional[Loc] = None) -> int:
    edits = 0

    if __loc is not None:
        _cell_string = puzzle.grid[__loc.row][__loc.col]

        __house: list[Loc]

        # print(_cell_string)

        match _cell_string:
            case 'nn':
                __house = __loc.south_locs(len(puzzle))
            case 'ww':
                __house = __loc.east_locs(len(puzzle))
            case 'ss':
                __house = __loc.north_locs()
            case 'ee':
                __house = __loc.west_locs()
            case _:
                return edits

        for __l in __house:
            if PLUS in puzzle.grid[__l.row][__l.col]:
                puzzle.grid[__l.row][__l.col].remove(PLUS)
                edits += 1

        # if len(__house) == 1 and MINUS in puzzle.grid[__house[0].row][__house[0].col]:
        #     temp: list = puzzle.grid[__house[0].row][__house[0].col]
        #     temp.remove(MINUS)
        #     edits += 1
        #     # edits += puzzle.rem([__house[0]], [MINUS])

    return edits


def hidden_single_cell_neighbors(puzzle: BotanicalPark, __candidate, __neighbors: list[Loc]) -> int:
    edits = 0
    iterator = (__loc for __loc in __neighbors if __candidate in puzzle.grid[__loc.row][__loc.col])
    __first = next(iterator)
    __second = next(iterator, None)
    if __second is not None:
        return edits
    for __other_candidate in list(puzzle.grid[__first.row][__first.col]):
        if __other_candidate == __candidate:
            continue
        puzzle.grid[__first.row][__first.col].remove(__other_candidate)
        edits += 1
    return edits


def cross_hatch_cell_neighbors(puzzle: BotanicalPark, __cell: Loc, __candidate, __neighbors: list[Loc]) -> int:
    edits = 0
    __neighbors = set(__neighbors)
    __neighbors.discard(__cell)
    __candidates = puzzle.grid[__cell.row][__cell.col]
    if len(__candidates) != 1 or __candidate not in __candidates:
        return edits
    for __other in __neighbors:
        __other_candidates: list = puzzle.grid[__other.row][__other.col]
        if __candidate not in __other_candidates:
            continue
        __other_candidates.remove(__candidate)
        edits += 1
    return edits


def cross_hatch_cell_row_col_touching(puzzle: BotanicalPark, __cell: Loc, __candidate) -> int:
    edits = 0
    edits += cross_hatch_cell_neighbors(puzzle, __cell, PLUS,
                                        Loc.house_row(__cell.row, len(puzzle)) + Loc.house_col(__cell.col, len(puzzle)))
    return cross_hatch_cell_neighbors(puzzle, __cell, PLUS, Loc.surrounding(__cell, len(puzzle))) + edits


def test_botanical_park_001():
    puzzle = BotanicalPark(Constants.botanical_park_001)
    pointing_hidden(puzzle, Loc(1, 4))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 4), PLUS)
    pointing_hidden(puzzle, Loc(3, 2))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 3), PLUS)
    loc = Loc(1, 2)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, loc, PLUS)
    loc = Loc(4, 1)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(loc.col, len(puzzle)))
    loc = Loc(4, 1)
    cross_hatch_cell_row_col_touching(puzzle, loc, PLUS)
    loc = Loc(1, 0)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(loc.col, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_002():
    puzzle = BotanicalPark(Constants.botanical_park_002)

    pointing_hidden(puzzle, Loc(1, 2))

    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 3), PLUS)

    puzzle.grid[2][0].remove(PLUS)
    puzzle.grid[1][1].remove(PLUS)

    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(1, len(puzzle)))

    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 0), PLUS)

    puzzle.grid[4][2].remove(PLUS)

    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(2, len(puzzle)))

    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 2), PLUS)

    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(1, len(puzzle)))

    cross_hatch_cell_row_col_touching(puzzle, Loc(4, 1), PLUS)

    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(4, len(puzzle)))

    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_003():
    puzzle = BotanicalPark(Constants.botanical_park_003)
    pointing_opposite_nsew(puzzle, Loc(1, 2))
    pointing_required(puzzle, Loc(1, 2))
    pointing_hidden(puzzle, Loc(4, 2))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 1), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(0, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(2, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 2), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(4, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 4), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(3, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_004():
    puzzle = BotanicalPark(Constants.botanical_park_004)
    pointing_hidden(puzzle, Loc(2, 2))
    pointing_hidden(puzzle, Loc(4, 4))
    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 1), PLUS)
    pointing_hidden(puzzle, Loc(2, 0))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 4), PLUS)
    loc = Loc(0, 2)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(4, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(1, len(puzzle)))
    loc = Loc(1, 5)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(3, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_005():
    puzzle = BotanicalPark(Constants.botanical_park_005)
    pointing_hidden(puzzle, Loc(2, 4))
    loc = Loc(1, 5)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    pointing_required(puzzle, Loc(3, 3))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(4, len(puzzle)))
    loc = Loc(3, 4)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    loc = Loc(3, 3)
    pointing_hidden(puzzle, loc)
    loc = Loc(5, 3)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(4, len(puzzle)))
    pointing_hidden(puzzle, Loc(0, 5))
    loc = Loc(4, 1)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    pointing_hidden(puzzle, Loc(5, 5))
    puzzle.grid[0][0].remove(MINUS)
    loc = Loc(0, 0)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(2, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_006():
    puzzle = BotanicalPark(Constants.botanical_park_006)
    pointing_hidden(puzzle, Loc(4, 1))
    loc = Loc(3, 0)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    pointing_hidden(puzzle, Loc(5, 4))
    loc = Loc(4, 3)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))
    puzzle.grid[2][2].remove(PLUS)
    puzzle.grid[0][1].remove(PLUS)
    puzzle.grid[1][1].remove(PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(1, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 1), PLUS)
    puzzle.grid[1][4].remove(PLUS)
    puzzle.grid[1][5].remove(PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(1, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 2), PLUS)
    pointing_hidden(puzzle, Loc(3, 5))
    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 4), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(0, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_007():
    puzzle = BotanicalPark(Constants.botanical_park_007)
    pointing_required(puzzle, Loc(2, 5))
    pointing_hidden(puzzle, Loc(2, 3))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 5), PLUS)
    pointing_hidden(puzzle, Loc(5, 1))
    cross_hatch_cell_row_col_touching(puzzle, Loc(6, 1), PLUS)
    pointing_hidden(puzzle, Loc(3, 3))
    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 2), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(1, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 0), PLUS)
    puzzle.grid[4][4].remove(PLUS)
    puzzle.grid[5][4].remove(PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(4, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 4), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(4, len(puzzle)))
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(3, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 3), PLUS)
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_008():
    puzzle = BotanicalPark(Constants.botanical_park_008)
    pointing_opposite_nsew(puzzle, Loc(0, 5))
    pointing_opposite_nsew(puzzle, Loc(3, 2))
    pointing_opposite_nsew(puzzle, Loc(6, 1))
    pointing_hidden(puzzle, Loc(3, 3))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 1), PLUS)
    pointing_hidden(puzzle, Loc(6, 4))
    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 0), PLUS)
    puzzle.grid[0][3].remove(PLUS)
    puzzle.grid[1][3].remove(PLUS)
    pointing_hidden(puzzle, Loc(6, 6))
    cross_hatch_cell_row_col_touching(puzzle, Loc(4, 4), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(3, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 6), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(0, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 2), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(1, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 5), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(6, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_009():
    puzzle = BotanicalPark(Constants.botanical_park_009)
    puzzle.grid[0][1].remove(PLUS)
    puzzle.grid[2][3].remove(PLUS)
    pointing_hidden(puzzle, Loc(3, 4))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 2), PLUS)
    pointing_hidden(puzzle, Loc(4, 1))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 5), PLUS)
    pointing_hidden(puzzle, Loc(4, 3))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 3), PLUS)
    pointing_hidden(puzzle, Loc(4, 6))
    cross_hatch_cell_row_col_touching(puzzle, Loc(4, 0), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(2, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(2, 6), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(5, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 4), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(6, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_010():
    puzzle = BotanicalPark(Constants.botanical_park_010)
    # puzzle.solve()
    pointing_hidden(puzzle, Loc(3, 3))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 2), PLUS)
    pointing_hidden(puzzle, Loc(3, 0))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 3), PLUS)
    pointing_hidden(puzzle, Loc(4, 4))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 1), PLUS)
    puzzle.grid[7][4].remove(PLUS)
    puzzle.grid[6][5].remove(PLUS)
    pointing_hidden(puzzle, Loc(4, 7))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 6), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(4, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(4, 0), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(6, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(6, 4), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(7, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(7, 7), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(2, len(puzzle)))
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_011():
    puzzle = BotanicalPark(Constants.botanical_park_011)
    pointing_required(puzzle, Loc(5, 2))
    pointing_opposite_nsew(puzzle, Loc(5, 2))
    pointing_hidden(puzzle, Loc(6, 3))
    pointing_opposite_nsew(puzzle, Loc(6, 3))
    cross_hatch_cell_row_col_touching(puzzle, Loc(6, 2), PLUS)
    pointing_hidden(puzzle, Loc(5, 2))
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 2), PLUS)
    pointing_hidden(puzzle, Loc(3, 7))
    cross_hatch_cell_row_col_touching(puzzle, Loc(4, 6), PLUS)
    puzzle.grid[2][5].remove(PLUS)
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 0), PLUS)
    pointing_hidden(puzzle, Loc(0, 7))
    cross_hatch_cell_row_col_touching(puzzle, Loc(3, 4), PLUS)
    pointing_hidden(puzzle, Loc(4, 1))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 5), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(3, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 3), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(7, len(puzzle)))
    cross_hatch_cell_row_col_touching(puzzle, Loc(7, 7), PLUS)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(2, len(puzzle)))

    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_012():
    puzzle = BotanicalPark(Constants.botanical_park_012)
    pointing_hidden(puzzle, Loc(1, 1))
    cross_hatch_cell_row_col_touching(puzzle, Loc(1, 0), PLUS)
    pointing_opposite_nsew(puzzle, Loc(3, 4))
    pointing_opposite_nsew(puzzle, Loc(5, 4))
    pointing_hidden(puzzle, Loc(5, 4))
    cross_hatch_cell_row_col_touching(puzzle, Loc(4, 4), PLUS)
    pointing_hidden(puzzle, Loc(5, 1))
    cross_hatch_cell_row_col_touching(puzzle, Loc(0, 6), PLUS)
    puzzle.grid[5][7].remove(MINUS)
    cross_hatch_cell_row_col_touching(puzzle, Loc(5, 7), PLUS)
    puzzle.grid[2][2].remove(PLUS)
    puzzle.grid[7][1].remove(PLUS)
    # x-wing
    puzzle.grid[6][3].remove(PLUS)
    puzzle.grid[6][5].remove(PLUS)
    print(puzzle)
    assert puzzle.is_solved()



