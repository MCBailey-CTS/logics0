# from typing import Union

import numpy
import pytest
from colorama import Fore

from Loc import Loc
import json

PLUS = '+'
MINUS = '-'


class BotanicalPark:
    def __init__(self, __puzzle: str | dict) -> None:
        if isinstance(__puzzle, str):
            self.__is_json = False
            __array = []
            for line in __puzzle.replace('\n', ' ', -1).split(' '):
                if len(line) > 0:
                    __array.append(line)
            self.__id = __array.pop(0)
            self.__length = int(__array.pop(0))
            self.__trees = int(__array.pop(len(__array) - 1))

            self.__grid = numpy.reshape(__array, (len(self), len(self)))
        else:
            self.__is_json = True
            self.__json = __puzzle
            self.grid = self.__json['grid']
            self.__id = self.__json['id']
            # self.grid =   self.__grid

    def __len__(self) -> int:
        if self.__is_json:
            return int(self.__json['length'])
        return self.__length

    @property
    def trees(self) -> int:
        return int(self.__json['trees'])

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
        __string = f'{self.__id}\n'
        __string += f'{len(self)}\n'
        for __r in range(len(self)):
            for __c in range(len(self)):
                __loc = Loc(__r, __c)

                __cell_string = self.__grid[__r][__c]

                if __cell_string in ['nn', 'ss', 'ww', 'ee', 'ne', 'nw', 'se', 'sw', ]:
                    __string += f'{Fore.CYAN}{__cell_string}{Fore.RESET} '
                elif __cell_string == '+_':
                    __string += f'{Fore.GREEN}TT{Fore.RESET} '
                elif __cell_string == '_-':
                    __string += f'.. '
                else:
                    __string += f'{self.__grid[__r][__c]}'.ljust(11) + ' '
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


def test_botanical_park_001():
    t = json.loads(
        '{ '
        '   "id"     : "001.botanical_park", '
        '   "length" : 5, '
        '   "trees"  : 1, '
        '   "grid"   : '
        '       ['
        '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
        '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["n", "n"]], '
        '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]], '
        '           [["+", "-"], ["+", "-"], ["e", "e"], ["+", "-"], ["+", "-"]], '
        '           [["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"], ["+", "-"]]  '
        '       ]'
        '}'
    )
    puzzle = BotanicalPark(t)
    puzzle.solve()
    if puzzle.is_solved():
        return
    print(puzzle.grid)
    assert False


@pytest.mark.skip("SKIPPED")
def test_botanical_park_002():
    puzzle_string = f"""
    002.botanical_park
    5
    +- +- +- +- +-
    +- +- ne +- +-
    +- +- +- +- +-
    +- +- nw +- +-
    +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
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
    puzzle_string = f"""
    004.botanical_park
    6
    +- +- +- +- +- +-
    +- +- +- +- +- +-
    ne +- ww +- +- +-
    +- +- +- +- +- +-
    +- +- +- +- ss +-
    +- +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()


@pytest.mark.skip("SKIPPED")
def test_botanical_park_005():
    puzzle_string = f"""
    005.botanical_park
    6
    +- +- +- +- +- sw
    +- +- +- +- +- +-
    +- +- +- +- ne +-
    +- +- +- ss +- +-
    +- +- +- +- +- +-
    +- +- +- +- +- nw
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
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


@pytest.mark.skip("SKIPPED")
def test_botanical_park_012():
    puzzle_string = f"""
    012.botanical_park
    8
    +- +- se +- +- +- +- +-
    +- ww +- +- +- +- +- +-
    se +- +- +- +- +- +- +-
    +- +- +- +- ss +- +- +-
    +- +- +- +- +- +- +- +-
    +- ne +- +- nn +- +- +-
    +- +- +- +- +- +- +- +-
    +- +- nn +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)
    puzzle.solve()
    print(puzzle)
    assert puzzle.is_solved()
# 573
