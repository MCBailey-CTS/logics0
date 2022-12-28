from Constants import Constants
from Techniques import Techs
from _puzzles import Sudoku, Magnets, Kropki, Parks1, Tenner, RobotFences
from Loc import Loc
from typing import Union, Optional
import pytest

EXPLICITLY = "EXPLICITLY"



def default_test_explicit_actual_expected(constructor, technique, actual, expected) -> bool:
    actual_puzzle = constructor(actual)
    expected_puzzle = constructor(expected)

    technique.solve0(actual_puzzle)

    actual_string = str(actual_puzzle).replace(actual_puzzle.id(), "")
    expected_string = str(expected_puzzle).replace(expected_puzzle.id(), "")

    if actual_string == expected_string:
        return True

    print(actual_puzzle)
    print(expected_puzzle)
    return False



def default_test_puzzle(puzzle_string, constructor, techniques) -> bool:
    puzzle = constructor(puzzle_string)
    edits = 0
    while True:
        original_edits = edits
        for tech in techniques:
            _edits = tech.solve0(puzzle)
            edits = edits + _edits
        if original_edits == edits:
            break
    if puzzle.is_solved():
        return True
    print(puzzle)
    return False


def sudoku_techniques() -> list:
    return [
        Techs.CrossHatch(),
        Techs.HiddenSingle(),
        Techs.NakedPair(),
        Techs.LockedCandidatesPointing(),
        Techs.LockedCandidatesClaiming(),
        Techs.HiddenSingle(),
        # Techs.UniqueRectangleType1(),
        # Techs.UniqueRectangleType2(),
        # Techs.UniqueRectangleType4(),
        # Techs.XWing(),
        # Techs.Bug(),
        # Techs.NakedTriple(),
        # Techs.WWing(),
        # Techs.ShashimiXWingPlus1(),
        # Techs.XyWing(),
        # Techs.FinnedXWing(),
        # Techs.AvoidableRectangleType1(),
        # Techs.WxyzWing(),
        # Techs.SwordFish(),
        # Techs.JellyFish(),
    ]


# def sudoku0_techniques_picnic():
#     return [Techs.CrossHatch()]
#
#
# def sudoku_techniques():
#     return sudoku0_techniques_picnic() + [Techs.HiddenSingle()]
#
#
# def sudoku_techniques():
#     return sudoku_techniques() + [Techs.LockedCandidatesPointing()]
#
#
# def sudoku3_techniques_intricate():
#     return sudoku_techniques() + [Techs.LockedCandidatesClaiming(), Techs.NakedPair()]
#
#
# def sudoku_techniques():
#     return sudoku3_techniques_intricate() + [
#         Techs.UniqueRectangleType1(),
#         # Techs.UniqueRectangleType2(),
#         # Techs.UniqueRectangleType3(),
#         Techs.UniqueRectangleType4(),
#         Techs.Bug(),
#         Techs.NakedTriple(),
#         Techs.HiddenPair(),
#         # Techs.RemotePair(),
#         Techs.XWing()]


# def sudoku5_techniques_annoying():
#     return [


