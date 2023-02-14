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

    # def __getitem__(self, __row)->list[Loc]:
    #     return
    # @property
    # def trees(self) -> int:
    #     return int(self.__json['trees'])

    # def cell_candidates(self, loc: Loc) -> list[str]:
    #     # string = self.__grid[loc.row][loc.col]
    #     # lst: list[str] = []
    #     # if PLUS in string:
    #     #     lst.append(PLUS)
    #     # if MINUS in string:
    #     #     lst.append(MINUS)
    #     # return lst
    #     return self.__grid[loc.row][loc.col]

    # def rem(self, locs: Loc | list[Loc] | set[Loc], candidates: iter) -> int:
    #     edits = 0
    #
    #     # print('made it here')
    #     if isinstance(locs, Loc):
    #         locs = [locs]
    #
    #     for loc in locs:
    #
    #         for candidate in candidates:
    #             cell_candidates = self.cell_candidates(loc)
    #             # if candidate not in cell_candidates:
    #             #     continue
    #
    #             current = len(self)
    #
    #             temp: list = self.__grid[loc.row][loc.col]
    #
    #             print(temp)
    #
    #             temp.remove(candidate)
    #
    #             edits += current - len(temp)
    #
    #             # self.__grid[loc.row][loc.col] = self.__grid[loc.row][loc.col].replace(str(candidate), "_")
    #
    #     return edits

    def __str__(self) -> str:
        __string = f'{self.id}\n'
        __string += f'{len(self)}\n'
        for __r in range(len(self)):
            for __c in range(len(self)):
                __string += f'{self.grid[__r][__c]}'.ljust(11) + ' '
            __string += '\n'
        __string += f'{self.trees}'
        return __string

    def pointing_arrows_hidden_single(self) -> int:
        edits = 0
        # for _r in range(len(self)):
        #     for _c in range(len(self)):
        #         _loc = Loc(_r, _c)
        #
        #         _cell_string = self.__grid[_r][_c]
        #
        #         print(_cell_string)
        #
        #         __house: list[Loc]
        #
        #         match _cell_string:
        #             case 'nn':
        #                 __house = _loc.north_locs()
        #             # case 'ww':
        #             #     __house = _loc.west_locs()
        #             # case 'ss':
        #             #     __house = _loc.south_locs(len(self))
        #             # case 'ee':
        #             #     __house = _loc.east_locs(len(self))
        #             # case 'ne':
        #             #     __house = _loc.north_east_locs(len(self))
        #             # case 'nw':
        #             #     __house = _loc.north_west_locs(len(self))
        #             # case 'se':
        #             #     __house = _loc.south_east_locs(len(self))
        #             # case 'sw':
        #             #     __house = _loc.south_west_locs(len(self))
        #             case _:
        #                 continue
        #
        #         __house = [_l for _l in __house if
        #                    len(self.cell_candidates(_l)) and PLUS in self.cell_candidates(_l)]
        #
        #         if len(__house) == 1:
        #             edits += self.rem([__house[0]], [MINUS])

        return edits

    def pointing_arrows_required_dominating(self) -> int:
        edits = 0
        # for _r in range(len(self)):
        #     for _c in range(len(self)):
        #         _loc = Loc(_r, _c)
        #
        #         _cell_string = set(self.__grid[_r][_c])
        #
        #         print(_cell_string)
        #
        #         __house: list[Loc]
        #
        #         match _cell_string:
        #             case 'nn':
        #                 __house = _loc.north_locs()
        #             case 'ww':
        #                 __house = _loc.west_locs()
        #             case 'ss':
        #                 __house = _loc.south_locs(len(self))
        #             case 'ee':
        #                 __house = _loc.east_locs(len(self))
        #             # case 'ne':
        #             #     __house = _loc.north_east_locs(len(self))
        #             # case 'nw':
        #             #     __house = _loc.north_west_locs(len(self))
        #             # case 'se':
        #             #     __house = _loc.south_east_locs(len(self))
        #             # case 'sw':
        #             #     __house = _loc.south_west_locs(len(self))
        #             case _:
        #                 continue
        #
        #         __house = [_l for _l in __house if
        #                    len(self.cell_candidates(_l)) and PLUS in self.cell_candidates(_l)]
        #
        #         if len(__house) == 2 and __house[0].is_next_to(__house[1]):
        #             if __house[0].in_same_row(__house[1]):
        #                 __required = [_l for _l in
        #                               [__house[0].north(), __house[1].north(), __house[0].south(), __house[1].south()]
        #                               if _l.is_valid_sudoku(len(self))]
        #
        #                 # if PLUS in
        #
        #                 edits += self.rem(__required, [PLUS])
        #
        #         # if len(__house) == 1:
        #         #     edits += self.rem([__house[0]], [MINUS])

        return edits

    def hidden_single_row_col(self) -> int:
        edits = 0

        # for __index in range(len(self)):
        #
        #     row_col_houses = [
        #         Loc.house_row(__index, len(self)),
        #         Loc.house_col(__index, len(self))
        #     ]
        #
        #     for house in row_col_houses:
        #
        #         __has_plus = [_l for _l in house if PLUS in self.cell_candidates(_l)]
        #
        #         if len(__has_plus) == 1:
        #             edits += self.rem(__has_plus, [MINUS])
        #
        #         # __loc = next((__loc for __loc in house if
        #         #               MINUS not in self.cell_candidates(__loc) and len(self.cell_candidates(__loc)) > 0), None)
        #         #
        #         # if __loc is None:
        #         #     continue
        #         #
        #         # house.remove(__loc)
        #         #
        #         # edits += self.rem(house, [PLUS])

        return edits

    def cross_hatch(self) -> int:
        edits = 0

        # for __index in range(len(self)):
        #
        #     row_col_houses = [
        #         Loc.house_row(__index, len(self)),
        #         Loc.house_col(__index, len(self))
        #     ]
        #
        #     for house in row_col_houses:
        #
        #         __loc = next((__loc for __loc in house if
        #                       MINUS not in self.cell_candidates(__loc) and len(self.cell_candidates(__loc)) > 0), None)
        #
        #         if __loc is None:
        #             continue
        #
        #         house.remove(__loc)
        #
        #         edits += self.rem(house, [PLUS])

        return edits

    def cross_hatch_touching(self) -> int:
        edits = 0

        # for _r in range(len(self)):
        #     for _c in range(len(self)):
        #         _loc = Loc(_r, _c)
        #
        #         if MINUS in self.cell_candidates(_loc):
        #             continue
        #
        #         if PLUS in self.cell_candidates(_loc):
        #             edits += self.rem(_loc.surrounding(len(self)), [PLUS])

        return edits

    def solve(self, techniques: iter = None) -> int:
        edits = 0
        while True:
            current_edits = 0

            # edits += current_edits

            current_edits += self.pointing_arrows_hidden_single()
            current_edits += self.cross_hatch()
            current_edits += self.hidden_single_row_col()
            current_edits += self.cross_hatch_touching()
            current_edits += self.pointing_arrows_required_dominating()

            edits += current_edits

            if current_edits == 0:
                break

        return edits

    def is_solved(self) -> bool:

        # expected = {{'-'},'_-', '+_', 'nn', 'ee', 'ww', 'ss', 'ne', 'nw', 'se', 'sw'}
        # for _r in range(len(self)):
        #     for _c in range(len(self)):
        #         __candidates = set(self.__grid[_r][_c])
        #
        #         if {'-'} == __candidates:
        #             continue
        #
        #         if {'+'} == __candidates:
        #             continue
        #
        #         print(__candidates)
        #
        #         return False

        # if "".join(self.__grid[_r][_c]) not in expected:
        #     # print(f'"{self.__grid[_r][_c]}" not in expected')
        #     return False
        # return True
        return False


