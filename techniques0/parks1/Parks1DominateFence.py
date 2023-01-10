from puzzles import Parks1


class Parks1DominateFence:
    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        for fence in puzzle.fences():
            fence_locs = puzzle.house_fence(fence)
            surrounding_cells = set()

            solved_empty = [loc for loc in fence_locs if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in fence_locs if
                           len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
            unsolved = list(set(fence_locs).difference(solved_tree + solved_empty))


            if len(solved_tree) == 1:
                continue



            for loc in unsolved:
                # from Techniques import Techs
                for surrounding in puzzle.surrounding( loc):
                    if fence == puzzle.cell_fence(surrounding):
                        continue
                    surrounding_cells.add(surrounding)
            for edge_cell in surrounding_cells:
                candidates = puzzle.cell_candidates(edge_cell)
                if len(candidates) == 1 and 1 in candidates:
                    continue
                fence_house = set(unsolved)
                while len(fence_house) > 0:
                    first = list(fence_house)[0]
                    if edge_cell.row == first.row or edge_cell.col == first.col:
                        fence_house.remove(first)
                        continue
                    # from Techniques import Techs
                    if first in puzzle.surrounding( edge_cell):
                        fence_house.remove(first)
                        continue
                    break
                if len(fence_house) == 0:
                    edits += puzzle.rem([edge_cell], [1])
        return edits





# class Parks1DominateFenceAgain:
#     def solve0(self, puzzle: Parks1) -> int:
#         edits = 0
#         for fence in puzzle.fences():
#             if fence != 'b':
#                 continue
#             house = puzzle.house_fence(fence)
#             print(house)
#
#             # surrounding_cells = set()
#             # for loc in house:
#             #     # from Techniques import Techs
#             #     for surrounding in puzzle.surrounding( loc):
#             #         if fence == puzzle.cell_fence(surrounding):
#             #             continue
#             #         surrounding_cells.add(surrounding)
#             # for edge_cell in surrounding_cells:
#             #     candidates = puzzle.cell_candidates(edge_cell)
#             #     if len(candidates) == 1 and 1 in candidates:
#             #         continue
#             #     fence_house = set(house)
#             #     while len(fence_house) > 0:
#             #         first = list(fence_house)[0]
#             #         if edge_cell.row == first.row or edge_cell.col == first.col:
#             #             fence_house.remove(first)
#             #             continue
#             #         # from Techniques import Techs
#             #         if first in puzzle.surrounding( edge_cell):
#             #             fence_house.remove(first)
#             #             continue
#             #         break
#             #     if len(fence_house) == 0:
#             #         edits += puzzle.rem([edge_cell], [1])
#         return edits
