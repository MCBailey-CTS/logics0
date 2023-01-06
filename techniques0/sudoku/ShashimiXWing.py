from Loc import Loc
from puzzles import Sudoku


class ShashimiXWing:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        candidate = 1

        row0 = 2
        row1 = 6

        row_house0 = puzzle.house_row(row0, candidate)
        row_house1 = puzzle.house_row(row1, candidate)

        all_locs = set(row_house0 + row_house1)

        row_dict = {}
        col_dict = {}
        fence_dict = {}

        for loc in all_locs:
            if loc.row not in row_dict:
                row_dict[loc.row] = []
            row_dict[loc.row].append(loc)

            if loc.col not in col_dict:
                col_dict[loc.col] = []
            col_dict[loc.col].append(loc)

            fence = puzzle.cell_fence(loc)
            if fence not in fence_dict:
                fence_dict[fence] = []
            fence_dict[fence].append(loc)

        if len(fence_dict) != 4:
            return 0

        if len(row_dict) == 2 and len(col_dict) == 3:
            return self.solve_length_4(puzzle, )

        if len(row_dict) == 2 and 1 < len(col_dict) < 5:
            col_chute_dict = {}

            for loc in all_locs:
                col_chute = puzzle.col_chute(loc)
                if col_chute not in col_chute_dict:
                    col_chute_dict[col_chute] = []
                col_chute_dict[col_chute].append(loc)

            if len(col_chute_dict) == 2 and len(all_locs) == 4:
                print("made it here")

            if len(col_chute_dict) == 2:
                # need to find the col_chute that has a length more than 2
                greater_than_2 = list(filter(lambda key: len(col_chute_dict[key]) > 2, col_chute_dict.keys()))

                if len(greater_than_2) == 1:
                    locs_in_col_chute = col_chute_dict[greater_than_2[0]]
                    sorted_fence_dict = {}

                    for loc in locs_in_col_chute:
                        fence0 = puzzle.cell_fence(loc)
                        if fence0 not in sorted_fence_dict:
                            sorted_fence_dict[fence0] = []
                        sorted_fence_dict[fence0].append(loc)

                    if len(sorted_fence_dict) == 2:
                        fence0, fence1 = sorted_fence_dict.keys()
                        if len(sorted_fence_dict[fence0]) == 1 and len(sorted_fence_dict[fence1]) > 1:
                            fence_house = puzzle.house_fence(fence1)
                            col_house = puzzle.house_col(sorted_fence_dict[fence0][0].col)
                            locs_to_remove = set(fence_house).intersection(col_house).difference(all_locs)
                            print(locs_to_remove)
                            edits += puzzle.rem(list(locs_to_remove), [candidate])

                        if len(sorted_fence_dict[fence0]) == 1 and len(sorted_fence_dict[fence1]) == 1:
                            print("made it here")
                            # fence_house = puzzle.house_fence(fence1)
                            # col_house = puzzle.house_col(sorted_fence_dict[fence0][0].col)
                            # locs_to_remove = set(fence_house).intersection(col_house).difference(all_locs)
                            # print(locs_to_remove)
                            # edits += puzzle.rem(list(locs_to_remove), [candidate])

        return edits