def default_test_puzzle(puzzle_string, constructor, techniques) -> bool:
    puzzle = constructor(puzzle_string)
    edits = 0
    edit_dict = {}
    while True:
        original_edits = edits
        for tech in techniques:
            _edits = tech.solve0(puzzle)
            if tech.__class__.__name__ not in edit_dict:
                edit_dict[tech.__class__.__name__] = 0
            edit_dict[tech.__class__.__name__] += _edits
            edits = edits + _edits
        if original_edits == edits:
            break
    if puzzle.is_solved():
        return True
    for tech in edit_dict:
        if edit_dict[tech] == 0:
            continue
        print(f'{tech}: {edit_dict[tech]}')
    print(f'Total edits: {edits}')
    print(puzzle)
    return False


#      '"expected":' \
#         '   [' \
# '[["+","-"], ["+","-"],["+","-"],["+","-"],["+","-"]],\
# '[["+","-"], ["+","-"],["+","-"],["+","-"],["n","n"]],\
# '[["+","-"], ["+","-"],["+","-"],["+","-"],["+","-"]],\
# '[["+","-"], ["+","-"],["e","e"],["+","-"],["+","-"]],\
# '[["+","-"], ["+","-"],["+","-"],["+","-"],["+","-"]],\


# botanical_dict = json.loads(
#     '   "001.botanical_park": { '
#     '       "length" : 5, '
#     '       "trees"  : 1, '
#     '       "grid"   : '
#     '            ['
#     '               [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '               [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["n", "n"]], '
#     '               [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '               [["+", "-"], ["+", "-"], ["e", "e"], ["+", "-"], ["+", "-"]], '
#     '               [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]  '
#     '           ]'
#     '   }'
# )


