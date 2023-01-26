from colorama import Fore

from Loc import Loc
from puzzles import Sudoku
from techniques.UniqueRectangleType1 import UniqueRectangleType1
import numpy

from techniques.UniqueRectangleType2 import UniqueRectangleType2


def grid_fence(length, string: str) -> tuple[numpy.ndarray, numpy.ndarray]:
    newcan = "".join(str(num + 1) for num in range(length))

    underscore = "".join('_' for num in range(length))

    string = string.replace('\n', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1) \
        .replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace(underscore, newcan).strip()

    temp = numpy.array(string.split(' '), str).reshape((length, length))

    grid = numpy.empty([length, length], dtype=object)
    fences = numpy.empty([length, length], dtype=object)

    if not temp[0][0][::-1][0].isalpha():
        fences = None

    for r in range(length):
        for c in range(length):
            grid[r][c] = set([int(char) for char in temp[r][c] if char.isnumeric()])

            if fences is not None:
                fences[r][c] = [char for char in temp[r][c] if char.isalpha()][0]

    return grid, fences


# def solve(length, actual, expected, technique) -> bool:
#     __grid_act, __fence_act = grid_fence(length, actual)
#     __grid_exp, __fence_exp = grid_fence(length, expected)
#
#     technique.solve_grid(length, __grid_act, __fence_act)
#
#     print(__grid_act)
#     print(__fence_act)
#
#     return False


# actual0 = \
#     f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
# from colorama import Fore
#
#
# def test_sudoku_4x4_():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_3x2():
#     actual = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_2x3():
#     actual = \
#         f"""
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_w_wing():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_almost_locked_candidates_claiming_row():
#     actual = \
#         f"""
#         __34a 12__a   ____b ____b
#         ____a ____a   12__b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         __34a 12__a   ____b ____b
#         ____a ____a   12__b __34b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_almost_locked_candidates_pointing_row():
#     actual = \
#         f"""
#         ____a 12__a   ____b ____b
#         ____a ____a   12__b __34b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         __34a 12__a   ____b ____b
#         ____a ____a   12__b __34b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_ur3_north_row():
#     actual = \
#         f"""
#         123_a 12_4a   __34b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         12__c 12__c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         123_a 12_4a   __34b 12__b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         12__c 12__c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_ur1_row_chute_sw():
#     actual = \
#         f"""
#         __34a ____a   __34b ____b
#         _234a ____a   __34b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         __34a ____a   __34b ____b
#         _2__a ____a   __34b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_cross_hatch():
#     actual = \
#         f"""
#         1___a ____a   ____b ____b
#         ____a ____a   2___b ____b
#
#         ____c 3___c   ____d ____d
#         ____c ____c   ____d ___4d
#         """
#     expected = \
#         f"""
#         1___a _2_4a   1_34b 123_b
#         _234a _2_4a   _2__b 123_b
#
#         _2_4c 3___c   1_34d 123_d
#         _2__c 12__c   1_34d ___4d
#             """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_xy_chain_west():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a 12__a   ____b _23_b
#
#         ____c ____c   ____d ____d
#         1__4c ____c   ____d __34d
#         """
#
#     expected = \
#         f"""
#         _234a ____a   ____b ____b
#         _234a 12__a   ____b _23_b
#
#         ____c _234c   ____d ____d
#         1__4c _234c   ____d __34d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_hidden_unique_rectangle_row_chute_south_east():
#     actual = \
#         f"""
#         ____a 12__a   ____b 1234b
#         _234a 1234a   _234b 1234b
#
#         ____c ____c   ____d _234d
#         ____c ____c   ____d _234d
#         """
#
#     expected = \
#         f"""
#         ____a 12__a   ____b 1234b
#         _234a 1234a   _234b 1_34b
#
#         ____c ____c   ____d _234d
#         ____c ____c   ____d _234d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_xyz_wing_fences2_row_chute():
#     actual = \
#         f"""
#         ____a 123_a   1_3_b ____b
#         _23_a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         12_4a 123_a   1_3_b ____b
#         _23_a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_4x4_wxyz_fences2_south():
#     actual = \
#         f"""
#         _234a 1__4a   ____b ____b
#         ____a 1_3_a   ____b ____b
#
#         ____c ____c   ____d ____d
#         2_4_c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         _234a 1__4a   ____b ____b
#         123_a 1_3_a   ____b ____b
#
#         ____c ____c   ____d ____d
#         2_4_c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_4x4_wxyz_fences2_north():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         _23_a ____a   ____b ____b
#
#         12__c 1__4c   ____d ____d
#         ____c __34c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         ____a ____a   ____b ____b
#         _23_a ____a   ____b ____b
#
#         12__c 1__4c   ____d ____d
#         12_4c __34c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_shashimi_x_wing_east_fins1():
#     actual = \
#         f"""
#         _234a ____a   234_b ____b
#         ____a ____a   ____b ____b
#
#         _234c ____c   ____d _234d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         _234a ____a   234_b ____b
#         ____a ____a   _234b ____b
#
#         _234c ____c   ____d _234d
#         ____c ____c   ____d _234d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_finned_x_wing_east_fins1():
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
#     if solve(actual, expected, None):
#         return
#     assert False

def to_sudoku(length: int, actual: str, _id: str) -> Sudoku:
    newcan = "".join(str(num + 1) for num in range(length))

    underscore = "".join('_' for _ in range(length))
    string = actual
    string = string.replace('\n', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1) \
        .replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace(underscore, newcan).strip()

    temp = numpy.array(string.split(' '), str).reshape((length, length))
    return Sudoku(temp, length, _id)


def solve(actual, expected, technique):
    edits = technique.solve0(actual)

    if expected is None:
        return edits == 0

    if actual == expected:
        return True

    for r in range(len(actual)):
        for c in range(len(actual)):
            if actual.grid[r][c] != expected.grid[r][c]:
                expected.override_loc_color([Loc(r, c)], Fore.CYAN)

    print(actual.to_string())
    print(expected.to_string())
    return False


def test_sudoku_4x4_ur1_row_chute_ne():
    actual = \
        f"""
        ____a _23_a   ____b 123_b
        ____a _23_a   ____b _23_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a _23_a   ____b 1___b
        ____a _23_a   ____b _23_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    actual0 = to_sudoku(4, actual, 'test_sudoku_4x4_ur1_row_chute_ne_actual')
    expected0 = to_sudoku(4, expected, 'test_sudoku_4x4_ur1_row_chute_ne_expected')

    if solve(actual0, expected0, UniqueRectangleType1()):
        return

    assert False


def test_sudoku_4x4_ur1_row_chute_ne_control():
    actual = \
        f"""
        ____a _23_a   ____b 123_b
        _23_a ____a   ____b _23_b

        ____c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """

    actual0 = to_sudoku(4, actual, 'test_sudoku_4x4_ur1_row_chute_ne_control')

    if solve(actual0, None, UniqueRectangleType1()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
        return

    assert False

    # expected = \
    #     f"""
    #        ____a _23_a   _23_b 123_b
    #        ____a _23_a   _234b 123_b
    #
    #        ____c ____c   ____d _234d
    #        ____c ____c   ____d _234d
    #        """


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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
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

    actual0 = to_sudoku(4, actual, '_actual')
    expected0 = to_sudoku(4, expected, '_expected')

    if solve(actual0, expected0, UniqueRectangleType2()):
        return

    assert False
