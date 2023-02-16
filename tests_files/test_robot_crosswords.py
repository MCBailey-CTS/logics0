from Loc import Loc
from Puzzle import Puzzle
from _defaults import default_test_puzzle
import pytest

from solving import Solving

class RobotCrosswords(Puzzle):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
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

    def __str__(self) -> str:
        string = f'///////////////////////////////////\n'
        string += f'{self.id()}\n'
        string += f'{self.__length}\n'
        for r in range(self.__length):
            for c in range(self.__length):
                string += f'{self.grid[r][c]} '
            string += '\n'
        string += f'///////////////////////////////////'
        return string

    def is_solved(self) -> bool:
        for house in self.houses():
            solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
            if len(solved_candidates) != len(house):
                return False
            if not RobotCrosswords.is_solved_candidate_house(solved_candidates):
                return False

        return True

    @staticmethod
    def is_solved_candidate_house(candidates: list[int]) -> bool:
        __sorted = sorted(candidates)
        return all(__sorted[i] + 1 == __sorted[i + 1] for i in range(len(candidates) - 1))

    def houses(self) -> list[list[Loc]]:
        houses = []
        for i in range(len(self)):
            for house in [self.house_row(i), self.house_col(i)]:
                actual_cells = set(
                    [loc for index, loc in enumerate(house) if 'x' not in self.grid[loc.row][loc.col]])
                house_chunks = []
                while len(actual_cells) > 0:
                    current = actual_cells.pop()
                    current_set = {current}
                    for other in list(actual_cells):
                        if any(other.is_next_to(loc) for loc in current_set):
                            actual_cells.remove(other)
                            current_set.add(other)
                    house_chunks.append(current_set)
                for house0 in house_chunks:
                    houses.append(list(house0))
        return houses


def test_robot_crosswords_002():
    puzzle_string = f"""
    002.robot_crosswords
    5
    x 6 7 x 6
    . . x 4 .
    6 x 4 3 x
    . . . x 9
    x 7 . 9 8
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


def test_robot_crosswords_003():
    puzzle_string = f"""
    003.robot_crosswords
    5
    9 8 . 7 x
    . x 7 . 6
    . 4 . x .
    7 . x 3 .
    x 5 2 . .
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_004():
    puzzle_string = f"""
    004.robot_crosswords
    5
    . 4 x 9 x
    4 x . . 7
    . 5 . x 6
    2 . . 4 x
    x 4 x 5 4
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


# @pytest.mark.skip("skipped")
def test_robot_crosswords_005():
    puzzle_string = f"""
    005.robot_crosswords
    5
    . x 1 . 2
    1 . . . x
    x . . x 9
    4 3 x 7 .
    3 . . 6 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