# botanical_park_001 = json.loads(
#     '{ '
#     '   "id"     : "001.botanical_park", '
#     '   "length" : 5, '
#     '   "trees"  : 1, '
#     '   "grid"   : '
#     '       ['
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], "nn"      ], '
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], "ee",       ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]  '
#     '       ]'
#     '}'
# )

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

# botanical_park_004 = json.loads(
#     '{ '
#     '   "id"     : "002.botanical_park", '
#     '   "length" : 5, '
#     '   "trees"  : 1, '
#     '   "grid"   : '
#     '       ['
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], "ne",       ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], "nw",       ["+", "-"], ["+", "-"]], '
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]  '
#     '       ]'
#     '}'
# )


# tep =[["+", "-"], ["+", "-"]], ["+", "-"]], ["+", "-"]], ["+", "-"]], ["+", "-"]]


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


@pytest.mark.skip("SKIPPED")
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


@pytest.mark.skip("SKIPPED")
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


@pytest.mark.skip("SKIPPED")
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
    # assert puzzle.is_solved()
    assert False


# @pytest.mark.skip("SKIPPED")
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
    puzzle_string = f"""
    006.botanical_park
    6
    +- +- +- +- +- +-
    +- +- +- +- +- +-
    +- +- +- +- +- +-
    +- +- +- +- +- nw
    +- nw +- +- +- +-
    +- +- +- +- nw +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
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


def pointing_arrows_hidden_single(self) -> int:
    edits = 0
    # for _r in range(len(self)):
    #     for _c in range(len(self)):
    #         _loc = Loc(_r, _c)
    #
    #         _cell_string = self.__grid[_r][_c]
    #
    #         print(_cell_string)
    #
    #         __house: list[Loc]
    #
    #         match _cell_string:
    #             case 'nn':
    #                 __house = _loc.north_locs()
    #             # case 'ww':
    #             #     __house = _loc.west_locs()
    #             # case 'ss':
    #             #     __house = _loc.south_locs(len(self))
    #             # case 'ee':
    #             #     __house = _loc.east_locs(len(self))
    #             # case 'ne':
    #             #     __house = _loc.north_east_locs(len(self))
    #             # case 'nw':
    #             #     __house = _loc.north_west_locs(len(self))
    #             # case 'se':
    #             #     __house = _loc.south_east_locs(len(self))
    #             # case 'sw':
    #             #     __house = _loc.south_west_locs(len(self))
    #             case _:
    #                 continue
    #
    #         __house = [_l for _l in __house if
    #                    len(self.cell_candidates(_l)) and PLUS in self.cell_candidates(_l)]
    #
    #         if len(__house) == 1:
    #             edits += self.rem([__house[0]], [MINUS])

    return edits


# botanical_park_012 = json.loads(
#     '{ '
#     '   "id"     : "012.botanical_park", '
#     '   "length" : 8, '
#     '   "trees"  : 1, '
#     '   "grid"   : '
#     '       ['
#     '           [["+", "-"], ["+", "-"], ["s", "e"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["+", "-"], ["w", "w"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["s", "e"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["s", "s"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["+", "-"], ["n", "e"], ["+", "-"], ["+", "-"], ["n", "n"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]],'
#     '           [["+", "-"], ["+", "-"], ["n", "n"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]'
#     '       ]'
#     '}'
# )

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


# def pointing_required_next_to_same_row(puzzle: BotanicalPark, __loc: Optional[Loc] = None) -> int:

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
    # __neighbors = set(__neighbors)

    print(__neighbors)

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

    # __candidates = puzzle.grid[__cell.row][__cell.col]

    # if len(__candidates) != 1 or __candidate not in __candidates:
    #     return edits
    #
    # for __other in __neighbors:
    #     __other_candidates: list = puzzle.grid[__other.row][__other.col]
    #     if __candidate not in __other_candidates:
    #         continue
    #     __other_candidates.remove(__candidate)
    #     edits += 1

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

    # match(len(__candidates)):
    #     case 0:
    #         raise Exception('Found cell that is empty')
    #     case 1:
    #         pass
    #     case _:
    #         return edits
    #
    #
    #
    #
    # if len(__house) == 1 and MINUS in puzzle.grid[__house[0].row][__house[0].col]:
    #     temp: list = puzzle.grid[__house[0].row][__house[0].col]
    #     temp.remove(MINUS)
    #     edits += 1
    # edits += puzzle.rem([__house[0]], [MINUS])

    # return edits


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
