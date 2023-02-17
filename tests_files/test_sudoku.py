# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing
import numpy
import pytest

from Loc import Loc
from Puzzle import Puzzle
from _defaults import default_test_puzzle
from techniques import *
from techniques.AlmostLockedCandidatesClaiming import AlmostLockedCandidatesClaiming
from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques.AvoidableRectangleType2 import AvoidableRectangleType2
from techniques.Bug import Bug
from techniques.CrossHatch import CrossHatch
from techniques.HiddenSingle import HiddenSingle
from techniques.HiddenUniqueRectangle import HiddenUniqueRectangle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType3 import UniqueRectangleType3
from techniques.UniqueRectangleType4 import UniqueRectangleType4
from techniques.WxyzWing import WxyzWing
from techniques.XyWing import XyWing
from techniques.XyzWing import XyzWing


# from tests_explicit.test_small_explicit import solve


class Sudoku(Puzzle):

    def __init__(self, puzzle: str | numpy.ndarray, length: int | None = None,
                 id: str | None = None) -> None:
        super().__init__(puzzle, length, id)

        self.__unsolved_locs: set[Loc] = set()

        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)

                candidates = self.cell_candidates(loc)

                if len(candidates) == 0 or len(candidates) == 1 and candidates[0] == 0:
                    new_string = ""

                    for candidate in self.expected_candidates():
                        new_string += f'{candidate}'

                    if self.has_fences:
                        new_string += f'{self.cell_fence(loc)}'

                    self.grid[r][c] = new_string
                else:
                    new_string = ""

                    for candidate in self.expected_candidates():
                        if candidate in candidates:
                            new_string += f'{candidate}'
                        else:
                            new_string += '_'

                    if self.has_fences:
                        new_string += f'{self.cell_fence(loc)}'

                    self.grid[r][c] = new_string

                if len(self.cell_candidates(loc)) > 1:
                    self.__unsolved_locs.add(loc)

    # def rem(self, locs: Loc| list[Loc]| set[Loc], candidates: iter) -> int:
    def rem(self, locs: Loc | list[Loc] | set[Loc], candidates: iter) -> int:
        edits = 0
        if isinstance(locs, Loc):
            return self.rem([locs], candidates)
        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                if len(cell_candidates) == 1:
                    raise Exception(f'Cannot remove final candidate {candidate} from Loc {loc}')
                if len(cell_candidates) == 2:
                    self.__unsolved_locs.remove(loc)
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1
        return edits

    # def __repr__(self):
    #     return 'Sudoku()'

    def unsolved_cells(self) -> set[Loc]:
        # unsolved = set()
        # for r in range(self.length):
        #     for c in range(self.length):
        #         loc = Loc(r, c)
        #         if len(self.cell_candidates(loc)) == 1:
        #             continue
        #         unsolved.add(loc)
        # return unsolved
        return self.__unsolved_locs

    def any_cell_is_solved(self, locs) -> bool:
        return [len(self.cell_candidates(loc)) == 1 for loc in locs] > 0

    def list_all_cell_locs(self) -> list[Loc]:
        locs = []
        for r in range(len(self)):
            for c in range(len(self)):
                locs.append(Loc(r, c))
        return locs

    def is_solved(self) -> bool:
        for house in self.houses_rows_cols_fences():
            solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
                                 len(self.cell_candidates(loc)) == 1]

            if len(solved_candidates) != len(self):
                print("house wasn't completely solved")
                return False

            expected = set(self.expected_candidates())

            if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
                continue

            print(solved_candidates)

            return False

        return True

    def row_chute(self, loc: Loc) -> int:
        if len(self) != 9:
            raise Exception("Can only ask for row chute of 9x9 sudoku")
        if loc.row < 0:
            raise Exception(f'Invalid loc to ask row chute for {loc}')
        if loc.row < 3:
            return 0
        elif loc.row < 6:
            return 1
        elif loc.row < 9:
            return 2
        raise Exception(f'Invalid loc to ask row chute for {loc}')

    def col_chute(self, loc: Loc) -> int:
        if len(self) != 9:
            raise Exception("Can only ask for col chute of 9x9 sudoku")
        if loc.col < 0:
            raise Exception(f'Invalid loc to ask col chute for {loc}')
        if loc.col < 3:
            return 0
        elif loc.col < 6:
            return 1
        elif loc.col < 9:
            return 2
        raise Exception(f'Invalid loc to ask col chute for {loc}')

    def loc_chute(self, loc: Loc) -> Loc:
        return Loc(self.row_chute(loc), self.col_chute(loc))

    def fence_from_chute(self, chute_loc: Loc) -> str:
        r, c = chute_loc

        if r == 0 and c == 0:
            return self.cell_fence(Loc(0, 0))

        if r == 0 and c == 1:
            return self.cell_fence(Loc(0, 3))

        if r == 0 and c == 2:
            return self.cell_fence(Loc(0, 6))

        if r == 1 and c == 0:
            return self.cell_fence(Loc(3, 0))

        if r == 1 and c == 1:
            return self.cell_fence(Loc(3, 3))

        if r == 1 and c == 2:
            return self.cell_fence(Loc(3, 6))

        if r == 2 and c == 0:
            return self.cell_fence(Loc(6, 0))

        if r == 2 and c == 1:
            return self.cell_fence(Loc(6, 3))

        if r == 2 and c == 2:
            return self.cell_fence(Loc(6, 6))

        raise Exception(f'Invalid chute loc: {chute_loc}')

    def fence_dict(self, loc_set):
        pass

    def to_string(self, include_colors=True) -> str:
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self)):
            if (len(self) == 9 and (r == 3 or r == 6)) or (len(self) == 4 and (r == 2)):
                string += '\n'
            for c in range(len(self)):
                if (len(self) == 9 and (c == 3 or c == 6)) or (len(self) == 4 and (c == 2)):
                    string += '   '
                loc = Loc(r, c)
                if include_colors and loc in self.color_override:
                    string += f'{self.color_override[loc]}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
                    continue
                if len(self.cell_candidates(loc)) == 0:
                    string += f'{Fore.GREEN}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
                else:
                    string += f'{self.grid[r][c].ljust(len(self))} '
            string += '\n'
        return string


# @staticmethod
def sudoku_techniques() -> list:
    return [
        CrossHatch(),
        HiddenSingle(),
        NakedPair(),
        LockedCandidatesPointing(),
        LockedCandidatesClaiming(),
        UniqueRectangleType1(),
        UniqueRectangleType2(),
        UniqueRectangleType4(),
        # FinnedXWing(),
        Bug(),
        tech.HiddenPair(),
        # tech.NakedTriple(),
        # tech.XWing(),
        # XyWing(),
        # SwordFish(),
        # JellyFish(),
    ]


def to_sudoku(length: int, actual: str, _id: str) -> Sudoku:
    newcan = "".join(str(num + 1) for num in range(length))

    underscore = "".join('_' for _ in range(length))
    string = actual
    string = string.replace('\n', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1) \
        .replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace(underscore, newcan).strip()

    temp = numpy.array(string.split(' '), str) \
        # .reshape((length, length))

    # if reshape is None:
    temp = temp.reshape((length, length))

    # else:
    #     temp = temp.reshape(reshape)

    return Sudoku(temp, length, _id)


def solve(length, actual, expected, technique):
    actual0 = to_sudoku(length, actual, '_actual')

    edits = technique.solve0(actual0)

    if expected is None:
        return edits == 0

    expected0 = to_sudoku(length, expected, '_expected')

    if actual0 == expected0:
        return True

    # for r in range(len(actual)):
    #     for c in range(len(actual)):
    #         if actual0.grid[r][c] != expected0.grid[r][c]:
    #             expected0.override_loc_color([Loc(r, c)], Fore.CYAN)

    print(actual0.to_string())
    print(expected0.to_string())
    return False


EXPLICITLY = "EXPLICITLY"

from pytest import mark


def test_4x4_cross_hatch():
    actual = \
        f"""
        1___a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        1___a _234a   _234b _234b
        _234a _234a   ____b ____b

        _234c ____c   ____d ____d
        _234c ____c   ____d ____d
            """
    if solve(4, actual, expected, CrossHatch()):
        return
    assert False


def test_9x9_cross_hatch():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    ____5____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """
    expected = \
        f"""
    1234_6789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    1234_6789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    1234_6789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    1234_6789d 1234_6789d 1234_6789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    ____5____d 1234_6789d 1234_6789d    1234_6789e 1234_6789e 1234_6789e    1234_6789f 1234_6789f 1234_6789f 
    1234_6789d 1234_6789d 1234_6789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    1234_6789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    1234_6789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    1234_6789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """
    if solve(9, actual, expected, CrossHatch()):
        return
    assert False


def test_sudoku_4x4_hidden_single_rows():
    actual = \
        f"""
        123_a 123_a   123_b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        123_a 123_a   123_b ___4b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, HiddenSingle()):
        return
    assert False


def test_sudoku_4x4_hidden_single_cols():
    actual = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        123_c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        123_c ____c   ____d ____d
        ___4c ____c   ____d ____d
        """
    if solve(4, actual, expected, HiddenSingle()):
        return
    assert False


def test_sudoku_4x4_hidden_single_fences():
    actual = \
        f"""
        123_a 123_a   ____b ____b
        123_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        123_a 123_a   ____b ____b
        123_a ___4a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, HiddenSingle()):
        return
    assert False


def test_sudoku_explicit_hidden_single_cols():
    actual = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c 1234_6789c
    _________a _________a _________a    _________b _________b _________b    _________c _________c 1234_6789c
    _________a _________a _________a    _________b _________b _________b    _________c _________c 1234_6789c

    _________d _________d _________d    _________e _________e _________e    _________f _________f 1234_6789f
    _________d _________d _________d    _________e _________e _________e    _________f _________f 1234_6789f
    _________d _________d _________d    _________e _________e _________e    _________f _________f 1234_6789f

    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g    _________h _________h _________h    _________i _________i 1234_6789i
    _________g _________g _________g    _________h _________h _________h    _________i _________i 1234_6789i
    """

    expected = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c 1234_6789c
    _________a _________a _________a    _________b _________b _________b    _________c _________c 1234_6789c
    _________a _________a _________a    _________b _________b _________b    _________c _________c 1234_6789c

    _________d _________d _________d    _________e _________e _________e    _________f _________f 1234_6789f
    _________d _________d _________d    _________e _________e _________e    _________f _________f 1234_6789f
    _________d _________d _________d    _________e _________e _________e    _________f _________f 1234_6789f

    _________g _________g _________g    _________h _________h _________h    _________i _________i ____5____i
    _________g _________g _________g    _________h _________h _________h    _________i _________i 1234_6789i
    _________g _________g _________g    _________h _________h _________h    _________i _________i 1234_6789i
    """
    if solve(9, actual, expected, HiddenSingle()):
        return
    assert False


def test_sudoku_explicit_hidden_single_fences():
    actual = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    1234_6789i 1234_6789i 1234_6789i
    _________g _________g _________g    _________h _________h _________h    1234_6789i _________i 1234_6789i
    _________g _________g _________g    _________h _________h _________h    1234_6789i 1234_6789i 1234_6789i
    """

    expected = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    1234_6789i 1234_6789i 1234_6789i
    _________g _________g _________g    _________h _________h _________h    1234_6789i ____5____i 1234_6789i
    _________g _________g _________g    _________h _________h _________h    1234_6789i 1234_6789i 1234_6789i
    """
    if solve(9, actual, expected, HiddenSingle()):
        return
    assert False


def test_sudoku_explicit_hidden_single_rows():
    actual = \
        f"""
    _________a _________a _________a   _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a   _________b _________b _________b    _________c _________c _________c
    1234_6789a 1234_6789a 1234_6789a   _________b 1234_6789b 1234_6789b    1234_6789c 1234_6789c 1234_6789c
    _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
    _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
    """

    expected = \
        f"""
    _________a _________a _________a   _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a   _________b _________b _________b    _________c _________c _________c
    1234_6789a 1234_6789a 1234_6789a   ____5____b 1234_6789b 1234_6789b    1234_6789c 1234_6789c 1234_6789c
    _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
    _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
    """
    if solve(9, actual, expected, HiddenSingle()):
        return
    assert False


def test_locked_candidates_pointing_rows():
    actual = \
        f"""
        123_a 123_a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        123_a 123_a   ____b ____b
        ____a ____a   123_b 123_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, LockedCandidatesPointing()):
        return
    assert False


def test_locked_candidates_pointing_cols():
    actual = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        ____c 123_c   ____d ____d
        ____c 123_c   ____d ____d
        """
    if solve(4, actual, expected, LockedCandidatesPointing()):
        return
    assert False


# sudoku_explicit_locked_candidates_pointing_2_fins_cols_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 12_456789b 12_456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_locked_candidates_pointing_2_fins_cols_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 12_456789b 12_456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_locked_candidates_pointing_2_fins_rows_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
#
# sudoku_explicit_locked_candidates_pointing_2_fins_rows_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 12345678_g 12345678_g 12345678_g    12345678_h 12345678_h 12345678_h    123456789i 123456789i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
#
# sudoku_explicit_locked_candidates_pointing_3_fins_cols_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_locked_candidates_pointing_3_fins_cols_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_locked_candidates_pointing_3_fins_rows_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
#
# sudoku_explicit_locked_candidates_pointing_3_fins_rows_expected
#
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 12345678_g 12345678_g 12345678_g    12345678_h 12345678_h 12345678_h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i


def test_locked_candidates_claiming_rows():
    actual = \
        f"""
        123_a 123_a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        123_a 123_a   ____b ____b
        ____a ____a   123_b 123_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, LockedCandidatesClaiming()):
        return
    assert False


def test_locked_candidates_claiming_cols():
    actual = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        ____c 123_c   ____d ____d
        ____c 123_c   ____d ____d
        """
    if solve(4, actual, expected, LockedCandidatesClaiming()):
        return
    assert False


def test_sudoku_explicit_locked_candidates_claiming_2_fins_rows():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f

    12345678_g 12345678_g 12345678_g    12345678_h 12345678_h 12345678_h    12345678_i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
    """
    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f

    12345678_g 12345678_g 12345678_g    12345678_h 12345678_h 12345678_h    12345678_i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
    """
    if solve(9, actual, expected, LockedCandidatesClaiming()):
        return
    assert False


def test_sudoku_explicit_locked_candidates_claiming_3_fins_cols():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c

    123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f

    123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
    """
    expected = \
        f"""
    123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    12_456789b 123456789b 12_456789b    123456789c 123456789c 123456789c

    123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 12_456789e 123456789e    123456789f 123456789f 123456789f

    123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 12_456789h 123456789h    123456789i 123456789i 123456789i
    """
    if solve(9, actual, expected, LockedCandidatesClaiming()):
        return
    assert False


def test_sudoku_explicit_locked_candidates_claiming_3_fins_rows():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f

    12345678_g 12345678_g 12345678_g    12345678_h 12345678_h 12345678_h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
    """
    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f

    12345678_g 12345678_g 12345678_g    12345678_h 12345678_h 12345678_h    123456789i 123456789i 123456789i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12345678_i 12345678_i 12345678_i
    """
    if solve(9, actual, expected, LockedCandidatesClaiming()):
        return
    assert False


def test_sudoku_explicit_naked_pair_cols():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e _______89e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h _______89h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """

    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 1234567__b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 1234567__b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 1234567__b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e _______89e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 1234567__e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 1234567__e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 1234567__h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h _______89h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 1234567__h 123456789h    123456789i 123456789i 123456789i 
    """
    if solve(9, actual, expected, NakedPair()):
        return
    assert False


def test_sudoku_explicit_naked_pair_fences():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e _______89e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e _______89e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """

    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    1234567__e _______89e 1234567__e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    1234567__e 1234567__e 1234567__e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    1234567__e 1234567__e _______89e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """
    if solve(9, actual, expected, NakedPair()):
        return
    assert False


def test_sudoku_explicit_naked_pair_rows():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e _______89e 123456789e    _______89f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """

    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    1234567__d 1234567__d 1234567__d    1234567__e _______89e 1234567__e    _______89f 1234567__f 1234567__f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """
    if solve(9, actual, expected, NakedPair()):
        return
    assert False


def test_sudoku_4x4_ur1_row_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c __34c   ____d 1234d
            ____c __34c   ____d __34d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c __34c   ____d 12__d
            ____c __34c   ____d __34d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_ne_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c __34c   ____d 1234d
            __34c ____c   ____d __34d
            """,
             None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_nw():
    if solve(4,
             f"""
            ____a 1234a   _23_b ____b
            ____a _23_a   _23_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 1__4a   _23_b ____b
            ____a _23_a   _23_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_nw_control():
    if solve(4,
             f"""
            ____a 1234a   _23_b ____b
            ____a _23_a   ____b ____b

            ____c ____c   _23_d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_se():
    if solve(4,
             f"""
            ____a 12__a   ____b 12__b
            ____a 12__a   ____b 1234b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 12__a   ____b 12__b
            ____a 12__a   ____b __34b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_se_control():
    if solve(4,
             f"""
            ____a 12__a   ____b 12__b
            ____a ____a   ____b 1234b

            ____c 12__c   12__d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_sw():
    if solve(4,
             f"""
            ____a __34a   __34b ____b
            ____a 1234a   __34b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a __34a   __34b ____b
            ____a 12__a   __34b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_sw_control():
    if solve(4,
             f"""
            ____a __34a   __34b ____b
            ____a 1234a   ____b __34b

            ____c ____c   ____d ____d
            ____c ____c   __34d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1__4b 1234b

            ____c ____c   1__4d 1__4d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1__4b _23_b

            ____c ____c   1__4d 1__4d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_ne_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a 1__4a   1__4b 1234b

            ____c 1__4c   ____d 1__4d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_nw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            1234a __34a   ____b ____b

            __34c __34c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            12__a __34a   ____b ____b

            __34c __34c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_nw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            1234a ____a   __34b ____b

            __34c __34c   __34d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_se():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   12__d 1234d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   12__d __34d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_se_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a 12__a   12__b 12__b

            ____c 12__c   ____d 1234d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_sw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   1234d 12__d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   __34d 12__d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_sw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a 12__a   12__b ____b

            ____c 12__c   1234d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_north_east_col_chute():
    if solve(9,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 1___5____f 1__45____f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 1___5____i 1___5____i 

        """,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 1___5____f ___4_____f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 1___5____i 1___5____i 

        """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_north_west_col_chute():
    if solve(9,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
1___5__8_d ____5__8_d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

____5__8_g ____5__8_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """,
             f"""
             123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
1________d ____5__8_d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

____5__8_g ____5__8_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 



            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_south_west_col_chute():
    if solve(9,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    ___45____c ___45____c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    ___456___f ___45____f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    ___45____c ___45____c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _____6___f ___45____f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_north_west_row_chute():
    if solve(9,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

123456789g 123456789g 123456789g    123456789h __34__7__h 123456789h    123456789i 123456789i __3___7__i 
123456789g 123456789g 123456789g    123456789h __3___7__h 123456789h    123456789i 123456789i __3___7__i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

123456789g 123456789g 123456789g    123456789h ___4_____h 123456789h    123456789i 123456789i __3___7__i 
123456789g 123456789g 123456789g    123456789h __3___7__h 123456789h    123456789i 123456789i __3___7__i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_south_east_col_chute():
    if solve(9,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
___4_6___a ___4_6___a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

___4_6___g ___4_6_8_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
___4_6___a ___4_6___a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

___4_6___g _______8_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_south_east_row_chute():
    if solve(9,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    _______89b 123456789b 123456789b    123456789c 123456789c _______89c 
123456789a 123456789a 123456789a    _______89b 123456789b 123456789b    123456789c 123456789c ____5__89c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    _______89b 123456789b 123456789b    123456789c 123456789c _______89c 
123456789a 123456789a 123456789a    _______89b 123456789b 123456789b    123456789c 123456789c ____5____c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_9x9_unique_rectangle_type1_south_west_row_chute():
    if solve(9,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e __3__6___e    123456789f __3__6___f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 1_3__6___e    123456789f __3__6___f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """,
             f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e __3__6___e    123456789f __3__6___f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 1________e    123456789f __3__6___f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 

            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur2_normal_east():
    actual = \
        f"""
        ____a _23_a   123_b 123_b
        ____a _23_a   ____b 123_b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a _23_a   _23_b 123_b
        ____a _23_a   _234b 123_b
        ____c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_goofy_east():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   12__b 123_b
        ____c ____c   12__d 123_d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b 12_4b
        ____a ____a   12__b 123_b
        ____c ____c   12__d 123_d
        ____c ____c   ____d 12_4d
        """

    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_north():
    actual = \
        f"""
        ____a 123_a   ____b ____b
        123_a 123_a   ____b ____b
        12__c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a 12__a   ____b ____b
        123_a 123_a   12_4b 12_4b
        12__c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_north():
    actual = \
        f"""
        ____a 123_a   123_b ____b
        ____a _23_a   _23_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        _234a 123_a   123_b _234b
        ____a _23_a   _23_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_normal_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   12__d ____d
        ____c 123_c   12__d ____d
        """
    expected = \
        f"""
        ____a 12_4a   ____b ____b
        ____a 12_4a   ____b ____b
        12__c 123_c   12__d ____d
        12_4c 123_c   12__d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a 12__a   ____b ____b
        123_c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a ____a   ____b ____b
        123_a 12__a   ____b ____b
        123_c 12__c   ____d ____d
        12_4c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_south():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   ____d ____d
        123_c ____c   ____d ____d
        """
    expected = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   12_4d 12_4d
        12__c 12_4c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_south():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a 123_a   123_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a 12__a   12__b ____b
        12_4a 123_a   123_b 12_4b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_normal_east_control():
    actual = \
        f"""
        ____a _23_a   123_b 123_b
        ____a ____a   ____b ____b
        ____c _23_c   ____d 123_d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_goofy_east_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 12__a   ____b 123_b
        ____c 12__c   ____d 123_d
        ____c ____c   ____d ____d
        """

    expected = None

    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_north_control():
    actual = \
        f"""
        ____a ____a   123_b ____b
        123_a ____a   123_b ____b
        12__c ____c   12__d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_north_control():
    actual = \
        f"""
        ____a 123_a   123_b ____b
        ____a ____a   ____b ____b
        ____c _23_c   ____d ____d
        ____c ____c   _23_d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_normal_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   12__b ____b
        123_c 123_c   ____d ____d
        ____c 123_c   12__d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a ____a   12__b ____b
        123_c ____c   12__d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_south_control():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        123_c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_south_control():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_goofy_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _2__5____a _2__5__8_a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _2__5____d _2__5__8_d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a 1234567_9a    _________b _________b _________b    _________c _________c _________c
        _________a _2__5____a _2__5__8_a    _________b _________b _________b    _________c _________c _________c
        _________a _________a 1234567_9a    _________b _________b _________b    _________c _________c _________c

        _________d _2__5____d _2__5__8_d    _________e _________e _________e    _________f _________f _________f
        _________d _________d 1234567_9d    _________e _________e _________e    _________f _________f _________f
        _________d _________d 1234567_9d    _________e _________e _________e    _________f _________f _________f

        _________g _________g 1234567_9g    _________h _________h _________h    _________i _________i _________i
        _________g _________g 1234567_9g    _________h _________h _________h    _________i _________i _________i
        _________g _________g 1234567_9g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_goofy_north():
    actual = \
        f"""
        _________a _________a __345____a    __345____b _________b _________b    _________c _________c _________c
        _________a _________a __3_5____a    __3_5____b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        123_56789a 123_56789a __345____a    __345____b 123_56789b 123_56789b    123_56789c 123_56789c 123_56789c
        _________a _________a __3_5____a    __3_5____b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_goofy_south():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g ______7_9g    ______7_9h _________h _________h    _________i _________i _________i
        _________g _________g ______789g    ______789h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g ______7_9g    ______7_9h _________h _________h    _________i _________i _________i
        1234567_9g 1234567_9g ______789g    ______789h 1234567_9h 1234567_9h    1234567_9i 1234567_9i 1234567_9i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_goofy_west():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d 123______d 12_______d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g 123______g 12_______g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a 12_456789a _________a    _________b _________b _________b    _________c _________c _________c
        _________a 12_456789a _________a    _________b _________b _________b    _________c _________c _________c
        _________a 12_456789a _________a    _________b _________b _________b    _________c _________c _________c

        _________d 12_456789d _________d    _________e _________e _________e    _________f _________f _________f
        _________d 123______d 12_______d    _________e _________e _________e    _________f _________f _________f
        _________d 12_456789d _________d    _________e _________e _________e    _________f _________f _________f

        _________g 123______g 12_______g    _________h _________h _________h    _________i _________i _________i
        _________g 12_456789g _________g    _________h _________h _________h    _________i _________i _________i
        _________g 12_456789g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_normal_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 12_______d    _________e _________e _________e    _________f _________f 123______f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d 12_______d    _________e _________e _________e    _________f _________f 123______f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c 12_456789c
        _________a _________a _________a    _________b _________b _________b    _________c _________c 12_456789c
        _________a _________a _________a    _________b _________b _________b    _________c _________c 12_456789c

        _________d _________d 12_______d    _________e _________e _________e    12_456789f 12_456789f 123______f
        _________d _________d _________d    _________e _________e _________e    12_456789f 12_456789f 12_456789f
        _________d _________d 12_______d    _________e _________e _________e    12_456789f 12_456789f 123______f

        _________g _________g _________g    _________h _________h _________h    _________i _________i 12_456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i 12_456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i 12_456789i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_normal_north():
    actual = \
        f"""
        _________a _________a _________a   _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a   _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a   _________b _________b _________b    1_3____8_c 1_3____8_c _________c

        _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d   _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g   _________h _________h _________h    __3____8_i __3____8_i _________i
        """

    expected = \
        f"""
        _________a _________a _________a   _________b _________b _________b    _23456789c _23456789c _23456789c
        _________a _________a _________a   _________b _________b _________b    _23456789c _23456789c _23456789c
        _23456789a _23456789a _23456789a   _23456789b _23456789b _23456789b    1_3____8_c 1_3____8_c _23456789c
        _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d   _________e _________e _________e    _________f _________f _________f
        _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g   _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g   _________h _________h _________h    __3____8_i __3____8_i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_normal_south():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    12_______e _________e 12_______e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    12_4_____h _________h 12_4_____h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    12_______e _________e 12_______e    _________f _________f _________f

        _________g _________g _________g    123_56789h 123_56789h 123_56789h    _________i _________i _________i
        _________g _________g _________g    123_56789h 123_56789h 123_56789h    _________i _________i _________i
        123_56789g 123_56789g 123_56789g    12_4_____h 123_56789h 12_4_____h    123_56789i 123_56789i 123_56789i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type2_normal_west():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 123______d    _________e _________e _________e    _________f _________f 12_______f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d 123______d    _________e _________e _________e    _________f _________f 12_______f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a 12_456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a 12_456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a 12_456789a    _________b _________b _________b    _________c _________c _________c

        12_456789d 12_456789d 123______d    _________e _________e _________e    _________f _________f 12_______f
        12_456789d 12_456789d 12_456789d    _________e _________e _________e    _________f _________f _________f
        12_456789d 12_456789d 123______d    _________e _________e _________e    _________f _________f 12_______f

        _________g _________g 12_456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g 12_456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g 12_456789g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type3_col_chute_fences_2_fins():
    actual = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 

    _________d _________d _________d    _________e _________e _________e    1____6___f 1____6___f _________f 
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 

    _________g _________g _________g    _________h _________h _________h    _________i _________i __3____8_i 
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
    _________g _________g _________g    _________h _________h _________h    1____6_8_i 1____6__9i __3____89i 
    """
    expected = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 

    _________d _________d _________d    _________e _________e _________e    1____6___f 1____6___f _________f 
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 

    _________g _________g _________g    _________h _________h _________h    12_4567__i 12_4567__i __3____8_i 
    _________g _________g _________g    _________h _________h _________h    12_4567__i 12_4567__i 12_4567__i 
    _________g _________g _________g    _________h _________h _________h    1____6_8_i 1____6__9i __3____89i 
    """
    if solve(9, actual, expected, UniqueRectangleType3()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type3_row_chute_west_cols_2_fins():
    actual = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
    _________a 1_3__67__a _________a    _________b _________b _________b    __3__6___c _________c _________c 
    _________a 1_3__67__a _________a    _________b _________b _________b    __3__6___c _________c _________c 

    _________d 1__4_____d _________d    _________e _________e _________e    _________f _________f _________f 
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 
    _________d ___4__7__d _________d    _________e _________e _________e    _________f _________f _________f 

    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 

    """
    expected = \
        f"""
    _________a _23_56_89a _________a    _________b _________b _________b    _________c _________c _________c 
    _________a 1_3__67__a _________a    _________b _________b _________b    __3__6___c _________c _________c 
    _________a 1_3__67__a _________a    _________b _________b _________b    __3__6___c _________c _________c 

    _________d 1__4_____d _________d    _________e _________e _________e    _________f _________f _________f 
    _________d _23_56_89d _________d    _________e _________e _________e    _________f _________f _________f 
    _________d ___4__7__d _________d    _________e _________e _________e    _________f _________f _________f 

    _________g _23_56_89g _________g    _________h _________h _________h    _________i _________i _________i 
    _________g _23_56_89g _________g    _________h _________h _________h    _________i _________i _________i 
    _________g _23_56_89g _________g    _________h _________h _________h    _________i _________i _________i 
    """
    if solve(9, actual, expected, UniqueRectangleType3()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_north_control():
    if solve(6,
             f"""
            ______a _23456a ______a   _23456b _23456b _23456b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e 12____e   ______f ______f ______f
            12____e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_south_control():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ____56c   ______d ______d ____56d
            ______c ______c ______c   ______d ______d ______d

            12345_e 12345_e 12345_e   ______f 12345_f ______f
            ______e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_west_control():
    actual = \
        f"""
        ______a 123_56a   ______b ______b   ______c ______c
        ______a ______a   __34__b ______b   ______c ______c
        ______a ______a   ______b ______b   ______c ______c

        ______d 123_56d   __34__e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_eat_control():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c

        ______d ______d   ______e 1____6e   ______f 123456f
        ______d ______d   ______e ______e   ______f 123456f
        ______d ______d   ______e 1____6e   ______f 123456f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_north_control():
    if solve(6,
             f"""
            123456a _23456a 123456a   123456b _23456b _23456b
            ______a ______a 12____a   12____b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_south_control():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ____56b ______b

            ______c ______c ____56c   ______d ______d ______d
            12345_c 12345_c 123456c   123456d 12345_d 12345_d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_west_control():
    actual = \
        f"""
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123456b __34__b   ______c ______c

        ______d ______d   123456e ______e   __34__f ______f
        ______d ______d   123_56e ______e   ______f ______f
        ______d _____6d   123_56e ______e   ______f ______f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_east_control():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b 1____6b   ______c 123456c

        ______d ______d   ______e 1____6e   ______f 123456f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e ______e   ______f _23456f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_north():
    if solve(6,
             f"""
            ______a _23456a ______a   _23456b _23456b _23456b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            12____e ______e 12____e   ______f ______f ______f
            """,
             f"""
            1_3456a _23456a 1_3456a   _23456b _23456b _23456b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            12____e ______e 12____e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_south():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ____56d ______d ____56d
            ______c ______c ______c   ______d ______d ______d

            12345_e 12345_e 12345_e   ______f 12345_f ______f
            ______e ______e ______e   ______f ______f ______f
            """,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ____56d ______d ____56d
            ______c ______c ______c   ______d ______d ______d

            12345_e 12345_e 12345_e   1234_6f 12345_f 1234_6f
            ______e ______e ______e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_west():
    actual = \
        f"""
        ______a 123_56a   ______b ______b   ______c ______c
        ______a ______a   __34__b ______b   ______c ______c
        ______a ______a   __34__b ______b   ______c ______c

        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        """

    expected = \
        f"""
        ______a 123_56a   ______b ______b   ______c ______c
        ______a 12_456a   __34__b ______b   ______c ______c
        ______a 12_456a   __34__b ______b   ______c ______c

        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_eat():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c

        ______d ______d   ______e 1____6e   ______f 123456f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e 1____6e   ______f 123456f
        """

    expected = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c

        ______d ______d   ______e 1____6e   ______f 12345_f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e 1____6e   ______f 12345_f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_north():
    if solve(6,
             f"""
            _23456a _23456a 123456a   123456b _23456b _23456b
            ______a ______a 12____a   12____b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """,
             f"""
            _23456a _23456a 1_3456a   1_3456b _23456b _23456b
            ______a ______a 12____a   12____b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_south():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ____56c   ____56d ______d ______d
            12345_c 12345_c 123456c   123456d 12345_d 12345_d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ____56c   ____56d ______d ______d
            12345_c 12345_c 1234_6c   1234_6d 12345_d 12345_d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_west():
    actual = \
        f"""
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123456b __34__b   ______c ______c

        ______d ______d   123456e __34__e   ______f ______f
        ______d ______d   123_56e ______e   ______f ______f
        ______d _____6d   123_56e ______e   ______f ______f
        """

    expected = \
        f"""
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   12_456b __34__b   ______c ______c

        ______d ______d   12_456e __34__e   ______f ______f
        ______d ______d   123_56e ______e   ______f ______f
        ______d _____6d   123_56e ______e   ______f ______f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


#
def test_sudoku_6x6_ur4_goofy_east():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   1____6c 123456c

        ______d ______d   ______e ______e   1____6f 123456f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e ______e   ______f _23456f
        """

    expected = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   1____6c 12345_c

        ______d ______d   ______e ______e   1____6f 12345_f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e ______e   ______f _23456f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_goofy_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b 12_______b _________b    _________c _________c _________c

        _________d _________d _________d    _________e 12_______e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i        
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b 12_______b 1_3456789b    _________c _________c _________c

        _________d _________d _________d    _________e 12_______e 1_3456789e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i        
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_goofy_north():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _23456789d _23456789d _________d    _________e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _23456789d _23456789d 1_3456789d    1_3456789e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


# _actual

#
# sudoku_explicit_unique_rectangle_type4_goofy_south_expected

#
def test_sudoku_explicit_unique_rectangle_type4_goofy_south():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _23456789d _23456789d _________d    _________e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _23456789d _23456789d 1_3456789d    1_3456789e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_goofy_west():
    actual = \
        f"""
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b 12_______b _________b    _________c _________c _________c

        _________d _________d _________d    _________e 12_______e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    1_3456789b 12_______b _________b    _________c _________c _________c

        _________d _________d _________d    1_3456789e 12_______e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_normal_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    ________9c _________c _________c
        _________a _________a _________a    _________b _________b _________b    __34_____c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _____6___c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _______8_f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ______7__f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ____5____f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _23______i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    12_4_____i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    1234_____i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    ________9c _________c _________c
        _________a _________a _________a    _________b _________b _________b    __34_____c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _____6___c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _______8_f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ______7__f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ____5____f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _23______i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    1__4_____i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    1_34_____i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_normal_south():
    actual = \
        f"""
        ___4__7__a ___4__7__a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        __34567__g __34567__g __3__6___g    ________9h _____67__h 1________h    _______8_i _2__56___i _23______i
        """

    expected = \
        f"""
        ___4__7__a ___4__7__a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        __3456___g __3456___g __3__6___g    ________9h _____67__h 1________h    _______8_i _2__56___i _23______i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_normal_west():
    actual = \
        f"""
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _________d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _23456789d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 1_3456789d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d 1_3456789d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _23456789d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


#

#

def test_sudoku_explicit_unique_rectangle_type4_normal_north():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _23456789d _23456789d _23456789d    _________e _23456789e _________e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    12_______h _________h 12_______h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _23456789d _23456789d _23456789d    1_3456789e _23456789e 1_3456789e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    12_______h _________h 12_______h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


# sudoku_explicit_naked_triple_cols_actual
# 1__4__7__a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1__4__7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1__4__7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_naked_triple_cols_expected
# 1__4__7__a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _23_56_89a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _23_56_89a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _23_56_89d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1__4__7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23_56_89d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23_56_89g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23_56_89g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1__4__7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_naked_triple_fences_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1__4__7__i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1__4__7__i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1__4__7__i
#
# sudoku_explicit_naked_triple_fences_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    _23_56_89i _23_56_89i 1__4__7__i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1__4__7__i _23_56_89i _23_56_89i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    _23_56_89i _23_56_89i 1__4__7__i
#
# sudoku_explicit_naked_triple_rows_actual
# 1__4__7__a 123456789a 123456789a    123456789b 1__4__7__b 123456789b    123456789c 123456789c 1__4__7__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_naked_triple_rows_expected
# 1__4__7__a _23_56_89a _23_56_89a    _23_56_89b 1__4__7__b _23_56_89b    _23_56_89c _23_56_89c 1__4__7__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#


def test_sudoku_explicit_hidden_pair_cols_():
    actual = \
        f"""
    1_3456_89a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    1_3456_89a _________a _________a    _________b _________b _________b    _________c _________c _________c

    1_3456_89d _________d _________d    _________e _________e _________e    _________f _________f _________f
    1_3456_89d _________d _________d    _________e _________e _________e    _________f _________f _________f
    1_3456_89d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    1_3456_89g _________g _________g    _________h _________h _________h    _________i _________i _________i
    1_3456_89g _________g _________g    _________h _________h _________h    _________i _________i _________i
    """
    expected = \
        f"""
    1_3456_89a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _2____7__a _________a _________a    _________b _________b _________b    _________c _________c _________c
    1_3456_89a _________a _________a    _________b _________b _________b    _________c _________c _________c

    1_3456_89d _________d _________d    _________e _________e _________e    _________f _________f _________f
    1_3456_89d _________d _________d    _________e _________e _________e    _________f _________f _________f
    1_3456_89d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _2____7__g _________g _________g    _________h _________h _________h    _________i _________i _________i
    1_3456_89g _________g _________g    _________h _________h _________h    _________i _________i _________i
    1_3456_89g _________g _________g    _________h _________h _________h    _________i _________i _________i
    """
    if solve(9, actual, expected, tech.HiddenPair()):
        return
    assert False


def test_sudoku_explicit_hidden_pair_fences():
    actual = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    1_3456_89i _________i 1_3456_89i
    _________g _________g _________g    _________h _________h _________h    1_3456_89i 1_3456_89i 1_3456_89i
    _________g _________g _________g    _________h _________h _________h    1_3456_89i 1_3456_89i _________i
    """
    expected = \
        f"""
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    1_3456_89i _2____7__i 1_3456_89i
    _________g _________g _________g    _________h _________h _________h    1_3456_89i 1_3456_89i 1_3456_89i
    _________g _________g _________g    _________h _________h _________h    1_3456_89i 1_3456_89i _2____7__i
    """
    if solve(9, actual, expected, tech.HiddenPair()):
        return
    assert False


def test_sudoku_explicit_hidden_pair_rows():
    temp = ""
    match temp:
        case "":
            print('jello')
    actual = \
        f"""
    1_3456_89a _________a 1_3456_89a    1_3456_89b 1_3456_89b _________b    1_3456_89c 1_3456_89c 1_3456_89c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    """
    expected = \
        f"""
    1_3456_89a _2____7__a 1_3456_89a    1_3456_89b 1_3456_89b _2____7__b    1_3456_89c 1_3456_89c 1_3456_89c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
    _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
    _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
    """
    if solve(9, actual, expected, tech.HiddenPair()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_x_wing_col():
    actual = \
        f"""
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f

        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        12345678_a _________a 12345678_a    _________b 12345678_b 12345678_b    12345678_c 12345678_c 12345678_c

        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f
        12345678_d _________d 12345678_d    _________e 12345678_e 12345678_e    12345678_f 12345678_f 12345678_f
        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f

        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, tech.XWing()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_x_wing_row():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        ____56___d _______8_d ___4_____d    1___5____e ______7__e ________9e    1____6___f __3______f _2_______f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _2__5____g ___4_____g _______8_g    ____56___h ________9h 1________h    _2___6___i ______7__i __3______i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        1234_6789a _________a _________a    1234_6789b _________b _________b    _________c _________c _________c
        1234_6789a _________a _________a    1234_6789b _________b _________b    _________c _________c _________c
        1234_6789a _________a _________a    1234_6789b _________b _________b    _________c _________c _________c

        1234_6789d _________d _________d    1234_6789e _________e _________e    _________f _________f _________f
        1234_6789d _________d _________d    1234_6789e _________e _________e    _________f _________f _________f
        ____56___d _______8_d ___4_____d    1___5____e ______7__e ________9e    1____6___f __3______f _2_______f

        1234_6789g _________g _________g    1234_6789h _________h _________h    _________i _________i _________i
        _2__5____g ___4_____g _______8_g    ____56___h ________9h 1________h    _2___6___i ______7__i __3______i
        1234_6789g _________g _________g    1234_6789h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, tech.XWing()):
        return
    assert False


# @pytest.mark.skip("EXPLICITLY")
# def test_finned_x_wing_east():
#     actual = \
#         f"""
#         _234a ____a   234_b ____b
#         ____a ____a   ____b ____b
#
#         _234c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         _234a ____a   234_b ____b
#         ____a ____a   ____b ____b
#
#         _234c ____c   ____d ____d
#         ____c ____c   ____d _234d
#         """
#     if solve(4, actual, expected, FinnedXWing()):
#         return
#     assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_ne_rows():
    actual = \
        f"""
        123_a ____a   123_b 123_b
        ____a ____a   ____b ____b

        123_c ____c   123_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_nw_rows():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_se_rows():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_sw_rows():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_ne_cols():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_nw_cols():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_se_cols():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_finned_x_wing_sw_cols():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_finned_x_wing_1_fin_cols():
    actual = \
        f"""
        _________a _________a __3______a    _________b _______8_b _________b    _________c _________c _________c
        _________a _________a _____6___a    _________b 1________b _________b    _________c _________c _________c
        _________a _________a ____5___9a    _________b ______7_9b _________b    _________c _________c _________c

        _________d _________d 1________d    _________e ____5____e _________e    _________f _________f _________f
        _________d _________d ___4_____d    _________e __3__67__e _________e    _________f _________f _________f
        _________d _________d ______7__d    _________e _2_______e _________e    _________f _________f _________f

        _________g _________g _______8_g    _2_______h __3__67__h ____5____h    _________i _________i _________i
        _________g _________g ____5___9g    __3___7_9h __34_67_9h __3__678_h    _________i _________i _________i
        _________g _________g _2_______g    1________h __34____9h __3____8_h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a __3______a    _________b _______8_b _________b    _________c _________c _________c
        _________a _________a _____6___a    _________b 1________b _________b    _________c _________c _________c
        _________a _________a ____5___9a    _________b ______7_9b _________b    _________c _________c _________c

        _________d _________d 1________d    _________e ____5____e _________e    _________f _________f _________f
        _________d _________d ___4_____d    _________e __3__67__e _________e    _________f _________f _________f
        _________d _________d ______7__d    _________e _2_______e _________e    _________f _________f _________f

        _________g _________g _______8_g    _2_______h __3__67__h ____5____h    _________i _________i _________i
        _________g _________g ____5___9g    __3___7__h __34_67_9h __3__678_h    _________i _________i _________i
        _________g _________g _2_______g    1________h __34____9h __3____8_h    _________i _________i _________i
        """
    if solve(9, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_finned_x_wing_1_fin_rows():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    12____7__e _________e _________e    _________f _________f _________f
        ___4_____d 1_______9d 1_______9d    _23__6___e _______8_e _23__6___e    _23_5____f _2__5____f ______7__f
        _________d _________d _________d    __3___7__e _________e _________e    _________f _________f _________f

        _2_______g 1______8_g _____6___g    1_3______h ______7__h ___4_____h    __3_5__8_i 1___5__8_i ________9i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    12____7__e _________e _________e    _________f _________f _________f
        ___4_____d 1_______9d 1_______9d    _23__6___e _______8_e _23__6___e    _23_5____f _2__5____f ______7__f
        _________d _________d _________d    ______7__e _________e _________e    _________f _________f _________f

        _2_______g 1______8_g _____6___g    1_3______h ______7__h ___4_____h    __3_5__8_i 1___5__8_i ________9i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_finned_x_wing_2_fin_cols():
    actual = \
        f"""
        _________a _23456789a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _23456789a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _23456789d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _23456789d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _23456789d _________d    _23456789e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _23456789g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _23456789g _________g    _23456789h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _23456789a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _23456789a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _23456789b _23456789b    _________c _________c _________c

        _________d _23456789d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _23456789d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _23456789d _________d    _23456789e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _23456789g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _23456789g _________g    _23456789h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, FinnedXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_finned_x_wing_2_fin_rows():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _23456789b _23456789b _23456789b    _________c _23456789c _23456789c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _23456789g _23456789g _________g    _23456789h _23456789h _23456789h    _________i _23456789i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _23456789b _23456789b _23456789b    _________c _23456789c _23456789c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _23456789g _23456789g _________g    _23456789h _23456789h _23456789h    _________i _23456789i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, FinnedXWing()):
        return
    assert False


def test_sudoku_explicit_shashimi_x_wing_1_fin_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _23456789a _23456789a _________a    _23456789b _23456789b _23456789b    _23456789c _________c _23456789c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _23456789g _23456789g _________g    _23456789h _23456789h _23456789h    _________i _23456789i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _23456789a _23456789a _________a    _23456789b _23456789b _23456789b    _23456789c _________c _23456789c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _23456789g _23456789g _________g    _23456789h _23456789h _23456789h    _________i _23456789i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _23456789i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _23456789i _________i
        """
    if solve(9, actual, expected, SashimiXWing()):
        return
    assert False


def test_sudoku_explicit_shashimi_x_wing_1_fin_west():
    actual = \
        f"""
        _________c _________c _________c   _________a _________a _________a    _________b _________b _________b
        _________c _________c _________c   _________a _________a _________a    _________b _________b _________b
        _23456789c _________c _23456789c   _23456789a _23456789a _________a    _23456789b _23456789b _23456789b

        _________f _________f _________f   _________d _________d _________d    _________e _________e _________e
        _________f _________f _________f   _________d _________d _________d    _________e _________e _________e
        _________f _________f _________f   _________d _________d _________d    _________e _________e _________e

        _________i _23456789i _23456789i   _23456789g _23456789g _________g    _23456789h _23456789h _23456789h
        _________i _________i _________i   _________g _________g _________g    _________h _________h _________h
        _________i _________i _________i   _________g _________g _________g    _________h _________h _________h
        """

    expected = \
        f"""
        _________c _________c _________c   _________a _________a _________a    _________b _________b _________b
        _________c _________c _________c   _________a _________a _________a    _________b _________b _________b
        _23456789c _________c _23456789c   _23456789a _23456789a _________a    _23456789b _23456789b _23456789b

        _________f _________f _________f   _________d _________d _________d    _________e _________e _________e
        _________f _________f _________f   _________d _________d _________d    _________e _________e _________e
        _________f _________f _________f   _________d _________d _________d    _________e _________e _________e

        _________i _23456789i _23456789i   _23456789g _23456789g _________g    _23456789h _23456789h _23456789h
        _________i _________i _________i   _________g _________g _________g    _________h _________h _________h
        _________i _________i _________i   _________g _________g _________g    _________h _________h _________h
        """
    if solve(9, actual, expected, SashimiXWing()):
        return
    assert False


def test_sudoku_explicit_shashimi_x_wing_2_fin_rows():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _23456789a _23456789a _________a    _23456789b _23456789b _23456789b    _23456789c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _23456789g _23456789g _________g    _23456789h _23456789h _23456789h    _________i _23456789i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _23456789a _23456789a _________a    _23456789b _23456789b _23456789b    _23456789c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _23456789g _23456789g _________g    _23456789h _23456789h _23456789h    _________i _23456789i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, SashimiXWing()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_sword_fish_cols():
    actual = \
        f"""
        123456789a 123456789a 123456789a    123456789b 123456789b ________9b    __3_5____c ___45____c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b __34_____b    __3____8_c ___4___8_c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b _____6___b    ______7_9c 1_______9c 123456789c

        123456789d 123456789d 123456789d    123456789e 123456789e _______8_e    1________f _____6___f 123456789f
        123456789d 123456789d 123456789d    123456789e 123456789e __3_5____e    ____5_7__f _2_______f 123456789f
        123456789d 123456789d 123456789d    123456789e 123456789e ______7__e    _______89f _______89f 123456789f

        123456789g 123456789g 123456789g    123456789h 123456789h 1________h    _____6___i ______7__i 123456789i
        123456789g 123456789g 123456789g    123456789h 123456789h __345____h    _2_______i 1___5____i 123456789i
        123456789g 123456789g 123456789g    123456789h 123456789h _2_______h    ___4_____i __3______i 123456789i
        """

    expected = \
        f"""
        1234_6789a 1234_6789a 1234_6789a    1234_6789b 1234_6789b ________9b    __3_5____c ___45____c 1234_6789c
        123456789a 123456789a 123456789a    123456789b 123456789b __34_____b    __3____8_c ___4___8_c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b _____6___b    ______7_9c 1_______9c 123456789c

        123456789d 123456789d 123456789d    123456789e 123456789e _______8_e    1________f _____6___f 123456789f
        1234_6789d 1234_6789d 1234_6789d    1234_6789e 1234_6789e __3_5____e    ____5_7__f _2_______f 1234_6789f
        123456789d 123456789d 123456789d    123456789e 123456789e ______7__e    _______89f _______89f 123456789f

        123456789g 123456789g 123456789g    123456789h 123456789h 1________h    _____6___i ______7__i 123456789i
        1234_6789g 1234_6789g 1234_6789g    1234_6789h 1234_6789h __345____h    _2_______i 1___5____i 1234_6789i
        123456789g 123456789g 123456789g    123456789h 123456789h _2_______h    ___4_____i __3______i 123456789i
        """
    if solve(9, actual, expected, tech.SwordFish()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_sword_fish_rows():
    actual = \
        f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        _23456789a _23456789a 123456789a    _23456789b 123456789b _23456789b    123456789c _23456789c _23456789c

        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
        _23456789d _23456789d 123456789d    _23456789e 123456789e _23456789e    123456789f _23456789f _23456789f
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        _23456789g _23456789g 123456789g    _23456789h 123456789h _23456789h    123456789i _23456789i _23456789i
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        """

    expected = \
        f"""
        123456789a 123456789a _23456789a    123456789b _23456789b 123456789b    _23456789c 123456789c 123456789c
        123456789a 123456789a _23456789a    123456789b _23456789b 123456789b    _23456789c 123456789c 123456789c
        _23456789a _23456789a 123456789a    _23456789b 123456789b _23456789b    123456789c _23456789c _23456789c

        123456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f 123456789f
        _23456789d _23456789d 123456789d    _23456789e 123456789e _23456789e    123456789f _23456789f _23456789f
        123456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f 123456789f

        123456789g 123456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i 123456789i
        _23456789g _23456789g 123456789g    _23456789h 123456789h _23456789h    123456789i _23456789i _23456789i
        123456789g 123456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i 123456789i
        """
    if solve(9, actual, expected, tech.SwordFish()):
        return
    assert False


def test_sudoku_explicit_hidden_triple_cols():
    actual = \
        f"""
    ____5____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    ___4_____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    1_3__6_89a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    12___6__9d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    _____6789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    1_3___789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    _2______9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    _2___6__9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    12___6__9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """

    expected = \
        f"""
    ____5____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    ___4_____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    __3____8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    12___6__9d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    ______78_d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    __3___78_d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    _2______9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    _2___6__9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    12___6__9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """
    if solve(9, actual, expected, tech.HiddenTriple()):
        return
    assert False


def test_sudoku_explicit_hidden_triple_fences():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    _2___67__c _2___678_c _2___6___c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    1_345_7__c ___4__7__c 1_345____c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __3_567__c _____678_c ________9c 

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """

    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    _2___67__c _2___678_c _2___6___c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    1_3_5____c ___4__7__c 1_3_5____c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __3_5____c _____678_c ________9c 

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    """
    if solve(9, actual, expected, tech.HiddenTriple()):
        return
    assert False


def test_sudoku_explicit_hidden_triple_rows():
    actual = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    ___456789g ___456789g 123456789g    ___456789h 123456789h ___456789h    123456789i ___456789i ___456789i 

    """

    expected = \
        f"""
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
    123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
    123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 

    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
    ___456789g ___456789g 123______g    ___456789h 123______h ___456789h    123______i ___456789i ___456789i 
    """
    if solve(9, actual, expected, tech.HiddenTriple()):
        return
    assert False


@pytest.mark.skip("EXPLICITLY")
def test_():
    actual = \
        f"""

        """

    expected = \
        f"""

        """
    if solve(9, actual, expected, FinnedXWing()):
        return
    assert False


# sudoku_explicit_finned_sword_fish_cols_actual
# 1234567_9a 123456789a 123456789a    123456789b _______89b 123456789b    123456789c 123456789c 1234567_9c
# 1234567_9a 123456789a 123456789a    123456789b __3____89b 123456789b    123456789c 123456789c ____5_78_c
# 1234567_9a 123456789a 123456789a    123456789b 1234567_9b 123456789b    123456789c 123456789c 1234567_9c
#
# 1234567_9d 123456789d 123456789d    123456789e 1234567_9e 123456789e    123456789f 123456789f 1234567_9f
# 1234567_9d 123456789d 123456789d    123456789e 1234567_9e 123456789e    123456789f 123456789f 1234567_9f
# 1234567_9d 123456789d 123456789d    123456789e 1234567_9e 123456789e    123456789f 123456789f 1234567_9f
#
# 1_____78_g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1234567_9i
# _2_4__78_g 123456789g 123456789g    123456789h 1234567_9h 123456789h    123456789i 123456789i ______78_i
# 1234567_9g 123456789g 123456789g    123456789h 1234567_9h 123456789h    123456789i 123456789i 1234567_9i
#
#
# sudoku_explicit_finned_sword_fish_cols_expected
# 1234567_9a 123456789a 123456789a    123456789b _______89b 123456789b    123456789c 123456789c 1234567_9c
# 1234567_9a 123456789a 123456789a    1234567_9b __3____89b 1234567_9b    123456789c 123456789c ____5_78_c
# 1234567_9a 123456789a 123456789a    123456789b 1234567_9b 123456789b    123456789c 123456789c 1234567_9c
#
# 1234567_9d 123456789d 123456789d    123456789e 1234567_9e 123456789e    123456789f 123456789f 1234567_9f
# 1234567_9d 123456789d 123456789d    123456789e 1234567_9e 123456789e    123456789f 123456789f 1234567_9f
# 1234567_9d 123456789d 123456789d    123456789e 1234567_9e 123456789e    123456789f 123456789f 1234567_9f
#
# 1_____78_g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1234567_9i
# _2_4__78_g 123456789g 123456789g    123456789h 1234567_9h 123456789h    123456789i 123456789i ______78_i
# 1234567_9g 123456789g 123456789g    123456789h 1234567_9h 123456789h    123456789i 123456789i 1234567_9i
#
@pytest.mark.skip("EXPLICITLY")
def test_():
    actual = \
        f"""

        """

    expected = \
        f"""

        """
    if solve(9, actual, expected, FinnedXWing()):
        return
    assert False


# sudoku_explicit_finned_sword_fish_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    _23456789b 123456789b _23456789b    123456789c _23456789c _23456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23456789d _23456789d 123456789d    _23456789e 123456789e _23456789e    123456789f _23456789f _23456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23456789g _23456789g 123456789g    _23456789h 123456789h _23456789h    123456789i _23456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_finned_sword_fish_rows_expected
# 123456789a 123456789a _23456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a _23456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    _23456789b 123456789b _23456789b    123456789c _23456789c _23456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23456789d _23456789d 123456789d    _23456789e 123456789e _23456789e    123456789f _23456789f _23456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23456789g _23456789g 123456789g    _23456789h 123456789h _23456789h    123456789i _23456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#


@pytest.mark.skip("SKIPPED")
def test_sudoku_explicit_shashimi_sword_fish_1_fin_cols():
    actual = \
        f"""
        _______8_a _________a _________a    _2_______b _________b _________b    ______7__c _________c _________c
        1________a _________a _________a    __3__67__b _________b _________b    ____5____c _________c _________c
        ____5____a _________a _________a    __3__678_b _________b _________b    1________c _________c _________c

        __3______d _________d _________d    _____67__e _________e _________e    _2_______f _________f _________f
        ______7__d _________d _________d    1_3______e _________e _________e    _______89f _________f _________f
        _____6__9d _________d _________d    ____5____e _________e _________e    __3______f _________f _________f

        ___4_____g _________g _________g    1____6_89h _________h _________h    _______89i _________i _________i
        _2_______g _________g _________g    ___4_____h _________h _________h    _____6___i _________i _________i
        _____6__9g _________g _________g    1_____789h _________h _________h    ___4_____i _________i _________i
        """

    expected = \
        f"""
        _______8_a _________a _________a    _2_______b _________b _________b    ______7__c _________c _________c
        1________a _________a _________a    __3__67__b _________b _________b    ____5____c _________c _________c
        ____5____a _________a _________a    __3__678_b _________b _________b    1________c _________c _________c

        __3______d _________d _________d    _____67__e _________e _________e    _2_______f _________f _________f
        ______7__d 12345678_d 12345678_d    1_3______e _________e _________e    _______89f _________f _________f
        _____6__9d _________d _________d    ____5____e _________e _________e    __3______f _________f _________f

        ___4_____g _________g _________g    1____6_89h _________h _________h    _______89i _________i _________i
        _2_______g _________g _________g    ___4_____h _________h _________h    _____6___i _________i _________i
        _____6__9g _________g _________g    1_____789h _________h _________h    ___4_____i _________i _________i
        """
    if solve(9, actual, expected, tech.ShashimiSwordFish()):
        return
    assert False


@pytest.mark.skip("SKIPPED")
def test_sudoku_explicit_shashimi_sword_fish_1_fin_rows():
    actual = \
        f"""
        _________a 123456_89a 123456_89a    123456_89b _________b 123456_89b    _________c 123456_89c 123456_89c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        123456_89a 123456_89a 123456_89a    123456_89b _________b 123456_89b    _________c 123456_89c 123456_89c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        123456_89g 123456_89g _________g    123456_89h 123456_89h 123456_89h    _________i 123456_89i 123456_89i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a 123456_89a 123456_89a    123456_89b _________b 123456_89b    _________c 123456_89c 123456_89c
        _________a _________a 123456_89a    _________b _________b _________b    _________c _________c _________c
        123456_89a 123456_89a 123456_89a    123456_89b _________b 123456_89b    _________c 123456_89c 123456_89c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        123456_89g _________g _________g    _________h _________h _________h    _________i _________i _________i
        123456_89g 123456_89g _________g    123456_89h 123456_89h 123456_89h    _________i 123456_89i 123456_89i
        123456_89g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, tech.ShashimiSwordFish()):
        return
    assert False


@pytest.mark.skip("SKIPPED")
def test_sudoku_explicit_shashimi_sword_fish_2_fin_cols():
    actual = \
        f"""
        _________a 1________a _________a    _________b _________b _________b    _________c _______8_c _________c
        _________a _____6__9a _________a    _________b 1234_6789b _________b    _________c _________c _________c
        _________a ______78_a _________a    _________b 1234_6789b _________b    _________c _________c _________c

        _________d ___4__789d _________d    _________e 1234_6789e _________e    _________f 1________f _________f
        _________d __3______d _________d    _________e 1234_6789e _________e    _________f 1234_6789f _________f
        _________d ___4__789d _________d    _________e 1234_6789e _________e    _________f 1234_6789f _________f

        _________g ___456_8_g _________g    _________h ____56_8_h _________h    _________i ___45___9i _________i
        _________g _2_______g _________g    _________h ___4_____h _________h    _________i 1234_6789i _________i
        _________g ___456_8_g _________g    _________h ____56___h _________h    _________i ___45_7__i _________i
        """

    expected = \
        f"""
        _________a 1________a _________a    _________b _________b _________b    1234_6789c _______8_c 1234_6789c
        _________a _____6__9a _________a    _________b 1234_6789b _________b    _________c _________c _________c
        _________a ______78_a _________a    _________b 1234_6789b _________b    _________c _________c _________c

        _________d ___4__789d _________d    _________e 1234_6789e _________e    _________f 1________f _________f
        _________d __3______d _________d    _________e 1234_6789e _________e    _________f 1234_6789f _________f
        _________d ___4__789d _________d    _________e 1234_6789e _________e    _________f 1234_6789f _________f

        _________g ___456_8_g _________g    _________h ____56_8_h _________h    _________i ___45___9i _________i
        _________g _2_______g _________g    _________h ___4_____h _________h    _________i 1234_6789i _________i
        _________g ___456_8_g _________g    _________h ____56___h _________h    _________i ___45_7__i _________i
        """
    if solve(9, actual, expected, tech.ShashimiSwordFish()):
        return
    assert False


@pytest.mark.skip('skipped')
def test_sudoku_explicit_w_wing_rows0():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 12_______d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    12_______f _________f _________f
        _________d _________d _________d    _23456789e _23456789e _23456789e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d 12_______d    _________e _________e _________e    1_3456789f 1_3456789f 1_3456789f
        1_3456789d 1_3456789d 1_3456789d    _________e _________e _________e    12_______f _________f _________f
        _________d _________d _________d    _23456789e _23456789e _23456789e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, WWing()):
        return
    assert False


@pytest.mark.skip('skipped')
def test_sudoku_explicit_w_wing_rows1():
    actual = \
        f"""
        _______8_g 1________g _23______g    _________h _________h _________h    _________i _________i __3__6___i
        ________9g __34_____g _234_____g    _________h _________h __3___6__h    _________i _________i _________i
        ____5____g _____6___g ______7__g    _________h _________h _________h    _________i _________i _________i

        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f


        """

    expected = \
        f"""
        _______8_g 1________g _23______g    12345_789h 12345_789h 12345_789h    _________i _________i __3__6___i
        ________9g __34_____g _234_____g    _________h _________h __3___6__h    12345_789i 12345_789i 12345_789i
        ____5____g _____6___g ______7__g    _________h _________h _________h    _________i _________i _________i

        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, WWing()):
        return
    assert False


#
# def test_sudoku_explicit_w_wing_cols0():
#     actual = \
#         f"""
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         """
#
#     expected = \
#         f"""
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         """
#     if solve(9, actual, expected, WWing()):
#         return
#     assert False
#
# def test_sudoku_explicit_w_wing_cols1():
#     actual = \
#         f"""
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         """
#
#     expected = \
#         f"""
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#         _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#         _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#         """
#     if solve(9, actual, expected, WWing()):
#         return
#     assert False


@pytest.mark.skip("SKIPPED")
def test_sudoku_explicit_jelly_fish_cols():
    actual = \
        f"""
        _________a __34_____a _________a    _________b _________b _______8_b    _____6___c _________c __34_____c
        _________a 1_3_5____a _________a    _________b _________b _____6___b    1_3______c _________c _______8_c
        _________a 1__4_____a _________a    _________b _________b __3______b    1__4_____c _________c ________9c

        _________d _______8_d _________d    _________e _________e ___45____e    _2_______f _________f __34_____f
        _________d _____6___d _________d    _________e _________e _2_______e    ________9f _________f ______7__f
        _________d _2_______d _________d    _________e _________e ______7__e    ____5____f _________f _____6___f

        _________g ______7_9g _________g    _________h _________h ___45____h    __34_____i _________i 1________i
        _________g 1_____7__g _________g    _________h _________h ________9h    _______8_i _________i ____5____i
        _________g ____5___9g _________g    _________h _________h 1________h    ______7__i _________i _2_______i
        """

    expected = \
        f"""
        123_56789a __34_____a 123_56789a    123_56789b 123_56789b _______8_b    _____6___c 123_56789c __34_____c
        _________a 1_3_5____a _________a    _________b _________b _____6___b    1_3______c _________c _______8_c
        123_56789a 1__4_____a 123_56789a    123_56789b 123_56789b __3______b    1__4_____c 123_56789c ________9c

        123_56789d _______8_d 123_56789d    123_56789e 123_56789e ___45____e    _2_______f 123_56789f __34_____f
        _________d _____6___d _________d    _________e _________e _2_______e    ________9f _________f ______7__f
        _________d _2_______d _________d    _________e _________e ______7__e    ____5____f _________f _____6___f

        123_56789g ______7_9g 123_56789g    123_56789h 123_56789h ___45____h    __34_____i 123_56789i 1________i
        _________g 1_____7__g _________g    _________h _________h ________9h    _______8_i _________i ____5____i
        _________g ____5___9g _________g    _________h _________h 1________h    ______7__i _________i _2_______i
        """
    if solve(9, actual, expected, tech.JellyFish()):
        return
    assert False


@pytest.mark.skip("SKIPPED")
def test_sudoku_explicit_jelly_fish_rows():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _23456789a _________a _23456789a    _________b _23456789b _________b    _23456789c _________c _23456789c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c

        _23456789d _________d _23456789d    _________e _23456789e _________e    _23456789f _________f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _23456789d _________d _23456789d    _________e _23456789e _________e    _23456789f _________f _23456789f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _23456789g _________g _23456789g    _________h _23456789h _________h    _23456789i _________i _23456789i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _23456789a _________a    _23456789b _________b _23456789b    _________c _23456789c _________c
        _23456789a _________a _23456789a    _________b _23456789b _________b    _23456789c _________c _23456789c
        _________a _23456789a _________a    _23456789b _________b _23456789b    _________c _23456789c _________c

        _23456789d _________d _23456789d    _________e _23456789e _________e    _23456789f _________f _23456789f
        _________d _23456789d _________d    _23456789e _________e _23456789e    _________f _23456789f _________f
        _23456789d _________d _23456789d    _________e _23456789e _________e    _23456789f _________f _23456789f

        _________g _23456789g _________g    _23456789h _________h _23456789h    _________i _23456789i _________i
        _23456789g _________g _23456789g    _________h _23456789h _________h    _23456789i _________i _23456789i
        _________g _23456789g _________g    _23456789h _________h _23456789h    _________i _23456789i _________i
        """
    if solve(9, actual, expected, tech.JellyFish()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_almost_locked_candidates_pointing_row():
    actual = \
        f"""
        ____a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, tech.AlmostLockedCandidatesPointing()):
        return
    assert False


# sudoku_explicit_almost_locked_candidates_pointing_rows_actual
#
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# ____5____d _______8_d ______7_9d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _2_4____9d _2___6___d 1________d    _______8_e ___4_6__9e __3______e    ____5____f ______7__f _2_4_____f
# _2_4_____d __3______d _____67__d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_almost_locked_candidates_pointing_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# ____5____d _______8_d ______7_9d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _2_4____9d _2___6___d 1________d    _______8_e _____6__9e __3______e    ____5____f ______7__f _2_4_____f
# _2_4_____d __3______d _____67__d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

@mark.skip("EXPLICITLY")
def test_almost_locked_candidates_claiming_row():
    actual = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, AlmostLockedCandidatesClaiming()):
        return
    assert False


# sudoku_explicit_almost_locked_candidates_claiming_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# __3456789d __3456789d __3456789d    __3456789e __3456789e 12_______e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    12_______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_almost_locked_candidates_claiming_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# __3456789d __3456789d __3456789d    __3456789e __3456789e 12_______e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    12_______f __3456789f __3456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    __3456789f __3456789f __3456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


def test_sudoku_4x4_hur_row_ne():
    if solve(4,
             f"""
            _234c 1234c   1234d _234d
            ____c 12__c   1234d ____d

            ____a ____a   _234b ____b
            ____a ____a   _234b ____b
            """,
             f"""
            _234c 1234c   1_34d _234d
            ____c 12__c   1234d ____d

            ____a ____a   _234b ____b
            ____a ____a   _234b ____b
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_ne_control():
    if solve(4,
             f"""
            _234c 1234c   1234d _234d
            ____c ____c   1234d ____d

            ____a ____a   _234b ____b
            12__a ____a   _234b ____b
            """,
             None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_nw():
    if solve(4,
             f"""
            1234d _234d  _234c 1234c
            1234d ____d  ____c 12__c   

            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a
            """,
             f"""
            1_34d _234d  _234c 1234c
            1234d ____d  ____c 12__c   

            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a  
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_nw_control():
    if solve(4,
             f"""
            1234d _234d  _234c 1234c
            _234d ____d  ____c 12__c   

            1234b ____b  ____a 12__a   
            _234b ____b  ____a ____a
            """, None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_se():
    if solve(4,
             f"""
            ____a ____a   _234b ____b
            ____a ____a   _234b ____b

            ____c 12__c   1234d ____d
            _234c 1234c   1234d _234d
            """,
             f"""
            ____a ____a   _234b ____b
            ____a ____a   _234b ____b

            ____c 12__c   1234d ____d
            _234c 1234c   1_34d _234d
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_se_control():
    if solve(4,
             f"""
            ____a ____a   1234b ____b
            ____a ____a   _234b ____b

            ____c 12__c   1234d ____d
            _234c 1234c   1234d _234d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_sw():
    if solve(4,
             f"""
            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a   

            1234d ____d  ____c 12__c   
            1234d _234d  _234c 1234c   
            """,
             f"""
            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a   

            1234d ____d  ____c 12__c   
            1_34d _234d  _234c 1234c
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_sw_control():
    if solve(4,
             f"""
            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a   

            1234d 12__d  ____c ____c   
            1234d _234d  _234c 1234c
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_ne_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_nw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_nw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_se():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_se_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_sw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_sw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_explicit_hidden_unique_rectangle_north_east_col_chute():
    actual = \
        f"""
        _________a _________a _________a    ____5____b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _____6___b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _2______9b _________b _________b    _________c _________c _________c

        _________d _________d _________d    ___4_____e _________e _________e    _________f _________f _________f
        _________d _________d _________d    1_3____8_e _________e _________e    _________f _________f _________f
        _________d _________d _________d    __3___78_e __3___7__e _________e    _________f _________f _________f

        _________g _________g _________g    _2______9h _________h _________h    _________i _________i _________i
        _________g _________g _________g    1_3______h _________h _________h    _________i _________i _________i
        1_3______g _2_______g ________9g    1_3___7__h 1_3___7__h ___4_____h    _____6___i ____5____i _______8_i
        """

    expected = \
        f"""
        _________a _________a _________a    ____5____b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _____6___b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _2______9b _________b _________b    _________c _________c _________c

        _________d _________d _________d    ___4_____e _________e _________e    _________f _________f _________f
        _________d _________d _________d    1_3____8_e _________e _________e    _________f _________f _________f
        _________d _________d _________d    __3___78_e __3___7__e _________e    _________f _________f _________f

        _________g _________g _________g    _2______9h _________h _________h    _________i _________i _________i
        _________g _________g _________g    1_3______h _________h _________h    _________i _________i _________i
        1_3______g _2_______g ________9g    1_____7__h 1_3___7__h ___4_____h    _____6___i ____5____i _______8_i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_hidden_unique_rectangle_north_east_row_chute():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _2___6___b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _______8_b    _________c _________c _________c
        _________a _________a _________a    _________b _________b ____5____b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _2_4_6___e    ___4_6___f _________f _________f
        _2_______d 1________d _______8_d    ______7__e __3______e ___4_6___e    ___456___f ____56___f ________9f
        _________d _________d _________d    _________e _________e 1________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h __3______h    _________i _________i _________i
        _________g _________g _________g    _________h _________h ________9h    _________i _________i _________i
        _________g _________g _________g    _________h _________h ______7__h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _2___6___b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _______8_b    _________c _________c _________c
        _________a _________a _________a    _________b _________b ____5____b    _________c _________c _________c

        _________d _________d _________d    _________e _________e _2_4_6___e    ___4_6___f _________f _________f
        _2_______d 1________d _______8_d    ______7__e __3______e ___4_____e    ___456___f ____56___f ________9f
        _________d _________d _________d    _________e _________e 1________e    _________f _________f _________f

        _________g _________g _________g    _________h _________h __3______h    _________i _________i _________i
        _________g _________g _________g    _________h _________h ________9h    _________i _________i _________i
        _________g _________g _________g    _________h _________h ______7__h    _________i _________i _________i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_hidden_unique_rectangle_north_west_col_chute():
    actual = \
        f"""
        _________a _________a _________a    _________b __3______b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _2_____8_b _________b    _________c _________c _________c
        _________a _________a _________a    _________b ___4_____b _________b    _________c _________c _________c

        _________d _________d _________d    _________e ____5____e _________e    _________f _________f _________f
        _________d _________d _________d    _____6_8_e _2___6_8_e _________e    _________f _________f _________f
        _________d _________d _________d    _________e ______7__e _________e    _________f _________f _________f

        __3______g _2_______g ____5____g    _____678_h _____6_8_h ______78_h    ________9i 1________i ___4_____i
        _________g _________g _________g    _________h ________9h _________h    _________i _________i _________i
        _________g _________g _________g    _________h 1________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b __3______b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _2_____8_b _________b    _________c _________c _________c
        _________a _________a _________a    _________b ___4_____b _________b    _________c _________c _________c

        _________d _________d _________d    _________e ____5____e _________e    _________f _________f _________f
        _________d _________d _________d    _____6_8_e _2___6_8_e _________e    _________f _________f _________f
        _________d _________d _________d    _________e ______7__e _________e    _________f _________f _________f


        __3______g _2_______g ____5____g    _____678_h _____6___h ______78_h    ________9i 1________i ___4_____i
        _________g _________g _________g    _________h ________9h _________h    _________i _________i _________i
        _________g _________g _________g    _________h 1________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_hidden_unique_rectangle_north_west_row_chute():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c

        _________d _________d 12_______d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _23456789f _________f _________f
        _23456789d _23456789d _________d    _23456789e _23456789e _23456789e    _________f _23456789f _23456789f

        _________g _________g _________g    _________h _________h _________h    _23456789i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _23456789i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _23456789i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _23456789c _________c _________c

        _________d _________d 12_______d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _23456789f _________f _________f
        _23456789d _23456789d _________d    _23456789e _23456789e _23456789e    1_3456789f _23456789f _23456789f

        _________g _________g _________g    _________h _________h _________h    _23456789i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _23456789i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _23456789i _________i _________i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_hidden_unique_rectangle_south_east_row_chute():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _______8_c _________c _________c
        _________a _________a _________a    _________b _________b _________b    __3______c _________c _________c
        _________a _________a _________a    _________b _________b _________b    ____5____c _________c _________c

        ____5____d _______8_d 1_3___7__d    1_______9e _2_______e _____6___e    1_____7_9f ___4_____f __3_____9f
        _________d _________d _________d    _________e _________e _________e    _2_______f _________f _________f
        _________d _________d 1_____7__d    _________e _________e _________e    1_____7_9f _________f _________f

        _________g _________g _________g    _________h _________h _________h    ___4_____i _________i _________i
        _________g _________g _________g    _________h _________h _________h    1_______9i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _____6___i _________i _________i
        """

    expected = \
        f"""
        # _________a _________a _________a    _________b _________b _________b    _______8_c _________c _________c
        # _________a _________a _________a    _________b _________b _________b    __3______c _________c _________c
        # _________a _________a _________a    _________b _________b _________b    ____5____c _________c _________c
        #
        # ____5____d _______8_d 1_3___7__d    1_______9e _2_______e _____6___e    ______7_9f ___4_____f __3_____9f
        # _________d _________d _________d    _________e _________e _________e    _2_______f _________f _________f
        # _________d _________d 1_____7__d    _________e _________e _________e    1_____7_9f _________f _________f
        #
        # _________g _________g _________g    _________h _________h _________h    ___4_____i _________i _________i
        # _________g _________g _________g    _________h _________h _________h    1_______9i _________i _________i
        # _________g _________g _________g    _________h _________h _________h    _____6___i _________i _________i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_hidden_unique_rectangle_south_west_col_chute():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c 1________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c __3______c
        __34_____a 1________a _____6___a    ________9b ______7__b __3__5___b    _______8_c _2_45____c _2__5____c

        _________d _________d _________d    _________e _________e _________e    _________f _2__5____f _2__5_7__f
        _________d _________d _________d    _________e _________e _________e    _________f _________f ___45____f
        _________d _________d _________d    _________e _________e _________e    _________f _________f ___4__7__f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _____6__9i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _______8_i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _____6__9i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c 1________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c __3______c
        __34_____a 1________a _____6___a    ________9b ______7__b __3__5___b    _______8_c _2_45____c _2_______c

        _________d _________d _________d    _________e _________e _________e    _________f _2__5____f _2__5_7__f
        _________d _________d _________d    _________e _________e _________e    _________f _________f ___45____f
        _________d _________d _________d    _________e _________e _________e    _________f _________f ___4__7__f

        _________g _________g _________g    _________h _________h _________h    _________i _________i _____6__9i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _______8_i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _____6__9i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("skipped")
def test_sudoku_explicit_hidden_unique_rectangle_south_west_row_chute():
    actual = \
        f"""
        ___4__67_a __3__6_8_a _2_______a    ___4_6_89b 1__4____9b 1__4____9b    ___4__7__c ____5____c 1_34____9c
        _________a ___4___8_a _________a    _2_4_6_89b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _2_4___89b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _2_4_6___e _________e _________e    _________f _________f _________f
        _________d _________d _________d    __3_____9e _________e _________e    _________f _________f _________f
        _________d _________d _________d    ____5____e _________e _________e    _________f _________f _________f

        _________g _________g _________g    1________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    __34____9h _________h _________h    _________i _________i _________i
        _________g _________g _________g    ______7__h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        ___4__67_a __3__6_8_a _2_______a    _____6_89b 1__4____9b 1__4____9b    ___4__7__c ____5____c 1_34____9c
        _________a ___4___8_a _________a    _2_4_6_89b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _2_4___89b _________b _________b    _________c _________c _________c

        _________d _________d _________d    _2_4_6___e _________e _________e    _________f _________f _________f
        _________d _________d _________d    __3_____9e _________e _________e    _________f _________f _________f
        _________d _________d _________d    ____5____e _________e _________e    _________f _________f _________f

        _________g _________g _________g    1________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    __34____9h _________h _________h    _________i _________i _________i
        _________g _________g _________g    ______7__h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_xyz_wing_north():
    actual = \
        f"""
        ____a 1_3_a   ____b ____b
        ____a ____a   ____b ____b

        ____c 123_c   ____d ____d
        _23_c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a 1_3_a   ____b ____b
        ____a ____a   ____b ____b

        ____c 123_c   ____d ____d
        _23_c 12_4c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False


def test_sudoku_4x4_xyz_wing_south():
    actual = \
        f"""
        ____a ____a   ____b 1__4b
        ____a ____a   12_4b ____b

        ____c ____c   _2_4d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   123_b 1__4b
        ____a ____a   12_4b ____b

        ____c ____c   _2_4d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False


def test_sudoku_4x4_xyz_wing_east():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c 123_c   1_3_d ____d
        _23_c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        12_4c 123_c   1_3_d ____d
        _23_c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False


def test_sudoku_4x4_xyz_wing_west():
    actual = \
        f"""
        1_3_a ____a   123_b ____b
        ____a ____a   ____b _23_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        1_3_a ____a   123_b 12_4b
        ____a ____a   ____b _23_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False


# sudoku_explicit_xyz_wing_cols_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a __3__6___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3_5____g 123456789g __3_56___g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_xyz_wing_cols_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a __3__6___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 12_456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3_5____g 123456789g __3_56___g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 12_456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_xyz_wing_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123______d    123456789e 123456789e 123456789e    1_3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23______d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_xyz_wing_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 12_456789d 12_456789d 123______d    123456789e 123456789e 123456789e    1_3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23______d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_xy_wing_2_fences_in_rows():
    actual = \
        f"""
        ____a 12__a   ____b 1_3_b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        12_4a 12__a   ____b 1_3_b
        _23_a ____a   ____b 12_4b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_xy_wing_2_fences_in_cols():
    actual = \
        f"""
        ____a ____a   _2_4b ____b
        ____a ____a   ____b 1__4b

        ____c ____c   ____d 12__d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   _2_4b 1_34b
        ____a ____a   ____b 1__4b

        ____c ____c   1_34d 12__d
        ____c ____c   1_34d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_ne():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 1_3_a   12__b ____b

        ____c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a 1_3_a   12__b ____b

        ____c 12_4c   _23_d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_nw():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 1__4a   12__b ____b

        ____c _2_4c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a 1__4a   12__b ____b

        ____c _2_4c   1_34d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_se():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   __34b ____b

        ____c 1__4c   1_3_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a 123_a   __34b ____b

        ____c 1__4c   1_3_d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_sw():
    actual = \
        f"""
        ____a ____a   ____b ____b
        __34a ____a   ____b ____b

        _2_4c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        __34a ____a   12_4b ____b

        _2_4c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


# sudoku_explicit_xy_wing_2_fences_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 1___5____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1_3______i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i __3_5____i 123456789i
#
# sudoku_explicit_xy_wing_2_fences_col_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _23456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _23456789f 1___5____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _23456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1_3______i _23456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i __3_5____i 123456789i
#
# sudoku_explicit_xy_wing_2_fences_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 12_______d    123456789e 123456789e 123456789e    1_3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23______d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_2_fences_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 12_456789d 12_456789d 12_______d    123456789e 123456789e 123456789e    1_3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23______d 123456789d 123456789d    123456789e 123456789e 123456789e    12_456789f 12_456789f 12_456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_east_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1___5____d    123456789e 123456789e 123456789e    123456789f 123456789f ____5___9f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1_______9i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_east_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1___5____d    123456789e 123456789e 123456789e    123456789f 123456789f ____5___9f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g _23456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1_______9i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_west_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b _______89b    ______78_c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e ______7_9e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_west_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b _______89b    ______78_c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e ______7_9e    123456_89f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_east_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    ______78_b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3____8_g 123456789g 123456789g    __3___7__h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_east_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1234567_9a 123456789a 123456789a    ______78_b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3____8_g 123456789g 123456789g    __3___7__h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_west_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _2_____8_e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 1______8_h 123456789h    12_______i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_west_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _2_____8_e 123456789e    1_3456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 1______8_h 123456789h    12_______i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


def test_sudoku_4x4_x_wing_in_rows():
    if solve(4,
             f"""
            ____a 1234a   _2__b ____b
            ____a _2__a   __3_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 12_4a   _2__b ____b
            ____a _2__a   __3_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_ne_control():
    if solve(4, f"""
                ____a ____a   ____b ____b
                ____a ___4a   __3_b ____b

                ____c ____c   ____d 1234d
                ____c __3_c   ____d ___4d
                """, None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_nw():
    if solve(4,
             f"""
            ____a 1234a   _2__b ____b
            ____a _2__a   __3_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 12_4a   _2__b ____b
            ____a _2__a   __3_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_nw_control():
    if solve(4, f"""
            ____a 1234a   _2__b ____b
            ____a ____a   __3_b ____b

            ____c _2__c   ____d ____d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_se():
    if solve(4,
             f"""
            ____a 1___a   ____b _2__b
            ____a _2__a   ____b 1234b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 1___a   ____b _2__b
            ____a _2__a   ____b _234b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_se_control():
    if solve(4, f"""
            ____a 1___a   ____b _2__b
            ____a ____a   ____b 1234b

            ____c _2__c   ____d ____d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_sw():
    if solve(4,
             f"""
            ____a ___4a   __3_b ____b
            ____a 1234a   ___4b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ___4a   __3_b ____b
            ____a 12_4a   ___4b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_sw_control():
    if solve(4, f"""
            ____a ____a   __3_b ____b
            ____a 1234a   ___4b ____b

            ____c ___4c   ____d ____d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 1234b

            ____c ____c   ___4d 1___d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 123_b

            ____c ____c   ___4d 1___d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_ne_control():
    if solve(4, f"""
            ____a 1___a   ____b 1234b
            ____a ____a   ____b ____b

            ____c ___4c   ____d 1___d
            ____c ____c   ____d ____d
            """,
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_nw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            1234a ___4a   ____b ____b

            ___4c __3_c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            12_4a ___4a   ____b ____b

            ___4c __3_c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_nw_control():
    if solve(4, f"""
            ____a ____a   ____b ____b
            1234a ___4a   ____b ____b

            ____c __3_c   ____d ____d
            ___4c ____c   ____d ____d
            """,
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_se():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ___4b 1___b

            ____c ____c   ____d ____d
            ____c ____c   1___d 1234d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ___4b 1___b

            ____c ____c   ____d ____d
            ____c ____c   1___d 123_d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_se_control():
    if solve(4, f"""
            ____a ____a   ____b ____b
            ____a ___4a   ____b 1___b

            ____c ____c   ____d ____d
            ____c 1___c   ____d 1234d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_sw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 2___b

            ____c ____c   1234d 1___d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 2___b

            ____c ____c   1_34d 1___d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_sw_control():
    if solve(4, f"""
            ____a ____a   ____b ____b
            ____a 1___a   ____b 2___b

            ____c 1234c   ____d 1___d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ___4c   ____d 1234d
            ____c __3_c   ____d ___4d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ___4c   ____d 12_4d
            ____c __3_c   ____d ___4d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_9x9_avoidable_rectangle_type1():
    if solve(9,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    ______7__f 123456789f _2_____8_f 

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    _______8_i 123456789i ______7__i 
        """,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    ______7__f 123456789f _2_______f 

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    _______8_i 123456789i ______7__i 
        """,
             AvoidableRectangleType1()):
        return
    assert False


# sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1________d    123456789e 123456789e 123456789e    _____6_8_f 123456789f 123456789f
# 123456789d 123456789d _____6___d    123456789e 123456789e 123456789e    1________f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1________d    123456789e 123456789e 123456789e    _______8_f 123456789f 123456789f
# 123456789d 123456789d _____6___d    123456789e 123456789e 123456789e    1________f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __3__6___c 123456789c 1________c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1________i 123456789i _____6___i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __3______c 123456789c 1________c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1________i 123456789i _____6___i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

# sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 1_____7__g    _______8_h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g _______8_g    ______7__h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 1________g    _______8_h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g _______8_g    ______7__h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ______7__a 123456789a _____6___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _____6___d 123456789d _2____7__d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ______7__a 123456789a _____6___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _____6___d 123456789d _2_______d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

# sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d _2_______d    1________e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1________d    _2______9e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d _2_______d    1________e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1________d    ________9e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _______8_a ________9a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1_______9d _______8_d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _______8_a ________9a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1________d _______8_d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

# sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# ________9d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 1________f 123456789f
# 1___56___d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ________9f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

# sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# ________9d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 1________f 123456789f
# ____56___d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ________9f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


def test_sudoku_4x4_ar2_normal_east():
    actual = \
        f"""
        ____a __3_a   ____b 12__b
        ____a _2__a   ____b 1_3_b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a __3_a   _234b 12__b
        ____a _2__a   _234b 1_3_b
        ____c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_goofy_east():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   _2__b 1_3_b
        ____c ____c   __3_d 12__d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b _234b
        ____a ____a   _2__b 1_3_b
        ____c ____c   __3_d 12__d
        ____c ____c   ____d _234d
        """

    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ar2_normal_east_control():
    actual = \
        f"""
        ____a __3_a   ____b 12__b
        ____a ____a   ____b ____b
        ____c _2__c   ____d 1_3_d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_goofy_east_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a _2__a   ____b 1_3_b
        ____c __3_c   ____d 12__d
        ____c ____c   ____d ____d
        """

    expected = None

    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ar2_chute_normal_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        1_3_a _23_a   ____b ____b
        _2__c 1___c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a 12_4a   ____b ____b
        1_3_a _23_a   12_4b 12_4b
        _2__c 1___c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_goofy_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        ____c _23_c   1_3_d ____d
        ____c 1___c   _2__d ____d
        """
    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        12_4c _23_c   1_3_d 12_4d
        ____c 1___c   _2__d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_normal_north_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        1_3_a 1_3_a   ____b ____b
        _2__c 1___c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_goofy_north_control():
    actual = \
        f"""
       ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        ____c _23_c   1_3_d ____d
        ____c 1___c   ____d _2__d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_normal_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   12__d ____d
        ____c 123_c   12__d ____d
        """
    expected = \
        f"""
        ____a 12_4a   ____b ____b
        ____a 12_4a   ____b ____b
        12__c 123_c   12__d ____d
        12_4c 123_c   12__d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_goofy_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a 12__a   ____b ____b
        123_c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a ____a   ____b ____b
        123_a 12__a   ____b ____b
        123_c 12__c   ____d ____d
        12_4c ____c   ____d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_normal_south():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   ____d ____d
        123_c ____c   ____d ____d
        """
    expected = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   12_4d 12_4d
        12__c 12_4c   ____d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_goofy_south():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a 123_a   123_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a 12__a   12__b ____b
        12_4a 123_a   123_b 12_4b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_normal_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   12__b ____b
        123_c 123_c   ____d ____d
        ____c 123_c   12__d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_goofy_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a ____a   12__b ____b
        123_c ____c   12__d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ar2_chute_normal_south_control():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        123_c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_goofy_south_control():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


# def test_():
#     if solve(9,
#              f"""
#
#             """,
#              f"""
#
#             """, None):
#         return
#     assert False


# sudoku_explicit_avoidable_rectangle_type2_east_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 1________e    _23______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e _2_______e    1_3______f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_east_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    12_456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    12_456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    12_456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 1________e    _23______f 12_456789f 12_456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    12_456789f 12_456789f 12_456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e _2_______e    1_3______f 12_456789f 12_456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12_456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12_456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    12_456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_east_goofy_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 1________b _23______b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _2_______e 1_3______e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_east_goofy_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 1________b _23______b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 12_456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 12_456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _2_______e 1_3______e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 12_456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 12_456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 12_456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_north_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    _23______b 123456789b 1_3______b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    1________h 123456789h _2_______h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_north_expected
# 123456789a 123456789a 123456789a    12_456789b 12_456789b 12_456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    12_456789b 12_456789b 12_456789b    123456789c 123456789c 123456789c
# 12_456789a 12_456789a 12_456789a    _23______b 12_456789b 1_3______b    12_456789c 12_456789c 12_456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    1________h 123456789h _2_______h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_north_goofy_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g _______89g    ______7_9h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g ______7__g    _______8_h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_north_goofy_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 12345678_g 12345678_g _______89g    ______7_9h 12345678_h 12345678_h    12345678_i 12345678_i 12345678_i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g ______7__g    _______8_h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_south_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    1________e 123456789e _2_______e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    _23______h 123456789h 1_3______h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_south_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    1________e 123456789e _2_______e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 12_456789g 12_456789g 12_456789g    _23______h 12_456789h 1_3______h    12_456789i 12_456789i 12_456789i
# 123456789g 123456789g 123456789g    12_456789h 12_456789h 12_456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    12_456789h 12_456789h 12_456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_west_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _2_____8_d ____5____d 1________d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _2___6__9d _____6__9d __3______d    123456789e 123456789e 123456789e    123456789f 123456789f _______8_f
# ______7__d _______89d ___4_____d    123456789e 123456789e 123456789e    123456789f 123456789f _____6___f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_avoidable_rectangle_type2_west_expected
# 123456789a 12345678_a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 12345678_a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 12345678_a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _2_____8_d ____5____d 1________d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _2___6___d _____6__9d __3______d    123456789e 123456789e 123456789e    123456789f 123456789f _______8_f
# ______7__d _______89d ___4_____d    123456789e 123456789e 123456789e    123456789f 123456789f _____6___f
#
# 123456789g 12345678_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 12345678_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 12345678_g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


# sudoku_explicit_wxyz_wing_2_fences_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e ____56___e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _____6__9e _______89e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h ____5__8_h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_wxyz_wing_2_fences_col_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 1234_6789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e ____56___e 1234_6789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _____6__9e _______89e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h ____5__8_h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_wxyz_wing_2_fences_row_chute_actual
# 123456789a 123456789a __3__6_8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a __3__6___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a __3__678_a    123456789b ______78_b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_wxyz_wing_2_fences_row_chute_expected
# 123456789a 123456789a __3__6_8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a __3__6___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1234567_9a 1234567_9a __3__678_a    123456789b ______78_b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_wxyz_wing_3_fences_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d _2_4_____d 123456789d    123456789e 1234_____e 123456789e    123456789f __34_____f 123456789f
# 123456789d 123456789d 123456789d    1__4_____e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# sudoku_explicit_wxyz_wing_3_fences_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d _2_4_____d 123456789d    123_56789e 1234_____e 123_56789e    123456789f __34_____f 123456789f
# 123456789d 123456789d 123456789d    1__4_____e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


# sudoku_explicit_wxyz_wing_3_fences_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ___45____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _2_4_____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _2__5___9g ___4____9g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_wxyz_wing_3_fences_col_chute_expected
#
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ___45____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _2_4_____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123_56789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _2__5___9g ___4____9g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123_56789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


# sudoku_explicit_naked_quad_cols_actual
# _2_456_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2__56_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2_4_6___a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 1_3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1_3_5____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# __3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# __3___7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ________9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __34_6___g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_naked_quad_cols_expected
# _2_4_6_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2___6_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2_4_6___a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 1_3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1_3_5____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# __3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# __3___7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ________9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ___4_6___g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_naked_quad_fences_actual
#
# __3__678_a ______7_9a _2_______a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ___4__78_a ___4__7_9a ___4___8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1_345678_a 1__45_7__a __3456_8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_naked_quad_fences_expected
# __3__6___a ______7_9a _2_______a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ___4__78_a ___4__7_9a ___4___8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1_3_56___a 1___5____a __3_56___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_naked_quad_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1__4__7_9g 123456789g 123456789g    1__4__7_9h 123456789h 1__4__7_9h    123456789i 123456789i 1__4__7_9i
#
# sudoku_explicit_naked_quad_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1__4__7_9g _23_56_8_g _23_56_8_g    1__4__7_9h _23_56_8_h 1__4__7_9h    _23_56_8_i _23_56_8_i 1__4__7_9i
#
#
#


# from tests_explicit.test_small_explicit import solve


def test_sudoku_explicit_simple_coloring():
    if solve(9,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b _23456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b _23456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b _23456789b    123456789c 123456789c 123456789c 

        _23456789d _23456789d 123456789d    123456789e _23456789e _23456789e    _23456789f _23456789f _23456789f 
        123456789d 123456789d 123456789d    _23456789e _23456789e _23456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    _23456789e _23456789e 123456789e    123456789f 123456789f 123456789f 

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h _23456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h _23456789h    123456789i 123456789i 123456789i 
        """,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b _23456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b _23456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b _23456789b    123456789c 123456789c 123456789c 

        _23456789d _23456789d 123456789d    123456789e _23456789e _23456789e    _23456789f _23456789f _23456789f 
        123456789d 123456789d 123456789d    _23456789e _23456789e _23456789e    123456789f 123456789f 123456789f 
        123456789d 123456789d 123456789d    _23456789e _23456789e 123456789e    123456789f 123456789f 123456789f 

        123456789g 123456789g _23456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h _23456789h    123456789i 123456789i 123456789i 
        123456789g 123456789g 123456789g    123456789h 123456789h _23456789h    123456789i 123456789i 123456789i 
        """,
             tech.SimpleColoring()):
        return
    assert False


# sudoku_explicit_hidden_quad_cols_actual
# _____67__a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _______89a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# __34_____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# ___456___d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _2____7_9d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1_3____8_d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# ___4__7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 12_______g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3_5____g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_hidden_quad_cols_expected
# _____67__a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _______89a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# __34_____a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# ___456___d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _2______9d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1______8_d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# ___4__7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 12_______g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3_5____g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_hidden_quad_fences_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 1_3__6_8_g 1___56_8_g _23___78_g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23____8_g _23______g ___4__7__g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1_3__6__9g 1___5_6_9g _234__7__g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_hidden_quad_fences_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 1____6___g 1___56___g _23___78_g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23____8_g _23______g ___4__7__g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1____6__9g 1___5_6_9g _234__7__g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_hidden_quad_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ____56789g 123456789g ____56789g    123456789h ____56789h 123456789h    ____56789i 123456789i ____56789i
#
#
# sudoku_explicit_hidden_quad_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ____56789g 1234_____g ____56789g    1234_____h ____56789h 1234_____h    ____56789i 1234_____i ____56789i
#
#
#


# from tests_explicit.test_small_explicit import solve


def test_sudoku_explicit_finned_jelly_fish_cols():
    actual = \
        f"""
    123456789a ____56__9a 123456789a    1234_6789b 123456789b 123456789b    123456789c ____5_7_9c ____5_7_9c 
    123456789a 1234_6789a 123456789a    ____5_7_9b 123456789b 123456789b    123456789c 1234_6789c 1234_6789c 
    123456789a 1234_6789a 123456789a    ____5_7_9b 123456789b 123456789b    123456789c ____5_7_9c 1234_6789c 

    123456789d 1234_6789d 123456789d    1234_6789e 123456789e 123456789e    123456789f 1234_6789f 1234_6789f 
    123456789d 1234_6789d 123456789d    1234_6789e 123456789e 123456789e    123456789f 1234_6789f 1234_6789f 
    123456789d 1234_6789d 123456789d    1234_6789e 123456789e 123456789e    123456789f 1234_6789f 1234_6789f 

    123456789g ____56__9g 123456789g    ____5___9h 123456789h 123456789h    123456789i 1234_6789i 1234_6789i 
    123456789g 1234_6789g 123456789g    1234_6789h 123456789h 123456789h    123456789i 1234_6789i 1234_6789i 
    123456789g 1234_6789g 123456789g    1234_6789h 123456789h 123456789h    123456789i __3_5____i 1___5____i 


    """
    expected = \
        f"""
    123456789a ____56__9a 123456789a    1234_6789b 1234_6789b 1234_6789b    123456789c ____5_7_9c ____5_7_9c 
    123456789a 1234_6789a 123456789a    ____5_7_9b 123456789b 123456789b    123456789c 1234_6789c 1234_6789c 
    123456789a 1234_6789a 123456789a    ____5_7_9b 1234_6789b 1234_6789b    123456789c ____5_7_9c 1234_6789c 

    123456789d 1234_6789d 123456789d    1234_6789e 123456789e 123456789e    123456789f 1234_6789f 1234_6789f 
    123456789d 1234_6789d 123456789d    1234_6789e 123456789e 123456789e    123456789f 1234_6789f 1234_6789f 
    123456789d 1234_6789d 123456789d    1234_6789e 123456789e 123456789e    123456789f 1234_6789f 1234_6789f 

    123456789g ____56__9g 123456789g    ____5___9h 123456789h 123456789h    123456789i 1234_6789i 1234_6789i 
    123456789g 1234_6789g 123456789g    1234_6789h 123456789h 123456789h    123456789i 1234_6789i 1234_6789i 
    123456789g 1234_6789g 123456789g    1234_6789h 123456789h 123456789h    123456789i __3_5____i 1___5____i 
    """
    if solve(9, actual, expected, tech.FinnedJellyFish()):
        return
    assert False


# sudoku_explicit_finned_jelly_fish_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b _23456789b 123456789b    _23456789c 123456789c _23456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _23456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23456789g 123456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_finned_jelly_fish_rows_expected
#
# 123456789a _23456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b _23456789b 123456789b    _23456789c 123456789c _23456789c
# 123456789a _23456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _23456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23456789g 123456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

# sudoku_explicit_shashimi_jelly_fish_cols_actual
# 123456789a 123456789a 1234_6789a    1234_6789b 1234_6789b 123456789b    123456789c 123456789c 1234_6789c
# 123456789a 123456789a 1234_6789a    ____5__8_b 1___5_78_b 123456789b    123456789c 123456789c 1234_6789c
# 123456789a 123456789a 1234_6789a    1234_6789b 1234_6789b 123456789b    123456789c 123456789c 1234_6789c
#
# 123456789d 123456789d 1234_6789d    1234_6789e 1234_6789e 123456789e    123456789f 123456789f 1234_6789f
# 123456789d 123456789d 1234_6789d    ____5__8_e 1234_6789e 123456789e    123456789f 123456789f 1234_6789f
# 123456789d 123456789d ____56_8_d    1234_6789e 1234_6789e 123456789e    123456789f 123456789f ____5__89f
#
# 123456789g 123456789g 1234_6789g    1234_6789h 1234_6789h 123456789h    123456789i 123456789i 1234_6789i
# 123456789g 123456789g 1234_6789g    1234_6789h 1___5_78_h 123456789h    123456789i 123456789i ____5__8_i
# 123456789g 123456789g 1___5__8_g    1234_6789h ____5_78_h 123456789h    123456789i 123456789i ____5__89i
#
# sudoku_explicit_shashimi_jelly_fish_cols_expected
# 123456789a 123456789a 1234_6789a    1234_6789b 1234_6789b 123456789b    123456789c 123456789c 1234_6789c
# 123456789a 123456789a 1234_6789a    ____5__8_b 1___5_78_b 123456789b    123456789c 123456789c 1234_6789c
# 123456789a 123456789a 1234_6789a    1234_6789b 1234_6789b 123456789b    123456789c 123456789c 1234_6789c
#
# 123456789d 123456789d 1234_6789d    1234_6789e 1234_6789e 123456789e    123456789f 123456789f 1234_6789f
# 123456789d 123456789d 1234_6789d    ____5__8_e 1234_6789e 123456789e    123456789f 123456789f 1234_6789f
# 123456789d 123456789d ____56_8_d    1234_6789e 1234_6789e 1234_6789e    123456789f 123456789f ____5__89f
#
# 123456789g 123456789g 1234_6789g    1234_6789h 1234_6789h 123456789h    123456789i 123456789i 1234_6789i
# 123456789g 123456789g 1234_6789g    1234_6789h 1___5_78_h 123456789h    123456789i 123456789i ____5__8_i
# 123456789g 123456789g 1___5__8_g    1234_6789h ____5_78_h 123456789h    123456789i 123456789i ____5__89i
# sudoku_explicit_shashimi_jelly_fish_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a _23456789a 123456789a    123456789b _23456789b 123456789b    _23456789c 123456789c _23456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _23456789d _23456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23456789g _23456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_shashimi_jelly_fish_rows_expected
# 123456789a _23456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a _23456789a 123456789a    123456789b _23456789b 123456789b    _23456789c 123456789c _23456789c
# 123456789a _23456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# _23456789d _23456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f _23456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# _23456789g _23456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i


# from tests_explicit.test_small_explicit import solve
from techniques.FishyCycle import FishyCycle


def test_sudoku_explicit_fishy_cycle():
    actual = \
        f"""
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
_23456789a _23456789a 123456789a    123456789b _23456789b _23456789b    _23456789c _23456789c _23456789c 

123456789d 123456789d 123456789d    123456789e _23456789e _23456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    _23456789e _23456789e _23456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    _23456789e _23456789e 123456789e    123456789f 123456789f 123456789f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
_23456789g _23456789g 123456789g    _23456789h _23456789h 123456789h    _23456789i _23456789i _23456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 


    """
    expected = \
        f"""
123456789a 123456789a _23456789a    _23456789b 123456789b _23456789b    123456789c 123456789c 123456789c 
123456789a 123456789a _23456789a    _23456789b 123456789b _23456789b    123456789c 123456789c 123456789c 
_23456789a _23456789a 123456789a    123456789b _23456789b _23456789b    _23456789c _23456789c _23456789c 

123456789d 123456789d _23456789d    123456789e _23456789e _23456789e    123456789f 123456789f 123456789f 
123456789d 123456789d _23456789d    _23456789e _23456789e _23456789e    123456789f 123456789f 123456789f 
123456789d 123456789d _23456789d    _23456789e _23456789e 123456789e    123456789f 123456789f 123456789f 

123456789g 123456789g _23456789g    _23456789h 123456789h _23456789h    123456789i 123456789i 123456789i 
_23456789g _23456789g 123456789g    _23456789h _23456789h 123456789h    _23456789i _23456789i _23456789i 
123456789g 123456789g _23456789g    _23456789h 123456789h _23456789h    123456789i 123456789i 123456789i 
"""
    if solve(9, actual, expected, FishyCycle()):
        return
    assert False


# from tests_explicit.test_small_explicit import solve


def test_sudoku_explicit_x_chain():
    if solve(9,
             f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        _23456789a _23456789a 123456789a    123456789b _23456789b _23456789b    _23456789c _23456789c _23456789c

        123456789d 123456789d 123456789d    123456789e _23456789e _23456789e    123456789f 123456789f 123456789f
        123456789d 123456789d 123456789d    _23456789e _23456789e _23456789e    123456789f 123456789f 123456789f
        123456789d 123456789d 123456789d    _23456789e _23456789e 123456789e    123456789f 123456789f 123456789f

        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
        _23456789g 123456789g _23456789g    _23456789h _23456789h 123456789h    _23456789i _23456789i _23456789i
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        """,
             f"""
        123456789a _23456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        123456789a _23456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        _23456789a _23456789a 123456789a    123456789b _23456789b _23456789b    _23456789c _23456789c _23456789c

        123456789d 123456789d 123456789d    123456789e _23456789e _23456789e    123456789f 123456789f 123456789f
        123456789d 123456789d 123456789d    _23456789e _23456789e _23456789e    123456789f 123456789f 123456789f
        123456789d 123456789d 123456789d    _23456789e _23456789e 123456789e    123456789f 123456789f 123456789f

        123456789g 123456789g _23456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        _23456789g 123456789g _23456789g    _23456789h _23456789h 123456789h    _23456789i _23456789i _23456789i
        123456789g 123456789g _23456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        """,
             tech.XChain()):
        return
    assert False


from tech import tech


# from tests_explicit.test_small_explicit import solve


def test_sudoku_explicit_xy_chain():
    if solve(9,
             f"""
            _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
            _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
            _________a _________a 12_______a    _________b _________b _23______b    _________c _________c _________c 

            _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 
            _________d _________d _________d    _________e _________e _________e    _________f _________f _________f 
            _________d 1__4_____d _________d    _________e _________e __34_____e    _________f _________f _________f 

            _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
            _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
            _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
            """,
             f"""
            _________a _23456789a _________a    _________b _________b _________b    _________c _________c _________c 
            _________a _23456789a _________a    _________b _________b _________b    _________c _________c _________c 
            _________a _23456789a 12_______a    _________b _________b _23______b    _________c _________c _________c 

            _________d _________d _23456789d    _________e _________e _________e    _________f _________f _________f 
            _________d _________d _23456789d    _________e _________e _________e    _________f _________f _________f 
            _________d 1__4_____d _23456789d    _________e _________e __34_____e    _________f _________f _________f 

            _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
            _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
            _________g _________g _________g    _________h _________h _________h    _________i _________i _________i 
            """,
             tech.XyChain()):
        return
    assert False


# sudoku_explicit_sue_de_coq_cols_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    1________c _2____78_c _2_45_7__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    ________9c _2___67__c _2_4567__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __34_____c _23____8_c _2_4_____c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ___4_____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f _____67__f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ________9f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i ____5____i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23__67__i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 1________i 123456789i
#
#
#
# sudoku_explicit_sue_de_coq_cols_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    1________c _2____78_c ____5_7__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    ________9c _2___67__c ____567__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __34_____c _23____8_c _2_4_____c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ___4_____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f _____67__f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ________9f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i ____5____i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23______i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 1________i 123456789i
#
# sudoku_explicit_sue_de_coq_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 12_______d 123456789d    12345____e 12345____e 12345____e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e __34_____e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_sue_de_coq_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    12___6789e 12___6789e 12___6789e    123456789f 123456789f 123456789f
# __34_6789d 12_______d __34_6789d    12345____e 12345____e 12345____e    __34_6789f __34_6789f __34_6789f
# 123456789d 123456789d 123456789d    12___6789e 12___6789e __34_____e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i

@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_0():
    puzzle_string = f"""
    almost_locked_candidates_0.sudoku
    9
    .7.|...|198
    829|713|564
    614|985|237
    ---+---+---
    15.|.9.|.7.
    .96|357|..1
    ..7|..1|.59
    ---+---+---
    762|138|945
    ...|629|713
    931|574|...
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_1():
    puzzle_string = f"""
    almost_locked_candidates_1.sudoku
    9
    4 0 0 0 6 0 0 2 0
    8 6 7 4 2 5 3 9 1
    0 0 0 8 0 7 6 4 5
    7 0 0 2 0 0 0 8 6
    3 2 0 0 0 6 0 1 9
    6 9 0 0 0 4 2 0 0
    9 7 0 3 0 2 0 0 0
    5 0 3 0 0 8 9 0 2
    0 8 0 0 5 0 0 0 0
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_2():
    puzzle_string = f"""
    almost_locked_candidates_2.sudoku
    9
    .7.|..6|3..
    .5.|2..|.89
    ..1|...|2..
    ---+---+---
    4.8|..2|...
    ...|1.5|...
    ...|6..|8.1
    ---+---+---
    ..4|...|1..
    18.|..4|.5.
    ..3|8..|.7.
    shashimi xwing
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_3():
    puzzle_string = f"""
    almost_locked_candidates_3.sudoku
    9
    987|..2|.4.
    132|4..|.9.
    .4.|7.9|28.
    ---+---+---
    .98|...|175
    .1.|975|86.
    75.|..1|93.
    ---+---+---
    .69|12.|.5.
    .71|..3|629
    .2.|697|418
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_4():
    puzzle_string = f"""
    almost_locked_candidates_4.sudoku
    9
    ..9|..5|.43
    ...|...|...
    .5.|..3|.28
    ---+---+---
    .8.|.2.|.5.
    ..6|...|9..
    .9.|.4.|.3.
    ---+---+---
    32.|9..|.1.
    ...|...|...
    41.|5..|6..
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_5():
    puzzle_string = f"""
    almost_locked_candidates_5.sudoku
    9
    0 0 0 1 0 0 0 0 4
    2 0 7 0 0 0 0 0 5
    0 1 0 5 0 0 3 6 0
    0 0 5 9 1 0 0 0 6
    0 0 0 0 0 0 0 0 0
    8 0 0 0 2 6 9 0 0
    0 8 3 0 0 5 0 1 0
    5 0 0 0 0 0 7 0 2
    1 0 0 0 0 8 0 0 0
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_6():
    puzzle_string = f"""
    almost_locked_candidates_6.sudoku
    9
    2 6 1 0 0 8 9 0 5
    3 9 8 6 0 5 4 0 2
    4 5 7 0 9 0 8 0 6
    9 1 4 0 6 0 5 8 3
    8 2 5 0 0 0 6 9 7
    7 3 6 8 5 9 1 2 4
    6 7 2 5 8 1 3 4 9
    1 4 3 9 2 6 7 5 8
    5 8 9 3 0 0 2 6 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_00():
    puzzle_string = f"""
    avoidable_rectangle_type1_00.sudoku
    9
    _a _a 8a 0b 3b 0b 0c 4c 0c
    _a _a _a 1b 7b 6b 0c 0c 0c
    6a _a _a 0b 8b 0b 0c 0c 0c
    7d 9d 0d 0e 0e 0e 8f 0f 3f
    0d 0d 4d 0e 0e 0e 9f 0f 0f
    1d 0d 2d 0e 0e 0e 0f 5f 7f
    0g 0g 0g 0h 6h 0h 0i 0i 2i
    0g 0g 0g 5h 2h 9h 0i 0i 0i
    0g 8g 0g 0h 4h 0h 3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_01():
    puzzle_string = f"""
    avoidable_rectangle_type1_01.sudoku
    9
    _a 9a 3a   2b _b _b   5c _c _c
    _a _a _a   _b _b 4b   9c _c _c
    4a _a _a   _b _b _b   _c 8c _c
    
    _d 4d 9d   3e _e _e   _f _f _f
    _d 7d _d   9e _e 1e   _f 5f _f
    _d _d _d   _e _e 7e   2f 3f _f
    
    _g 8g _g   _h _h _h   _i _i 6i
    _g _g 1g   8h _h _h   _i _i _i
    _g _g 2g   _h _h 5h   3i 1i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), NakedPair(),
                                UniqueRectangleType1(), ShashimiXWing(), AvoidableRectangleType1(),
                                LockedCandidatesClaiming()])


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_02():
    puzzle_string = f"""
    avoidable_rectangle_type1_02.sudoku
    9
    _a _a _a 8b 0b 0b 0c 0c 2c
    _a _a _a 0b 0b 6b 4c 0c 5c
    1a _a _a 2b 9b 4b 0c 0c 7c
    0d 0d 0d 0e 0e 0e 2f 0f 9f
    0d 5d 3d 0e 0e 0e 7f 8f 0f
    8d 0d 4d 0e 0e 0e 0f 0f 0f
    4g 0g 0g 3h 5h 7h 0i 0i 6i
    5g 0g 6g 9h 0h 0h 0i 0i 0i
    2g 0g 0g 0h 0h 8h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_03():
    puzzle_string = f"""
    avoidable_rectangle_type1_03.sudoku
    9
    _a _a _a 0b 7b 3b 0c 5c 0c
    2a _a _a 8b 0b 0b 0c 0c 3c
    _a _a _a 0b 2b 0b 0c 8c 0c
    0d 1d 5d 7e 0e 0e 0f 0f 6f
    3d 2d 0d 0e 0e 0e 0f 1f 8f
    8d 0d 0d 0e 0e 2e 9f 3f 0f
    0g 9g 0g 0h 1h 0h 0i 0i 0i
    1g 0g 0g 0h 0h 6h 0i 0i 9i
    0g 6g 0g 5h 4h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_04():
    puzzle_string = f"""
    avoidable_rectangle_type1_04.sudoku
    9
    6a _a _a 9b 0b 0b 5c 1c 4c
    5a 9a 1a 6b 4b 3b 8c 2c 7c
    7a 2a 4a 8b 5b 1b 9c 3c 6c
    8d 5d 2d 7e 6e 4e 1f 9f 3f
    4d 0d 9d 1e 0e 0e 7f 0f 5f
    1d 7d 0d 5e 0e 0e 4f 0f 2f
    2g 0g 0g 4h 0h 0h 3i 5i 8i
    3g 0g 0g 2h 0h 0h 6i 4i 9i
    9g 4g 0g 3h 8h 0h 2i 7i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_05():
    puzzle_string = f"""
    avoidable_rectangle_type1_05.sudoku
    9
    _a _a 6a 0b 2b 8b 0c 5c 0c
    _a 8a _a 0b 0b 0b 0c 0c 0c
    _a _a 1a 0b 0b 6b 7c 0c 9c
    8d 0d 0d 2e 9e 0e 4f 0f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 0d 7d 0e 6e 1e 0f 0f 5f
    6g 0g 4g 7h 0h 0h 1i 0i 0i
    0g 0g 0g 0h 0h 0h 0i 3i 0i
    0g 5g 0g 1h 4h 0h 9i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_07():
    puzzle_string = f"""
    avoidable_rectangle_type1_07.sudoku
    9
    4a _a _a 0b 0b 6b 0c 7c 0c
    1a 8a _a 0b 0b 0b 0c 0c 0c
    3a _a _a 0b 1b 0b 0c 8c 6c
    0d 0d 7d 6e 0e 0e 0f 0f 8f
    0d 6d 0d 0e 5e 0e 0f 9f 0f
    8d 0d 0d 0e 0e 9e 2f 0f 0f
    6g 1g 0g 0h 3h 0h 0i 0i 9i
    0g 0g 0g 0h 0h 0h 0i 2i 4i
    0g 4g 0g 7h 0h 0h 0i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_08():
    puzzle_string = f"""
    avoidable_rectangle_type1_08.sudoku
    9
    _a _a 8a 2b 0b 4b 0c 0c 0c
    _a 2a _a 0b 1b 5b 0c 0c 0c
    _a 4a _a 0b 0b 0b 6c 5c 0c
    0d 0d 4d 7e 0e 0e 0f 0f 8f
    9d 0d 0d 0e 8e 0e 0f 0f 6f
    7d 0d 0d 0e 0e 2e 9f 0f 0f
    0g 1g 3g 0h 0h 0h 0i 7i 0i
    0g 0g 0g 1h 9h 0h 0i 4i 0i
    0g 0g 0g 8h 0h 7h 3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_09():
    puzzle_string = f"""
    avoidable_rectangle_type1_09.sudoku
    9
    _a _a _a 0b 0b 4b 0c 0c 0c
    4a 7a 1a 0b 0b 0b 2c 9c 0c
    _a _a 9a 7b 0b 0b 1c 0c 8c
    0d 0d 0d 2e 0e 8e 0f 0f 9f
    0d 0d 0d 0e 6e 0e 0f 0f 0f
    3d 0d 0d 5e 0e 7e 0f 0f 0f
    7g 0g 5g 0h 0h 2h 4i 0i 0i
    0g 3g 6g 0h 0h 0h 8i 2i 7i
    0g 0g 0g 3h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_10():
    puzzle_string = f"""
    avoidable_rectangle_type1_10.sudoku
    9
    9a 7a 4a 0b 0b 5b 0c 0c 0c
    _a _a 8a 0b 0b 1b 2c 0c 0c
    _a _a _a 0b 0b 7b 4c 0c 0c
    0d 2d 0d 1e 0e 0e 0f 8f 0f
    0d 0d 0d 0e 8e 0e 0f 0f 0f
    0d 1d 0d 0e 0e 9e 0f 2f 0f
    0g 0g 7g 9h 0h 0h 0i 0i 0i
    0g 0g 6g 5h 0h 0h 3i 0i 0i
    0g 0g 0g 4h 0h 0h 7i 6i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_11():
    puzzle_string = f"""
    avoidable_rectangle_type1_11.sudoku
    9
    1a 4a 9a 0b 3b 0b 0c 0c 0c
    _a 2a _a 0b 0b 0b 1c 0c 0c
    _a 6a 7a 1b 0b 2b 0c 3c 0c
    0d 0d 0d 2e 0e 4e 0f 0f 0f
    0d 8d 0d 0e 0e 0e 0f 7f 0f
    0d 0d 0d 6e 0e 8e 0f 0f 0f
    0g 5g 0g 4h 0h 3h 8i 1i 0i
    0g 0g 4g 0h 0h 0h 0i 6i 0i
    0g 0g 0g 0h 1h 0h 4i 2i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_12():
    puzzle_string = f"""
    avoidable_rectangle_type1_12.sudoku
    9
    _a _a 3a 0b 0b 4b 0c 7c 0c
    _a 4a 2a 0b 0b 0b 0c 0c 8c
    1a 6a _a 0b 8b 0b 0c 0c 0c
    2d 0d 6d 3e 0e 0e 0f 8f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 7d 0d 0e 0e 1e 2f 0f 9f
    0g 0g 0g 0h 1h 0h 0i 2i 3i
    9g 0g 0g 0h 0h 0h 4i 5i 0i
    0g 1g 0g 2h 0h 0h 7i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_13():
    puzzle_string = f"""
    avoidable_rectangle_type1_13.sudoku
    9
    _a 2a 5a 0b 7b 6b 0c 4c 0c
    7a 1a 9a 0b 0b 0b 8c 6c 0c
    _a 6a 4a 1b 0b 0b 2c 0c 7c
    0d 3d 8d 7e 0e 2e 0f 0f 6f
    0d 9d 6d 0e 8e 0e 7f 0f 0f
    5d 7d 2d 9e 6e 1e 4f 0f 0f
    9g 4g 3g 6h 1h 7h 5i 0i 0i
    6g 5g 1g 0h 0h 0h 3i 7i 4i
    2g 8g 7g 4h 3h 5h 6i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type2_0():
    puzzle_string = f"""
    avoidable_rectangle_type2_0.sudoku
    9
    _a _a 5a 0b 0b 0b 6c 8c 3c
    _a 6a 4a 5b 3b 8b 9c 0c 2c
    8a 2a 3a 9b 6b 0b 0c 5c 0c
    2d 0d 0d 0e 0e 6e 5f 0f 0f
    3d 0d 0d 0e 0e 0e 0f 2f 6f
    6d 0d 1d 2e 0e 0e 0f 0f 9f
    4g 3g 2g 6h 5h 1h 7i 9i 8i
    0g 0g 7g 8h 0h 0h 3i 6i 5i
    5g 8g 6g 0h 0h 0h 2i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_finned_x_wing_02():
    puzzle_string = f"""
    finned_x_wing_02.sudoku
    9
    4a 2a 1a 8b 0b 9b 0c 7c 0c
    6a 5a _a 1b 2b 0b 9c 0c 0c
    3a 9a _a 0b 5b 0b 0c 0c 1c
    0d 8d 0d 0e 0e 1e 7f 0f 0f
    7d 4d 3d 0e 9e 0e 8f 1f 6f
    0d 1d 6d 7e 8e 0e 0f 5f 0f
    8g 3g 0g 9h 4h 0h 1i 6i 7i
    1g 6g 9g 0h 7h 8h 0i 4i 0i
    0g 7g 4g 3h 1h 6h 0i 9i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_finned_x_wing_03():
    puzzle_string = f"""
    finned_x_wing_03.sudoku
    9
    _a 7a 6a 0b 8b 9b 0c 0c 0c
    _a _a _a 0b 0b 3b 0c 8c 6c
    5a 8a 3a 0b 0b 4b 0c 0c 0c
    3d 0d 7d 8e 4e 0e 1f 0f 0f
    0d 2d 0d 0e 9e 0e 0f 4f 0f
    0d 0d 4d 0e 3e 0e 8f 0f 5f
    0g 0g 0g 9h 0h 0h 2i 3i 8i
    6g 0g 2g 3h 0h 8h 0i 0i 0i
    0g 3g 0g 4h 2h 0h 6i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_0():
    puzzle_string = f"""
    hidden_quad_0.sudoku
    9
    8a _a _a 1b 0b 9b 0c 4c 0c
    _a _a _a 0b 5b 0b 0c 6c 8c
    _a _a _a 7b 0b 0b 1c 9c 3c
    1d 0d 2d 0e 0e 0e 0f 5f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 7d 0d 0e 0e 0e 3f 0f 4f
    9g 1g 5g 0h 0h 3h 0i 0i 0i
    7g 2g 0g 0h 6h 0h 0i 0i 0i
    0g 8g 0g 5h 0h 1h 0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_1():
    puzzle_string = f"""
    hidden_quad_1.sudoku
    9
    3a 6a 4a 0b 0b 9b 0c 0c 0c
    5a _a _a 3b 0b 6b 1c 0c 0c
    8a _a 1a 0b 7b 0b 0c 0c 0c
    7d 0d 0d 0e 0e 0e 6f 2f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 4d 5d 0e 0e 0e 0f 0f 9f
    0g 0g 0g 0h 8h 0h 9i 0i 2i
    0g 0g 2g 6h 0h 7h 0i 0i 1i
    0g 0g 0g 4h 0h 0h 3i 7i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_2():
    puzzle_string = f"""
    hidden_quad_2.sudoku
    9
    _a _a _a 0b 0b 7b 0c 5c 0c
    _a _a _a 0b 0b 3b 0c 4c 0c
    _a _a _a 6b 4b 0b 0c 0c 8c
    0d 4d 1d 0e 0e 0e 2f 9f 0f
    6d 0d 3d 0e 9e 0e 1f 0f 5f
    0d 9d 2d 0e 0e 0e 6f 8f 0f
    3g 0g 0g 0h 1h 9h 0i 0i 0i
    0g 6g 0g 7h 0h 0h 0i 0i 0i
    0g 1g 0g 3h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_3():
    puzzle_string = f"""
    hidden_quad_3.sudoku
    9
    _a _a _a 6b 0b 0b 8c 0c 0c
    _a _a _a 0b 9b 1b 0c 4c 0c
    _a _a _a 3b 0b 0b 9c 0c 0c
    5d 0d 2d 0e 0e 0e 4f 0f 1f
    3d 1d 0d 0e 2e 0e 0f 8f 7f
    7d 0d 9d 0e 0e 0e 2f 0f 5f
    0g 0g 1g 0h 0h 6h 0i 0i 0i
    0g 3g 0g 2h 7h 0h 0i 0i 0i
    0g 0g 7g 0h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_4():
    puzzle_string = f"""
    hidden_quad_4.sudoku
    9
    3a 1a _a 4b 0b 9b 0c 0c 0c
    _a _a _a 1b 7b 5b 0c 0c 0c
    _a _a 7a 0b 3b 0b 0c 0c 0c
    0d 0d 9d 0e 0e 0e 0f 8f 7f
    0d 0d 1d 0e 9e 0e 4f 0f 0f
    8d 7d 0d 0e 0e 0e 3f 0f 0f
    0g 0g 0g 0h 6h 0h 2i 0i 0i
    0g 0g 0g 5h 1h 3h 0i 0i 0i
    0g 0g 0g 9h 0h 2h 0i 6i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_8():
    puzzle_string = f"""
    hidden_quad_8.sudoku
    9
    _a _a _a 5b 4b 1b 0c 9c 0c
    _a _a _a 7b 9b 3b 5c 0c 0c
    _a _a _a 2b 8b 6b 3c 0c 4c
    0d 4d 0d 1e 0e 8e 9f 0f 5f
    0d 6d 0d 9e 2e 5e 4f 3f 0f
    9d 0d 5d 3e 0e 4e 0f 2f 0f
    6g 3g 1g 8h 5h 2h 7i 4i 9i
    0g 0g 0g 4h 3h 7h 0i 0i 0i
    0g 8g 0g 6h 1h 9h 2i 5i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_9():
    puzzle_string = f"""
    hidden_quad_9.sudoku
    9
    2a 4a 7a 6b 3b 1b 9c 8c 5c
    8a 3a 6a 5b 4b 9b 1c 2c 7c
    5a 9a 1a 8b 2b 7b 4c 3c 6c
    6d 0d 0d 0e 0e 0e 3f 7f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 1d 9d 0e 0e 0e 0f 0f 8f
    9g 2g 3g 1h 8h 5h 7i 6i 4i
    1g 7g 5g 4h 6h 2h 8i 9i 3i
    4g 6g 8g 7h 9h 3h 5i 1i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_0():
    puzzle_string = f"""
    hidden_triple_0.sudoku
    9
    _a _a _a 5b 0b 0b 0c 7c 9c
    _a 1a _a 0b 0b 0b 0c 5c 4c
    _a _a 4a 0b 8b 0b 0c 0c 0c
    2d 0d 0d 9e 0e 3e 0f 0f 8f
    0d 0d 7d 0e 0e 0e 9f 0f 0f
    6d 0d 0d 2e 0e 7e 0f 0f 3f
    0g 0g 0g 0h 7h 0h 1i 0i 0i
    1g 6g 0g 0h 0h 0h 0i 8i 0i
    4g 7g 0g 0h 0h 5h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_2():
    puzzle_string = f"""
    hidden_triple_2.sudoku
    9
    _a 3a _a 0b 8b 0b 0c 1c 0c
    _a _a _a 0b 3b 0b 8c 0c 0c
    _a _a _a 6b 7b 0b 0c 3c 5c
    7d 9d 2d 1e 6e 3e 5f 8f 4f
    5d 4d 8d 2e 9e 7e 3f 6f 1f
    3d 0d 0d 5e 4e 8e 7f 0f 0f
    6g 0g 0g 0h 1h 4h 0i 0i 0i
    4g 0g 9g 0h 2h 6h 1i 0i 0i
    0g 7g 0g 0h 5h 9h 0i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_3():
    puzzle_string = f"""
    hidden_triple_3.sudoku
    9
    _a 9a _a 2b 3b 6b 0c 1c 0c
    5a _a _a 1b 7b 0b 3c 0c 9c
    _a _a _a 5b 9b 0b 2c 0c 0c
    0d 0d 0d 9e 4e 2e 7f 0f 0f
    2d 4d 9d 7e 8e 5e 6f 3f 1f
    8d 7d 5d 3e 6e 1e 0f 0f 0f
    0g 5g 7g 6h 2h 3h 0i 0i 0i
    6g 0g 0g 8h 5h 0h 0i 0i 3i
    0g 8g 0g 4h 1h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_4():
    puzzle_string = f"""
    hidden_triple_4.sudoku
    9
    _a _a _a 9b 0b 0b 7c 0c 0c
    _a 5a _a 6b 0b 3b 0c 4c 2c
    _a _a _a 0b 0b 0b 0c 0c 1c
    8d 3d 0d 0e 5e 0e 9f 2f 0f
    7d 0d 0d 0e 0e 0e 0f 0f 3f
    0d 2d 5d 0e 4e 0e 0f 8f 7f
    5g 0g 0g 0h 0h 0h 0i 0i 0i
    3g 6g 0g 8h 0h 7h 0i 1i 0i
    0g 0g 1g 0h 0h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_5():
    puzzle_string = f"""
    hidden_triple_5.sudoku
    9
_a _a _a 0b 7b 0b 0c 0c 0c
9a _a _a 4b 2b 5b 1c 0c 0c
4a _a _a 0b 0b 3b 0c 2c 5c
0d 5d 0d 0e 0e 0e 7f 0f 8f
0d 6d 0d 0e 0e 0e 0f 3f 0f
8d 0d 3d 0e 0e 0e 0f 6f 0f
6g 1g 0g 7h 0h 0h 0i 0i 9i
0g 0g 5g 1h 8h 6h 0i 0i 7i
0g 0g 0g 0h 3h 0h 0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_6():
    puzzle_string = f"""
    hidden_triple_6.sudoku
    9
_a 9a _a 0b 0b 0b 0c 5c 4c
_a _a _a 0b 0b 5b 0c 6c 7c
_a _a 4a 0b 2b 0b 0c 0c 0c
3d 0d 0d 6e 0e 1e 0f 0f 8f
0d 0d 6d 0e 0e 0e 7f 0f 0f
1d 0d 9d 8e 0e 7e 6f 0f 2f
0g 0g 0g 0h 6h 0h 9i 0i 0i
4g 6g 0g 5h 0h 0h 0i 0i 0i
9g 3g 0g 0h 0h 0h 0i 2i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_0():
    puzzle_string = f"""
    naked_quad_0.sudoku
    9
    _a 7a 3a 6b 0b 4b 0c 0c 0c
    _a 4a 2a 0b 0b 1b 0c 0c 0c
    5a _a 9a 3b 0b 0b 0c 4c 0c
    3d 0d 7d 0e 0e 0e 8f 0f 0f
    0d 9d 0d 8e 0e 0e 0f 7f 0f
    0d 0d 6d 0e 0e 0e 3f 0f 4f
    0g 2g 0g 0h 0h 8h 1i 0i 6i
    0g 0g 0g 2h 0h 0h 4i 5i 0i
    0g 0g 0g 1h 0h 9h 7i 2i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_1():
    puzzle_string = f"""
    naked_quad_1.sudoku
    9
    5a _a _a 7b 0b 4b 2c 0c 0c
    _a 7a _a 1b 0b 0b 9c 0c 4c
    _a _a _a 8b 0b 0b 0c 0c 0c
    7d 0d 0d 0e 0e 0e 3f 0f 0f
    2d 0d 1d 0e 0e 0e 7f 0f 5f
    0d 0d 4d 0e 0e 0e 0f 0f 6f
    0g 0g 0g 0h 0h 6h 0i 0i 0i
    4g 0g 6g 0h 0h 8h 0i 1i 0i
    0g 0g 5g 9h 0h 1h 0i 0i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_2():
    puzzle_string = f"""
    naked_quad_2.sudoku
    9
    5a _a _a 1b 4b 0b 0c 7c 2c
    _a 7a _a 0b 0b 6b 0c 0c 5c
    _a _a _a 0b 5b 0b 0c 1c 6c
    0d 0d 0d 5e 0e 0e 0f 0f 0f
    8d 3d 0d 0e 0e 0e 0f 4f 7f
    0d 0d 0d 0e 0e 2e 0f 0f 0f
    6g 8g 0g 0h 0h 0h 0i 0i 0i
    7g 0g 0g 3h 0h 0h 0i 9i 0i
    7g 0g 0g 3h 0h 0h 0i 9i 0i
    9g 4g 0g 0h 8h 5h 0i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_3():
    puzzle_string = f"""
    naked_quad_3.sudoku
    9
    9a _a _a 0b 3b 0b 6c 0c 0c
    _a _a _a 6b 0b 5b 0c 9c 3c
    _a 3a _a 9b 0b 7b 0c 0c 0c
    7d 6d 3d 0e 9e 8e 0f 0f 4f
    5d 4d 8d 7e 6e 0e 3f 0f 9f
    1d 9d 2d 0e 5e 0e 8f 7f 6f
    0g 0g 0g 8h 0h 0h 0i 0i 0i
    8g 2g 0g 5h 0h 0h 0i 0i 0i
    0g 0g 9g 0h 4h 0h 0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_1():
    puzzle_string = f"""
    wxyz_wing_1.sudoku
    9
_a 4a 1a 0b 0b 0b 0c 0c 0c
8a 7a _a 2b 4b 0b 0c 0c 0c
2a _a 6a 0b 0b 9b 0c 0c 0c
4d 0d 0d 7e 9e 5e 3f 0f 0f
0d 0d 0d 3e 0e 0e 0f 0f 0f
0d 0d 5d 6e 8e 4e 0f 0f 9f
0g 0g 4g 9h 0h 0h 1i 0i 2i
0g 0g 0g 1h 6h 3h 4i 5i 8i
0g 0g 0g 4h 0h 0h 9i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_2():
    puzzle_string = f"""
    wxyz_wing_2.sudoku
    9
_a 4a 1a 0b 0b 0b 0c 0c 0c
8a 7a _a 2b 4b 0b 0c 0c 0c
2a _a 6a 0b 0b 9b 0c 0c 0c
4d 0d 0d 7e 9e 5e 3f 0f 0f
0d 0d 0d 3e 0e 0e 0f 0f 0f
0d 0d 5d 6e 8e 4e 0f 0f 9f
0g 0g 4g 9h 0h 0h 1i 0i 2i
0g 0g 0g 1h 6h 3h 4i 5i 8i
0g 0g 0g 4h 0h 0h 9i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_3():
    puzzle_string = f"""
    wxyz_wing_3.sudoku
    9
_a 4a 1a 0b 0b 0b 0c 0c 0c
8a 7a _a 2b 4b 0b 0c 0c 0c
2a _a 6a 0b 0b 9b 0c 0c 0c
4d 0d 0d 7e 9e 5e 3f 0f 0f
0d 0d 0d 3e 0e 0e 0f 0f 0f
0d 0d 5d 6e 8e 4e 0f 0f 9f
0g 0g 4g 9h 0h 0h 1i 0i 2i
0g 0g 0g 1h 6h 3h 4i 5i 8i
0g 0g 0g 4h 0h 0h 9i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_7():
    puzzle_string = f"""
    wxyz_wing_7.sudoku
    9
3a 6a 7a 5b 9b 2b 1c 4c 8c
2a 5a 4a 8b 1b 0b 9c 0c 7c
9a 1a 8a 0b 0b 4b 0c 0c 0c
1d 9d 0d 0e 0e 0e 8f 0f 0f
4d 7d 0d 9e 0e 0e 0f 0f 1f
8d 3d 6d 0e 0e 0e 0f 7f 9f
5g 0g 9g 3h 0h 7h 6i 1i 0i
7g 0g 3g 0h 6h 0h 0i 9i 5i
6g 2g 1g 4h 5h 9h 7i 8i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_8():
    puzzle_string = f"""
    wxyz_wing_8.sudoku
    9
4a _a 7a 0b 0b 0b 0c 9c 8c
_a 6a 3a 8b 0b 4b 5c 7c 2c
5a _a 8a 0b 0b 0b 0c 1c 4c
8d 7d 1d 5e 3e 9e 2f 4f 6f
0d 0d 4d 2e 0e 1e 9f 0f 7f
2d 0d 0d 4e 7e 0e 1f 0f 3f
0g 8g 0g 0h 0h 0h 4i 0i 5i
0g 4g 0g 3h 0h 0h 7i 2i 1i
7g 0g 0g 0h 4h 0h 8i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_9():
    puzzle_string = f"""
    wxyz_wing_9.sudoku
    9
_a _a _a 0b 0b 7b 5c 2c 0c
_a _a _a 0b 0b 0b 0c 9c 4c
_a _a _a 8b 0b 0b 1c 6c 7c
0d 0d 7d 9e 0e 6e 0f 8f 0f
0d 6d 0d 7e 0e 2e 0f 3f 0f
0d 5d 0d 4e 8e 3e 7f 1f 6f
1g 0g 3g 0h 0h 9h 6i 0i 0i
6g 4g 0g 0h 0h 0h 0i 0i 0i
0g 2g 5g 6h 0h 0h 0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_1():
    puzzle_string = f"""
    w_wing_type_d_1.sudoku
    9
7a _a _a 9b 0b 5b 2c 0c 0c
2a 5a 4a 0b 8b 7b 0c 9c 6c
9a _a _a 2b 0b 0b 0c 5c 7c
5d 7d 9d 0e 0e 3e 6f 0f 2f
8d 2d 0d 5e 9e 6e 0f 7f 0f
6d 4d 0d 7e 2e 0e 5f 0f 9f
0g 8g 7g 0h 0h 2h 9i 6i 5i
3g 9g 2g 6h 5h 0h 7i 0i 0i
0g 6g 5g 0h 7h 9h 0i 2i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_2():
    puzzle_string = f"""
    w_wing_type_d_2.sudoku
    9
4a _a 8a 1b 6b 0b 3c 2c 0c
_a _a 1a 0b 0b 0b 8c 4c 0c
_a _a 2a 8b 7b 4b 5c 1c 0c
6d 1d 4d 2e 9e 8e 7f 5f 3f
8d 0d 5d 0e 4e 1e 6f 9f 2f
0d 2d 9d 6e 5e 0e 4f 8f 1f
2g 8g 7g 5h 1h 0h 9i 0i 4i
5g 4g 6g 0h 0h 0h 1i 0i 8i
1g 9g 3g 4h 8h 0h 2i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_3():
    puzzle_string = f"""
    w_wing_type_d_3.sudoku
    9
_a _a 8a 0b 2b 0b 0c 6c 0c
_a _a 6a 4b 1b 0b 0c 0c 2c
_a 5a _a 8b 0b 0b 0c 9c 0c
5d 0d 0d 0e 0e 0e 0f 0f 0f
9d 0d 7d 0e 0e 0e 3f 0f 6f
0d 0d 0d 0e 0e 0e 0f 0f 7f
0g 3g 0g 0h 0h 9h 0i 2i 0i
1g 0g 0g 0h 8h 2h 6i 0i 0i
0g 7g 0g 0h 6h 0h 1i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_4():
    puzzle_string = f"""
    w_wing_type_d_4.sudoku
    9
_a 5a _a 0b 0b 0b 9c 3c 0c
9a _a 1a 0b 8b 0b 0c 0c 0c
6a _a 3a 0b 9b 4b 8c 1c 5c
0d 1d 6d 0e 5e 0e 3f 7f 2f
7d 0d 9d 0e 0e 0e 5f 0f 1f
5d 3d 0d 0e 0e 0e 0f 9f 0f
1g 9g 7g 6h 3h 0h 0i 5i 0i
3g 6g 5g 0h 4h 0h 7i 0i 9i
2g 8g 4g 0h 7h 0h 1i 6i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_5():
    puzzle_string = f"""
    w_wing_type_d_5.sudoku
    9
7a 5a 2a 3b 0b 0b 4c 1c 0c
8a _a _a 0b 0b 9b 0c 0c 0c
_a _a _a 0b 4b 0b 0c 0c 0c
0d 6d 0d 0e 0e 0e 0f 0f 0f
0d 9d 0d 6e 8e 3e 0f 5f 0f
0d 0d 0d 0e 0e 0e 0f 8f 0f
0g 0g 0g 0h 1h 0h 0i 0i 0i
0g 0g 0g 4h 0h 0h 0i 0i 8i
0g 3g 1g 0h 0h 5h 2i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_0():
    puzzle_string = f"""
    xyz_wing_0.sudoku
    9
_a _a _a 0b 0b 3b 4c 0c 5c
_a 9a 6a 0b 0b 0b 7c 8c 0c
_a _a _a 0b 0b 0b 0c 2c 0c
0d 1d 0d 0e 8e 9e 6f 0f 0f
0d 0d 0d 4e 0e 5e 0f 0f 0f
0d 0d 5d 1e 2e 0e 0f 4f 0f
0g 3g 0g 0h 0h 0h 0i 0i 0i
0g 4g 9g 0h 0h 0h 3i 1i 0i
2g 0g 7g 6h 0h 0h 0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_1():
    puzzle_string = f"""
    xyz_wing_1.sudoku
    9
9a 3a _a 0b 0b 8b 0c 0c 0c
_a _a _a 3b 0b 0b 0c 8c 5c
6a _a _a 0b 1b 0b 0c 9c 4c
0d 5d 0d 0e 0e 0e 0f 1f 9f
0d 0d 6d 0e 0e 0e 4f 0f 0f
1d 7d 0d 0e 0e 0e 0f 2f 0f
7g 6g 0g 0h 9h 0h 0i 0i 1i
5g 8g 0g 0h 0h 3h 0i 0i 0i
0g 0g 0g 1h 0h 0h 0i 3i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_2():
    puzzle_string = f"""
    xyz_wing_2.sudoku
    9
9a 3a _a 0b 0b 8b 0c 0c 0c
_a _a _a 3b 0b 0b 0c 8c 5c
6a _a _a 0b 1b 0b 0c 9c 4c
0d 5d 0d 0e 0e 0e 0f 1f 9f
0d 0d 6d 0e 0e 0e 4f 0f 0f
1d 7d 0d 0e 0e 0e 0f 2f 0f
7g 6g 0g 0h 9h 0h 0i 0i 1i
5g 8g 0g 0h 0h 3h 0i 0i 0i
0g 0g 0g 1h 0h 0h 0i 3i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_3():
    puzzle_string = f"""
    xyz_wing_3.sudoku
    9
9a 3a _a 0b 0b 8b 0c 0c 0c
_a _a _a 3b 0b 0b 0c 8c 5c
6a _a _a 0b 1b 0b 0c 9c 4c
0d 5d 0d 0e 0e 0e 0f 1f 9f
0d 0d 6d 0e 0e 0e 4f 0f 0f
1d 7d 0d 0e 0e 0e 0f 2f 0f
7g 6g 0g 0h 9h 0h 0i 0i 1i
5g 8g 0g 0h 0h 3h 0i 0i 0i
0g 0g 0g 1h 0h 0h 0i 3i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_4():
    puzzle_string = f"""
    xyz_wing_4.sudoku
    9
8a _a 3a 7b 6b 0b 0c 2c 1c
1a 7a 2a 0b 0b 0b 0c 9c 6c
4a _a 6a 2b 1b 0b 0c 7c 8c
7d 3d 4d 8e 2e 5e 6f 1f 9f
6d 1d 5d 0e 0e 0e 8f 4f 2f
2d 8d 9d 6e 4e 1e 7f 5f 3f
5g 4g 0g 0h 0h 6h 2i 3i 7i
3g 2g 0g 0h 0h 0h 9i 6i 4i
9g 6g 7g 4h 3h 2h 1i 8i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_5():
    puzzle_string = f"""
    xyz_wing_5.sudoku
    9
    9
9a 7a _a 4b 0b 0b 0c 5c 0c
1a _a _a 0b 0b 0b 0c 0c 0c
_a 3a 8a 0b 0b 2b 0c 7c 0c
5d 0d 0d 2e 3e 0e 0f 0f 0f
0d 0d 0d 1e 0e 6e 0f 0f 0f
0d 0d 0d 0e 4e 7e 0f 0f 8f
0g 2g 0g 3h 0h 0h 1i 6i 0i
0g 0g 0g 0h 0h 0h 0i 0i 4i
0g 8g 0g 0h 0h 5h 0i 9i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_6():
    puzzle_string = f"""
    xyz_wing_6.sudoku
    9
7a 1a 3a 8b 9b 4b 5c 6c 2c
6a 9a 2a 3b 1b 5b 8c 4c 7c
_a _a 5a 7b 6b 2b 3c 1c 9c
0d 0d 8d 1e 5e 9e 0f 0f 0f
0d 0d 1d 4e 8e 7e 0f 0f 0f
0d 0d 9d 2e 3e 6e 1f 0f 8f
0g 0g 7g 6h 2h 1h 0i 0i 0i
1g 5g 4g 9h 7h 8h 6i 2i 3i
9g 2g 6g 5h 4h 3h 7i 8i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_7():
    puzzle_string = f"""
    xyz_wing_7.sudoku
    9
    9
_a 2a 9a 3b 5b 0b 1c 8c 6c
6a 5a 8a 0b 0b 0b 3c 0c 2c
_a _a 3a 2b 6b 8b 0c 9c 0c
8d 6d 5d 1e 4e 3e 0f 0f 0f
9d 7d 1d 8e 2e 5e 0f 0f 3f
0d 0d 2d 9e 7e 6e 8f 5f 1f
0g 8g 6g 0h 0h 0h 0i 0i 0i
2g 0g 7g 5h 8h 0h 0i 0i 4i
5g 9g 4g 6h 3h 2h 7i 1i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_8():
    puzzle_string = f"""
    xyz_wing_8.sudoku
    9
_a _a 6a 3b 5b 8b 0c 4c 0c
5a _a 8a 4b 2b 1b 0c 0c 3c
3a 4a 2a 9b 6b 7b 1c 5c 8c
8d 0d 9d 7e 0e 5e 0f 2f 0f
4d 5d 7d 2e 9e 6e 8f 3f 1f
2d 6d 0d 8e 0e 4e 0f 0f 5f
0g 2g 0g 6h 0h 3h 5i 0i 0i
6g 0g 5g 1h 0h 2h 0i 0i 7i
0g 8g 0g 5h 0h 9h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_9():
    puzzle_string = f"""
    xyz_wing_9.sudoku
    9
5a 4a 3a 8b 6b 1b 7c 9c 2c
7a 9a 2a 5b 3b 4b 0c 8c 0c
8a 1a 6a 9b 7b 2b 0c 0c 4c
9d 2d 1d 0e 0e 0e 8f 7f 3f
4d 5d 8d 7e 2e 3e 0f 6f 0f
6d 3d 7d 1e 9e 8e 4f 2f 5f
1g 0g 9g 3h 0h 0h 2i 0i 7i
3g 0g 4g 2h 0h 7h 0i 1i 0i
2g 7g 5g 0h 1h 9h 0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_01():
    puzzle_string = f"""
    9
6a 9a _a 0b 7b 8b 5c 3c 2c
_a 7a 3a 9b 2b 0b 6c 8c 4c
2a 8a _a 0b 0b 0b 7c 1c 9c
8d 0d 0d 0e 3e 0e 9f 0f 7f
4d 3d 0d 7e 6e 9e 0f 5f 8f
9d 0d 7d 0e 8e 0e 0f 0f 3f
0g 4g 9g 8h 0h 0h 3i 2i 6i
0g 0g 0g 0h 0h 0h 8i 9i 5i
0g 0g 8g 2h 9h 0h 4i 7i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_02():
    puzzle_string = f"""
    xy_wing_02.sudoku
    9
3a 1a 4a 9b 2b 5b 8c 7c 6c
_a 9a 7a 1b 8b 6b 0c 0c 0c
6a 8a _a 4b 7b 3b 0c 0c 1c
8d 5d 6d 7e 3e 2e 0f 0f 9f
0d 3d 9d 5e 4e 0e 7f 6f 0f
4d 7d 0d 6e 9e 0e 5f 0f 3f
7g 6g 0g 2h 1h 4h 0i 0i 0i
0g 4g 0g 8h 6h 9h 0i 0i 7i
9g 2g 0g 3h 5h 7h 6i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_03():
    puzzle_string = f"""
    xy_wing_03.sudoku
    9
3a 1a 4a 9b 2b 5b 8c 7c 6c
_a 9a 7a 1b 8b 6b 0c 0c 0c
6a 8a _a 4b 7b 3b 0c 0c 1c
8d 5d 6d 7e 3e 2e 0f 0f 9f
0d 3d 9d 5e 4e 0e 7f 6f 0f
4d 7d 0d 6e 9e 0e 5f 0f 3f
7g 6g 0g 2h 1h 4h 0i 0i 0i
0g 4g 0g 8h 6h 9h 0i 0i 7i
9g 2g 0g 3h 5h 7h 6i 0i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_04():
    puzzle_string = f"""
    xy_wing_04.sudoku
    9
_a 6a 3a 0b 4b 5b 2c 8c 0c
_a _a _a 0b 0b 3b 6c 7c 4c
4a _a _a 0b 0b 6b 0c 5c 3c
8d 4d 0d 0e 0e 0e 7f 0f 6f
0d 3d 1d 4e 6e 7e 8f 0f 0f
9d 7d 6d 0e 0e 0e 0f 0f 0f
6g 5g 0g 0h 0h 0h 0i 0i 2i
0g 1g 0g 6h 0h 0h 5i 0i 8i
3g 9g 8g 5h 2h 0h 0i 6i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_05():
    puzzle_string = f"""
    xy_wing_05.sudoku
    9
_a _a 6a 0b 8b 0b 1c 0c 7c
_a _a 8a 0b 0b 0b 9c 0c 5c
7a _a 5a 3b 0b 2b 6c 8c 4c
3d 7d 9d 0e 0e 4e 2f 5f 8f
5d 6d 1d 8e 2e 3e 4f 7f 9f
8d 4d 2d 9e 0e 0e 3f 6f 1f
0g 2g 3g 0h 0h 8h 7i 4i 6i
6g 8g 4g 0h 3h 0h 5i 0i 2i
0g 5g 7g 2h 4h 6h 8i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_06():
    puzzle_string = f"""
    xy_wing_06.sudoku
    9
3a _a 1a 8b 0b 0b 7c 5c 2c
_a _a _a 0b 0b 1b 6c 8c 9c
_a 8a _a 7b 0b 0b 3c 1c 4c
0d 0d 0d 0e 0e 8e 5f 0f 1f
1d 0d 0d 5e 2e 0e 8f 0f 3f
8d 5d 3d 9e 1e 7e 4f 2f 6f
7g 4g 8g 1h 9h 3h 2i 6i 5i
2g 3g 9g 6h 8h 5h 1i 4i 7i
6g 1g 5g 0h 7h 0h 9i 3i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_07():
    puzzle_string = f"""
    xy_wing_07.sudoku
    9
6a 2a 1a 3b 7b 9b 5c 4c 8c
9a 4a 5a 1b 8b 2b 6c 3c 7c
7a 3a 8a 0b 5b 0b 2c 9c 1c
1d 0d 9d 8e 0e 0e 0f 0f 0f
8d 0d 3d 0e 6e 1e 9f 0f 0f
4d 6d 2d 5e 9e 7e 8f 1f 3f
5g 1g 6g 0h 0h 8h 3i 0i 9i
2g 8g 7g 9h 0h 0h 0i 0i 0i
3g 9g 4g 0h 0h 5h 0i 8i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_08():
    puzzle_string = f"""
    xy_wing_08.sudoku
    9
6a 8a 9a 7b 2b 1b 4c 5c 3c
1a 5a 2a 4b 8b 3b 9c 6c 7c
_a 7a _a 9b 6b 5b 0c 8c 0c
0d 4d 0d 8e 3e 0e 0f 7f 5f
7d 0d 0d 0e 4e 0e 3f 0f 8f
0d 3d 0d 0e 7e 2e 0f 0f 4f
0g 0g 0g 6h 5h 8h 7i 4i 9i
5g 9g 7g 2h 1h 4h 8i 3i 6i
0g 6g 0g 3h 9h 7h 5i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_09():
    puzzle_string = f"""
    xy_wing_09.sudoku
    9
    1a 9a 3a 6b 0b 0b 7c 0c 8c
    4a 2a 8a 1b 7b 0b 6c 0c 0c
    7a 5a 6a 0b 0b 0b 0c 0c 0c
    0d 4d 7d 0e 3e 0e 0f 6f 0f
    5d 6d 0d 4e 9e 7e 0f 8f 3f
    0d 3d 0d 0e 6e 0e 4f 7f 0f
    6g 8g 9g 7h 1h 0h 3i 0i 4i
    3g 1g 5g 0h 4h 6h 0i 9i 7i
    2g 7g 4g 0h 0h 0h 0i 1i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_10():
    puzzle_string = f"""
    xy_wing_10.sudoku
    9
_a 6a _a 4b 0b 1b 0c 8c 0c
9a 8a 4a 5b 7b 6b 2c 3c 1c
1a _a _a 0b 0b 9b 6c 7c 4c
6d 0d 2d 0e 0e 3e 4f 0f 7f
3d 4d 1d 7e 9e 0e 8f 6f 0f
8d 7d 0d 6e 4e 0e 1f 0f 3f
4g 0g 8g 0h 0h 7h 0i 0i 6i
5g 3g 0g 2h 6h 4h 0i 1i 8i
0g 1g 6g 0h 0h 8h 0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_11():
    puzzle_string = f"""
    xy_wing_11.sudoku
    9
9a 3a 2a 0b 1b 0b 6c 7c 5c
6a 5a 4a 3b 2b 7b 9c 8c 1c
1a 8a 7a 6b 9b 5b 2c 3c 4c
7d 0d 6d 9e 0e 0e 0f 0f 0f
3d 0d 9d 0e 4e 6e 0f 0f 7f
5d 4d 8d 1e 7e 2e 3f 6f 9f
2g 9g 5g 7h 0h 0h 0i 0i 0i
8g 7g 3g 0h 0h 1h 0i 9i 0i
4g 6g 1g 0h 0h 9h 7i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_0():
    puzzle_string = f"""
    x_wing_0.sudoku
    9
    _a _a _a 0b 0b 0b 7c 0c 4c
    3a _a _a 0b 7b 0b 0c 0c 5c
    _a _a _a 0b 1b 8b 0c 0c 2c
    1d 5d 0d 9e 2e 0e 8f 0f 3f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    6d 0d 8d 0e 3e 1e 0f 4f 7f
    2g 0g 0g 8h 4h 0h 0i 0i 0i
    5g 0g 0g 0h 9h 0h 0i 0i 1i
    4g 0g 7g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_1():
    puzzle_string = f"""
    x_wing_1.sudoku
    9
    8a 7a 9a _________b 5b _________b 4c _________c _________c
    2a 5a _________a 7b _________b 4b _________c 9c 8c
    _________a 1a 4a 9b 8b 2b 7c 5c _________c
    9d 4d 7d 5e _________e _________e _________f _________f _________f
    1d 8d 5d 6e 2e 7e 3f 4f 9f
    _________d _________d 2d 4e 9e 8e 5f 1f 7f
    4g 2g 1g 8h 7h _________h _________i _________i 5i
    7g 9g _________g 2h _________h 5h _________i _________i 4i
    5g _________g _________g _________h 4h _________h _________i 7i _________i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_2():
    puzzle_string = f"""
    x_wing_2.sudoku
    9
9a 8a 7a 2b 5b 6b 1c 4c 3c
4a 3a 6a 8b 1b 7b 9c 2c 5c
5a 2a 1a 9b 3b 4b 0c 7c 0c
7d 5d 0d 6e 2e 1e 0f 9f 0f
0d 4d 9d 5e 7e 8e 0f 1f 0f
1d 6d 0d 4e 9e 3e 0f 5f 7f
0g 1g 0g 7h 8h 9h 5i 6i 0i
6g 9g 5g 3h 4h 2h 7i 8i 1i
8g 7g 0g 1h 6h 5h 0i 3i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_3():
    puzzle_string = f"""
    x_wing_3.sudoku
    9
    5a _a 7a 9b 0b 0b 1c 0c 6c
    6a 3a 4a 1b 7b 5b 8c 9c 2c
    _a 1a 9a 0b 0b 0b 5c 0c 7c
    7d 9d 6d 2e 1e 3e 4f 5f 8f
    3d 4d 2d 5e 9e 8e 7f 6f 1f
    1d 5d 8d 6e 4e 7e 9f 2f 3f
    0g 0g 1g 0h 5h 0h 3i 7i 9i
    9g 7g 5g 3h 2h 1h 6i 8i 4i
    4g 0g 3g 7h 0h 9h 2i 1i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_east_in_rows():
    puzzle_string = f"""
        unique_rectangle_type1_south_east_in_rows.sudoku
        9
        6a 7a 2a 5b 9b 3b 1c 4c 8c
1a 3a 8a 0b 0b 4b 5c 7c 9c
4a 9a 5a 1b 7b 8b 3c 2c 6c
9d 2d 0d 0e 5e 1e 8f 3f 0f
3d 1d 0d 8e 0e 9e 0f 5f 0f
5d 8d 4d 7e 3e 2e 9f 6f 1f
0g 4g 1g 3h 0h 6h 7i 9i 5i
0g 5g 3g 9h 0h 7h 6i 1i 0i
7g 6g 9g 0h 1h 5h 0i 8i 3i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_west_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_south_west_in_cols.sudoku
        9
2a 6a _a 9b 3b 0b 0c 0c 0c
_a 8a 3a 6b 4b 0b 0c 0c 2c
4a 9a 7a 5b 2b 8b 6c 3c 1c
7d 4d 6d 2e 8e 9e 3f 1f 5f
8d 5d 9d 3e 1e 6e 2f 4f 7f
0d 0d 2d 7e 5e 4e 8f 6f 9f
6g 2g 8g 4h 9h 5h 1i 7i 3i
9g 7g 0g 0h 6h 3h 5i 2i 0i
0g 0g 0g 0h 7h 2h 0i 0i 6i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_east_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_north_east_in_cols.sudoku
        9
9a 1a 2a 5b 4b 8b 7c 3c 6c
5a 4a _a 1b 7b 0b 8c 9c 2c
8a 7a _a 0b 9b 2b 1c 5c 4c
0d 6d 4d 0e 1e 0e 5f 8f 0f
0d 5d 9d 4e 8e 0e 6f 2f 0f
0d 3d 8d 0e 0e 0e 4f 7f 0f
6g 9g 7g 8h 2h 4h 3i 1i 5i
4g 8g 5g 9h 3h 1h 2i 6i 7i
3g 2g 1g 7h 0h 0h 9i 4i 8i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_east_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_south_east_in_cols.sudoku
        9
8a 3a 7a 4b 0b 0b 5c 6c 1c
_a _a 9a 5b 3b 6b 2c 7c 8c
5a 2a 6a 1b 7b 8b 9c 0c 0c
2d 0d 8d 9e 4e 3e 0f 1f 5f
3d 0d 5d 8e 6e 1e 0f 2f 9f
0d 9d 1d 2e 5e 7e 8f 0f 0f
0g 0g 4g 7h 0h 5h 3i 8i 0i
7g 5g 3g 6h 8h 0h 1i 9i 0i
0g 8g 2g 3h 0h 0h 0i 5i 7i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_west_in_rows():
    puzzle_string = f"""
        unique_rectangle_type1_north_west_in_rows.sudoku
        9
9a 1a 2a 0b 0b 0b 6c 0c 8c
8a 4a 6a 9b 0b 2b 0c 0c 5c
3a 7a 5a 8b 6b 1b 9c 4c 2c
6d 5d 9d 7e 8e 4e 3f 2f 1f
1d 8d 3d 5e 2e 9e 4f 6f 7f
4d 2d 7d 6e 1e 3e 5f 8f 9f
2g 6g 8g 0h 0h 0h 0i 0i 3i
5g 0g 4g 0h 0h 8h 2i 0i 6i
7g 0g 1g 2h 0h 6h 8i 5i 4i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_east_in_rows():
    puzzle_string = f"""
        unique_rectangle_type1_north_east_in_rows.sudoku
        9
2a 3a 7a 6b 5b 9b 8c 4c 1c
8a 9a 6a 3b 0b 0b 7c 2c 5c
5a 4a 1a 8b 2b 7b 9c 6c 3c
6d 7d 3d 1e 8e 5e 2f 9f 4f
9d 8d 0d 2e 0e 6e 0f 0f 7f
1d 2d 0d 9e 7e 0e 6f 0f 8f
4g 5g 2g 7h 9h 0h 0i 8i 6i
7g 0g 8g 5h 0h 2h 4i 0i 9i
3g 0g 9g 4h 0h 8h 5i 7i 2i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_west_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_north_west_in_cols.sudoku
        9
_a 9a 7a 2b 0b 0b 0c 3c 0c
_a 3a 4a 0b 0b 7b 0c 2c 0c
2a 5a 8a 0b 6b 0b 0c 1c 7c
7d 2d 5d 0e 0e 0e 3f 6f 9f
4d 1d 6d 0e 7e 0e 2f 5f 8f
3d 8d 9d 5e 2e 6e 7f 4f 1f
9g 4g 1g 7h 3h 5h 6i 8i 2i
5g 6g 3g 8h 9h 2h 1i 7i 4i
8g 7g 2g 6h 1h 4h 5i 9i 3i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_west_in_rows():
    puzzle_string = f"""   
        unique_rectangle_type1_south_west_in_rows.sudoku
        9
4a _a 3a 7b 0b 0b 0c 0c 5c
8a _a 2a 5b 0b 0b 0c 0c 3c
9a 5a 7a 0b 3b 6b 0c 4c 1c
1d 4d 5d 3e 2e 0e 6f 8f 0f
3d 2d 6d 0e 0e 0e 4f 5f 0f
7d 9d 8d 4e 6e 5e 3f 1f 2f
6g 3g 0g 0h 5h 0h 1i 0i 8i
5g 8g 0g 0h 0h 3h 0i 0i 6i
2g 7g 0g 6h 0h 8h 5i 3i 4i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type2_east():
    puzzle_string = f"""
        unique_rectangle_type2_east.sudoku
        9
7a 2a 3a 0b 5b 4b 9c 8c 0c
_a 8a 4a 0b 9b 2b 0c 0c 3c
_a 9a 1a 8b 0b 3b 0c 2c 4c
3d 4d 5d 0e 1e 8e 0f 9f 2f
8d 0d 6d 3e 2e 9e 4f 0f 5f
9d 0d 2d 4e 0e 5e 8f 3f 0f
2g 3g 7g 9h 4h 6h 1i 5i 8i
4g 5g 9g 2h 8h 1h 3i 6i 7i
1g 6g 8g 5h 3h 7h 2i 4i 9i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type2_south():
    puzzle_string = f"""
        unique_rectangle_type2_south.sudoku
        9
_a 8a _a 0b 3b 0b 2c 7c 4c
_a 4a 2a 0b 0b 7b 0c 5c 3c
3a 7a _a 0b 2b 0b 9c 1c 0c
4d 1d 3d 7e 9e 8e 5f 6f 2f
6d 5d 7d 0e 4e 0e 3f 8f 9f
2d 9d 8d 6e 5e 3e 7f 4f 1f
8g 6g 9g 0h 7h 0h 0i 3i 5i
7g 2g 4g 3h 0h 5h 0i 9i 0i
5g 3g 1g 0h 8h 0h 0i 2i 7i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type2_west():
    puzzle_string = f"""
        unique_rectangle_type2_west.sudoku
        9
2a _a _a 6b 0b 1b 3c 5c 7c
1a 5a 6a 7b 2b 3b 9c 8c 4c
_a 7a 3a 9b 5b 0b 2c 6c 1c
9d 3d 2d 4e 6e 5e 7f 1f 8f
5d 4d 8d 1e 7e 9e 6f 3f 2f
7d 6d 1d 8e 3e 2e 4f 9f 5f
3g 0g 5g 2h 0h 0h 0i 0i 6i
0g 0g 7g 3h 0h 6h 5i 2i 9i
6g 2g 0g 5h 0h 0h 0i 0i 3i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type4_south_rows():
    puzzle_string = f"""
        unique_rectangle_type4_south_rows.sudoku
        9
        3a _a 5a 8b 2b _b 1c 7c 9c
        _a _a _a _b 1b _b 4c _c 6c
        _a _a 1a _b 9b _b 2c _c _c
        5d 1d 6d 4e 8e 9e 7f 2f 3f
        7d 8d 4d _e 3e _e 6f 9f 1f
        2d 9d 3d 6e 7e 1e 8f _f _f
        _g 5g _g _h 6h _h 3i _i 7i
        1g _g 7g _h 5h _h 9i 6i _i
        6g 3g _g _h 4h _h 5i _i 2i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type4_south_cols():
    puzzle_string = f"""
        unique_rectangle_type4_south_cols.sudoku
        9
_a 6a _a 8b 2b 5b 7c 1c 9c
7a _a _a 4b 1b 6b 3c 5c 0c
_a 5a _a 3b 7b 9b 6c 0c 4c
5d 1d 7d 6e 0e 0e 0f 3f 0f
0d 0d 0d 7e 0e 0e 1f 0f 5f
0d 8d 0d 1e 5e 3e 0f 7f 6f
8g 3g 5g 0h 6h 1h 0i 4i 7i
0g 7g 0g 0h 4h 8h 5i 0i 3i
9g 4g 2g 5h 3h 7h 8i 6i 1i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_unique_rectangle_type4_east_rows():
    puzzle_string = f"""
        unique_rectangle_type4_east_rows.sudoku
        9
9a 4a 2a 0b 0b 3b 7c 1c 0c
8a 1a _a 2b 4b 0b 9c 5c 0c
5a 6a _a 0b 0b 1b 4c 2c 0c
2d 8d 6d 3e 0e 0e 0f 9f 4f
0d 7d 9d 0e 8e 2e 3f 6f 0f
0d 3d 5d 0e 0e 0e 8f 7f 2f
6g 5g 1g 7h 3h 4h 2i 8i 9i
7g 9g 4g 0h 2h 8h 6i 3i 0i
3g 2g 8g 6h 0h 0h 0i 4i 7i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_unique_rectangle_type4_west_rows():
    puzzle_string = f"""
        unique_rectangle_type4_west_rows.sudoku
        9        
        6a 9a 1a 0b 4b 8b 2c 7c 0c
_a _a 7a 0b 0b 0b 0c 9c 0c
_a _a _a 0b 9b 7b 0c 4c 0c
7d 8d 6d 9e 1e 2e 3f 5f 4f
9d 0d 0d 0e 3e 0e 7f 8f 1f
5d 1d 3d 7e 8e 4e 9f 2f 6f
1g 3g 0g 0h 0h 0h 8i 6i 7i
0g 7g 0g 0h 6h 0h 5i 1i 2i
2g 6g 5g 8h 7h 1h 4i 3i 9i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_unique_rectangle_type4_west_cols():
    puzzle_string = f"""
        unique_rectangle_type4_west_cols.sudoku
        9
6a 1a _a 5b 7b 4b 0c 0c 2c
2a _a 5a 1b 9b 8b 0c 0c 0c
_a 7a _a 6b 3b 2b 1c 0c 5c
0d 0d 0d 3e 0e 6e 0f 0f 9f
3d 5d 6d 9e 2e 7e 8f 1f 4f
0d 0d 0d 8e 0e 1e 0f 0f 0f
5g 8g 2g 7h 6h 9h 4i 3i 1i
0g 6g 0g 4h 8h 0h 0i 0i 7i
4g 0g 7g 2h 1h 0h 0i 6i 8i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_unique_rectangle_type4_east_cols():
    puzzle_string = f"""
        unique_rectangle_type4_east_cols.sudoku
        9
2a _a _a 0b 0b 0b 7c 9c 5c
_a 5a 7a 9b 0b 0b 6c 1c 4c
9a 1a 6a 7b 4b 5b 3c 8c 2c
7d 6d 1d 2e 8e 4e 5f 3f 9f
0d 0d 0d 5e 9e 1e 8f 6f 7f
5d 9d 8d 3e 7e 6e 2f 4f 1f
1g 3g 0g 8h 5h 7h 0i 2i 6i
0g 0g 5g 0h 0h 9h 0i 7i 3i
6g 7g 0g 4h 0h 0h 0i 5i 8i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_bug():
    puzzle_string = f"""
        bug.sudoku
        9
        4a 6a 5a 1b 3b 2b 9c 7c 8c
        _a _a _a 8b 6b 4b 3c 1c 5c
        1a 3a 8a 5b 9b 7b 4c 2c 6c
        6d 8d 0d 3e 4e 0e 0f 5f 0f
        5d 0d 3d 2e 7e 0e 6f 8f 4f
        0d 0d 4d 6e 5e 8e 0f 3f 0f
        8g 7g 1g 9h 2h 6h 5i 4i 3i
        2g 5g 9g 4h 1h 3h 8i 6i 7i
        3g 4g 6g 7h 8h 5h 2i 9i 1i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_row():
    puzzle_string = f"""
        hidden_triple_row.sudoku
        9
_a 3a 5a 7b 2b 1b 8c 4c 0c
7a _a _a 3b 4b 6b 2c 0c 5c
_a 4a 2a 8b 5b 9b 0c 3c 0c
0d 5d 6d 9e 0e 2e 3f 0f 4f
0d 0d 0d 0e 3e 0e 5f 0f 0f
3d 0d 4d 6e 0e 5e 1f 0f 0f
0g 9g 0g 0h 0h 0h 0i 5i 0i
5g 0g 1g 2h 9h 3h 4i 0i 8i
4g 0g 0g 5h 0h 8h 9i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_fence():
    puzzle_string = f"""
        hidden_quad_fence.sudoku
        9
6a 1a 7a 0b 8b 0b 5c 0c 0c
9a 8a 4a 5b 0b 6b 0c 0c 0c
5a 2a 3a 1b 9b 7b 6c 8c 4c
0d 0d 0d 0e 0e 0e 4f 5f 0f
1d 0d 6d 0e 0e 0e 2f 0f 8f
0d 4d 0d 0e 0e 0e 0f 0f 0f
2g 7g 0g 3h 0h 1h 8i 4i 0i
4g 0g 0g 9h 0h 8h 0i 2i 3i
0g 0g 0g 0h 4h 2h 0i 0i 5i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_col():
    puzzle_string = f"""
        hidden_triple_col.sudoku
        9
3a _a 5a 0b 0b 0b 0c 0c 0c
6a 1a 2a 8b 0b 4b 9c 3c 0c
_a 7a 8a 0b 3b 1b 6c 0c 0c
8d 2d 0d 0e 0e 9e 0f 0f 6f
1d 6d 0d 0e 0e 0e 0f 7f 0f
7d 5d 0d 4e 0e 0e 0f 0f 2f
0g 3g 7g 6h 0h 8h 0i 5i 0i
0g 8g 1g 3h 0h 2h 7i 6i 0i
0g 0g 6g 0h 0h 0h 8i 0i 3i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_fence():
    puzzle_string = f"""
        hidden_triple_fence.sudoku
        9
_a _a 1a 0b 7b 6b 0c 0c 0c
_a 9a _a 0b 3b 1b 0c 4c 0c
8a _a 3a 4b 5b 9b 0c 0c 0c
3d 1d 8d 7e 9e 4e 0f 0f 0f
2d 5d 6d 3e 1e 8e 4f 7f 9f
0d 0d 0d 5e 6e 2e 0f 0f 8f
0g 0g 0g 0h 2h 3h 0i 0i 5i
0g 3g 0g 0h 8h 7h 0i 2i 4i
0g 0g 2g 9h 4h 5h 7i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_row():
    puzzle_string = f"""
        hidden_quad_row.sudoku
        9
_a _a _a 0b 0b 0b 0c 0c 0c
1a 6a _a 0b 9b 2b 0c 8c 3c
5a 9a _a 0b 6b 0b 0c 0c 7c
0d 3d 0d 0e 2e 1e 0f 0f 0f
0d 0d 0d 0e 0e 0e 0f 0f 0f
0d 0d 0d 4e 5e 0e 0f 2f 0f
7g 0g 0g 0h 3h 0h 0i 6i 4i
8g 4g 0g 6h 1h 5h 0i 7i 9i
0g 0g 0g 0h 0h 0h 0i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_col():
    puzzle_string = f"""
        hidden_quad_col.sudoku
        9
7a 9a 6a 0b 0b 2b 8c 4c 3c
8a 1a 3a 0b 0b 9b 5c 2c 6c
5a 4a 2a 6b 0b 0b 9c 1c 7c
9d 8d 4d 0e 0e 0e 7f 6f 1f
3d 6d 1d 0e 0e 0e 4f 5f 2f
2d 7d 5d 0e 0e 0e 3f 9f 8f
4g 3g 8g 0h 0h 1h 6i 7i 5i
1g 5g 9g 8h 0h 0h 2i 3i 4i
6g 2g 7g 3h 0h 0h 1i 8i 9i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_row():
    puzzle_string = f"""
        x_wing_row.sudoku
        9
_a 7a 9a 1b 0b 8b 2c 4c 0c
4a 5a _a 9b 2b 0b 0c 8c 0c
8a _a 2a 4b 0b 0b 0c 0c 0c
2d 4d 5d 3e 7e 1e 9f 6f 8f
7d 3d 6d 8e 4e 9e 1f 5f 2f
1d 9d 8d 5e 6e 2e 4f 3f 7f
9g 2g 4g 0h 8h 5h 0i 1i 3i
5g 0g 0g 0h 9h 3h 8i 2i 4i
0g 8g 0g 2h 1h 4h 5i 0i 0i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_col():
    puzzle_string = f"""
        x_wing_col.sudoku
        9
_a 9a 6a 0b 0b 5b 4c 2c 7c
7a _a 4a 2b 0b 6b 5c 1c 9c
2a 1a 5a 7b 4b 9b 6c 8c 3c
9d 4d 7d 5e 6e 1e 8f 3f 2f
5d 0d 0d 4e 0e 3e 0f 7f 6f
0d 6d 3d 0e 7e 2e 0f 5f 4f
0g 0g 0g 0h 5h 4h 7i 6i 8i
4g 5g 8g 6h 2h 7h 3i 9i 1i
6g 7g 0g 3h 0h 8h 2i 4i 5i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_row():
    puzzle_string = f"""
        w_wing_row.sudoku
        9
3a 1a 5a 4b 9b 8b 2c 6c 7c
8a _a _a 0b 0b 0b 4c 3c 1c
_a 7a _a 3b 1b 2b 9c 8c 5c
0d 8d 7d 2e 0e 3e 0f 1f 9f
9d 3d 0d 0e 8e 0e 0f 2f 0f
5d 0d 0d 0e 0e 9e 8f 0f 3f
7g 6g 0g 9h 2h 1h 3i 5i 0i
1g 5g 3g 8h 0h 0h 0i 9i 2i
2g 0g 0g 0h 3h 5h 1i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_col():
    puzzle_string = f"""
        w_wing_col.sudoku
        9
_a 4a 5a 0b 6b 9b 7c 3c 2c
_a 3a _a 0b 5b 0b 4c 8c 9c
_a _a 2a 3b 4b 0b 5c 1c 6c
4d 0d 0d 0e 7e 1e 3f 0f 5f
5d 2d 0d 6e 3e 4e 9f 7f 0f
0d 0d 3d 5e 9e 0e 0f 0f 4f
3g 6g 0g 0h 8h 5h 2i 4i 0i
0g 0g 4g 0h 2h 6h 0i 5i 3i
2g 5g 0g 4h 1h 3h 6i 9i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_rows():
    puzzle_string = f"""
        xyz_wing_rows.sudoku
        9
9a 6a 1a 3b 5b 8b 2c 4c 7c
3a 7a 2a 0b 4b 1b 5c 0c 0c
4a 8a 5a 0b 7b 2b 0c 0c 0c
1d 3d 7d 2e 8e 5e 0f 0f 4f
2d 9d 8d 7e 6e 4e 1f 5f 3f
5d 4d 6d 1e 0e 0e 8f 7f 2f
0g 5g 9g 4h 0h 6h 0i 2i 0i
0g 1g 4g 5h 2h 0h 0i 0i 6i
6g 2g 3g 8h 0h 7h 4i 0i 5i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_cols():
    puzzle_string = f"""
        xyz_wing_cols.sudoku
        9
1a 8a 2a 0b 0b 0b 9c 0c 7c
5a 9a _a 7b 8b 0b 2c 1c 3c
7a _a _a 9b 2b 1b 0c 5c 0c
8d 2d 1d 3e 4e 7e 0f 0f 0f
3d 6d 5d 1e 9e 8e 7f 0f 0f
9d 0d 0d 5e 6e 2e 3f 8f 1f
2g 1g 0g 0h 0h 0h 0i 0i 0i
4g 5g 8g 2h 7h 9h 1i 3i 6i
6g 0g 9g 8h 1h 0h 4i 0i 0i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_center_col():
    puzzle_string = f"""   
        w_wing_center_col.sudoku
        9
9a 8a 1a 0b 0b 5b 2c 3c 7c
5a 7a 3a 8b 1b 2b 4c 9c 6c
2a 4a 6a 0b 0b 9b 1c 8c 5c
6d 5d 7d 9e 2e 8e 3f 1f 4f
8d 3d 4d 1e 0e 0e 5f 2f 9f
1d 2d 9d 0e 5e 0e 7f 6f 8f
0g 6g 5g 2h 9h 0h 8i 4i 1i
0g 1g 2g 0h 8h 0h 9i 5i 3i
0g 9g 8g 5h 0h 1h 6i 7i 2i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_left_col():
    puzzle_string = f"""   
        w_wing_left_col.sudoku
        9
2a _a 6a 3b 1b 0b 5c 7c 4c
_a _a 7a 0b 2b 4b 6c 1c 9c
4a _a _a 0b 6b 0b 2c 3c 8c
0d 2d 0d 9e 5e 0e 4f 6f 0f
7d 6d 0d 2e 4e 1e 3f 0f 5f
0d 0d 4d 0e 3e 6e 0f 2f 0f
0g 0g 2g 1h 7h 0h 0i 4i 6i
1g 4g 0g 6h 8h 0h 7i 0i 2i
6g 7g 0g 4h 9h 2h 1i 0i 3i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_001_4x4():
    puzzle_string = f"""
    001_4x4.sudoku
    4
    1234a 1234a 1234c __3_c
    1234a 1___a 1234c ___4c
    ___4b _2__b __3_d 1___d
    1___b __3_b ___4d _2__d
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_bug_0():
    puzzle_string = f"""
    bug_0.sudoku
    9
    _a _a _a 9b 0b 8b 2c 0c 0c
    _a _a _a 0b 1b 0b 0c 7c 0c
    6a _a 2a 0b 0b 0b 4c 0c 0c
    0d 2d 0d 0e 0e 9e 8f 0f 0f
    0d 0d 1d 4e 0e 5e 3f 0f 0f
    0d 0d 6d 8e 0e 0e 0f 1f 0f
    0g 0g 9g 0h 0h 0h 1i 0i 8i
    0g 4g 0g 0h 8h 0h 0i 0i 0i
    0g 0g 3g 5h 0h 7h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_hidden_pair_0():
    puzzle_string = f"""
    hidden_pair_0.sudoku
    9
    6a 5a 1a 8b 9b 7b 4c 3c 2c
    9a _a 2a 0b 1b 3b 7c 0c 0c
    3a 7a _a 0b 2b 6b 1c 0c 9c
    7d 0d 5d 3e 4e 2e 9f 0f 1f
    1d 3d 0d 7e 6e 9e 0f 0f 0f
    2d 0d 9d 1e 8e 5e 3f 7f 0f
    5g 9g 3g 6h 7h 1h 0i 0i 0i
    4g 2g 7g 9h 5h 8h 6i 1i 3i
    8g 1g 6g 2h 3h 4h 5i 9i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_hidden_single_0():
    puzzle_string = f"""
    hidden_single_0.sudoku
    9
    7a 4a 1a 0b 2b 0b 5c 3c 8c
    3a 6a 8a 0b 0b 1b 4c 9c 2c
    5a 9a 2a 4b 3b 8b 1c 6c 7c
    8d 7d 5d 0e 0e 3e 6f 2f 4f
    2d 1d 9d 0e 0e 4e 8f 5f 3f
    6d 3d 4d 2e 8e 5e 9f 7f 1f
    9g 8g 6g 3h 4h 2h 7i 1i 5i
    1g 5g 3g 8h 0h 0h 2i 4i 9i
    4g 2g 7g 0h 0h 0h 3i 8i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_hidden_single_1():
    puzzle_string = f"""
    hidden_single_1.sudoku
    9
    _a 4a _a 0b 0b 3b 0c 2c 6c
    1a _a _a 0b 0b 0b 0c 0c 0c
    _a 2a _a 0b 6b 7b 5c 0c 4c
    0d 0d 6d 0e 0e 1e 0f 0f 5f
    4d 1d 0d 0e 0e 0e 0f 7f 9f
    5d 0d 0d 7e 0e 0e 8f 0f 0f
    2g 0g 1g 3h 7h 0h 0i 5i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 7i
    8g 7g 0g 4h 0h 0h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_hidden_single_2():
    puzzle_string = f"""
    hidden_single_2.sudoku
    9
    2a _a 7a 0b 0b 0b 8c 9c 0c
    _a 9a _a 7b 4b 5b 3c 6c 2c
    _a _a 3a 9b 2b 8b 7c 0c 0c
    9d 0d 0d 3e 0e 4e 5f 0f 0f
    4d 0d 0d 5e 0e 2e 9f 0f 3f
    7d 3d 5d 0e 0e 9e 4f 2f 0f
    0g 0g 0g 4h 0h 0h 6i 0i 9i
    3g 7g 9g 2h 0h 6h 1i 4i 0i
    6g 1g 4g 0h 9h 0h 2i 0i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_locked_candidates_claiming_0():
    puzzle_string = f"""
    locked_candidates_claiming_0.sudoku
    9
    _a _a _a 9b 0b 0b 0c 0c 4c
    4a _a 6a 0b 0b 8b 7c 0c 3c
    _a _a _a 0b 0b 0b 0c 2c 0c
    0d 8d 9d 1e 0e 0e 0f 0f 0f
    6d 0d 7d 0e 0e 0e 9f 0f 5f
    0d 0d 0d 0e 0e 9e 8f 3f 0f
    0g 6g 0g 0h 0h 0h 0i 0i 0i
    3g 0g 2g 5h 0h 0h 1i 0i 7i
    1g 0g 0g 0h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()])


def test_sudoku_locked_candidates_claiming_1():
    puzzle_string = f"""
    locked_candidates_claiming_1.sudoku
    9
    _a _a _a 0b 0b 0b 3c 0c 4c
    8a 5a _a 6b 0b 0b 0c 0c 0c
    _a _a _a 1b 2b 0b 0c 6c 9c
    0d 0d 8d 0e 0e 0e 2f 7f 0f
    9d 0d 0d 0e 0e 0e 0f 0f 6f
    0d 6d 2d 0e 0e 0e 4f 0f 0f
    1g 9g 0g 0h 7h 3h 0i 0i 0i
    0g 0g 0g 0h 0h 2h 0i 1i 3i
    3g 0g 5g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()])


def test_sudoku_locked_candidates_claiming_2():
    puzzle_string = f"""
    locked_candidates_claiming_2.sudoku
    9
    _a 8a _a 0b 0b 2b 0c 0c 0c
    2a _a _a 0b 6b 0b 8c 3c 0c
    _a _a _a 7b 0b 3b 0c 0c 0c
    4d 0d 0d 0e 0e 7e 6f 1f 0f
    0d 0d 8d 0e 0e 0e 9f 0f 0f
    0d 1d 6d 4e 0e 0e 0f 0f 2f
    0g 0g 0g 6h 0h 4h 0i 0i 0i
    0g 4g 7g 0h 9h 0h 0i 0i 1i
    0g 0g 0g 5h 0h 0h 0i 2i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()])


def test_sudoku_locked_candidates_pointing_0():
    puzzle_string = f"""
    locked_candidates_pointing_0.sudoku
    9
    _a 3a _a 0b 0b 0b 0c 6c 0c
    _a _a _a 0b 0b 3b 9c 0c 0c
    _a 4a 2a 6b 0b 0b 0c 8c 0c
    0d 0d 0d 0e 3e 2e 8f 0f 0f
    0d 7d 0d 4e 0e 6e 0f 5f 0f
    0d 0d 5d 1e 7e 0e 0f 0f 0f
    0g 9g 0g 0h 0h 8h 2i 4i 0i
    0g 0g 6g 2h 0h 0h 0i 0i 0i
    0g 8g 0g 0h 0h 0h 0i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()])


def test_sudoku_naked_pair_0():
    puzzle_string = f"""
    naked_pair_0.sudoku
    9
    _a 1a 9a 3b 0b 8b 0c 0c 0c
    _a 2a 6a 9b 0b 7b 3c 8c 0c
    8a 3a 7a 0b 0b 5b 0c 0c 0c
    6d 7d 2d 5e 0e 9e 8f 4f 0f
    0d 5d 8d 0e 0e 6e 0f 0f 0f
    0d 4d 1d 8e 0e 2e 5f 0f 6f
    1g 8g 3g 6h 9h 4h 7i 5i 2i
    7g 9g 4g 2h 5h 3h 1i 6i 8i
    2g 6g 5g 7h 8h 1h 4i 3i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


def test_sudoku_naked_pair_1():
    puzzle_string = f"""
    naked_pair_1.sudoku
    9
    6a 1a _a 8b 5b 3b 0c 0c 9c
    9a _a 8a 0b 4b 0b 6c 3c 5c
    5a _a _a 9b 0b 6b 0c 1c 8c
    3d 8d 9d 0e 0e 4e 1f 0f 6f
    2d 6d 1d 0e 3e 8e 0f 9f 4f
    7d 4d 5d 6e 0e 0e 3f 8f 2f
    8g 5g 0g 4h 0h 2h 9i 6i 0i
    4g 0g 0g 0h 0h 0h 0i 0i 0i
    1g 0g 0g 3h 0h 5h 0i 0i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


def test_sudoku_naked_pair_2():
    puzzle_string = f"""
    naked_pair_2.sudoku
    9
    _a _a 1a 2b 0b 9b 0c 7c 0c
    6a _a _a 4b 5b 7b 8c 3c 1c
    _a _a 7a 8b 1b 0b 9c 2c 0c
    2d 0d 5d 7e 0e 0e 1f 0f 8f
    0d 0d 0d 0e 2e 0e 0f 5f 3f
    3d 0d 4d 0e 8e 5e 7f 0f 2f
    0g 0g 3g 5h 7h 8h 0i 0i 9i
    9g 5g 8g 6h 4h 2h 3i 1i 7i
    0g 0g 0g 3h 9h 1h 0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_0():
    puzzle_string = f"""
    naked_triple_0.sudoku
    9
    _a 4a _a 0b 0b 0b 3c 0c 0c
    2a _a _a 7b 0b 0b 0c 6c 0c
    _a _a 9a 8b 0b 0b 0c 0c 0c
    0d 0d 8d 0e 0e 0e 0f 9f 6f
    9d 0d 0d 2e 0e 4e 0f 0f 1f
    7d 2d 0d 0e 0e 0e 5f 0f 0f
    0g 0g 0g 0h 0h 5h 8i 0i 0i
    0g 1g 0g 0h 0h 7h 0i 0i 2i
    0g 0g 3g 0h 0h 0h 0i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_1():
    puzzle_string = f"""
    naked_triple_1.sudoku
    9
    _a _a _a 9b 0b 0b 0c 0c 0c
    _a _a _a 0b 3b 6b 0c 4c 9c
    3a 5a _a 0b 0b 1b 0c 0c 0c
    0d 0d 0d 2e 0e 0e 8f 0f 6f
    5d 6d 0d 0e 0e 0e 0f 7f 4f
    9d 0d 3d 0e 0e 4e 0f 0f 0f
    0g 0g 0g 4h 0h 0h 0i 8i 1i
    2g 9g 0g 6h 1h 0h 0i 0i 0i
    0g 0g 0g 0h 0h 7h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_2():
    puzzle_string = f"""
    naked_triple_2.sudoku
    9
    _a _a _a 0b 2b 0b 0c 0c 0c
    _a 3a 5a 6b 0b 0b 2c 0c 0c
    4a _a _a 5b 0b 0b 0c 0c 8c
    0d 0d 8d 0e 9e 7e 0f 0f 0f
    0d 0d 2d 8e 0e 6e 1f 0f 0f
    0d 0d 0d 4e 1e 0e 5f 0f 0f
    3g 0g 0g 0h 0h 5h 0i 0i 7i
    0g 0g 4g 0h 0h 8h 9i 6i 0i
    0g 0g 0g 0h 4h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_3():
    puzzle_string = f"""
    naked_triple_3.sudoku
    9
    6a _a _a 0b 0b 0b 0c 0c 7c
    _a _a 5a 0b 6b 0b 0c 9c 0c
    8a _a _a 4b 0b 0b 2c 0c 0c
    0d 3d 0d 0e 0e 0e 7f 0f 0f
    0d 1d 0d 9e 0e 7e 0f 3f 0f
    0d 0d 8d 0e 0e 0e 0f 1f 0f
    0g 0g 7g 0h 0h 5h 0i 0i 8i
    0g 2g 0g 0h 8h 0h 1i 0i 0i
    4g 0g 0g 0h 0h 0h 0i 0i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_4():
    puzzle_string = f"""
    naked_triple_4.sudoku
    9
    _a _a _a 0b 0b 0b 6c 9c 8c
    _a _a _a 0b 2b 6b 0c 0c 0c
    1a _a _a 9b 0b 0b 0c 0c 5c
    0d 0d 7d 0e 4e 0e 0f 3f 2f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    3d 6d 0d 0e 5e 0e 8f 0f 0f
    5g 0g 0g 0h 0h 4h 0i 0i 1i
    0g 0g 0g 5h 7h 0h 0i 0i 0i
    9g 2g 8g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_5():
    puzzle_string = f"""
    naked_triple_5.sudoku
    9
    4a 7a 8a 0b 1b 0b 6c 5c 0c
    _a 3a _a 0b 0b 7b 8c 1c 0c
    _a 1a _a 0b 0b 8b 0c 0c 0c
    0d 0d 7d 5e 8e 0e 0f 3f 6f
    6d 5d 4d 7e 3e 2e 1f 9f 8f
    3d 8d 0d 0e 9e 6e 5f 0f 0f
    8g 0g 0g 0h 0h 0h 0i 6i 0i
    0g 6g 0g 8h 0h 0h 0i 4i 0i
    7g 0g 3g 0h 6h 5h 9i 8i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_6():
    puzzle_string = f"""
    naked_triple_6.sudoku
    9
    5a 8a _a 7b 3b 9b 2c 1c 0c
    9a 3a _a 1b 2b 6b 0c 0c 8c
    1a 2a _a 5b 8b 4b 0c 9c 3c
    0d 9d 5d 8e 4e 2e 0f 0f 0f
    6d 4d 8d 9e 1e 0e 0f 2f 5f
    0d 1d 2d 6e 0e 0e 4f 8f 9f
    8g 7g 9g 4h 0h 1h 0i 3i 2i
    4g 6g 3g 2h 0h 0h 0i 0i 0i
    2g 5g 1g 3h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_7():
    puzzle_string = f"""
    naked_triple_7.sudoku
    9
    1a 6a _a 0b 7b 5b 4c 0c 0c
    _a 5a 4a 2b 1b 0b 0c 0c 7c
    2a 3a 7a 9b 4b 6b 8c 1c 5c
    5d 9d 3d 7e 8e 2e 1f 4f 6f
    7d 8d 2d 1e 6e 4e 5f 3f 9f
    4d 1d 6d 0e 0e 0e 2f 7f 8f
    0g 2g 5g 4h 3h 7h 0i 0i 1i
    0g 4g 0g 0h 0h 1h 7i 0i 0i
    0g 7g 1g 6h 2h 0h 0i 5i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_8():
    puzzle_string = f"""
    naked_triple_8.sudoku
    9
    _a 4a _a 0b 0b 0b 9c 3c 0c
    3a 7a _a 2b 0b 8b 6c 4c 1c
    _a 6a _a 0b 4b 0b 5c 0c 7c
    5d 0d 4d 0e 1e 7e 3f 9f 0f
    6d 0d 1d 0e 0e 0e 0f 7f 5f
    9d 0d 7d 5e 0e 0e 1f 0f 4f
    4g 1g 6g 0h 2h 9h 0i 5i 3i
    7g 5g 2g 1h 0h 0h 0i 0i 9i
    8g 9g 3g 0h 0h 0h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_9():
    puzzle_string = f"""
    naked_triple_9.sudoku
    9
    _a 4a 2a 7b 0b 0b 0c 0c 0c
    _a _a 3a 9b 0b 0b 7c 0c 4c
    5a 7a _a 0b 4b 0b 0c 0c 0c
    7d 0d 5d 0e 6e 2e 4f 0f 0f
    0d 0d 0d 0e 9e 0e 0f 0f 0f
    0d 0d 0d 4e 7e 0e 2f 0f 3f
    0g 0g 0g 0h 0h 7h 0i 8i 6i
    6g 0g 1g 0h 0h 4h 5i 0i 0i
    0g 0g 7g 6h 0h 9h 3i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_row():
    puzzle_string = f"""
    naked_triple_row.sudoku
    9
    7a 8a 2a 3b 5b 4b 1c 9c 6c
    _a _a _a 2b 6b 7b 4c 5c 8c
    4a 5a 6a 8b 9b 1b 3c 2c 7c
    0d 0d 1d 5e 0e 0e 6f 0f 0f
    5d 7d 0d 6e 0e 9e 2f 0f 1f
    0d 6d 0d 0e 0e 8e 5f 0f 0f
    6g 3g 7g 4h 8h 5h 9i 1i 2i
    0g 4g 0g 0h 0h 6h 0i 3i 5i
    0g 0g 5g 9h 0h 0h 0i 6i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


def test_sudoku_unique_rectangle_type1_00():
    puzzle_string = f"""
    unique_rectangle_type1_00.sudoku
    9
    _a 6a 4a 0b 3b 7b 0c 0c 0c
    1a _a _a 0b 0b 0b 0c 0c 0c
    5a _a _a 4b 0b 0b 3c 0c 9c
    0d 0d 0d 9e 5e 0e 2f 0f 0f
    0d 9d 0d 0e 0e 0e 0f 8f 0f
    0d 0d 8d 0e 4e 1e 0f 0f 0f
    7g 0g 1g 0h 0h 2h 0i 0i 8i
    0g 0g 0g 0h 0h 0h 0i 0i 4i
    0g 0g 0g 7h 9h 0h 6i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_01():
    puzzle_string = f"""
    unique_rectangle_type1_01.sudoku
    9
    3a _a 2a 4b 0b 0b 0c 0c 7c
    _a 6a 4a 0b 7b 0b 3c 5c 0c
    _a 7a _a 0b 0b 0b 0c 2c 0c
    0d 5d 7d 0e 0e 0e 0f 6f 1f
    0d 0d 0d 6e 0e 8e 0f 0f 0f
    6d 4d 0d 0e 0e 0e 8f 9f 0f
    0g 3g 0g 0h 0h 0h 0i 4i 0i
    0g 1g 6g 0h 8h 0h 5i 3i 0i
    4g 0g 0g 0h 0h 6h 1i 0i 2i
"""
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_02():
    puzzle_string = f"""
    unique_rectangle_type1_02.sudoku
    9
    _a 3a _a 8b 0b 5b 4c 6c 0c
    _a _a _a 0b 0b 0b 0c 3c 0c
    _a _a _a 6b 4b 0b 1c 0c 2c
    6d 0d 9d 0e 0e 0e 0f 2f 0f
    0d 1d 4d 0e 0e 0e 9f 8f 0f
    0d 2d 0d 0e 0e 0e 6f 0f 1f
    1g 0g 2g 0h 5h 7h 0i 0i 0i
    0g 9g 0g 0h 0h 0h 0i 0i 0i
    0g 4g 7g 1h 0h 6h 0i 5i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_03():
    puzzle_string = f"""
    unique_rectangle_type1_03.sudoku
    9
    _a _a _a 8b 0b 0b 7c 2c 0c
    _a _a 8a 0b 4b 0b 0c 0c 0c
    _a _a 3a 1b 7b 2b 9c 0c 0c
    0d 3d 0d 0e 0e 0e 0f 0f 8f
    0d 0d 4d 0e 0e 0e 1f 0f 0f
    2d 0d 0d 0e 0e 0e 0f 7f 0f
    0g 0g 2g 6h 8h 9h 3i 0i 0i
    0g 0g 0g 0h 3h 0h 4i 0i 0i
    0g 1g 6g 0h 0h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_04():
    puzzle_string = f"""
    unique_rectangle_type1_04.sudoku
    9
    6a 2a _a _b _b 4b 5c _c _c
    8a _a _a _b _b _b _c 4c _c
    _a _a 4a 3b _b _b _c _c 8c
    2d 9d _d 1e _e _e 3f _f _f
    _d _d _d _e 8e _e _f _f _f
    _d _d 8d _e _e 9e _f 2f 6f
    4g _g _g _h _h 2h 6i _i _i
    _g 6g _g _h _h _h _i _i 1i
    _g _g 1g 5h _h _h _i 3i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_almost_locked_candidates_col():
    puzzle_string = f"""
    almost_locked_candidates_col.sudoku
    9
    _a 5a _a   2b 0b 0b   8c 7c 4c
    2a 8a 7a   5b 0b 0b   3c 1c 9c
    1a 3a 4a   8b 7b 9b   5c 2c 6c

    0d 2d 8d   0e 5e 0e   0f 6f 1f
    0d 0d 0d   7e 8e 2e   4f 0f 0f
    0d 4d 3d   0e 9e 0e   0f 8f 0f

    8g 6g 2g   9h 0h 5h   1i 0i 7i
    3g 0g 5g   0h 2h 7h   6i 0i 8i
    4g 7g 0g   0h 0h 8h   0i 5i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_almost_locked_candidates_row():
    puzzle_string = f"""
    almost_locked_candidates_row.sudoku
    9
_a 2a 9a   7b 0b 0b   0c 4c 0c
_a 7a 8a   0b 9b 0b   0c 0c 6c
_a 5a 1a   3b 0b 0b   7c 0c 9c

1d 6d 2d   5e 8e 9e   4f 7f 3f
8d 9d 7d   0e 3e 0e   0f 0f 0f
5d 3d 4d   6e 1e 7e   2f 9f 8f

2g 8g 5g   1h 7h 6h   9i 3i 4i
9g 4g 6g   8h 2h 3h   5i 1i 7i
7g 1g 3g   9h 0h 0h   0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_almost_locked_candidates_rows_center():
    puzzle_string = f"""
    almost_locked_candidates_rows_center.sudoku
    9
6a 2a _a   0b 0b 4b   9c 3c 1c
_a _a 5a   6b 0b 3b   2c 8c 4c
3a 4a _a   0b 9b 0b   6c 5c 7c

0d 1d 0d   0e 2e 0e   8f 6f 5f
8d 0d 0d   1e 6e 5e   0f 2f 0f
2d 5d 6d   0e 8e 0e   0f 1f 0f

5g 8g 0g   7h 0h 6h   0i 9i 2i
0g 3g 2g   9h 0h 8h   5i 7i 6i
7g 6g 9g   0h 0h 0h   0i 4i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_als_xz():
    puzzle_string = f"""
    als_xz.sudoku
    9
4a _a _a   0b 0b 0b   5c 0c 0c
6a _a _a   4b 5b 2b   8c 0c 0c
3a 5a _a   0b 0b 7b   4c 1c 0c

9d 0d 0d   0e 0e 6e   0f 5f 0f
0d 2d 0d   5e 3e 4e   0f 7f 0f
5d 3d 0d   7e 0e 0e   0f 8f 4f

0g 6g 3g   9h 0h 5h   0i 4i 0i
0g 0g 5g   2h 4h 0h   0i 0i 8i
0g 0g 0g   0h 0h 0h   0i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_alternating_inference_chain():
    puzzle_string = f"""
    alternating_inference_chain.sudoku
    9
_a 5a _a   0b 0b 0b   0c 3c 0c
_a 3a 2a   4b 1b 0b   5c 9c 7c
_a 1a 9a   0b 3b 5b   0c 8c 0c

0d 2d 0d   8e 0e 1e   9f 6f 0f
9d 6d 0d   0e 0e 0e   8f 1f 0f
1d 4d 8d   3e 0e 0e   7f 2f 5f

0g 9g 0g   5h 8h 7h   3i 4i 0i
5g 8g 4g   1h 2h 3h   6i 7i 9i
0g 7g 0g   0h 0h 0h   0i 5i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type1_0():
    puzzle_string = f"""
    avoidable_rectangle_type1_0.sudoku
    9
_a 6a _a   0b 0b 0b   0c 3c 9c
_a 8a _a   3b 2b 0b   0c 0c 0c
9a _a _a   5b 0b 6b   0c 0c 0c

2d 0d 0d   0e 0e 4e   6f 0f 0f
0d 0d 7d   0e 5e 0e   2f 0f 0f
0d 0d 5d   6e 0e 0e   0f 0f 8f

0g 0g 0g   4h 0h 8h   0i 0i 5i
0g 0g 0g   0h 3h 1h   0i 4i 0i
7g 1g 0g   0h 0h 0h   0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_1():
    puzzle_string = f"""
    avoidable_rectangle_type2_1.sudoku
    9
_a _a 2a   0b 0b 0b   0c 3c 0c
_a _a 6a   0b 3b 1b   0c 4c 0c
3a _a _a   0b 0b 9b   2c 7c 0c

0d 0d 7d   0e 0e 2e   0f 0f 0f
2d 0d 0d   0e 0e 0e   0f 0f 6f
0d 0d 0d   1e 0e 0e   9f 0f 0f

0g 4g 9g   5h 0h 0h   0i 0i 2i
0g 2g 0g   6h 9h 0h   7i 0i 0i
0g 1g 0g   0h 0h 0h   4i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_2():
    puzzle_string = f"""
    avoidable_rectangle_type2_2.sudoku
    9
_a _a _a   0b 0b 0b   0c 0c 1c
_a 6a _a   3b 0b 8b   0c 0c 7c
5a _a 3a   4b 0b 0b   0c 0c 2c

0d 0d 0d   0e 8e 0e   6f 7f 0f
4d 0d 0d   6e 0e 3e   0f 0f 5f
0d 5d 6d   0e 4e 0e   0f 0f 0f

9g 0g 0g   0h 0h 7h   5i 0i 8i
7g 0g 0g   2h 0h 4h   0i 3i 0i
6g 0g 0g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_3():
    puzzle_string = f"""
    avoidable_rectangle_type2_3.sudoku
    9
_a _a _a   0b 0b 0b   0c 0c 1c
_a 6a _a   3b 0b 8b   0c 0c 7c
5a _a 3a   4b 0b 0b   0c 0c 2c

0d 0d 0d   0e 8e 0e   6f 7f 0f
4d 0d 0d   6e 0e 3e   0f 0f 5f
0d 5d 6d   0e 4e 0e   0f 0f 0f

9g 0g 0g   0h 0h 7h   5i 0i 8i
7g 0g 0g   2h 0h 4h   0i 3i 0i
6g 0g 0g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_4():
    puzzle_string = f"""
    avoidable_rectangle_type2_4.sudoku
    9
_a _a 3a   0b 0b 0b   0c 7c 0c
_a _a _a   3b 0b 0b   0c 0c 4c
_a _a 5a   2b 4b 9b   6c 0c 0c

3d 0d 0d   1e 0e 0e   0f 0f 0f
6d 0d 7d   0e 0e 0e   4f 0f 3f
0d 0d 0d   0e 0e 5e   0f 0f 6f

0g 0g 8g   7h 6h 3h   2i 0i 0i
5g 0g 0g   0h 0h 4h   0i 0i 0i
0g 3g 0g   0h 0h 0h   9i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_5():
    puzzle_string = f"""
    avoidable_rectangle_type2_5.sudoku
    9
_a _a _a   9b 0b 0b   2c 0c 0c
9a _a _a   0b 0b 4b   0c 1c 7c
_a 7a _a   0b 6b 8b   5c 0c 0c

0d 4d 0d   0e 0e 0e   0f 6f 8f
0d 0d 8d   0e 0e 0e   4f 0f 0f
1d 9d 0d   0e 0e 0e   0f 3f 0f

0g 0g 1g   4h 7h 0h   0i 5i 0i
3g 6g 0g   5h 0h 0h   0i 0i 4i
0g 0g 7g   0h 0h 9h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_6():
    puzzle_string = f"""
    avoidable_rectangle_type2_6.sudoku
    9
_a _a _a   0b 0b 0b   0c 0c 7c
_a 6a _a   2b 0b 3b   0c 0c 4c
9a _a 1a   0b 0b 4b   0c 0c 8c

0d 4d 7d   0e 9e 0e   0f 0f 0f
1d 0d 0d   7e 0e 6e   0f 0f 3f
0d 0d 0d   0e 3e 0e   7f 1f 0f

2g 0g 0g   3h 0h 0h   6i 0i 1i
4g 0g 0g   6h 0h 9h   0i 7i 0i
5g 0g 0g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_north():
    puzzle_string = f"""
    avoidable_rectangle_type2_north.sudoku
    9
_a 7a 5a   4b 0b 0b   0c 2c 0c
_a 1a _a   0b 0b 0b   0c 0c 6c
4a _a 9a   0b 6b 8b   7c 0c 0c

9d 0d 0d   1e 0e 0e   0f 8f 0f
0d 0d 0d   0e 0e 0e   0f 0f 0f
0d 6d 0d   0e 0e 5e   0f 0f 1f

0g 0g 6g   9h 5h 0h   1i 0i 4i
7g 0g 0g   0h 0h 0h   0i 6i 0i
0g 9g 0g   0h 0h 4h   5i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_south():
    puzzle_string = f"""
    avoidable_rectangle_type2_south.sudoku
    9
_a _a 5a   0b 0b 0b   0c 0c 4c
_a _a 7a   3b 9b 6b   2c 0c 0c
_a _a _a   0b 0b 5b   0c 9c 0c

0d 5d 0d   0e 0e 1e   0f 0f 0f
0d 2d 4d   0e 0e 0e   9f 5f 0f
0d 0d 0d   7e 0e 0e   0f 2f 0f

0g 7g 0g   9h 0h 0h   0i 0i 0i
0g 0g 8g   5h 2h 4h   6i 0i 0i
5g 0g 0g   0h 0h 0h   3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_west():
    puzzle_string = f"""
    avoidable_rectangle_type2_west.sudoku
    9
_a 9a 4a   1b 0b 0b   0c 0c 3c
5a _a _a   0b 4b 0b   0c 0c 0c
_a _a _a   0b 0b 0b   7c 4c 2c

3d 7d 0d   4e 0e 0e   0f 0f 0f
0d 5d 0d   0e 0e 0e   0f 3f 0f
0d 0d 0d   0e 0e 7e   0f 9f 8f

1g 2g 5g   0h 0h 0h   0i 0i 0i
0g 0g 0g   0h 9h 0h   0i 0i 4i
4g 0g 0g   0h 0h 3h   2i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_0():
    puzzle_string = f"""
    finned_jellyfish_0.sudoku
    9

4a _a _a   2b 0b 9b   0c 7c 8c
_a 9a _a   8b 0b 0b   4c 0c 0c
8a _a _a   4b 6b 0b   1c 9c 0c

0d 0d 0d   3e 0e 4e   0f 8f 0f
0d 0d 9d   0e 8e 0e   2f 0f 0f
0d 4d 8d   9e 0e 5e   0f 0f 0f

0g 7g 4g   0h 9h 0h   0i 0i 5i
5g 8g 1g   0h 0h 2h   0i 0i 0i
9g 3g 0g   5h 4h 0h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_1():
    puzzle_string = f"""
    finned_jellyfish_1.sudoku
    9

_a _a _a   1b 0b 0b   9c 0c 0c
_a 9a _a   0b 0b 8b   0c 0c 7c
_a 1a _a   0b 4b 0b   5c 0c 8c

9d 0d 0d   8e 0e 6e   0f 0f 0f
0d 0d 8d   0e 1e 0e   2f 0f 0f
0d 0d 0d   3e 0e 9e   0f 0f 1f

7g 0g 9g   0h 8h 0h   0i 6i 0i
3g 0g 0g   6h 0h 0h   0i 7i 0i
0g 0g 5g   0h 0h 2h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_2():
    puzzle_string = f"""
    finned_jellyfish_2.sudoku
    9

_a _a _a   4b 0b 3b   8c 0c 5c
8a 5a _a   0b 0b 0b   6c 3c 4c
_a 4a 3a   6b 5b 8b   7c 0c 9c

3d 0d 7d   8e 0e 4e   2f 5f 0f
5d 0d 0d   0e 3e 0e   0f 0f 0f
0d 0d 4d   5e 0e 6e   3f 0f 8f

4g 0g 5g   3h 0h 0h   0i 0i 2i
0g 3g 2g   0h 0h 5h   0i 8i 0i
6g 0g 0g   7h 0h 2h   5i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_3():
    puzzle_string = f"""
    finned_jellyfish_3.sudoku
    9

_a 6a 5a   3b 2b 0b   9c 7c 8c
9a 2a _a   7b 0b 8b   0c 0c 0c
8a 3a 7a   0b 5b 0b   0c 0c 0c

0d 9d 2d   0e 0e 5e   0f 7f 8f
5d 0d 8d   2e 0e 7e   0f 9f 6f
0d 7d 6d   8e 0e 0e   1f 5f 2f

6g 0g 9g   0h 8h 3h   0i 0i 7i
2g 0g 0g   0h 7h 6h   8i 3i 9i
7g 8g 3g   0h 0h 2h   6i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_0():
    puzzle_string = f"""
    finned_swordfish_0.sudoku
    9

_a _a _a   0b 4b 0b   5c 9c 0c
_a 5a 9a   0b 0b 0b   1c 4c 2c
_a 1a _a   5b 9b 0b   0c 8c 0c

6d 2d 5d   7e 1e 8e   9f 3f 4f
0d 0d 8d   6e 5e 3e   2f 7f 1f
3d 7d 1d   4e 2e 9e   8f 6f 5f

5g 8g 0g   2h 0h 4h   0i 1i 9i
1g 0g 0g   9h 0h 5h   3i 2i 8i
0g 0g 2g   0h 8h 0h   4i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_1():
    puzzle_string = f"""
    finned_swordfish_1.sudoku
    9

2a _a _a   0b 6b 1b   9c 0c 0c
_a _a _a   3b 0b 0b   0c 0c 5c
_a 5a _a   0b 0b 9b   0c 6c 0c

0d 1d 0d   0e 7e 8e   0f 0f 0f
0d 0d 4d   0e 0e 0e   6f 0f 0f
0d 0d 0d   2e 3e 0e   0f 4f 0f

0g 6g 0g   7h 0h 0h   0i 5i 0i
9g 0g 0g   0h 0h 4h   0i 0i 0i
0g 0g 1g   6h 9h 0h   0i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_2():
    puzzle_string = f"""
    finned_swordfish_2.sudoku
    9

8a _a 5a   9b 0b 0b   0c 0c 0c
7a 4a 1a   0b 0b 8b   9c 0c 0c
_a 9a _a   0b 1b 5b   0c 7c 8c

0d 0d 0d   8e 0e 0e   6f 9f 0f
0d 8d 0d   1e 9e 2e   0f 4f 0f
0d 0d 9d   0e 0e 0e   0f 0f 0f

1g 3g 0g   5h 0h 9h   0i 2i 0i
9g 5g 8g   7h 2h 4h   1i 6i 3i
0g 0g 0g   0h 0h 1h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_3():
    puzzle_string = f"""
    finned_swordfish_3.sudoku
    9

2a _a 8a   0b 0b 0b   0c 0c 3c
1a 4a _a   0b 0b 2b   0c 0c 9c
7a _a 6a   0b 5b 0b   0c 4c 2c

0d 0d 0d   3e 0e 0e   0f 0f 0f
5d 0d 2d   4e 8e 1e   9f 0f 6f
0d 0d 0d   2e 0e 5e   0f 0f 0f

3g 0g 0g   0h 2h 0h   4i 9i 5i
6g 0g 0g   9h 0h 0h   0i 8i 7i
4g 0g 9g   5h 0h 0h   6i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_00():
    puzzle_string = f"""
    finned_x_wing_00.sudoku
    9

4a 5a 6a   9b 8b 7b   3c 1c 2c
_a 9a _a   4b 3b 2b   6c 7c 5c
2a 3a 7a   0b 1b 0b   0c 9c 0c

0d 4d 0d   8e 0e 0e   0f 2f 0f
0d 6d 0d   3e 0e 4e   0f 5f 0f
0d 0d 0d   0e 0e 1e   0f 6f 0f

0g 8g 0g   0h 4h 9h   0i 3i 1i
9g 0g 4g   1h 5h 3h   0i 8i 6i
0g 1g 3g   7h 0h 8h   0i 4i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_04():
    puzzle_string = f"""
    finned_x_wing_04.sudoku
    9

_a _a 8a   0b 0b 9b   3c 5c 2c
5a _a 3a   0b 2b 8b   0c 1c 0c
_a 4a _a   3b 5b 0b   8c 7c 0c

0d 2d 0d   0e 0e 5e   0f 3f 8f
6d 8d 0d   2e 9e 3e   0f 4f 0f
3d 0d 0d   8e 0e 0e   2f 6f 0f

8g 5g 6g   0h 3h 2h   0i 9i 0i
0g 1g 0g   9h 0h 0h   5i 8i 3i
4g 3g 9g   5h 8h 0h   6i 2i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_05():
    puzzle_string = f"""
    finned_x_wing_05.sudoku
    9

_a _a _a   5b 9b 1b   3c 4c 8c
_a _a _a   7b 4b 2b   0c 0c 6c
4a _a 5a   8b 6b 3b   7c 2c 0c

1d 0d 0d   9e 0e 8e   6f 0f 5f
0d 0d 0d   1e 0e 5e   4f 8f 0f
5d 0d 8d   6e 0e 4e   0f 0f 2f

0g 0g 2g   4h 0h 6h   0i 0i 0i
6g 0g 0g   3h 0h 9h   2i 0i 7i
9g 5g 3g   2h 1h 7h   8i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_06():
    puzzle_string = f"""
    finned_x_wing_06.sudoku
    9

_a 1a _a   3b 0b 7b   0c 4c 9c
_a _a _a   0b 0b 0b   0c 0c 0c
_a _a 8a   5b 0b 0b   3c 6c 0c

0d 0d 7d   0e 0e 3e   0f 0f 4f
4d 0d 6d   0e 0e 0e   1f 0f 3f
1d 0d 0d   2e 0e 0e   7f 0f 0f

0g 5g 1g   0h 0h 2h   4i 0i 0i
0g 0g 0g   0h 0h 0h   0i 0i 0i
6g 2g 0g   9h 0h 1h   0i 3i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_07():
    puzzle_string = f"""
    finned_x_wing_07.sudoku
    9

1a 4a _a   0b 0b 0b   9c 0c 8c
_a 2a _a   0b 9b 4b   1c 0c 6c
_a _a 6a   5b 1b 0b   2c 3c 4c

0d 0d 4d   0e 0e 0e   0f 8f 2f
0d 5d 2d   0e 0e 0e   4f 0f 1f
8d 1d 0d   0e 0e 0e   5f 0f 0f

2g 3g 7g   0h 0h 0h   8i 1i 5i
5g 0g 0g   0h 0h 0h   0i 4i 0i
4g 0g 1g   0h 0h 0h   0i 2i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_08():
    puzzle_string = f"""
    finned_x_wing_08.sudoku
    9

_a _a _a   9b 0b 7b   0c 3c 0c
_a _a _a   0b 2b 0b   0c 8c 7c
_a _a 1a   0b 0b 3b   0c 6c 0c

0d 0d 0d   0e 0e 0e   3f 9f 4f
2d 0d 0d   0e 0e 0e   0f 0f 8f
9d 4d 3d   0e 0e 0e   0f 0f 0f

0g 8g 0g   6h 0h 0h   1i 0i 0i
5g 3g 0g   0h 9h 0h   0i 0i 0i
0g 2g 0g   8h 0h 5h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_09():
    puzzle_string = f"""
    finned_x_wing_09.sudoku
    9

3a 7a 8a   5b 6b 2b   1c 9c 4c
_a 2a 4a   0b 0b 0b   0c 0c 5c
5a _a 9a   4b 0b 8b   0c 0c 3c

2d 0d 0d   0e 4e 0e   5f 0f 7f
0d 9d 7d   2e 0e 5e   3f 4f 6f
4d 0d 5d   0e 0e 0e   0f 0f 9f

7g 4g 0g   0h 2h 1h   9i 5i 8i
9g 0g 2g   0h 5h 4h   6i 7i 1i
0g 5g 1g   0h 9h 7h   4i 3i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_10():
    puzzle_string = f"""
    finned_x_wing_10.sudoku
    9

3a _a _a   0b 2b 6b   0c 5c 0c
_a _a 6a   8b 5b 0b   3c 1c 9c
_a 5a _a   0b 1b 0b   2c 6c 0c

5d 0d 2d   6e 0e 0e   7f 3f 0f
4d 8d 0d   2e 3e 0e   5f 9f 6f
0d 0d 3d   0e 0e 5e   1f 0f 2f

1g 7g 9g   0h 6h 0h   0i 2i 5i
8g 3g 4g   5h 9h 2h   6i 7i 1i
0g 0g 5g   1h 7h 0h   9i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_11():
    puzzle_string = f"""
    finned_x_wing_11.sudoku
    9

_a 2a _a   0b 0b 0b   0c 0c 9c
_a _a 9a   0b 0b 1b   0c 6c 3c
7a 3a _a   0b 0b 0b   4c 0c 0c

0d 0d 3d   7e 1e 0e   0f 0f 2f
0d 0d 0d   0e 8e 0e   0f 0f 0f
8d 0d 0d   0e 3e 2e   1f 0f 0f

0g 0g 7g   0h 0h 0h   0i 2i 4i
2g 6g 0g   4h 0h 0h   8i 0i 0i
1g 0g 0g   0h 0h 0h   0i 3i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_12():
    puzzle_string = f"""
    finned_x_wing_12.sudoku
    9

_a 7a 2a   0b 0b 0b   0c 0c 0c
3a _a _a   6b 9b 0b   4c 5c 0c
6a _a _a   2b 0b 0b   0c 0c 0c

0d 0d 6d   0e 0e 0e   0f 0f 5f
0d 5d 1d   7e 0e 6e   3f 2f 0f
7d 0d 0d   0e 0e 0e   6f 0f 0f

0g 0g 0g   0h 0h 4h   0i 0i 8i
0g 6g 4g   0h 5h 1h   0i 0i 7i
0g 0g 0g   0h 0h 0h   9i 1i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_13():
    puzzle_string = f"""
    finned_x_wing_13.sudoku
    9

1a _a _a   3b 8b 0b   0c 0c 0c
_a 7a _a   0b 0b 0b   0c 0c 1c
_a 2a _a   1b 0b 4b   3c 0c 7c

0d 0d 0d   0e 0e 1e   0f 0f 5f
8d 0d 0d   5e 0e 3e   0f 0f 6f
6d 0d 0d   7e 0e 0e   0f 0f 0f

7g 0g 3g   4h 0h 2h   0i 5i 0i
2g 0g 0g   0h 0h 0h   0i 9i 0i
0g 0g 0g   0h 3h 5h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_14():
    puzzle_string = f"""
    finned_x_wing_14.sudoku
    9

2a _a _a   7b 4b 1b   5c 3c 6c
_a _a _a   5b 2b 3b   0c 0c 7c
3a 5a 7a   6b 9b 8b   4c 2c 1c

4d 2d 0d   0e 7e 9e   0f 0f 5f
0d 0d 5d   0e 6e 2e   7f 4f 0f
7d 0d 0d   8e 5e 4e   0f 0f 2f

9g 7g 2g   4h 8h 5h   6i 1i 3i
5g 0g 0g   9h 1h 6h   2i 7i 0i
0g 1g 0g   2h 3h 7h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_15():
    puzzle_string = f"""
    finned_x_wing_15.sudoku
    9

6a 8a 9a   5b 0b 2b   0c 4c 1c
7a 2a 1a   0b 0b 0b   5c 0c 8c
4a 3a 5a   0b 0b 0b   2c 0c 9c

2d 5d 3d   0e 0e 1e   6f 0f 4f
9d 0d 6d   0e 0e 0e   0f 0f 2f
8d 0d 7d   2e 0e 0e   9f 0f 5f

5g 9g 4g   0h 0h 0h   1i 2i 7i
3g 7g 2g   0h 0h 0h   8i 9i 6i
1g 6g 8g   7h 2h 9h   4i 5i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_16():
    puzzle_string = f"""
    finned_x_wing_16.sudoku
    9

7a 4a 9a   8b 1b 3b   2c 5c 6c
6a 5a 3a   9b 7b 2b   4c 1c 8c
_a 1a _a   0b 0b 0b   9c 3c 7c

3d 0d 7d   0e 0e 8e   5f 9f 0f
1d 0d 5d   0e 0e 0e   8f 7f 4f
9d 8d 4d   7e 0e 0e   0f 0f 3f

0g 3g 6g   0h 0h 0h   7i 4i 0i
4g 9g 0g   0h 0h 7h   0i 0i 5i
5g 7g 1g   2h 0h 4h   0i 8i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_17():
    puzzle_string = f"""
    finned_x_wing_17.sudoku
    9

3a _a _a   7b 4b 8b   5c 0c 0c
_a _a 1a   5b 2b 6b   3c 0c 4c
_a _a _a   1b 3b 9b   0c 0c 8c

0d 0d 8d   3e 0e 2e   0f 0f 7f
2d 0d 0d   0e 0e 4e   0f 0f 6f
4d 0d 0d   0e 0e 5e   2f 0f 0f

1g 0g 0g   2h 8h 7h   0i 0i 5i
9g 0g 6g   4h 5h 1h   8i 0i 0i
0g 0g 5g   6h 9h 3h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_cols_1_fin():
    puzzle_string = f"""
    finned_x_wing_cols_1_fin.sudoku
    9

_a _a _a   4b 0b 6b   0c 8c 9c
_a _a 6a   0b 7b 0b   0c 2c 4c
_a _a 9a   0b 0b 5b   0c 6c 0c

1d 7d 2d   0e 0e 0e   6f 0f 0f
6d 0d 0d   7e 1e 2e   0f 0f 8f
0d 0d 0d   6e 0e 0e   2f 1f 7f

0g 5g 0g   2h 0h 0h   9i 0i 0i
3g 6g 0g   0h 8h 0h   0i 0i 2i
9g 2g 0g   3h 0h 7h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_rows_1_fin():
    puzzle_string = f"""
    finned_x_wing_rows_1_fin.sudoku
    9

6a _a _a   0b 7b 5b   0c 3c 0c
9a 8a 3a   4b 6b 0b   5c 0c 0c
5a _a 7a   0b 9b 0b   0c 0c 6c

3d 0d 1d   5e 0e 0e   7f 6f 0f
8d 5d 6d   7e 3e 0e   0f 2f 4f
0d 7d 9d   0e 0e 6e   3f 0f 0f

7g 6g 0g   0h 5h 0h   8i 9i 1i
1g 9g 5g   6h 8h 7h   2i 4i 3i
0g 3g 8g   9h 1h 0h   6i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fishy_cycle():
    puzzle_string = f"""
    fishy_cycle.sudoku
    9

3a _a 8a   5b 0b 1b   2c 9c 7c
_a _a 9a   7b 3b 0b   1c 8c 5c
5a 7a 1a   8b 2b 9b   3c 4c 6c

0d 0d 6d   0e 0e 5e   0f 0f 8f
8d 3d 0d   0e 0e 0e   0f 5f 9f
0d 0d 5d   0e 0e 8e   6f 0f 0f

9g 1g 0g   0h 5h 7h   8i 0i 3i
0g 5g 7g   0h 8h 3h   9i 0i 0i
6g 8g 3g   9h 0h 2h   5i 7i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fishy_cycle_0():
    puzzle_string = f"""
    fishy_cycle_0.sudoku
    9

_a 3a _a   0b 0b 0b   0c 8c 6c
1a _a _a   6b 0b 5b   0c 0c 0c
2a _a _a   0b 0b 1b   3c 0c 0c

7d 0d 0d   2e 0e 0e   0f 9f 0f
0d 0d 0d   5e 0e 8e   0f 0f 0f
0d 5d 0d   0e 0e 3e   0f 0f 7f

0g 0g 2g   1h 0h 0h   0i 0i 3i
0g 0g 0g   3h 0h 4h   0i 0i 8i
3g 8g 0g   0h 0h 0h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fishy_cycle_1():
    puzzle_string = f"""
    fishy_cycle_1.sudoku
    9

7a 8a 3a   9b 5b 6b   1c 4c 2c
6a _a _a   3b 2b 0b   9c 8c 7c
9a 2a _a   8b 0b 7b   6c 3c 5c

8d 0d 0d   0e 0e 9e   0f 0f 4f
0d 9d 2d   0e 0e 0e   8f 6f 0f
4d 0d 0d   0e 0e 8e   0f 9f 0f

2g 4g 9g   6h 0h 5h   3i 0i 8i
3g 0g 8g   0h 9h 2h   0i 0i 6i
0g 6g 7g   0h 8h 3h   0i 2i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_hidden_pair_1():
    puzzle_string = f"""
    hidden_pair_1.sudoku
    9

5a 4a 3a   0b 8b 0b   7c 6c 2c
2a 6a 8a   0b 7b 0b   3c 1c 9c
7a 9a 1a   0b 0b 6b   4c 8c 5c

1d 8d 2d   0e 0e 7e   0f 4f 6f
4d 5d 7d   6e 1e 0e   0f 3f 8f
9d 3d 6d   8e 0e 0e   0f 7f 1f

8g 2g 9g   7h 6h 3h   1i 5i 4i
3g 1g 5g   0h 0h 8h   6i 2i 7i
6g 7g 4g   0h 5h 0h   8i 9i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_hidden_pair_col():
    puzzle_string = f"""
    hidden_pair_col.sudoku
    9

9a 5a 4a   6b 3b 8b   7c 1c 2c
6a 7a 8a   0b 0b 0b   3c 9c 5c
1a 3a 2a   5b 0b 0b   6c 8c 4c

5d 4d 1d   0e 6e 0e   8f 2f 7f
8d 6d 7d   0e 0e 0e   1f 3f 9f
2d 9d 3d   0e 8e 0e   4f 5f 6f

3g 2g 6g   0h 0h 4h   5i 7i 8i
4g 8g 9g   0h 0h 0h   2i 6i 1i
7g 1g 5g   8h 2h 6h   9i 4i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_hidden_pair_fence():
    puzzle_string = f"""
    hidden_pair_fence.sudoku
    9

_a 9a 6a   0b 2b 0b   7c 3c 1c
8a 1a _a   0b 6b 3b   2c 0c 5c
2a 3a _a   1b 0b 0b   6c 0c 8c

0d 2d 0d   3e 9e 6e   8f 1f 7f
1d 6d 8d   5e 7e 4e   9f 2f 3f
9d 7d 3d   2e 8e 1e   4f 5f 6f

6g 5g 2g   0h 1h 0h   3i 7i 4i
7g 4g 1g   6h 3h 2h   5i 8i 9i
3g 8g 9g   0h 0h 0h   1i 6i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_hidden_pair_row():
    puzzle_string = f"""
    hidden_pair_row.sudoku
    9

1a 8a 2a   4b 6b 9b   3c 7c 5c
4a 9a 5a   7b 3b 1b   6c 2c 8c
6a 7a 3a   5b 2b 8b   4c 1c 9c

9d 4d 0d   0e 0e 2e   0f 5f 0f
0d 5d 6d   0e 1e 0e   9f 0f 2f
0d 2d 0d   9e 5e 0e   0f 0f 0f

5g 1g 9g   0h 0h 0h   2i 3i 4i
2g 3g 4g   1h 9h 5h   8i 6i 7i
8g 6g 7g   2h 4h 3h   5i 9i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_quad_5():
    puzzle_string = f"""
    hidden_quad_5.sudoku
    9

_a _a _a   2b 0b 0b   0c 0c 0c
_a _a 1a   9b 0b 4b   8c 0c 0c
_a _a 2a   0b 8b 0b   4c 3c 7c

0d 0d 0d   0e 0e 0e   0f 0f 1f
0d 2d 3d   0e 0e 0e   6f 9f 0f
4d 0d 0d   0e 0e 0e   0f 0f 3f

8g 6g 5g   3h 4h 0h   7i 0i 0i
2g 0g 9g   6h 0h 8h   3i 0i 0i
0g 0g 0g   0h 0h 2h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_quad_6():
    puzzle_string = f"""
    hidden_quad_6.sudoku
    9

4a 2a 6a   0b 0b 5b   8c 9c 3c
5a 7a 1a   3b 0b 0b   6c 4c 2c
8a 3a 9a   6b 0b 0b   5c 1c 7c

2d 1d 7d   0e 0e 0e   9f 3f 6f
6d 9d 4d   0e 0e 0e   7f 8f 5f
3d 8d 5d   0e 0e 0e   4f 2f 1f

1g 5g 3g   0h 0h 7h   2i 6i 8i
9g 6g 8g   0h 0h 1h   3i 7i 4i
7g 4g 2g   8h 0h 0h   1i 5i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_quad_7():
    puzzle_string = f"""
    hidden_quad_7.sudoku
    9

9a 3a 5a   4b 8b 1b   6c 2c 7c
8a 4a 6a   7b 5b 2b   3c 1c 9c
1a 2a 7a   6b 9b 3b   4c 8c 5c

0d 1d 0d   0e 0e 0e   7f 0f 6f
0d 0d 0d   0e 0e 0e   0f 0f 0f
4d 0d 9d   0e 0e 0e   0f 3f 0f

6g 8g 2g   9h 7h 4h   1i 5i 3i
7g 9g 1g   8h 3h 5h   2i 6i 4i
3g 5g 4g   2h 1h 6h   9i 7i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_0():
    puzzle_string = f"""
    hidden_unique_rectangle_0.sudoku
    9

_a _a _a   0b 0b 9b   3c 0c 6c
_a _a _a   0b 8b 0b   4c 1c 0c
_a 6a _a   0b 0b 0b   0c 0c 2c

0d 4d 0d   5e 0e 0e   6f 0f 0f
1d 0d 2d   0e 0e 0e   5f 0f 9f
0d 0d 5d   0e 0e 8e   0f 2f 0f

9g 0g 0g   0h 0h 0h   0i 3i 0i
0g 7g 8g   0h 3h 0h   0i 0i 0i
5g 0g 4g   9h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_1():
    puzzle_string = f"""
    hidden_unique_rectangle_1.sudoku
    9

6a 4a _a   0b 7b 3b   9c 8c 5c
_a 3a _a   0b 9b 0b   2c 6c 7c
_a 7a 9a   0b 0b 6b   4c 1c 3c

9d 2d 7d   6e 0e 0e   3f 5f 1f
3d 5d 8d   0e 1e 0e   6f 7f 4f
4d 1d 6d   7e 3e 5e   8f 0f 0f

7g 6g 3g   0h 0h 0h   1i 0i 8i
0g 8g 4g   0h 6h 0h   0i 3i 0i
1g 9g 0g   3h 0h 0h   0i 4i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_2():
    puzzle_string = f"""
    hidden_unique_rectangle_2.sudoku
    9

_a _a _a   0b 0b 0b   9c 0c 0c
_a _a 1a   6b 0b 2b   7c 0c 0c
_a 3a _a   9b 5b 0b   0c 0c 4c

0d 0d 2d   3e 0e 0e   0f 0f 6f
0d 7d 0d   0e 0e 0e   0f 8f 0f
6d 0d 0d   0e 0e 8e   5f 0f 0f

1g 0g 0g   0h 2h 9h   0i 7i 0i
0g 0g 9g   1h 0h 4h   8i 0i 0i
0g 0g 4g   0h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_3():
    puzzle_string = f"""
    hidden_unique_rectangle_3.sudoku
    9

_a _a 3a   1b 0b 9b   5c 6c 8c
_a _a _a   0b 6b 8b   2c 0c 3c
6a 8a _a   3b 2b 5b   0c 0c 0c

0d 0d 0d   0e 0e 6e   9f 0f 2f
0d 5d 0d   2e 0e 0e   8f 3f 6f
0d 6d 2d   8e 0e 3e   0f 0f 0f

0g 0g 0g   9h 0h 1h   6i 2i 4i
0g 0g 1g   6h 0h 0h   3i 0i 0i
4g 9g 6g   5h 3h 2h   1i 8i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_4():
    puzzle_string = f"""
    hidden_unique_rectangle_4.sudoku
    9

_a 2a _a   7b 0b 0b   4c 0c 0c
_a _a _a   0b 6b 0b   0c 9c 5c
_a _a _a   0b 1b 5b   8c 0c 7c

0d 0d 0d   5e 0e 0e   0f 0f 9f
0d 0d 8d   0e 0e 0e   3f 0f 0f
9d 0d 0d   0e 0e 8e   0f 0f 0f

3g 0g 7g   2h 5h 0h   0i 0i 0i
2g 1g 0g   0h 9h 0h   0i 0i 0i
0g 0g 6g   0h 0h 1h   0i 3i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_5():
    puzzle_string = f"""
    hidden_unique_rectangle_5.sudoku
    9

6a _a 2a   9b 5b 4b   3c 0c 0c
4a 3a 8a   6b 1b 7b   5c 9c 2c
9a 5a _a   3b 8b 2b   6c 4c 0c

8d 0d 0d   4e 9e 3e   2f 0f 0f
0d 9d 4d   5e 2e 6e   8f 7f 0f
5d 2d 0d   8e 7e 1e   4f 0f 9f

0g 8g 0g   7h 6h 5h   9i 0i 4i
7g 4g 5g   2h 3h 9h   1i 0i 0i
0g 6g 9g   1h 4h 8h   7i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_nec():
    puzzle_string = f"""
    hidden_unique_rectangle_nec.sudoku
    9

_a _a 4a   0b 0b 5b   6c 7c 8c
_a 8a _a   0b 6b 0b   4c 0c 2c
6a _a _a   0b 0b 8b   3c 0c 9c

1d 9d 3d   8e 0e 2e   7f 6f 0f
0d 0d 8d   0e 3e 0e   1f 2f 0f
0d 5d 0d   7e 0e 0e   8f 9f 3f

5g 0g 1g   6h 8h 0h   0i 3i 7i
8g 0g 0g   0h 0h 0h   0i 4i 1i
0g 3g 7g   2h 0h 0h   5i 8i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_nwc():
    puzzle_string = f"""
    hidden_unique_rectangle_nwc.sudoku
    9

3a 8a 9a   2b 1b 5b   4c 0c 0c
_a _a 4a   8b 9b 0b   1c 3c 0c
_a 1a _a   4b 0b 3b   8c 0c 0c

4d 5d 2d   0e 3e 1e   9f 8f 0f
1d 3d 0d   9e 8e 2e   5f 0f 4f
0d 0d 8d   0e 0e 4e   2f 1f 3f

0g 4g 1g   0h 2h 0h   3i 0i 0i
0g 2g 3g   1h 0h 9h   7i 4i 0i
0g 0g 0g   3h 4h 8h   6i 2i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_sec():
    puzzle_string = f"""
    hidden_unique_rectangle_sec.sudoku
    9

2a 1a _a   0b 0b 5b   0c 0c 0c
_a 7a 4a   0b 2b 0b   6c 5c 9c
_a _a _a   7b 4b 0b   1c 8c 2c

1d 4d 9d   0e 0e 0e   7f 2f 5f
0d 6d 0d   2e 1e 7e   9f 3f 4f
7d 2d 3d   4e 5e 9e   8f 1f 6f

4g 0g 1g   6h 8h 2h   5i 0i 0i
6g 5g 2g   0h 7h 0h   0i 0i 8i
0g 8g 7g   5h 0h 4h   2i 6i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_ser():
    puzzle_string = f"""
    hidden_unique_rectangle_ser.sudoku
    9

_a _a 2a   4b 8b 0b   0c 1c 3c
8a 7a 4a   1b 3b 6b   2c 5c 9c
_a _a _a   0b 0b 2b   8c 4c 0c

1d 2d 7d   0e 4e 9e   0f 8f 5f
0d 8d 5d   0e 0e 0e   9f 2f 0f
0d 6d 0d   2e 5e 8e   0f 7f 1f

2g 3g 0g   0h 0h 0h   0i 6i 0i
5g 4g 6g   7h 2h 3h   1i 9i 8i
7g 0g 0g   0h 6h 4h   5i 3i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_swc():
    puzzle_string = f"""
    hidden_unique_rectangle_swc.sudoku
    9

_a 2a 9a   3b 1b 6b   4c 0c 5c
_a _a 3a   7b 0b 2b   9c 1c 6c
6a _a 1a   4b 0b 0b   3c 2c 0c

0d 0d 2d   8e 0e 0e   1f 6f 3f
1d 8d 0d   6e 7e 3e   2f 0f 0f
9d 3d 6d   0e 0e 1e   8f 0f 0f

0g 1g 0g   0h 0h 7h   6i 0i 0i
3g 9g 0g   1h 6h 0h   7i 0i 2i
2g 6g 7g   9h 0h 8h   5i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_swr():
    puzzle_string = f"""
    hidden_unique_rectangle_swr.sudoku
    9

_a 8a _a   0b 3b 0b   0c 5c 1c
1a _a 9a   5b 7b 0b   4c 6c 0c
5a 6a _a   0b 0b 0b   0c 0c 0c

0d 0d 2d   8e 0e 7e   5f 0f 0f
6d 0d 0d   2e 0e 3e   0f 0f 9f
0d 0d 1d   9e 0e 5e   3f 0f 0f

0g 0g 0g   0h 0h 0h   0i 0i 5i
0g 1g 6g   0h 5h 0h   8i 0i 0i
4g 0g 0g   0h 8h 0h   0i 7i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_0():
    puzzle_string = f"""
    jellyfish_0.sudoku
    9

_a _a 1a   9b 0b 2b   5c 0c 0c
_a _a 6a   0b 0b 0b   0c 0c 0c
2a 9a _a   0b 5b 0b   0c 0c 1c

5d 0d 0d   6e 0e 0e   3f 1f 9f
0d 0d 0d   0e 0e 0e   0f 0f 0f
1d 4d 3d   0e 0e 7e   0f 0f 5f

4g 0g 0g   0h 3h 0h   0i 7i 6i
0g 0g 0g   0h 0h 0h   1i 0i 0i
0g 0g 9g   7h 0h 1h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_1():
    puzzle_string = f"""
    jellyfish_1.sudoku
    9

_a _a _a   4b 5b 9b   0c 0c 0c
5a _a 9a   3b 2b 0b   0c 7c 4c
4a 2a _a   7b 6b 0b   9c 3c 5c

0d 1d 3d   0e 9e 7e   5f 4f 2f
0d 5d 0d   0e 0e 0e   3f 1f 9f
9d 4d 2d   5e 1e 3e   8f 6f 7f

0g 7g 4g   9h 3h 6h   0i 5i 0i
1g 9g 6g   0h 7h 5h   4i 0i 3i
0g 0g 5g   1h 0h 0h   7i 9i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_2():
    puzzle_string = f"""
    jellyfish_2.sudoku
    9

9a 3a _a   0b 7b 0b   6c 8c 5c
7a _a _a   8b 0b 6b   0c 0c 3c
_a _a _a   0b 9b 3b   7c 0c 1c

1d 7d 0d   9e 6e 0e   5f 3f 2f
0d 9d 0d   0e 3e 0e   1f 6f 0f
2d 6d 3d   0e 0e 1e   0f 7f 0f

3g 0g 0g   0h 0h 5h   0i 0i 0i
4g 5g 7g   3h 0h 9h   0i 0i 6i
0g 1g 9g   0h 2h 0h   3i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_of_1_in_rows():
    puzzle_string = f"""
    jellyfish_of_1_in_rows.sudoku
    9

6a _a 9a   5b 7b 3b   0c 8c 2c
8a 7a _a   0b 9b 0b   6c 3c 5c
_a _a 5a   0b 6b 0b   9c 0c 7c

7d 6d 0d   9e 4e 2e   0f 5f 8f
9d 0d 0d   7e 8e 5e   0f 6f 0f
5d 8d 0d   3e 1e 6e   0f 0f 9f

4g 0g 7g   6h 5h 9h   8i 2i 0i
0g 5g 6g   0h 2h 0h   0i 9i 4i
2g 9g 8g   4h 3h 0h   5i 0i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_of_3_in_cols():
    puzzle_string = f"""
    jellyfish_of_3_in_cols.sudoku
    9

2a _a _a   4b 7b 5b   0c 0c 0c
9a _a 7a   0b 6b 8b   2c 5c 4c
_a 5a _a   9b 2b 0b   7c 0c 0c

5d 7d 0d   6e 9e 2e   0f 1f 8f
0d 2d 1d   8e 5e 7e   0f 9f 6f
8d 9d 6d   0e 4e 0e   5f 2f 7f

7g 8g 9g   2h 3h 6h   1i 4i 5i
1g 0g 2g   5h 8h 0h   6i 7i 0i
0g 0g 5g   7h 1h 0h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_locked_candidates_claiming_col():
    puzzle_string = f"""
    locked_candidates_claiming_col.sudoku
    9

5a _a _a   9b 8b 2b   1c 4c 3c
2a 9a 8a   4b 3b 1b   0c 0c 0c
4a _a _a   6b 7b 5b   2c 8c 9c

9d 0d 2d   5e 4e 7e   0f 0f 0f
0d 0d 0d   2e 9e 0e   0f 0f 0f
0d 0d 0d   1e 6e 0e   9f 0f 0f

7g 0g 0g   8h 2h 4h   0i 0i 1i
0g 0g 0g   7h 0h 9h   3i 0i 0i
0g 2g 0g   3h 0h 6h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_locked_candidates_claiming_row():
    puzzle_string = f"""
    locked_candidates_claiming_row.sudoku
    9

6a 9a 2a   3b 7b 8b   5c 1c 4c
_a _a 5a   6b 2b 0b   0c 3c 0c
_a 3a 8a   0b 4b 0b   2c 0c 0c

0d 0d 9d   0e 3e 0e   0f 0f 1f
0d 0d 1d   0e 5e 0e   3f 0f 0f
3d 0d 0d   1e 9e 0e   4f 0f 0f

0g 0g 4g   0h 1h 0h   7i 0i 0i
0g 8g 0g   4h 6h 2h   1i 0i 0i
0g 0g 0g   7h 8h 0h   0i 4i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_locked_candidates_pointing_col():
    puzzle_string = f"""
    locked_candidates_pointing_col.sudoku
    9

2a 6a _a   7b 0b 0b   0c 9c 0c
8a 1a _a   0b 2b 0b   7c 6c 0c
5a 7a _a   0b 4b 6b   1c 2c 0c

4d 8d 7d   0e 9e 0e   6f 0f 2f
3d 5d 1d   6e 8e 2e   4f 7f 9f
9d 2d 6d   4e 0e 7e   0f 0f 0f

6g 9g 8g   0h 3h 0h   2i 4i 7i
7g 4g 2g   0h 6h 0h   3i 5i 1i
1g 3g 5g   2h 7h 4h   9i 8i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_locked_candidates_pointing_row():
    puzzle_string = f"""
    locked_candidates_pointing_row.sudoku
    9

9a _a _a   2b 4b 0b   8c 3c 0c
6a _a _a   7b 8b 3b   2c 1c 9c
8a 2a 3a   1b 0b 9b   4c 0c 0c

0d 0d 0d   0e 9e 2e   0f 8f 0f
0d 8d 2d   0e 0e 0e   0f 9f 0f
0d 9d 0d   6e 7e 8e   0f 2f 0f

2g 0g 8g   9h 0h 4h   1i 0i 0i
7g 0g 9g   0h 2h 0h   0i 0i 8i
0g 3g 0g   8h 0h 7h   9i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_medusa_coloring_3d():
    puzzle_string = f"""
    medusa_coloring_3d.sudoku
    9

_a 3a 8a   0b 1b 0b   0c 0c 0c
4a 5a 2a   7b 9b 6b   1c 8c 3c
1a _a _a   0b 0b 8b   5c 0c 0c

0d 2d 1d   0e 0e 7e   4f 9f 6f
7d 4d 5d   9e 6e 2e   8f 3f 1f
0d 6d 9d   0e 0e 0e   7f 2f 5f

0g 0g 0g   4h 0h 0h   0i 0i 8i
5g 8g 3g   6h 7h 9h   2i 1i 4i
0g 0g 4g   0h 8h 0h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_medusa_coloring_3d_0():
    puzzle_string = f"""
    medusa_coloring_3d_0.sudoku
    9

3a _a _a   0b 0b 0b   8c 0c 0c
_a _a 4a   0b 9b 0b   0c 7c 0c
_a 7a 9a   0b 0b 2b   0c 0c 1c

0d 6d 0d   7e 0e 0e   0f 0f 4f
0d 0d 8d   0e 6e 0e   7f 0f 0f
5d 0d 0d   0e 0e 8e   0f 1f 0f

8g 0g 0g   5h 0h 0h   1i 6i 0i
0g 3g 0g   0h 1h 0h   2i 0i 0i
0g 0g 1g   0h 0h 0h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_naked_pair_col():
    puzzle_string = f"""
    naked_pair_col.sudoku
    9
    9a 6a 1a   0b 0b 5b   7c 4c 8c
    7a 4a 5a   0b 0b 0b   0c 3c 2c
    2a 3a 8a   0b 7b 4b   5c 1c 0c
    
    8d 2d 9d   0e 5e 1e   3f 7f 0f
    1d 7d 3d   0e 0e 0e   0f 5f 0f
    4d 5d 6d   7e 9e 3e   2f 8f 1f
    
    6g 1g 7g   5h 8h 9h   4i 2i 3i
    5g 9g 4g   0h 0h 2h   8i 6i 7i
    3g 8g 2g   0h 0h 7h   1i 9i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_pair_fence():
    puzzle_string = f"""
    naked_pair_fence.sudoku
    9

5a 6a 7a   9b 3b 8b   2c 1c 4c
2a 9a 3a   4b 1b 5b   0c 6c 0c
4a 1a 8a   2b 7b 6b   5c 3c 9c

0d 2d 4d   8e 0e 3e   1f 7f 5f
0d 5d 0d   0e 0e 0e   0f 4f 0f
0d 8d 1d   5e 4e 0e   6f 0f 0f

0g 4g 0g   0h 8h 9h   0i 5i 0i
0g 3g 0g   7h 5h 0h   4i 8i 0i
8g 7g 5g   0h 0h 4h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_naked_pair_row():
    puzzle_string = f"""
    naked_pair_row.sudoku
    9

4a 8a 1a   7b 3b 2b   9c 5c 6c
6a 3a 2a   9b 5b 8b   4c 1c 7c
7a 9a 5a   6b 4b 1b   3c 2c 8c

0d 0d 0d   4e 0e 0e   6f 0f 0f
0d 0d 4d   8e 0e 6e   2f 0f 0f
0d 6d 7d   5e 0e 3e   8f 4f 1f

5g 7g 3g   2h 6h 4h   1i 8i 9i
0g 4g 6g   1h 0h 5h   7i 3i 2i
1g 2g 0g   3h 0h 0h   5i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_4():
    puzzle_string = f"""
    naked_quad_4.sudoku
    9

_a _a _a   0b 7b 0b   0c 0c 0c
_a _a _a   2b 5b 0b   7c 0c 0c
7a _a _a   1b 0b 0b   2c 9c 6c

2d 0d 0d   0e 0e 0e   6f 0f 4f
0d 4d 7d   0e 0e 0e   5f 1f 0f
5d 0d 6d   0e 0e 0e   0f 0f 8f

1g 3g 8g   0h 0h 9h   0i 0i 7i
0g 0g 4g   0h 6h 1h   0i 0i 0i
0g 0g 0g   0h 4h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_5():
    puzzle_string = f"""
    naked_quad_5.sudoku
    9

9a 4a _a   0b 3b 5b   0c 6c 0c
3a 5a _a   6b 0b 0b   0c 0c 0c
_a 8a _a   0b 4b 0b   0c 0c 5c

6d 0d 0d   1e 0e 0e   0f 0f 0f
0d 0d 0d   0e 7e 0e   0f 0f 0f
0d 0d 0d   0e 0e 9e   0f 0f 4f

5g 0g 0g   0h 9h 0h   0i 4i 0i
0g 0g 0g   0h 0h 7h   0i 8i 9i
0g 7g 0g   4h 8h 0h   0i 3i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_6():
    puzzle_string = f"""
    naked_quad_6.sudoku
    9

_a _a _a   0b 1b 0b   0c 5c 7c
_a _a _a   0b 0b 8b   4c 0c 0c
_a _a _a   9b 0b 5b   1c 0c 3c

0d 1d 2d   0e 0e 0e   0f 7f 6f
0d 0d 0d   0e 0e 0e   0f 0f 0f
3d 6d 0d   0e 0e 0e   8f 9f 0f

7g 0g 6g   8h 0h 2h   0i 0i 0i
0g 0g 9g   7h 0h 0h   0i 0i 0i
4g 3g 0g   0h 5h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_7():
    puzzle_string = f"""
    naked_quad_7.sudoku
    9

_a _a 1a   2b 0b 5b   0c 9c 0c
5a _a 6a   0b 0b 4b   2c 7c 0c
2a _a _a   0b 0b 3b   0c 0c 0c

0d 0d 5d   0e 0e 0e   0f 8f 0f
0d 4d 9d   0e 0e 0e   1f 5f 0f
0d 2d 0d   5e 0e 0e   6f 0f 0f

0g 5g 0g   6h 0h 0h   0i 0i 0i
0g 6g 2g   3h 0h 0h   0i 1i 4i
9g 1g 3g   4h 0h 7h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_col():
    puzzle_string = f"""
    naked_quad_col.sudoku
    9

_a _a 1a   4b 0b 0b   0c 0c 0c
_a _a 5a   2b 1b 8b   0c 9c 0c
_a 2a _a   9b 5b 0b   0c 0c 0c

4d 0d 7d   0e 0e 9e   0f 0f 0f
0d 5d 0d   7e 2e 1e   0f 8f 0f
1d 0d 2d   0e 4e 0e   7f 0f 9f

0g 0g 0g   6h 9h 5h   0i 1i 0i
0g 1g 0g   3h 7h 4h   9i 0i 0i
5g 0g 0g   1h 8h 2h   6i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_fence():
    puzzle_string = f"""
    naked_quad_fence.sudoku
    9

_a 5a _a   0b 0b 3b   0c 0c 0c
3a _a 9a   0b 4b 8b   0c 0c 0c
_a 1a _a   6b 0b 0b   0c 0c 0c

0d 9d 6d   0e 3e 0e   4f 0f 8f
0d 3d 8d   0e 0e 0e   7f 0f 0f
1d 0d 7d   8e 0e 0e   3f 5f 0f

0g 0g 0g   0h 0h 1h   0i 7i 0i
0g 0g 0g   4h 8h 5h   9i 0i 2i
0g 0g 0g   3h 0h 0h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_row():
    puzzle_string = f"""
    naked_quad_row.sudoku
    9

_a _a 9a   0b 3b 0b   0c 2c 6c
_a _a _a   0b 0b 0b   0c 0c 0c
_a 6a _a   0b 2b 0b   5c 1c 4c

0d 0d 7d   0e 0e 5e   0f 6f 0f
0d 8d 0d   0e 0e 0e   0f 3f 5f
0d 5d 0d   1e 0e 0e   4f 0f 0f

4g 9g 2g   0h 8h 0h   0i 5i 0i
0g 0g 0g   0h 0h 0h   0i 0i 0i
8g 3g 0g   0h 7h 0h   2i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_triple_col():
    puzzle_string = f"""
    naked_triple_col.sudoku
    9

7a 9a _a   5b 0b 0b   8c 0c 6c
_a _a 8a   6b 0b 7b   0c 0c 0c
_a 6a _a   8b 1b 0b   0c 0c 4c

6d 0d 0d   2e 0e 0e   0f 0f 0f
2d 0d 0d   1e 0e 8e   0f 0f 5f
0d 0d 0d   7e 0e 4e   0f 0f 9f

8g 0g 0g   4h 7h 5h   9i 6i 0i
9g 7g 6g   3h 2h 1h   4i 5i 8i
4g 0g 5g   9h 8h 6h   0i 3i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_triple_fence():
    puzzle_string = f"""
    naked_triple_fence.sudoku
    9

_a 3a _a   0b 0b 5b   1c 0c 0c
_a 7a 1a   9b 0b 4b   6c 2c 0c
_a _a 4a   0b 0b 0b   0c 0c 0c

0d 0d 5d   6e 4e 9e   0f 7f 0f
0d 0d 7d   5e 2e 1e   9f 0f 6f
0d 9d 6d   8e 7e 3e   2f 0f 0f

0g 0g 0g   0h 0h 0h   5i 0i 0i
0g 5g 3g   4h 0h 0h   7i 6i 0i
0g 0g 8g   3h 5h 0h   4i 9i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_triple_row():
    puzzle_string = f"""
    naked_triple_row.sudoku
    9

7a 8a 2a   3b 5b 4b   1c 9c 6c
_a _a _a   2b 6b 7b   4c 5c 8c
4a 5a 6a   8b 9b 1b   3c 2c 7c

0d 0d 1d   5e 0e 0e   6f 0f 0f
5d 7d 0d   6e 0e 9e   2f 0f 1f
0d 6d 0d   0e 0e 8e   5f 0f 0f

6g 3g 7g   4h 8h 5h   9i 1i 2i
0g 4g 0g   0h 0h 6h   0i 3i 5i
0g 0g 5g   9h 0h 0h   0i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_0():
    puzzle_string = f"""
    remote_pair_0.sudoku
    9

_a _a 2a   0b 0b 5b   0c 0c 6c
_a _a _a   6b 0b 2b   0c 0c 9c
3a 1a _a   0b 0b 0b   0c 0c 0c

2d 0d 4d   0e 8e 0e   0f 5f 0f
0d 0d 1d   0e 0e 0e   8f 0f 0f
0d 9d 0d   0e 2e 0e   4f 0f 1f

0g 0g 0g   0h 0h 0h   0i 4i 8i
7g 0g 0g   4h 0h 3h   0i 0i 0i
4g 0g 0g   1h 0h 0h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_1():
    puzzle_string = f"""
    remote_pair_1.sudoku
    9

_a 8a 6a   4b 3b 9b   0c 0c 2c
_a 4a 1a   7b 8b 2b   0c 9c 6c
2a _a 9a   1b 5b 6b   4c 0c 8c

8d 1d 5d   3e 7e 4e   2f 6f 9f
6d 2d 0d   5e 9e 8e   0f 0f 4f
9d 0d 4d   2e 6e 1e   0f 8f 5f

1g 9g 2g   8h 4h 7h   6i 5i 3i
0g 6g 0g   9h 2h 5h   8i 4i 1i
4g 5g 8g   6h 1h 3h   9i 2i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_2():
    puzzle_string = f"""
    remote_pair_2.sudoku
    9

1a 2a 8a   9b 4b 6b   5c 3c 7c
3a 6a 7a   1b 2b 5b   4c 8c 9c
4a 9a 5a   3b 7b 8b   0c 0c 0c

8d 5d 4d   7e 0e 1e   0f 0f 0f
2d 1d 0d   8e 5e 0e   0f 7f 4f
0d 7d 3d   2e 0e 4e   1f 5f 8f

5g 4g 2g   6h 8h 0h   7i 0i 0i
0g 3g 0g   4h 1h 7h   8i 2i 5i
7g 8g 1g   5h 0h 2h   0i 4i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_row():
    puzzle_string = f"""
    remote_pair_row.sudoku
    9

1a 9a _a   2b 6b 5b   0c 3c 0c
6a _a 4a   0b 0b 9b   5c 0c 2c
5a 3a 2a   4b 7b 8b   0c 6c 0c

0d 5d 1d   0e 4e 6e   2f 9f 0f
2d 6d 0d   0e 9e 0e   0f 4f 5f
9d 4d 3d   7e 5e 2e   8f 1f 6f

0g 1g 5g   6h 2h 4h   0i 0i 0i
4g 0g 9g   5h 0h 0h   6i 2i 0i
0g 2g 6g   9h 8h 0h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_0():
    puzzle_string = f"""
    shashimi_jellyfish_0.sudoku
    9

2a 9a _a   4b 0b 3b   6c 0c 5c
7a 4a _a   0b 6b 5b   2c 3c 0c
3a 5a 6a   2b 0b 1b   4c 0c 0c

0d 0d 0d   0e 1e 4e   3f 6f 2f
6d 3d 0d   7e 0e 2e   0f 0f 4f
4d 1d 2d   6e 3e 0e   5f 0f 0f

0g 6g 0g   1h 4h 0h   9i 2i 3i
0g 0g 4g   3h 2h 0h   0i 5i 6i
0g 2g 3g   0h 0h 6h   7i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_1():
    puzzle_string = f"""
    shashimi_jellyfish_1.sudoku
    9

_a _a 2a   0b 7b 0b   0c 0c 0c
6a _a _a   0b 1b 8b   0c 0c 4c
_a _a _a   0b 0b 0b   3c 7c 0c

0d 7d 0d   1e 0e 0e   6f 0f 8f
0d 0d 9d   0e 0e 0e   4f 0f 0f
8d 0d 5d   0e 0e 9e   0f 2f 0f

0g 2g 8g   0h 0h 0h   0i 0i 0i
5g 0g 0g   7h 3h 0h   0i 0i 6i
0g 0g 0g   0h 9h 0h   5i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_2():
    puzzle_string = f"""
    shashimi_jellyfish_2.sudoku
    9

_a _a 5a   0b 0b 7b   8c 6c 0c
_a _a 6a   0b 0b 0b   5c 0c 0c
4a _a _a   0b 5b 6b   2c 0c 7c

0d 0d 0d   3e 4e 0e   6f 5f 8f
5d 0d 0d   7e 6e 8e   0f 0f 2f
8d 6d 0d   0e 2e 5e   0f 7f 0f

1g 5g 7g   6h 0h 0h   0i 0i 3i
6g 4g 8g   0h 7h 3h   0i 0i 5i
3g 9g 2g   5h 0h 4h   7i 0i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_3():
    puzzle_string = f"""
    shashimi_jellyfish_3.sudoku
    9

_a 2a _a   6b 3b 0b   5c 8c 0c
8a 5a 6a   1b 0b 2b   3c 7c 0c
9a 3a _a   7b 8b 5b   0c 6c 2c

0d 8d 0d   2e 1e 7e   0f 9f 0f
1d 6d 2d   3e 0e 0e   7f 0f 8f
0d 7d 9d   0e 6e 8e   2f 1f 0f

6g 4g 5g   8h 2h 1h   9i 3i 7i
0g 1g 0g   9h 0h 6h   8i 0i 0i
0g 9g 8g   0h 0h 3h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_0():
    puzzle_string = f"""
    shashimi_swordfish_0.sudoku
    9

_a _a 9a   0b 6b 4b   0c 0c 7c
8a _a _a   1b 0b 0b   5c 0c 0c
1a _a _a   3b 0b 5b   0c 9c 0c

0d 0d 0d   9e 0e 0e   0f 0f 5f
0d 0d 1d   0e 0e 0e   7f 0f 0f
2d 0d 0d   0e 0e 7e   0f 0f 0f

0g 2g 0g   7h 0h 1h   0i 0i 9i
0g 0g 5g   0h 0h 3h   0i 0i 4i
6g 0g 0g   4h 9h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_1():
    puzzle_string = f"""
    shashimi_swordfish_1.sudoku
    9

_a _a _a   0b 3b 0b   0c 0c 8c
_a _a 3a   0b 9b 0b   0c 2c 0c
9a 4a _a   8b 0b 6b   5c 3c 0c

2d 3d 1d   6e 0e 0e   0f 7f 9f
0d 0d 5d   0e 0e 0e   3f 0f 2f
7d 9d 0d   0e 0e 3e   1f 5f 6f

0g 0g 6g   0h 0h 2h   0i 1i 3i
0g 2g 0g   3h 6h 0h   7i 0i 0i
3g 0g 0g   0h 0h 0h   2i 6i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_2():
    puzzle_string = f"""
    shashimi_swordfish_2.sudoku
    9

_a _a _a   0b 0b 0b   0c 5c 0c
_a _a 6a   0b 1b 0b   0c 0c 2c
3a 5a _a   0b 0b 2b   1c 0c 0c

0d 1d 3d   0e 0e 5e   0f 6f 9f
0d 0d 5d   0e 0e 0e   8f 0f 0f
6d 9d 0d   1e 0e 0e   3f 2f 0f

0g 0g 8g   7h 0h 0h   0i 9i 4i
2g 0g 0g   0h 9h 0h   5i 0i 0i
0g 7g 0g   0h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_3():
    puzzle_string = f"""
    shashimi_swordfish_3.sudoku
    9

_a _a 6a   2b 8b 5b   0c 1c 0c
_a 9a _a   0b 1b 3b   8c 0c 7c
8a 1a _a   7b 0b 9b   5c 3c 0c

0d 6d 0d   5e 0e 0e   0f 0f 1f
2d 0d 1d   0e 0e 0e   0f 0f 5f
0d 5d 0d   0e 0e 1e   0f 8f 0f

0g 4g 0g   1h 0h 2h   0i 0i 8i
1g 0g 0g   3h 9h 0h   0i 5i 0i
0g 2g 0g   8h 0h 7h   1i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_4():
    puzzle_string = f"""
    shashimi_swordfish_4.sudoku
    9

_a 2a 7a   3b 9b 6b   5c 4c 0c
5a 6a 8a   8b 0b 0b   9c 0c 2c
4a 9a _a   0b 2b 5b   0c 6c 3c

0d 8d 2d   0e 5e 7e   4f 3f 0f
0d 0d 0d   9e 0e 2e   0f 5f 0f
0d 5d 0d   4e 8e 3e   2f 0f 0f

0g 1g 5g   2h 0h 8h   0i 9i 4i
2g 0g 9g   0h 0h 0h   0i 8i 5i
0g 0g 0g   5h 0h 9h   3i 2i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_5():
    puzzle_string = f"""
    shashimi_swordfish_5.sudoku
    9

7a 2a _a   0b 1b 0b   3c 5c 4c
8a _a 3a   4b 5b 2b   7c 0c 6c
5a 4a _a   0b 0b 0b   0c 0c 8c

2d 0d 0d   0e 0e 0e   8f 7f 5f
0d 0d 8d   1e 7e 5e   0f 0f 3f
0d 5d 7d   0e 0e 0e   1f 0f 9f

0g 0g 5g   0h 0h 1h   0i 8i 7i
1g 7g 0g   5h 8h 0h   6i 0i 2i
6g 8g 2g   0h 4h 0h   5i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_cols_1_fin():
    puzzle_string = f"""
    shashimi_sword_fish_cols_1_fin.sudoku
    9

_a 4a 7a   2b 3b 0b   8c 9c 6c
_a 9a 3a   6b 8b 0b   0c 0c 1c
_a 6a _a   0b 9b 0b   0c 0c 3c

6d 3d 0d   0e 7e 0e   9f 1f 8f
0d 7d 1d   9e 6e 8e   3f 5f 0f
9d 8d 0d   3e 0e 0e   6f 7f 0f

7g 5g 0g   0h 0h 6h   2i 3i 9i
3g 1g 6g   7h 2h 9h   4i 8i 5i
0g 2g 9g   0h 5h 3h   1i 6i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_cols_2_fins():
    puzzle_string = f"""
    shashimi_sword_fish_cols_2_fins.sudoku
    9

_a _a _a   8b 4b 0b   5c 2c 0c
5a _a 4a   3b 0b 0b   9c 0c 8c
_a 8a _a   0b 0b 5b   0c 0c 4c

4d 5d 9d   0e 7e 0e   0f 0f 1f
8d 0d 0d   0e 0e 0e   0f 4f 5f
1d 3d 6d   4e 5e 8e   2f 7f 9f

3g 4g 0g   9h 0h 0h   0i 5i 0i
2g 0g 8g   5h 0h 6h   4i 0i 0i
0g 6g 5g   0h 0h 4h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_rows_1_fin():
    puzzle_string = f"""
    shashimi_sword_fish_rows_1_fin.sudoku
    9

5a 8a 6a   2b 4b 1b   3c 9c 7c
_a _a 9a   7b 8b 0b   2c 0c 6c
_a 2a 7a   9b 0b 6b   8c 0c 0c

6d 0d 8d   0e 9e 0e   7f 0f 0f
2d 9d 0d   6e 0e 7e   0f 8f 0f
7d 0d 0d   8e 1e 0e   9f 6f 0f

9g 7g 0g   4h 6h 8h   1i 2i 0i
8g 0g 0g   0h 2h 0h   6i 7i 9i
0g 6g 2g   0h 7h 9h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_rows_2_fins():
    puzzle_string = f"""
    shashimi_sword_fish_rows_2_fins.sudoku
    9

_a 7a _a   9b 1b 0b   2c 6c 3c
_a _a _a   0b 0b 6b   0c 7c 1c
1a 6a _a   0b 3b 0b   5c 8c 0c

0d 2d 0d   0e 0e 0e   8f 3f 0f
0d 4d 0d   0e 2e 0e   0f 1f 0f
0d 1d 6d   0e 0e 0e   0f 9f 2f

0g 9g 4g   0h 5h 0h   0i 2i 7i
2g 5g 7g   3h 0h 0h   0i 4i 0i
6g 0g 1g   0h 0h 2h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_00():
    puzzle_string = f"""
    shashimi_x_wing_00.sudoku
    9

1a _a _a   0b 8b 0b   6c 0c 0c
_a _a _a   6b 0b 0b   8c 0c 0c
_a 6a _a   1b 0b 3b   0c 0c 2c

0d 0d 0d   7e 0e 0e   0f 0f 9f
4d 0d 9d   0e 0e 0e   1f 0f 3f
3d 0d 0d   0e 0e 9e   0f 0f 0f

5g 0g 0g   4h 0h 8h   0i 9i 0i
0g 0g 7g   0h 0h 2h   0i 0i 0i
0g 0g 3g   0h 5h 0h   0i 0i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_01():
    puzzle_string = f"""
    shashimi_x_wing_01.sudoku
    9

1a _a 8a   0b 0b 5b   0c 0c 4c
_a _a 5a   7b 0b 4b   0c 8c 9c
_a _a _a   0b 0b 0b   5c 0c 0c

0d 0d 0d   0e 0e 7e   0f 0f 2f
0d 9d 0d   0e 8e 0e   0f 7f 0f
6d 0d 0d   3e 0e 0e   0f 0f 0f

0g 0g 1g   0h 0h 0h   0i 0i 0i
9g 8g 0g   2h 0h 3h   7i 0i 0i
2g 0g 0g   6h 0h 0h   9i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_02():
    puzzle_string = f"""
    shashimi_x_wing_02.sudoku
    9

_a 9a _a   5b 0b 0b   0c 0c 0c
_a 6a _a   0b 7b 2b   8c 0c 4c
_a _a _a   9b 8b 4b   0c 0c 0c

3d 2d 0d   0e 0e 0e   4f 0f 6f
0d 0d 6d   0e 0e 0e   2f 0f 0f
7d 0d 4d   0e 0e 0e   0f 1f 9f

0g 0g 0g   3h 9h 1h   0i 0i 0i
9g 0g 7g   8h 4h 0h   0i 2i 0i
0g 0g 0g   0h 0h 7h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_03():
    puzzle_string = f"""
    shashimi_x_wing_03.sudoku
    9

5a _a _a   0b 2b 0b   1c 0c 9c
2a _a 9a   3b 0b 0b   0c 5c 4c
_a _a _a   0b 0b 8b   0c 0c 6c

0d 1d 0d   0e 0e 4e   0f 0f 0f
0d 0d 7d   0e 0e 0e   5f 0f 0f
0d 0d 0d   2e 0e 0e   0f 1f 0f

1g 0g 0g   9h 0h 0h   0i 0i 0i
4g 5g 0g   0h 0h 2h   9i 0i 1i
9g 0g 3g   0h 6h 0h   0i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_04():
    puzzle_string = f"""
    shashimi_x_wing_04.sudoku
    9

7a 2a 8a   0b 1b 0b   9c 0c 5c
_a 9a _a   0b 0b 0b   8c 0c 0c
_a _a 3a   0b 9b 8b   0c 4c 0c

0d 0d 9d   8e 2e 0e   7f 0f 3f
8d 7d 0d   0e 3e 9e   0f 5f 0f
2d 3d 1d   0e 0e 6e   4f 8f 9f

0g 1g 0g   9h 4h 0h   5i 0i 8i
9g 8g 2g   0h 0h 0h   0i 0i 4i
0g 0g 0g   0h 8h 0h   0i 9i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_05():
    puzzle_string = f"""
    shashimi_x_wing_05.sudoku
    9

5a 9a _a   4b 0b 0b   8c 3c 2c
_a _a 4a   0b 0b 2b   7c 1c 5c
1a 2a _a   8b 5b 0b   6c 9c 4c

2d 7d 0d   1e 0e 0e   0f 4f 6f
3d 4d 0d   0e 0e 0e   0f 7f 1f
9d 6d 1d   7e 4e 5e   2f 8f 3f

7g 1g 2g   6h 8h 4h   3i 5i 9i
0g 0g 9g   5h 0h 0h   4i 0i 7i
4g 5g 0g   0h 7h 9h   1i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_06():
    puzzle_string = f"""
    shashimi_x_wing_06.sudoku
    9

7a _a 5a   3b 0b 0b   9c 2c 4c
4a _a 6a   5b 2b 0b   7c 3c 8c
3a 2a _a   0b 7b 4b   6c 5c 1c

5d 4d 1d   2e 9e 3e   8f 7f 6f
0d 3d 0d   7e 4e 0e   5f 1f 2f
2d 0d 7d   0e 1e 5e   4f 9f 3f

8g 7g 3g   4h 5h 2h   1i 6i 9i
0g 0g 4g   0h 3h 7h   2i 8i 5i
0g 5g 2g   0h 0h 0h   3i 4i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_07():
    puzzle_string = f"""
    shashimi_x_wing_07.sudoku
    9

4a 7a _a   6b 9b 0b   5c 0c 1c
9a 6a _a   8b 5b 1b   0c 0c 0c
5a 1a _a   0b 0b 4b   0c 9c 6c

2d 9d 6d   0e 1e 0e   4f 0f 5f
8d 5d 7d   4e 0e 0e   1f 6f 0f
3d 4d 1d   5e 6e 0e   2f 7f 0f

1g 8g 5g   9h 0h 0h   6i 0i 0i
6g 3g 0g   2h 0h 5h   0i 1i 0i
7g 2g 0g   1h 8h 6h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_08():
    puzzle_string = f"""
    shashimi_x_wing_08.sudoku
    9

4a 7a _a   6b 9b 0b   5c 0c 1c
9a 6a _a   8b 5b 1b   0c 0c 0c
5a 1a _a   0b 0b 4b   0c 9c 6c

2d 9d 6d   0e 1e 0e   4f 0f 5f
8d 5d 7d   4e 0e 0e   1f 6f 0f
3d 4d 1d   5e 6e 0e   2f 7f 0f

1g 8g 5g   9h 0h 0h   6i 0i 0i
6g 3g 0g   2h 0h 5h   0i 1i 0i
7g 2g 0g   1h 8h 6h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_09():
    puzzle_string = f"""
    shashimi_x_wing_09.sudoku
    9

1a _a _a   0b 9b 7b   5c 0c 4c
_a 4a 9a   5b 1b 6b   7c 2c 0c
5a 7a _a   0b 0b 4b   0c 9c 1c

2d 9d 8d   4e 6e 5e   1f 0f 0f
7d 1d 4d   9e 0e 0e   2f 5f 6f
0d 0d 5d   1e 7e 2e   8f 4f 9f

9g 5g 0g   0h 2h 0h   4i 1i 0i
0g 2g 1g   7h 4h 9h   0i 0i 5i
4g 0g 0g   0h 5h 1h   9i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_col_1_fin():
    puzzle_string = f"""
    shashimi_x_wing_col_1_fin.sudoku
    9

3a _a 4a   6b 1b 0b   0c 7c 0c
_a _a 1a   0b 0b 0b   6c 4c 9c
_a 6a 8a   0b 4b 0b   0c 0c 0c

1d 4d 6d   0e 0e 8e   9f 2f 7f
0d 3d 0d   0e 2e 6e   4f 5f 0f
5d 0d 2d   4e 9e 0e   0f 0f 6f

6g 0g 3g   0h 7h 0h   5i 9i 4i
4g 0g 0g   0h 0h 0h   0i 6i 0i
0g 1g 0g   0h 6h 4h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_col_2_fins():
    puzzle_string = f"""
    shashimi_x_wing_col_2_fins.sudoku
    9

7a _a 3a   5b 4b 0b   0c 8c 6c
4a _a 5a   9b 8b 6b   0c 0c 0c
8a _a 6a   0b 0b 7b   4c 0c 5c

1d 5d 4d   0e 6e 0e   0f 7f 8f
9d 3d 8d   7e 0e 0e   5f 6f 0f
2d 6d 7d   8e 5e 0e   3f 1f 0f

6g 8g 9g   4h 0h 0h   0i 5i 0i
5g 0g 2g   1h 0h 8h   6i 0i 0i
3g 0g 1g   6h 9h 5h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_row_1_fin():
    puzzle_string = f"""
    shashimi_x_wing_row_1_fin.sudoku
    9

7a _a _a   0b 0b 9b   0c 3c 2c
_a 9a 3a   2b 0b 0b   5c 6c 7c
2a _a 6a   7b 3b 0b   0c 4c 0c

0d 1d 9d   4e 8e 7e   2f 5f 0f
0d 2d 5d   1e 9e 6e   7f 8f 0f
0d 7d 8d   3e 5e 2e   0f 9f 0f

0g 6g 0g   9h 7h 3h   0i 2i 5i
9g 0g 7g   0h 2h 0h   3i 1i 0i
5g 3g 2g   8h 0h 0h   0i 7i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_row_2_fins():
    puzzle_string = f"""
    shashimi_x_wing_row_2_fins.sudoku
    9

_a 9a 7a   1b 0b 4b   0c 0c 3c
4a _a _a   0b 3b 7b   0c 9c 0c
_a 3a _a   6b 0b 9b   4c 8c 7c

7d 0d 0d   0e 9e 8e   0f 0f 0f
9d 5d 0d   2e 6e 0e   0f 7f 4f
0d 0d 0d   7e 0e 0e   0f 0f 9f

0g 1g 0g   0h 7h 2h   9i 0i 0i
0g 2g 9g   0h 1h 6h   7i 0i 5i
6g 7g 0g   9h 0h 5h   2i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_simple_coloring_0():
    puzzle_string = f"""
    simple_coloring_0.sudoku
    9

3a 5a 6a   2b 0b 0b   9c 0c 4c
4a 2a 9a   5b 3b 0b   0c 6c 0c
_a _a 7a   9b 4b 6b   5c 2c 3c

0d 0d 5d   4e 0e 0e   0f 0f 0f
6d 9d 3d   1e 7e 2e   4f 5f 8f
0d 4d 0d   0e 0e 5e   0f 0f 0f

5g 6g 0g   8h 0h 4h   7i 3i 9i
0g 3g 4g   7h 5h 9h   6i 0i 2i
9g 7g 0g   0h 0h 0h   0i 4i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_simple_coloring_1():
    puzzle_string = f"""
    simple_coloring_1.sudoku
    9

6a _a 1a   4b 0b 5b   9c 2c 8c
8a 4a _a   9b 1b 2b   7c 6c 0c
2a _a 9a   0b 0b 0b   1c 0c 4c

0d 1d 0d   0e 0e 4e   0f 0f 0f
9d 8d 6d   7e 2e 3e   5f 4f 1f
4d 0d 0d   1e 0e 0e   0f 0f 0f

1g 6g 8g   0h 0h 7h   4i 9i 0i
7g 9g 4g   0h 8h 1h   0i 0i 6i
0g 2g 0g   6h 4h 9h   8i 1i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_simple_coloring_trap_0():
    puzzle_string = f"""
    simple_coloring_trap_0.sudoku
    9

5a _a _a   0b 2b 7b   0c 0c 4c
_a _a 4a   0b 0b 0b   5c 0c 0c
_a 7a 6a   0b 0b 4b   0c 3c 0c

0d 0d 0d   0e 0e 0e   0f 2f 3f
0d 0d 7d   0e 3e 0e   6f 0f 0f
8d 3d 0d   0e 0e 0e   0f 0f 0f

0g 5g 0g   6h 0h 0h   3i 8i 0i
0g 0g 8g   0h 0h 0h   4i 0i 0i
6g 0g 0g   4h 8h 0h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_0():
    puzzle_string = f"""
    sue_de_coq_0.sudoku
    9

_a 7a _a   0b 9b 6b   4c 0c 0c
_a _a _a   0b 0b 5b   6c 0c 0c
_a _a _a   0b 0b 0b   0c 2c 0c

0d 0d 0d   6e 0e 4e   0f 5f 1f
0d 4d 0d   8e 0e 1e   0f 9f 0f
8d 9d 0d   2e 0e 3e   0f 0f 0f

0g 3g 0g   0h 0h 0h   0i 0i 0i
0g 0g 7g   5h 0h 0h   0i 0i 0i
0g 0g 9g   1h 0h 2h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_1():
    puzzle_string = f"""
    sue_de_coq_1.sudoku
    9

_a _a 8a   0b 0b 0b   0c 0c 0c
_a 4a 2a   0b 8b 0b   6c 0c 0c
_a 9a _a   5b 0b 4b   0c 1c 0c

0d 0d 5d   0e 0e 9e   1f 4f 0f
0d 0d 0d   0e 0e 0e   0f 0f 0f
0d 3d 4d   2e 0e 0e   7f 0f 0f

8g 7g 0g   1h 0h 2h   0i 6i 0i
0g 0g 6g   0h 7h 5h   3i 8i 0i
0g 0g 0g   0h 0h 0h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_2():
    puzzle_string = f"""
    sue_de_coq_2.sudoku
    9

_a _a _a   0b 5b 8b   0c 2c 0c
2a 8a _a   6b 1b 0b   0c 0c 0c
_a _a 1a   2b 9b 0b   0c 3c 8c

7d 6d 2d   5e 8e 1e   4f 9f 3f
5d 1d 4d   0e 2e 0e   7f 8f 6f
0d 0d 8d   4e 7e 6e   2f 1f 5f

0g 2g 0g   0h 3h 0h   8i 0i 0i
0g 0g 0g   8h 4h 5h   0i 6i 2i
8g 0g 0g   1h 6h 2h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_col():
    puzzle_string = f"""
    sue_de_coq_col.sudoku
    9

_a _a _a   0b 9b 3b   0c 6c 0c
3a 9a 1a   0b 6b 0b   0c 4c 0c
_a _a 6a   0b 0b 0b   9c 0c 3c

4d 1d 7d   9e 5e 2e   8f 3f 6f
0d 3d 0d   0e 4e 0e   0f 2f 0f
8d 6d 2d   0e 0e 7e   4f 5f 9f

0g 0g 8g   0h 0h 0h   2i 0i 0i
0g 7g 3g   0h 2h 0h   6i 8i 5i
0g 2g 0g   5h 0h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_row():
    puzzle_string = f"""
    sue_de_coq_row.sudoku
    9

_a 4a _a   0b 9b 8b   7c 5c 6c
8a 9a 7a   6b 4b 5b   3c 1c 2c
_a _a 5a   1b 0b 7b   4c 9c 8c

0d 0d 4d   5e 8e 0e   0f 7f 0f
0d 8d 0d   0e 0e 0e   0f 6f 4f
0d 1d 0d   0e 6e 4e   8f 0f 0f

0g 7g 0g   8h 5h 2h   6i 4i 0i
4g 2g 6g   9h 7h 3h   0i 8i 0i
0g 5g 8g   4h 1h 6h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_0():
    puzzle_string = f"""
    swordfish_0.sudoku
    9

2a _a _a   0b 0b 0b   0c 0c 0c
7a _a 5a   0b 0b 6b   0c 0c 1c
3a _a 9a   0b 8b 0b   2c 0c 7c

0d 0d 0d   0e 0e 5e   0f 0f 0f
1d 0d 8d   3e 0e 9e   7f 0f 2f
0d 0d 0d   1e 0e 0e   0f 0f 0f

4g 0g 6g   0h 1h 0h   9i 0i 3i
8g 0g 0g   2h 0h 0h   6i 0i 4i
0g 0g 0g   0h 0h 0h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_1():
    puzzle_string = f"""
    swordfish_1.sudoku
    9
    
8a 3a 4a   7b 2b 0b   0c 1c 5c
2a 1a 5a   8b 0b 0b   0c 7c 0c
_a 9a _a   0b 5b 1b   0c 2c 8c

0d 7d 2d   6e 3e 5e   0f 8f 4f
0d 4d 3d   9e 8e 7e   0f 5f 2f
5d 8d 0d   0e 1e 0e   7f 3f 0f

3g 0g 0g   5h 0h 0h   8i 4i 0i
4g 0g 0g   0h 0h 8h   5i 9i 3i
0g 5g 8g   0h 4h 0h   2i 6i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_2():
    puzzle_string = f"""
    swordfish_2.sudoku
    9

2a _a _a   0b 0b 0b   0c 0c 0c
_a _a 4a   9b 0b 6b   0c 3c 0c
6a 3a _a   0b 0b 4b   0c 0c 5c

0d 0d 0d   0e 0e 3e   0f 1f 6f
0d 0d 3d   0e 0e 0e   2f 0f 0f
7d 4d 0d   1e 0e 0e   0f 0f 0f

1g 0g 0g   3h 0h 0h   0i 9i 2i
0g 5g 0g   2h 0h 7h   4i 0i 0i
0g 0g 0g   0h 0h 0h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_3():
    puzzle_string = f"""
    swordfish_3.sudoku
    9

5a 7a 1a   3b 0b 0b   0c 0c 0c
6a 2a _a   0b 4b 0b   0c 0c 0c
4a _a _a   0b 0b 7b   1c 0c 0c

0d 0d 4d   0e 1e 0e   0f 2f 0f
7d 0d 0d   8e 0e 5e   0f 0f 4f
0d 8d 0d   0e 9e 0e   7f 0f 0f

0g 0g 3g   9h 0h 0h   0i 0i 5i
0g 0g 0g   0h 2h 0h   0i 4i 1i
0g 0g 0g   0h 0h 3h   2i 7i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_4():
    puzzle_string = f"""
    swordfish_4.sudoku
    9

_a _a _a   7b 0b 0b   0c 0c 5c
_a 5a _a   0b 6b 0b   9c 0c 0c
4a _a 9a   0b 8b 0b   0c 7c 0c

8d 0d 7d   0e 0e 0e   0f 0f 0f
0d 1d 6d   0e 0e 0e   4f 2f 0f
0d 0d 0d   0e 0e 0e   3f 0f 7f

0g 7g 0g   0h 9h 0h   1i 0i 3i
0g 0g 2g   0h 5h 0h   0i 4i 0i
9g 0g 0g   0h 0h 1h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_5():
    puzzle_string = f"""
    swordfish_5.sudoku
    9

_a _a 1a   8b 7b 9b   0c 0c 5c
5a 9a 8a   0b 0b 3b   7c 2c 1c
_a 7a 6a   5b 2b 1b   8c 9c 0c

0d 1d 9d   7e 0e 5e   3f 0f 0f
7d 0d 5d   0e 0e 0e   0f 1f 0f
0d 0d 4d   1e 0e 2e   5f 7f 0f

0g 5g 7g   2h 0h 0h   9i 4i 0i
0g 8g 3g   9h 0h 7h   2i 5i 6i
9g 0g 2g   0h 5h 0h   1i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_6():
    puzzle_string = f"""
    swordfish_6.sudoku
    9

_a _a 6a   3b 9b 0b   7c 0c 4c
4a 2a 1a   0b 7b 8b   3c 0c 9c
7a 9a 3a   0b 0b 4b   8c 0c 0c

0d 7d 8d   9e 1e 5e   4f 0f 2f
0d 1d 2d   8e 4e 6e   9f 0f 7f
9d 0d 4d   0e 3e 0e   1f 8f 0f

2g 0g 0g   4h 0h 0h   6i 9i 1i
0g 4g 9g   0h 2h 0h   5i 7i 0i
1g 0g 0g   0h 0h 9h   2i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_of_5_in_rows():
    puzzle_string = f"""
    swordfish_of_5_in_rows.sudoku
    9

3a _a 6a   0b 4b 8b   2c 7c 9c
9a _a _a   7b 2b 6b   0c 0c 3c
2a 8a 7a   3b 9b 0b   6c 0c 4c

8d 9d 1d   6e 3e 4e   7f 2f 5f
4d 0d 0d   8e 7e 9e   1f 3f 6f
7d 6d 3d   2e 0e 0e   4f 9f 8f

5g 0g 0g   0h 8h 2h   3i 6i 0i
1g 0g 0g   0h 6h 3h   0i 4i 0i
6g 3g 0g   4h 0h 7h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_of_8_in_cols():
    puzzle_string = f"""
    swordfish_of_8_in_cols.sudoku
    9

6a 8a _a   0b 3b 4b   0c 0c 2c
3a _a _a   0b 0b 0b   0c 0c 0c
5a 7a _a   0b 9b 2b   0c 3c 6c

0d 0d 0d   2e 0e 3e   0f 0f 0f
2d 9d 0d   5e 0e 7e   0f 6f 3f
0d 0d 0d   9e 0e 8e   0f 0f 0f

1g 4g 0g   0h 2h 9h   0i 7i 5i
0g 0g 0g   4h 0h 1h   0i 0i 9i
9g 0g 0g   3h 0h 0h   0i 4i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_00():
    puzzle_string = f"""
    unique_rectangle_type3_00.sudoku
    9

9a 3a _a   0b 0b 8b   0c 0c 0c
_a _a _a   3b 0b 0b   0c 8c 5c
6a _a _a   0b 1b 0b   0c 9c 4c

0d 5d 0d   0e 0e 0e   0f 1f 9f
0d 0d 6d   0e 0e 0e   4f 0f 0f
1d 7d 0d   0e 0e 0e   0f 2f 0f

7g 6g 0g   0h 9h 0h   0i 0i 1i
5g 8g 0g   0h 0h 3h   0i 0i 0i
0g 0g 0g   1h 0h 0h   0i 3i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_01():
    puzzle_string = f"""
    unique_rectangle_type3_01.sudoku
    9

8a _a _a   2b 0b 0b   6c 1c 0c
_a _a 5a   0b 0b 1b   0c 0c 0c
_a _a 7a   0b 3b 0b   0c 0c 0c

0d 6d 0d   4e 0e 0e   0f 0f 8f
0d 0d 3d   0e 9e 0e   1f 0f 0f
5d 0d 0d   0e 0e 6e   0f 3f 0f

0g 0g 0g   0h 5h 0h   4i 0i 0i
0g 0g 0g   7h 0h 0h   3i 0i 0i
0g 3g 6g   0h 0h 8h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_02():
    puzzle_string = f"""
    unique_rectangle_type3_02.sudoku
    9

_a _a 5a   0b 6b 0b   0c 4c 0c
2a 4a 7a   0b 0b 0b   0c 1c 0c
6a _a _a   4b 0b 0b   0c 0c 9c

0d 0d 9d   0e 0e 0e   0f 0f 2f
4d 0d 0d   3e 0e 6e   0f 0f 7f
8d 0d 0d   0e 0e 0e   5f 0f 0f

7g 0g 0g   0h 0h 3h   0i 0i 8i
0g 3g 0g   0h 0h 0h   4i 5i 6i
0g 2g 0g   0h 9h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_03():
    puzzle_string = f"""
    unique_rectangle_type3_03.sudoku
    9

_a _a 3a   0b 0b 0b   7c 0c 0c
_a _a _a   0b 0b 8b   0c 0c 0c
5a 4a _a   0b 0b 0b   6c 3c 0c

1d 7d 0d   0e 0e 6e   0f 5f 0f
0d 8d 0d   3e 0e 5e   0f 6f 0f
0d 6d 0d   9e 0e 0e   0f 2f 7f

0g 1g 4g   0h 0h 0h   0i 9i 5i
0g 0g 0g   2h 0h 0h   0i 0i 0i
0g 0g 6g   0h 0h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_04():
    puzzle_string = f"""
    unique_rectangle_type3_04.sudoku
    9

_a _a _a   8b 0b 0b   0c 6c 1c
8a 1a _a   0b 0b 3b   0c 0c 0c
_a 3a _a   0b 4b 0b   0c 9c 5c

7d 0d 0d   0e 0e 0e   0f 3f 9f
0d 0d 2d   0e 0e 0e   5f 0f 0f
3d 4d 0d   0e 0e 0e   0f 0f 6f

4g 2g 0g   0h 3h 0h   0i 5i 0i
0g 0g 0g   1h 0h 0h   0i 4i 8i
1g 6g 0g   0h 0h 8h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_05():
    puzzle_string = f"""
    unique_rectangle_type3_05.sudoku
    9

_a _a 5a   2b 0b 0b   0c 0c 0c
_a 9a _a   0b 0b 7b   4c 0c 2c
_a _a 3a   0b 6b 0b   0c 0c 0c

4d 0d 0d   0e 0e 1e   0f 9f 0f
0d 0d 6d   0e 8e 0e   2f 0f 0f
0d 5d 0d   4e 0e 0e   0f 0f 6f

0g 0g 0g   0h 5h 0h   1i 0i 0i
6g 0g 4g   9h 0h 0h   0i 8i 0i
0g 0g 0g   0h 0h 3h   6i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_06():
    puzzle_string = f"""
    unique_rectangle_type3_06.sudoku
    9

8a _a _a   7b 0b 0b   0c 0c 2c
_a _a _a   5b 2b 6b   0c 0c 0c
_a 5a 7a   0b 0b 4b   0c 0c 3c

7d 0d 0d   0e 0e 0e   5f 0f 0f
0d 8d 0d   0e 0e 0e   0f 3f 0f
0d 0d 4d   0e 0e 0e   0f 0f 7f

9g 0g 0g   6h 0h 0h   7i 1i 0i
0g 0g 0g   4h 9h 3h   0i 0i 0i
4g 0g 0g   0h 0h 2h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_07():
    puzzle_string = f"""
    unique_rectangle_type3_07.sudoku
    9

_a 9a _a   2b 0b 0b   7c 6c 1c
4a 7a 1a   8b 9b 6b   3c 2c 5c
6a 3a 2a   1b 5b 7b   9c 8c 4c

1d 0d 9d   4e 0e 0e   6f 3f 0f
0d 4d 6d   9e 0e 0e   1f 5f 0f
0d 0d 3d   0e 0e 1e   8f 4f 9f

3g 1g 0g   7h 0h 0h   2i 9i 6i
9g 6g 4g   3h 1h 2h   5i 7i 8i
2g 0g 7g   0h 0h 9h   4i 1i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_east_col():
    puzzle_string = f"""
    unique_rectangle_type3_east_col.sudoku
    9

6a _a _a   2b 8b 5b   3c 0c 0c
7a 3a 2a   1b 9b 6b   5c 8c 4c
8a _a 5a   3b 4b 7b   0c 6c 2c

0d 8d 0d   6e 2e 4e   0f 3f 5f
5d 2d 0d   9e 1e 3e   6f 0f 8f
0d 6d 3d   5e 7e 8e   0f 2f 0f

2g 5g 8g   0h 3h 0h   0i 0i 6i
3g 0g 1g   0h 6h 2h   8i 5i 0i
0g 0g 6g   8h 5h 0h   2i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_east_fence():
    puzzle_string = f"""
    unique_rectangle_type3_east_fence.sudoku
    9

5a 2a 9a   7b 3b 6b   4c 1c 8c
6a 7a 8a   0b 0b 1b   2c 0c 0c
3a 4a 1a   8b 2b 9b   7c 6c 5c

2d 9d 5d   6e 0e 0e   0f 4f 0f
0d 6d 3d   0e 0e 2e   5f 8f 0f
0d 8d 4d   0e 0e 5e   0f 2f 6f

9g 3g 7g   1h 6h 4h   8i 5i 2i
4g 5g 6g   2h 0h 0h   0i 7i 1i
8g 1g 2g   0h 0h 7h   6i 0i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_north_row():
    puzzle_string = f"""
    unique_rectangle_type3_north_row.sudoku
    9

9a 8a _a   0b 0b 0b   5c 7c 1c
3a _a _a   8b 0b 0b   2c 9c 6c
7a 2a _a   0b 9b 0b   8c 3c 4c

8d 0d 9d   0e 0e 0e   4f 1f 2f
5d 0d 0d   1e 0e 8e   9f 6f 3f
6d 0d 0d   0e 0e 0e   7f 8f 5f

4g 9g 7g   0h 1h 0h   6i 5i 8i
1g 6g 8g   0h 0h 5h   3i 2i 9i
2g 5g 3g   0h 8h 0h   1i 4i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_south_row():
    puzzle_string = f"""
    unique_rectangle_type3_south_row.sudoku
    9

_a 9a 3a   0b 5b 0b   6c 0c 7c
_a 6a _a   9b 0b 0b   1c 0c 5c
4a _a _a   0b 0b 6b   8c 0c 9c

6d 0d 0d   7e 2e 9e   3f 5f 8f
3d 7d 8d   0e 4e 0e   9f 6f 2f
5d 2d 9d   6e 8e 3e   4f 7f 1f

0g 0g 0g   8h 0h 0h   7i 9i 6i
9g 8g 0g   0h 6h 7h   5i 1i 0i
7g 0g 6g   0h 9h 0h   2i 8i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_west_fence():
    puzzle_string = f"""
    unique_rectangle_type3_west_fence.sudoku
    9

1a _a 3a   8b 0b 0b   7c 4c 2c
8a 5a 7a   1b 4b 2b   6c 3c 9c
2a 4a _a   0b 0b 3b   1c 8c 5c

4d 0d 8d   0e 0e 7e   5f 2f 0f
0d 7d 5d   0e 0e 8e   4f 6f 0f
0d 0d 2d   4e 0e 0e   9f 7f 8f

5g 2g 1g   3h 6h 4h   8i 9i 7i
7g 3g 4g   5h 8h 9h   2i 1i 6i
0g 8g 0g   0h 0h 1h   3i 5i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_0():
    puzzle_string = f"""
    wxyz_wing_0.sudoku
    9

_a 6a 7a   0b 3b 1b   0c 0c 9c
_a 3a _a   0b 0b 0b   0c 4c 0c
8a _a 4a   0b 0b 0b   0c 0c 0c

4d 0d 0d   2e 0e 0e   0f 0f 0f
9d 0d 0d   6e 0e 8e   0f 0f 3f
0d 0d 0d   0e 0e 9e   0f 0f 8f

0g 0g 0g   0h 0h 0h   6i 0i 1i
0g 7g 0g   0h 0h 0h   0i 5i 0i
3g 0g 0g   1h 5h 0h   7i 9i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_19():
    puzzle_string = f"""
    wxyz_wing_19.sudoku
    9

9a _a 3a   8b 0b 1b   0c 0c 6c
8a _a 6a   0b 7b 0b   0c 0c 1c
1a 5a 7a   6b 0b 2b   0c 4c 0c

2d 3d 9d   1e 6e 0e   4f 0f 7f
6d 1d 8d   0e 0e 0e   2f 0f 0f
4d 7d 5d   2e 0e 0e   6f 1f 0f

5g 6g 4g   9h 1h 3h   0i 0i 2i
3g 9g 2g   0h 8h 0h   1i 6i 4i
7g 8g 1g   4h 2h 6h   9i 3i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_4():
    puzzle_string = f"""
    wxyz_wing_4.sudoku
    9

_a _a _a   0b 0b 0b   0c 2c 0c
_a _a _a   0b 5b 2b   1c 0c 9c
9a 4a _a   3b 0b 0b   0c 0c 0c

5d 0d 0d   0e 0e 0e   0f 6f 1f
0d 2d 0d   0e 9e 0e   0f 4f 0f
6d 8d 0d   0e 0e 0e   0f 0f 5f

0g 0g 0g   0h 0h 3h   0i 5i 7i
2g 0g 8g   6h 4h 0h   0i 0i 0i
0g 3g 0g   0h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_5():
    puzzle_string = f"""
    wxyz_wing_5.sudoku
    9

_a _a 2a   4b 0b 0b   0c 8c 9c
_a _a _a   8b 3b 2b   0c 4c 1c
8a 4a _a   0b 0b 5b   3c 2c 7c

4d 0d 3d   0e 0e 0e   9f 0f 8f
0d 5d 0d   0e 0e 8e   4f 6f 3f
6d 0d 8d   3e 0e 4e   1f 0f 2f

1g 6g 4g   2h 8h 3h   7i 9i 5i
9g 8g 5g   7h 6h 1h   2i 3i 4i
0g 0g 7g   5h 4h 9h   8i 1i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_6():
    puzzle_string = f"""
    wxyz_wing_6.sudoku
    9

_a _a _a   0b 0b 0b   8c 7c 4c
_a _a 3a   0b 0b 4b   9c 5c 6c
9a 4a _a   0b 0b 8b   2c 1c 3c

3d 0d 0d   1e 4e 9e   7f 2f 8f
1d 0d 4d   0e 5e 7e   3f 6f 9f
0d 7d 9d   3e 0e 6e   5f 4f 1f

5g 3g 0g   4h 0h 2h   1i 9i 7i
4g 9g 0g   0h 0h 0h   6i 0i 2i
0g 0g 2g   0h 0h 0h   4i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_cols_2_fences():
    puzzle_string = f"""
    wxyz_wing_cols_2_fences.sudoku
    9

6a 3a 2a   8b 0b 0b   1c 0c 0c
7a 1a 5a   2b 6b 0b   8c 4c 0c
4a 8a 9a   0b 5b 0b   6c 2c 0c

1d 5d 8d   7e 2e 6e   9f 3f 4f
2d 4d 6d   0e 0e 0e   7f 8f 0f
9d 7d 3d   0e 0e 8e   2f 0f 6f

3g 2g 1g   0h 7h 0h   4i 6i 8i
5g 6g 7g   0h 8h 0h   3i 9i 2i
8g 9g 4g   6h 3h 2h   5i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_cols_3_fences():
    puzzle_string = f"""
    wxyz_wing_cols_3_fences.sudoku
    9

9a _a 7a   2b 0b 0b   5c 0c 0c
6a 2a _a   5b 7b 8b   1c 9c 0c
_a 5a 1a   0b 0b 0b   0c 0c 7c

0d 9d 0d   0e 4e 0e   7f 0f 0f
0d 0d 0d   3e 0e 5e   0f 0f 9f
0d 0d 2d   7e 9e 0e   0f 5f 0f

0g 0g 0g   0h 0h 0h   8i 3i 5i
0g 6g 0g   4h 5h 0h   9i 7i 1i
0g 0g 0g   0h 0h 7h   4i 6i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_rows_2_fences():
    puzzle_string = f"""
    wxyz_wing_rows_2_fences.sudoku
    9

5a 7a 3a   0b 0b 2b   4c 8c 1c
_a _a 9a   7b 4b 5b   2c 3c 6c
4a 6a 2a   3b 1b 8b   5c 7c 9c

0d 5d 1d   0e 7e 0e   6f 0f 8f
2d 0d 6d   0e 0e 0e   7f 0f 3f
0d 4d 7d   0e 0e 0e   9f 1f 0f

6g 0g 5g   0h 3h 7h   8i 0i 4i
7g 3g 8g   0h 0h 4h   1i 0i 0i
0g 2g 4g   8h 0h 0h   3i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_rows_3_fences():
    puzzle_string = f"""
    wxyz_wing_rows_3_fences.sudoku
    9

8a _a _a   7b 9b 0b   0c 2c 0c
_a 9a 5a   0b 1b 2b   7c 0c 0c
_a 7a 2a   3b 0b 0b   9c 0c 0c

0d 0d 9d   2e 0e 1e   0f 0f 0f
0d 0d 0d   0e 5e 9e   0f 0f 0f
0d 0d 8d   4e 3e 7e   6f 9f 0f

0g 0g 7g   9h 4h 8h   1i 5i 3i
5g 8g 3g   1h 7h 6h   2i 4i 9i
9g 4g 1g   5h 2h 3h   8i 7i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_w_wing_type_d_0():
    puzzle_string = f"""
    w_wing_type_d_0.sudoku
    9

_a _a _a   8b 0b 0b   2c 0c 0c
3a 6a _a   0b 0b 5b   1c 4c 7c
_a _a _a   0b 3b 0b   0c 0c 0c

0d 2d 0d   0e 0e 0e   0f 0f 0f
0d 4d 0d   5e 2e 9e   0f 8f 0f
0d 0d 0d   0e 0e 0e   0f 9f 0f

0g 0g 0g   0h 6h 0h   0i 0i 0i
7g 9g 3g   4h 0h 0h   0i 5i 6i
0g 0g 2g   0h 0h 3h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_w_wing_type_d_6():
    puzzle_string = f"""
    w_wing_type_d_6.sudoku
    9

7a _a 6a   0b 0b 3b   9c 1c 8c
_a _a 9a   0b 0b 6b   7c 0c 0c
_a 5a _a   9b 7b 0b   6c 2c 0c

0d 0d 0d   8e 6e 0e   4f 7f 0f
0d 0d 0d   3e 9e 7e   0f 0f 0f
0d 0d 7d   0e 4e 5e   3f 0f 0f

0g 6g 8g   7h 1h 9h   0i 3i 0i
9g 7g 0g   0h 3h 0h   1i 0i 0i
2g 1g 3g   6h 0h 4h   0i 9i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain():
    puzzle_string = f"""
    xy_chain.sudoku
    9

6a _a _a   1b 9b 5b   0c 3c 2c
2a 1a 3a   7b 0b 8b   5c 0c 9c
_a 9a 5a   0b 0b 2b   1c 0c 0c

0d 3d 1d   4e 0e 7e   0f 0f 0f
4d 0d 6d   5e 0e 9e   0f 0f 3f
0d 0d 9d   0e 0e 3e   4f 8f 0f

3g 0g 7g   9h 5h 1h   6i 2i 0i
9g 6g 2g   0h 7h 4h   0i 0i 0i
1g 5g 0g   0h 0h 6h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain_0():
    puzzle_string = f"""
    xy_chain_0.sudoku
    9

6a _a 1a   3b 9b 8b   2c 5c 0c
9a 5a 2a   4b 7b 1b   6c 8c 3c
_a 3a _a   2b 5b 6b   9c 0c 0c

5d 0d 3d   9e 6e 4e   7f 2f 0f
2d 0d 7d   1e 3e 5e   4f 0f 0f
0d 6d 0d   8e 2e 7e   3f 0f 5f

3g 0g 0g   7h 0h 9h   5i 4i 0i
0g 0g 5g   6h 0h 2h   1i 3i 9i
0g 0g 0g   5h 0h 3h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain_1():
    puzzle_string = f"""
    xy_chain_1.sudoku
    9

5a 7a 1a   3b 2b 4b   8c 9c 6c
9a 6a 3a   0b 0b 8b   7c 2c 4c
_a 8a _a   6b 7b 9b   3c 1c 5c

3d 9d 7d   0e 0e 5e   0f 4f 0f
1d 5d 0d   0e 3e 2e   0f 7f 0f
0d 2d 0d   9e 0e 7e   5f 3f 1f

7g 3g 0g   0h 8h 1h   0i 6i 0i
0g 4g 0g   7h 9h 6h   1i 5i 3i
6g 1g 0g   2h 0h 3h   0i 8i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain_2():
    puzzle_string = f"""
    xy_chain_2.sudoku
    9

_a _a 1a   0b 0b 0b   0c 0c 0c
_a _a 8a   4b 0b 0b   6c 3c 0c
_a 2a 9a   0b 0b 1b   0c 7c 0c

0d 6d 0d   0e 0e 3e   0f 0f 0f
5d 0d 0d   0e 0e 0e   0f 0f 2f
0d 0d 0d   8e 0e 0e   0f 4f 0f

0g 7g 0g   9h 0h 0h   3i 8i 0i
0g 1g 4g   0h 0h 6h   7i 0i 0i
0g 0g 0g   0h 0h 0h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_00():
    puzzle_string = f"""
    xy_wing_00.sudoku
    9

_a _a _a   3b 9b 0b   0c 7c 6c
9a _a _a   0b 0b 0b   2c 8c 0c
8a 3a _a   0b 0b 0b   1c 0c 0c

0d 6d 0d   0e 2e 0e   0f 0f 0f
0d 0d 0d   1e 7e 3e   0f 0f 0f
0d 0d 0d   0e 8e 0e   0f 3f 0f

0g 0g 3g   0h 0h 0h   0i 5i 2i
0g 2g 8g   0h 0h 0h   0i 0i 4i
7g 4g 0g   0h 3h 1h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_cols_2_fences():
    puzzle_string = f"""
    xy_wing_cols_2_fences.sudoku
    9

3a 1a 2a   4b 6b 9b   8c 5c 7c
5a 4a 7a   0b 0b 3b   1c 9c 6c
6a 8a 9a   5b 7b 1b   4c 0c 0c

4d 3d 6d   0e 9e 0e   2f 7f 0f
2d 9d 1d   6e 0e 7e   3f 8f 0f
7d 5d 8d   3e 0e 0e   9f 6f 0f

9g 7g 3g   0h 0h 6h   5i 0i 8i
8g 6g 4g   9h 0h 0h   7i 1i 0i
1g 2g 5g   7h 0h 0h   6i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_north_east_3_fences():
    puzzle_string = f"""
    xy_wing_north_east_3_fences.sudoku
    9

7a _a _a   8b 3b 0b   6c 1c 2c
6a 1a 3a   2b 4b 7b   5c 8c 9c
8a _a _a   1b 0b 6b   3c 4c 7c

0d 8d 6d   0e 0e 0e   0f 5f 3f
5d 9d 7d   6e 1e 3e   8f 2f 4f
3d 0d 0d   5e 8e 0e   0f 7f 6f

0g 6g 8g   9h 0h 0h   0i 3i 5i
4g 7g 5g   3h 6h 8h   2i 9i 1i
9g 3g 0g   0h 0h 0h   0i 6i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_north_west_3_fences():
    puzzle_string = f"""
    xy_wing_north_west_3_fences.sudoku
    9

5a 8a 1a   0b 4b 0b   6c 2c 7c
9a 4a 7a   6b 2b 1b   5c 3c 8c
6a 2a 3a   0b 0b 8b   4c 9c 1c

0d 0d 0d   0e 8e 0e   2f 0f 0f
0d 0d 8d   2e 9e 6e   1f 5f 0f
2d 0d 5d   0e 1e 0e   0f 8f 0f

8g 0g 2g   1h 0h 0h   0i 6i 0i
0g 0g 0g   8h 3h 2h   9i 0i 5i
3g 0g 0g   0h 6h 0h   8i 1i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_rows_2_fences():
    puzzle_string = f"""
    xy_wing_rows_2_fences.sudoku
    9
2a _a _a   3b 5b 4b   0c 0c 1c
4a 8a 6a   9b 1b 7b   3c 2c 5c
1a 5a 3a   2b 6b 8b   9c 7c 4c

7d 0d 0d   0e 2e 6e   0f 9f 0f
0d 2d 0d   0e 9e 0e   7f 1f 0f
9d 0d 0d   1e 7e 0e   0f 4f 2f

5g 0g 0g   7h 3h 2h   4i 0i 0i
3g 4g 2g   6h 8h 9h   1i 5i 7i
0g 0g 0g   5h 4h 1h   2i 3i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_south_east_3_fences():
    puzzle_string = f"""
    xy_wing_south_east_3_fences.sudoku
    9
_a 5a _a   4b 9b 2b   0c 0c 8c
_a 8a 9a   1b 7b 5b   0c 2c 3c
_a _a _a   3b 6b 8b   0c 5c 9c

0d 2d 0d   5e 1e 3e   9f 4f 7f
9d 0d 5d   7e 8e 0e   2f 0f 1f
0d 1d 7d   9e 2e 0e   0f 8f 5f

0g 6g 0g   8h 5h 1h   0i 9i 4i
5g 9g 4g   2h 3h 7h   8i 1i 6i
0g 0g 0g   6h 4h 9h   5i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_south_west_3_fences():
    puzzle_string = f"""
    xy_wing_south_west_3_fences.sudoku
    9
3a 4a 2a   5b 8b 1b   6c 9c 7c
6a 8a 1a   0b 0b 7b   0c 0c 3c
_a 9a _a   6b 0b 3b   0c 1c 0c

8d 0d 6d   0e 0e 4e   2f 0f 1f
0d 1d 9d   8e 7e 0e   3f 6f 4f
4d 0d 3d   1e 6e 0e   0f 8f 9f

0g 6g 0g   0h 0h 9h   1i 3i 0i
1g 0g 0g   0h 0h 8h   9i 0i 6i
9g 3g 0g   2h 1h 6h   0i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_x_chain():
    puzzle_string = f"""
    x_chain.sudoku
    9
7a 2a 3a   1b 6b 0b   0c 0c 0c
6a 5a 8a   0b 2b 4b   0c 0c 0c
1a 4a 9a   5b 0b 7b   2c 6c 0c

0d 6d 1d   0e 5e 3e   0f 2f 0f
3d 0d 5d   2e 7e 0e   6f 0f 4f
0d 7d 2d   6e 0e 0e   5f 3f 0f

2g 1g 7g   0h 0h 5h   0i 9i 6i
0g 3g 4g   7h 9h 6h   1i 0i 2i
0g 0g 6g   0h 1h 2h   3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_x_chain_0():
    puzzle_string = f"""
    x_chain_0.sudoku
    9
    4a 8a _a   1b 0b 0b   0c 9c 7c
    _a 3a _a   0b 0b 2b   0c 1c 0c
    _a _a _a   0b 0b 0b   5c 0c 6c
    
    0d 0d 0d   5e 2e 0e   0f 0f 0f
    7d 0d 0d   6e 0e 1e   0f 0f 8f
    0d 0d 0d   0e 7e 8e   0f 0f 0f
    
    8g 0g 6g   0h 0h 0h   0i 0i 0i
    0g 5g 0g   2h 0h 0h   6i 0i 0i
    9g 4g 0g   0h 0h 5h   0i 7i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


#
# avoidable_rectangle_type1_north_east_in_cols
# _a _a _a   2b 5b 0b   6c 0c 0c
# _a _a 6a   0b 0b 8b   0c 0c 0c
# _a _a _a   7b 0b 9b   0c 0c 1c
#
# 0d 8d 0d   0e 0e 0e   0f 1f 0f
# 1d 2d 5d   0e 0e 0e   3f 9f 6f
# 0d 4d 0d   0e 0e 0e   0f 7f 0f
#
# 2g 0g 0g   9h 0h 3h   0i 0i 0i
# 0g 0g 0g   4h 0h 0h   5i 0i 0i
# 0g 0g 3g   0h 8h 6h   0i 0i 0i
#
# avoidable_rectangle_type1_north_east_in_rows
# _a _a 7a   0b 1b 6b   0c 2c 0c
# _a _a _a   0b 0b 0b   6c 0c 0c
# 8a 5a _a   0b 0b 2b   0c 9c 0c
#
# 7d 0d 0d   0e 2e 9e   0f 5f 0f
# 0d 0d 0d   0e 0e 0e   0f 0f 0f
# 0d 4d 0d   1e 8e 0e   0f 0f 6f
#
# 0g 9g 0g   5h 0h 0h   0i 4i 2i
# 0g 0g 3g   0h 0h 0h   0i 0i 0i
# 0g 8g 0g   9h 4h 0h   7i 0i 0i
#
# avoidable_rectangle_type1_north_west_in_cols
# _a _a 9a   0b 7b 3b   0c 0c 0c
# 2a _a _a   4b 0b 8b   0c 0c 0c
# _a _a _a   6b 0b 0b   9c 0c 0c
#
# 0d 8d 0d   0e 0e 0e   0f 1f 0f
# 9d 4d 5d   0e 0e 0e   7f 3f 2f
# 0d 2d 0d   0e 0e 0e   0f 6f 0f
#
# 0g 0g 7g   0h 0h 1h   0i 0i 0i
# 0g 0g 0g   5h 0h 4h   0i 0i 3i
# 0g 0g 0g   9h 6h 0h   5i 0i 0i
#
# avoidable_rectangle_type1_north_west_in_rows
# _a 8a _a   0b 0b 0b   0c 0c 0c
# 6a 2a _a   0b 0b 4b   0c 0c 0c
# 1a 3a 7a   0b 0b 5b   0c 8c 0c
#
# 3d 5d 0d   2e 0e 0e   0f 1f 0f
# 0d 0d 6d   0e 0e 0e   3f 0f 0f
# 0d 9d 0d   0e 0e 7e   0f 4f 6f
#
# 0g 1g 0g   7h 0h 0h   4i 9i 2i
# 0g 0g 0g   1h 0h 0h   0i 6i 7i
# 0g 0g 0g   0h 0h 0h   0i 5i 0i
#
#
# avoidable_rectangle_type1_south_east_in_cols
# _a 5a 2a   0b 0b 0b   0c 0c 1c
# 6a 9a 1a   0b 3b 0b   8c 0c 0c
# _a 3a _a   0b 0b 0b   0c 0c 0c
#
# 0d 0d 8d   2e 0e 5e   9f 0f 0f
# 0d 1d 0d   0e 0e 0e   0f 8f 0f
# 0d 0d 5d   6e 0e 9e   1f 0f 0f
#
# 0g 0g 0g   0h 0h 0h   0i 1i 0i
# 0g 0g 4g   0h 2h 0h   6i 5i 9i
# 5g 0g 0g   0h 0h 0h   3i 7i 0i
#
#
# avoidable_rectangle_type1_south_east_in_rows
# _a _a _a   3b 0b 2b   0c 1c 0c
# _a _a _a   0b 9b 4b   0c 0c 3c
# 4a 7a _a   0b 0b 0b   0c 0c 2c
#
# 0d 0d 1d   5e 0e 0e   0f 2f 0f
# 0d 0d 7d   0e 1e 0e   8f 0f 0f
# 0d 8d 0d   0e 0e 3e   5f 0f 0f
#
# 5g 0g 0g   0h 0h 0h   0i 6i 9i
# 2g 0g 0g   9h 8h 0h   0i 0i 0i
# 0g 6g 0g   1h 0h 5h   0i 0i 0i
#
# avoidable_rectangle_type1_south_west_in_rows
# 8a 4a _a   0b 0b 7b   0c 0c 0c
# _a _a 3a   0b 0b 5b   0c 0c 6c
# 1a _a 7a   6b 0b 0b   0c 4c 0c
#
# 0d 0d 0d   0e 0e 9e   0f 8f 0f
# 0d 0d 9d   0e 0e 0e   6f 0f 0f
# 0d 7d 0d   3e 0e 0e   0f 0f 0f
#
# 0g 9g 0g   0h 0h 4h   2i 0i 8i
# 5g 0g 0g   7h 0h 0h   9i 0i 0i
# 0g 0g 0g   2h 0h 0h   0i 3i 7i
#
# avoidable_rectangle_type1_0
# _a 6a _a   0b 0b 0b   0c 3c 9c
# _a 8a _a   3b 2b 0b   0c 0c 0c
# 9a _a _a   5b 0b 6b   0c 0c 0c
#
# 2d 0d 0d   0e 0e 4e   6f 0f 0f
# 0d 0d 7d   0e 5e 0e   2f 0f 0f
# 0d 0d 5d   6e 0e 0e   0f 0f 8f
#
# 0g 0g 0g   4h 0h 8h   0i 0i 5i
# 0g 0g 0g   0h 3h 1h   0i 4i 0i
# 7g 1g 0g   0h 0h 0h   0i 8i 0i


def test_sudoku_first_lesson():
    puzzle_string = f"""
    first_lesson.sudoku
    9
    7a 5a 1a 2b 8b 9b 3c 6c 4c
    6a 2a 3a 1b 4b 7b 5c 9c 8c
    9a 4a 8a 3b 5b 6b 1c 2c 7c
    3d 8d 7d 4e 9e 5e 6f 1f 2f
    2d 1d 4d 6e 3e 8e 7f 5f 9f
    5d 9d 6d 7e 2e 1e 4f 8f 3f
    8g 7g 9g 5h 1h 3h 2i 4i 6i
    1g 3g 2g 0h 6h 4h 8i 7i 5i
    4g 6g 5g 8h 7h 2h 9i 3i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_second_lesson_0():
    puzzle_string = f"""
    second_lesson_0.sudoku
    9
    3a 5a 8a 2b 0b 1b 4c 6c 7c
    2a 1a 6a 4b 0b 7b 9c 8c 5c
    4a 9a 7a 8b 0b 5b 2c 1c 3c
    6d 4d 3d 5e 0e 2e 7f 9f 1f
    9d 7d 5d 3e 0e 4e 6f 2f 8f
    1d 8d 2d 9e 0e 6e 5f 3f 4f
    7g 2g 9g 1h 0h 3h 8i 4i 6i
    8g 6g 1g 7h 0h 9h 3i 5i 2i
    5g 3g 4g 6h 0h 8h 1i 7i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_easiest_0():
    puzzle_string = f"""
    easiest_0.sudoku
    9
    _a 3a 1a 8b 0b 2b 5c 9c 4c
    6a _a 8a 9b 0b 4b 0c 2c 7c
    2a 9a 4a 7b 1b 5b 0c 6c 3c
    8d 4d 6d 0e 0e 9e 0f 5f 1f
    3d 0d 9d 2e 5e 1e 4f 0f 6f
    1d 2d 0d 4e 0e 0e 3f 7f 9f
    9g 8g 0g 1h 2h 3h 6i 4i 5i
    5g 1g 0g 6h 0h 7h 9i 0i 8i
    4g 6g 3g 5h 0h 8h 7i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_easy_as_pie_0():
    puzzle_string = f"""
    easy_as_pie_0.sudoku
    9
    _a 4a 6a 8b 0b 1b 2c 0c 7c
    _a 9a 1a 4b 0b 7b 8c 0c 5c
    _a 0a 3a 5b 2b 9b 4c 1c 6c
    4d 0d 0d 2e 0e 0e 0f 7f 8f
    0d 6d 0d 3e 1e 8e 0f 4f 0f
    9d 3d 0d 0e 0e 5e 0f 0f 2f
    6g 8g 4g 1h 7h 2h 9i 0i 0i
    1g 0g 7g 9h 0h 3h 6i 8i 0i
    3g 0g 9g 6h 0h 4h 7i 2i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_picnic_0():
    puzzle_string = f"""
    picnic_0.sudoku
    9
    4a _a 2a 0b 8b 9b 0c 7c 3c
    7a 9a 1a 4b 0b 6b 0c 5c 0c
    _a 0a _a 0b 0b 0b 4c 0c 9c
    8d 1d 7d 0e 0e 5e 0f 0f 0f
    0d 6d 0d 8e 9e 7e 0f 2f 0f
    0d 0d 0d 6e 0e 0e 5f 8f 7f
    3g 0g 5g 0h 0h 0h 0i 0i 0i
    0g 8g 0g 7h 0h 3h 1i 9i 4i
    1g 7g 0g 2h 6h 0h 8i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_picnic_1():
    puzzle_string = f"""
    picnic_1.sudoku
    9
    _a 0a 6a 3b 2b 7b 0c 8c 0c
    4a _a 0a 0b 5b 1b 0c 7c 6c
    _a 2a _a 4b 8b 0b 0c 3c 1c
    0d 3d 1d 0e 0e 0e 8f 2f 7f
    0d 0d 0d 0e 3e 0e 0f 0f 0f
    8d 7d 4d 0e 0e 0e 3f 9f 0f
    9g 4g 0g 0h 7h 5h 0i 6i 0i
    3g 6g 0g 2h 1h 0h 0i 0i 8i
    0g 5g 0g 6h 9h 3h 7i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_picnic_2():
    puzzle_string = f"""
    picnic_2.sudoku
    9
    _a 7a _a 5b 1b 3b 0c 2c 9c
    3a _a 9a 0b 6b 2b 0c 0c 1c
    5a 2a _a 0b 0b 0b 0c 3c 6c
    0d 0d 0d 0e 3e 0e 1f 4f 8f
    4d 0d 0d 0e 2e 0e 0f 0f 7f
    1d 6d 3d 0e 7e 0e 0f 0f 0f
    9g 1g 0g 0h 0h 0h 0i 8i 4i
    8g 0g 0g 4h 9h 0h 5i 0i 2i
    7g 5g 0g 2h 8h 6h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_simple_0():
    puzzle_string = f"""
    simple_0.sudoku
    9
    _a 4a _a 7b 8b 0b 0c 0c 0c
    6a _a 1a 0b 0b 4b 2c 0c 0c
    5a 7a _a 2b 6b 0b 0c 0c 0c
    0d 3d 0d 5e 0e 8e 0f 0f 6f
    1d 0d 0d 0e 0e 0e 0f 0f 7f
    7d 0d 0d 4e 0e 3e 0f 8f 0f
    0g 0g 0g 0h 4h 9h 0i 5i 8i
    0g 0g 6g 8h 0h 0h 3i 0i 2i
    0g 0g 0g 0h 3h 2h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_0():
    puzzle_string = f"""
    mild_0.sudoku
    9
    _a 4a 3a 8b 0b 0b 0c 0c 0c
    5a _a 0a 0b 0b 0b 0c 0c 0c
    2a 1a _a 0b 0b 6b 0c 9c 4c
    4d 2d 0d 9e 0e 0e 6f 3f 0f
    3d 0d 5d 0e 0e 0e 4f 0f 1f
    0d 8d 1d 0e 0e 4e 0f 2f 9f
    8g 7g 0g 4h 0h 0h 0i 6i 5i
    0g 0g 0g 0h 0h 0h 0i 0i 2i
    0g 0g 0g 0h 0h 2h 3i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_1():
    puzzle_string = f"""
    mild_1.sudoku
    9
    4a 3a _a 0b 6b 2b 5c 0c 8c
    _a 0a 2a 4b 7b 0b 0c 6c 0c
    _a 0a _a 0b 0b 0b 4c 0c 0c
    0d 0d 0d 0e 0e 0e 0f 0f 4f
    8d 0d 0d 7e 1e 5e 0f 0f 2f
    1d 0d 0d 0e 0e 0e 0f 0f 0f
    0g 0g 9g 0h 0h 0h 0i 0i 0i
    0g 6g 0g 0h 2h 9h 3i 0i 0i
    2g 0g 4g 1h 8h 0h 0i 9i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_2():
    puzzle_string = f"""
    mild_2.sudoku
    9
    8a 6a _a 0b 5b 0b 0c 0c 0c
    _a 0a _a 0b 0b 3b 8c 1c 6c
    _a 0a _a 0b 1b 0b 0c 0c 0c
    0d 4d 0d 0e 0e 0e 0f 6f 2f
    0d 0d 7d 2e 0e 9e 3f 0f 0f
    2d 8d 0d 0e 0e 0e 0f 5f 0f
    0g 0g 0g 0h 2h 0h 0i 0i 0i
    7g 1g 3g 6h 0h 0h 0i 0i 0i
    0g 0g 0g 0h 9h 0h 0i 3i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_3():
    puzzle_string = f"""
    mild_3.sudoku
    9
    5a 9a _a 4b 6b 0b 0c 0c 1c
    _a 3a 6a 8b 0b 7b 0c 0c 5c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    0d 0d 0d 0e 0e 0e 3f 2f 0f
    0d 0d 0d 7e 4e 9e 0f 0f 0f
    0d 1d 7d 0e 0e 0e 0f 0f 0f
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    2g 0g 0g 6h 0h 8h 1i 7i 0i
    3g 0g 0g 0h 2h 1h 0i 5i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_4():
    puzzle_string = f"""
    mild_4.sudoku
    9
    4a _a 0a 0b 5b 7b 2c 8c 0c
    _a 1a _a 0b 2b 0b 4c 0c 0c
    _a 0a _a 0b 0b 0b 0c 0c 9c
    9d 6d 0d 0e 7e 0e 0f 4f 1f
    0d 7d 0d 0e 0e 0e 0f 3f 0f
    8d 3d 0d 0e 1e 0e 0f 5f 7f
    3g 0g 0g 0h 0h 0h 0i 0i 0i
    0g 0g 8g 0h 6h 0h 0i 2i 0i
    0g 5g 6g 3h 8h 0h 0i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_moderate_0():
    puzzle_string = f"""
    moderate_0.sudoku
    9
    1a _a 2a 0b 0b 0b 4c 0c 0c
    _a 3a 9a 0b 8b 0b 0c 7c 0c
    _a 7a 8a 0b 0b 0b 0c 0c 0c
    7d 0d 0d 8e 0e 6e 0f 0f 1f
    0d 5d 0d 0e 0e 0e 0f 8f 0f
    8d 0d 0d 5e 0e 2e 0f 0f 9f
    0g 0g 0g 0h 0h 0h 8i 6i 0i
    0g 1g 0g 0h 6h 0h 3i 5i 0i
    0g 0g 7g 0h 0h 0h 9i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


def test_sudoku_intricate_0():
    puzzle_string = f"""
    intricate_0.sudoku
    9
    _a _a 1a _b _b _b _c _c _c
    _a _a 8a 5b _b 3b _c _c 9c
    _a _a 9a _b _b _b 2c 5c _c
    0d 0d 0d 6e 0e 0e 0f 0f 1f
    1d 0d 6d 9e 0e 8e 5f 0f 3f
    3d 0d 0d 0e 0e 4e 0f 0f 0f
    0g 4g 3g 0h 0h 0h 1i 0i 0i
    2g 0g 0g 1h 0h 7h 3i 0i 0i
    0g 0g 0g 0h 0h 0h 9i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_1():
    puzzle_string = f"""
    intricate_1.sudoku
    9
    1a 7a _a _b _b 9b 3c 8c 5c
    5a 6a _a _b 3b _b _c _c _c
    8a 3a 9a _b 7b _b 6c _c _c
    0d 2d 0d 0e 5e 3e 4f 0f 8f
    0d 5d 0d 2e 8e 4e 0f 3f 0f
    3d 4d 8d 0e 9e 0e 5f 2f 0f
    4g 8g 5g 9h 1h 7h 2i 6i 3i
    2g 1g 3g 0h 0h 0h 7i 0i 9i
    6g 9g 7g 3h 0h 0h 8i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_2():
    puzzle_string = f"""
    intricate_2.sudoku
    9
    _a 9a _a 6b _b _b _c 7c 3c
    _a _a 7a 3b _b _b 9c _c 8c
    _a _a _a 8b 7b 9b 2c _c 6c
    7d 5d 0d 4e 2e 8e 0f 6f 0f
    2d 0d 0d 7e 0e 0e 0f 8f 4f
    4d 8d 0d 1e 0e 0e 0f 2f 0f
    0g 0g 5g 0h 0h 3h 0i 0i 0i
    0g 0g 4g 0h 0h 7h 8i 0i 0i
    1g 7g 0g 0h 0h 4h 0i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesClaiming()])


def test_sudoku_intricate_3():
    puzzle_string = f"""
    intricate_3.sudoku
    9
    _a 4a 9a _b 7b 3b 5c _c _c
    5a 7a 8a _b 1b 6b _c 3c _c
    _a 3a 1a _b _b 5b _c _c 7c
    4d 1d 2d 5e 3e 8e 0f 7f 0f
    9d 5d 3d 7e 6e 2e 0f 0f 4f
    7d 8d 6d 1e 9e 4e 2f 5f 3f
    8g 0g 5g 3h 4h 0h 7i 6i 0i
    3g 0g 7g 6h 5h 0h 0i 0i 0i
    1g 6g 4g 0h 0h 7h 3i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_4():
    puzzle_string = f"""
    intricate_4.sudoku
    9
    _a 3a 1a _b 7b _b 9c _c 2c
    7a 9a 5a _b _b _b 1c _c 8c
    _a _a 6a _b 1b 9b _c _c 7c
    9d 7d 2d 0e 0e 6e 4f 8f 1f
    6d 4d 3d 7e 8e 1e 0f 0f 9f
    5d 1d 8d 4e 9e 2e 6f 7f 3f
    0g 0g 9g 1h 0h 7h 0i 0i 0i
    3g 0g 4g 9h 0h 8h 7i 1i 0i
    1g 0g 7g 0h 6h 0h 8i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesPointing()])


def test_sudoku_intricate_5():
    puzzle_string = f"""
    intricate_5.sudoku
    9
    6a _a _a 9b _b 7b _c _c _c
    _a _a 7a _b 2b _b _c _c _c
    2a 5a _a 3b _b 1b _c _c _c
    1d 0d 0d 0e 0e 0e 9f 8f 0f
    0d 8d 6d 0e 0e 0e 5f 2f 0f
    0d 2d 4d 0e 0e 0e 0f 0f 3f
    0g 0g 0g 4h 0h 5h 0i 7i 8i
    0g 0g 0g 0h 8h 0h 1i 0i 0i
    0g 0g 0g 6h 0h 3h 0i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()])


def test_sudoku_intricate_6():
    puzzle_string = f"""
    intricate_6.sudoku
    9
    6a _a 5a 8b _b 3b 1c _c 4c
    8a _a _a 4b _b 2b 3c 6c _c
    _a 3a 4a _b 6b 1b 8c 9c _c
    0d 4d 8d 0e 0e 9e 6f 3f 0f
    0d 6d 2d 3e 0e 4e 5f 0f 0f
    0d 0d 3d 6e 0e 0e 4f 0f 0f
    4g 5g 9g 2h 3h 6h 7i 1i 8i
    0g 0g 6g 1h 4h 0h 9i 5i 3i
    3g 0g 0g 9h 0h 5h 2i 4i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_7():
    puzzle_string = f"""
    intricate_7.sudoku
    9
    9a _a _a _b _b _b _c _c _c
    _a 8a _a 7b 3b _b _c 6c 9c
    _a _a _a _b _b 2b _c 7c 1c
    0d 0d 0d 6e 0e 0e 0f 3f 5f
    0d 0d 0d 4e 0e 5e 0f 0f 0f
    2d 6d 0d 0e 0e 8e 0f 0f 0f
    4g 5g 0g 2h 0h 0h 0i 0i 0i
    6g 3g 0g 0h 9h 7h 0i 8i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_8():
    puzzle_string = f"""
    intricate_8.sudoku
    9
    _a 5a _a _b 8b _b _c _c 7c
    1a 3a 7a _b _b 9b _c _c _c
    9a 8a _a 7b _b _b _c _c _c
    0d 4d 0d 2e 1e 8e 0f 5f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 7d 0d 4e 9e 5e 0f 2f 0f
    0g 0g 0g 0h 0h 7h 0i 9i 5i
    0g 0g 0g 6h 0h 0h 2i 4i 3i
    5g 0g 0g 0h 3h 0h 0i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


@pytest.mark.skip("skipped")
def test_difficult_01():
    puzzle_string = f"""
    difficult_01.sudoku
    9
    8a 6a _a   _b 7b _b   _c 3c 4c
    2a 1a 7a   6b 4b 3b   8c 9c 5c
    3a 4a _a   8b _b _b   _c 7c _c

    1d 7d 3d   5e 2e 4e   9f 6f 8f
    4d 9d 6d   3e 8e 7e   5f 1f 2f
    5d 8d 2d   1e 6e 9e   3f 4f 7f

    9g 2g _g   7h 5h 6h   _i 8i 3i
    6g 5g _g   4h 3h _h   7i 2i 9i
    7g 3g _g   _h _h _h   _i 5i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), LockedCandidatesPointing(), LockedCandidatesClaiming(),
                                UniqueRectangleType4(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_difficult_04():
    puzzle_string = f"""
    difficult_04.sudoku
    9

    3a _a 0a   9b 0b 0b   4c 0c 1c
    _a 0a 7a   0b 3b 0b   8c 0c 0c
    _a 0a _a   0b 0b 0b   0c 5c 6c

    0d 0d 0d   8e 5e 4e   0f 0f 0f
    0d 8d 0d   0e 0e 0e   0f 4f 0f
    0d 0d 0d   3e 2e 6e   0f 0f 0f

    9g 7g 0g   0h 0h 0h   0i 0i 0i
    0g 0g 3g   0h 4h 0h   2i 0i 0i
    2g 0g 4g   0h 0h 8h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_05():
    puzzle_string = f"""
    difficult_05.sudoku
    9

    6a 4a _a   0b 0b 0b   9c 8c 2c
    8a _a 0a   0b 0b 0b   0c 0c 0c
    _a 0a 7a   0b 0b 8b   0c 0c 0c

    4d 0d 0d   7e 0e 0e   0f 2f 5f
    0d 0d 8d   2e 0e 1e   3f 0f 0f
    1d 5d 0d   0e 0e 6e   0f 0f 9f

    0g 0g 0g   4h 0h 0h   5i 0i 0i
    0g 0g 0g   0h 0h 0h   0i 0i 8i
    9g 7g 5g   0h 0h 0h   0i 6i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_08():
    puzzle_string = f"""
    difficult_08.sudoku
    9

    _a 0a 8a   0b 1b 4b   0c 0c 3c
    _a 0a _a   0b 0b 0b   0c 8c 0c
    6a 2a _a   0b 0b 7b   9c 0c 4c

    7d 0d 3d   1e 0e 0e   0f 0f 0f
    4d 0d 0d   0e 0e 0e   0f 0f 8f
    0d 0d 0d   0e 0e 9e   5f 0f 7f

    8g 0g 4g   9h 0h 0h   0i 3i 6i
    0g 3g 0g   0h 0h 0h   0i 0i 0i
    5g 0g 0g   6h 4h 0h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_15():
    puzzle_string = f"""
    difficult_15.sudoku
    9

    3a _a 0a   0b 0b 0b   0c 0c 0c
    1a _a 0a   6b 0b 4b   0c 0c 0c
    4a _a 5a   0b 0b 3b   8c 7c 0c

    0d 0d 3d   0e 5e 0e   0f 0f 7f
    0d 0d 0d   0e 0e 0e   0f 0f 0f
    6d 0d 0d   0e 3e 0e   5f 0f 0f

    0g 7g 6g   2h 0h 0h   3i 0i 5i
    0g 0g 0g   1h 0h 8h   0i 0i 4i
    0g 0g 0g   0h 0h 0h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_20():
    puzzle_string = f"""
    difficult_20.sudoku
    9

    _a 0a _a   9b 1b 0b   0c 7c 0c
    _a 0a 4a   0b 5b 7b   2c 8c 0c
    _a 0a _a   0b 0b 6b   0c 9c 0c

    0d 0d 5d   0e 0e 0e   1f 4f 2f
    0d 0d 0d   0e 0e 0e   0f 0f 0f
    8d 2d 6d   0e 0e 0e   7f 0f 0f

    0g 5g 0g   6h 0h 0h   0i 0i 0i
    0g 9g 2g   7h 8h 0h   4i 0i 0i
    0g 3g 0g   0h 9h 1h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_21():
    puzzle_string = f"""
    difficult_21.sudoku
    9

    _a 0a 4a   3b 0b 0b   0c 8c 6c
    _a 2a _a   0b 7b 0b   5c 4c 3c
    _a 3a _a   0b 0b 0b   7c 0c 0c

    0d 0d 5d   0e 0e 7e   4f 0f 0f
    0d 0d 0d   0e 8e 0e   0f 0f 0f
    0d 0d 9d   6e 0e 0e   2f 0f 0f

    0g 0g 7g   0h 0h 0h   0i 6i 0i
    3g 4g 6g   0h 1h 0h   0i 2i 0i
    1g 5g 0g   0h 0h 3h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_31():
    puzzle_string = f"""
    difficult_31.sudoku
    9

    8a 3a 4a   1b 2b 7b   5c 6c 9c
    5a 9a 7a   6b 3b 4b   0c 8c 0c
    1a 2a 6a   5b 8b 9b   7c 4c 3c

    0d 8d 5d   9e 0e 1e   0f 0f 0f
    0d 7d 0d   3e 0e 5e   0f 9f 8f
    9d 6d 0d   2e 0e 8e   0f 5f 0f

    6g 1g 8g   7h 5h 0h   9i 0i 4i
    7g 5g 0g   4h 9h 0h   8i 1i 6i
    0g 4g 9g   8h 1h 6h   0i 7i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_00():
    puzzle_string = f"""
    difficult_00.sudoku
    9
    7a _a 0a 6b 0b 0b 0c 9c 0c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    5a _a 6a 8b 0b 1b 4c 0c 0c
    0d 0d 3d 9e 0e 0e 8f 7f 4f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    9d 2d 4d 0e 0e 3e 5f 0f 0f
    0g 0g 2g 4h 0h 9h 3i 0i 6i
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    0g 8g 0g 0h 0h 7h 0i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_02():
    puzzle_string = f"""
    difficult_02.sudoku
    9
    _a 0a 9a 0b 0b 0b 6c 0c 0c
    _a 7a 4a 0b 0b 1b 0c 0c 0c
    1a _a 0a 4b 0b 0b 0c 0c 0c
    0d 0d 3d 8e 7e 0e 9f 0f 2f
    7d 0d 0d 0e 0e 0e 0f 0f 8f
    4d 0d 2d 0e 6e 3e 7f 0f 0f
    0g 0g 0g 0h 0h 9h 0i 0i 5i
    0g 0g 0g 7h 0h 0h 3i 8i 0i
    0g 0g 1g 0h 0h 0h 2i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_03():
    puzzle_string = f"""
    difficult_03.sudoku
    9
    _a 0a _a 0b 0b 5b 9c 0c 3c
    _a 1a _a 7b 2b 0b 0c 0c 5c
    8a _a 0a 0b 9b 3b 0c 1c 0c
    0d 3d 0d 9e 0e 0e 0f 0f 0f
    0d 0d 4d 0e 0e 0e 3f 0f 0f
    0d 0d 0d 0e 0e 8e 0f 9f 0f
    0g 9g 0g 2h 4h 0h 0i 0i 7i
    5g 0g 0g 0h 7h 9h 0i 6i 0i
    2g 0g 3g 5h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_06():
    puzzle_string = f"""
    difficult_06.sudoku
    9
    1a 8a 5a 3b 4b 7b 9c 6c 2c
    _a 0a _a 0b 0b 0b 0c 0c 3c
    3a 9a _a 1b 0b 0b 0c 0c 8c
    0d 2d 0d 0e 7e 0e 0f 0f 1f
    0d 0d 0d 4e 0e 3e 0f 8f 5f
    5d 3d 0d 0e 1e 0e 0f 9f 7f
    7g 0g 0g 0h 0h 6h 0i 2i 4i
    0g 0g 0g 7h 0h 0h 0i 0i 9i
    0g 0g 3g 2h 8h 0h 5i 7i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_07():
    puzzle_string = f"""
    difficult_07.sudoku
    9
    8a 7a 4a 2b 3b 9b 6c 5c 1c
    3a 5a 2a 1b 6b 7b 9c 4c 8c
    1a 9a 6a 0b 0b 0b 2c 7c 3c
    6d 0d 3d 4e 7e 2e 0f 9f 5f
    7d 2d 5d 9e 1e 8e 4f 3f 6f
    9d 4d 0d 3e 5e 6e 7f 0f 2f
    5g 6g 0g 7h 0h 0h 3i 2i 9i
    4g 0g 9g 0h 2h 3h 5i 0i 7i
    2g 3g 7g 0h 9h 0h 0i 0i 4i
    requires a remote pair
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_09():
    puzzle_string = f"""
    difficult_09.sudoku
    9
    _a 1a _a 7b 8b 0b 6c 0c 0c
    6a 5a _a 0b 0b 0b 0c 0c 8c
    _a 8a 7a 0b 9b 6b 0c 0c 4c
    4d 3d 1d 0e 0e 0e 5f 8f 0f
    7d 2d 8d 0e 4e 0e 0f 0f 3f
    9d 6d 5d 8e 0e 3e 4f 2f 0f
    0g 7g 2g 4h 6h 8h 3i 9i 0i
    8g 4g 3g 0h 5h 0h 0i 0i 0i
    0g 9g 6g 0h 3h 7h 8i 4i 0i
    unique rectangle type 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_10():
    puzzle_string = f"""
    difficult_10.sudoku
    9
    _a 2a _a 1b 0b 4b 0c 7c 0c
    _a 0a _a 0b 0b 7b 0c 0c 2c
    1a _a 0a 2b 0b 0b 4c 0c 6c
    8d 1d 2d 9e 0e 0e 7f 0f 4f
    9d 5d 0d 0e 0e 0e 0f 2f 0f
    3d 0d 6d 0e 0e 2e 9f 0f 0f
    2g 6g 3g 0h 0h 1h 5i 4i 9i
    7g 8g 5g 4h 0h 0h 0i 0i 0i
    4g 9g 1g 5h 0h 6h 0i 0i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_11():
    puzzle_string = f"""
    difficult_11.sudoku
    9
    _a 0a 6a 9b 2b 0b 4c 8c 5c
    _a 8a _a 4b 0b 7b 9c 2c 6c
    _a 4a _a 5b 8b 6b 7c 3c 1c
    0d 6d 0d 1e 7e 2e 0f 4f 0f
    8d 2d 7d 3e 4e 5e 6f 1f 9f
    1d 3d 4d 8e 6e 9e 2f 5f 7f
    0g 9g 3g 0h 0h 8h 0i 6i 4i
    4g 5g 0g 6h 9h 0h 0i 7i 0i
    6g 0g 8g 0h 0h 4h 0i 9i 0i
    Unique Rectangle Type 3
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_12():
    puzzle_string = f"""
    difficult_12.sudoku
    9
    7a _a 0a 0b 0b 0b 0c 0c 0c
    _a 1a _a 4b 0b 6b 0c 0c 0c
    5a 2a _a 0b 0b 3b 0c 6c 0c
    3d 0d 0d 0e 0e 0e 0f 1f 6f
    0d 0d 5d 9e 0e 1e 3f 0f 0f
    8d 6d 0d 0e 0e 0e 0f 0f 2f
    0g 5g 0g 8h 0h 0h 0i 2i 1i
    0g 0g 0g 1h 0h 2h 0i 8i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()])


def test_sudoku_difficult_13():
    puzzle_string = f"""
    difficult_13.sudoku
    9
    4a 7a 2a 1b 5b 3b 0c 0c 9c
    _a 0a _a 7b 8b 6b 3c 2c 4c
    8a 6a 3a 4b 9b 2b 7c 1c 5c
    0d 2d 0d 0e 0e 0e 0f 4f 8f
    0d 0d 6d 9e 4e 8e 2f 0f 0f
    0d 8d 4d 0e 0e 0e 0f 0f 0f
    0g 4g 8g 0h 0h 1h 5i 9i 0i
    0g 9g 1g 5h 7h 4h 0i 0i 2i
    2g 0g 0g 8h 6h 9h 4i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()])


def test_sudoku_difficult_14():
    puzzle_string = f"""
    difficult_14.sudoku
    9
    _a 0a _a 7b 4b 1b 3c 6c 8c
    7a 8a 1a 2b 6b 3b 4c 5c 9c
    3a 4a 6a 9b 8b 5b 7c 2c 1c
    0d 5d 0d 0e 1e 6e 0f 0f 0f
    0d 0d 0d 0e 3e 2e 0f 1f 0f
    1d 0d 0d 5e 9e 7e 0f 4f 0f
    6g 7g 4g 3h 5h 8h 1i 9i 2i
    0g 3g 0g 1h 2h 9h 6i 7i 4i
    2g 1g 9g 6h 7h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_difficult_16():
    puzzle_string = f"""
    difficult_16.sudoku
    9
    _a 9a 4a 6b 2b 0b 0c 8c 1c
    1a 3a 2a 0b 5b 0b 6c 9c 7c
    8a _a 6a 0b 1b 0b 4c 2c 0c
    9d 6d 3d 5e 8e 1e 2f 7f 4f
    2d 8d 5d 0e 4e 0e 1f 3f 6f
    4d 1d 7d 2e 3e 6e 9f 5f 8f
    0g 4g 1g 0h 9h 0h 0i 6i 2i
    3g 0g 8g 1h 6h 2h 0i 4i 9i
    6g 2g 9g 0h 7h 0h 8i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_17():
    puzzle_string = f"""
    difficult_17.sudoku
    9
    8a _a 1a 0b 0b 9b 7c 3c 0c
    6a 5a 3a 8b 7b 1b 9c 2c 4c
    7a 9a _a 0b 3b 0b 1c 8c 0c
    0d 7d 8d 0e 0e 0e 2f 9f 1f
    0d 6d 5d 1e 9e 0e 8f 4f 0f
    9d 1d 0d 0e 8e 0e 6f 5f 0f
    1g 8g 7g 9h 5h 3h 4i 6i 2i
    5g 0g 6g 0h 1h 8h 3i 7i 9i
    0g 3g 9g 7h 0h 0h 5i 1i 8i
    uniqe rec3
    remote pair
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


def test_sudoku_difficult_18():
    puzzle_string = f"""
    difficult_18.sudoku
    9
    3a _a 4a 9b 5b 0b 0c 0c 0c
    _a 9a _a 0b 0b 0b 0c 6c 5c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    9d 3d 0d 2e 0e 0e 0f 0f 4f
    4d 0d 8d 3e 0e 6e 1f 0f 9f
    6d 0d 0d 0e 0e 9e 0f 2f 7f
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    1g 7g 0g 0h 0h 0h 0i 4i 0i
    0g 0g 0g 0h 3h 7h 2i 0i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


def test_sudoku_difficult_19():
    puzzle_string = f"""
    difficult_19.sudoku
    9
    _a 0a _a 0b 0b 0b 8c 5c 2c
    6a _a 0a 4b 0b 0b 3c 0c 0c
    5a _a 0a 0b 9b 0b 0c 0c 0c
    0d 0d 9d 0e 0e 6e 4f 0f 0f
    0d 5d 0d 0e 3e 0e 0f 1f 0f
    0d 0d 7d 1e 0e 0e 6f 0f 0f
    0g 0g 0g 0h 7h 0h 0i 0i 8i
    0g 0g 5g 0h 0h 8h 0i 0i 3i
    1g 4g 8g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_22():
    puzzle_string = f"""
    difficult_22.sudoku
    9
    _a 0a 3a 2b 0b 8b 0c 0c 4c
    6a 4a _a 0b 0b 7b 0c 2c 0c
    _a 0a _a 0b 0b 4b 8c 0c 9c
    0d 2d 0d 0e 0e 0e 0f 4f 0f
    9d 0d 0d 0e 0e 0e 0f 0f 3f
    0d 3d 0d 0e 0e 0e 0f 8f 0f
    3g 0g 5g 8h 0h 0h 0i 0i 0i
    0g 6g 0g 7h 0h 0h 0i 5i 2i
    2g 0g 0g 6h 0h 5h 1i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.XWing()])


def test_sudoku_difficult_23():
    puzzle_string = f"""
    difficult_23.sudoku
    9
    5a 7a _a 0b 0b 2b 8c 0c 0c
    _a 0a _a 0b 3b 0b 7c 0c 0c
    _a 1a _a 0b 0b 6b 0c 3c 0c
    0d 0d 0d 0e 0e 0e 9f 5f 1f
    9d 0d 0d 4e 0e 1e 0f 0f 6f
    1d 8d 5d 0e 0e 0e 0f 0f 0f
    0g 9g 0g 2h 0h 0h 0i 4i 0i
    0g 0g 8g 0h 1h 0h 0i 0i 0i
    0g 0g 2g 5h 0h 0h 0i 9i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()])


def test_sudoku_difficult_24():
    puzzle_string = f"""
    difficult_24.sudoku
    9
    _a 0a _a 5b 0b 1b 0c 7c 0c
    _a 0a 2a 9b 0b 0b 8c 0c 0c
    7a _a 6a 2b 0b 0b 4c 0c 0c
    5d 0d 3d 0e 0e 0e 0f 1f 0f
    0d 0d 0d 3e 0e 5e 0f 0f 0f
    0d 9d 0d 0e 0e 0e 3f 0f 2f
    0g 0g 5g 0h 0h 7h 6i 0i 9i
    0g 0g 4g 0h 0h 2h 5i 0i 0i
    0g 6g 0g 4h 0h 8h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_25():
    puzzle_string = f"""
    difficult_25.sudoku
    9
    _a 8a _a 6b 0b 0b 0c 0c 1c
    4a 7a _a 5b 0b 0b 0c 6c 0c
    _a 0a 3a 0b 0b 9b 0c 0c 0c
    0d 2d 0d 0e 0e 0e 0f 0f 6f
    0d 6d 0d 9e 0e 4e 0f 8f 0f
    5d 0d 0d 0e 0e 0e 0f 3f 0f
    0g 0g 0g 7h 0h 0h 2i 0i 0i
    0g 5g 0g 0h 0h 3h 0i 7i 9i
    8g 0g 0g 0h 0h 2h 0i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesClaiming(), tech.NakedTriple()])


def test_sudoku_difficult_26():
    puzzle_string = f"""
    difficult_26.sudoku
    9
    3a _a 0a 7b 0b 0b 4c 0c 6c
    _a 6a _a 9b 0b 8b 0c 0c 0c
    8a _a 0a 1b 0b 0b 0c 0c 3c
    2d 0d 3d 0e 0e 0e 0f 5f 0f
    0d 0d 0d 3e 0e 2e 0f 0f 0f
    0d 4d 0d 0e 0e 0e 1f 0f 2f
    1g 0g 0g 0h 0h 4h 0i 0i 9i
    0g 0g 0g 5h 0h 3h 0i 7i 0i
    6g 0g 7g 0h 0h 1h 0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_27():
    puzzle_string = f"""
    difficult_27.sudoku
    9
    _a 0a _a 0b 0b 0b 0c 6c 0c
    _a 3a _a 0b 5b 0b 7c 0c 2c
    _a 0a 1a 7b 0b 8b 0c 0c 3c
    0d 9d 0d 0e 0e 0e 0f 0f 7f
    0d 0d 5d 3e 0e 9e 8f 0f 0f
    8d 0d 0d 0e 0e 0e 0f 4f 0f
    9g 0g 0g 4h 0h 1h 6i 0i 0i
    5g 0g 2g 0h 3h 0h 0i 1i 0i
    0g 6g 0g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_28():
    puzzle_string = f"""
    difficult_28.sudoku
    9
    _a 7a _a 9b 0b 0b 0c 6c 0c
    _a 0a _a 0b 0b 5b 4c 0c 0c
    9a _a 4a 1b 7b 0b 0c 0c 0c
    1d 0d 2d 0e 0e 0e 9f 4f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 5d 6d 0e 0e 0e 7f 0f 8f
    0g 0g 0g 0h 6h 2h 1i 0i 5i
    0g 0g 9g 7h 0h 0h 0i 0i 0i
    0g 6g 0g 0h 0h 3h 0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_29():
    puzzle_string = f"""
    difficult_29.sudoku
    9
    7a 3a 4a 0b 2b 0b 1c 5c 6c
    5a 6a 2a 0b 1b 0b 8c 9c 7c
    9a 8a 1a 6b 5b 7b 2c 3c 4c
    4d 1d 6d 0e 3e 5e 0f 2f 0f
    3d 9d 5d 0e 0e 0e 4f 0f 1f
    8d 2d 7d 0e 4e 0e 5f 6f 3f
    6g 4g 9g 5h 7h 0h 3i 1i 0i
    1g 5g 3g 0h 0h 0h 0i 0i 0i
    2g 7g 8g 0h 9h 0h 6i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_30():
    puzzle_string = f"""
    difficult_30.sudoku
    9
    9a 8a 1a 0b 0b 7b 4c 2c 0c
    4a 7a 6a 0b 2b 8b 0c 5c 0c
    3a 2a 5a 0b 0b 0b 0c 8c 7c
    0d 4d 9d 0e 0e 3e 2f 7f 0f
    7d 1d 2d 0e 0e 0e 0f 3f 9f
    0d 6d 3d 2e 7e 9e 0f 4f 0f
    2g 9g 8g 7h 0h 0h 3i 6i 4i
    1g 5g 4g 6h 3h 2h 7i 9i 8i
    6g 3g 7g 8h 9h 4h 5i 1i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_32():
    puzzle_string = f"""
    difficult_32.sudoku
    9
    7a 3a 4a 0b 2b 0b 1c 5c 6c
    5a 6a 2a 0b 1b 0b 8c 9c 7c
    9a 8a 1a 6b 5b 7b 2c 3c 4c
    4d 1d 6d 0e 3e 5e 0f 2f 0f
    3d 9d 5d 0e 0e 0e 4f 0f 1f
    8d 2d 7d 0e 4e 0e 5f 6f 3f
    6g 4g 9g 5h 7h 0h 3i 1i 0i
    1g 5g 3g 0h 0h 0h 0i 0i 0i
    2g 7g 8g 0h 9h 0h 6i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_33():
    puzzle_string = f"""
    difficult_33.sudoku
    9
    9a 8a 1a 0b 0b 7b 4c 2c 0c
    4a 7a 6a 0b 2b 8b 0c 5c 0c
    3a 2a 5a 0b 0b 0b 0c 8c 7c
    0d 4d 9d 0e 0e 3e 2f 7f 0f
    7d 1d 2d 0e 0e 0e 0f 3f 9f
    0d 6d 3d 2e 7e 9e 0f 4f 0f
    2g 9g 8g 7h 0h 0h 3i 6i 4i
    1g 5g 4g 6h 3h 2h 7i 9i 8i
    6g 3g 7g 8h 9h 4h 5i 1i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


def test_sudoku_difficult_34():
    puzzle_string = f"""
    difficult_34.sudoku
    9
    _a 0a _a 6b 0b 7b 0c 5c 4c
    _a 0a _a 0b 8b 0b 9c 0c 0c
    5a _a 0a 4b 0b 0b 6c 7c 0c
    9d 3d 0d 1e 0e 0e 0f 0f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 0d 0d 0e 0e 9e 0f 2f 6f
    0g 5g 7g 0h 0h 1h 0i 0i 8i
    0g 0g 3g 0h 4h 0h 0i 0i 0i
    2g 8g 0g 9h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming(), UniqueRectangleType4(),
                                Bug()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_35():
    puzzle_string = f"""
    difficult_35.sudoku
    9
    _a 0a 2a 0b 0b 9b 0c 0c 0c
    _a 0a 5a 3b 4b 0b 0c 1c 0c
    _a 0a _a 7b 0b 0b 0c 0c 8c
    0d 4d 7d 0e 0e 0e 0f 0f 3f
    3d 0d 9d 1e 0e 4e 6f 0f 5f
    2d 0d 0d 0e 0e 0e 9f 4f 0f
    7g 0g 0g 0h 0h 6h 0i 0i 0i
    0g 5g 0g 0h 1h 7h 3i 0i 0i
    0g 0g 0g 2h 0h 0h 4i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_36():
    puzzle_string = f"""
    difficult_36.sudoku
    9
    _a 0a _a 7b 0b 0b 0c 0c 9c
    _a 1a _a 0b 3b 0b 0c 6c 0c
    3a _a 0a 0b 9b 0b 4c 0c 0c
    0d 0d 3d 6e 0e 0e 2f 4f 0f
    0d 8d 0d 0e 0e 0e 0f 1f 0f
    0d 5d 4d 0e 0e 3e 8f 0f 0f
    0g 0g 1g 0h 2h 0h 0i 0i 5i
    0g 3g 0g 0h 8h 0h 0i 7i 0i
    6g 0g 0g 0h 0h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), LockedCandidatesPointing(), Bug(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_37():
    puzzle_string = f"""
    difficult_37.sudoku
    9
    _a 0a 5a 0b 0b 8b 0c 7c 3c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    _a 7a 2a 4b 0b 0b 1c 0c 0c
    0d 2d 4d 0e 7e 0e 0f 0f 6f
    0d 8d 0d 2e 0e 5e 0f 3f 0f
    5d 0d 0d 0e 4e 0e 7f 1f 0f
    0g 0g 8g 0h 0h 1h 9i 6i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    4g 1g 0g 9h 0h 0h 8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.NakedTriple()])


def test_sudoku_difficult_38():
    puzzle_string = f"""
    difficult_38.sudoku
    9
    _a 4a _a _b _b _b _c _c _c
    2a _a 9a 8b _b _b 7c _c _c
    _a _a _a 7b _b 2b _c 1c _c
    _d 2d 4d 5e _e _e _f 3f _f
    1d 8d _d 2e _e 9e _f 6f 7f
    _d 3d _d _e _e 1e 5f 8f _f
    _g 5g _g 3h _h 7h _i _i _i
    _g _g 2g _h _h 4h 8i _i 3i
    _g _g _g _h _h _h _i 5i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug()])


def test_sudoku_difficult_39():
    puzzle_string = f"""
    difficult_39.sudoku
    9
    _a 3a _a _b 9b _b 8c _c 7c
    8a _a _a 1b _b _b 6c _c 3c
    2a _a _a _b _b 8b _c _c _c
    _d _d 3d _e _e _e 5f _f _f
    6d _d _d _e _e _e _f _f 1f
    _d _d 2d _e _e _e 7f _f _f
    _g _g _g 8h _h _h _i _i 4i
    7g _g 1g _h _h 3h _i _i 8i
    9g _g 5g _h 7h _h _i 1i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_40():
    puzzle_string = f"""
    unique_rectangle_type1_05.sudoku
    9
    _a 4a _a 0b 7b 5b 1c 2c 0c
    5a _a 2a 9b 4b 0b 7c 3c 0c
    _a 0a 7a 2b 0b 0b 4c 9c 5c
    7d 5d 1d 0e 0e 0e 9f 0f 2f
    2d 3d 8d 1e 9e 0e 5f 0f 7f
    4d 9d 6d 5e 2e 7e 8f 1f 3f
    8g 2g 4g 6h 5h 9h 3i 7i 1i
    1g 7g 5g 4h 3h 2h 6i 8i 9i
    0g 6g 0g 7h 1h 8h 2i 5i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_difficult_41():
    puzzle_string = f"""
    unique_rectangle_type2_00.sudoku
    9
    _a 0a _a 0b 0b 0b 0c 0c 0c
    9a _a 2a 7b 0b 0b 0c 0c 0c
    1a 3a _a 0b 0b 0b 9c 5c 0c
    0d 0d 0d 4e 5e 0e 7f 8f 0f
    4d 5d 0d 9e 0e 7e 0f 1f 6f
    0d 6d 8d 0e 1e 2e 0f 0f 0f
    0g 1g 7g 0h 0h 0h 0i 2i 9i
    0g 0g 0g 0h 0h 8h 4i 0i 5i
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_42():
    puzzle_string = f"""
    unique_rectangle_type2_01.sudoku
    9
    _a 0a _a 0b 0b 0b 2c 0c 0c
    7a 5a _a 0b 3b 4b 0c 0c 0c
    3a _a 8a 9b 0b 0b 0c 0c 0c
    0d 0d 6d 0e 7e 0e 0f 8f 0f
    4d 7d 0d 0e 8e 0e 0f 1f 6f
    0d 8d 0d 0e 4e 0e 9f 0f 0f
    0g 0g 0g 0h 0h 6h 3i 0i 2i
    0g 0g 0g 7h 2h 0h 0i 4i 8i
    0g 0g 1g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_43():
    puzzle_string = f"""
    unique_rectangle_type2_02.sudoku
    9
    3a _a 0a 0b 0b 5b 0c 0c 2c
    _a 0a 7a 0b 1b 8b 0c 0c 0c
    _a 9a 5a 4b 0b 6b 3c 0c 0c
    9d 0d 0d 0e 0e 7e 0f 0f 0f
    0d 4d 0d 0e 0e 0e 0f 2f 0f
    0d 0d 0d 1e 0e 0e 0f 0f 4f
    0g 0g 8g 9h 0h 1h 4i 3i 0i
    0g 0g 0g 5h 3h 0h 1i 0i 0i
    7g 0g 0g 6h 0h 0h 0i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_44():
    puzzle_string = f"""
    unique_rectangle_type2_03.sudoku
    9
    _a 0a _a 2b 0b 0b 9c 0c 0c
    8a _a 0a 0b 6b 0b 5c 0c 2c
    7a _a 0a 0b 0b 8b 0c 0c 0c
    2d 0d 1d 5e 0e 0e 0f 0f 0f
    6d 0d 0d 8e 0e 9e 0f 0f 3f
    0d 0d 0d 0e 0e 1e 7f 0f 8f
    0g 0g 0g 7h 0h 0h 0i 0i 5i
    1g 0g 9g 0h 5h 0h 0i 0i 6i
    0g 0g 8g 0h 0h 6h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_45():
    puzzle_string = f"""
    unique_rectangle_type2_04.sudoku
    9
    _a 0a 9a 0b 5b 0b 0c 0c 0c
    _a 4a 3a 0b 0b 0b 8c 0c 0c
    6a _a 0a 0b 0b 9b 0c 0c 4c
    3d 8d 7d 0e 0e 4e 2f 0f 0f
    0d 2d 0d 0e 0e 0e 0f 6f 0f
    0d 0d 5d 2e 0e 0e 9f 3f 7f
    1g 0g 0g 5h 0h 0h 0i 0i 9i
    0g 0g 6g 0h 0h 0h 5i 2i 0i
    0g 0g 0g 0h 1h 0h 6i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_46():
    puzzle_string = f"""
    unique_rectangle_type2_05.sudoku
    9
    _a 0a _a 0b 4b 0b 3c 5c 0c
    _a 0a 8a 0b 0b 1b 0c 6c 0c
    _a 0a 3a 0b 2b 9b 7c 0c 0c
    0d 0d 0d 4e 5e 0e 0f 8f 0f
    0d 0d 0d 2e 0e 3e 0f 0f 0f
    0d 1d 0d 0e 8e 6e 0f 0f 0f
    0g 0g 6g 1h 3h 0h 2i 0i 0i
    0g 4g 0g 8h 0h 0h 5i 0i 0i
    0g 2g 5g 0h 9h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_47():
    puzzle_string = f"""
    unique_rectangle_type2_06.sudoku
    9
    9a 8a _a 0b 0b 4b 0c 7c 0c
    _a 3a 1a 8b 9b 0b 0c 0c 0c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    0d 5d 0d 0e 7e 1e 9f 0f 6f
    4d 0d 0d 5e 0e 9e 0f 0f 1f
    1d 0d 8d 3e 6e 0e 0f 4f 0f
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    0g 0g 0g 0h 3h 6h 2i 1i 0i
    0g 1g 0g 9h 0h 0h 0i 6i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_48():
    puzzle_string = f"""
    unique_rectangle_type2_07.sudoku
    9
    _a 0a _a 4b 0b 0b 0c 0c 2c
    _a 0a _a 0b 7b 8b 0c 0c 4c
    6a _a 0a 3b 0b 0b 0c 9c 0c
    4d 2d 0d 0e 0e 0e 0f 8f 0f
    0d 0d 7d 0e 2e 0e 4f 0f 0f
    0d 1d 0d 0e 0e 0e 0f 5f 6f
    0g 3g 0g 0h 0h 7h 0i 0i 1i
    8g 0g 0g 2h 1h 0h 0i 0i 0i
    2g 0g 0g 0h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_49():
    puzzle_string = f"""
    unique_rectangle_type2_08.sudoku
    9
    _a 3a 4a 0b 7b 8b 2c 5c 6c
    6a _a 5a 2b 4b 0b 0c 3c 7c
    _a 2a _a 5b 6b 3b 0c 1c 4c
    0d 7d 0d 0e 5e 0e 4f 2f 3f
    5d 0d 2d 0e 3e 4e 7f 6f 9f
    3d 4d 0d 0e 2e 7e 5f 8f 1f
    4g 9g 1g 3h 8h 2h 6i 7i 5i
    0g 6g 0g 4h 1h 5h 3i 9i 2i
    2g 5g 3g 7h 9h 6h 1i 4i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_50():
    puzzle_string = f"""
    unique_rectangle_type2_09.sudoku
    9
    5a 4a _a 0b 9b 0b 0c 0c 0c
    _a 9a _a 3b 0b 0b 0c 0c 6c
    _a 0a _a 5b 0b 0b 0c 1c 9c
    9d 0d 3d 6e 0e 0e 5f 0f 0f
    4d 0d 0d 0e 0e 0e 0f 0f 1f
    0d 0d 7d 0e 0e 1e 6f 0f 3f
    1g 2g 0g 0h 0h 5h 0i 0i 0i
    7g 0g 0g 0h 0h 9h 0i 2i 0i
    0g 0g 0g 0h 3h 0h 0i 7i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_51():
    puzzle_string = f"""
    unique_rectangle_type2_10.sudoku
    9
    _a 0a _a 0b 2b 0b 0c 9c 8c
    2a 7a _a 0b 0b 8b 0c 0c 0c
    5a _a 0a 0b 0b 1b 0c 2c 0c
    1d 0d 5d 7e 0e 0e 3f 0f 0f
    7d 0d 0d 0e 0e 0e 0f 0f 9f
    0d 0d 8d 0e 0e 5e 1f 0f 2f
    0g 6g 0g 2h 0h 0h 0i 0i 3i
    0g 0g 0g 8h 0h 0h 0i 6i 7i
    4g 3g 0g 0h 1h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_52():
    puzzle_string = f"""
    unique_rectangle_type2_11.sudoku
    9
    4a 2a 3a 9b 8b 6b 0c 0c 1c
    6a 5a 9a 7b 2b 1b 3c 8c 4c
    7a 8a 1a 5b 3b 4b 0c 0c 2c
    3d 0d 5d 1e 4e 2e 0f 0f 8f
    2d 1d 0d 8e 9e 3e 0f 0f 0f
    9d 4d 8d 6e 5e 7e 1f 2f 3f
    1g 9g 0g 3h 6h 8h 2i 0i 0i
    5g 0g 2g 4h 1h 9h 8i 3i 0i
    8g 3g 0g 2h 7h 5h 0i 1i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_53():
    puzzle_string = f"""
    unique_rectangle_type2_12.sudoku
    9
    3a 1a _a 0b 0b 0b 5c 6c 9c
    7a 6a _a 0b 0b 0b 8c 4c 3c
    4a 9a _a 3b 6b 0b 7c 1c 2c
    6d 8d 7d 2e 0e 0e 4f 9f 1f
    1d 2d 4d 9e 8e 6e 3f 5f 7f
    9d 5d 3d 4e 1e 7e 6f 2f 8f
    8g 4g 6g 0h 0h 2h 0i 3i 5i
    0g 3g 9g 0h 0h 0h 0i 7i 6i
    0g 7g 1g 6h 0h 0h 0i 8i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_54():
    puzzle_string = f"""
    unique_rectangle_type4_00.sudoku
    9
    2a _a 0a 6b 0b 9b 7c 0c 0c
    _a 4a _a 1b 0b 0b 0c 0c 9c
    _a 6a 1a 0b 0b 0b 0c 0c 0c
    0d 0d 0d 9e 0e 0e 3f 6f 0f
    3d 0d 6d 0e 0e 0e 1f 0f 7f
    0d 8d 9d 0e 0e 1e 0f 0f 0f
    0g 0g 0g 0h 0h 0h 2i 5i 0i
    6g 0g 0g 0h 0h 2h 0i 4i 0i
    0g 0g 2g 8h 0h 3h 0i 0i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_55():
    puzzle_string = f"""
    unique_rectangle_type4_01.sudoku
    9
    _a 0a 7a 0b 2b 0b 0c 6c 0c
    _a 4a _a 0b 1b 0b 0c 0c 8c
    _a 6a 3a 7b 0b 0b 4c 1c 0c
    0d 2d 0d 0e 0e 0e 0f 8f 0f
    0d 0d 1d 0e 5e 0e 2f 0f 0f
    0d 5d 0d 0e 0e 0e 0f 4f 0f
    0g 1g 4g 0h 0h 2h 6i 7i 0i
    6g 0g 0g 0h 3h 0h 0i 5i 0i
    0g 7g 0g 0h 4h 0h 8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_56():
    puzzle_string = f"""
    unique_rectangle_type4_02.sudoku
    9
    _a 4a _a 0b 0b 5b 6c 7c 0c
    _a 1a _a 8b 0b 7b 0c 0c 0c
    _a 0a 6a 0b 4b 0b 0c 0c 1c
    0d 3d 0d 2e 0e 0e 0f 0f 0f
    8d 0d 0d 0e 0e 0e 0f 0f 7f
    0d 0d 0d 0e 0e 4e 0f 2f 0f
    9g 0g 0g 0h 2h 0h 3i 0i 0i
    0g 0g 0g 4h 0h 3h 0i 9i 0i
    0g 5g 1g 6h 0h 0h 0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_57():
    puzzle_string = f"""
    unique_rectangle_type4_03.sudoku
    9
    _a 0a 7a 4b 1b 0b 0c 0c 5c
    _a 0a _a 0b 0b 7b 9c 0c 0c
    8a _a 0a 0b 0b 0b 4c 0c 0c
    6d 0d 0d 0e 0e 1e 2f 4f 0f
    4d 0d 1d 0e 2e 0e 5f 0f 3f
    0d 7d 2d 6e 0e 0e 0f 0f 9f
    0g 0g 8g 0h 0h 0h 0i 0i 2i
    0g 0g 3g 9h 0h 0h 0i 0i 0i
    7g 0g 0g 0h 3h 6h 8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_58():
    puzzle_string = f"""
    unique_rectangle_type4_04.sudoku
    9
    _a 3a _a 0b 9b 0b 8c 0c 7c
    8a _a 0a 1b 0b 0b 6c 0c 3c
    2a _a 0a 0b 0b 8b 0c 0c 0c
    0d 0d 3d 0e 0e 0e 5f 0f 0f
    6d 0d 0d 0e 0e 0e 0f 0f 1f
    0d 0d 2d 0e 0e 0e 7f 0f 0f
    0g 0g 0g 8h 0h 0h 0i 0i 4i
    7g 0g 1g 0h 0h 3h 0i 0i 8i
    9g 0g 5g 0h 7h 0h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_59():
    puzzle_string = f"""
    unique_rectangle_type4_05.sudoku
    9
    6a 9a 2a 5b 0b 0b 7c 3c 8c
    5a 3a 8a 2b 9b 7b 4c 6c 1c
    7a _a 0a 3b 8b 6b 5c 9c 2c
    0d 8d 0d 0e 0e 0e 6f 0f 0f
    1d 0d 0d 0e 0e 0e 9f 0f 4f
    0d 0d 5d 0e 0e 0e 1f 8f 0f
    8g 5g 9g 4h 7h 2h 3i 1i 6i
    4g 2g 6g 1h 5h 3h 8i 7i 9i
    3g 0g 0g 0h 6h 0h 2i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


@pytest.mark.skip("skipped")
def test_annoying_00():
    puzzle_string = f"""
    annoying_00.sudoku
    9
    _a 0a _a   0b 0b 5b   0c 6c 0c
    4a _a 5a   0b 2b 0b   7c 1c 0c
    _a 7a _a   8b 0b 0b   0c 0c 3c

    0d 0d 7d   0e 5e 0e   0f 0f 9f
    0d 0d 0d   9e 0e 4e   0f 0f 0f
    9d 0d 0d   0e 6e 0e   1f 0f 0f

    7g 0g 0g   0h 0h 6h   0i 9i 0i
    0g 5g 6g   0h 9h 0h   2i 0i 7i
    0g 3g 0g   1h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_02():
    puzzle_string = f"""
    annoying_02.sudoku
    9
    _a 5a 1a   8b 9b 6b   0c 2c 4c
    _a 9a 6a   0b 2b 4b   0c 8c 0c
    4a 8a 2a   3b 0b 0b   0c 9c 6c

    6d 2d 7d   4e 3e 8e   9f 1f 5f
    5d 4d 3d   6e 1e 9e   2f 7f 8f
    9d 1d 8d   0e 0e 2e   4f 6f 3f

    2g 6g 4g   0h 8h 3h   0i 5i 9i
    8g 7g 0g   0h 4h 0h   6i 3i 0i
    1g 3g 0g   0h 6h 0h   8i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_05():
    puzzle_string = f"""
    annoying_05.sudoku
    9
    6a 8a _a   0b 0b 0b   3c 0c 2c
    2a 5a 3a   7b 0b 6b   1c 0c 0c
    _a 0a _a   2b 8b 3b   6c 5c 0c

    1d 6d 2d   0e 0e 4e   7f 0f 0f
    5d 7d 8d   1e 3e 2e   9f 4f 6f
    4d 3d 9d   8e 6e 7e   5f 2f 1f

    8g 0g 5g   6h 2h 0h   4i 0i 0i
    0g 2g 0g   3h 0h 5h   8i 6i 0i
    3g 0g 6g   0h 7h 8h   2i 1i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_06():
    puzzle_string = f"""
    annoying_06.sudoku
    9
    7a _a 0a   0b 0b 9b   5c 0c 0c
    _a 5a 8a   0b 3b 2b   0c 0c 0c
    9a _a 6a   0b 0b 5b   0c 0c 0c

    5d 0d 0d   0e 9e 0e   0f 0f 0f
    0d 4d 0d   2e 0e 8e   0f 3f 0f
    0d 0d 0d   0e 7e 0e   0f 0f 6f

    0g 0g 0g   1h 0h 0h   4i 0i 9i
    0g 0g 0g   0h 2h 0h   1i 0i 0i
    0g 0g 1g   9h 0h 0h   0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_07():
    puzzle_string = f"""
    annoying_07.sudoku
    9
    3a _a 7a   2b 5b 0b   6c 0c 4c
    _a 0a 5a   0b 0b 0b   0c 7c 3c
    _a 0a _a   0b 7b 3b   0c 8c 5c

    0d 0d 2d   7e 3e 0e   0f 0f 1f
    6d 3d 0d   0e 9e 0e   0f 2f 7f
    5d 7d 0d   0e 0e 2e   3f 0f 0f

    0g 5g 6g   8h 4h 0h   0i 3i 0i
    0g 0g 3g   0h 6h 0h   0i 0i 0i
    8g 9g 4g   3h 2h 1h   7i 5i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_11():
    puzzle_string = f"""
    annoying_11.sudoku
    9
    _a 0a 6a   4b 7b 9b   3c 0c 2c
    9a 3a _a   5b 8b 2b   0c 4c 6c
    _a 2a _a   6b 1b 3b   0c 9c 0c

    0d 6d 0d   0e 0e 7e   4f 0f 0f
    8d 4d 9d   3e 0e 6e   0f 7f 1f
    0d 7d 5d   0e 0e 4e   0f 6f 0f

    6g 9g 0g   7h 4h 5h   0i 0i 0i
    0g 1g 0g   2h 6h 8h   0i 0i 0i
    7g 0g 2g   9h 3h 1h   6i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_13():
    puzzle_string = f"""
    annoying_13.sudoku
    9
    _a 6a 7a   0b 0b 0b   0c 5c 0c
    _a 3a 2a   5b 7b 6b   8c 0c 9c
    5a 8a 9a   0b 1b 0b   0c 7c 6c

    6d 0d 5d   7e 0e 0e   0f 2f 8f
    9d 7d 3d   0e 4e 0e   1f 6f 5f
    8d 2d 0d   6e 0e 0e   7f 0f 3f

    2g 0g 0g   0h 6h 0h   0i 8i 7i
    3g 0g 6g   4h 8h 7h   5i 0i 2i
    7g 0g 8g   0h 0h 0h   6i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_17():
    puzzle_string = f"""
    annoying_17.sudoku
    9
    _a 7a 5a   2b 4b 3b   0c 0c 1c
    3a 2a _a   1b 6b 7b   5c 4c 0c
    4a 6a 1a   0b 0b 0b   3c 2c 7c

    5d 1d 7d   0e 0e 4e   0f 3f 0f
    0d 3d 4d   0e 0e 1e   9f 7f 5f
    0d 8d 0d   7e 3e 5e   0f 1f 4f

    7g 9g 3g   4h 0h 0h   1i 0i 2i
    0g 4g 2g   0h 1h 0h   7i 0i 3i
    1g 5g 0g   3h 7h 2h   4i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_22():
    puzzle_string = f"""
    annoying_22.sudoku
    9
    _a 3a 4a   5b 0b 0b   0c 0c 0c
    _a 0a 6a   9b 0b 3b   4c 0c 7c
    5a _a 0a   0b 6b 4b   0c 0c 0c

    0d 9d 0d   0e 0e 0e   0f 0f 0f
    4d 0d 2d   0e 7e 0e   9f 0f 1f
    0d 0d 0d   0e 0e 0e   0f 2f 0f

    0g 0g 0g   6h 2h 0h   0i 0i 8i
    1g 0g 8g   7h 0h 9h   3i 0i 0i
    0g 0g 0g   0h 0h 8h   2i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_23():
    puzzle_string = f"""
    annoying_23.sudoku
    9
    _a 6a _a   0b 9b 0b   0c 3c 0c
    _a 0a _a   0b 0b 8b   0c 0c 1c
    _a 0a 7a   0b 6b 0b   2c 0c 0c

    2d 4d 0d   0e 0e 6e   7f 8f 0f
    0d 0d 0d   5e 0e 3e   0f 0f 0f
    0d 8d 9d   2e 0e 0e   0f 1f 5f

    0g 0g 4g   0h 5h 0h   1i 0i 0i
    9g 0g 0g   4h 0h 0h   0i 0i 0i
    0g 5g 0g   0h 3h 0h   0i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_25():
    puzzle_string = f"""
    annoying_25.sudoku
    9
    6a _a 0a   0b 8b 0b   0c 2c 9c
    _a 0a _a   0b 2b 6b   8c 7c 0c
    _a 0a 4a   0b 0b 3b   0c 0c 0c

    0d 4d 0d   0e 0e 0e   0f 0f 1f
    0d 0d 3d   0e 0e 0e   5f 0f 0f
    9d 0d 0d   0e 0e 0e   0f 3f 0f

    0g 0g 0g   7h 0h 0h   2i 0i 0i
    0g 2g 9g   6h 3h 0h   0i 0i 0i
    5g 7g 0g   0h 9h 0h   0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_26():
    puzzle_string = f"""
    annoying_26.sudoku
    9
    _a 7a _a   4b 2b 8b   0c 0c 1c
    _a 0a 3a   0b 0b 0b   0c 0c 0c
    2a 8a _a   0b 1b 0b   0c 0c 0c

    6d 0d 0d   0e 5e 0e   0f 0f 0f
    0d 0d 5d   3e 0e 4e   2f 0f 0f
    0d 0d 0d   0e 6e 0e   0f 0f 4f

    0g 0g 0g   0h 4h 0h   0i 9i 5i
    0g 0g 0g   0h 0h 0h   8i 0i 0i
    9g 0g 0g   5h 3h 2h   0i 6i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_27():
    puzzle_string = f"""
    annoying_27.sudoku
    9
    _a 0a _a   9b 8b 0b   4c 0c 0c
    2a _a 0a   0b 0b 0b   0c 0c 0c
    _a 0a _a   0b 5b 4b   9c 7c 0c

    8d 3d 0d   0e 0e 2e   0f 0f 9f
    0d 4d 1d   0e 0e 0e   7f 2f 0f
    9d 0d 0d   8e 0e 0e   0f 4f 5f

    0g 2g 6g   4h 1h 0h   0i 0i 0i
    0g 0g 0g   0h 0h 0h   0i 0i 4i
    0g 0g 8g   0h 3h 9h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_28():
    puzzle_string = f"""
    annoying_28.sudoku
    9
    5a _a 0a   0b 4b 6b   0c 0c 0c
    1a _a 0a   3b 5b 2b   8c 7c 0c
    _a 2a _a   0b 0b 0b   0c 0c 0c

    8d 0d 0d   5e 0e 3e   9f 0f 0f
    0d 0d 0d   0e 0e 0e   0f 0f 0f
    0d 0d 5d   6e 0e 1e   0f 0f 7f

    0g 0g 0g   0h 0h 0h   0i 4i 0i
    0g 3g 8g   1h 7h 9h   0i 0i 6i
    0g 0g 0g   4h 6h 0h   0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_29():
    puzzle_string = f"""
    annoying_29.sudoku
    9
    _a 0a _a   0b 8b 0b   1c 0c 0c
    _a 0a 3a   0b 0b 0b   6c 0c 5c
    9a 1a _a   0b 0b 0b   0c 4c 0c

    0d 4d 0d   0e 9e 0e   0f 0f 7f
    0d 9d 0d   1e 0e 5e   0f 2f 0f
    2d 0d 0d   0e 6e 0e   0f 9f 0f

    0g 7g 0g   0h 0h 0h   0i 5i 4i
    4g 0g 8g   0h 0h 0h   7i 0i 0i
    0g 0g 9g   0h 5h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_30():
    puzzle_string = f"""
    annoying_30.sudoku
    9
    _a 7a 5a   6b 0b 0b   0c 0c 0c
    2a _a 0a   0b 0b 0b   8c 0c 0c
    1a _a 3a   0b 0b 8b   0c 0c 2c

    0d 1d 0d   2e 0e 9e   0f 0f 0f
    0d 0d 8d   0e 0e 0e   5f 0f 0f
    0d 0d 0d   1e 0e 6e   0f 3f 0f

    5g 0g 0g   4h 0h 0h   1i 0i 6i
    0g 0g 6g   0h 0h 0h   0i 0i 9i
    0g 0g 0g   0h 0h 2h   7i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_32():
    puzzle_string = f"""
    annoying_32.sudoku
    9
    _a 7a 5a   2b 0b 0b   1c 0c 0c
    _a 9a 3a   6b 0b 1b   8c 0c 0c
    _a 0a 4a   0b 0b 0b   0c 0c 0c

    0d 1d 0d   0e 0e 4e   0f 0f 0f
    0d 0d 9d   5e 0e 2e   4f 0f 0f
    0d 0d 0d   8e 0e 0e   0f 3f 0f

    0g 0g 0g   0h 0h 0h   3i 0i 0i
    0g 0g 2g   3h 0h 9h   7i 1i 0i
    0g 0g 8g   0h 0h 7h   6i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_33():
    puzzle_string = f"""
    annoying_33.sudoku
    9
    _a 4a _a   0b 0b 0b   0c 0c 0c
    6a 5a _a   0b 3b 0b   0c 0c 1c
    _a 0a _a   8b 0b 0b   2c 0c 0c

    0d 3d 0d   0e 2e 0e   9f 0f 0f
    0d 2d 9d   3e 0e 4e   6f 5f 0f
    0d 0d 7d   0e 6e 0e   0f 3f 0f

    0g 0g 4g   0h 0h 6h   0i 0i 0i
    7g 0g 0g   0h 8h 0h   0i 9i 6i
    0g 0g 0g   0h 0h 0h   0i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_35():
    puzzle_string = f"""
    annoying_35.sudoku
    9
    _a 5a 9a   0b 0b 0b   0c 0c 0c
    8a _a 0a   0b 0b 0b   0c 7c 1c
    _a 0a _a   0b 0b 8b   2c 5c 0c

    6d 0d 0d   0e 3e 0e   7f 0f 0f
    7d 8d 0d   6e 0e 1e   0f 4f 5f
    0d 0d 4d   0e 7e 0e   0f 0f 8f

    0g 2g 3g   1h 0h 0h   0i 0i 0i
    5g 7g 0g   0h 0h 0h   0i 0i 3i
    0g 0g 0g   0h 0h 0h   1i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_01():
    puzzle_string = f"""
    annoying_01.sudoku
    9
    9 4 2 5 6 1 7 8 3
    . 8 . 7 . 4 . . 1
    1 . 7 . 8 . 5 4 .
    8 . . 1 . 9 . 7 .
    . . . 6 . 7 . . 8
    7 9 . 3 . 8 . . 4
    . . 9 4 . . 8 . 7
    . 7 . 8 . 5 4 3 .
    4 . 8 . 7 . . 1 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_03():
    puzzle_string = f"""
    annoying_03.sudoku
    9
    2 4 9 5 3 7 1 6 8
    7 1 . . 2 8 . 3 4
    . . . . 4 1 2 . 7
    . 9 2 1 7 . 8 4 3
    4 3 7 8 9 2 6 1 5
    . . 1 3 . 4 7 2 9
    1 . . 4 8 . . 7 2
    . 7 4 2 1 . . 8 6
    . 2 . 7 . 3 4 . 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_04():
    puzzle_string = f"""
    annoying_04.sudoku
    9
    . 5 4 . . 6 7 . .
    3 . . . . . . 6 .
    6 . 7 2 . . . . .
    . 6 . . 8 9 1 . 5
    8 . 9 5 . 2 6 . 7
    4 . 5 6 3 . 8 2 9
    . . . . 6 4 9 . .
    . . . . 2 . . . 6
    . . 6 9 . . 2 8 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_08():
    puzzle_string = f"""
    annoying_08.sudoku
    9
    . 5 2 8 . . . 4 .
    . 3 4 2 . . . 7 9
    . 7 6 1 . . . 2 5
    . 1 9 . 8 . . 5 .
    . 2 7 9 3 . 4 1 8
    . 4 8 . 1 . 9 6 .
    2 8 . . . 1 . 9 4
    4 9 1 . 2 8 5 3 .
    7 6 . . . 9 2 8 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_09():
    puzzle_string = f"""
    annoying_09.sudoku
    9
    . 5 . 8 3 . 7 . 6
    8 . 7 4 . 1 3 . .
    3 . 2 7 5 . . 8 .
    . . . . . . 8 . .
    . 3 . 9 . 5 . 7 .
    . . 5 . . . . . .
    . . . . 9 . 5 3 7
    5 . 3 1 . 7 2 . 8
    7 . . 5 . 3 . 4 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_10():
    puzzle_string = f"""
    annoying_10.sudoku
    9
    3 4 . . 2 . 1 7 .
    2 . 9 1 . 4 3 5 8
    . . 1 . . 3 2 4 .
    . . . 6 3 5 4 1 2
    1 2 3 4 9 7 6 8 5
    4 . . 8 1 2 9 3 7
    . 3 . 2 . 1 . . 4
    6 . 4 3 . . 5 2 1
    . 1 2 . 4 . . . 3
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_12():
    puzzle_string = f"""
    annoying_12.sudoku
    9
    5 . 2 . 6 9 3 7 8
    9 3 8 . . 5 6 4 1
    6 . 7 3 8 . 2 5 9
    1 8 4 6 5 . . . 2
    2 6 5 . . . 4 8 .
    3 7 9 . . 8 1 6 5
    4 5 1 . . 2 8 . 6
    7 9 3 8 1 6 5 2 4
    8 2 6 5 . . . 1 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_14():
    puzzle_string = f"""
    annoying_14.sudoku
    9
    9 . . 2 . 7 . 6 .
    . . . . . . 9 . .
    . . 7 9 4 6 . . 1
    8 2 . 4 . . . 9 .
    5 7 9 8 1 . 4 . 6
    . 3 4 . . 9 . 8 .
    4 . . 7 9 8 2 . .
    . . 8 . . . . 4 9
    . 9 . 3 . 4 . . .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_15():
    puzzle_string = f"""
    annoying_15.sudoku
    9
    4 3 5 1 8 9 . . .
    6 9 7 2 4 5 3 8 1
    1 2 8 6 3 7 4 5 9
    3 8 . . . 1 . 9 .
    9 . 1 . 2 3 8 . 4
    7 . . . . 8 1 3 .
    2 1 3 . . 6 7 4 8
    5 7 6 8 1 4 9 2 3
    8 4 9 3 7 2 5 1 6
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_16():
    puzzle_string = f"""
    annoying_16.sudoku
    9
    4 1 7 9 8 2 5 6 3
    8 5 2 6 . . 9 7 1
    3 6 9 1 5 7 4 8 2
    5 7 1 4 6 . 3 2 .
    6 . 4 5 . . . . 7
    . 3 8 . . 1 6 5 4
    . 8 5 . 1 . 7 . 6
    1 4 6 . . 5 . . .
    7 . 3 8 . 6 . . 5
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_18():
    puzzle_string = f"""
    annoying_18.sudoku
    9
    . . 7 . . . . . .
    4 . 9 1 7 . 5 . .
    2 . 8 . 6 . 9 . 7
    . . . 4 . 6 . . .
    6 . 5 2 . 8 7 . 9
    . . . 7 . 5 . . .
    1 . 3 6 5 . 8 . 2
    . . 6 . . 7 3 . 1
    . . . . . 1 6 . .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_19():
    puzzle_string = f"""
    annoying_19.sudoku
    9
    . . . . 3 . . 7 .
    7 . 8 1 . 6 . . .
    3 . 1 . . . 8 . .
    9 . . 3 . 2 . . .
    . 3 . . . . . 4 .
    . . . 6 . 5 . . 9
    . . 4 . . . 9 . 3
    . . 3 2 . 4 7 . 5
    . 8 . . 5 3 . . .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_20():
    puzzle_string = f"""
    annoying_20.sudoku
    9
    4..|9..|.7.
    .76|.85|...
    ..5|...|...
    ---+---+---
    1.4|2..|...
    .8.|1.9|.5.
    ...|..3|4.1
    ---+---+---
    ...|...|7..
    ...|36.|59.
    .2.|..7|..8
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_21():
    puzzle_string = f"""
    annoying_21.sudoku
    9
    .4.|2.5|.3.
    8..|97.|4..
    ...|...|.92
    ---+---+---
    ..4|...|.78
    ...|...|...
    71.|...|3..
    ---+---+---
    58.|...|...
    ..2|.13|..5
    .9.|8.6|.2.
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_24():
    puzzle_string = f"""
    annoying_24.sudoku
    9
    6..|5..|2..
    7..|..6|.49
    .9.|4.7|3..
    ---+---+---
    .3.|...|62.
    4..|...|..7
    .26|...|.3.
    ---+---+---
    ..1|3.5|.8.
    37.|1..|..6
    ..2|..9|..3
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_31():
    puzzle_string = f"""
    annoying_31.sudoku
    9
    ..5|8.4|.31
    3..|.5.|...
    ..9|.6.|.5.
    ---+---+---
    9..|..7|..8
    5..|...|..2
    2..|5..|..9
    ---+---+---
    .9.|.1.|8..
    ...|.8.|..7
    86.|9.3|4..
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_36():
    puzzle_string = f"""
    annoying_36.sudoku
    9
    ...|...|..3
    .4.|..3|1.5
    .1.|4..|69.
    ---+---+---
    8..|9.4|...
    .57|...|46.
    ...|7.6|..2
    ---+---+---
    .89|..1|.5.
    5.1|3..|.8.
    7..|...|...
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_1():
    puzzle_string = f"""
    devious_1.sudoku
    9
    _a 0a 3a   9b 0b 4b   0c 0c 0c
    5a _a 4a   2b 3b 0b   0c 0c 0c
    _a 8a _a   0b 0b 0b   0c 0c 5c

    0d 0d 0d   0e 4e 0e   3f 5f 0f
    3d 0d 0d   0e 0e 0e   0f 0f 6f
    0d 1d 2d   0e 6e 0e   0f 0f 0f

    6g 0g 0g   0h 0h 0h   0i 1i 0i
    0g 0g 0g   0h 1h 3h   6i 0i 9i
    0g 0g 0g   5h 0h 6h   8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_2():
    puzzle_string = f"""
    devious_2.sudoku
    9
    _a 0a _a   0b 0b 0b   7c 0c 0c
    _a 8a _a   0b 0b 6b   0c 0c 1c
    9a 7a _a   0b 0b 0b   0c 5c 3c

    0d 0d 8d   2e 0e 0e   3f 6f 0f
    0d 0d 0d   7e 0e 4e   0f 0f 0f
    0d 5d 3d   0e 0e 8e   4f 0f 0f

    4g 9g 0g   0h 0h 0h   0i 2i 8i
    6g 0g 0g   1h 0h 0h   0i 7i 0i
    0g 0g 7g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_3():
    puzzle_string = f"""
    devious_3.sudoku
    9
    1a _a 0a   7b 0b 0b   0c 0c 0c
    _a 2a _a   9b 0b 5b   0c 6c 0c
    _a 0a 9a   0b 0b 0b   8c 0c 0c

    6d 7d 0d   0e 0e 4e   9f 0f 8f
    0d 0d 8d   0e 0e 0e   2f 0f 0f
    2d 0d 1d   8e 0e 0e   0f 7f 6f

    0g 0g 3g   0h 0h 0h   6i 0i 0i
    0g 4g 0g   1h 0h 8h   0i 3i 0i
    0g 0g 0g   0h 0h 7h   0i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_4():
    puzzle_string = f"""
    devious_4.sudoku
    9
    _a 0a _a   6b 7b 5b   2c 0c 0c
    _a 0a _a   0b 2b 0b   0c 0c 8c
    _a 3a _a   4b 0b 1b   0c 0c 0c

    0d 7d 5d   0e 4e 0e   6f 8f 0f
    0d 0d 6d   0e 0e 0e   3f 0f 0f
    0d 4d 9d   0e 1e 0e   7f 2f 0f

    0g 0g 0g   7h 0h 4h   0i 9i 0i
    4g 0g 0g   0h 3h 0h   0i 0i 0i
    0g 0g 1g   2h 6h 8h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_5():
    puzzle_string = f"""
    devious_5.sudoku
    9
    _a 0a 8a   0b 0b 7b   0c 0c 0c
    3a _a 0a   6b 0b 0b   0c 8c 0c
    _a 0a 5a   1b 8b 0b   0c 4c 0c

    0d 0d 4d   0e 7e 0e   0f 6f 1f
    0d 0d 6d   0e 0e 0e   3f 0f 0f
    9d 1d 0d   0e 4e 0e   8f 0f 0f

    0g 5g 0g   0h 3h 8h   9i 0i 0i
    0g 2g 0g   0h 0h 1h   0i 0i 3i
    0g 0g 0g   7h 0h 0h   6i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_6():
    puzzle_string = f"""
    devious_6.sudoku
    9

    6a _a 0a   0b 0b 3b   5c 0c 0c
    8a _a 0a   4b 0b 0b   0c 0c 3c
    _a 5a 2a   0b 6b 0b   0c 0c 0c

    0d 0d 0d   0e 0e 9e   2f 0f 4f
    5d 7d 0d   0e 2e 0e   0f 9f 6f
    2d 0d 8d   6e 0e 0e   0f 0f 0f

    0g 0g 0g   0h 1h 0h   7i 4i 0i
    7g 0g 0g   0h 0h 8h   0i 0i 5i
    0g 0g 5g   7h 0h 0h   0i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_7():
    puzzle_string = f"""
    devious_7.sudoku
    9

    _a 0a 6a   0b 0b 4b   0c 0c 0c
    8a _a 0a   0b 0b 6b   0c 0c 0c
    _a 9a _a   5b 0b 0b   1c 8c 0c

    0d 7d 0d   0e 2e 0e   0f 0f 0f
    6d 3d 1d   0e 0e 0e   7f 2f 9f
    0d 0d 0d   0e 9e 0e   0f 3f 0f

    0g 2g 3g   0h 0h 7h   0i 1i 0i
    0g 0g 0g   2h 0h 0h   0i 0i 5i
    0g 0g 0g   1h 0h 0h   2i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_8():
    puzzle_string = f"""
    devious_8.sudoku
    9

    3a _a 0a   0b 0b 9b   0c 0c 0c
    _a 5a 9a   8b 0b 0b   1c 0c 0c
    _a 1a _a   0b 5b 0b   4c 9c 0c

    0d 4d 0d   2e 0e 0e   0f 5f 0f
    0d 0d 0d   5e 0e 8e   0f 0f 0f
    0d 6d 0d   0e 0e 3e   0f 4f 0f

    0g 3g 6g   0h 8h 0h   0i 2i 0i
    0g 0g 5g   0h 0h 2h   9i 1i 0i
    0g 0g 0g   7h 0h 0h   0i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fiendish_0():
    puzzle_string = f"""
    fiendish_0.sudoku
    9

    _a 8a _a   3b 0b 0b   0c 0c 0c
    _a 6a _a   0b 4b 2b   0c 0c 8c
    3a _a 0a   8b 0b 0b   5c 4c 0c

    0d 3d 0d   0e 0e 0e   0f 0f 9f
    0d 4d 0d   1e 0e 8e   0f 7f 0f
    7d 0d 0d   0e 0e 0e   0f 2f 0f

    0g 2g 7g   0h 0h 4h   0i 0i 5i
    8g 0g 0g   2h 3h 0h   0i 6i 0i
    0g 0g 0g   0h 0h 9h   0i 8i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_diabolical_0():
    puzzle_string = f"""
    diabolical_0.sudoku
    9

    _a 0a _a   4b 0b 0b   7c 0c 0c
    _a 2a _a   0b 0b 6b   0c 1c 0c
    _a 0a _a   0b 3b 0b   0c 4c 2c

    3d 5d 2d   9e 0e 0e   0f 0f 7f
    4d 0d 0d   0e 0e 0e   0f 0f 9f
    9d 0d 0d   0e 0e 8e   3f 6f 4f

    8g 6g 0g   0h 7h 0h   0i 0i 0i
    0g 4g 0g   1h 0h 0h   0i 7i 0i
    0g 0g 7g   0h 0h 5h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_nightmare_0():
    puzzle_string = f"""
    nightmare_0.sudoku
    9

    4a 5a 3a   7b 0b 9b   2c 0c 6c
    _a 0a 1a   0b 0b 0b   0c 0c 3c
    8a _a 0a   0b 0b 0b   0c 4c 0c

    5d 0d 8d   4e 0e 0e   0f 7f 0f
    0d 4d 0d   0e 0e 0e   0f 3f 0f
    0d 7d 0d   0e 0e 2e   4f 0f 5f

    0g 2g 0g   0h 0h 0h   0i 0i 4i
    6g 0g 0g   0h 0h 0h   3i 0i 0i
    7g 0g 4g   5h 0h 6h   8i 2i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@pytest.mark.skip("skipped")
def test_maelstrom_0():
    puzzle_string = f"""
    maelstrom_0.sudoku
    9

    4a _a 0a   0b 0b 0b   0c 6c 0c
    _a 0a 7a   0b 8b 0b   5c 0c 3c
    3a 2a _a   0b 9b 0b   7c 0c 0c

    9d 0d 0d   0e 5e 8e   0f 0f 0f
    0d 0d 0d   9e 0e 1e   0f 0f 0f
    0d 0d 0d   6e 2e 0e   0f 0f 5f

    0g 0g 6g   0h 7h 0h   0i 1i 4i
    8g 0g 1g   0h 6h 0h   3i 0i 0i
    0g 7g 0g   0h 0h 0h   0i 0i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, sudoku_techniques())


@mark.skip("EXPLICITLY")
def test_ur3_north_row():
    actual = \
        f"""
        123_a 12_4a   __34b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        12__c 12__c   ____d ____d
        """

    expected = \
        f"""
        123_a 12_4a   __34b 12__b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        12__c 12__c   ____d ____d
        """
    if solve(actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_xy_chain_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 12__a   ____b _23_b

        ____c ____c   ____d ____d
        1__4c ____c   ____d __34d
        """

    expected = \
        f"""
        _234a ____a   ____b ____b
        _234a 12__a   ____b _23_b

        ____c _234c   ____d ____d
        1__4c _234c   ____d __34d
        """
    if solve(4, actual, expected, tech.XyChain()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_xyz_wing_fences2_row_chute():
    actual = \
        f"""
        ____a 123_a   1_3_b ____b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        12_4a 123_a   1_3_b ____b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_wxyz_fences2_south():
    actual = \
        f"""
        _234a 1__4a   ____b ____b
        ____a 1_3_a   ____b ____b

        ____c ____c   ____d ____d
        2_4_c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a 1__4a   ____b ____b
        123_a 1_3_a   ____b ____b

        ____c ____c   ____d ____d
        2_4_c ____c   ____d ____d
        """
    if solve(4, actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_wxyz_fences2_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        _23_a ____a   ____b ____b

        12__c 1__4c   ____d ____d
        ____c __34c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        _23_a ____a   ____b ____b

        12__c 1__4c   ____d ____d
        12_4c __34c   ____d ____d
        """
    if solve(4, actual, expected, WxyzWing()):
        return
    assert False