# @pytest.mark.skip("skipped")
def test_robot_crosswords_006():
    puzzle_string = f"""
    006.robot_crosswords
    6
    . 5 x . 3 1
    7 x 4 . x 2
    . . 3 x 2 x
    x 1 x . . .
    3 . 5 . x 1
    x . . . 4 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_007():
    puzzle_string = f"""
    007.robot_crosswords
    6
    2 . 5 . x 2
    x 6 x . 4 .
    . . . 2 x 4
    4 x . . 3 x
    . 2 . x . .
    2 x . 4 x 6
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_008():
    puzzle_string = f"""
    008.robot_crosswords
    6
    5 . 3 x 2 x
    x 5 x 1 . .
    1 . . . x 1
    x 2 1 . . x
    2 x 3 x 5 4
    1 . . 3 x 5
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_009():
    puzzle_string = f"""
    009.robot_crosswords
    6
    7 . x 2 3 x
    x . . x 2 .
    7 5 . . x 6
    4 x 2 . 4 .
    . 5 x . x .
    . x 6 . 7 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_010():
    puzzle_string = f"""
    010.robot_crosswords
    6
    9 x . . 8 x
    . 7 . 6 x 1
    x 6 x . 6 .
    4 . 6 x . 2
    5 x 5 . . .
    x . . 7 . x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_011():
    puzzle_string = f"""
    011.robot_crosswords
    6
    x 9 . 6 . x
    . x 6 x 6 7
    . . . . x 6
    9 x 5 6 4 x
    6 7 x . . .
    x . 5 x 2 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_012():
    puzzle_string = f"""
    012.robot_crosswords
    6
    x 2 . . x 8
    4 x 5 . . .
    . . x . . 7
    . . 7 x 8 x
    x 9 x 4 . 6
    8 . . . x 7
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_013():
    puzzle_string = f"""
    013.robot_crosswords
    6
    x . . 4 3 x
    . . 4 x . 4
    6 x . . . x
    x . . 4 x 2
    2 1 x 3 . 4
    3 x 4 . 1 .
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_014():
    puzzle_string = f"""
    014.robot_crosswords
    6
    5 x 9 . . .
    . 3 x 7 x 5
    4 x 4 5 . .
    3 . 5 x 1 x
    x 2 x . . .
    2 . 4 x 2 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_015():
    puzzle_string = f"""
    015.robot_crosswords
    6
    2 _ x _ 5 x
    x _ _ 2 x 9
    6 5 x _ _ _
    9 x _ 3 x _
    _ _ _ x 4 x
    7 x _ 6 _ 4
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_031():
    puzzle_string = f"""
    031.robot_crosswords
    7
    . 4 x 2 . 3 x
    4 x . . 5 x 2
    . . 5 . x 4 .
    . 4 . x 2 3 x
    x . 2 . . x 2
    8 . x 6 x 2 3
    9 x 2 . . 3 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_034():
    puzzle_string = f"""
    034.robot_crosswords
    7
    1 . . . x 1 x
    2 . 4 x . . 4
    x 4 x 2 . x 5
    6 . 4 x 2 . x
    5 x 5 4 x 1 .
    4 5 x . 3 . x
    x . 7 x . . .
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_035():
    puzzle_string = f"""
    035.robot_crosswords
    7
    x 2 x . 8 . 6
    5 . . . x 3 .
    . 4 . x 4 . 5
    . x . . . . x
    . 2 x 3 . x 3
    x . 5 x . . 2
    . . . 1 x 4 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_036():
    puzzle_string = f"""
    036.robot_crosswords
    7
    1 . x . 3 x 2
    x . 4 . x 4 .
    5 . x 4 5 6 x
    4 x . . x . 6
    x 4 . x . . .
    . x 2 . 4 x 5
    1 . . x 2 4 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_071():
    puzzle_string = f"""
    071.robot_crosswords
    8
    7 5 . . . x 6 .
    . . . x 1 . 4 .
    x 4 x 4 . . . .
    9 x 5 . x 5 x 4
    . 5 x . . . 3 .
    . . 4 . . x 2 x
    7 x . x . . . 3
    x 2 . 5 4 3 x 4
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_101():
    puzzle_string = f"""
    101.robot_crosswords
    9
    4 1 . . . x 1 . 2
    3 . 2 x . . . . .
    . . x 5 6 . . x .
    x . 7 . . . x 2 x
    1 . . 4 x 1 . . .
    2 x . . 1 . x 4 .
    x 4 . x 2 x 1 x 1
    3 . . . x . . 6 .
    2 . x 5 3 . . x 5
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_141():
    puzzle_string = f"""
    141.robot_crosswords
    10
    1 . 3 . . x . 5 . 3
    x 5 x 5 x 4 . x . x
    5 . . . . x 1 . . .
    x 4 . . . . x 2 x 5
    9 x 9 . x . . . 7 x
    . 6 . x 2 . x 5 . 7
    . . 8 . x . . 4 x .
    5 . x 6 . x 6 x . 5
    . . . x . 7 x 2 . x
    x . 7 . 8 x . . . 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_171():
    puzzle_string = f"""
    171.robot_crosswords
    11
    1 x 8 . . x 6 7 x 2 x
    . 3 x 7 . 9 x . . . 7
    . . 4 x 6 . . x . . x
    x . . 4 . x . . . x 9
    . . . x . . x 2 . . .
    5 6 . . x . 4 . x . 6
    . x . . 3 . x . 5 x .
    . 2 x 7 . . . 6 x 6 7
    3 . 4 x 6 x 6 x 9 . x
    x . x 2 . . . 1 x . 8
    4 . . . x 5 4 x 8 7 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_186():
    puzzle_string = f"""
    186.robot_crosswords
    12
    9 x 2 . 5 . x 4 2 . . .
    . 8 . . x . 4 . x 6 . .
    . x . . . . x . 3 . . x
    x 2 . . 3 x 8 x 2 x . .
    4 . x . x . . . x . 1 .
    x . . x 4 . x . . 3 x 1
    . 3 . . x . . 3 . x . .
    1 x 6 . . x 4 x 4 . . x
    x . . . 5 . x 2 x 7 . .
    1 . x 6 x 1 . . . x . .
    . x 3 . . . x 3 . . 7 .
    x 1 . x 2 . . 1 x 6 x 7
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())
