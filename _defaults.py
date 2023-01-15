from puzzles import Puzzle

EXPLICITLY = "explicitly"


def default_test_explicit_actual_expected(constructor, technique, actual, expected) -> bool:
    # print(actual)
    # temp = next((name for name in dir()))


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
    puzzle: Puzzle = constructor(puzzle_string)
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
