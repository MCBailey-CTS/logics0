# from typing import Union

import numpy
import pytest
from colorama import Fore

from Loc import Loc

PLUS = '+'
MINUS = '-'


class BotanicalPark:
    def __init__(self, __puzzle: str) -> None:
        __array = []
        for line in __puzzle.replace('\n', ' ', -1).split(' '):
            if len(line) > 0:
                __array.append(line)
        self.__id = __array.pop(0)
        self.__length = int(__array.pop(0))
        self.__trees = int(__array.pop(len(__array) - 1))

        self.__grid = numpy.reshape(__array, (len(self), len(self)))

    def __len__(self) -> int:
        return self.__length

    @property
    def trees(self) -> int:
        return self.__trees

    def cell_candidates(self, loc: Loc) -> list[str]:
        string = self.__grid[loc.row][loc.col]
        lst: list[str] = []
        if PLUS in string:
            lst.append(PLUS)
        if MINUS in string:
            lst.append(MINUS)
        return lst

    def rem(self, locs: Loc | list[Loc] | set[Loc], candidates: iter) -> int:
        edits = 0
        if isinstance(locs, Loc):
            locs = [locs]

        for loc in locs:

            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.__grid[loc.row][loc.col] = self.__grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits

    def __str__(self) -> str:
        __string = f'{self.__id}\n'
        __string += f'{len(self)}\n'
        for __r in range(len(self)):
            for __c in range(len(self)):
                __loc = Loc(__r, __c)

                __cell_string = self.__grid[__r][__c]

                match __cell_string:
                    case 'nn':
                        __string += f'{Fore.CYAN}⇑⇑{Fore.RESET} '
                    case '+_':
                        __string += f'{Fore.GREEN}TT{Fore.RESET} '
                    case _:
                        __string += f'{self.__grid[__r][__c]} '
            __string += '\n'
        __string += f'{self.__trees}'
        return __string

    def solve(self) -> int:
        edits = 0
        while True:
            current_edits = 0

            edits += current_edits

            for __r in range(len(self)):
                for __c in range(len(self)):
                    __loc = Loc(__r, __c)

                    __cell_string = self.__grid[__r][__c]

                    match __cell_string:
                        case 'nn':
                            pass
                            __north = __loc.north_locs()

                            if len(__north) == 1:
                                edits += self.rem([__north[0]], [MINUS])

                        case _:
                            pass

            temp = [Loc(0, __c) for __c in range(len(self))]

            temp_string = "".join(self.__grid[__l.row][__l.col] for __l in temp)

            print(temp_string)

            # for __index in range(len(self)):
            #     row_col_houses = [
            #         # Loc.row_house_locs(len(self))
            #         [Loc(__index, __c) for __c in range(len(self))]
            #     ]
            #
            #     for house in row_col_houses:
            #
            #         # print(house)
            #
            #         solved_as_trees = [__loc for __loc in house if MINUS not in self.cell_candidates(__loc)]
            #
            #         print(solved_as_trees)
            #
            #         if len(solved_as_trees) != self.__trees:
            #             continue
            #
            #         ttt = list(set(solved_as_trees).difference(house))
            #
            #         print(ttt)

            # edits += self.rem(, [PLUS])

            if current_edits == 0:
                break

        return edits


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


# @pytest.mark.skip("SKIPPED")
def test_botanical_park_001():
    puzzle_string = f"""
    001.botanical_park
    5
    +- +- +- +- +-
    +- +- +- +- nn
    +- +- +- +- +-
    +- +- ee +- +-
    +- +- +- +- +-
    1
    """
    puzzle = BotanicalPark(puzzle_string)

    puzzle.solve()

    print(puzzle)

    assert False
#     return f"""

#     1
#     """

# @staticmethod
# def botanical_park_002():
#     return f"""
#     002.botanical_park
#     5
#     +- +- +- +- +-
#     +- +- ne +- +-
#     +- +- +- +- +-
#     +- +- nw +- +-
#     +- +- +- +- +-
#     1
#     """

# @staticmethod
# def botanical_park_003():
#     return f"""
#     003.botanical_park
#     5
#     +- +- +- +- +-
#     +- +- ww +- +-
#     +- +- +- +- +-
#     +- +- +- +- +-
#     +- +- nw +- nn
#     1
#     """

# @staticmethod
# def botanical_park_004():
#     return f"""
#     004.botanical_park
#     6
#     +- +- +- +- +- +-
#     +- +- +- +- +- +-
#     ne +- ww +- +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- ss +-
#     +- +- +- +- +- +-
#     1
#     """

# @staticmethod
# def botanical_park_005():
#     return f"""
#     005.botanical_park
#     6
#     +- +- +- +- +- sw
#     +- +- +- +- +- +-
#     +- +- +- +- ne +-
#     +- +- +- ss +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- +- nw
#     1
#     """

# @staticmethod
# def botanical_park_006():
#     return f"""
#     006.botanical_park
#     6
#     +- +- +- +- +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- +- nw
#     +- nw +- +- +- +-
#     +- +- +- +- nw +-
#     1
#     """

# @staticmethod
# def botanical_park_007():
#     return f"""
#     007.botanical_park
#     7
#     +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- +- ne +- nn +-
#     +- +- +- nw +- +- +-
#     +- +- +- +- +- +- +-
#     +- ss +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     1
#     """

# @staticmethod
# def botanical_park_008():
#     return f"""
#     008.botanical_park
#     7
#     +- +- +- +- +- ww +-
#     +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- nn sw +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- ee +- +- nw +- nw
#     1
#     """

# @staticmethod
# def botanical_park_009():
#     return f"""
#     009.botanical_park
#     7
#     +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     ne +- +- +- nw +- +-
#     +- ne +- nn +- +- ww
#     +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     1
#     """

# @staticmethod
# def botanical_park_010():
#     return f"""
#     010.botanical_park
#     8
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     ne se +- ww +- +- +- +-
#     +- +- +- +- nw +- ww sw
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     1
#     """

# @staticmethod
# def botanical_park_011():
#     return f"""
#     011.botanical_park
#     8
#     +- +- +- +- +- +- +- sw
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- sw
#     +- ne +- +- +- +- +- +-
#     +- +- ww +- +- +- +- +-
#     +- +- +- ww +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     1
#     """

# @staticmethod
# def botanical_park_012():
#     return f"""
#     012.botanical_park
#     8
#     +- +- se +- +- +- +- +-
#     +- ww +- +- +- +- +- +-
#     se +- +- +- +- +- +- +-
#     +- +- +- +- ss +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- ne +- +- nn +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- nn +- +- +- +- +-
#     1
#     """
