
EXPLICITLY = "explicitly"


def default_test_explicit_actual_expected(constructor, technique, actual, expected) -> bool:
    actual_puzzle = constructor(actual)
    expected_puzzle = constructor(expected)
    technique.solve0(actual_puzzle)
    actual_string = str(actual_puzzle).replace(actual_puzzle.id(), "")
    expected_string = str(expected_puzzle).replace(expected_puzzle.id(), "")
    if actual_string == expected_string:
        return True

    print(actual_string.replace('\n',''))
    print(expected_string.replace('\n',''))

    print(actual_puzzle.to_string())
    print(expected_puzzle)
    return False


def default_test_puzzle(puzzle_string, constructor, techniques) -> bool:
    puzzle = constructor(puzzle_string)
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
    print(puzzle.to_string())
    return False


# def default_test_puzzle0(puzzle_string, constructor, techniques) -> bool:
#     puzzle: Puzzle = constructor(puzzle_string)
#     edits = 0
#     edit_dict = {}
#     while True:
#         original_edits = edits
#         for tech in techniques:
#             _edits = tech.solve0(puzzle)
#             if tech.__class__.__name__ not in edit_dict:
#                 edit_dict[tech.__class__.__name__] = 0
#             edit_dict[tech.__class__.__name__] += _edits
#             edits = edits + _edits
#         if original_edits == edits:
#             break
#     if puzzle.is_solved():
#         return True
#     for tech in edit_dict:
#         if edit_dict[tech] == 0:
#             continue
#         print(f'{tech}: {edit_dict[tech]}')
#     print(f'Total edits: {edits}')
#     print(puzzle)
#     return False



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



# def test_sudoku_9x9_unique_rectangle_type1_south_west_row_chute():
#     if solve(9,
#              f"""
# _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
# _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
# _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#
# _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
# _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
# _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#
# _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
# _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
# _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#
#             """,
#              f"""
# _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
# _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
# _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
#
# _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
# _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
# _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
#
# _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
# _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
# _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
#
#             """, UniqueRectangleType1()):
#         return
#     assert False