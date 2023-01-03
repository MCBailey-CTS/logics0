
    class NakedTriple():
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            naked_count = 3
            for house in puzzle.houses_rows_cols_fences():
                for i in range(puzzle.length):
                    for ii in range(puzzle.length):
                        for iii in range(puzzle.length):
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

                            for j in range(puzzle.length):
                                if j not in indexes:
                                    edits += puzzle.rem(house[j], list(candidate_set))
            return edits

