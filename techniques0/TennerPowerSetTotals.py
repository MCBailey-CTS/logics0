from _puzzles import Tenner


class TennerPowerSetTotals:
    def solve0(self, puzzle: Tenner) -> int:
        edits = 0
        edits = self.solve3(puzzle)
        edits += self.solve4(puzzle)
        edits += self.solve5(puzzle)
        edits += self.solve6(puzzle)
        return edits

    # class TennerPowerSetTotals3:
    def solve3(self, puzzle: Tenner) -> int:
        edits = 0
        TOTAL = 3
        if puzzle.length != TOTAL:
            return edits
        for col in range(puzzle.col_length):
            house = puzzle.house_col_cell_locs(col)
            total = puzzle.total(col)
            if total is None:
                continue
            valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
            for candidate0 in puzzle.cell_candidates(house[0]):
                for candidate1 in puzzle.cell_candidates(house[1]):
                    for candidate2 in puzzle.cell_candidates(house[2]):
                        candidates = [candidate0, candidate1, candidate2]
                        self.mid(puzzle, valid_candidates_dict, candidates, house, total)
            edits += self.end(puzzle, valid_candidates_dict, house)
        return edits

    def solve4(self, puzzle: Tenner) -> int:
        edits = 0
        TOTAL = 4
        if puzzle.length != TOTAL:
            return edits
        for col in range(puzzle.col_length):
            house = puzzle.house_col_cell_locs(col)
            total = puzzle.total(col)
            if total is None:
                continue
            valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
            for candidate0 in puzzle.cell_candidates(house[0]):
                for candidate1 in puzzle.cell_candidates(house[1]):
                    for candidate2 in puzzle.cell_candidates(house[2]):
                        for candidate3 in puzzle.cell_candidates(house[3]):
                            candidates = [candidate0, candidate1, candidate2, candidate3]
                            self.mid(puzzle, valid_candidates_dict, candidates, house, total)
            edits += self.end(puzzle, valid_candidates_dict, house)
        return edits

    # class TennerPowerSetTotals5:
    def solve5(self, puzzle: Tenner) -> int:
        edits = 0
        TOTAL = 5
        if puzzle.length != TOTAL:
            return edits
        for col in range(puzzle.col_length):
            house = puzzle.house_col_cell_locs(col)
            total = puzzle.total(col)
            if total is None:
                continue
            valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
            for candidate0 in puzzle.cell_candidates(house[0]):
                for candidate1 in puzzle.cell_candidates(house[1]):
                    for candidate2 in puzzle.cell_candidates(house[2]):
                        for candidate3 in puzzle.cell_candidates(house[3]):
                            for candidate4 in puzzle.cell_candidates(house[4]):
                                candidates = [candidate0, candidate1, candidate2, candidate3, candidate4]
                                self.mid(puzzle, valid_candidates_dict, candidates, house, total)
            edits += self.end(puzzle, valid_candidates_dict, house)
        return edits

    # class TennerPowerSetTotals6:
    def solve6(self, puzzle: Tenner) -> int:
        edits = 0
        TOTAL = 6
        if puzzle.length != TOTAL:
            return edits
        for col in range(puzzle.col_length):
            house = puzzle.house_col_cell_locs(col)
            total = puzzle.total(col)
            if total is None:
                continue
            valid_candidates_dict = {house[i]: set() for i in range(puzzle.length)}
            for candidate0 in puzzle.cell_candidates(house[0]):
                for candidate1 in puzzle.cell_candidates(house[1]):
                    for candidate2 in puzzle.cell_candidates(house[2]):
                        for candidate3 in puzzle.cell_candidates(house[3]):
                            for candidate4 in puzzle.cell_candidates(house[4]):
                                for candidate5 in puzzle.cell_candidates(house[5]):
                                    candidates = [candidate0, candidate1, candidate2, candidate3, candidate4,
                                                  candidate5]
                                    self.mid(puzzle, valid_candidates_dict, candidates, house, total)
            edits += self.end(puzzle, valid_candidates_dict, house)

        return edits

    def mid(self, puzzle, valid_candidates_dict, candidates, house, total):
        if sum(candidates) != total:
            return
        is_valid_column = [candidates[index] != candidates[index + 1] for index in
                           range(puzzle.length - 1)]
        if not all(is_valid_column):
            return
        for index in range(puzzle.length):
            valid_candidates_dict[house[index]].add(candidates[index])

    def end(self, puzzle: Tenner, valid_candidates_dict, house) -> int:
        edits = 0
        for index in range(puzzle.length):
            edits += puzzle.rem([house[index]],
                                list(set(puzzle.expected_candidates()).difference(
                                    valid_candidates_dict[house[index]])))
        return edits
