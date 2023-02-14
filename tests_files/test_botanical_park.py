# from typing import Union
from typing import Optional

import numpy
import pytest
from colorama import Fore

from Loc import Loc
import json

PLUS = '+'
MINUS = '-'





class BotanicalPark:
    def __init__(self, __json) -> None:
        self.__json = __json
        self.id = self.__json['id']
        self.trees = self.__json['trees']
        temp = self.__json['grid']
        self.grid = []
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


botanical_park_001 = json.loads(
    '{ '
    '   "id"     : "001.botanical_park", '
    '   "length" : 5, '
    '   "trees"  : 1, '
    '   "grid"   : '
    '       ['
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "nn"      ], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], "ee",       ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]  '
    '       ]'
    '}'
)

botanical_park_002 = json.loads(
    '{ '
    '   "id"     : "002.botanical_park", '
    '   "length" : 5, '
    '   "trees"  : 1, '
    '   "grid"   : '
    '       ['
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], "ne",       ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], "nw",       ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]  '
    '       ]'
    '}'
)


botanical_park_004 = json.loads(
    '{ '
    '   "id"     : "004.botanical_park", '
    '   "length" : 6, '
    '   "trees"  : 1, '
    '   "grid"   : '
    '       ['
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           ["ne"      , ["+", "-"], "ww"      , ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "ss"      , ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]] '
    '       ]'
    '}'
)

botanical_park_005 = json.loads(
    '{ '
    '   "id"     : "005.botanical_park", '
    '   "length" : 6, '
    '   "trees"  : 1, '
    '   "grid"   : '
    '       ['
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "sw"      ], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "ne"      , ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], "ss"      , ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "nw"      ] '
    '       ]'
    '}'
)

botanical_park_006 = json.loads(
    '{ '
    '   "id"     : "006.botanical_park", '
    '   "length" : 6, '
    '   "trees"  : 1, '
    '   "grid"   : '
    '       ['
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "nw"      ], '
    '           [["+", "-"], "nw"      , ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "nw"      , ["+", "-"]] '
    '       ]'
    '}'
)



botanical_park_012 = json.loads(
    '{ '
    '   "id"     : "012.botanical_park", '
    '   "length" : 8, '
    '   "trees"  : 1, '
    '   "grid"   : '
    '       ['
    '           [["+", "-"], ["+", "-"], "se",       ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           [["+", "-"], "ww",       ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           ["se",       ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "ss",       ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           [["+", "-"], "ne",       ["+", "-"], ["+", "-"], "nn",       ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
    '           [["+", "-"], ["+", "-"], "nn",       ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]'
    '       ]'
    '}'
)


def test_botanical_park_001():
    puzzle = BotanicalPark(botanical_park_001)

    pointing_hidden(puzzle, Loc(1, 4))

    loc = Loc(0, 4)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    pointing_hidden(puzzle, Loc(3, 2))

    loc = Loc(3, 3)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    loc = Loc(1, 2)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(loc.col, len(puzzle)))

    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    loc = Loc(4, 1)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(loc.col, len(puzzle)))

    loc = Loc(4, 1)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    loc = Loc(1, 0)
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(loc.col, len(puzzle)))

    print(puzzle)
    assert puzzle.is_solved()


