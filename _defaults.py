EXPLICITLY = "explicitly"

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