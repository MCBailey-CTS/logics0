from puzzles import Sudoku


class ShashimiXWingPlus1:
    @staticmethod
    def solve0(puzzle: Sudoku) -> int:
        edits = 0
        for candidate in puzzle.expected_candidates():
            for i in range(puzzle.__length):
                for ii in range(puzzle.__length):
                    if i == ii:
                        continue

                    house0 = [loc for loc in puzzle.house_col(i) if
                              candidate in puzzle.cell_candidates(loc) and len(puzzle.cell_candidates(loc)) != 1]
                    house1 = [loc for loc in puzzle.house_col(ii) if
                              candidate in puzzle.cell_candidates(loc) and len(puzzle.cell_candidates(loc)) != 1]

                    if len(house0) != 2 or len(house0) != 2:
                        continue

                    loc_set = set(house0 + house1)

                    fence_dict = puzzle.fence_dict(loc_set)

                    if len(fence_dict) != 4:
                        continue

                    if not all([len(fence_dict[fence]) == 1 for fence in fence_dict]):
                        continue

                    rows = set([loc.row for loc in loc_set])
                    cols = set([loc.col for loc in loc_set])

                    if len(cols) == 2 and len(rows) == 3:
                        row_dict = {}

                        for loc in loc_set:
                            if loc.row not in row_dict:
                                row_dict[loc.row] = []
                            row_dict[loc.row].append(loc)

                        # print(row_dict)

                        if len(row_dict) == 3:
                            shashimi_set = set(loc_set)
                            for r in row_dict:
                                if len(row_dict[r]) == 2:
                                    for loc in row_dict[r]:
                                        shashimi_set.remove(loc)

                            pincer0, pincer1 = shashimi_set

                            fence0 = puzzle.cell_fence(pincer0)
                            fence1 = puzzle.cell_fence(pincer1)

                            fence0_locs = set(puzzle.house_fence(fence0))
                            fence1_locs = set(puzzle.house_fence(fence1))
                            row0_locs = set(puzzle.house_row(pincer0.row))
                            row1_locs = set(puzzle.house_row(pincer1.row))

                            pincer0_intersection = fence1_locs.intersection(row0_locs)
                            pincer1_intersection = fence0_locs.intersection(row1_locs)

                            for loc in list(pincer0_intersection) + list(pincer1_intersection):
                                if loc == pincer0 or loc == pincer1:
                                    continue
                                edits += puzzle.rem(loc, [candidate])

        return edits


