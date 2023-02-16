from techniques.AbstractPaintingScraperAndHouse import AbstractPaintingScraperAndHouse
from typing import Optional
from Loc import Loc
class AbstractPaintingTech(AbstractPaintingScraperAndHouse):
    def solve1(self, puzzle, scraper: Optional[int], house: list[Loc]) -> int:
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
