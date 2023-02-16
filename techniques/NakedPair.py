
from techniques.BaseSudokuHouseTechnique import BaseSudokuHouseTechnique
from Loc import Loc


class NakedPair(BaseSudokuHouseTechnique):
    @staticmethod
    def static_solve_house(puzzle, house: list[Loc]) -> int:
        edits = 0
        # print(f'{len(house)} {len(puzzle)}')
        # print(house)
        for i in range(0, len(puzzle) - 1):
            for ii in range(i + 1, len(puzzle)):
                if i == ii:
                    continue
                index_set = {i, ii}
                candidate_set = set()
                candidates0 = puzzle.cell_candidates(house[i])
                candidates1 = puzzle.cell_candidates(house[ii])
                if len(candidates0) == 1 or len(candidates1) == 1:
                    continue
                for c in candidates0:
                    candidate_set.add(c)
                for c in candidates1:
                    candidate_set.add(c)
                if len(candidate_set) != 2:
                    continue
                for j in range(len(puzzle)):
                    if j not in index_set:
                        edits += puzzle.rem([house[j]], list(candidate_set))
        return edits

    def solve_house(self, puzzle, house: list[Loc]) -> int:
        return NakedPair.static_solve_house(puzzle, house)





class NakedTriple(BaseSudokuHouseTechnique):

    def solve_house(self, puzzle, house: list[Loc]) -> int:
        edits = 0

        naked_count = 3

        for i in range(len(puzzle)):
            for ii in range(len(puzzle)):
                for iii in range(len(puzzle)):
                    indexes = {i, ii, iii}

                    if len(indexes) != naked_count:
                        continue

                    candidate_set = set()
                    for index in indexes:
                        for candidate in puzzle.cell_candidates(house[index]):
                            candidate_set.add(candidate)

                    _candidates0 = puzzle.cell_candidates(house[i])
                    _candidates1 = puzzle.cell_candidates(house[ii])
                    _candidates2 = puzzle.cell_candidates(house[iii])

                    if len(_candidates0) < 2 or len(_candidates0) > naked_count or \
                            len(_candidates1) < 2 or len(_candidates1) > naked_count or \
                            len(_candidates2) < 2 or len(_candidates2) > naked_count:
                        continue

                    if not candidate_set.issuperset(_candidates0) or \
                            not candidate_set.issuperset(_candidates1) or \
                            not candidate_set.issuperset(_candidates2):
                        continue

                    if len(candidate_set) != naked_count:
                        continue

                    for j in range(len(puzzle)):
                        if j not in indexes:
                            edits += puzzle.rem([house[j]], list(candidate_set))
        return edits
