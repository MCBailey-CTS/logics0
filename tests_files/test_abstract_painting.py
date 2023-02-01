import pytest

from _defaults import default_test_puzzle
from puzzles import AbstractPainting
from solving import Solving


def test_abstract_painting_001():
    puzzle_string = f"""
    001.abstractpainting
    4
    10a 10b 10b 10b 03
    10a 10a 10b 10b 02
    10c 10c 10c 10c 04
    10d 10d 10c 10c 02
    01   02   04   04   $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_002():
    puzzle_string = f"""
    002.abstractpainting
    4
    10a 10a 10e 10e 02
    10b 10a 10e 10e 03
    10b 10b 10b 10d 04
    10b 10c 10c 10d 02
    03 01 03 04 $$
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_003():
    puzzle_string = f"""
    003.abstractpainting
    4
    10a 10a 10a 10b 3
    10a 10a 10a 10b 3
    10c 10c 10d 10d 2
    10c 10c 10d 10d 2
    2 2 4 2        $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_004():
    puzzle_string = f"""
    004.abstractpainting
    4
    10a 10a 10c 10c 2
    10a 10a 10c 10c 2
    10b 10a 10c 10d ?
    10b 10b 10b 10d 3
    2 1 4 2 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_005():
    puzzle_string = f"""
    005.abstractpainting
    4
    10a 10c 10d 10d 3
    10a 10c 10d 10d 3
    10a 10d 10d 10e ?
    10b 10b 10e 10e 2
    1 4 3 2 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_006():
    puzzle_string = f"""
    006.abstractpainting
    4
    10a 10a 10d 10d 4
    10a 10a 10d 10d 4
    10b 10a 10d 10e 3
    10b 10c 10c 10e 1
    4 ? 3 2 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_007():
    puzzle_string = f"""
    007.abstractpainting
    4
    10a 10a 10e 10e 2
    10a 10a 10d 10e 3
    10b 10b 10d 10d 2
    10c 10c 10d 10d 4
    3 ? 3 2             $$
        
        
        
        
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_008():
    puzzle_string = f"""
    008.abstractpainting
    4
    10a 10a 10a 10e 4
    10a 10a 10a 10e 4
    10b 10b 10b 10e 1
    10c 10c 10d 10d ?
    3 3 2 3          $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_009():
    puzzle_string = f"""
    009.abstractpainting
    4
    10a 10e 10e 10e 1
    10a 10d 10d 10d 4
    10a 10a 10c 10c 4
    10b 10b 10c 10c ?
    3 2 3 3
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_018():
    puzzle_string = f"""
    018.abstractpainting
    5
    10a 10a 10e 10f 10f 4
    10a 10a 10e 10f 10f 4
    10b 10b 10b 10f 10f 2
    10b 10b 10d 10d 10d ?
    10c 10c 10d 10d 10d 3
    2 2 2 5 5 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_019():
    puzzle_string = f"""
    019.abstractpainting
    5
    10a 10a 10a 10a 10a 5
    10b 10b 10b 10f 10f 2
    10c 10c 10b 10f 10f ?
    10d 10e 10e 10f 10g 4
    10d 10d 10e 10g 10g 3
    1 2 3 5 5 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_025():
    puzzle_string = f"""
    025.abstractpainting
    5
    10a 10a 10f 10f 10f 2
    10b 10a 10d 10f 10f ?
    10b 10a 10d 10d 10d 5
    10b 10b 10c 10d 10e 3
    10b 10c 10c 10e 10e 1
    5 4 ? 2 1 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_027():
    puzzle_string = f"""
    027.abstractpainting
    5
    10a 10a 10d 10d 10d 3
    10a 10b 10d 10d 10d 4
    10b 10b 10c 10e 10e 4
    10b 10c 10c 10e 10f ?
    10b 10c 10c 10e 10f ?
    3 2 2 5 3 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_028():
    puzzle_string = f"""
    028.abstractpainting
    5
    10a 10a 10a 10e 10f 4
    10a 10b 10b 10e 10f ?
    10b 10b 10c 10e 10e 3
    10b 10c 10c 10e 10e 4
    10b 10c 10d 10d 10d 4
    2 3 4 5 ? $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_029():
    puzzle_string = f"""
    029.abstractpainting
    5
    10a 10a 10a 10a 10c 4
    10b 10b 10a 10a 10c 2
    10d 10f 10f 10f 10g 1
    10d 10d 10f 10f 10g ?
    10d 10e 10e 10e 10e 5
    ? 3 3 3 1 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_030():
    puzzle_string = f"""
    030.abstractpainting
    5
    10a 10a 10a 10f 10f ?
    10a 10a 10f 10f 10f 5
    10a 10c 10d 10d 10e 2
    10b 10c 10d 10d 10e 1
    10b 10b 10b 10d 10e 1
    3 2 ? 2 5 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_031():
    puzzle_string = f"""
    031.abstractpainting
    6
    10a 10a 10b 10d 10d 10d 4
    10b 10b 10b 10e 10e 10k 3
    10c 10b 10i 10j 10j 10k ?
    10c 10b 10i 10j 10j 10k ?
    10f 10f 10f 10f 10h 10h 4
    10f 10f 10g 10g 10h 10h ?
    3 5 3 4 3 1     $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_010():
    puzzle_string = f"""
    010.abstractpainting
    4
    10a 10a 10c 10c 2
    10b 10a 10a 10e 3
    10b 10b 10e 10e 2
    10d 10d 10e 10e 2
    ? 2 3 3 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_011():
    puzzle_string = f"""
    011.abstractpainting
    5
    10a 10a 10g 10g 10g 5
    10b 10b 10g 10h 10h 1
    10b 10b 10b 10e 10e 2
    10c 10d 10e 10e 10f 4
    10c 10d 10e 10e 10f 4
    1 3 4 4 ? $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_012():
    puzzle_string = f"""
    012.abstractpainting
    5
    10a 10a 10a 10g 10g 5
    10a 10a 10a 10g 10g 5
    10b 10b 10e 10e 10g 1
    10c 10c 10d 10e 10f 2
    10c 10c 10d 10e 10f 2
    4 4 2 2  ? $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_013():
    puzzle_string = f"""
    013.abstractpainting
    5
    10a 10c 10c 10c 10d 4
    10a 10a 10a 10c 10d 4
    10a 10a 10f 10f 10f 5
    10b 10b 10e 10e 10f 1
    10b 10b 10b 10e 10f ?
    3 3 3 3 3          $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_014():
    puzzle_string = f"""
    014.abstractpainting
    5
    10a 10a 10a 10g 10g 5
    10b 10a 10a 10g 10g 5
    10b 10e 10e 10f 10f 3
    10b 10b 10c 10d 10d 2
    10b 10b 10c 10c 10c 2
    5 4 ? 3 3 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_015():
    puzzle_string = f"""
    015.abstractpainting
    5
    10a 10e 10e 10g 10g 2
    10a 10e 10e 10e 10f 3
    10a 10e 10f 10f 10f 1
    10a 10b 10b 10d 10d 4
    10b 10b 10c 10c 10d 3
    1 ? 3 2 2 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_016():
    puzzle_string = f"""
    016.abstractpainting
    5
    10a 10a 10e 10e 10f 2
    10a 10a 10e 10e 10f ?
    10a 10b 10c 10c 10f 2
    10b 10b 10c 10c 10d 3
    10b 10b 10d 10d 10d 5
    5 5 1 1 2 $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_017():
    puzzle_string = f"""
    017.abstractpainting
    5
    10a 10a 10e 10e 10e 2
    10a 10a 10a 10e 10e ?
    10a 10b 10d 10d 10d 5
    10b 10b 10c 10c 10d 3
    10b 10b 10c 10c 10d 3
    5 5 2 1 3    $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_035():
    puzzle_string = f"""
    035.abstractpainting
    6
    10a 10a 10b 10b 10c 10c 4
    10a 10a 10b 10b 10h 10h 2
    10a 10d 10d 10h 10h 10i 4
    10a 10d 10d 10h 10i 10i 5
    10e 10e 10f 10g 10i 10i 3
    10e 10f 10f 10g 10g 10g 3
    4 4 ? ? 4 ?     $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


