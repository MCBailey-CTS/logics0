from Loc import Loc
from _puzzles import Parks1


class Parks1CrossHatch:

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        houses = []
        fence_dict = {}
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                fence = puzzle.cell_fence(loc)

                if fence not in fence_dict:
                    fence_dict[fence] = []

                fence_dict[fence].append(loc)

        for fence in fence_dict.keys():
            houses.append(fence_dict[fence])

        for row in range(puzzle.length):
            house = []
            for col in range(puzzle.length):
                house.append(Loc(row, col))
            houses.append(house)
        for col in range(puzzle.length):
            house = []
            for row in range(puzzle.length):
                house.append(Loc(row, col))
            houses.append(house)
        for house in houses:
            for i in range(len(house)):
                for ii in range(len(house)):
                    if i == ii:
                        continue
                    candidates0 = puzzle.cell_candidates(house[i])
                    if len(candidates0) == 1 and candidates0[0] == 1:
                        edits += puzzle.rem([house[ii]], [1])
        return edits