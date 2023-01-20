import pytest
import numpy
from Loc import Loc
from colorama import Fore

def all_file_leaves():
    from os import walk
    files = []
    for filename in next(walk('C:\\Users\\mcbailey\\Desktop\\files'), (None, None, []))[2]:  # [] if no file
        if 'actual' in filename:
            files.append(filename)
    return files


def the_data():
    for _id in all_file_leaves():
        yield _id



def __test_file_puzzle(data) -> tuple[bool, str]:
    actual_path, technique = data

    if technique is None:
        pytest.skip(actual_path)

    actual_path = f'C:\\Repos\\logics0\\files\\{actual_path}'

    expected_path = actual_path.replace('actual', 'expected')

    actual = numpy.loadtxt(actual_path, dtype=str)
    expected = numpy.loadtxt(expected_path, dtype=str)

    actual_split = actual_path.split('\\')
    expected_split = expected_path.split('\\')

    actual_id = actual_split[-1]
    expected_id = expected_split[-1]

    length_actual = int(actual[0, 0])
    actual = numpy.delete(actual, 0, 0)

    length_expected = int(expected[0, 0])
    expected = numpy.delete(expected, 0, 0)

    if actual_id.endswith('.sudoku'):
        constructor = Sudoku
    elif actual_id.endswith('.kropki'):
        constructor = Kropki
    else:
        return False, 'Could not determine puzzle type'

    if constructor is None:
        return False, "Constructor was None"

    actual_puzzle = constructor(actual, length_actual, actual_id)
    expected_puzzle = constructor(expected, length_expected, expected_id)

    technique.solve0(actual_puzzle)

    if actual_puzzle == expected_puzzle:
        return True, ""

    if actual_id.endswith('.sudoku'):
        for r in range(len(actual_puzzle)):
            for c in range(len(actual_puzzle)):
                loc = Loc(r, c)
                actual_candidates = actual_puzzle.cell_candidates(loc)
                expected_candidates = expected_puzzle.cell_candidates(loc)

                if set(actual_candidates) == set(expected_candidates):
                    continue

                expected_puzzle.override_loc_color([loc], Fore.CYAN)

    print(actual_puzzle.to_string())
    print(expected_puzzle.to_string())

    return False, "{actual_puzzle} dit not equal {expected_puzzle}"


@pytest.mark.parametrize('data', [
    'C:\\Users\\mcbailey\\Desktop\\files\\naked_pair_row.sudoku.sudoku'
])
def test_file_puzzle1(data):
    # result, message = __test_file_puzzle(data)
    #
    # assert result, message
    f = open(data, 'r')
    string = f.read()
    print(string)

    assert False
