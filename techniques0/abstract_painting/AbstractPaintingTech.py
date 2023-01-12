from Loc import Loc
from puzzles import AbstractPainting
from typing import Optional


class AbstractPaintingTech:
    def solve0(self, puzzle: AbstractPainting) -> int:
        edits = 0
        for index in range(puzzle.length):
            row_house = puzzle.house_row(index)
            row_scraper = puzzle.east_scraper(index)
            edits += self.solve1(puzzle, row_scraper, row_house)
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)
            edits += self.solve1(puzzle, col_scraper, col_house)
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                candidates = puzzle.cell_candidates(loc)
                if len(candidates) != 1:
                    continue
                fence = puzzle.cell_fence(loc)
                if 1 in candidates:
                    edits += puzzle.rem(puzzle.house_fence(fence), [0])
                if 0 in candidates:
                    edits += puzzle.rem(puzzle.house_fence(fence), [1])
        return edits

    def solve1(self, puzzle: AbstractPainting, scraper: Optional[int], house: list[Loc]) -> int:
        edits = 0
        solved_abstract = []
        solved_empty = []
        unsolved = []
        for index in range(len(house)):
            candidates = puzzle.cell_candidates(house[index])
            if len(candidates) > 1:
                unsolved.append(house[index])
                continue
            if 1 in candidates:
                solved_abstract.append(house[index])
            if 0 in candidates:
                solved_empty.append(house[index])
        # full house
        if scraper == len(house):
            edits += puzzle.rem(house, [0])
        if scraper == len(solved_abstract):
            edits += puzzle.rem(unsolved, [1])

        # hidden paint
        if len(unsolved) == scraper and len(solved_abstract) == 0:
            edits += puzzle.rem(unsolved, [0])
            

        # check fence length
        fence_dict = {}
        for loc in house:
            fence = puzzle.cell_fence(loc)
            if fence not in fence_dict:
                fence_dict[fence] = []
            fence_dict[fence].append(loc)

        for fence in fence_dict:
            if scraper is not None and len(fence_dict[fence]) > scraper:
                edits += puzzle.rem(puzzle.house_fence(fence), [1])




        return edits
