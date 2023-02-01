# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"

# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#
#     ('lightenup_001', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_002', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_003', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_004', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_005', LightenUp, Solving.lightenup_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)


# 

import pytest
import pytest

from _defaults import default_test_puzzle
from puzzles import LightenUp
from solving import Solving


# @pytest.mark.skip("skip")
def test_lighten_up_001():
    puzzle_string = f"""
    001.lightenup
    5
    +- +- ?? +- ??
    +- +- +- 04 +-
    +- +- 04 +- +-
    +- +- +- +- +-
    +- 00 +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


# @pytest.mark.skip("skip")
def test_lighten_up_002():
    puzzle_string = f"""
    002.lightenup
    5
    +- +- ?? +- +-
    +- +- +- +- +-
    +- 03 +- +- +-
    +- +- ?? +- 03
    +- +- +- ?? +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


# @pytest.mark.skip("skip")
def test_lighten_up_003():
    puzzle_string = f"""
    003.lightenup
    5
    +- +- +- +- +-
    +- +- +- 02 +-
    +- 02 +- +- +-
    +- +- 04 +- ??
    +- +- +- ?? +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


# @pytest.mark.skip("skip")
def test_lighten_up_004():
    puzzle_string = f"""
    004.lightenup
    5
    +- +- +- +- +-
    +- 01 +- +- +-
    +- 03 +- +- 01
    03 +- 02 +- +-
    +- +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


