# # from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# # from techniques.LockedCandidatesPointing import LockedCandidatesPointing
#
# EXPLICITLY = "EXPLICITLY"
#
#
# def all_file_leaves():
#     from os import walk
#     files = []
#     for filename in next(walk('C:\\Repos\\logics0\\files'), (None, None, []))[2]:  # [] if no file
#         if 'actual' in filename:
#             files.append(filename)
#     return files

#
# def the_data():
#     for _id in all_file_leaves():
#
#         if 'hidden_single' in _id:
#             yield [_id, HiddenSingle()]
#         elif 'almost_locked_candidates_claiming' in _id:
#             yield [_id, AlmostLockedCandidatesClaiming()]
#         elif 'hidden_pair' in _id:
#             yield [_id, tech.HiddenPair()]
#         elif 'hidden_triple' in _id:
#             yield [_id, tech.HiddenTriple()]
#         elif 'hidden_quad' in _id:
#             yield [_id, tech.HiddenQuad()]
#         elif 'naked_pair' in _id:
#             yield [_id, NakedPair()]
#         elif 'naked_triple' in _id:
#             yield [_id, tech.NakedTriple()]
#         elif 'naked_quad' in _id:
#             yield [_id, tech.NakedQuad()]
#         elif 'cross_hatch' in _id:
#             yield [_id, CrossHatch()]
#         elif 'avoidable_rectangle_type1' in _id:
#             yield [_id, AvoidableRectangleType1()]
#         elif 'avoidable_rectangle_type2' in _id:
#             yield [_id, AvoidableRectangleType2()]
#         elif 'hidden_unique_rectangle' in _id:
#             yield [_id, HiddenUniqueRectangle()]
#         elif 'unique_rectangle_type1' in _id:
#             yield [_id, UniqueRectangleType1()]
#         elif 'unique_rectangle_type2' in _id:
#             yield [_id, UniqueRectangleType2()]
#         elif 'unique_rectangle_type3' in _id:
#             yield [_id, UniqueRectangleType3()]
#         elif 'unique_rectangle_type4' in _id:
#             yield [_id, UniqueRectangleType4()]
#         elif 'locked_candidates_pointing' in _id:
#             yield [_id, LockedCandidatesPointing()]
#         elif 'locked_candidates_claiming' in _id:
#             yield [_id, LockedCandidatesClaiming()]
#         elif 'finned_jelly_fish' in _id:
#             yield [_id, tech.FinnedJellyFish()]
#         elif 'shashimi_jelly_fish' in _id:
#             yield [_id, tech.ShashimiJellyFish()]
#         elif 'jelly_fish' in _id:
#             yield [_id, tech.JellyFish()]
#         elif 'finned_sword_fish' in _id:
#             yield [_id, tech.FinnedSwordFish()]
#         elif 'shashimi_sword_fish' in _id:
#             yield [_id, tech.ShashimiSwordFish()]
#         elif 'sword_fish' in _id:
#             yield [_id, tech.SwordFish()]
#         elif 'finned_x_wing' in _id:
#             yield [_id, FinnedXWing()]
#         elif 'shashimi_x_wing' in _id:
#             yield [_id, ShashimiXWing()]
#         elif 'x_wing' in _id:
#             yield [_id, tech.XWing()]
#         elif 'x_chain' in _id:
#             yield [_id, tech.XChain()]
#         elif 'xy_chain' in _id:
#             yield [_id, tech.XyChain()]
#         elif 'xy_wing' in _id:
#             yield [_id, XyWing()]
#         elif 'wxyz_wing' in _id:
#             yield [_id, WxyzWing()]
#         elif 'xyz_wing' in _id:
#             yield [_id, tech.XyzWing()]
#         elif 'w_wing' in _id:
#             yield [_id, WWing()]
#         elif 'simple_coloring' in _id:
#             yield [_id, tech.SimpleColoring()]
#         elif 'sue_de_coq' in _id:
#             yield [_id, tech.SueDeCoq()]
#         elif 'fishy_cycle' in _id:
#             yield [_id, tech.FishyCycle()]
#         else:
#             yield [_id, None]

#
# def __test_file_puzzle(data) -> tuple[bool, str]:
#     actual_path, technique = data
#
#     if technique is None:
#         pytest.skip(actual_path)
#
#     actual_path = f'C:\\Repos\\logics0\\files\\{actual_path}'
#
#     expected_path = actual_path.replace('actual', 'expected')
#
#     actual = numpy.loadtxt(actual_path, dtype=str)
#     expected = numpy.loadtxt(expected_path, dtype=str)
#
#     actual_split = actual_path.split('\\')
#     expected_split = expected_path.split('\\')
#
#     actual_id = actual_split[-1]
#     expected_id = expected_split[-1]
#
#     length_actual = int(actual[0, 0])
#     actual = numpy.delete(actual, 0, 0)
#
#     length_expected = int(expected[0, 0])
#     expected = numpy.delete(expected, 0, 0)
#
#     if actual_id.endswith('.sudoku'):
#         constructor = Sudoku
#     elif actual_id.endswith('.kropki'):
#         constructor = Kropki
#     else:
#         return False, 'Could not determine puzzle type'
#
#     if constructor is None:
#         return False, "Constructor was None"
#
#     actual_puzzle = constructor(actual, length_actual, actual_id)
#     expected_puzzle = constructor(expected, length_expected, expected_id)
#
#     technique.solve0(actual_puzzle)
#
#     if actual_puzzle == expected_puzzle:
#         return True, ""
#
#     if actual_id.endswith('.sudoku'):
#         for r in range(len(actual_puzzle)):
#             for c in range(len(actual_puzzle)):
#                 loc = Loc(r, c)
#                 actual_candidates = actual_puzzle.cell_candidates(loc)
#                 expected_candidates = expected_puzzle.cell_candidates(loc)
#
#                 if set(actual_candidates) == set(expected_candidates):
#                     continue
#
#                 expected_puzzle.override_loc_color([loc], Fore.CYAN)
#
#     print(actual_puzzle.to_string())
#     print(expected_puzzle.to_string())
#
#     return False, "{actual_puzzle} dit not equal {expected_puzzle}"

#
# @pytest.mark.parametrize('data', the_data(), ids=[i[0] for i in the_data()])
# def test_file_puzzle(data):
#     result, message = __test_file_puzzle(data)
#
#     assert result, message