# @pytest.mark.skip("SKIPPED")
def test_botanical_park_002():
    puzzle = BotanicalPark(botanical_park_002)

    loc = Loc(1, 2)
    # cross_hatch_cell_neighbors(puzzle, loc, PLUS,
    #                            Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    # cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    pointing_hidden(puzzle, loc)

    # puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_003():
    puzzle_string = f"""
    003.botanical_park
    5
    +- +- +- +- +-
    +- +- ww +- +-
    +- +- +- +- +-
    +- +- +- +- +-
    +- +- nw +- nn
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()

    puzzle_string = str(puzzle)

    print(puzzle_string)

    assert puzzle.is_solved()


def test_botanical_park_004():
    puzzle = BotanicalPark(botanical_park_004)

    pointing_hidden(puzzle, Loc(2, 2))
    pointing_hidden(puzzle, Loc(4, 4))

    loc = Loc(2, 1)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    pointing_hidden(puzzle, Loc(2, 0))

    loc = Loc(5, 4)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

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

    # # puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


def test_botanical_park_005():
    puzzle = BotanicalPark(botanical_park_005)

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

    # loc =
    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(4, len(puzzle)))

    pointing_hidden(puzzle, Loc(0, 5))

    loc = Loc(4, 1)

    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    pointing_hidden(puzzle, Loc(5, 5))

    # explicit

    puzzle.grid[0][0].remove(MINUS)

    loc = Loc(0, 0)
    #
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    # cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(2, len(puzzle)))

    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_006():
    puzzle = BotanicalPark(botanical_park_006)

    pointing_hidden(puzzle, Loc(4,1))
    loc = Loc(3, 0)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))

    # print(Loc.surrounding(loc, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))

    pointing_hidden(puzzle, Loc(5,4))
    loc = Loc(4, 3)
    cross_hatch_cell_neighbors(puzzle, loc, PLUS,
                               Loc.house_row(loc.row, len(puzzle)) + Loc.house_col(loc.col, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, loc, PLUS, Loc.surrounding(loc, len(puzzle)))


    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_007():
    puzzle_string = f"""
    007.botanical_park
    7
    +- +- +- +- +- +- +-
    +- +- +- +- +- +- +-
    +- +- +- ne +- nn +-
    +- +- +- nw +- +- +-
    +- +- +- +- +- +- +-
    +- ss +- +- +- +- +-
    +- +- +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_008():
    puzzle_string = f"""
    008.botanical_park
    7
    +- +- +- +- +- ww +-
    +- +- +- +- +- +- +-
    +- +- +- +- +- +- +-
    +- +- nn sw +- +- +-
    +- +- +- +- +- +- +-
    +- +- +- +- +- +- +-
    +- ee +- +- nw +- nw
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_009():
    puzzle_string = f"""
    009.botanical_park
    7
    +- +- +- +- +- +- +-
    +- +- +- +- +- +- +-
    +- +- +- +- +- +- +-
    ne +- +- +- nw +- +-
    +- ne +- nn +- +- ww
    +- +- +- +- +- +- +-
    +- +- +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_010():
    puzzle_string = f"""
    010.botanical_park
    8
    +- +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- +-
    ne se +- ww +- +- +- +-
    +- +- +- +- nw +- ww sw
    +- +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_011():
    puzzle_string = f"""
    011.botanical_park
    8
    +- +- +- +- +- +- +- sw
    +- +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- sw
    +- ne +- +- +- +- +- +-
    +- +- ww +- +- +- +- +-
    +- +- +- ww +- +- +- +-
    +- +- +- +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


class BotanicalParkPointingHiddenSingle:
    def __int__(self, __loc: Optional[Loc] = None):
        self.__loc = __loc

    def solve_cell(self, __loc: Loc) -> int:
        edits = 0

        return edits

    def solve(self) -> int:
        edits = 0

        if self.__loc is not None:
            return self.solve_cell(self.__loc)

        return edits





@pytest.mark.skip("SKIPPED")
def test_botanical_park_012():
    # from Loc import Loc
    puzzle = BotanicalPark(botanical_park_012)

    pointing_hidden(puzzle, Loc(1, 1))
    cross_hatch_cell_neighbors(puzzle, Loc(1, 0), PLUS, Loc.house_row(1, len(puzzle)) + Loc.house_col(0, len(puzzle)))
    cross_hatch_cell_neighbors(puzzle, Loc(1, 0), PLUS, Loc.surrounding(Loc(1, 0), len(puzzle)))

    print(puzzle)
    assert puzzle.is_solved()
# 573