# @pytest.mark.skip("skip")
def test_lighten_up_005():
    puzzle_string = f"""
    005.lightenup
    5
    +- +- +- +- 02
    +- +- +- +- +-
    ?? +- +- +- +-
    +- +- 03 +- ??
    +- +- +- ?? +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_006():
    puzzle_string = f"""
    006.lightenup
    5
    +- +- +- +- ??
    +- 01 +- +- ??
    +- +- +- +- +-
    +- +- +- 03 +-
    +- +- +- +- 01
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_007():
    puzzle_string = f"""
    007.lightenup
    5
    +- +- 00 +- +-
    +- +- +- +- +-
    ?? +- +- +- 01
    +- +- +- +- +-
    +- 00 00 +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_009():
    puzzle_string = f"""
    009.lightenup
    5
    +- +- ?? +- +-
    +- 02 +- +- +-
    +- +- +- +- 02
    +- +- +- +- +-
    +- ?? +- 02 +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_010():
    puzzle_string = f"""
    010.lightenup
    5
    +- +- +- +- +-
    +- +- +- +- +-
    00 00 +- +- 01
    +- +- +- +- +-
    +- 01 +- 01 +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_011():
    puzzle_string = f"""
    011.lightenup
    5
    +- 01 +- +- +-
    +- +- +- +- +-
    +- +- +- 00 +-
    01 +- +- +- +-
    +- +- ?? 01 +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_012():
    puzzle_string = f"""
    012.lightenup
    5
    +- +- +- 01 +-
    +- 02 +- ?? +-
    +- +- +- 00 +-
    +- +- +- +- 01
    +- +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_013():
    puzzle_string = f"""
    013.lightenup
    5
    +- +- ?? +- ??
    +- +- 02 +- +-
    01 +- +- +- +-
    +- +- +- +- +-
    +- +- +- 02 +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_014():
    puzzle_string = f"""
    014.lightenup
    5
    +- +- +- 00 00
    +- +- +- 01 +-
    +- +- +- +- +-
    +- +- +- 01 +-
    00 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_015():
    puzzle_string = f"""
    015.lightenup
    5
    +- +- +- +- +-
    +- 01 +- +- 00
    +- +- +- +- +-
    +- +- 02 +- 02
    +- +- ?? +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_016():
    puzzle_string = f"""
    016.lightenup
    6
    00 +- 00 +- +- 01
    +- +- +- +- +- +-
    01 +- +- +- 00 +-
    +- +- 03 +- +- +-
    +- 01 +- +- +- +-
    +- +- +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_017():
    puzzle_string = f"""
    017.lightenup
    6
    +- +- +- +- +- 02
    +- +- +- +- +- +-
    +- +- +- +- +- 02
    02 +- +- ?? +- +-
    +- +- +- 01 +- ??
    +- 01 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_018():
    puzzle_string = f"""
    018.lightenup
    6
    +- +- 00 +- +- +-
    01 +- +- +- 03 +-
    +- 00 01 +- +- +-
    +- +- +- +- +- +-
    +- +- +- +- +- ??
    +- 00 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_019():
    puzzle_string = f"""
    019.lightenup
    6
    +- 02 +- +- 02 +-
    +- +- +- +- +- +-
    +- +- +- 01 +- +-
    +- +- 01 +- +- +-
    +- +- 00 02 +- +-
    +- +- +- +- +- 00
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_020():
    puzzle_string = f"""
    020.lightenup
    6
    +- ?? +- +- 02 +-
    +- ?? +- 01 +- +-
    +- +- +- +- +- +-
    +- +- 04 +- +- +-
    +- +- +- +- +- 00
    +- 01 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


# @pytest.mark.skip("skip")
def test_lighten_up_021():
    puzzle_string = f"""
    021.lightenup
    6
    01 +- +- +- +- +-
    +- +- 00 +- 03 +-
    +- ?? +- +- +- +-
    +- +- +- +- +- ??
    +- +- +- +- +- +-
    +- +- +- 01 +- 01
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_022():
    puzzle_string = f"""
    022.lightenup
    6
    +- 02 +- +- +- ??
    +- 00 +- +- +- +-
    +- +- +- +- 01 +-
    +- +- +- +- +- +-
    +- +- +- 01 02 +-
    +- +- +- +- +- 01
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_023():
    puzzle_string = f"""
    023.lightenup
    6
    01 +- +- +- +- +-
    01 +- +- 00 +- +-
    +- +- +- +- +- +-
    +- +- +- +- +- +-
    00 +- +- +- 02 +-
    00 +- +- 01 +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_024():
    puzzle_string = f"""
    024.lightenup
    7
    ?? +- ?? +- +- +- +-
    +- +- +- +- +- 01 +-
    +- +- 02 +- +- +- ??
    +- +- +- +- +- +- ??
    +- 02 +- 00 ?? +- ??
    +- +- +- +- 02 +- +-
    +- 00 +- +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


# @pytest.mark.skip("skip")
def test_lighten_up_025():
    puzzle_string = f"""
    025.lightenup
    7
    ?? +- +- +- +- +- +-
    +- 01 02 +- 02 +- +-
    +- +- +- 04 +- ?? ??
    01 ?? +- +- +- +- +-
    +- +- +- +- +- +- 01
    01 +- +- +- +- +- +-
    +- +- ?? +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_026():
    puzzle_string = f"""
    026.lightenup
    7
    +- 01 +- +- +- +- +-
    +- +- +- 02 +- +- +-
    +- +- +- +- 02 +- 01
    +- +- ?? ?? +- +- +-
    00 ?? +- 02 +- +- 01
    +- +- +- +- +- +- +-
    01 +- +- +- +- 01 +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_027():
    puzzle_string = f"""
    027.lightenup
    7
    +- +- +- ?? +- +- +-
    00 +- 02 +- +- +- +-
    +- +- +- +- ?? 00 +-
    ?? +- +- +- +- +- +-
    ?? +- 01 +- +- +- +-
    02 +- +- +- +- ?? ??
    +- +- +- 01 +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_028():
    puzzle_string = f"""
    028.lightenup
    7
    ?? +- +- 01 +- +- ??
    +- +- +- +- +- ?? +-
    +- +- +- +- +- +- 03
    +- +- +- +- ?? +- +-
    03 +- +- +- +- +- +-
    +- +- +- +- +- +- ??
    +- +- +- 02 +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_029():
    puzzle_string = f"""
    029.lightenup
    7
    +- +- +- +- 00 +- 01
    +- +- +- +- 00 +- +-
    01 +- +- +- 01 +- +-
    +- +- +- ?? +- +- +-
    01 +- +- +- ?? +- +-
    01 +- 02 +- 02 +- +-
    +- +- +- +- +- +- ??
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_030():
    puzzle_string = f"""
    030.lightenup
    7
    +- ?? +- +- +- +- 01
    +- +- 01 +- +- +- ??
    +- +- +- +- +- +- +-
    +- 00 00 00 01 +- +-
    +- +- +- +- +- +- +-
    +- +- ?? +- +- +- +-
    +- ?? +- +- 01 +- 01
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_031():
    puzzle_string = f"""
    031.lightenup
    7
    00 +- +- ?? +- 01 +-
    +- +- +- +- +- +- +-
    +- 02 +- +- 02 +- +-
    ?? +- 02 +- +- +- +-
    +- +- +- +- +- +- ??
    +- +- +- 01 +- +- 01
    +- 00 01 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_032():
    puzzle_string = f"""
    032.lightenup
    7
    +- +- +- +- +- +- 01
    ?? +- +- +- ?? 02 +-
    +- +- +- 00 +- +- +-
    +- +- 00 ?? +- +- +-
    +- 02 +- +- +- 01 +-
    +- +- +- +- +- +- +-
    ?? ?? +- 02 +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_033():
    puzzle_string = f"""
    033.lightenup
    7
    ?? 00 +- +- +- 00 +-
    +- +- +- +- +- +- +-
    +- +- 00 00 +- +- +-
    +- +- +- +- +- 01 00
    +- +- +- +- +- +- +-
    +- 01 +- 01 +- +- 01
    00 ?? +- +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_034():
    puzzle_string = f"""
    034.lightenup
    8
    +- 02 +- +- ?? +- +- +-
    +- +- +- +- 01 +- +- +-
    +- 03 +- +- +- +- +- +-
    +- +- +- 01 +- +- +- +-
    +- +- 01 +- +- +- +- 02
    01 +- +- ?? +- +- 03 +-
    +- +- 01 00 +- +- +- +-
    +- +- +- +- +- +- 01 ??
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_035():
    puzzle_string = f"""
    035.lightenup
    8
    +- +- +- +- 00 +- 00 +-
    +- 01 +- 00 +- +- +- +-
    +- +- +- +- +- +- +- ??
    +- +- +- 00 +- 02 +- +-
    +- +- +- +- +- +- +- +-
    +- +- 00 +- 01 00 00 +-
    +- 00 +- +- ?? +- +- +-
    +- +- +- +- +- 01 +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_070():
    puzzle_string = f"""
    070.lightenup
    10
    ?? ?? 01 +- +- +- +- +- +- +-
    +- +- +- +- +- +- +- +- +- +-
    +- +- 01 +- 00 +- +- +- +- 02
    +- ?? +- +- +- +- +- +- +- +-
    01 ?? +- +- 01 +- +- 00 +- +-
    +- +- +- +- ?? ?? +- +- ?? +-
    +- 03 +- +- ?? +- +- 02 +- ??
    +- ?? 01 +- +- +- +- +- +- +-
    +- +- +- +- +- ?? +- +- 01 +-
    +- +- +- +- 01 +- +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_078():
    puzzle_string = f"""
    078.lightenup
    11
    +- 02 ?? +- +- +- 01 +- +- +- ??
    +- +- +- +- +- ?? +- +- ?? +- +-
    +- +- +- +- +- +- 03 +- +- 00 +-
    +- ?? ?? ?? +- +- +- +- +- +- +-
    +- +- +- 03 +- ?? +- 00 +- +- 01
    +- +- +- +- +- 00 +- ?? +- +- +-
    +- +- +- +- +- +- +- +- +- +- +-
    ?? +- +- +- +- +- +- +- 00 +- +-
    02 +- +- +- +- +- 01 +- +- +- +-
    +- +- ?? 01 +- +- +- 02 +- 04 +-
    +- +- +- +- +- +- ?? ?? +- +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_080():
    puzzle_string = f"""
    080.lightenup
    11
    ?? +- 02 +- +- 01 +- +- 00 +- +-
    +- +- +- +- +- +- 01 +- +- +- +-
    +- 00 +- +- +- +- +- 02 +- ?? +-
    +- 01 +- 01 ?? 01 +- +- +- +- 01
    ?? +- +- +- +- +- +- +- +- 01 +-
    +- +- +- +- +- +- +- +- ?? +- +-
    +- +- 01 +- +- 02 +- 01 +- +- +-
    +- 01 +- +- +- +- +- +- +- +- 01
    00 +- +- +- +- 02 +- +- +- +- +-
    +- +- 01 +- +- +- +- +- +- +- +-
    +- +- +- ?? ?? +- +- +- +- +- 01
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())


@pytest.mark.skip("skip")
def test_lighten_up_081():
    puzzle_string = f"""
    081.lightenup
    11
    ?? +- +- +- +- +- +- +- ?? +- +-
    +- +- +- ?? +- +- ?? +- +- +- 01
    02 +- +- 02 +- 02 +- 03 +- +- ??
    +- +- +- +- ?? ?? +- +- +- +- +-
    ?? +- +- +- +- +- +- +- +- 01 +-
    ?? +- 00 +- +- +- ?? +- +- +- +-
    +- +- +- +- +- +- +- +- 01 ?? +-
    +- +- +- 03 +- +- +- +- +- ?? +-
    +- ?? +- +- +- +- +- +- 02 +- +-
    01 +- +- +- +- 02 +- +- +- +- +-
    +- +- +- 01 +- +- +- +- ?? +- +-
    """
    assert default_test_puzzle(puzzle_string, LightenUp, Solving.lightenup_techniques())