def test_abstract_painting_036():
    puzzle_string = f"""
    036.abstractpainting
    6
    10a 10a 10b 10b 10c 10c ?
    10a 10b 10b 10b 10c 10c 5
    10d 10e 10f 10g 10g 10g 1
    10d 10e 10f 10f 10g 10h ?
    10d 10e 10f 10h 10g 10h 3
    10e 10e 10e 10h 10h 10h 6
    1 5 3 4 3 ?     $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_051():
    puzzle_string = f"""
    051.abstractpainting
    7
    10a 10a 10a 10a 10f 10g 10g 6
    10a 10a 10f 10f 10f 10g 10g 4
    10b 10d 10d 10e 10f 10g 10h 3
    10b 10b 10d 10e 10h 10h 10h 5
    10b 10e 10e 10e 10i 10j 10j 2
    10b 10c 10c 10i 10i 10j 10j ?
    10c 10c 10i 10i 10i 10j 10j 3
    ? 3 ? 3 ? 4 ?      $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_101():
    puzzle_string = f"""
    101.abstractpainting
    8
    10a 10b 10h 10h 10h 10h 10l 10l 4
    10a 10b 10h 10h 10h 10l 10l 10l ?
    10b 10b 10g 10g 10i 10l 10m 10n 1
    10b 10b 10b 10i 10i 10l 10m 10n ?
    10c 10c 10c 10i 10j 10j 10k 10k 5
    10d 10c 10i 10i 10j 10k 10k 10k ?
    10d 10c 10f 10f 10f 10k 10j 10j 7
    10d 10e 10e 10e 10j 10j 10j 10j ?
    4 ? ? 4 ? 3 2 ?       $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_151():
    puzzle_string = f"""
    151.abstractpainting
    9
    10a 10l 10l 10n 10o 10o 10p 10p 10t 5
    10a 10a 10m 10n 10p 10p 10p 10p 10t ?
    10a 10a 10m 10m 10q 10q 10r 10r 10t ?
    10b 10b 10f 10f 10q 10q 10r 10r 10s 4
    10b 10c 10c 10f 10f 10f 10i 10r 10s 6
    10b 10c 10c 10e 10e 10h 10i 10k 10k 3
    10b 10c 10e 10e 10g 10h 10i 10j 10j 4
    10b 10c 10d 10d 10g 10h 10i 10i 10j ?
    10d 10d 10d 10d 10h 10h 10i 10j 10j ?
    ? 7 5 4 ? 7 ? ? ?       $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_abstract_painting_191():
    puzzle_string = f"""
    191.abstractpainting
    10
    10a 10i 10i 10i 10i 10p 10s 10s 10s 10s ?
    10a 10i 10i 10j 10j 10p 10r 10r 10r 10r 6
    10b 10b 10k 10k 10m 10p 10p 10p 10r 10r ?
    10b 10b 10k 10l 10m 10m 10p 10p 10q 10q ?
    10c 10b 10l 10l 10m 10m 10m 10m 10q 10q 9
    10c 10b 10l 10l 10n 10n 10n 10o 10o 10q ?
    10d 10e 10l 10l 10n 10n 10o 10o 10o 10o ?
    10d 10e 10e 10e 10f 10g 10g 10g 10h 10h ?
    10d 10d 10e 10f 10f 10f 10g 10g 10h 10h 4
    10d 10d 10e 10f 10f 10f 10g 10g 10h 10h ?
    6 4 ? 5 ? 5 ? ? 4 ?         $
    """
    assert default_test_puzzle(puzzle_string, AbstractPainting, Solving.abstractpainting_techniques())
