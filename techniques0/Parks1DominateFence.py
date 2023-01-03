from _puzzles import Parks1



class Parks1DominateFence:
    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        for fence in puzzle.fences():
            # if fence != "b":
            #     continue
            house = puzzle.house_fence(fence)

            surrounding_cells = set()

            for loc in house:
                from Techniques import Techs

                for surrounding in Techs.MinesweeperSolver.surrounding(puzzle, loc):
                    if fence == puzzle.cell_fence(surrounding):
                        continue
                    surrounding_cells.add(surrounding)

            for edge_cell in surrounding_cells:

                candidates = puzzle.cell_candidates(edge_cell)

                if len(candidates) == 1 and 1 in candidates:
                    continue

                fence_house = set(house)

                while len(fence_house) > 0:
                    first = list(fence_house)[0]

                    if edge_cell.row == first.row or edge_cell.col == first.col:
                        fence_house.remove(first)
                        continue
                    from Techniques import Techs

                    if first in Techs.MinesweeperSolver.surrounding(puzzle, edge_cell):
                        fence_house.remove(first)
                        continue
                    break

                if len(fence_house) == 0:
                    edits += puzzle.rem([edge_cell], [1])

        return edits