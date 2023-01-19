from puzzles import Sumscrapers

class HiddenSingleSumscrapers:
    def solve0(self, puzzle: Sumscrapers) -> int:
        edits = 0
        houses = []
        for index in range(len(puzzle)):
            houses.append(puzzle.house_row(index))
            houses.append(puzzle.house_col(index))

        for house in houses:
            candidate_dict = {}
            for index in range(len(puzzle)):
                for candidate in puzzle.cell_candidates(house[index]):
                    if candidate not in candidate_dict:
                        candidate_dict[candidate] = []
                    candidate_dict[candidate].append(house[index])
            for candidate in candidate_dict.keys():
                locs = candidate_dict[candidate]

                if len(locs) == 1:
                    edits += puzzle.rem(candidate_dict[candidate],
                                        set(puzzle.expected_candidates()).difference([candidate]))

        return edits