def test_puzzle_sudoku_difficult_00():
    assert default_test_puzzle(Constants.sudoku_difficult_00(), Sudoku,
                               [Techs.CrossHatch(), Techs.HiddenSingle(), Techs.UniqueRectangleType1()])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_01():
    assert default_test_puzzle(Constants.sudoku_difficult_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_02():
    assert default_test_puzzle(
        Constants.sudoku_difficult_02(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            # Techs.RemotePair()
        ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_03():
    assert default_test_puzzle(
        Constants.sudoku_difficult_03(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            # Techs.RemotePair()
        ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_03():
    assert default_test_puzzle(Constants.sudoku_difficult_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_04():
    assert default_test_puzzle(Constants.sudoku_difficult_04(), Sudoku, sudoku_techniques())

@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_05():
    assert default_test_puzzle(
        Constants.sudoku_difficult_05(),
        Sudoku,
        sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_06():
    assert default_test_puzzle(
        Constants.sudoku_difficult_06(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_07():
    assert default_test_puzzle(Constants.sudoku_difficult_07(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_difficult_08():
    assert default_test_puzzle(
        Constants.sudoku_difficult_08(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.UniqueRectangleType1(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


def test_puzzle_sudoku_difficult_09():
    assert default_test_puzzle(
        Constants.sudoku_difficult_09(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_10():
    assert default_test_puzzle(
        Constants.sudoku_difficult_10(),
        Sudoku,sudoku_techniques())
        
@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_11():
    assert default_test_puzzle(
        Constants.sudoku_difficult_11(),
        Sudoku
        ,sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_12():
    assert default_test_puzzle(
        Constants.sudoku_difficult_12(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.LockedCandidatesPointing(),
            Techs.LockedCandidatesClaiming(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


def test_puzzle_sudoku_difficult_13():
    assert default_test_puzzle(
        Constants.sudoku_difficult_13(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


def test_puzzle_sudoku_difficult_14():
    assert default_test_puzzle(
        Constants.sudoku_difficult_14(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


def test_puzzle_sudoku_difficult_15():
    assert default_test_puzzle(
        Constants.sudoku_difficult_15(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.LockedCandidatesPointing(),
            Techs.LockedCandidatesClaiming(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


def test_puzzle_sudoku_difficult_16():
    assert default_test_puzzle(
        Constants.sudoku_difficult_16(),
        Sudoku,
        [
            Techs.CrossHatch(),
            Techs.HiddenSingle(),
            Techs.UniqueRectangleType1(),
            Techs.UniqueRectangleType4(),
            Techs.NakedPair(),
            Techs.Bug()
        ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_17():
    assert default_test_puzzle(Constants.sudoku_difficult_17(), Sudoku, sudoku_techniques())

@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_18():
    assert default_test_puzzle(Constants.sudoku_difficult_18(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_19():
    assert default_test_puzzle(Constants.sudoku_difficult_19(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_20():
    assert default_test_puzzle(Constants.sudoku_difficult_20(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_21():
    assert default_test_puzzle(Constants.sudoku_difficult_21(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_22():
    assert default_test_puzzle(Constants.sudoku_difficult_22(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_23():
    assert default_test_puzzle(Constants.sudoku_difficult_23(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_24():
    #     assert default_test_puzzle(Constants.sudoku_difficult_24(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_24(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_25():
    #     assert default_test_puzzle(Constants.sudoku_difficult_25(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_25(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_26():
    #     assert default_test_puzzle(Constants.sudoku_difficult_26(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_26(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_27():
    #     assert default_test_puzzle(Constants.sudoku_difficult_27(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_27(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_28():
    assert default_test_puzzle(Constants.sudoku_difficult_28(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_29():
    #     assert default_test_puzzle(Constants.sudoku_difficult_29(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_29(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_30():
    #     assert default_test_puzzle(Constants.sudoku_difficult_30(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_30(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_31():
    assert default_test_puzzle(Constants.sudoku_difficult_31(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_32():
    #     assert default_test_puzzle(Constants.sudoku_difficult_32(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_32(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_33():
    #     assert default_test_puzzle(Constants.sudoku_difficult_33(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_33(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_34():
    #     assert default_test_puzzle(Constants.sudoku_difficult_34(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_34(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_35():
    assert default_test_puzzle(Constants.sudoku_difficult_35(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_difficult_36():
    #     assert default_test_puzzle(Constants.sudoku_difficult_36(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_36(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_difficult_37():
    assert default_test_puzzle(Constants.sudoku_difficult_37(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_difficult_38():
    #     assert default_test_puzzle(Constants.sudoku_difficult_38(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_38(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.LockedCandidatesClaiming(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                                   Techs.Bug()
                               ])


def test_puzzle_sudoku_difficult_39():
    #     assert default_test_puzzle(Constants.sudoku_difficult_39(), Sudoku, sudoku_techniques())
    assert default_test_puzzle(Constants.sudoku_difficult_39(), Sudoku,
                               [
                                   Techs.CrossHatch(),
                                   Techs.HiddenSingle(),
                                   Techs.LockedCandidatesPointing(),
                                   Techs.UniqueRectangleType1(),
                                   Techs.UniqueRectangleType4(),
                                   Techs.NakedPair(),
                               ])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_swordfish_5():
    assert default_test_puzzle(Constants.sudoku_shashimi_swordfish_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_00():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_01():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_02():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_03():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_06():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_06(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_07():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_08():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_08(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_09():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_09(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_simple_coloring_trap_0():
    assert default_test_puzzle(Constants.sudoku_simple_coloring_trap_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_sue_de_coq_0():
    assert default_test_puzzle(Constants.sudoku_sue_de_coq_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_sue_de_coq_1():
    assert default_test_puzzle(Constants.sudoku_sue_de_coq_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_sue_de_coq_2():
    assert default_test_puzzle(Constants.sudoku_sue_de_coq_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_0():
    assert default_test_puzzle(Constants.sudoku_swordfish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_1():
    assert default_test_puzzle(Constants.sudoku_swordfish_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_2():
    assert default_test_puzzle(Constants.sudoku_swordfish_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_3():
    assert default_test_puzzle(Constants.sudoku_swordfish_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_4():
    assert default_test_puzzle(Constants.sudoku_swordfish_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_5():
    assert default_test_puzzle(Constants.sudoku_swordfish_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_swordfish_6():
    assert default_test_puzzle(Constants.sudoku_swordfish_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_00():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_01():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_02():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_03():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_04():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_05():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_06():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_06(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type3_07():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type3_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_0():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_1():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_19():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_19(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_2():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_3():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_4():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_5():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_6():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_7():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_7(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_8():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_8(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_wxyz_wing_9():
    assert default_test_puzzle(Constants.sudoku_wxyz_wing_9(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_0():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_1():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_2():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_3():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_4():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_5():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_w_wing_type_d_6():
    assert default_test_puzzle(Constants.sudoku_w_wing_type_d_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_0():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_1():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_2():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_3():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_4():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_5():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_6():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_7():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_7(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_8():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_8(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xyz_wing_9():
    assert default_test_puzzle(Constants.sudoku_xyz_wing_9(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_chain_0():
    assert default_test_puzzle(Constants.sudoku_xy_chain_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_chain_1():
    assert default_test_puzzle(Constants.sudoku_xy_chain_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_chain_2():
    assert default_test_puzzle(Constants.sudoku_xy_chain_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_00():
    assert default_test_puzzle(Constants.sudoku_xy_wing_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_01():
    assert default_test_puzzle(Constants.sudoku_xy_wing_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_02():
    assert default_test_puzzle(Constants.sudoku_xy_wing_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_03():
    assert default_test_puzzle(Constants.sudoku_xy_wing_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_04():
    assert default_test_puzzle(Constants.sudoku_xy_wing_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_05():
    assert default_test_puzzle(Constants.sudoku_xy_wing_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_06():
    assert default_test_puzzle(Constants.sudoku_xy_wing_06(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_07():
    assert default_test_puzzle(Constants.sudoku_xy_wing_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_08():
    assert default_test_puzzle(Constants.sudoku_xy_wing_08(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_09():
    assert default_test_puzzle(Constants.sudoku_xy_wing_09(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_10():
    assert default_test_puzzle(Constants.sudoku_xy_wing_10(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_xy_wing_11():
    assert default_test_puzzle(Constants.sudoku_xy_wing_11(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_x_chain_0():
    assert default_test_puzzle(Constants.sudoku_x_chain_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_x_wing_0():
    assert default_test_puzzle(Constants.sudoku_x_wing_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_x_wing_1():
    assert default_test_puzzle(Constants.sudoku_x_wing_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_x_wing_2():
    assert default_test_puzzle(Constants.sudoku_x_wing_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_x_wing_3():
    assert default_test_puzzle(Constants.sudoku_x_wing_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_05():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_06():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_06(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_07():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_08():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_08(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_09():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_09(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_10():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_10(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_11():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_11(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_12():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_12(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_13():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_13(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_14():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_14(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_15():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_15(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_16():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_16(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_17():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_17(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_fishy_cycle_0():
    assert default_test_puzzle(Constants.sudoku_fishy_cycle_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_fishy_cycle_1():
    assert default_test_puzzle(Constants.sudoku_fishy_cycle_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_0():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_1():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_2():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_3():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_4():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_5():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_6():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_7():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_7(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_8():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_8(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_quad_9():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_9(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_triple_0():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_triple_2():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_triple_3():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_triple_4():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_triple_5():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_triple_6():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_unique_rectangle_0():
    assert default_test_puzzle(Constants.sudoku_hidden_unique_rectangle_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_unique_rectangle_1():
    assert default_test_puzzle(Constants.sudoku_hidden_unique_rectangle_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_unique_rectangle_2():
    assert default_test_puzzle(Constants.sudoku_hidden_unique_rectangle_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_unique_rectangle_3():
    assert default_test_puzzle(Constants.sudoku_hidden_unique_rectangle_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_unique_rectangle_4():
    assert default_test_puzzle(Constants.sudoku_hidden_unique_rectangle_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_unique_rectangle_5():
    assert default_test_puzzle(Constants.sudoku_hidden_unique_rectangle_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_jellyfish_0():
    assert default_test_puzzle(Constants.sudoku_jellyfish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_jellyfish_1():
    assert default_test_puzzle(Constants.sudoku_jellyfish_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_jellyfish_2():
    assert default_test_puzzle(Constants.sudoku_jellyfish_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_maelstrom_0():
    assert default_test_puzzle(Constants.sudoku_maelstrom_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_medusa_coloring_3d_0():
    assert default_test_puzzle(Constants.sudoku_medusa_coloring_3d_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_0():
    assert default_test_puzzle(Constants.sudoku_naked_quad_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_1():
    assert default_test_puzzle(Constants.sudoku_naked_quad_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_2():
    assert default_test_puzzle(Constants.sudoku_naked_quad_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_3():
    assert default_test_puzzle(Constants.sudoku_naked_quad_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_4():
    assert default_test_puzzle(Constants.sudoku_naked_quad_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_5():
    assert default_test_puzzle(Constants.sudoku_naked_quad_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_6():
    assert default_test_puzzle(Constants.sudoku_naked_quad_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_quad_7():
    assert default_test_puzzle(Constants.sudoku_naked_quad_7(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_nightmare_0():
    assert default_test_puzzle(Constants.sudoku_nightmare_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_remote_pair_0():
    assert default_test_puzzle(Constants.sudoku_remote_pair_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_remote_pair_1():
    assert default_test_puzzle(Constants.sudoku_remote_pair_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_remote_pair_2():
    assert default_test_puzzle(Constants.sudoku_remote_pair_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_jellyfish_0():
    assert default_test_puzzle(Constants.sudoku_shashimi_jellyfish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_jellyfish_1():
    assert default_test_puzzle(Constants.sudoku_shashimi_jellyfish_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_jellyfish_2():
    assert default_test_puzzle(Constants.sudoku_shashimi_jellyfish_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_jellyfish_3():
    assert default_test_puzzle(Constants.sudoku_shashimi_jellyfish_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_swordfish_0():
    assert default_test_puzzle(Constants.sudoku_shashimi_swordfish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_swordfish_1():
    assert default_test_puzzle(Constants.sudoku_shashimi_swordfish_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_swordfish_2():
    assert default_test_puzzle(Constants.sudoku_shashimi_swordfish_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_swordfish_3():
    assert default_test_puzzle(Constants.sudoku_shashimi_swordfish_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_swordfish_4():
    assert default_test_puzzle(Constants.sudoku_shashimi_swordfish_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_unique_rectangle_type4_south_cols():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_south_cols(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_unique_rectangle_type4_east_rows():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_east_rows(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_unique_rectangle_type4_west_rows():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_west_rows(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_unique_rectangle_type4_west_cols():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_west_cols(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_unique_rectangle_type4_east_cols():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_east_cols(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_bug():
    assert default_test_puzzle(Constants.sudoku_bug(), Sudoku, [Techs.CrossHatch(), Sudoku, Techs.Bug()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_pair_row():
    assert default_test_puzzle(Constants.sudoku_hidden_pair_row(), Sudoku,
                               [Techs.CrossHatch(), Techs.HiddenPair(), Techs.Bug()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_pair_col():
    assert default_test_puzzle(Constants.sudoku_hidden_pair_col(), Sudoku,
                               [Techs.CrossHatch(), Techs.HiddenPair(), Techs.Bug()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_pair_fence():
    assert default_test_puzzle(Constants.sudoku_hidden_pair_fence(),
                               Sudoku, [Techs.CrossHatch(), Techs.HiddenPair(), Techs.Bug()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_triple_row():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_row(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_triple_col():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_col(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_triple_fence():
    assert default_test_puzzle(Constants.sudoku_hidden_triple_fence(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_quad_row():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_row(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_quad_col():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_col(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_hidden_quad_fence():
    assert default_test_puzzle(Constants.sudoku_hidden_quad_fence(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_remote_pair_row():
    assert default_test_puzzle(Constants.sudoku_remote_pair_row(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_x_wing_row():
    assert default_test_puzzle(Constants.sudoku_x_wing_row(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_x_wing_col():
    assert default_test_puzzle(Constants.sudoku_x_wing_col(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_swordfish_of_5_in_rows():
    assert default_test_puzzle(Constants.sudoku_swordfish_of_5_in_rows(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_swordfish_of_8_in_cols():
    assert default_test_puzzle(Constants.sudoku_swordfish_of_8_in_cols(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_jellyfish_of_1_in_rows():
    assert default_test_puzzle(Constants.sudoku_jellyfish_of_1_in_rows(), Sudoku, [Techs.CrossHatch()])


@pytest.mark.skip(EXPLICITLY)
def test_1sudoku_technique_sudoku_jellyfish_of_3_in_cols():
    assert default_test_puzzle(Constants.sudoku_jellyfish_of_3_in_cols(), Sudoku,
                               [Techs.CrossHatch(), Techs.JellyFish()])


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_001_4x4():
    assert default_test_puzzle(Constants.sudoku_001_4x4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_00():
    assert default_test_puzzle(Constants.sudoku_annoying_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_02():
    assert default_test_puzzle(Constants.sudoku_annoying_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_05():
    assert default_test_puzzle(Constants.sudoku_annoying_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_06():
    assert default_test_puzzle(Constants.sudoku_annoying_06(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_07():
    assert default_test_puzzle(Constants.sudoku_annoying_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_11():
    assert default_test_puzzle(Constants.sudoku_annoying_11(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_13():
    assert default_test_puzzle(Constants.sudoku_annoying_13(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_17():
    assert default_test_puzzle(Constants.sudoku_annoying_17(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_22():
    assert default_test_puzzle(Constants.sudoku_annoying_22(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_23():
    assert default_test_puzzle(Constants.sudoku_annoying_23(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_25():
    assert default_test_puzzle(Constants.sudoku_annoying_25(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_26():
    assert default_test_puzzle(Constants.sudoku_annoying_26(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_27():
    assert default_test_puzzle(Constants.sudoku_annoying_27(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_28():
    assert default_test_puzzle(Constants.sudoku_annoying_28(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_29():
    assert default_test_puzzle(Constants.sudoku_annoying_29(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_30():
    assert default_test_puzzle(Constants.sudoku_annoying_30(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_32():
    assert default_test_puzzle(Constants.sudoku_annoying_32(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_33():
    assert default_test_puzzle(Constants.sudoku_annoying_33(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_35():
    assert default_test_puzzle(Constants.sudoku_annoying_35(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_bug_0():
    assert default_test_puzzle(Constants.sudoku_bug_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_easiest_0():
    assert default_test_puzzle(Constants.sudoku_easiest_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_easy_as_pie_0():
    assert default_test_puzzle(Constants.sudoku_easy_as_pie_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_first_lesson():
    assert default_test_puzzle(Constants.sudoku_first_lesson(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_pair_0():
    assert default_test_puzzle(Constants.sudoku_hidden_pair_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_hidden_pair_1():
    assert default_test_puzzle(Constants.sudoku_hidden_pair_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_hidden_single_0():
    assert default_test_puzzle(Constants.sudoku_hidden_single_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_hidden_single_1():
    assert default_test_puzzle(Constants.sudoku_hidden_single_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_hidden_single_2():
    assert default_test_puzzle(Constants.sudoku_hidden_single_2(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_0():
    assert default_test_puzzle(Constants.sudoku_intricate_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_1():
    assert default_test_puzzle(Constants.sudoku_intricate_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_2():
    assert default_test_puzzle(Constants.sudoku_intricate_2(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_3():
    assert default_test_puzzle(Constants.sudoku_intricate_3(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_4():
    assert default_test_puzzle(Constants.sudoku_intricate_4(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_5():
    assert default_test_puzzle(Constants.sudoku_intricate_5(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_6():
    assert default_test_puzzle(Constants.sudoku_intricate_6(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_7():
    assert default_test_puzzle(Constants.sudoku_intricate_7(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_intricate_8():
    assert default_test_puzzle(Constants.sudoku_intricate_8(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_locked_candidates_claiming_0():
    assert default_test_puzzle(Constants.sudoku_locked_candidates_claiming_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_locked_candidates_claiming_1():
    assert default_test_puzzle(Constants.sudoku_locked_candidates_claiming_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_locked_candidates_claiming_2():
    assert default_test_puzzle(Constants.sudoku_locked_candidates_claiming_2(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_locked_candidates_pointing_0():
    assert default_test_puzzle(Constants.sudoku_locked_candidates_pointing_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_mild_0():
    assert default_test_puzzle(Constants.sudoku_mild_0(), Sudoku, sudoku_techniques())


#
#
def test_puzzle_sudoku_mild_1():
    assert default_test_puzzle(Constants.sudoku_mild_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_mild_2():
    assert default_test_puzzle(Constants.sudoku_mild_2(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_mild_3():
    assert default_test_puzzle(Constants.sudoku_mild_3(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_mild_4():
    assert default_test_puzzle(Constants.sudoku_mild_4(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_moderate_0():
    assert default_test_puzzle(Constants.sudoku_moderate_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_naked_pair_0():
    assert default_test_puzzle(Constants.sudoku_naked_pair_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_naked_pair_1():
    assert default_test_puzzle(Constants.sudoku_naked_pair_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_naked_pair_2():
    assert default_test_puzzle(Constants.sudoku_naked_pair_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_0():
    assert default_test_puzzle(Constants.sudoku_naked_triple_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_1():
    assert default_test_puzzle(Constants.sudoku_naked_triple_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_2():
    assert default_test_puzzle(Constants.sudoku_naked_triple_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_3():
    assert default_test_puzzle(Constants.sudoku_naked_triple_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_4():
    assert default_test_puzzle(Constants.sudoku_naked_triple_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_5():
    assert default_test_puzzle(Constants.sudoku_naked_triple_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_6():
    assert default_test_puzzle(Constants.sudoku_naked_triple_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_7():
    assert default_test_puzzle(Constants.sudoku_naked_triple_7(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_8():
    assert default_test_puzzle(Constants.sudoku_naked_triple_8(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_9():
    assert default_test_puzzle(Constants.sudoku_naked_triple_9(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_naked_triple_row():
    assert default_test_puzzle(Constants.sudoku_naked_triple_row(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_picnic_0():
    assert default_test_puzzle(Constants.sudoku_picnic_0(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_picnic_1():
    assert default_test_puzzle(Constants.sudoku_picnic_1(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_picnic_2():
    assert default_test_puzzle(Constants.sudoku_picnic_2(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_second_lesson_0():
    assert default_test_puzzle(Constants.sudoku_second_lesson_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_04():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_shashimi_x_wing_05():
    assert default_test_puzzle(Constants.sudoku_shashimi_x_wing_05(), Sudoku, sudoku_techniques())


def test_puzzle_sudoku_simple_0():
    assert default_test_puzzle(Constants.sudoku_simple_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type1_00():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type1_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type1_01():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type1_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type1_02():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type1_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type1_03():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type1_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type1_04():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type1_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type1_05():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type1_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_00():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_01():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_02():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_03():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_04():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_05():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_06():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_06(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_07():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_08():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_08(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_09():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_09(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_10():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_10(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_11():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_11(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type2_12():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type2_12(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type4_00():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type4_01():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type4_02():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type4_03():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type4_04():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_unique_rectangle_type4_05():
    assert default_test_puzzle(Constants.sudoku_unique_rectangle_type4_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_0():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_1():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_2():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_3():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_4():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_5():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_almost_locked_candidates_6():
    assert default_test_puzzle(Constants.sudoku_almost_locked_candidates_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_01():
    assert default_test_puzzle(Constants.sudoku_annoying_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_03():
    assert default_test_puzzle(Constants.sudoku_annoying_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_04():
    assert default_test_puzzle(Constants.sudoku_annoying_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_08():
    assert default_test_puzzle(Constants.sudoku_annoying_08(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_09():
    assert default_test_puzzle(Constants.sudoku_annoying_09(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_10():
    assert default_test_puzzle(Constants.sudoku_annoying_10(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_12():
    assert default_test_puzzle(Constants.sudoku_annoying_12(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_14():
    assert default_test_puzzle(Constants.sudoku_annoying_14(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_15():
    assert default_test_puzzle(Constants.sudoku_annoying_15(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_16():
    assert default_test_puzzle(Constants.sudoku_annoying_16(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_18():
    assert default_test_puzzle(Constants.sudoku_annoying_18(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_19():
    assert default_test_puzzle(Constants.sudoku_annoying_19(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_20():
    assert default_test_puzzle(Constants.sudoku_annoying_20(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_21():
    assert default_test_puzzle(Constants.sudoku_annoying_21(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_24():
    assert default_test_puzzle(Constants.sudoku_annoying_24(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_31():
    assert default_test_puzzle(Constants.sudoku_annoying_31(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_annoying_36():
    assert default_test_puzzle(Constants.sudoku_annoying_36(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_00():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_01():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_02():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_03():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_04():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_04(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_05():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_05(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_07():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_07(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_08():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_08(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_09():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_09(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_10():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_10(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_11():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_11(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_12():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_12(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type1_13():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type1_13(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_0():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_1():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_2():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_3():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_4():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_5():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_avoidable_rectangle_type2_6():
    assert default_test_puzzle(Constants.sudoku_avoidable_rectangle_type2_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_0():
    assert default_test_puzzle(Constants.sudoku_devious_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_1():
    assert default_test_puzzle(Constants.sudoku_devious_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_2():
    assert default_test_puzzle(Constants.sudoku_devious_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_3():
    assert default_test_puzzle(Constants.sudoku_devious_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_4():
    assert default_test_puzzle(Constants.sudoku_devious_4(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_5():
    assert default_test_puzzle(Constants.sudoku_devious_5(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_6():
    assert default_test_puzzle(Constants.sudoku_devious_6(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_7():
    assert default_test_puzzle(Constants.sudoku_devious_7(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_devious_8():
    assert default_test_puzzle(Constants.sudoku_devious_8(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_diabolical_0():
    assert default_test_puzzle(Constants.sudoku_diabolical_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_fiendish_0():
    assert default_test_puzzle(Constants.sudoku_fiendish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_jellyfish_0():
    assert default_test_puzzle(Constants.sudoku_finned_jellyfish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_jellyfish_1():
    assert default_test_puzzle(Constants.sudoku_finned_jellyfish_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_jellyfish_2():
    assert default_test_puzzle(Constants.sudoku_finned_jellyfish_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_jellyfish_3():
    assert default_test_puzzle(Constants.sudoku_finned_jellyfish_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_swordfish_0():
    assert default_test_puzzle(Constants.sudoku_finned_swordfish_0(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_swordfish_1():
    assert default_test_puzzle(Constants.sudoku_finned_swordfish_1(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_swordfish_2():
    assert default_test_puzzle(Constants.sudoku_finned_swordfish_2(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_swordfish_3():
    assert default_test_puzzle(Constants.sudoku_finned_swordfish_3(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_00():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_00(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_01():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_01(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_02():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_02(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_03():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_03(), Sudoku, sudoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sudoku_finned_x_wing_04():
    assert default_test_puzzle(Constants.sudoku_finned_x_wing_04(), Sudoku, sudoku_techniques())


def test_1explicit_sudoku_explicit_jelly_fish_cols():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.JellyFish(),
        Constants.sudoku_explicit_jelly_fish_cols_actual(),
        Constants.sudoku_explicit_jelly_fish_cols_expected())


def test_1explicit_sudoku_explicit_jelly_fish_rows():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.JellyFish(),
        Constants.sudoku_explicit_jelly_fish_rows_actual(),
        Constants.sudoku_explicit_jelly_fish_rows_expected())


def test_1explicit_sudoku_explicit_w_wing_rows():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.WWing(),
        Constants.sudoku_explicit_w_wing_rows_actual(),
        Constants.sudoku_explicit_w_wing_rows_expected())


def test_1explicit_sudoku_explicit_w_wing_cols():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.WWing(),
        Constants.sudoku_explicit_w_wing_cols_actual(),
        Constants.sudoku_explicit_w_wing_cols_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_north_west_row_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_north_west_row_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_north_west_row_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_south_east_row_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_east_row_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_east_row_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_south_west_row_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_west_row_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_west_row_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_north_east_col_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_north_east_col_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_north_east_col_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_north_west_col_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_north_west_col_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_north_west_col_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_south_east_col_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_east_col_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_east_col_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type1_south_west_col_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType1(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_west_col_chute_actual(),
        Constants.sudoku_explicit_unique_rectangle_type1_south_west_col_chute_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_goofy_east():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType2(),
        Constants.sudoku_explicit_unique_rectangle_type2_goofy_east_actual(),
        Constants.sudoku_explicit_unique_rectangle_type2_goofy_east_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_goofy_north():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType2(),
        Constants.sudoku_explicit_unique_rectangle_type2_goofy_north_actual(),
        Constants.sudoku_explicit_unique_rectangle_type2_goofy_north_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_normal_west():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType2(),
        Constants.sudoku_explicit_unique_rectangle_type2_normal_west_actual(),
        Constants.sudoku_explicit_unique_rectangle_type2_normal_west_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_normal_south():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType2(),
        Constants.sudoku_explicit_unique_rectangle_type2_normal_south_actual(),
        Constants.sudoku_explicit_unique_rectangle_type2_normal_south_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_goofy_west():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.UniqueRectangleType2(),
        Constants.sudoku_explicit_unique_rectangle_type2_goofy_west_actual(),
        Constants.sudoku_explicit_unique_rectangle_type2_goofy_west_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_normal_east():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType2(),
                                                 Constants.sudoku_explicit_unique_rectangle_type2_normal_east_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type2_normal_east_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_goofy_south():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType2(),
                                                 Constants.sudoku_explicit_unique_rectangle_type2_goofy_south_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type2_goofy_south_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_north():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_north_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_north_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_normal_east():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_normal_east_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_normal_east_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_normal_south():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_normal_south_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_normal_south_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_normal_west():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_normal_west_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_normal_west_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_goofy_west():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_west_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_west_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_goofy_north():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_north_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_north_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_goofy_east():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_east_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_east_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type4_goofy_south():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType4(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_south_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type4_goofy_south_expected())


def test_1explicit_sudoku_explicit_hidden_pair_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenPair(),
                                                 Constants.sudoku_explicit_hidden_pair_fences_actual(),
                                                 Constants.sudoku_explicit_hidden_pair_fences_expected())


def test_1explicit_sudoku_explicit_hidden_pair_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenPair(),
                                                 Constants.sudoku_explicit_hidden_pair_rows_actual(),
                                                 Constants.sudoku_explicit_hidden_pair_rows_expected())


def test_1explicit_sudoku_explicit_hidden_pair_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenPair(),
                                                 Constants.sudoku_explicit_hidden_pair_cols_actual(),
                                                 Constants.sudoku_explicit_hidden_pair_cols_expected())


def test_1explicit_sudoku_explicit_sword_fish_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.SwordFish(),
                                                 Constants.sudoku_explicit_sword_fish_rows_actual(),
                                                 Constants.sudoku_explicit_sword_fish_rows_expected())


def test_1explicit_sudoku_explicit_sword_fish_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.SwordFish(),
                                                 Constants.sudoku_explicit_sword_fish_cols_actual(),
                                                 Constants.sudoku_explicit_sword_fish_cols_expected())


def test_1explicit_sudoku_explicit_xy_wing_north_east():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.XyWing(),
        Constants.sudoku_explicit_xy_wing_north_east_actual(),
        Constants.sudoku_explicit_xy_wing_north_east_expected())


def test_1explicit_sudoku_explicit_xy_wing_south_west():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyWing(),
                                                 Constants.sudoku_explicit_xy_wing_south_west_actual(),
                                                 Constants.sudoku_explicit_xy_wing_south_west_expected())


def test_1explicit_sudoku_explicit_xyz_wing_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyzWing(),
                                                 Constants.sudoku_explicit_xyz_wing_rows_actual(),
                                                 Constants.sudoku_explicit_xyz_wing_rows_expected())


def test_1explicit_sudoku_explicit_xyz_wing_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyzWing(),
                                                 Constants.sudoku_explicit_xyz_wing_cols_actual(),
                                                 Constants.sudoku_explicit_xyz_wing_cols_expected())


def test_1explicit_sudoku_explicit_xy_wing_north_west():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyWing(),
                                                 Constants.sudoku_explicit_xy_wing_north_west_actual(),
                                                 Constants.sudoku_explicit_xy_wing_north_west_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_north_east_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_col_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType1(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute_expected())


def test_1explicit_sudoku_explicit_finned_x_wing_2_fin_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedXWing(),
                                                 Constants.sudoku_explicit_finned_x_wing_2_fin_cols_actual(),
                                                 Constants.sudoku_explicit_finned_x_wing_2_fin_cols_expected())


def test_1explicit_sudoku_explicit_finned_x_wing_2_fin_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedXWing(),
                                                 Constants.sudoku_explicit_finned_x_wing_2_fin_rows_actual(),
                                                 Constants.sudoku_explicit_finned_x_wing_2_fin_rows_expected())


def test_1explicit_sudoku_explicit_unique_rectangle_type2_normal_north():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType2(),
                                                 Constants.sudoku_explicit_unique_rectangle_type2_normal_north_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type2_normal_north_expected())


def test_1explicit_sudoku_explicit_xy_wing_south_east():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyWing(),
                                                 Constants.sudoku_explicit_xy_wing_south_east_actual(),
                                                 Constants.sudoku_explicit_xy_wing_south_east_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_type1_north_east_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_type1_north_east_row_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_type1_north_east_row_chute_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_north_west_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_north_west_row_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_north_west_row_chute_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_north_west_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_north_west_col_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_north_west_col_chute_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_north_east_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_north_east_col_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_north_east_col_chute_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_south_east_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_south_east_col_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_south_east_col_chute_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_south_west_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_south_west_col_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_south_west_col_chute_expected())


def test_1explicit_sudoku_explicit_hidden_unique_rectangle_south_east_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_south_east_row_chute_actual(),
                                                 Constants.sudoku_explicit_hidden_unique_rectangle_south_east_row_chute_expected())


def test_1explicit_hidden_unique_rectangle_default():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenUniqueRectangle(),
                                                 Constants.hidden_unique_rectangle_default_actual(),
                                                 Constants.hidden_unique_rectangle_default_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_xy_chain():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyChain(), Constants.sudoku_explicit_xy_chain_actual(),
                                                 Constants.sudoku_explicit_xy_chain_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_fishy_cycle():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FishyCycle(),
                                                 Constants.sudoku_explicit_fishy_cycle_actual(),
                                                 Constants.sudoku_explicit_fishy_cycle_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_simple_coloring():
    assert default_test_explicit_actual_expected(Sudoku, Techs.SimpleColoring(),
                                                 Constants.sudoku_explicit_simple_coloring_actual(),
                                                 Constants.sudoku_explicit_simple_coloring_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_sue_de_coq_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.SueDeCoq(),
                                                 Constants.sudoku_explicit_sue_de_coq_rows_actual(),
                                                 Constants.sudoku_explicit_sue_de_coq_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_sue_de_coq_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.SueDeCoq(),
                                                 Constants.sudoku_explicit_sue_de_coq_cols_actual(),
                                                 Constants.sudoku_explicit_sue_de_coq_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_unique_rectangle_type3_col_chute_fences_2_fins():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType3(),
                                                 Constants.sudoku_explicit_unique_rectangle_type3_col_chute_fences_2_fins_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type3_col_chute_fences_2_fins_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_unique_rectangle_type3_row_chute_west_cols_2_fins():
    assert default_test_explicit_actual_expected(Sudoku, Techs.UniqueRectangleType3(),
                                                 Constants.sudoku_explicit_unique_rectangle_type3_row_chute_west_cols_2_fins_actual(),
                                                 Constants.sudoku_explicit_unique_rectangle_type3_row_chute_west_cols_2_fins_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_jelly_fish_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiJellyFish(),
                                                 Constants.sudoku_explicit_shashimi_jelly_fish_cols_actual(),
                                                 Constants.sudoku_explicit_shashimi_jelly_fish_cols_expected())


# @pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_finned_x_wing_1_fin_rows():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.FinnedXWing(),
        Constants.sudoku_explicit_finned_x_wing_1_fin_rows_actual(),
        Constants.sudoku_explicit_finned_x_wing_1_fin_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_finned_x_wing_1_fin_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedXWing(),
                                                 Constants.sudoku_explicit_finned_x_wing_1_fin_cols_actual(),
                                                 Constants.sudoku_explicit_finned_x_wing_1_fin_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_finned_sword_fish_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedSwordFish(),
                                                 Constants.sudoku_explicit_finned_sword_fish_cols_actual(),
                                                 Constants.sudoku_explicit_finned_sword_fish_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_finned_jelly_fish_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedJellyFish(),
                                                 Constants.sudoku_explicit_finned_jelly_fish_cols_actual(),
                                                 Constants.sudoku_explicit_finned_jelly_fish_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_sword_fish_1_fin_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiSwordFish(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_1_fin_rows_actual(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_1_fin_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_sword_fish_2_fin_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiSwordFish(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_2_fin_cols_actual(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_2_fin_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_x_chain():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XChain(), Constants.sudoku_explicit_x_chain_actual(),
                                                 Constants.sudoku_explicit_x_chain_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_sword_fish_1_fin_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiSwordFish(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_1_fin_cols_actual(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_1_fin_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_hidden_triple_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenTriple(),
                                                 Constants.sudoku_explicit_hidden_triple_rows_actual(),
                                                 Constants.sudoku_explicit_hidden_triple_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_hidden_triple_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenTriple(),
                                                 Constants.sudoku_explicit_hidden_triple_fences_actual(),
                                                 Constants.sudoku_explicit_hidden_triple_fences_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_hidden_quad_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenQuad(),
                                                 Constants.sudoku_explicit_hidden_quad_rows_actual(),
                                                 Constants.sudoku_explicit_hidden_quad_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_hidden_quad_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenQuad(),
                                                 Constants.sudoku_explicit_hidden_quad_cols_actual(),
                                                 Constants.sudoku_explicit_hidden_quad_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type2_east():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType2(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type2_east_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type2_east_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_wxyz_wing_3_fences_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.WxyzWing(),
                                                 Constants.sudoku_explicit_wxyz_wing_3_fences_row_chute_actual(),
                                                 Constants.sudoku_explicit_wxyz_wing_3_fences_row_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_wxyz_wing_2_fences_row_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.WxyzWing(),
                                                 Constants.sudoku_explicit_wxyz_wing_2_fences_row_chute_actual(),
                                                 Constants.sudoku_explicit_wxyz_wing_2_fences_row_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_wxyz_wing_3_fences_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.WxyzWing(),
                                                 Constants.sudoku_explicit_wxyz_wing_3_fences_col_chute_actual(),
                                                 Constants.sudoku_explicit_wxyz_wing_3_fences_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_wxyz_wing_2_fences_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.WxyzWing(),
                                                 Constants.sudoku_explicit_wxyz_wing_2_fences_col_chute_actual(),
                                                 Constants.sudoku_explicit_wxyz_wing_2_fences_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type2_north():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.AvoidableRectangleType2(),
        Constants.sudoku_explicit_avoidable_rectangle_type2_north_actual(),
        Constants.sudoku_explicit_avoidable_rectangle_type2_north_expected())


def test_1explicit_sudoku_explicit_x_wing_col():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.XWing(),
        Constants.sudoku_explicit_x_wing_col_actual(),
        Constants.sudoku_explicit_x_wing_col_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_finned_sword_fish_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedSwordFish(),
                                                 Constants.sudoku_explicit_finned_sword_fish_rows_actual(),
                                                 Constants.sudoku_explicit_finned_sword_fish_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_finned_jelly_fish_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.FinnedJellyFish(),
                                                 Constants.sudoku_explicit_finned_jelly_fish_rows_actual(),
                                                 Constants.sudoku_explicit_finned_jelly_fish_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_x_wing_1_fin_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiXWing(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_1_fin_rows_actual(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_1_fin_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_x_wing_2_fin_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiXWing(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_2_fin_rows_actual(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_2_fin_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_sword_fish_2_fin_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiSwordFish(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_2_fin_rows_actual(),
                                                 Constants.sudoku_explicit_shashimi_sword_fish_2_fin_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_jelly_fish_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiJellyFish(),
                                                 Constants.sudoku_explicit_shashimi_jelly_fish_rows_actual(),
                                                 Constants.sudoku_explicit_shashimi_jelly_fish_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_almost_locked_candidates_claming_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AlmostLockedCandidatesClaiming(),
                                                 Constants.sudoku_explicit_almost_locked_candidates_claming_rows_actual(),
                                                 Constants.sudoku_explicit_almost_locked_candidates_claming_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_almost_locked_candidates_pointing_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AlmostLockedCandidatesPointing(),
                                                 Constants.sudoku_explicit_almost_locked_candidates_pointing_rows_actual(),
                                                 Constants.sudoku_explicit_almost_locked_candidates_pointing_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_x_wing_1_fin_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiXWing(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_1_fin_cols_actual(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_1_fin_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_shashimi_x_wing_2_fin_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.ShashimiXWing(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_2_fin_cols_actual(),
                                                 Constants.sudoku_explicit_shashimi_x_wing_2_fin_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_avoidable_rectangle_type2_south():
    assert default_test_explicit_actual_expected(Sudoku, Techs.AvoidableRectangleType2(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type2_south_actual(),
                                                 Constants.sudoku_explicit_avoidable_rectangle_type2_south_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_hidden_triple_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenTriple(),
                                                 Constants.sudoku_explicit_hidden_triple_cols_actual(),
                                                 Constants.sudoku_explicit_hidden_triple_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_hidden_quad_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenQuad(),
                                                 Constants.sudoku_explicit_hidden_quad_fences_actual(),
                                                 Constants.sudoku_explicit_hidden_quad_fences_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_x_wing_row():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XWing(), Constants.sudoku_explicit_x_wing_row_actual(),
                                                 Constants.sudoku_explicit_x_wing_row_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_xy_wing_2_fences_row_chute():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.XyWing(),
        Constants.sudoku_explicit_xy_wing_2_fences_row_chute_actual(),
        Constants.sudoku_explicit_xy_wing_2_fences_row_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_xy_wing_2_fences_col_chute():
    assert default_test_explicit_actual_expected(Sudoku, Techs.XyWing(),
                                                 Constants.sudoku_explicit_xy_wing_2_fences_col_chute_actual(),
                                                 Constants.sudoku_explicit_xy_wing_2_fences_col_chute_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_naked_quad_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedQuad(),
                                                 Constants.sudoku_explicit_naked_quad_rows_actual(),
                                                 Constants.sudoku_explicit_naked_quad_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_naked_quad_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedQuad(),
                                                 Constants.sudoku_explicit_naked_quad_cols_actual(),
                                                 Constants.sudoku_explicit_naked_quad_cols_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_sudoku_explicit_naked_quad_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedQuad(),
                                                 Constants.sudoku_explicit_naked_quad_fences_actual(),
                                                 Constants.sudoku_explicit_naked_quad_fences_expected())


def test_1explicit_sudoku_explicit_cross_hatch_rows():
    assert default_test_explicit_actual_expected(
        Sudoku,
        Techs.CrossHatchRows(),
        Constants.sudoku_explicit_cross_hatch_rows_actual(),
        Constants.sudoku_explicit_cross_hatch_rows_expected())


def test_1explicit_sudoku_explicit_cross_hatch_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.CrossHatchCols(),
                                                 Constants.sudoku_explicit_cross_hatch_cols_actual(),
                                                 Constants.sudoku_explicit_cross_hatch_cols_expected())


def test_1explicit_sudoku_explicit_cross_hatch_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.CrossHatchFences(),
                                                 Constants.sudoku_explicit_cross_hatch_fences_actual(),
                                                 Constants.sudoku_explicit_cross_hatch_fences_expected())


def test_1explicit_sudoku_explicit_hidden_single_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenSingleRows(),
                                                 Constants.sudoku_explicit_hidden_single_rows_actual(),
                                                 Constants.sudoku_explicit_hidden_single_rows_expected())


def test_1explicit_sudoku_explicit_hidden_single_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenSingleCols(),
                                                 Constants.sudoku_explicit_hidden_single_cols_actual(),
                                                 Constants.sudoku_explicit_hidden_single_cols_expected())


def test_1explicit_sudoku_explicit_hidden_single_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.HiddenSingleFences(),
                                                 Constants.sudoku_explicit_hidden_single_fences_actual(),
                                                 Constants.sudoku_explicit_hidden_single_fences_expected())


def test_1explicit_sudoku_explicit_locked_candidates_pointing_3_fins_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesPointing(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_3_fins_rows_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_3_fins_rows_expected())


def test_1explicit_sudoku_explicit_locked_candidates_pointing_3_fins_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesPointing(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_3_fins_cols_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_3_fins_cols_expected())


def test_1explicit_sudoku_explicit_locked_candidates_pointing_2_fins_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesPointing(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_2_fins_rows_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_2_fins_rows_expected())


def test_1explicit_sudoku_explicit_locked_candidates_pointing_2_fins_cols_():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesPointing(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_2_fins_cols_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_pointing_2_fins_cols_expected())


def test_1explicit_sudoku_explicit_locked_candidates_claiming_3_fins_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesClaiming(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_3_fins_rows_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_3_fins_rows_expected())


def test_1explicit_sudoku_explicit_locked_candidates_claiming_2_fins_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesClaiming(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_2_fins_rows_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_2_fins_rows_expected())


def test_1explicit_sudoku_explicit_locked_candidates_claiming_2_fins_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesClaiming(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_2_fins_cols_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_2_fins_cols_expected())


def test_1explicit_sudoku_explicit_locked_candidates_claiming_3_fins_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.LockedCandidatesClaiming(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_3_fins_cols_actual(),
                                                 Constants.sudoku_explicit_locked_candidates_claiming_3_fins_cols_expected())


def test_1explicit_sudoku_explicit_naked_pair_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedPair(),
                                                 Constants.sudoku_explicit_naked_pair_rows_actual(),
                                                 Constants.sudoku_explicit_naked_pair_rows_expected())


def test_1explicit_sudoku_explicit_naked_pair_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedPair(),
                                                 Constants.sudoku_explicit_naked_pair_cols_actual(),
                                                 Constants.sudoku_explicit_naked_pair_cols_expected())


def test_1explicit_sudoku_explicit_naked_pair_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedPairFences(),
                                                 Constants.sudoku_explicit_naked_pair_fences_actual(),
                                                 Constants.sudoku_explicit_naked_pair_fences_expected())


def test_1explicit_sudoku_explicit_naked_triple_cols():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedTriple(),
                                                 Constants.sudoku_explicit_naked_triple_cols_actual(),
                                                 Constants.sudoku_explicit_naked_triple_cols_expected())


def test_1explicit_sudoku_explicit_naked_triple_rows():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedTriple(),
                                                 Constants.sudoku_explicit_naked_triple_rows_actual(),
                                                 Constants.sudoku_explicit_naked_triple_rows_expected())


def test_1explicit_sudoku_explicit_naked_triple_fences():
    assert default_test_explicit_actual_expected(Sudoku, Techs.NakedTriple(),
                                                 Constants.sudoku_explicit_naked_triple_fences_actual(),
                                                 Constants.sudoku_explicit_naked_triple_fences_expected())


def magnets_techniques() -> list:
    return []


def test_1explicit_magnets_zero_cols():
    assert default_test_explicit_actual_expected(Magnets, Techs.MagnetsZero(), Constants.magnets_zero_cols_actual(),
                                                 Constants.magnets_zero_cols_expected())


def test_1explicit_magnets_pairs():
    assert default_test_explicit_actual_expected(Magnets, Techs.MagnetsPair(), Constants.magnets_pairs_actual(),
                                                 Constants.magnets_pairs_expected())


def test_1explicit_magnets_full_house_even():
    assert default_test_explicit_actual_expected(Magnets, Techs.MagnetsFullHouse(),
                                                 Constants.magnets_full_house_even_actual(),
                                                 Constants.magnets_full_house_even_expected())


def test_1explicit_magnets_zero_rows():
    assert default_test_explicit_actual_expected(Magnets, Techs.MagnetsZero(), Constants.magnets_zero_rows_actual(),
                                                 Constants.magnets_zero_rows_expected())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_033():
    assert default_test_puzzle(Constants.magnets_033(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_034():
    assert default_test_puzzle(Constants.magnets_034(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_035():
    assert default_test_puzzle(Constants.magnets_035(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_036():
    assert default_test_puzzle(Constants.magnets_036(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_037():
    assert default_test_puzzle(Constants.magnets_037(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_038():
    assert default_test_puzzle(Constants.magnets_038(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_039():
    assert default_test_puzzle(Constants.magnets_039(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_040():
    assert default_test_puzzle(Constants.magnets_040(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_041():
    assert default_test_puzzle(Constants.magnets_041(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_042():
    assert default_test_puzzle(Constants.magnets_042(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_04():
    assert default_test_puzzle(Constants.magnets_04(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_044():
    assert default_test_puzzle(Constants.magnets_044(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_045():
    assert default_test_puzzle(Constants.magnets_045(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_046():
    assert default_test_puzzle(Constants.magnets_046(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_047():
    assert default_test_puzzle(Constants.magnets_047(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_048():
    assert default_test_puzzle(Constants.magnets_048(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_049():
    assert default_test_puzzle(Constants.magnets_049(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_050():
    assert default_test_puzzle(Constants.magnets_050(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_051():
    assert default_test_puzzle(Constants.magnets_051(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_052():
    assert default_test_puzzle(Constants.magnets_052(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_053():
    assert default_test_puzzle(Constants.magnets_053(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_054():
    assert default_test_puzzle(Constants.magnets_054(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_055():
    assert default_test_puzzle(Constants.magnets_055(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_056():
    assert default_test_puzzle(Constants.magnets_056(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_057():
    assert default_test_puzzle(Constants.magnets_057(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_058():
    assert default_test_puzzle(Constants.magnets_058(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_059():
    assert default_test_puzzle(Constants.magnets_059(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_060():
    assert default_test_puzzle(Constants.magnets_060(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_063():
    assert default_test_puzzle(Constants.magnets_063(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_082():
    assert default_test_puzzle(Constants.magnets_082(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_083():
    assert default_test_puzzle(Constants.magnets_083(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_119():
    assert default_test_puzzle(Constants.magnets_119(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_022():
    assert default_test_puzzle(Constants.magnets_022(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_023():
    assert default_test_puzzle(Constants.magnets_023(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_024():
    assert default_test_puzzle(Constants.magnets_024(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_025():
    assert default_test_puzzle(Constants.magnets_025(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_026():
    assert default_test_puzzle(Constants.magnets_026(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_027():
    assert default_test_puzzle(Constants.magnets_027(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_028():
    assert default_test_puzzle(Constants.magnets_028(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_029():
    assert default_test_puzzle(Constants.magnets_029(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_030():
    assert default_test_puzzle(Constants.magnets_030(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_031():
    assert default_test_puzzle(Constants.magnets_031(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_032():
    assert default_test_puzzle(Constants.magnets_032(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_015():
    assert default_test_puzzle(Constants.magnets_015(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_016():
    assert default_test_puzzle(Constants.magnets_016(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_017():
    assert default_test_puzzle(Constants.magnets_017(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_018():
    assert default_test_puzzle(Constants.magnets_018(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_019():
    assert default_test_puzzle(Constants.magnets_019(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_020():
    assert default_test_puzzle(Constants.magnets_020(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_021():
    assert default_test_puzzle(Constants.magnets_021(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_008():
    assert default_test_puzzle(Constants.magnets_008(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_009():
    assert default_test_puzzle(Constants.magnets_009(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_010():
    assert default_test_puzzle(Constants.magnets_010(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_011():
    assert default_test_puzzle(Constants.magnets_011(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_013():
    assert default_test_puzzle(Constants.magnets_013(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_012():
    assert default_test_puzzle(Constants.magnets_012(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_001():
    assert default_test_puzzle(Constants.magnets_001(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_002():
    assert default_test_puzzle(Constants.magnets_002(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_004():
    assert default_test_puzzle(Constants.magnets_004(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_005():
    assert default_test_puzzle(Constants.magnets_005(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_006():
    assert default_test_puzzle(Constants.magnets_006(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_007():
    assert default_test_puzzle(Constants.magnets_007(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_003():
    assert default_test_puzzle(Constants.magnets_003(), Magnets, magnets_techniques())


#


def kropki_techniques() -> list:
    return [
        Techs.KropkiBlack(),
        Techs.KropkiWhite(),
        Techs.KropkiEmpty(),
        Techs.KropkiNakedPair(),
    ]


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_001():
    assert default_test_puzzle(Constants.kropki_001(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_002():
    assert default_test_puzzle(Constants.kropki_002(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_003():
    assert default_test_puzzle(Constants.kropki_003(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_004():
    assert default_test_puzzle(Constants.kropki_004(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_005():
    assert default_test_puzzle(Constants.kropki_005(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_006():
    assert default_test_puzzle(Constants.kropki_006(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_007():
    assert default_test_puzzle(Constants.kropki_007(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_008():
    assert default_test_puzzle(Constants.kropki_008(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_009():
    assert default_test_puzzle(Constants.kropki_009(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_010():
    assert default_test_puzzle(Constants.kropki_010(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_011():
    assert default_test_puzzle(Constants.kropki_011(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_012():
    assert default_test_puzzle(Constants.kropki_012(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_013():
    assert default_test_puzzle(Constants.kropki_013(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_014():
    assert default_test_puzzle(Constants.kropki_014(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_015():
    assert default_test_puzzle(Constants.kropki_015(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_016():
    assert default_test_puzzle(Constants.kropki_016(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_017():
    assert default_test_puzzle(Constants.kropki_017(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_018():
    assert default_test_puzzle(Constants.kropki_018(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_019():
    assert default_test_puzzle(Constants.kropki_019(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_020():
    assert default_test_puzzle(Constants.kropki_020(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_021():
    assert default_test_puzzle(Constants.kropki_021(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kropki_022():
    assert default_test_puzzle(Constants.kropki_022(), Kropki, kropki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_ww():
    assert default_test_explicit_actual_expected(
        Kropki,
        Techs.KropkiWw(),
        Constants.kropki_explicit_ww_actual(),
        Constants.kropki_explicit_ww_expected())


def test_1explicit_kropki_explicit_bw():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiBw(),
                                                 Constants.kropki_explicit_bw_actual(),
                                                 Constants.kropki_explicit_bw_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_hidden_single():
    assert default_test_explicit_actual_expected(
        Kropki,
        Techs.KropkiHiddenSingle(),
        Constants.kropki_explicit_hidden_single_actual(),
        Constants.kropki_explicit_hidden_single_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_hidden_pair():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiHiddenPair(),
                                                 Constants.kropki_explicit_hidden_pair_actual(),
                                                 Constants.kropki_explicit_hidden_pair_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_hidden_triple():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiHiddenTriple(),
                                                 Constants.kropki_explicit_hidden_triple_actual(),
                                                 Constants.kropki_explicit_hidden_triple_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_hidden_quad():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiHiddenQuad(),
                                                 Constants.kropki_explicit_hidden_quad_actual(),
                                                 Constants.kropki_explicit_hidden_quad_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_naked_pair():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiNakedPair(),
                                                 Constants.kropki_explicit_naked_pair_actual(),
                                                 Constants.kropki_explicit_naked_pair_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_naked_triple():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiNakedTriple(),
                                                 Constants.kropki_explicit_naked_triple_actual(),
                                                 Constants.kropki_explicit_naked_triple_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_naked_quad():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiNakedQuad(),
                                                 Constants.kropki_explicit_naked_quad_actual(),
                                                 Constants.kropki_explicit_naked_quad_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_locked_candidates_pointing():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiLockedCandidatesPointing(),
                                                 Constants.kropki_explicit_locked_candidates_pointing_actual(),
                                                 Constants.kropki_explicit_locked_candidates_pointing_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_kropki_explicit_locked_candidates_claiming():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiLockedCandidatesClaiming(),
                                                 Constants.kropki_explicit_locked_candidates_claiming_actual(),
                                                 Constants.kropki_explicit_locked_candidates_claiming_expected())


def test_1explicit_kropki_explicit_black():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiBlack(),
                                                 Constants.kropki_explicit_black_actual(),
                                                 Constants.kropki_explicit_black_expected())


def test_1explicit_kropki_explicit_white():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiWhite(),
                                                 Constants.kropki_explicit_white_actual(),
                                                 Constants.kropki_explicit_white_expected())


def test_1explicit_kropki_explicit_empty():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiEmpty(), Constants.kropki_explicit_empty_actual(),
                                                 Constants.kropki_explicit_empty_expected())


def test_1explicit_kropki_explicit_bb():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiBb(), Constants.kropki_explicit_bb_actual(),
                                                 Constants.kropki_explicit_bb_expected())


def test_1explicit_kropki_explicit_dominating_empty1():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty1_actual(),
                                                 Constants.kropki_explicit_dominating_empty1_expected())


def test_1explicit_kropki_explicit_dominating_empty3():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty3_actual(),
                                                 Constants.kropki_explicit_dominating_empty3_expected())


def test_1explicit_kropki_explicit_dominating_empty4():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty4_actual(),
                                                 Constants.kropki_explicit_dominating_empty4_expected())


def test_1explicit_kropki_explicit_dominating_empty5():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty5_actual(),
                                                 Constants.kropki_explicit_dominating_empty5_expected())


def test_1explicit_kropki_explicit_dominating_empty6():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty6_actual(),
                                                 Constants.kropki_explicit_dominating_empty6_expected())


def test_1explicit_kropki_explicit_dominating_empty7():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty7_actual(),
                                                 Constants.kropki_explicit_dominating_empty7_expected())


def test_1explicit_kropki_explicit_dominating_empty8():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty8_actual(),
                                                 Constants.kropki_explicit_dominating_empty8_expected())


def test_1explicit_kropki_explicit_dominating_empty9():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDominatingEmpty(),
                                                 Constants.kropki_explicit_dominating_empty9_actual(),
                                                 Constants.kropki_explicit_dominating_empty9_expected())


def test_1explicit_kropki_explicit_diamond_wwwe():
    assert default_test_explicit_actual_expected(Kropki, Techs.KropkiDiamondWwwe(),
                                                 Constants.kropki_explicit_diamond_wwwe_actual(),
                                                 Constants.kropki_explicit_diamond_wwwe_expected())


def robot_fences_techniques() -> list:
    return [Techs.CrossHatchRobotFences(), Techs.HiddenSingleRobotFences()]


def test_puzzle_robot_fences_001():
    assert default_test_puzzle(Constants.robot_fences_001(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_002():
    assert default_test_puzzle(Constants.robot_fences_002(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_003():
    assert default_test_puzzle(Constants.robot_fences_003(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_004():
    assert default_test_puzzle(Constants.robot_fences_004(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_005():
    assert default_test_puzzle(Constants.robot_fences_005(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_006():
    assert default_test_puzzle(Constants.robot_fences_006(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_007():
    assert default_test_puzzle(Constants.robot_fences_007(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_008():
    assert default_test_puzzle(Constants.robot_fences_008(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_009():
    assert default_test_puzzle(Constants.robot_fences_009(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_010():
    assert default_test_puzzle(Constants.robot_fences_010(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_011():
    assert default_test_puzzle(Constants.robot_fences_011(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_012():
    assert default_test_puzzle(Constants.robot_fences_012(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_013():
    assert default_test_puzzle(Constants.robot_fences_013(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_014():
    assert default_test_puzzle(Constants.robot_fences_014(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_015():
    assert default_test_puzzle(Constants.robot_fences_015(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_016():
    assert default_test_puzzle(Constants.robot_fences_016(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_017():
    assert default_test_puzzle(Constants.robot_fences_017(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_018():
    assert default_test_puzzle(Constants.robot_fences_018(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_019():
    assert default_test_puzzle(Constants.robot_fences_019(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_020():
    assert default_test_puzzle(Constants.robot_fences_020(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_021():
    assert default_test_puzzle(Constants.robot_fences_021(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_022():
    assert default_test_puzzle(Constants.robot_fences_022(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_023():
    assert default_test_puzzle(Constants.robot_fences_023(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_024():
    assert default_test_puzzle(Constants.robot_fences_024(), RobotFences, robot_fences_techniques())


def test_puzzle_robot_fences_025():
    assert default_test_puzzle(Constants.robot_fences_025(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_026():
    assert default_test_puzzle(Constants.robot_fences_026(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_027():
    assert default_test_puzzle(Constants.robot_fences_027(), RobotFences, robot_fences_techniques())


# @pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_028():
    assert default_test_puzzle(Constants.robot_fences_028(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_029():
    assert default_test_puzzle(Constants.robot_fences_029(), RobotFences, robot_fences_techniques())


# @pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_030():
    assert default_test_puzzle(Constants.robot_fences_030(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_031():
    assert default_test_puzzle(Constants.robot_fences_031(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_032():
    assert default_test_puzzle(Constants.robot_fences_032(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_033():
    assert default_test_puzzle(Constants.robot_fences_033(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_034():
    assert default_test_puzzle(Constants.robot_fences_034(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_035():
    assert default_test_puzzle(Constants.robot_fences_035(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_036():
    assert default_test_puzzle(Constants.robot_fences_036(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_037():
    assert default_test_puzzle(Constants.robot_fences_037(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_038():
    assert default_test_puzzle(Constants.robot_fences_038(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_039():
    assert default_test_puzzle(Constants.robot_fences_039(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_040():
    assert default_test_puzzle(Constants.robot_fences_040(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_041():
    assert default_test_puzzle(Constants.robot_fences_041(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_042():
    assert default_test_puzzle(Constants.robot_fences_042(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_043():
    assert default_test_puzzle(Constants.robot_fences_043(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_044():
    assert default_test_puzzle(Constants.robot_fences_044(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_045():
    assert default_test_puzzle(Constants.robot_fences_045(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_046():
    assert default_test_puzzle(Constants.robot_fences_046(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_047():
    assert default_test_puzzle(Constants.robot_fences_047(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_048():
    assert default_test_puzzle(Constants.robot_fences_048(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_049():
    assert default_test_puzzle(Constants.robot_fences_049(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_050():
    assert default_test_puzzle(Constants.robot_fences_050(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_051():
    assert default_test_puzzle(Constants.robot_fences_051(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_052():
    assert default_test_puzzle(Constants.robot_fences_052(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_053():
    assert default_test_puzzle(Constants.robot_fences_053(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_054():
    assert default_test_puzzle(Constants.robot_fences_054(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_055():
    assert default_test_puzzle(Constants.robot_fences_055(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_056():
    assert default_test_puzzle(Constants.robot_fences_056(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_057():
    assert default_test_puzzle(Constants.robot_fences_057(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_058():
    assert default_test_puzzle(Constants.robot_fences_058(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_059():
    assert default_test_puzzle(Constants.robot_fences_059(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_060():
    assert default_test_puzzle(Constants.robot_fences_060(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_061():
    assert default_test_puzzle(Constants.robot_fences_061(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_062():
    assert default_test_puzzle(Constants.robot_fences_062(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_063():
    assert default_test_puzzle(Constants.robot_fences_063(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_064():
    assert default_test_puzzle(Constants.robot_fences_064(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_065():
    assert default_test_puzzle(Constants.robot_fences_065(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_066():
    assert default_test_puzzle(Constants.robot_fences_066(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_067():
    assert default_test_puzzle(Constants.robot_fences_067(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_068():
    assert default_test_puzzle(Constants.robot_fences_068(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_069():
    assert default_test_puzzle(Constants.robot_fences_069(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_070():
    assert default_test_puzzle(Constants.robot_fences_070(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_071():
    assert default_test_puzzle(Constants.robot_fences_071(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_072():
    assert default_test_puzzle(Constants.robot_fences_072(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_073():
    assert default_test_puzzle(Constants.robot_fences_073(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_074():
    assert default_test_puzzle(Constants.robot_fences_074(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_075():
    assert default_test_puzzle(Constants.robot_fences_075(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_076():
    assert default_test_puzzle(Constants.robot_fences_076(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_077():
    assert default_test_puzzle(Constants.robot_fences_077(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_078():
    assert default_test_puzzle(Constants.robot_fences_078(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_079():
    assert default_test_puzzle(Constants.robot_fences_079(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_080():
    assert default_test_puzzle(Constants.robot_fences_080(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_081():
    assert default_test_puzzle(Constants.robot_fences_081(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_082():
    assert default_test_puzzle(Constants.robot_fences_082(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_083():
    assert default_test_puzzle(Constants.robot_fences_083(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_084():
    assert default_test_puzzle(Constants.robot_fences_084(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_085():
    assert default_test_puzzle(Constants.robot_fences_085(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_086():
    assert default_test_puzzle(Constants.robot_fences_086(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_087():
    assert default_test_puzzle(Constants.robot_fences_087(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_088():
    assert default_test_puzzle(Constants.robot_fences_088(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_089():
    assert default_test_puzzle(Constants.robot_fences_089(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_090():
    assert default_test_puzzle(Constants.robot_fences_090(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_091():
    assert default_test_puzzle(Constants.robot_fences_091(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_092():
    assert default_test_puzzle(Constants.robot_fences_092(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_093():
    assert default_test_puzzle(Constants.robot_fences_093(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_094():
    assert default_test_puzzle(Constants.robot_fences_094(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_095():
    assert default_test_puzzle(Constants.robot_fences_095(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_096():
    assert default_test_puzzle(Constants.robot_fences_096(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_097():
    assert default_test_puzzle(Constants.robot_fences_097(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_098():
    assert default_test_puzzle(Constants.robot_fences_098(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_099():
    assert default_test_puzzle(Constants.robot_fences_099(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_100():
    assert default_test_puzzle(Constants.robot_fences_100(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_101():
    assert default_test_puzzle(Constants.robot_fences_101(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_102():
    assert default_test_puzzle(Constants.robot_fences_102(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_103():
    assert default_test_puzzle(Constants.robot_fences_103(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_104():
    assert default_test_puzzle(Constants.robot_fences_104(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_105():
    assert default_test_puzzle(Constants.robot_fences_105(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_106():
    assert default_test_puzzle(Constants.robot_fences_106(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_107():
    assert default_test_puzzle(Constants.robot_fences_107(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_108():
    assert default_test_puzzle(Constants.robot_fences_108(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_109():
    assert default_test_puzzle(Constants.robot_fences_109(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_110():
    assert default_test_puzzle(Constants.robot_fences_110(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_111():
    assert default_test_puzzle(Constants.robot_fences_111(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_112():
    assert default_test_puzzle(Constants.robot_fences_112(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_113():
    assert default_test_puzzle(Constants.robot_fences_113(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_114():
    assert default_test_puzzle(Constants.robot_fences_114(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_115():
    assert default_test_puzzle(Constants.robot_fences_115(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_116():
    assert default_test_puzzle(Constants.robot_fences_116(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_117():
    assert default_test_puzzle(Constants.robot_fences_117(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_118():
    assert default_test_puzzle(Constants.robot_fences_118(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_119():
    assert default_test_puzzle(Constants.robot_fences_119(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_120():
    assert default_test_puzzle(Constants.robot_fences_120(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_121():
    assert default_test_puzzle(Constants.robot_fences_121(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_122():
    assert default_test_puzzle(Constants.robot_fences_122(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_123():
    assert default_test_puzzle(Constants.robot_fences_123(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_124():
    assert default_test_puzzle(Constants.robot_fences_124(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_125():
    assert default_test_puzzle(Constants.robot_fences_125(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_126():
    assert default_test_puzzle(Constants.robot_fences_126(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_127():
    assert default_test_puzzle(Constants.robot_fences_127(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_128():
    assert default_test_puzzle(Constants.robot_fences_128(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_129():
    assert default_test_puzzle(Constants.robot_fences_129(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_130():
    assert default_test_puzzle(Constants.robot_fences_130(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_131():
    assert default_test_puzzle(Constants.robot_fences_131(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_132():
    assert default_test_puzzle(Constants.robot_fences_132(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_133():
    assert default_test_puzzle(Constants.robot_fences_133(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_134():
    assert default_test_puzzle(Constants.robot_fences_134(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_135():
    assert default_test_puzzle(Constants.robot_fences_135(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_136():
    assert default_test_puzzle(Constants.robot_fences_136(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_137():
    assert default_test_puzzle(Constants.robot_fences_137(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_138():
    assert default_test_puzzle(Constants.robot_fences_138(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_139():
    assert default_test_puzzle(Constants.robot_fences_139(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_140():
    assert default_test_puzzle(Constants.robot_fences_140(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_141():
    assert default_test_puzzle(Constants.robot_fences_141(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_142():
    assert default_test_puzzle(Constants.robot_fences_142(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_143():
    assert default_test_puzzle(Constants.robot_fences_143(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_144():
    assert default_test_puzzle(Constants.robot_fences_144(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_145():
    assert default_test_puzzle(Constants.robot_fences_145(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_146():
    assert default_test_puzzle(Constants.robot_fences_146(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_147():
    assert default_test_puzzle(Constants.robot_fences_147(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_148():
    assert default_test_puzzle(Constants.robot_fences_148(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_149():
    assert default_test_puzzle(Constants.robot_fences_149(), RobotFences, robot_fences_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_fences_150():
    assert default_test_puzzle(Constants.robot_fences_150(), RobotFences, robot_fences_techniques())


Techs = Techs
Constants = Constants


class Parks2:
    def ConstantsinitConstants(self, puzzle: str) -> None:
        pass


def parks1_techniques() -> list:
    return [
        Techs.Parks1CrossHatch(),
        Techs.Parks1HiddenSingle(),
        Techs.Parks1CrossHatchTouching(),
        Techs.Parks1LockedCandidatesPointing(),
        # Techs.Parks1LockedCandidatesClaiming(),
        Techs.Parks1Bent3(),
        Techs.Parks1Shape_00_01()
    ]


def parks2_techniques() -> list:
    return []


def test_puzzle_parks1_001():
    assert default_test_puzzle(Constants.parks1_001(), Parks1, parks1_techniques())


def test_puzzle_parks1_002():
    assert default_test_puzzle(Constants.parks1_002(), Parks1, parks1_techniques())


def test_puzzle_parks1_003():
    assert default_test_puzzle(Constants.parks1_003(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_004():
    assert default_test_puzzle(Constants.parks1_004(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_005():
    assert default_test_puzzle(Constants.parks1_005(), Parks1, parks1_techniques())


# @pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_006():
    assert default_test_puzzle(Constants.parks1_006(), Parks1, parks1_techniques())


# @pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_007():
    assert default_test_puzzle(Constants.parks1_007(), Parks1, parks1_techniques())


# @pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_008():
    assert default_test_puzzle(Constants.parks1_008(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_009():
    assert default_test_puzzle(Constants.parks1_009(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_010():
    assert default_test_puzzle(Constants.parks1_010(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_011():
    assert default_test_puzzle(Constants.parks1_011(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_012():
    assert default_test_puzzle(Constants.parks1_012(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_013():
    assert default_test_puzzle(Constants.parks1_013(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_014():
    assert default_test_puzzle(Constants.parks1_014(), Parks1, parks1_techniques())


def test_puzzle_parks1_beach_001():
    assert default_test_puzzle(Constants.parks1_beach_001(), Parks1, parks1_techniques())


def test_puzzle_parks1_beach_002():
    assert default_test_puzzle(Constants.parks1_beach_002(), Parks1, parks1_techniques())


def test_puzzle_parks1_beach_003():
    assert default_test_puzzle(Constants.parks1_beach_003(), Parks1, parks1_techniques())


def test_puzzle_parks1_beach_004():
    assert default_test_puzzle(Constants.parks1_beach_004(), Parks1, parks1_techniques())


def test_puzzle_parks1_maui_001():
    assert default_test_puzzle(Constants.parks1_maui_001(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_001():
    assert default_test_puzzle(Constants.parks1_spring_001(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_002():
    assert default_test_puzzle(Constants.parks1_spring_002(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_003():
    assert default_test_puzzle(Constants.parks1_spring_003(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_004():
    assert default_test_puzzle(Constants.parks1_spring_004(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_005():
    assert default_test_puzzle(Constants.parks1_spring_005(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_006():
    assert default_test_puzzle(Constants.parks1_spring_006(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_007():
    assert default_test_puzzle(Constants.parks1_spring_007(), Parks1, parks1_techniques())


def test_puzzle_parks1_spring_008():
    assert default_test_puzzle(Constants.parks1_spring_008(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_009():
    assert default_test_puzzle(Constants.parks1_spring_009(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_010():
    assert default_test_puzzle(Constants.parks1_spring_010(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_011():
    assert default_test_puzzle(Constants.parks1_spring_011(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_012():
    assert default_test_puzzle(Constants.parks1_spring_012(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_013():
    assert default_test_puzzle(Constants.parks1_spring_013(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_014():
    assert default_test_puzzle(Constants.parks1_spring_014(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_015():
    assert default_test_puzzle(Constants.parks1_spring_015(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_016():
    assert default_test_puzzle(Constants.parks1_spring_016(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_017():
    assert default_test_puzzle(Constants.parks1_spring_017(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_018():
    assert default_test_puzzle(Constants.parks1_spring_018(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_019():
    assert default_test_puzzle(Constants.parks1_spring_019(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_020():
    assert default_test_puzzle(Constants.parks1_spring_020(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_021():
    assert default_test_puzzle(Constants.parks1_spring_021(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_022():
    assert default_test_puzzle(Constants.parks1_spring_022(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_023():
    assert default_test_puzzle(Constants.parks1_spring_023(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_024():
    assert default_test_puzzle(Constants.parks1_spring_024(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_025():
    assert default_test_puzzle(Constants.parks1_spring_025(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_026():
    assert default_test_puzzle(Constants.parks1_spring_026(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_027():
    assert default_test_puzzle(Constants.parks1_spring_027(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_028():
    assert default_test_puzzle(Constants.parks1_spring_028(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_029():
    assert default_test_puzzle(Constants.parks1_spring_029(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_030():
    assert default_test_puzzle(Constants.parks1_spring_030(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_031():
    assert default_test_puzzle(Constants.parks1_spring_031(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_032():
    assert default_test_puzzle(Constants.parks1_spring_032(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_033():
    assert default_test_puzzle(Constants.parks1_spring_033(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_034():
    assert default_test_puzzle(Constants.parks1_spring_034(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_039():
    assert default_test_puzzle(Constants.parks1_spring_039(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_045():
    assert default_test_puzzle(Constants.parks1_spring_045(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_046():
    assert default_test_puzzle(Constants.parks1_spring_046(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_047():
    assert default_test_puzzle(Constants.parks1_spring_047(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_051():
    assert default_test_puzzle(Constants.parks1_spring_051(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_spring_062():
    assert default_test_puzzle(Constants.parks1_spring_062(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_037():
    assert default_test_puzzle(Constants.parks1_winter_037(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_038():
    assert default_test_puzzle(Constants.parks1_winter_038(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_039():
    assert default_test_puzzle(Constants.parks1_winter_039(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_040():
    assert default_test_puzzle(Constants.parks1_winter_040(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_041():
    assert default_test_puzzle(Constants.parks1_winter_041(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_042():
    assert default_test_puzzle(Constants.parks1_winter_042(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_044():
    assert default_test_puzzle(Constants.parks1_winter_044(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_045():
    assert default_test_puzzle(Constants.parks1_winter_045(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_046():
    assert default_test_puzzle(Constants.parks1_winter_046(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_047():
    assert default_test_puzzle(Constants.parks1_winter_047(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_048():
    assert default_test_puzzle(Constants.parks1_winter_048(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_049():
    assert default_test_puzzle(Constants.parks1_winter_049(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_050():
    assert default_test_puzzle(Constants.parks1_winter_050(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks1_winter_051():
    assert default_test_puzzle(Constants.parks1_winter_051(), Parks1, parks1_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_015():
    assert default_test_puzzle(Constants.parks2_015(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_016():
    assert default_test_puzzle(Constants.parks2_016(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_017():
    assert default_test_puzzle(Constants.parks2_017(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_018():
    assert default_test_puzzle(Constants.parks2_018(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_019():
    assert default_test_puzzle(Constants.parks2_019(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_020():
    assert default_test_puzzle(Constants.parks2_020(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_021():
    assert default_test_puzzle(Constants.parks2_021(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_022():
    assert default_test_puzzle(Constants.parks2_022(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_023():
    assert default_test_puzzle(Constants.parks2_023(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_024():
    assert default_test_puzzle(Constants.parks2_024(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_025():
    assert default_test_puzzle(Constants.parks2_025(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_026():
    assert default_test_puzzle(Constants.parks2_026(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_027():
    assert default_test_puzzle(Constants.parks2_027(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_028():
    assert default_test_puzzle(Constants.parks2_028(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_029():
    assert default_test_puzzle(Constants.parks2_029(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_030():
    assert default_test_puzzle(Constants.parks2_030(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_031():
    assert default_test_puzzle(Constants.parks2_031(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_032():
    assert default_test_puzzle(Constants.parks2_032(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_033():
    assert default_test_puzzle(Constants.parks2_033(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_034():
    assert default_test_puzzle(Constants.parks2_034(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_035():
    assert default_test_puzzle(Constants.parks2_035(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_036():
    assert default_test_puzzle(Constants.parks2_036(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_037():
    assert default_test_puzzle(Constants.parks2_037(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_038():
    assert default_test_puzzle(Constants.parks2_038(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_039():
    assert default_test_puzzle(Constants.parks2_039(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_040():
    assert default_test_puzzle(Constants.parks2_040(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_parks2_041():
    assert default_test_puzzle(Constants.parks2_041(), Parks2, parks2_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_parks1_explicit_hidden_single():
    assert default_test_explicit_actual_expected(
        Parks1,
        Techs.Parks1HiddenSingle(),
        Constants.parks1_explicit_hidden_single_actual(),
        Constants.parks1_explicit_hidden_single_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_parks1_explicit_cross_hatch():
    assert default_test_explicit_actual_expected(
        Parks1,
        Techs.Parks1CrossHatch(),
        Constants.parks1_explicit_cross_hatch_actual(),
        Constants.parks1_explicit_cross_hatch_expected())


def tenner_techniques() -> list:
    return [Techs.TennerCrossHatch(),
            Techs.TennerNakedPair(),
            Techs.TennerHiddenPair(),
            Techs.TennerHiddenSingle(),
            Techs.TennerTotalHiddenSingle(),
            Techs.TennerPowerSetTotals(),
            Techs.TennerNakedPairColumn()]


def test_puzzle_tenner_001():
    assert default_test_puzzle(Constants.tenner_001(), Tenner, tenner_techniques())


def test_puzzle_tenner_002():
    assert default_test_puzzle(Constants.tenner_002(), Tenner, tenner_techniques())


def test_puzzle_tenner_003():
    assert default_test_puzzle(Constants.tenner_003(), Tenner, tenner_techniques())


def test_puzzle_tenner_004():
    assert default_test_puzzle(Constants.tenner_004(), Tenner, tenner_techniques())


def test_puzzle_tenner_005():
    assert default_test_puzzle(Constants.tenner_005(), Tenner, tenner_techniques())


def test_puzzle_tenner_006():
    assert default_test_puzzle(Constants.tenner_006(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_007():
    assert default_test_puzzle(Constants.tenner_007(), Tenner, tenner_techniques())


def test_puzzle_tenner_008():
    assert default_test_puzzle(Constants.tenner_008(), Tenner, tenner_techniques())


def test_puzzle_tenner_009():
    assert default_test_puzzle(Constants.tenner_009(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_010():
    assert default_test_puzzle(Constants.tenner_010(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_011():
    assert default_test_puzzle(Constants.tenner_011(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_012():
    assert default_test_puzzle(Constants.tenner_012(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_013():
    assert default_test_puzzle(Constants.tenner_013(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_014():
    assert default_test_puzzle(Constants.tenner_014(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_015():
    assert default_test_puzzle(Constants.tenner_015(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_016():
    assert default_test_puzzle(Constants.tenner_016(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_017():
    assert default_test_puzzle(Constants.tenner_017(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_018():
    assert default_test_puzzle(Constants.tenner_018(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_019():
    assert default_test_puzzle(Constants.tenner_019(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_020():
    assert default_test_puzzle(Constants.tenner_020(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_021():
    assert default_test_puzzle(Constants.tenner_021(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_022():
    assert default_test_puzzle(Constants.tenner_022(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_023():
    assert default_test_puzzle(Constants.tenner_023(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_024():
    assert default_test_puzzle(Constants.tenner_024(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_challenging_001():
    assert default_test_puzzle(Constants.tenner_challenging_001(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_challenging_002():
    assert default_test_puzzle(Constants.tenner_challenging_002(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_challenging_003():
    assert default_test_puzzle(Constants.tenner_challenging_003(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_challenging_004():
    assert default_test_puzzle(Constants.tenner_challenging_004(), Tenner, tenner_techniques())


def test_puzzle_tenner_easier_001():
    assert default_test_puzzle(Constants.tenner_easier_001(), Tenner, tenner_techniques())


def test_puzzle_tenner_easier_002():
    assert default_test_puzzle(Constants.tenner_easier_002(), Tenner, tenner_techniques())


def test_puzzle_tenner_easier_003():
    assert default_test_puzzle(Constants.tenner_easier_003(), Tenner, tenner_techniques())


def test_puzzle_tenner_easier_004():
    assert default_test_puzzle(Constants.tenner_easier_004(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_harder_001():
    assert default_test_puzzle(Constants.tenner_harder_001(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_harder_002():
    assert default_test_puzzle(Constants.tenner_harder_002(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_harder_003():
    assert default_test_puzzle(Constants.tenner_harder_003(), Tenner, tenner_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tenner_harder_004():
    assert default_test_puzzle(Constants.tenner_harder_004(), Tenner, tenner_techniques())


class AbstractPainting:
    pass


def abstractpainting_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_017():
    assert default_test_puzzle(Constants.abstractpainting_017(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_018():
    assert default_test_puzzle(Constants.abstractpainting_018(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_019():
    assert default_test_puzzle(Constants.abstractpainting_019(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_025():
    assert default_test_puzzle(Constants.abstractpainting_025(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_027():
    assert default_test_puzzle(Constants.abstractpainting_027(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_028():
    assert default_test_puzzle(Constants.abstractpainting_028(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_029():
    assert default_test_puzzle(Constants.abstractpainting_029(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_030():
    assert default_test_puzzle(Constants.abstractpainting_030(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_031():
    assert default_test_puzzle(Constants.abstractpainting_031(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_035():
    assert default_test_puzzle(Constants.abstractpainting_035(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_036():
    assert default_test_puzzle(Constants.abstractpainting_036(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_051():
    assert default_test_puzzle(Constants.abstractpainting_051(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_101():
    assert default_test_puzzle(Constants.abstractpainting_101(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_151():
    assert default_test_puzzle(Constants.abstractpainting_151(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_191():
    assert default_test_puzzle(Constants.abstractpainting_191(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_009():
    assert default_test_puzzle(Constants.abstractpainting_009(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_010():
    assert default_test_puzzle(Constants.abstractpainting_010(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_011():
    assert default_test_puzzle(Constants.abstractpainting_011(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_012():
    assert default_test_puzzle(Constants.abstractpainting_012(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_013():
    assert default_test_puzzle(Constants.abstractpainting_013(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_014():
    assert default_test_puzzle(Constants.abstractpainting_014(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_015():
    assert default_test_puzzle(Constants.abstractpainting_015(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_016():
    assert default_test_puzzle(Constants.abstractpainting_016(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_001():
    assert default_test_puzzle(Constants.abstractpainting_001(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_002():
    assert default_test_puzzle(Constants.abstractpainting_002(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_003():
    assert default_test_puzzle(Constants.abstractpainting_003(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_004():
    assert default_test_puzzle(Constants.abstractpainting_004(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_005():
    assert default_test_puzzle(Constants.abstractpainting_005(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_006():
    assert default_test_puzzle(Constants.abstractpainting_006(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_007():
    assert default_test_puzzle(Constants.abstractpainting_007(), AbstractPainting, abstractpainting_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_abstractpainting_008():
    assert default_test_puzzle(Constants.abstractpainting_008(), AbstractPainting, abstractpainting_techniques())


class BattleShips:
    pass


def battle_ships_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_battle_ships_super_tanker_003():
    assert default_test_puzzle(Constants.battle_ships_super_tanker_003(), BattleShips, battle_ships_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_battle_ships_001():
    assert default_test_puzzle(Constants.battle_ships_001(), BattleShips, battle_ships_techniques())


# def botanical_park

@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_001():
    assert default_test_puzzle(Constants.botanical_park_001(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_002():
    assert default_test_puzzle(Constants.botanical_park_002(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_003():
    assert default_test_puzzle(Constants.botanical_park_003(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_004():
    assert default_test_puzzle(Constants.botanical_park_004(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_005():
    assert default_test_puzzle(Constants.botanical_park_005(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_006():
    assert default_test_puzzle(Constants.botanical_park_006(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_007():
    assert default_test_puzzle(Constants.botanical_park_007(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_007():
    assert default_test_puzzle(Constants.botanical_park_007(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_008():
    assert default_test_puzzle(Constants.botanical_park_008(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_009():
    assert default_test_puzzle(Constants.botanical_park_009(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_010():
    assert default_test_puzzle(Constants.botanical_park_010(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_011():
    assert default_test_puzzle(Constants.botanical_park_011(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_botanical_park_011():
    assert default_test_puzzle(Constants.botanical_park_011(), Walls, walls_techniques())


class Clouds:
    pass


def clouds_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_clouds_001():
    assert default_test_puzzle(Constants.clouds_001(), Clouds, clouds_techniques())


class Futoshiki:
    def ConstantsinitConstants(self, puzzle: str) -> None:
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            # print(temp)

            array.append(temp)
        self.Constantsid = array[0]
        self.Constantslength = int(array[1])
        array.pop(0)
        array.pop(0)
        self.Constantsgrid = []
        for r in range(self.Constantslength * 2 - 1):
            line = array[0].strip().replace("  ", " ", -1).split(" ")
            print(line)
            self.Constantsgrid.append(line)
            array.pop(0)

        # print("/////")
        # print(array)

    def id(self) -> str:
        return self.Constantsid

    @property
    def length(self):
        return self.Constantslength

    def cell_string(self, loc: Loc) -> str:
        return self.Constantsgrid[loc.row][loc.col]

    def cell_candidates(self, loc: Loc) -> list[int]:
        return [int(s) for s in self.Constantsgrid[loc.row][loc.col] if s.isnumeric()]

    def rem(self, locs: list[Loc], candidates: list) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.Constantsgrid[loc.row][loc.col] = self.Constantsgrid[loc.row][loc.col].replace(candidate, "_")
                edits += 1

        return edits

    def ConstantsstrConstants(self):
        string = f'{self.Constantsid}\n'
        string += f'{self.Constantslength}\n'

        for r in range(self.Constantslength * 2 - 1):
            for c in range(self.Constantslength * 2 - 1):
                string += f'{self.Constantsgrid[r][c]} '
            string += '\n'
        return string


class FutoshikiGreaterThanLessThan:  # (BaseFutoshikiTechnique):
    def solve0(self, puzzle: Futoshiki) -> int:
        edits = 0

        for r in range(puzzle.length * 2 - 1):
            for c in range(puzzle.length * 2 - 1):

                even_row = r % 2 == 0
                even_col = c % 2 == 0

                if even_row and even_col:
                    continue

                if not even_row and not even_col:
                    continue

                if even_row:
                    loc = Loc(r, c)
                    string = puzzle.cell_string(loc)

                    if string == '>':
                        edits += self.solve_greater_than(puzzle, loc.east(), loc.west())

                    # print(puzzle.cell_string(loc))
        # for row_house in puzzle.house_row_cells()

        return edits

    def solve_greater_than(self, puzzle: Futoshiki, lesser: Loc, greater: Loc):
        edits = 0
        lesser_candidates = puzzle.cell_candidates(lesser)
        greater_candidates = puzzle.cell_candidates(greater)

        min_greater = min(greater_candidates)
        max_lesser = max(lesser_candidates)

        print(min_greater)
        print(max_lesser)

        for candidate in lesser_candidates:
            if candidate >= min_greater:
                print(f'removing {candidate} from {lesser}')
                edits += puzzle.rem([lesser], [str(candidate)])

        # print(lesser_candidates)
        # print(greater_candidates)

        return edits


def futoshiki_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_futoshiki_explicit_cross_hatch():
    assert default_test_explicit_actual_expected(Futoshiki, Techs.FutoshikiCrossHatch(),
                                                 Constants.futoshiki_explicit_cross_hatch_actual(),
                                                 Constants.futoshiki_explicit_cross_hatch_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_futoshiki_explicit_hidden_single():
    assert default_test_explicit_actual_expected(Futoshiki, Techs.FutoshikiHiddenSingle(),
                                                 Constants.futoshiki_explicit_hidden_single_actual(),
                                                 Constants.futoshiki_explicit_hidden_single_expected())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_001():
    assert default_test_puzzle(Constants.futoshiki_001(), Futoshiki, futoshiki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_002():
    assert default_test_puzzle(Constants.futoshiki_002(), Futoshiki, futoshiki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_003():
    assert default_test_puzzle(Constants.futoshiki_003(), Futoshiki, futoshiki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_015():
    assert default_test_puzzle(Constants.futoshiki_015(), Futoshiki, futoshiki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_023():
    assert default_test_puzzle(Constants.futoshiki_023(), Futoshiki, futoshiki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_010():
    assert default_test_puzzle(Constants.futoshiki_010(), Futoshiki, futoshiki_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_futoshiki_001():
    assert default_test_puzzle(Constants.futoshiki_001(), Futoshiki, futoshiki_techniques())


class HiddenStars:
    pass


def hidden_stars_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_001():
    assert default_test_puzzle(Constants.hidden_stars_001(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_002():
    assert default_test_puzzle(Constants.hidden_stars_002(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_003():
    assert default_test_puzzle(Constants.hidden_stars_003(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_004():
    assert default_test_puzzle(Constants.hidden_stars_004(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_005():
    assert default_test_puzzle(Constants.hidden_stars_005(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_006():
    assert default_test_puzzle(Constants.hidden_stars_006(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_007():
    assert default_test_puzzle(Constants.hidden_stars_007(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_008():
    assert default_test_puzzle(Constants.hidden_stars_008(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_009():
    assert default_test_puzzle(Constants.hidden_stars_009(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_010():
    assert default_test_puzzle(Constants.hidden_stars_010(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_011():
    assert default_test_puzzle(Constants.hidden_stars_011(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_012():
    assert default_test_puzzle(Constants.hidden_stars_012(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_013():
    assert default_test_puzzle(Constants.hidden_stars_013(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_014():
    assert default_test_puzzle(Constants.hidden_stars_014(), HiddenStars, hidden_stars_techniques())


class Kakuro:
    pass


def kakuro_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_kakuro_001():
    assert default_test_puzzle(Constants.kakuro_001(), Kakuro, kakuro_techniques())


class Knightoku:  # (Sudoku):
    def ConstantsinitConstants(self, puzzle: str) -> None:
        super().ConstantsinitConstants(puzzle)




def knightoku_techniques() -> list:
    return [Techs.CrossHatchKnightoku()] + sudoku_techniques()


# from test_and_tests import Ex
@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_001():
    assert default_test_puzzle(Constants.knightoku_001(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_002():
    assert default_test_puzzle(Constants.knightoku_002(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_003():
    assert default_test_puzzle(Constants.knightoku_003(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_004():
    assert default_test_puzzle(Constants.knightoku_004(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_005():
    assert default_test_puzzle(Constants.knightoku_005(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_006():
    assert default_test_puzzle(Constants.knightoku_006(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_008():
    assert default_test_puzzle(Constants.knightoku_008(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_009():
    assert default_test_puzzle(Constants.knightoku_009(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_010():
    assert default_test_puzzle(Constants.knightoku_010(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_011():
    assert default_test_puzzle(Constants.knightoku_011(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_013():
    assert default_test_puzzle(Constants.knightoku_013(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_014():
    assert default_test_puzzle(Constants.knightoku_014(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_015():
    assert default_test_puzzle(Constants.knightoku_015(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_016():
    assert default_test_puzzle(Constants.knightoku_016(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_017():
    assert default_test_puzzle(Constants.knightoku_017(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_014():
    assert default_test_puzzle(Constants.knightoku_014(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_019():
    assert default_test_puzzle(Constants.knightoku_019(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_020():
    assert default_test_puzzle(Constants.knightoku_020(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_021():
    assert default_test_puzzle(Constants.knightoku_021(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_022():
    assert default_test_puzzle(Constants.knightoku_022(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_023():
    assert default_test_puzzle(Constants.knightoku_023(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_025():
    assert default_test_puzzle(Constants.knightoku_025(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_026():
    assert default_test_puzzle(Constants.knightoku_026(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_027():
    assert default_test_puzzle(Constants.knightoku_027(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_028():
    assert default_test_puzzle(Constants.knightoku_028(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_029():
    assert default_test_puzzle(Constants.knightoku_029(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_030():
    assert default_test_puzzle(Constants.knightoku_030(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_031():
    assert default_test_puzzle(Constants.knightoku_031(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_032():
    assert default_test_puzzle(Constants.knightoku_032(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_034():
    assert default_test_puzzle(Constants.knightoku_034(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_035():
    assert default_test_puzzle(Constants.knightoku_035(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_037():
    assert default_test_puzzle(Constants.knightoku_037(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_038():
    assert default_test_puzzle(Constants.knightoku_038(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_041():
    assert default_test_puzzle(Constants.knightoku_041(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_042():
    assert default_test_puzzle(Constants.knightoku_042(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_043():
    assert default_test_puzzle(Constants.knightoku_043(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_044():
    assert default_test_puzzle(Constants.knightoku_044(), Knightoku, knightoku_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_knightoku_045():
    assert default_test_puzzle(Constants.knightoku_045(), Knightoku, knightoku_techniques())


class LightenUp:  # (Sudoku):
    def ConstantsinitConstants(self, puzzle: str) -> None:
        super().__init__(puzzle)
        self.Constantsgrid = []
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)

        # for r in range(self.length):
        #     for c in range(self.length):
        #         loc = Loc(r, c)

        for temp in array:
            print(temp)

        # for row in range(self.length + 1):
        #     temp = []
        #     split = array[row].replace("\r", " ", -1).replace("\t", " ", -1).replace("  ", " ", -1).strip().split(' ')
        #     for t in split:
        #         if len(t) == 0:
        #             continue
        #         temp.append(t)
        #     self.Constantsgrid.append(temp)

    @property
    def col_length(self) -> int:
        return 10

    def is_row_house_solved(self, row: int) -> bool:
        solved_candidates = set(
            [self.cell_candidates(loc)[0] for loc in self.house_row_cell_locs(row) if self.is_cell_solved(loc)])
        return solved_candidates.issuperset(self.expected_candidates()) and solved_candidates.issubset(
            self.expected_candidates())

    def is_col_house_solved(self, col: int) -> bool:
        solved_candidates = [
            self.cell_candidates(loc)[0]
            for loc in self.house_col_cell_locs(col)
            if self.is_cell_solved(loc)
        ]
        if len(solved_candidates) != self.length:
            return False
        total = self.total(col)
        if total is None:
            return True
        return sum(solved_candidates) == total

    def is_solved(self) -> bool:
        return False
        for row in range(self.length):
            if not self.is_row_house_solved(row):
                print(f'print bad row: {row}')

                return False

        for col in range(self.col_length):
            if not self.is_col_house_solved(col):
                print(f'print bad col: {col}')
                return False

        for r in range(self.length):
            for c in range(self.col_length):
                cell = Loc(r, c)
                if not self.is_cell_solved(cell):
                    # print(f'{self.Constantsgrid[r][c]}///////////////////////////')
                    return False
                solved_candidate = self.cell_candidates(cell)[0]
                directions = [
                    cell.north(),
                    cell.east(),
                    cell.south(),
                    cell.west(),
                    cell.north().east(),
                    cell.north().west(),
                    cell.south().east(),
                    cell.south().west()
                ]
                for direction in directions:
                    if direction.row < 0 or direction.col < 0:
                        continue
                    if direction.row >= self.length or direction.col >= 10:
                        continue

                    if not self.is_cell_solved(direction):
                        return False

                    other = self.cell_candidates(direction)[0]

                    if other == solved_candidate:
                        print(f'{cell} {direction}')
                        return False

        return True

    def expected_candidates(self) -> list:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def ConstantsstrConstants(self):
        string = f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.length + 1):
            for c in range(self.col_length):
                string += f'{self.Constantsgrid[r][c].ljust(self.col_length)} '
            string += '\n'
        return string

    def house_row_cell_locs(self, loc_row: Union[int, Loc]) -> list[Loc]:
        if isinstance(loc_row, Loc):
            return self.house_row_cell_locs(loc_row.row)
        return [Loc(loc_row, col) for col in range(self.col_length)]

    def house_col_cell_locs(self, loc_col: Union[int, Loc]) -> list[Loc]:
        if isinstance(loc_col, Loc):
            return self.house_col_cell_locs(loc_col.col)
        return [Loc(row, loc_col) for row in range(self.length)]

    def cell_candidates(self, loc: Loc):
        return [int(s) for s in self.Constantsgrid[loc.row][loc.col] if s.isnumeric()]

    def rem(self, locs: list[Loc], candidates: list[int]) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.Constantsgrid[loc.row][loc.col] = self.Constantsgrid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits

    def is_cell_solved(self, loc: Loc) -> bool:
        return len(self.cell_candidates(loc)) == 1

    def total(self, col: int) -> Union[int, None]:
        string = self.Constantsgrid[self.length][col]
        if string.isnumeric():
            return int(string)
        return None


def lightenup_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_001():
    assert default_test_puzzle(Constants.lightenup_001(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_002():
    assert default_test_puzzle(Constants.lightenup_002(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_003():
    assert default_test_puzzle(Constants.lightenup_003(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_004():
    assert default_test_puzzle(Constants.lightenup_004(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_005():
    assert default_test_puzzle(Constants.lightenup_005(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_006():
    assert default_test_puzzle(Constants.lightenup_006(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_007():
    assert default_test_puzzle(Constants.lightenup_007(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_009():
    assert default_test_puzzle(Constants.lightenup_009(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_010():
    assert default_test_puzzle(Constants.lightenup_010(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_011():
    assert default_test_puzzle(Constants.lightenup_011(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_012():
    assert default_test_puzzle(Constants.lightenup_012(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_013():
    assert default_test_puzzle(Constants.lightenup_013(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_014():
    assert default_test_puzzle(Constants.lightenup_014(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_015():
    assert default_test_puzzle(Constants.lightenup_015(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_016():
    assert default_test_puzzle(Constants.lightenup_016(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_017():
    assert default_test_puzzle(Constants.lightenup_017(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_018():
    assert default_test_puzzle(Constants.lightenup_018(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_019():
    assert default_test_puzzle(Constants.lightenup_019(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_020():
    assert default_test_puzzle(Constants.lightenup_020(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_021():
    assert default_test_puzzle(Constants.lightenup_021(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_022():
    assert default_test_puzzle(Constants.lightenup_022(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_023():
    assert default_test_puzzle(Constants.lightenup_023(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_024():
    assert default_test_puzzle(Constants.lightenup_024(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_025():
    assert default_test_puzzle(Constants.lightenup_025(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_026():
    assert default_test_puzzle(Constants.lightenup_026(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_027():
    assert default_test_puzzle(Constants.lightenup_027(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_028():
    assert default_test_puzzle(Constants.lightenup_028(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_029():
    assert default_test_puzzle(Constants.lightenup_029(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_030():
    assert default_test_puzzle(Constants.lightenup_030(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_031():
    assert default_test_puzzle(Constants.lightenup_031(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_032():
    assert default_test_puzzle(Constants.lightenup_032(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_033():
    assert default_test_puzzle(Constants.lightenup_033(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_034():
    assert default_test_puzzle(Constants.lightenup_034(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_035():
    assert default_test_puzzle(Constants.lightenup_035(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_070():
    assert default_test_puzzle(Constants.lightenup_070(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_078():
    assert default_test_puzzle(Constants.lightenup_078(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_080():
    assert default_test_puzzle(Constants.lightenup_080(), LightenUp, lightenup_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lightenup_081():
    assert default_test_puzzle(Constants.lightenup_081(), LightenUp, lightenup_techniques())


class Lighthouses:
    pass


def lighthouses_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_001():
    assert default_test_puzzle(Constants.lighthouses_001(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_002():
    assert default_test_puzzle(Constants.lighthouses_002(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_003():
    assert default_test_puzzle(Constants.lighthouses_003(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_004():
    assert default_test_puzzle(Constants.lighthouses_004(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_005():
    assert default_test_puzzle(Constants.lighthouses_005(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_006():
    assert default_test_puzzle(Constants.lighthouses_006(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_007():
    assert default_test_puzzle(Constants.lighthouses_007(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_008():
    assert default_test_puzzle(Constants.lighthouses_008(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_009():
    assert default_test_puzzle(Constants.lighthouses_009(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_010():
    assert default_test_puzzle(Constants.lighthouses_010(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_011():
    assert default_test_puzzle(Constants.lighthouses_011(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_012():
    assert default_test_puzzle(Constants.lighthouses_012(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_013():
    assert default_test_puzzle(Constants.lighthouses_013(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_014():
    assert default_test_puzzle(Constants.lighthouses_014(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_015():
    assert default_test_puzzle(Constants.lighthouses_015(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_016():
    assert default_test_puzzle(Constants.lighthouses_016(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_017():
    assert default_test_puzzle(Constants.lighthouses_017(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_018():
    assert default_test_puzzle(Constants.lighthouses_018(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_019():
    assert default_test_puzzle(Constants.lighthouses_019(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_020():
    assert default_test_puzzle(Constants.lighthouses_020(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_021():
    assert default_test_puzzle(Constants.lighthouses_021(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_022():
    assert default_test_puzzle(Constants.lighthouses_022(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_023():
    assert default_test_puzzle(Constants.lighthouses_023(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_024():
    assert default_test_puzzle(Constants.lighthouses_024(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_025():
    assert default_test_puzzle(Constants.lighthouses_025(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_026():
    assert default_test_puzzle(Constants.lighthouses_026(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_027():
    assert default_test_puzzle(Constants.lighthouses_027(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_028():
    assert default_test_puzzle(Constants.lighthouses_028(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_029():
    assert default_test_puzzle(Constants.lighthouses_029(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_030():
    assert default_test_puzzle(Constants.lighthouses_030(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_031():
    assert default_test_puzzle(Constants.lighthouses_031(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_032():
    assert default_test_puzzle(Constants.lighthouses_032(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_033():
    assert default_test_puzzle(Constants.lighthouses_033(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_021():
    assert default_test_puzzle(Constants.lighthouses_021(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_022():
    assert default_test_puzzle(Constants.lighthouses_022(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_023():
    assert default_test_puzzle(Constants.lighthouses_023(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_024():
    assert default_test_puzzle(Constants.lighthouses_024(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_025():
    assert default_test_puzzle(Constants.lighthouses_025(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_027():
    assert default_test_puzzle(Constants.lighthouses_027(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_028():
    assert default_test_puzzle(Constants.lighthouses_028(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_029():
    assert default_test_puzzle(Constants.lighthouses_029(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_030():
    assert default_test_puzzle(Constants.lighthouses_030(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_031():
    assert default_test_puzzle(Constants.lighthouses_031(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_026():
    assert default_test_puzzle(Constants.lighthouses_026(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_012():
    assert default_test_puzzle(Constants.lighthouses_012(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_013():
    assert default_test_puzzle(Constants.lighthouses_013(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_014():
    assert default_test_puzzle(Constants.lighthouses_014(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_015():
    assert default_test_puzzle(Constants.lighthouses_015(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_016():
    assert default_test_puzzle(Constants.lighthouses_016(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_017():
    assert default_test_puzzle(Constants.lighthouses_017(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_018():
    assert default_test_puzzle(Constants.lighthouses_018(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_019():
    assert default_test_puzzle(Constants.lighthouses_019(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_020():
    assert default_test_puzzle(Constants.lighthouses_020(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_032():
    assert default_test_puzzle(Constants.lighthouses_032(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_033():
    assert default_test_puzzle(Constants.lighthouses_033(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_001():
    assert default_test_puzzle(Constants.lighthouses_001(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_002():
    assert default_test_puzzle(Constants.lighthouses_002(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_003():
    assert default_test_puzzle(Constants.lighthouses_003(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_004():
    assert default_test_puzzle(Constants.lighthouses_004(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_005():
    assert default_test_puzzle(Constants.lighthouses_005(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_006():
    assert default_test_puzzle(Constants.lighthouses_006(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_007():
    assert default_test_puzzle(Constants.lighthouses_007(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_008():
    assert default_test_puzzle(Constants.lighthouses_008(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_009():
    assert default_test_puzzle(Constants.lighthouses_009(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_010():
    assert default_test_puzzle(Constants.lighthouses_010(), Lighthouses, lighthouses_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_lighthouses_011():
    assert default_test_puzzle(Constants.lighthouses_011(), Lighthouses, lighthouses_techniques())


class Mathrax:
    def ConstantsinitConstants(self, puzzle: str) -> None:
        pass

    def solve0(self):
        pass


class MathraxCrossHatch:

    def solve0(self, puzzle: Mathrax) -> int:
        edits = 0
        return edits


class MathraxHiddenSingle:

    def solve0(self, puzzle: Mathrax) -> int:
        edits = 0
        return edits


def mathrax_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_mathrax_explicit_cross_hatch():
    assert default_test_explicit_actual_expected(Mathrax, Techs.MathraxCrossHatch(),
                                                 Constants.mathrax_explicit_cross_hatch_actual(),
                                                 Constants.mathrax_explicit_cross_hatch_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_mathrax_explicit_hidden_single():
    assert default_test_explicit_actual_expected(Mathrax, Techs.MathraxHiddenSingle(),
                                                 Constants.mathrax_explicit_hidden_single_actual(),
                                                 Constants.mathrax_explicit_hidden_single_expected())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_013():
    assert default_test_puzzle(Constants.mathrax_013(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_magnets_014():
    assert default_test_puzzle(Constants.magnets_014(), Magnets, magnets_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_014():
    assert default_test_puzzle(Constants.mathrax_014(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_015():
    assert default_test_puzzle(Constants.mathrax_015(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_016():
    assert default_test_puzzle(Constants.mathrax_016(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_017():
    assert default_test_puzzle(Constants.mathrax_017(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_018():
    assert default_test_puzzle(Constants.mathrax_018(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_019():
    assert default_test_puzzle(Constants.mathrax_019(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_020():
    assert default_test_puzzle(Constants.mathrax_020(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_001():
    assert default_test_puzzle(Constants.mathrax_001(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_002():
    assert default_test_puzzle(Constants.mathrax_002(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_003():
    assert default_test_puzzle(Constants.mathrax_003(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_004():
    assert default_test_puzzle(Constants.mathrax_004(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_005():
    assert default_test_puzzle(Constants.mathrax_005(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_006():
    assert default_test_puzzle(Constants.mathrax_006(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_007():
    assert default_test_puzzle(Constants.mathrax_007(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_008():
    assert default_test_puzzle(Constants.mathrax_008(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_010():
    assert default_test_puzzle(Constants.mathrax_010(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_011():
    assert default_test_puzzle(Constants.mathrax_011(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_009():
    assert default_test_puzzle(Constants.mathrax_009(), Mathrax, mathrax_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mathrax_012():
    assert default_test_puzzle(Constants.mathrax_012(), Mathrax, mathrax_techniques())


class MineShips:
    pass


def mine_ships_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mine_ships_001():
    assert default_test_puzzle(Constants.mine_ships_001(), MineShips, mine_ships_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mine_ships_002():
    assert default_test_puzzle(Constants.mine_ships_002(), MineShips, mine_ships_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_mine_ships_003():
    assert default_test_puzzle(Constants.mine_ships_003(), MineShips, mine_ships_techniques())


Techs = Techs
Constants = Constants


class Minesweeper:  # (Puzzle):
    def is_solved(self) -> bool:
        return False

    def ConstantsinitConstants(self, puzzle: str) -> None:
        super().ConstantsinitConstants(puzzle)
        array = []
        self.grid = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            self.grid.append(line.split(' '))

    def is_number_cell(self, loc: Loc) -> bool:
        return self.grid[loc.row][loc.col].isalnum()

    def is_mine_cell(self, loc: Loc) -> bool:
        return not self.is_number_cell(loc)

    def ConstantsstrConstants(self):
        string = f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.length):
            for c in range(self.length):
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string

    def rem(self, locs: list[Loc], candidates: list[str]) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits


class MinesweeperSolver:  # (BasePuzzleTechnique):

    @staticmethod
    def surrounding(puzzle: Minesweeper, loc: Loc) -> list[Loc]:
        valid = []
        directions = [
            loc.north(),
            loc.east(),
            loc.south(),
            loc.west(),
            loc.north().east(),
            loc.north().west(),
            loc.south().east(),
            loc.south().west(),
        ]

        for temp in directions:
            if temp.is_valid_parks(puzzle.grid):
                valid.append(temp)

        return valid

    def solve0(self, puzzle: Minesweeper) -> int:
        edits = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                if puzzle.is_number_cell(loc):
                    number = int(self.grid[loc.row][loc.col])

                    if number == 0:
                        edits += puzzle.rem()

        return edits


def minesweeper_techniques():
    return [Techs.MinesweeperSolver()]


@pytest.mark.skip(EXPLICITLY)
def test_explicit_minesweeper_explicit_0_fences():
    assert default_test_explicit_actual_expected(
        Minesweeper,
        Techs.MinesweeperSolver(),
        Constants.minesweeper_explicit_0_actual(),
        Constants.minesweeper_explicit_0_expected())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_001():
    assert default_test_puzzle(Constants.minesweeper_001(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_002():
    assert default_test_puzzle(Constants.minesweeper_002(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_003():
    assert default_test_puzzle(Constants.minesweeper_003(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_006():
    assert default_test_puzzle(Constants.minesweeper_006(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_008():
    assert default_test_puzzle(Constants.minesweeper_008(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_009():
    assert default_test_puzzle(Constants.minesweeper_009(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_010():
    assert default_test_puzzle(Constants.minesweeper_010(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_011():
    assert default_test_puzzle(Constants.minesweeper_011(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_012():
    assert default_test_puzzle(Constants.minesweeper_012(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_013():
    assert default_test_puzzle(Constants.minesweeper_013(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_024():
    assert default_test_puzzle(Constants.minesweeper_024(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_006():
    assert default_test_puzzle(Constants.minesweeper_006(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_008():
    assert default_test_puzzle(Constants.minesweeper_008(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_009():
    assert default_test_puzzle(Constants.minesweeper_009(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_010():
    assert default_test_puzzle(Constants.minesweeper_010(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_011():
    assert default_test_puzzle(Constants.minesweeper_011(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_012():
    assert default_test_puzzle(Constants.minesweeper_012(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_013():
    assert default_test_puzzle(Constants.minesweeper_013(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_024():
    assert default_test_puzzle(Constants.minesweeper_024(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_004():
    assert default_test_puzzle(Constants.minesweeper_004(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_005():
    assert default_test_puzzle(Constants.minesweeper_005(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_014():
    assert default_test_puzzle(Constants.minesweeper_014(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_015():
    assert default_test_puzzle(Constants.minesweeper_015(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_017():
    assert default_test_puzzle(Constants.minesweeper_017(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_007():
    assert default_test_puzzle(Constants.minesweeper_007(), Minesweeper, minesweeper_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_minesweeper_016():
    assert default_test_puzzle(Constants.minesweeper_016(), Minesweeper, minesweeper_techniques())


class Nurikabe:
    pass


def nurikabe_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_002():
    assert default_test_puzzle(Constants.nurikabe_002(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_003():
    assert default_test_puzzle(Constants.nurikabe_003(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_004():
    assert default_test_puzzle(Constants.nurikabe_004(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_005():
    assert default_test_puzzle(Constants.nurikabe_005(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_005():
    assert default_test_puzzle(Constants.nurikabe_005(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_006():
    assert default_test_puzzle(Constants.nurikabe_006(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_001():
    assert default_test_puzzle(Constants.nurikabe_001(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_007():
    assert default_test_puzzle(Constants.nurikabe_007(), Nurikabe, nurikabe_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_nurikabe_008():
    assert default_test_puzzle(Constants.nurikabe_008(), Nurikabe, nurikabe_techniques())


class PowerGrid:
    def ConstantsinitConstants(self, puzzle: str) -> None:
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        self.Constantsid = array[0]
        self.Constantslength = int(array[1])
        array.pop(0)
        array.pop(0)
        self.Constantsgrid = []
        for _ in range(self.Constantslength + 1):
            line = array[0].strip().replace("  ", " ", -1).split(" ")
            temp = []
            for l in line:
                if len(l) == 0:
                    continue
                temp.append(l)
            self.Constantsgrid.append(temp)
            array.pop(0)

    def id(self) -> str:
        return self.Constantsid

    @property
    def length(self) -> int:
        return self.Constantslength

    @property
    def grid_length(self):
        return self.length + 1

    def grid(self, loc: Loc) -> str:
        return self.Constantsgrid[loc.row][loc.col]

    def is_cell_solved_as_power(self, loc: Loc) -> bool:
        return '-' not in self.Constantsgrid[loc.row][loc.col]

    def is_cell_solved_as_empty(self, loc: Loc) -> bool:
        return '+' not in self.Constantsgrid[loc.row][loc.col]

    def ConstantsstrConstants(self) -> str:
        string = f'{self.Constantsid}\n'
        string += f'{self.Constantslength}\n'
        for r in range(self.grid_length):
            for c in range(self.grid_length):
                string += f'{self.grid(Loc(r, c))} '
            string += '\n'
        return string

    def is_solved(self) -> bool:
        return False

    def house_row_edge(self, row: int) -> int:
        string: str = self.Constantsgrid[row][self.length]
        if string.isnumeric():
            return int(string)
        return -1

    def house_row_cells(self, row: int) -> list[Loc]:
        house = []
        for index in range(self.length):
            house.append(Loc(row, index))
        return house

    def house_col_edge(self, col: int) -> int:
        string: str = self.Constantsgrid[self.length][col]
        if string.isnumeric():
            return int(string)
        return -1

    def house_col_cells(self, col: int) -> list[Loc]:
        house = []
        for index in range(self.length):
            house.append(Loc(index, col))
        return house

    def house_rows_cols_edges(self) -> list[tuple[list[Loc], int]]:
        house_edges = []
        for index in range(self.length):
            row_house = self.house_row_cells(index)
            row_edge = self.house_row_edge(index)
            col_house = self.house_col_cells(index)
            col_edge = self.house_col_edge(index)
            house_edges.append((row_house, row_edge))
            house_edges.append((col_house, col_edge))
        return house_edges

    def cell_candidates(self, loc: Loc) -> list[str]:
        return [candidate for candidate in self.Constantsgrid[loc.row][loc.col]]

    def rem(self, locs: list[Loc], _candidates: list[int]) -> int:
        edits = 0

        for loc in locs:
            for candidate in _candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.Constantsgrid[loc.row][loc.col] = self.Constantsgrid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits

    def require_power2(self, locs: list[Loc]) -> int:
        edits = 0

        if len(locs) == 2:

            # return 0
            if not locs[0].is_next_to(locs[1]):
                return edits

            row_set = set([loc.row for loc in locs])
            col_set = set([loc.col for loc in locs])

            cells_to_remove = []

            if len(row_set) == 1:
                cells_to_remove.append(locs[0].north())
                cells_to_remove.append(locs[1].north())
                cells_to_remove.append(locs[0].south())
                cells_to_remove.append(locs[1].south())

            if len(col_set) == 1:
                cells_to_remove.append(locs[0].east())
                cells_to_remove.append(locs[1].east())
                cells_to_remove.append(locs[0].west())
                cells_to_remove.append(locs[1].west())

        cells_to_remove = [loc for loc in cells_to_remove if loc.is_valid_sudoku(self.length)]

        # edits

        return self.rem(cells_to_remove, ['+'])

    def require_power3(self, locs: list[Loc]) -> int:
        return 0

    def require_power(self, locs: list[Loc]) -> int:
        return self.require_power2(locs) + self.require_power3(locs)

    def require_power(self, locs: list[Loc]) -> int:
        return self.require_power2(locs) + self.require_power3(locs)


class PowerGridTech:
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        for group in puzzle.house_rows_cols_edges():
            house, edge = group

            if edge < 1:
                continue

            if puzzle.length == 9 and edge == 6:
                next_to0 = [house.pop(0), house.pop(0)]
                next_to1 = [house.pop(len(house) - 1), house.pop(len(house) - 1)]
                edits += puzzle.rem(house, ["+"])
                edits += puzzle.required_power(next_to0)
                edits += puzzle.required_power(next_to1)

        #
        #     print(house)
        #     print(edge)

        # for index in range(puzzle.length):

        return edits


def power_grid_techniques() -> list:
    return [PowerGridTech()]


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_001():
    assert default_test_puzzle(Constants.power_grid_001(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_002():
    assert default_test_puzzle(Constants.power_grid_002(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_003():
    assert default_test_puzzle(Constants.power_grid_003(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_004():
    assert default_test_puzzle(Constants.power_grid_004(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_005():
    assert default_test_puzzle(Constants.power_grid_005(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_006():
    assert default_test_puzzle(Constants.power_grid_006(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_007():
    assert default_test_puzzle(Constants.power_grid_007(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_008():
    assert default_test_puzzle(Constants.power_grid_008(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_power_grid_009():
    assert default_test_puzzle(Constants.power_grid_009(), PowerGrid, power_grid_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_001():
    assert default_test_puzzle(Constants.hidden_stars_001(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_002():
    assert default_test_puzzle(Constants.hidden_stars_002(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_003():
    assert default_test_puzzle(Constants.hidden_stars_003(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_004():
    assert default_test_puzzle(Constants.hidden_stars_004(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_005():
    assert default_test_puzzle(Constants.hidden_stars_005(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_006():
    assert default_test_puzzle(Constants.hidden_stars_006(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_007():
    assert default_test_puzzle(Constants.hidden_stars_007(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_008():
    assert default_test_puzzle(Constants.hidden_stars_008(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_009():
    assert default_test_puzzle(Constants.hidden_stars_009(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_010():
    assert default_test_puzzle(Constants.hidden_stars_010(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_011():
    assert default_test_puzzle(Constants.hidden_stars_011(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_012():
    assert default_test_puzzle(Constants.hidden_stars_012(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_013():
    assert default_test_puzzle(Constants.hidden_stars_013(), HiddenStars, hidden_stars_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_hidden_stars_014():
    assert default_test_puzzle(Constants.hidden_stars_014(), HiddenStars, hidden_stars_techniques())


class RobotCrosswords:  # (Puzzle):
    def ConstantsinitConstants(self, puzzle: str) -> None:
        super().ConstantsinitConstants(puzzle)
        array = []
        self.grid = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            split = line.split(' ')
            other = []

            for item in split:
                if item == '.' or item == '_':
                    other.append('123456789')
                elif item == 'x':
                    other.append('xxxxxxxxx')
                elif item.isalnum():
                    number = int(item)
                    temp = ''
                    for num in range(1, 10):
                        if number == num:
                            temp += f'{num}'
                        else:
                            temp += '_'
                    other.append(temp)
            # print(split)
            # self.grid.append(line.split(" "))
            self.grid.append(other)

    def ConstantsstrConstants(self) -> str:
        string = f'///////////////////////////////////\n'
        string += f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.length):
            for c in range(self.length):
                string += f'{self.grid[r][c]} '
            string += '\n'
        string += f'///////////////////////////////////'
        return string

    def is_solved(self) -> bool:
        return False


class RobotCrosswordsHouses:  # (BasePuzzleTechnique):
    def solve0(self, puzzle: RobotCrosswords) -> int:
        edits = 0

        houses = []

        for row in range(puzzle.length):
            house = []
            for col in range(puzzle.length):
                house.append(Loc(row, col))
            houses.append(house)

        for col in range(puzzle.length):
            house = []
            for row in range(puzzle.length):
                house.append(Loc(row, col))
            houses.append(house)

        for house in houses:

            # temp_house = list(house)
            #
            #
            #
            #
            #
            #
            # continue

            string = ""

            all_crosswords = []

            in_crossword = False

            crossword = []

            for index in range(len(house)):
                if 'x' in puzzle.grid[house[index].row][house[index].col]:
                    if in_crossword:
                        all_crosswords.append(list(crossword))
                        crossword = []
                        in_crossword = False
                        # continue
                elif in_crossword:
                    crossword.append(house[index])
                else:
                    crossword.append(house[index])
                    in_crossword = True
            # for cross in

            print(all_crosswords)

            # loc = house[index]

            #     string += f'{puzzle.grid[loc.row][loc.col]} '
            #
            # string = string.replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).strip()
            # .split(" ")

            # string = string.strip()

            # print(string)

        return edits


def robot_crosswords_techniques() -> list:
    return [Techs.RobotCrosswordsHouses()]


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_005():
    assert default_test_puzzle(Constants.robot_crosswords_005(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_006():
    assert default_test_puzzle(Constants.robot_crosswords_006(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_007():
    assert default_test_puzzle(Constants.robot_crosswords_007(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_008():
    assert default_test_puzzle(Constants.robot_crosswords_008(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_009():
    assert default_test_puzzle(Constants.robot_crosswords_009(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_010():
    assert default_test_puzzle(Constants.robot_crosswords_010(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_011():
    assert default_test_puzzle(Constants.robot_crosswords_011(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_012():
    assert default_test_puzzle(Constants.robot_crosswords_012(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_013():
    assert default_test_puzzle(Constants.robot_crosswords_013(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_014():
    assert default_test_puzzle(Constants.robot_crosswords_014(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_015():
    assert default_test_puzzle(Constants.robot_crosswords_015(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_031():
    assert default_test_puzzle(Constants.robot_crosswords_031(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_034():
    assert default_test_puzzle(Constants.robot_crosswords_034(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_035():
    assert default_test_puzzle(Constants.robot_crosswords_035(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_036():
    assert default_test_puzzle(Constants.robot_crosswords_036(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_071():
    assert default_test_puzzle(Constants.robot_crosswords_071(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_101():
    assert default_test_puzzle(Constants.robot_crosswords_101(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_141():
    assert default_test_puzzle(Constants.robot_crosswords_141(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_171():
    assert default_test_puzzle(Constants.robot_crosswords_171(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_003():
    assert default_test_puzzle(Constants.robot_crosswords_003(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_004():
    assert default_test_puzzle(Constants.robot_crosswords_004(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_186():
    assert default_test_puzzle(Constants.robot_crosswords_186(), RobotCrosswords, robot_crosswords_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_robot_crosswords_002():
    assert default_test_puzzle(Constants.robot_crosswords_002(), RobotCrosswords, robot_crosswords_techniques())


class Sentinels:
    pass


def sentinels_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sentinels_001():
    assert default_test_puzzle(Constants.sentinels_001(), Sentinels, sentinels_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sentinels_002():
    assert default_test_puzzle(Constants.sentinels_002(), Sentinels, sentinels_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sentinels_004():
    assert default_test_puzzle(Constants.sentinels_004(), Sentinels, sentinels_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sentinels_006():
    assert default_test_puzzle(Constants.sentinels_006(), Sentinels, sentinels_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sentinels_003():
    assert default_test_puzzle(Constants.sentinels_003(), Sentinels, sentinels_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sentinels_007():
    assert default_test_puzzle(Constants.sentinels_007(), Sentinels, sentinels_techniques())


class Skyscrapers:
    pass


def skyscrapers_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_001():
    assert default_test_puzzle(Constants.skyscrapers_001(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_002():
    assert default_test_puzzle(Constants.skyscrapers_002(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_003():
    assert default_test_puzzle(Constants.skyscrapers_003(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_004():
    assert default_test_puzzle(Constants.skyscrapers_004(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_005():
    assert default_test_puzzle(Constants.skyscrapers_005(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_006():
    assert default_test_puzzle(Constants.skyscrapers_006(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_007():
    assert default_test_puzzle(Constants.skyscrapers_007(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_008():
    assert default_test_puzzle(Constants.skyscrapers_008(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_009():
    assert default_test_puzzle(Constants.skyscrapers_009(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_010():
    assert default_test_puzzle(Constants.skyscrapers_010(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_011():
    assert default_test_puzzle(Constants.skyscrapers_011(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_012():
    assert default_test_puzzle(Constants.skyscrapers_012(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_013():
    assert default_test_puzzle(Constants.skyscrapers_013(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_014():
    assert default_test_puzzle(Constants.skyscrapers_014(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_015():
    assert default_test_puzzle(Constants.skyscrapers_015(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_016():
    assert default_test_puzzle(Constants.skyscrapers_016(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_017():
    assert default_test_puzzle(Constants.skyscrapers_017(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_018():
    assert default_test_puzzle(Constants.skyscrapers_018(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_019():
    assert default_test_puzzle(Constants.skyscrapers_019(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_020():
    assert default_test_puzzle(Constants.skyscrapers_020(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_021():
    assert default_test_puzzle(Constants.skyscrapers_021(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_022():
    assert default_test_puzzle(Constants.skyscrapers_022(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_023():
    assert default_test_puzzle(Constants.skyscrapers_023(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_024():
    assert default_test_puzzle(Constants.skyscrapers_024(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_025():
    assert default_test_puzzle(Constants.skyscrapers_025(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_026():
    assert default_test_puzzle(Constants.skyscrapers_026(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_027():
    assert default_test_puzzle(Constants.skyscrapers_027(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_028():
    assert default_test_puzzle(Constants.skyscrapers_028(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_029():
    assert default_test_puzzle(Constants.skyscrapers_029(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_030():
    assert default_test_puzzle(Constants.skyscrapers_030(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_skydoku_001():
    assert default_test_puzzle(Constants.skyscrapers_skydoku_001(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_skydoku_004():
    assert default_test_puzzle(Constants.skyscrapers_skydoku_004(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_skydoku_021():
    assert default_test_puzzle(Constants.skyscrapers_skydoku_021(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_skydoku_030():
    assert default_test_puzzle(Constants.skyscrapers_skydoku_030(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_skydoku_036():
    assert default_test_puzzle(Constants.skyscrapers_skydoku_036(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_001():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_001(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_002():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_002(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_003():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_003(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_004():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_004(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_013():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_013(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_019():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_019(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_030():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_030(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_033():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_033(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_039():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_039(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_046():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_046(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_062():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_062(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_068():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_068(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_087():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_087(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_093():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_093(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_100():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_100(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tcbig_119():
    assert default_test_puzzle(Constants.skyscrapers_tcbig_119(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_001():
    assert default_test_puzzle(Constants.skyscrapers_tc_001(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_002():
    assert default_test_puzzle(Constants.skyscrapers_tc_002(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_003():
    assert default_test_puzzle(Constants.skyscrapers_tc_003(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_004():
    assert default_test_puzzle(Constants.skyscrapers_tc_004(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_005():
    assert default_test_puzzle(Constants.skyscrapers_tc_005(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_006():
    assert default_test_puzzle(Constants.skyscrapers_tc_006(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_007():
    assert default_test_puzzle(Constants.skyscrapers_tc_007(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_008():
    assert default_test_puzzle(Constants.skyscrapers_tc_008(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_009():
    assert default_test_puzzle(Constants.skyscrapers_tc_009(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_010():
    assert default_test_puzzle(Constants.skyscrapers_tc_010(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_011():
    assert default_test_puzzle(Constants.skyscrapers_tc_011(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_012():
    assert default_test_puzzle(Constants.skyscrapers_tc_012(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_013():
    assert default_test_puzzle(Constants.skyscrapers_tc_013(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_014():
    assert default_test_puzzle(Constants.skyscrapers_tc_014(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_015():
    assert default_test_puzzle(Constants.skyscrapers_tc_015(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_016():
    assert default_test_puzzle(Constants.skyscrapers_tc_016(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_017():
    assert default_test_puzzle(Constants.skyscrapers_tc_017(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_018():
    assert default_test_puzzle(Constants.skyscrapers_tc_018(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_019():
    assert default_test_puzzle(Constants.skyscrapers_tc_019(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_025():
    assert default_test_puzzle(Constants.skyscrapers_tc_025(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_026():
    assert default_test_puzzle(Constants.skyscrapers_tc_026(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_027():
    assert default_test_puzzle(Constants.skyscrapers_tc_027(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_028():
    assert default_test_puzzle(Constants.skyscrapers_tc_028(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_029():
    assert default_test_puzzle(Constants.skyscrapers_tc_029(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_030():
    assert default_test_puzzle(Constants.skyscrapers_tc_030(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_031():
    assert default_test_puzzle(Constants.skyscrapers_tc_031(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_032():
    assert default_test_puzzle(Constants.skyscrapers_tc_032(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_033():
    assert default_test_puzzle(Constants.skyscrapers_tc_033(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_034():
    assert default_test_puzzle(Constants.skyscrapers_tc_034(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_038():
    assert default_test_puzzle(Constants.skyscrapers_tc_038(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_039():
    assert default_test_puzzle(Constants.skyscrapers_tc_039(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_046():
    assert default_test_puzzle(Constants.skyscrapers_tc_046(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_051():
    assert default_test_puzzle(Constants.skyscrapers_tc_051(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_052():
    assert default_test_puzzle(Constants.skyscrapers_tc_052(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_056():
    assert default_test_puzzle(Constants.skyscrapers_tc_056(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_057():
    assert default_test_puzzle(Constants.skyscrapers_tc_057(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_062():
    assert default_test_puzzle(Constants.skyscrapers_tc_062(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_068():
    assert default_test_puzzle(Constants.skyscrapers_tc_068(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_087():
    assert default_test_puzzle(Constants.skyscrapers_tc_087(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_093():
    assert default_test_puzzle(Constants.skyscrapers_tc_093(), Skyscrapers, skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_100():
    assert default_test_puzzle(
        Constants.skyscrapers_tc_100(),
        Skyscrapers,
        skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_119():
    assert default_test_puzzle(
        Constants.skyscrapers_tc_119(),
        Skyscrapers,
        skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_130():
    assert default_test_puzzle(
        Constants.skyscrapers_tc_130(),
        Skyscrapers,
        skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_skyscrapers_tc_135():
    assert default_test_puzzle(
        Constants.skyscrapers_tc_135(),
        Skyscrapers,
        skyscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_skyscrapers_explicit_cross_hatch():
    assert default_test_explicit_actual_expected(Skyscrapers, Techs.SkyscrapersCrossHatch(),
                                                 Constants.skyscrapers_explicit_cross_hatch_actual(),
                                                 Constants.skyscrapers_explicit_cross_hatch_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_skyscrapers_explicit_hidden_single():
    assert default_test_explicit_actual_expected(Skyscrapers, Techs.SkyscrapersHiddenSingle(),
                                                 Constants.skyscrapers_explicit_hidden_single_actual(),
                                                 Constants.skyscrapers_explicit_hidden_single_expected())


@pytest.mark.skip(EXPLICITLY)
def test_1explicit_skyscrapers_explicit_edges():
    assert default_test_explicit_actual_expected(Skyscrapers, Techs.SkyscrapersEdges(),
                                                 Constants.skyscrapers_explicit_edges_actual(),
                                                 Constants.skyscrapers_explicit_edges_expected())


class Snail3:
    pass


def snail3_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_004():
    assert default_test_puzzle(Constants.snail3_004(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_005():
    assert default_test_puzzle(Constants.snail3_005(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_006():
    assert default_test_puzzle(Constants.snail3_006(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_007():
    assert default_test_puzzle(Constants.snail3_007(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_008():
    assert default_test_puzzle(Constants.snail3_008(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_009():
    assert default_test_puzzle(Constants.snail3_009(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_010():
    assert default_test_puzzle(Constants.snail3_010(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_001():
    assert default_test_puzzle(Constants.snail3_001(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_002():
    assert default_test_puzzle(Constants.snail3_002(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_003():
    assert default_test_puzzle(Constants.snail3_003(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_011():
    assert default_test_puzzle(Constants.snail3_011(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_012():
    assert default_test_puzzle(Constants.snail3_012(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_013():
    assert default_test_puzzle(Constants.snail3_013(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_014():
    assert default_test_puzzle(Constants.snail3_014(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_015():
    assert default_test_puzzle(Constants.snail3_015(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_016():
    assert default_test_puzzle(Constants.snail3_016(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_017():
    assert default_test_puzzle(Constants.snail3_017(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_031():
    assert default_test_puzzle(Constants.snail3_031(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_032():
    assert default_test_puzzle(Constants.snail3_032(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_033():
    assert default_test_puzzle(Constants.snail3_033(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_034():
    assert default_test_puzzle(Constants.snail3_034(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_035():
    assert default_test_puzzle(Constants.snail3_035(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_036():
    assert default_test_puzzle(Constants.snail3_036(), Snail3, snail3_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_snail3_077():
    assert default_test_puzzle(Constants.snail3_077(), Snail3, snail3_techniques())


class Sumscrapers:
    pass


def sumscrapers_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_006():
    assert default_test_puzzle(Constants.sumscrapers_006(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_007():
    assert default_test_puzzle(Constants.sumscrapers_007(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_008():
    assert default_test_puzzle(Constants.sumscrapers_008(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_009():
    assert default_test_puzzle(Constants.sumscrapers_009(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_010():
    assert default_test_puzzle(Constants.sumscrapers_010(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_011():
    assert default_test_puzzle(Constants.sumscrapers_011(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_012():
    assert default_test_puzzle(Constants.sumscrapers_012(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_017():
    assert default_test_puzzle(Constants.sumscrapers_017(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_018():
    assert default_test_puzzle(Constants.sumscrapers_018(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_019():
    assert default_test_puzzle(Constants.sumscrapers_019(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_020():
    assert default_test_puzzle(Constants.sumscrapers_020(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_001():
    assert default_test_puzzle(Constants.sumscrapers_001(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_002():
    assert default_test_puzzle(Constants.sumscrapers_002(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_003():
    assert default_test_puzzle(Constants.sumscrapers_003(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_004():
    assert default_test_puzzle(Constants.sumscrapers_004(), Sumscrapers, sumscrapers_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_sumscrapers_005():
    assert default_test_puzzle(Constants.sumscrapers_005(), Sumscrapers, sumscrapers_techniques())


class Tents:
    pass


def tents_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tents_001():
    assert default_test_puzzle(Constants.tents_001(), Tents, tents_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_tents_009():
    assert default_test_puzzle(Constants.tents_009(), Tents, tents_techniques())


class Walls:
    pass


def walls_techniques() -> list:
    return []


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_001():
    assert default_test_puzzle(Constants.walls_001(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_002():
    assert default_test_puzzle(Constants.walls_002(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_003():
    assert default_test_puzzle(Constants.walls_003(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_004():
    assert default_test_puzzle(Constants.walls_004(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_005():
    assert default_test_puzzle(Constants.walls_005(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_006():
    assert default_test_puzzle(Constants.walls_006(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_007():
    assert default_test_puzzle(Constants.walls_007(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_008():
    assert default_test_puzzle(Constants.walls_008(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_009():
    assert default_test_puzzle(Constants.walls_009(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_010():
    assert default_test_puzzle(Constants.walls_010(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_011():
    assert default_test_puzzle(Constants.walls_011(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_012():
    assert default_test_puzzle(Constants.walls_012(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_013():
    assert default_test_puzzle(Constants.walls_013(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_014():
    assert default_test_puzzle(Constants.walls_014(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_015():
    assert default_test_puzzle(Constants.walls_015(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_016():
    assert default_test_puzzle(Constants.walls_016(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_017():
    assert default_test_puzzle(Constants.walls_017(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_018():
    assert default_test_puzzle(Constants.walls_018(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_019():
    assert default_test_puzzle(Constants.walls_019(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_020():
    assert default_test_puzzle(Constants.walls_020(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_021():
    assert default_test_puzzle(Constants.walls_021(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_022():
    assert default_test_puzzle(Constants.walls_022(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_023():
    assert default_test_puzzle(Constants.walls_023(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_024():
    assert default_test_puzzle(Constants.walls_024(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_025():
    assert default_test_puzzle(Constants.walls_025(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_026():
    assert default_test_puzzle(Constants.walls_026(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_027():
    assert default_test_puzzle(Constants.walls_027(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_028():
    assert default_test_puzzle(Constants.walls_028(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_029():
    assert default_test_puzzle(Constants.walls_029(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_030():
    assert default_test_puzzle(Constants.walls_030(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_031():
    assert default_test_puzzle(Constants.walls_031(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_032():
    assert default_test_puzzle(Constants.walls_032(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_033():
    assert default_test_puzzle(Constants.walls_033(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_034():
    assert default_test_puzzle(Constants.walls_034(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_035():
    assert default_test_puzzle(Constants.walls_035(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_036():
    assert default_test_puzzle(Constants.walls_036(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_037():
    assert default_test_puzzle(Constants.walls_037(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_038():
    assert default_test_puzzle(Constants.walls_038(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_039():
    assert default_test_puzzle(Constants.walls_039(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_040():
    assert default_test_puzzle(Constants.walls_040(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_041():
    assert default_test_puzzle(Constants.walls_041(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_042():
    assert default_test_puzzle(Constants.walls_042(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_043():
    assert default_test_puzzle(Constants.walls_043(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_044():
    assert default_test_puzzle(Constants.walls_044(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_045():
    assert default_test_puzzle(Constants.walls_045(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_048():
    assert default_test_puzzle(Constants.walls_048(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_049():
    assert default_test_puzzle(Constants.walls_049(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_050():
    assert default_test_puzzle(Constants.walls_050(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_051():
    assert default_test_puzzle(Constants.walls_051(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_062():
    assert default_test_puzzle(Constants.walls_062(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_063():
    assert default_test_puzzle(Constants.walls_063(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_064():
    assert default_test_puzzle(Constants.walls_064(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_065():
    assert default_test_puzzle(Constants.walls_065(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_066():
    assert default_test_puzzle(Constants.walls_066(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_067():
    assert default_test_puzzle(Constants.walls_067(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_068():
    assert default_test_puzzle(Constants.walls_068(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_069():
    assert default_test_puzzle(Constants.walls_069(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_070():
    assert default_test_puzzle(Constants.walls_070(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_071():
    assert default_test_puzzle(Constants.walls_071(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_072():
    assert default_test_puzzle(Constants.walls_072(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_092():
    assert default_test_puzzle(Constants.walls_092(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_101():
    assert default_test_puzzle(Constants.walls_101(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_109():
    assert default_test_puzzle(Constants.walls_109(), Walls, walls_techniques())


@pytest.mark.skip(EXPLICITLY)
def test_puzzle_walls_111():
    assert default_test_puzzle(Constants.walls_111(), Walls, walls_techniques())
