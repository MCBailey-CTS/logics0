import pytest

from _defaults import default_test_puzzle
from puzzles import PowerGrid
from solving import Solving

from techniques.PowerGridTechniques import  power_grid_techniques

EXPLICITLY = "EXPLICITLY"


def test_power_grid_001():
    puzzle_string = f"""
    001.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    05 01 06 01 05 05 01 06 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_002():
    puzzle_string = f"""
    002.power_grid
    9
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    04 03 03 07 01 05 01 06 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_003():
    puzzle_string = f"""
    003.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    04 03 03 03 04 04 04 03 03 $$
    diagonal        
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_004():
    puzzle_string = f"""
    004.power_grid
    9
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    01 01 02 01 01 01 01 03 04 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_005():
    puzzle_string = f"""
    005.power_grid
    9
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    02 06 01 01 01 01 01 01 03 $$
    diagonal     
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_006():
    puzzle_string = f"""
    006.power_grid
    9
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    03 03 01 01 06 01 05 01 06 $$      
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())

@pytest.mark.skip("explicitly")
def test_power_grid_007():
    puzzle_string = f"""
    007.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    01 01 01 01 01 01 03 04 04 $$     
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_008():
    puzzle_string = f"""
    008.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    01 01 01 01 01 01 03 03 03 $$     
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_009():
    puzzle_string = f"""
    009.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 01
    02 01 01 01 01 01 02 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_010():
    puzzle_string = f"""
    010.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    01 01 01 01 01 01 03 05 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_011():
    puzzle_string = f"""
    011.power_grid
    9
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 05
    06 01 06 01 05 01 01 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_012():
    puzzle_string = f"""
    012.power_grid
    9
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    03 ?? 01 05 01 ?? 01 01 02 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_013():
    puzzle_string = f"""
    013.power_grid
    9
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    03 03 ?? 01 06 ?? 05 01 06 $$
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())

@pytest.mark.skip("help")
def test_power_grid_014():
    puzzle_string = f"""
    014.power_grid
    9
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    05 01 01 ?? 01 01 02 01 02 $$
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_015():
    puzzle_string = f"""
    015.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    ?? 01 01 01 03 03 03 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_016():
    puzzle_string = f"""
    016.power_grid
    9
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    01 01 02 01 02 01 ?? ?? 02 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_017():
    puzzle_string = f"""
    017.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 07
    10 10 10 10 10 10 10 10 10 01
    01 01 02 01 01 01 05 01 06 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_018():
    puzzle_string = f"""
    018.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01 
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    01 01 ?? 01 01 ?? 01 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_019():
    puzzle_string = f"""
    019.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    03 03 03 01 01 .. 01 01 01 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_020():
    puzzle_string = f"""
    020.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    01 01 01 01 03 05 01 01 01 ..
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_021():
    puzzle_string = f"""
    021.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 04
    02 01 01 01 01 .. .. 04 03 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_022():
    puzzle_string = f"""
    022.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    01 05 05 01 06 .. 05 01 06 ..
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_023():
    puzzle_string = f"""
    023.power_grid
    9
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    .. 01 01 .. 01 01 01 06 .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_024():
    puzzle_string = f"""
    024.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    .. 05 05 .. 07 01 .. 01 05 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_025():
    puzzle_string = f"""
    025.power_grid
    9
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 03
    .. 01 01 01 01 01 01 .. 01 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_026():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_027():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_028():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_29():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_030():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_031():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_032():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_033():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_034():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_035():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_036():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_037():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_038():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_039():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_040():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_041():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_042():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_043():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_044():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_045():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_046():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_047():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_048():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_049():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_050():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_051():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_052():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_053():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_054():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_055():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_056():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_057():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_058():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_059():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_060():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())

# def test_power_grid_094():
#     puzzle_string = f"""
#     018.power_grid
#     10
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     .. .. .. .. .. .. .. .. .. .. ..
#     """
#     assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())
