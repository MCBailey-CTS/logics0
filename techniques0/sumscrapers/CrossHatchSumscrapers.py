from _puzzles import Sumscrapers


class CrossHatchSumscrapers:
    def solve0(self, puzzle: Sumscrapers) -> int:
        edits = 0
        houses = []
        for index in range(puzzle.length):
            houses.append(puzzle.house_row(index))
            houses.append(puzzle.house_col(index))
        for house in houses:
            for index0 in range(len(house)):
                for index1 in range(len(house)):
                    if index0 == index1:
                        continue
                    loc0 = house[index0]
                    loc1 = house[index1]
                    candidates0 = puzzle.cell_candidates(loc0)
                    if len(candidates0) == 1:
                        edits += puzzle.rem([loc1], [candidates0[0]])
        return edits
