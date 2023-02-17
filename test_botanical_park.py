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
        self.cells: list[Loc] = []
        for r in range(len(self)):
            for c in range(len(self)):
                self.cells.append(Loc(r, c))

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


def pointing_hidden(puzzle: BotanicalPark, __candidate, __loc: Optional[Loc] = None) -> int:
    edits = 0
    if __loc is not None:
        _cell_string = puzzle.grid[__loc.row][__loc.col]
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
                   len(puzzle.grid[_l.row][_l.col]) and __candidate in puzzle.grid[_l.row][_l.col]]

        if len(__house) != 1:
            return edits
        # if len(__house) == 1 and MINUS in puzzle.grid[__house[0].row][__house[0].col]:
        #     temp: list = puzzle.grid[__house[0].row][__house[0].col]
        #     temp.remove(MINUS)
        #     edits += 1

        for __other in list(puzzle.grid[__house[0].row][__house[0].col]):
            if __other == __candidate:
                continue

            # if len(__house) == 1 and MINUS in puzzle.grid[__house[0].row][__house[0].col]:
            #     temp: list =
            puzzle.grid[__house[0].row][__house[0].col].remove(__other)
            edits += 1
        return edits
    for r in range(len(puzzle)):
        for c in range(len(puzzle)):
            edits += pointing_hidden(puzzle, __candidate, Loc(r, c))
    return edits


def pointing_required(puzzle: BotanicalPark, __candidate, __loc: Optional[Loc] = None) -> int:
    edits = 0

    if __loc is not None:
        _cell_string = puzzle.grid[__loc.row][__loc.col]
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

                    if __candidate in __candidates:
                        __candidates.remove(__candidate)
                        edits += 1

        return edits
    for r in range(len(puzzle)):
        for c in range(len(puzzle)):
            edits += pointing_required(puzzle, __candidate, Loc(r, c))
    return edits


def pointing_opposite_nsew(puzzle: BotanicalPark, __candidate, __loc: Optional[Loc] = None) -> int:
    edits = 0

    if puzzle.trees == 2:
        return edits

    if __loc is not None:
        _cell_string = puzzle.grid[__loc.row][__loc.col]
        __house: list[Loc]
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
            if __candidate in puzzle.grid[__l.row][__l.col]:
                puzzle.grid[__l.row][__l.col].remove(__candidate)
                edits += 1
        return edits
    for r in range(len(puzzle)):
        for c in range(len(puzzle)):
            edits += pointing_opposite_nsew(puzzle, __candidate, Loc(r, c))
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


def hidden_single_row_col(puzzle: BotanicalPark, __candidate) -> int:
    edits = 0
    for i in range(len(puzzle)):
        edits += hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_row(i, len(puzzle)))
        edits += hidden_single_cell_neighbors(puzzle, PLUS, Loc.house_col(i, len(puzzle)))
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


def cross_hatch_cell_row_col_touching(puzzle: BotanicalPark, __candidate, __cell: Loc | None = None) -> int:
    edits = 0

    if __cell is not None:
        edits += cross_hatch_cell_neighbors(puzzle, __cell, PLUS,
                                            Loc.house_row(__cell.row, len(puzzle)) + Loc.house_col(__cell.col,
                                                                                                   len(puzzle)))
        return cross_hatch_cell_neighbors(puzzle, __cell, PLUS, Loc.surrounding(__cell, len(puzzle))) + edits

    for r in range(len(puzzle)):
        for c in range(len(puzzle)):
            edits += cross_hatch_cell_row_col_touching(puzzle, PLUS, Loc(r, c))
    return edits


techs = [
    cross_hatch_cell_row_col_touching,
    pointing_hidden,
    hidden_single_row_col,
    pointing_required,
    pointing_opposite_nsew
]


def default_test(puzzle_string, edits=None) -> bool:
    puzzle = BotanicalPark(puzzle_string)

    if edits is not None:
        for edit in edits:
            r, c, candidate = edit

            puzzle.grid[r][c].remove(candidate)

    while sum(tech(puzzle, PLUS) for tech in techs) > 0:
        continue
    print(puzzle)
    return puzzle.is_solved()


def test_botanical_park_001():
    assert default_test(Constants.botanical_park_001)


def test_botanical_park_002():
    assert default_test(Constants.botanical_park_002, [
        (2, 0, PLUS),
        (1, 1, PLUS),
        (4, 2, PLUS),
    ])


def test_botanical_park_003():
    assert default_test(Constants.botanical_park_003)


def test_botanical_park_004():
    assert default_test(Constants.botanical_park_004)


def test_botanical_park_005():
    assert default_test(Constants.botanical_park_005, [(0, 0, PLUS)])


def test_botanical_park_006():
    assert default_test(Constants.botanical_park_006, [
        (2, 2, PLUS),
        (0, 1, PLUS),
        (1, 1, PLUS),
        (1, 4, PLUS),
        (1, 5, PLUS)
    ])


def test_botanical_park_007():
    assert default_test(Constants.botanical_park_007, [
        (4, 4, PLUS),
        (5, 4, PLUS),
        (1, 1, PLUS),
        (1, 4, PLUS),
        (1, 5, PLUS)
    ])


def test_botanical_park_008():
    assert default_test(Constants.botanical_park_008, [
        (0, 3, PLUS),
        (1, 3, PLUS)
    ])


def test_botanical_park_009():
    assert default_test(Constants.botanical_park_009, [
        (0, 1, PLUS),
        (2, 3, PLUS)
    ])


def test_botanical_park_010():
    assert default_test(Constants.botanical_park_010, [
        (7, 4, PLUS),
        (6, 5, PLUS)
    ])


def test_botanical_park_011():
    assert default_test(Constants.botanical_park_011, [(2, 5, PLUS)])


@pytest.mark.skip("SKIPPED")
def test_botanical_park_012():
    assert default_test(Constants.botanical_park_012, [
        (5, 7, MINUS),
        (2, 2, PLUS),
        (7, 1, PLUS),
        (6, 3, PLUS),
        (6, 5, PLUS),
    ])


@pytest.mark.skip("SKIPPED")
def test_botanical_park_014():
    puzzle = BotanicalPark(Constants.botanical_park_014)
    while sum(tech(puzzle, PLUS) for tech in techs) > 0:
        continue
    print(puzzle)
    assert puzzle.is_solved()
